from itertools import product, permutations
from math import gcd, comb

IRR={2:0b111,3:0b1011,4:0b10011}

def gf_mul(a,b,f,mod):
    r=0
    x=a; y=b
    while y:
        if y&1:r^=x
        y>>=1; x<<=1
        if x>>f: x^=mod
    return r & ((1<<f)-1)

def gf_pow(a,n,f,mod):
    r=1
    while n:
        if n&1:r=gf_mul(r,a,f,mod)
        a=gf_mul(a,a,f,mod); n>>=1
    return r

def frob(a,f,mod): return gf_pow(a,2,f,mod)

def minpoly_bits(a,f,mod):
    orb=[]; x=a
    while x not in orb:
        orb.append(x); x=frob(x,f,mod)
    poly=[1]
    for r in orb:
        out=[0]*(len(poly)+1)
        for i,c in enumerate(poly):
            out[i] ^= gf_mul(c,r,f,mod)
            out[i+1] ^= c
        poly=out
    assert all(c in (0,1) for c in poly), (a,f,poly)
    return tuple(poly)

def char_sig(c,arr,f,mod):
    # factorization signature of characteristic polynomial over F_2:
    # {minimal-polynomial coefficient tuple: exponent}
    D={}
    # base F_2 factor T-c
    p=(c,1)
    D[p]=D.get(p,0)+1
    for a in arr:
        mp=minpoly_bits(a,f,mod)
        d=len(mp)-1
        D[mp]=D.get(mp,0)+f//d
    return tuple(sorted(D.items()))

def orbit_key(c,arr,f,mod):
    # Frobenius orbits in each K-coordinate, then permutation multiset
    mins=sorted(minpoly_bits(a,f,mod) for a in arr)
    return (c,tuple(mins))

def actual_orbits_f2(f,m):
    mod=IRR[f]; K=range(1<<f)
    elems=[(c,tuple(arr)) for c in (0,1) for arr in product(K,repeat=m)]
    unseen=set(elems); orbits=[]
    while unseen:
        seed=next(iter(unseen)); stack=[seed]; orb=set()
        while stack:
            z=stack.pop()
            if z in orb: continue
            orb.add(z); c,arr=z
            # independent Frobenius generators
            for i in range(m):
                b=list(arr); b[i]=frob(b[i],f,mod); stack.append((c,tuple(b)))
            # adjacent swaps generate S_m
            for i in range(m-1):
                b=list(arr); b[i],b[i+1]=b[i+1],b[i]; stack.append((c,tuple(b)))
        unseen-=orb; orbits.append(orb)
    return orbits

def H(q,f):
    return sum(q**gcd(f,i) for i in range(f))//f

def check_nonsplit(l,f):
    q=2; m=(l-1)//f
    assert pow(q,f,l)==1 and all(pow(q,d,l)!=1 for d in range(1,f))
    orbs=actual_orbits_f2(f,m)
    predicted=q*comb(H(q,f)+m-1,m)
    assert len(orbs)==predicted,(l,len(orbs),predicted)
    # characteristic polynomial is constant on and separates automorphism orbits
    sig_to_orb={}
    unit_orbs=0
    for j,orb in enumerate(orbs):
        sigs={char_sig(c,a,f,IRR[f]) for c,a in orb}
        assert len(sigs)==1
        sig=next(iter(sigs))
        assert sig not in sig_to_orb,(l,j,sig)
        sig_to_orb[sig]=j
        c,a=next(iter(orb))
        if c!=0 and all(x!=0 for x in a): unit_orbs+=1
    predicted_units=(q-1)*comb(H(q,f)+m-2,m)
    assert unit_orbs==predicted_units,(l,unit_orbs,predicted_units)
    print(f'non_split l={l} q=2 f={f} m={m} H={H(q,f)} orbits={len(orbs)} unit_orbits={unit_orbs}')

def check_split(q,l):
    assert (q-1)%l==0
    elems=list(product(range(q),repeat=l))
    unseen=set(elems); orbs=[]
    perms=list(permutations(range(l)))
    while unseen:
        a=next(iter(unseen))
        orb={tuple(a[i] for i in p) for p in perms}
        unseen-=orb; orbs.append(orb)
    pred=comb(q+l-1,l)
    assert len(orbs)==pred
    # char polynomial over F_q is determined by root multiplicities, i.e. multiset
    sigs=set()
    unit=0
    for orb in orbs:
        a=next(iter(orb)); sig=tuple(a.count(r) for r in range(q))
        assert sig not in sigs; sigs.add(sig)
        if all(x!=0 for x in a): unit+=1
    predu=comb(q+l-2,l)
    assert unit==predu
    print(f'split l={l} q={q} orbits={len(orbs)} unit_orbits={unit}')

if __name__=='__main__':
    check_nonsplit(3,2)
    check_nonsplit(5,4)
    check_nonsplit(7,3)
    check_split(3,2)
    print('VERIFY_OK')
