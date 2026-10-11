#!/usr/bin/env python3
"""Reconstruct the dodecahedral matching-complex discrete-Morse certificate.
Standard-library only. All graph data are generated from the given presentation.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache


def edges_gp_10_2():
    outer = {tuple(sorted((i, (i+1)%10))) for i in range(10)}
    spokes = {(i, 10+i) for i in range(10)}
    inner = {tuple(sorted((10+i, 10+(i+2)%10))) for i in range(10)}
    out = sorted(outer | spokes | inner)
    assert len(out)==30 and len(set(out))==30
    assert all(0<=u<v<20 for u,v in out)
    assert all(sum(u in e for e in out)==3 for u in range(20))
    return out


def all_matching_faces(edges):
    conflicts=[]
    for u,v in edges:
        conflicts.append(sum((1<<j) for j,(x,y) in enumerate(edges)
                             if u==x or u==y or v==x or v==y))
    faces=[0]
    for i in range(len(edges)):
        bit=1<<i
        faces.extend([s|bit for s in faces if not (s & conflicts[i])])
    assert len(faces)==len(set(faces))
    return faces


def boundary(simplex):
    """Facets and signed incidences, edge vertices ordered by list index."""
    v=simplex;order=0
    while v:
        bit=v & -v
        yield simplex ^ bit, (-1 if order&1 else 1)
        v^=bit;order+=1


def build_matching(faces):
    rem=set(faces); up={};down={}
    for i in range(30):
        bit=1<<i
        for s in list(rem):
            if not s&bit and (s|bit) in rem:
                up[s]=s|bit;down[s|bit]=s
                rem.remove(s);rem.remove(s|bit)
    assert set(up).isdisjoint(down)
    assert len(up)==len(down)
    assert (2*len(up)+len(rem))==len(faces)
    return rem,up,down


def singleton_gradient_path(high, rem,up,down):
    """Unique *unsigned* V-paths from high to each critical lower cell."""
    @lru_cache(maxsize=None)
    def paths(low):
        if low in down:
            return {}
        if low in rem:
            return {low:(1,(low,))}
        assert low in up
        accum={}
        for new_low,_ in boundary(up[low]):
            if new_low==low:continue
            for end,(count,path) in paths(new_low).items():
                before=accum.get(end)
                if before is None:accum[end]=(count,(low,)+path)
                else:accum[end]=(min(2,before[0]+count),())
        return accum
    accum={}
    for start,_ in boundary(high):
        for end,(count,path) in paths(start).items():
            before=accum.get(end)
            if before is None:accum[end]=(count,path)
            else:accum[end]=(min(2,before[0]+count),())
    return {end:path for end,(count,path) in accum.items() if count==1}


def cancellation(rem,up,down,high,low,path):
    assert high in rem and low in rem and path[-1]==low
    tops=[high]+[up[s] for s in path[:-1]]
    assert len(tops)==len(path)
    for s,t in zip(path,tops):
        up[s]=t;down[t]=s
    rem.remove(high);rem.remove(low)
    assert len(up)==len(down)


def optimize(rem,up,down):
    log=[]
    for high_size in (8,7):
        while sum(s.bit_count()==high_size for s in rem) > (0 if high_size==8 else 117):
            choices=[]
            for high in sorted(s for s in rem if s.bit_count()==high_size):
                for low,path in singleton_gradient_path(high,rem,up,down).items():
                    choices.append((len(path),high,low,path))
            assert choices, ('No unique cancellation path',high_size,Counter(s.bit_count() for s in rem))
            _,high,low,path=min(choices)
            log.append((high_size,high,low,len(path),len(choices)))
            cancellation(rem,up,down,high,low,path)
    assert len(log)==10
    assert Counter(s.bit_count()-1 for s in rem)=={5:5,6:117}
    return log


def acyclicity(faces,up,omit_empty=True):
    face_to_index={f:i for i,f in enumerate(faces) if (f or not omit_empty)}
    incidences=0
    degree=[0]*len(faces)
    graph=[[] for _ in faces]
    for s in faces:
        if omit_empty and s==0:continue
        for i in range(30):
            bit=1<<i
            if s&bit:continue
            larger=s|bit
            if larger not in face_to_index:continue
            incidences+=1
            a,b=face_to_index[s],face_to_index[larger]
            if up.get(s)==larger:a,b=b,a
            graph[a].append(b);degree[b]+=1
    q=deque(i for i,d in enumerate(degree) if d==0 and (faces[i]!=0 or not omit_empty))
    seen=0
    while q:
        s=q.popleft();seen+=1
        for t in graph[s]:
            degree[t]-=1
            if degree[t]==0:q.append(t)
    assert seen==len(face_to_index),(seen,len(face_to_index))
    return seen,incidences


def morse_degree_matrix(rem,up,down):
    crit5=sorted(s for s in rem if s.bit_count()==6)
    crit6=sorted(s for s in rem if s.bit_count()==7)
    low_ids={s:i for i,s in enumerate(crit5)}
    @lru_cache(maxsize=None)
    def projection(face):
        if face in down:return ()
        if face in rem:return ((low_ids[face],1),)
        assert face in up
        high=up[face]
        facets=list(boundary(high))
        sign_pivot=next(sign for s,sign in facets if s==face)
        acc=defaultdict(int)
        for s,sign in facets:
            if s==face:continue
            for r,c in projection(s):acc[r]-=sign_pivot*sign*c
        return tuple((i,v) for i,v in sorted(acc.items()) if v)
    matrix=[[0 for _ in crit6] for _ in crit5]
    for j,c in enumerate(crit6):
        for face,sign in boundary(c):
            for row,v in projection(face):matrix[row][j]+=sign*v
    assert not any(v for row in matrix for v in row)
    return len(crit5),len(crit6),projection.cache_info()


def main():
    edges=edges_gp_10_2()
    faces=all_matching_faces(edges)
    hist=Counter(s.bit_count() for s in faces)
    assert dict(sorted(hist.items()))=={0:1,1:30,2:375,3:2540,4:10155,5:24474,6:34805,7:27300,8:10260,9:1400,10:36}
    rem,up,down=build_matching(faces)
    assert Counter(s.bit_count()-1 for s in rem)=={5:10,6:127,7:5}
    cancellation_log=optimize(rem,up,down)
    assert up.get(0) is not None
    singleton=up.pop(0)
    assert singleton.bit_count()==1 and down.pop(singleton)==0
    rem.add(singleton)
    assert Counter(s.bit_count()-1 for s in rem)=={0:1,5:5,6:117}
    assert 2*len(up)+len(rem)==len(faces)-1
    assert all((s & h)==s and h.bit_count()==s.bit_count()+1 and down.get(h)==s for s,h in up.items())
    assert len(set(up.values()))==len(up)
    seen,incidences=acyclicity(faces,up,True)
    shape= morse_degree_matrix(rem,up,down)
    assert shape[0:2]==(5,117)
    euler=sum(((-1)**(j-1)*v for j,v in hist.items() if j>0))
    assert euler==1-5+117==113
    print('MORSE_OK')
    print('graph_vertices=20 graph_edges=30 faces_including_empty=',len(faces))
    print('face_size_histogram=',dict(sorted(hist.items())))
    print('cancellations=',cancellation_log)
    print('ordinary_critical=',dict(sorted(Counter(s.bit_count()-1 for s in rem).items())))
    print('morse_pairs=',len(up),'ordinary_faces=',len(faces)-1)
    print('acyclic_vertices=',seen,'directed_incidences=',incidences)
    print('signed_Morse_boundary_6_to_5=zero_matrix_shape_5_by_117, projection_cache=',shape[2])
    print('ordinary_Euler=',euler)

if __name__=='__main__':main()
