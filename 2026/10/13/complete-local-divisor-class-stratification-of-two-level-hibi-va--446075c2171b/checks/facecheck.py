#!/usr/bin/env python3
"""Exact-rank enumerator of toric face singularities of stable-set polytopes K_{a,b}.
Facets and vertices are explicit; no external data or symbolic software needed.
"""
from itertools import combinations
from fractions import Fraction

def rank(rows):
    if not rows: return 0
    m = [[Fraction(t) for t in row] for row in rows]
    h,w=len(m),len(m[0]); row=0
    for c in range(w):
        pivot=next((k for k in range(row,h) if m[k][c]),None)
        if pivot is None: continue
        m[row],m[pivot]=m[pivot],m[row]
        z=m[row][c]
        for t in range(c,w): m[row][t]/=z
        for k in range(row+1,h):
            z=m[k][c]
            if z:
                for t in range(c,w): m[k][t]-=z*m[row][t]
        row+=1
        if row==h:break
    return row

def check(a,b,verbose=False):
    d=a+b
    vertices = [tuple(int(bool(mask&(1<<i))) for i in range(a))+(0,)*b for mask in range(1<<a)]
    vertices += [(0,)*a+tuple(int(bool(mask&(1<<j))) for j in range(b)) for mask in range(1,1<<b)]
    facets=[]
    for i in range(d):
        norm=[0]*d; norm[i]=1
        facets.append((tuple(norm),0,('axis',i)))
    for i in range(a):
        for j in range(b):
            norm=[0]*d; norm[i]=-1; norm[a+j]=-1
            facets.append((tuple(norm),1,('edge',i,j)))
    sets=[]
    for norm,const,tag in facets:
        vset=frozenset(i for i,v in enumerate(vertices) if sum(t*s for t,s in zip(norm,v))+const==0)
        assert len(vset)>1, (a,b,tag,len(vset))
        sets.append(vset)
    faces={frozenset(range(len(vertices)))}
    for fset in sets:
        faces |= {f&fset for f in tuple(faces)}
    faces.discard(frozenset())
    dims={F:rank([tuple(x-y for x,y in zip(vertices[i], vertices[min(F)])) for i in F if i != min(F)]) for F in faces}
    sing={}
    for F in faces:
        active=[k for k,S in enumerate(sets) if F<=S]
        rr=rank([facets[k][0] for k in active])
        assert rr+ dims[F]==d,(a,b,rr,dims[F],d)
        avg=[Fraction(sum(vertices[k][h] for k in F),len(F)) for h in range(d)]
        p=sum(avg[i]==1 for i in range(a))
        q=sum(avg[a+j]==1 for j in range(b))
        if p:
            want=p*(b-1)
        elif q:
            want=q*(a-1)
        else:
            c=min(1-avg[i] for i in range(a))
            e=max(avg[a+j] for j in range(b))
            if c==e:
                left=sum(1-avg[i]==c for i in range(a))
                right=sum(avg[a+j]==c for j in range(b))
                want=(left-1)*(right-1)
            else:want=0
        assert len(active)-rr==want, (a,b,F,avg,len(active)-rr,want)
        if len(active)>rr:
            sing[F]=(dims[F],tuple(active))
    maximal = {F:sing[F] for F in sing if not any(F<G for G in sing)}
    expected_faces = {}
    for i in range(a):
        F=frozenset(k for k,v in enumerate(vertices) if v[i]==1)
        expected_faces[F] = (a-1,2*b,'lower')
    for j in range(b):
        F=frozenset(k for k,v in enumerate(vertices) if v[a+j]==1)
        expected_faces[F] = (b-1,2*a,'upper')
    for i,h in combinations(range(a),2):
        for j,k in combinations(range(b),2):
            F=frozenset(idx for idx,v in enumerate(vertices) if (v[i]==v[h]==1) or (v[a+j]==v[a+k]==1))
            expected_faces[F]=(a+b-3,4,'interior')
    assert set(maximal)==set(expected_faces),(a,b,'component face mismatch')
    for F,(dim,active) in maximal.items():
        wanted_dim,wanted_rays,_=expected_faces[F]
        assert dim==wanted_dim and len(active)==wanted_rays, (a,b,dim,len(active),expected_faces[F])
    for idx,v in enumerate(vertices):
        F=frozenset([idx]); active=[k for k,S in enumerate(sets) if F<=S]
        sizA=sum(v[:a]); sizB=sum(v[a:]);
        target=sizA*(b-1)+sizB*(a-1)
        assert len(active)-d==target,(a,b,v,len(active)-d,target)
    expected= a+b+a*(a-1)//2*(b*(b-1)//2)
    codims={d-dim for dim,act in maximal.values()}
    assert len(maximal)==expected, (a,b,len(maximal),expected)
    expected_dims=[(d-3,a*(a-1)//2*(b*(b-1)//2)),(a-1,a),(b-1,b)]
    obs={}
    for dim,_ in maximal.values():obs[dim]=obs.get(dim,0)+1
    exp={}
    for dim,c in expected_dims:exp[dim]=exp.get(dim,0)+c
    assert obs==exp,(a,b,obs,exp)
    if verbose: print('a,b:',a,b,'vertices',len(vertices),'faces',len(faces),'singular faces',len(sing),'components',len(maximal),'dimensions',obs,'models', {x:sum(1 for _f,(_d,_r,y) in expected_faces.items() if y==x) for x in ['interior','lower','upper']})
    return len(faces),len(sing),len(maximal),obs

if __name__=='__main__':
    for a,b in [(2,2),(3,2),(2,3),(3,3),(4,2),(2,4)]:
        check(a,b,True)
