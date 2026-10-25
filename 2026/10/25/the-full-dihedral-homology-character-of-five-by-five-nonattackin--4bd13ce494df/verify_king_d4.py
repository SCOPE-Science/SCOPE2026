#!/usr/bin/env python3
"""Exact integral chain verification of the graded dihedral action on a 5x5 kings complex.
Only the Python standard library is required. The algorithm enumerates every face;
no randomness, external numerical packages or unstated data are used.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

N=5

def all_faces():
    patterns=[a for a in range(1<<N) if not(a&(a<<1))]
    follow={a:[b for b in patterns if not(a&(b|(b<<1)|(b>>1)))] for a in patterns}
    faces=[]
    def build(r,prev,s):
        if r==N:faces.append(s);return
        for a in patterns if r==0 else follow[prev]:
            build(r+1,a,s|(a<<(N*r)))
    build(0,0,0)
    return faces

def build_pairs(faces):
    un=set(faces);pairs={}
    for c in range(N):
        for r in range(N):
            v=1<<(N*r+c)
            for a in list(un):
                if not(a&v) and a|v in un:
                    b=a|v;pairs[a]=b;un.remove(a);un.remove(b)
    return pairs,un

def boundary(s):
    i=0
    while s:
        b=s&-s;s-=b
        yield b, (-1 if i&1 else 1)
        i+=1

def acyclic(faces,pairs):
    deg={s:0 for s in faces}
    for s in faces:
        for bit,_ in boundary(s):
            t=s^bit
            if pairs.get(t)==s:deg[s]+=1
            else:deg[t]+=1
    queue=deque(s for s in faces if deg[s]==0);count=0
    while queue:
        s=queue.popleft();count+=1
        if s in pairs:
            t=pairs[s];deg[t]-=1
            if deg[t]==0:queue.append(t)
        for bit,_ in boundary(s):
            t=s^bit
            if pairs.get(t)==s:continue
            deg[t]-=1
            if deg[t]==0:queue.append(t)
    assert count==len(faces),(count,len(faces))

def apply(s,perm):
    vertices=[]
    while s:
        b=s&-s;s-=b;vertices.append(perm[b.bit_length()-1])
    out=sum(1<<i for i in vertices)
    inversions=sum(a>b for j,a in enumerate(vertices) for b in vertices[j+1:])
    return out,(-1 if inversions%2 else 1)

def main():
    faces=all_faces();allset=set(faces)
    assert len(faces)==6427
    pairs,crit=build_pairs(faces);back={b:a for a,b in pairs.items()}
    assert len(pairs)==3174 and len(crit)==79
    assert all(not any((s|(1<<v)) in allset for v in range(N*N) if not(s&(1<<v))) for s in crit)
    acyclic(faces,pairs)
    count=Counter(s.bit_count()-1 for s in crit)
    assert count=={3:45,4:32,5:2}
    @lru_cache(None)
    def project(s):
        if s in crit:return {s:1}
        if s in back:return {}
        u=pairs[s];bit=u^s;den=-1 if (s&(bit-1)).bit_count()%2 else 1
        out=defaultdict(int)
        for b,coef in boundary(u):
            v=u^b
            if v==s:continue
            for c,w in project(v).items():out[c]-=den*coef*w
        return {c:w for c,w in out.items() if w}
    @lru_cache(None)
    def correction(s):
        u=pairs[s];bit=u^s;den=-1 if (s&(bit-1)).bit_count()%2 else 1
        out=defaultdict(int);out[u]=den
        for b,coef in boundary(u):
            v=u^b
            if v==s or v not in pairs:continue
            for c,w in correction(v).items():out[c]-=den*coef*w
        return {c:w for c,w in out.items() if w}
    def lift(s):
        out=defaultdict(int);out[s]=1
        for b,coef in boundary(s):
            v=s^b
            if v in pairs:
                for c,w in correction(v).items():out[c]-=coef*w
        return {c:w for c,w in out.items() if w}
    cycles={}
    for s in crit:
        z=lift(s);cycles[s]=z
        bd=defaultdict(int);red=defaultdict(int)
        for u,c in z.items():
            for b,coef in boundary(u):bd[u^b]+=c*coef
            for y,w in project(u).items():red[y]+=c*w
        assert not any(bd.values())
        assert {y:w for y,w in red.items() if w}=={s:1}
    # Explicit full-chain check of the reduced Morse differential.
    for s in faces:
        red=defaultdict(int)
        for b,coef in boundary(s):
            for y,w in project(s^b).items():red[y]+=coef*w
        assert not any(red.values())
    degrees={d:sorted(s for s in crit if s.bit_count()-1==d) for d in (3,4,5)}
    maps={
        'e':lambda r,c:(r,c),
        'r90':lambda r,c:(c,4-r),
        'r180':lambda r,c:(4-r,4-c),
        'r270':lambda r,c:(4-c,r),
        'axis_h':lambda r,c:(4-r,c),
        'axis_v':lambda r,c:(r,4-c),
        'diag':lambda r,c:(c,r),
        'anti_diag':lambda r,c:(4-c,4-r),
    }
    perms={name:tuple(5*f(r,c)[0]+f(r,c)[1] for r in range(5) for c in range(5)) for name,f in maps.items()}
    traces={}
    matrices={}
    for name,perm in perms.items():
        matrices[name]={}
        traces[name]={}
        for d,cs in degrees.items():
            ci={s:i for i,s in enumerate(cs)};L=len(cs)
            mat=[[0]*L for i in range(L)]
            for col,s in enumerate(cs):
                v=defaultdict(int)
                for u,coef in cycles[s].items():
                    y,sign=apply(u,perm)
                    for q,w in project(y).items():v[q]+=coef*sign*w
                for q,w in v.items():
                    if w:mat[ci[q]][col]=w
            matrices[name][d]=mat
            traces[name][d]=sum(mat[i][i] for i in range(L))
        # Independent simplicial Lefschetz trace.
        L=sum((-1)**d*traces[name][d] for d in degrees)
        simp=0
        for s in faces:
            q,sign=apply(s,perm)
            if q==s:simp+=(-1)**(s.bit_count()-1)*sign
        assert L==simp,(name,L,simp)
    # The representation matrices satisfy generating relations of D4 on each degree.
    def mm(A,B):
        n=len(A)
        return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    for d,cs in degrees.items():
        E=matrices['e'][d];R=matrices['r90'][d];H=matrices['axis_h'][d]
        I=[[int(i==j) for j in range(len(cs))] for i in range(len(cs))]
        assert E==I
        assert mm(mm(mm(R,R),R),R)==I
        assert mm(H,H)==I
        assert mm(mm(H,R),H)==matrices['r270'][d]
        assert mm(R,R)==matrices['r180'][d]
    class_chars={d:(traces['e'][d],traces['r90'][d],traces['r180'][d],traces['axis_h'][d],traces['diag'][d]) for d in degrees}
    expected={3:(45,-1,5,3,-3),4:(32,0,0,4,0),5:(2,0,-2,0,0)}
    assert class_chars==expected,(class_chars,expected)
    chars={'A1':(1,1,1,1,1),'A2':(1,1,1,-1,-1),
           'B1':(1,-1,1,1,-1),'B2':(1,-1,1,-1,1),'E':(2,0,-2,0,0)}
    mults={}
    for d,values in class_chars.items():
        mults[d]={}
        for label,ch in chars.items():
            numerator=sum(a*b*size for a,b,size in zip(values,ch,(1,2,1,2,2)))
            assert numerator>=0 and numerator%8==0
            mults[d][label]=numerator//8
    assert mults=={
        3:{'A1':6,'A2':6,'B1':8,'B2':5,'E':10},
        4:{'A1':5,'A2':3,'B1':5,'B2':3,'E':8},
        5:{'A1':0,'A2':0,'B1':0,'B2':0,'E':1}}
    for d in degrees:
        print(f'degree {d}: D4 character {class_chars[d]}, irreducibles {mults[d]}')
    print('PASS: all 6427 simplices, 3174 matched pairs, DAG, 79 maximal critical simplices, integral cycles, maps, D4 relations, Lefschetz traces')
if __name__=='__main__':main()
