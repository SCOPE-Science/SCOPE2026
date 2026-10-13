#!/usr/bin/env python3

def tmod(ell,N):
    return [n.bit_count()%ell for n in range(N)]

def factor_set(seq,n):
    return {tuple(seq[i:i+n]) for i in range(len(seq)-n+1)}

def rcount(F):
    return len({min(w,w[::-1]) for w in F})

difference_checks=0
local_checks=0
for ell in range(3,21):
    x=tmod(ell,50002)
    for n in range(50000):
        d=(x[n+1]-x[n])%ell
        v2=(((n+1)&-(n+1)).bit_length()-1)
        assert d==(1-v2)%ell
        difference_checks+=1
    for i in range(49997):
        d0=(x[i+1]-x[i])%ell
        d1=(x[i+2]-x[i+1])%ell
        d2=(x[i+3]-x[i+2])%ell
        if (i+2)%2==0:
            assert d0==1 and d2==1
        else:
            assert d1==1 and (d0==0 or d2==0)
        a,b,c=(-d2)%ell,(-d1)%ell,(-d0)%ell
        possible=((a==1 and c==1) or (b==1 and (a==0 or c==0)))
        assert not possible
        local_checks+=1

factor_checks=0
for ell in range(3,10):
    s=tmod(ell,1<<18)
    for n in range(1,49):
        F=factor_set(s,n)
        if n==3:
            for w in F:
                if w[::-1] in F:
                    assert w==w[::-1]
            assert rcount(F)==len(F)
        if n>=4:
            assert all(w[::-1] not in F for w in F)
            assert rcount(F)==len(F)
        factor_checks+=len(F)

s=tmod(4,1<<18)
expected=[(1,4,4),(2,16,10),(3,28,28),(4,44,44),(5,56,56),(6,72,72)]
for n,p,r in expected:
    F=factor_set(s,n)
    assert (n,len(F),rcount(F))==(n,p,r)

print('VERIFY_OK '
      f'difference_checks={difference_checks} local_length4_checks={local_checks} '
      f'observed_factor_instances={factor_checks} ell=3..9 lengths=1..48 '
      'mod4=4/4,16/10,28/28,44/44,56/56,72/72 '
      'theorem=rho_equals_r_for_ell_ge3_n_ge3')
