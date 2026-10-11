#!/usr/bin/env python3
from fractions import Fraction
from itertools import product, combinations

def alternating_vertices(word):
    m=len(word)
    out={(0,)*m}
    for r in range(2,m+1,2):
        for sub in combinations(range(m),r):
            if all(word[i]==("U" if t%2==0 else "D") for t,i in enumerate(sub)):
                v=[0]*m
                for t,i in enumerate(sub):
                    v[i]=1 if t%2==0 else -1
                out.add(tuple(v))
    return out

def center(word):
    m=len(word)
    p=word.count("U")
    q=m-p
    return tuple(Fraction(q,m) if s=="U" else -Fraction(p,m) for s in word)

def prefix_strip(word,c):
    s=Fraction(0)
    for j in range(len(word)-1):
        s+=c[j]
        if not (0<=s<=1):
            return False
    return True

def source_facets_at_center(word,c):
    # Signs and total equality are automatic for the canonical center.
    assert all((x>=0 if word[i]=="U" else x<=0) for i,x in enumerate(c))
    assert sum(c)==0
    pref=[]
    s=Fraction(0)
    for x in c:
        s+=x
        pref.append(s)
    # Falls U|D impose prefix <=1; rises D|U impose prefix >=0.
    for j in range(len(word)-1):
        if word[j]=="U" and word[j+1]=="D" and not pref[j]<=1:
            return False
        if word[j]=="D" and word[j+1]=="U" and not pref[j]>=0:
            return False
    return True

words=0
vertices=0
for m in range(2,11):
    for middle in product("UD", repeat=m-2):
        word="U"+"".join(middle)+"D"
        p=word.count("U")
        q=word.count("D")
        c=center(word)
        want=Fraction(p*q,m)
        V=alternating_vertices(word)

        for v in V:
            d2=sum((Fraction(v[i])-c[i])**2 for i in range(m))
            assert d2==want,(word,v,d2,want)
            tv=[v[i]+(1 if word[i]=="D" else 0) for i in range(m)]
            assert all(z in (0,1) for z in tv)
            assert sum(tv)==q
            vertices+=1

        strip=prefix_strip(word,c)
        facets=source_facets_at_center(word,c)
        assert strip==facets,(word,strip,facets)

        if word=="U"*p+"D"*q:
            assert strip==(p*q<=p+q)
            assert (p*q<=p+q)==((p-1)*(q-1)<=1)

        words+=1

print(f"VERIFY_OK shard-common-sphere words={words} vertices={vertices} m=2..10 exact=yes")
