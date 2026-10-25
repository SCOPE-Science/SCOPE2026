#!/usr/bin/env python3
"""Finite checks for the S3 equational-probability spectrum theorem."""
from collections import deque
from fractions import Fraction
from itertools import product


def bits(k):
    return tuple(product((0,1), repeat=k))


def generator(k,i):
    e=tuple(int(j==i) for j in range(k))
    c=tuple(int(j==i) for b in bits(k) for j in range(k))
    return (e,c)


def multiply(k,A,B):
    e,c=A; f,d=B
    out=[]
    for ib,b in enumerate(bits(k)):
        t=-1 if sum(e[j]*b[j] for j in range(k))%2 else 1
        for i in range(k):out.append((c[ib*k+i]+t*d[ib*k+i])%3)
    return (tuple((e[i]+f[i])%2 for i in range(k)),tuple(out))


def exact_probability(k,A):
    e,c=A
    total=0
    for ib,b in enumerate(bits(k)):
        if sum(e[i]*b[i] for i in range(k))%2:continue
        total+=(3 if all(c[ib*k+i]==0 for i in range(k)) else 1)
    return Fraction(total,3*(2**k))


def rank3(vectors,k):
    a=[list(v) for v in vectors]
    row=0
    for col in range(k):
        pivot=next((j for j in range(row,len(a)) if a[j][col]%3),None)
        if pivot is None:continue
        a[row],a[pivot]=a[pivot],a[row]
        inv=pow(a[row][col],-1,3)
        a[row]=[(inv*t)%3 for t in a[row]]
        for j in range(len(a)):
            if j!=row and a[j][col]%3:
                f=a[j][col]
                a[j]=[(a[j][l]-f*a[row][l])%3 for l in range(k)]
        row+=1
    return row


def local_generators(k,b):
    t=[1 if b[i]==0 else -1 for i in range(k)]
    vectors=[]
    for i in range(k):
        v=[0]*k;v[i]=(1+t[i])%3
        vectors.append(v)
    for i in range(k):
        for j in range(i+1,k):
            v=[0]*k
            v[i]=(t[j]-1)%3
            v[j]=(1-t[i])%3
            vectors.append(v)
    return vectors


def enumerate_word_functions(k):
    ident=((0,)*k,(0,)*(k*(2**k)))
    gens=[generator(k,i) for i in range(k)]
    visited={ident}
    queue=deque([ident])
    while queue:
        cur=queue.popleft()
        for g in gens:
            nxt=multiply(k,cur,g)
            if nxt not in visited:
                visited.add(nxt);queue.append(nxt)
    return visited


def run():
    states=enumerate_word_functions(2)
    # 3^(2+1+1+1) choices for each of four parity classes in the even word group;
    # four possible sign characters give 4*3^5 word maps.
    assert len(states)==4*(3**5),(len(states),4*3**5)
    observed={exact_probability(2,s) for s in states}
    expected={Fraction(j,6) for j in range(1,7)}
    assert observed==expected,(observed,expected)
    nlocal=0
    for k in range(2,7):
        for b in bits(k):
            g=local_generators(k,b)
            d=tuple(((-1)**b[i]-1)%3 for i in range(k))
            assert all(sum(d[i]*v[i] for i in range(k))%3==0 for v in g)
            actual=rank3(g,k)
            expected=k if not any(b) else k-1
            assert actual==expected,(k,b,actual,expected)
            nlocal+=1
    # Direct multiplication check: the recursive word-map law must agree with
    # multiplication in F3 semidirect F2 at every assignment for two variables.
    k=2;one=((0,)*k,(0,)*(k*(2**k)))
    funcs=[generator(k,i) for i in range(k)]
    w=one
    checked=0
    for length in range(1,24):
        w=multiply(k,w,funcs[length%2])
        for b in bits(k):
            ib=bits(k).index(b)
            for a in product(range(3),repeat=k):
                x=(0,0)
                for i in range(1,length+1):
                    j=i%2
                    x=((x[0]+(-1 if x[1] else 1)*a[j])%3,(x[1]+b[j])%2)
                y=(sum(w[1][ib*k+i]*a[i] for i in range(k))%3,
                   sum(w[0][i]*b[i] for i in range(k))%2)
                assert x==y,(length,b,a,x,y)
                checked+=1
    print('S3_EQUATIONAL_WORD_MAP_OK',len(states),'maps',len(observed),'probabilities',nlocal,'local_ranks',checked,'evaluations')

if __name__=='__main__':run()
