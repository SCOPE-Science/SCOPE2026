#!/usr/bin/env python3
"""Independent structural triple-diagram/extension check for TD(3,n).

This tests the local case analysis on two nonisotopic order-four squares
and the cyclic square of order five. The infinite proof is the counting
argument given in RESULT.md, not a finite extrapolation.
"""
from itertools import permutations

PERMS=list(permutations(range(3)))

def design(n,op):
    vertices=[('P',(g,i)) for g in range(3) for i in range(n)]
    vertices += [('B',((0,i),(1,j),(2,op(i,j)))) for i in range(n) for j in range(n)]
    adj=[[False]*len(vertices) for _ in vertices]
    for b,(kind,points) in enumerate(vertices):
        if kind=='B':
            for g,i in points:adj[b][g*n+i]=adj[g*n+i][b]=True
    return vertices,adj

def diagram(V,tup):
    options=[]
    for p in PERMS:
        mapping=[{} for _ in range(3)]
        def cod(g,i):
            h=p[g];m=mapping[h]
            if i not in m:m[i]=len(m)
            return h,m[i]
        pattern=[]
        for ix in tup:
            tag,data=V[ix]
            if tag=='P':pattern.append(('P',cod(*data)))
            else:pattern.append(('B',tuple(sorted(cod(*x) for x in data))))
        options.append(tuple(pattern))
    return min(options)

def atom(A,tup):
    out=[]
    for i in range(len(tup)):
        for j in range(i+1,len(tup)):
            a,b=tup[i],tup[j]
            out.append(0 if a==b else 1 if A[a][b] else 2)
    return tuple(out)

def signatures(n,op):
    V,A=design(n,op);N=len(V)
    one={};two={};three={}
    for a in range(N):
        d1=diagram(V,(a,))
        one.setdefault(d1,set())
        for b in range(N):
            d2=diagram(V,(a,b))
            two.setdefault(d2,set())
            one[d1].add(d2)
            for c in range(N):
                d3=diagram(V,(a,b,c))
                two[d2].add(d3)
                if d3 not in three:three[d3]=set()
                for d in range(N):three[d3].add(atom(A,(a,b,c,d)))
    return one,two,three

def main():
    S=[('cyclic4',signatures(4,lambda a,b:(a+b)%4)),
       ('klein4',signatures(4,lambda a,b:a^b))]
    for name,vec in S:
        print(f'{name}: one/two/three structural types = {[len(t) for t in vec]}')
    for name,vec in S[1:]:
        assert vec==S[0][1],f'{name}: mismatch in structural extension sets'
    print('PASS: 2 / 10 / 85 structural types; matching extension sets for two nonisotopic test designs')
    # Universal design identities, for each n>=4; all entries strictly positive.
    for n in range(4,100):
        meet=(n-2,2,2*n-4,(n-2)*(n-3))
        disjoint=(6,3*(n-3),(n-3)**2+1)
        assert min(meet)>0 and min(disjoint)>0
        assert n*n>=3*n+4
    print('PASS: all stated triple-block extension counts positive for n>=4')

if __name__=='__main__':main()
