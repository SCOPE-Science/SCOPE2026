#!/usr/bin/env python3
"""Standalone exhaustive checks of word-morphism centralizers and composition roots.
Pure Python 3, no third-party packages. Finite checks do not establish generality.
"""
from itertools import product, permutations
from collections import Counter
from math import factorial, comb


def words(n, maxlen):
    return [w for length in range(1, maxlen+1)
            for w in product(range(n), repeat=length)]


def apply(morphism, w):
    return tuple(y for x in w for y in morphism[x])


def power_images(profile):
    return tuple((i,)*m for i,m in enumerate(profile))


def composition_power(morph, k):
    values = morph
    for _ in range(k-1):
        values = tuple(apply(morph, w) for w in values)
    return values


def centralizes(morph, profile):
    power_map = power_images(profile)
    return all(apply(morph,power_map[i]) == apply(power_map,morph[i])
               for i in range(len(profile)))


def centralizer_normal_form(morph, profile):
    for i,w in enumerate(morph):
        if profile[i] == 1:
            if any(profile[x] != 1 for x in w):
                return False
        else:
            if any(x != w[0] for x in w) or profile[w[0]] != profile[i]:
                return False
    return True


def cycles(perm):
    unseen=set(range(len(perm)))
    out=[]
    while unseen:
        start=min(unseen);cur=start;cyc=[]
        while cur in unseen:
            unseen.remove(cur);cyc.append(cur);cur=perm[cur]
        assert cur==start
        out.append(cyc)
    return out


def factorizations(M,d):
    if d==1:
        return 1
    total=0
    def rec(left, slots):
        if slots==1:
            return 1
        return sum(rec(left//a,slots-1) for a in range(1,left+1) if left%a==0)
    return rec(M,d)


def exact_root_count(profile,k):
    n=len(profile);total=0
    for pi in permutations(range(n)):
        contribution=1
        for c in cycles(pi):
            d=len(c)
            if k%d or any(profile[i]!=profile[c[0]] for i in c):
                contribution=0;break
            N=profile[c[0]]
            # exact integer power check, without any floating reliance
            candidates=[a for a in range(1,N+1) if a**(k//d)==N]
            if not candidates:
                contribution=0;break
            contribution*=factorizations(candidates[0],d)
        total+=contribution
    return total


def coefficient_cycle_count(profile,k):
    answer=1
    for m in set(profile):
        count=profile.count(m)
        weights={}
        for d in range(1,count+1):
            if k%d:continue
            candidates=[a for a in range(1,m+1) if a**(k//d)==m]
            weights[d]=factorizations(candidates[0],d) if candidates else 0
        dp=[0]*(count+1)
        dp[0]=1
        for t in range(1,count+1):
            dp[t]=sum(comb(t-1,d-1)*factorial(d-1)*weights[d]*dp[t-d]
                      for d in weights if d<=t)
        answer*=dp[count]
    return answer


def check(n,maxlen,ks,max_profile):
    pool=words(n,maxlen)
    profiles=list(product(range(1,max_profile+1), repeat=n))
    target={power_images(p):p for p in profiles}
    empirical={k:Counter() for k in ks}
    total_morphisms=0
    for m in product(pool,repeat=n):
        total_morphisms+=1
        for k in ks:
            val=composition_power(m,k)
            p=target.get(val)
            if p is not None:
                empirical[k][p]+=1
    for k in ks:
        for p in profiles:
            a=empirical[k][p]
            b=exact_root_count(p,k)
            c=coefficient_cycle_count(p,k)
            assert a==b==c,(n,maxlen,k,p,a,b,c)
    print('ROOT_OK',{'n':n,'max_image_length':maxlen,'iterates':list(ks),
                     'profiles_checked':len(profiles),'morphisms_exhausted':total_morphisms})


def check_centralizers(n,maxlen,profiles):
    pool=words(n,maxlen)
    total=0
    for m in product(pool,repeat=n):
        total+=1
        for p in profiles:
            assert centralizes(m,p)==centralizer_normal_form(m,p), (m,p)
    print('CENTRALIZER_OK',{'n':n,'max_image_length':maxlen,
                            'profiles_checked':len(profiles),'morphisms_exhausted':total})

if __name__=='__main__':
    check(2,4,(2,3),4)
    check(3,3,(2,3),3)
    check_centralizers(2,3,[(1,1),(1,2),(2,1),(2,2),(2,3),(3,3)])
    check_centralizers(3,2,[(1,1,1),(2,2,2),(1,2,2),(2,1,3),(2,2,3)])
    for profile,k,expected in [((2,2),2,2),((4,4,4),2,10),
                               ((6,6,6,6),2,48),((8,8,8),3,21)]:
        actual=coefficient_cycle_count(profile,k)
        assert actual==expected,(profile,k,actual,expected)
    print('EXACT_COEFFICIENT_EXAMPLES_OK')
    print('VERIFY_OK')
