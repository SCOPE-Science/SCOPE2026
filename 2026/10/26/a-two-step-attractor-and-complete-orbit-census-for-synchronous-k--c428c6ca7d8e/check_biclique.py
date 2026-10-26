"""Exhaustive finite checks for synchronous k-reversible biclique dynamics.
This is a finite check only; the accompanying proof applies to all parameters.
Run: python3 check_biclique.py
"""
from math import comb


def advance(state, a, b, k):
    mask_a = (1 << a) - 1
    x, y = state & mask_a, state >> a
    i, j = x.bit_count(), y.bit_count()
    X = 0
    for t in range(a):
        bit = (x >> t) & 1
        if (j if bit == 0 else b-j) >= k:
            bit ^= 1
        X |= bit << t
    Y = 0
    for t in range(b):
        bit = (y >> t) & 1
        if (i if bit == 0 else a-i) >= k:
            bit ^= 1
        Y |= bit << t
    return X | (Y << a)


def lm(d, k):
    ell = sum(comb(d, t) for t in range(min(k-1, d-k)+1))
    return ell, 2**d-2*ell, int(d<=2*k-2)


def expected(a, b, k):
    n=2**(a+b)
    if k > max(a,b):
        return {'fix':n, 'two':0, 't0':n, 't1':0, 't2':0}
    if k>min(a,b):
        s, d = sorted([a,b])
        L,M,I=lm(d,k)
        fix=2*L+I*(2**s)*M
        two=(1-I)*(2**s)*M
        return {'fix':fix, 'two':two, 't0':fix+two, 't1':n-fix-two, 't2':0}
    La,Ma,Ia=lm(a,k);Lb,Mb,Ib=lm(b,k)
    fix=2+Ia*Ib*Ma*Mb
    two=2+(1-Ia*Ib)*Ma*Mb
    t0=fix+two
    t2=2*((La-1)*Mb+(Lb-1)*Ma)
    return {
      'fix':fix,'two':two,'t0':t0,'t1':n-t0-t2,'t2':t2,
      'basin_zero':La*Lb+Ib*La*Mb+Ia*Ma*Lb,
      'basin_one':La*Lb+Ib*La*Mb+Ia*Ma*Lb,
      'basin_anti':2*La*Lb+2*(1-Ib)*La*Mb+2*(1-Ia)*Ma*Lb,
      'internal':Ma*Mb
    }


def verify(a,b,k):
    N = 2**(a+b)
    p=expected(a,b,k)
    obs={'fix':0,'two':0,'t0':0,'t1':0,'t2':0}
    if k<=min(a,b):
        obs.update({'basin_zero':0,'basin_one':0,'basin_anti':0,'internal':0})
    mA=(1<<a)-1
    anti=(mA,(N-1)^mA)
    for st in range(N):
        s1=advance(st,a,b,k)
        s2=advance(s1,a,b,k)
        s3=advance(s2,a,b,k)
        s4=advance(s3,a,b,k)
        assert s4==s2, (a,b,k,st)
        if st==s1:
            obs['fix']+=1
        elif st==s2:
            obs['two']+=1
        if st==s2:obs['t0']+=1
        elif s1==s3:obs['t1']+=1
        else:
            assert s2==s4
            obs['t2']+=1
        if k<=min(a,b):
            if s2==0:obs['basin_zero']+=1
            elif s2==N-1:obs['basin_one']+=1
            elif s2 in anti:obs['basin_anti']+=1
            else:
                i=(s2&mA).bit_count();j=(s2>>a).bit_count()
                La,Ma,Ia=lm(a,k);Lb,Mb,Ib=lm(b,k)
                # Verify it is a middle/middle state, hence periodic.
                lowa=min(k-1,a-k);lowb=min(k-1,b-k)
                assert lowa<i<a-lowa and lowb<j<b-lowb,(a,b,k,st,s2)
                obs['internal']+=1
    assert obs==p,(a,b,k,obs,p)


def main():
    n=0
    for a in range(1,8):
        for b in range(1,8):
            for k in range(1,max(a,b)+2):
                verify(a,b,k);n+=1
    print('PASS: exact orbit/entry/basin census for',n,'parameter triples, a,b<=7.')
    print('PASS: F^4=F^2 for every enumerated state and parameter.')
    print('Example a=b=6, k=2:', expected(6,6,2))
    print('Example a=b=4, k=3:', expected(4,4,3))
    print('Example a=2,b=10,k=3:', expected(2,10,3))

if __name__=='__main__':
    main()
