"""Independent arithmetic check of the Venn-zone two-anchor invariant."""
from collections import defaultdict
from math import comb

def bounded_tuples(n,k,b):
    a=k-b
    w=n-k-b
    for t in range(a+1):
        for u in range(b+1):
            for v in range(b+1):
                z=k-t-u-v
                if 0<=z<=w:
                    yield t,u,v,z

def test(n,k,b):
    a=k-b;w=n-k-b
    sig_groups=defaultdict(set)
    orbit_keys=set()
    weighted_counts=defaultdict(int)
    tuples=list(bounded_tuples(n,k,b))
    for p in tuples:
        t,u,v,z=p
        distance_a=k-t-u
        distance_b=k-t-v
        fminus=z*(a-t)
        fplus=t*(w-z)
        feature=(distance_a,distance_b,fminus,fplus)
        if n==2*k:
            flip=(a-z,b-v,b-u,a-t)
            assert flip in tuples
            orbit_key=min(p,flip)
        else:
            orbit_key=p
        sig_groups[feature].add(orbit_key)
        orbit_keys.add(orbit_key)
        weight=comb(a,t)*comb(b,u)*comb(b,v)*comb(w,z)
        weighted_counts[orbit_key]+=weight
        assert fminus-fplus==a*(distance_a+distance_b-k)+t*(2*k-n)
    assert all(len(v)==1 for v in sig_groups.values()), (n,k,b)
    assert len(sig_groups)==len(orbit_keys), (n,k,b)
    assert sum(weighted_counts.values())==comb(n,k)
    if n==2*k:
        assert len(sig_groups)==(len(tuples)+(a+1)*(b+1))//2
    else:
        assert len(sig_groups)==len(tuples)
    return len(tuples), len(sig_groups)

def main():
    configurations=0
    signatures=0
    for n in range(6, 37):
        for k in range(3,n//2+1):
            for b in range(1,k+1):
                t,c=test(n,k,b)
                configurations+=1
                signatures+=t
    print('parameter_configurations',configurations)
    print('feasible_venn_signatures_checked',signatures)
    for n,k,b in [(6,3,1),(8,4,2),(9,4,2),(12,6,3)]:
        print('example',n,k,b,'venn_tuples_orbit_cells',*test(n,k,b))
    print('PASS: local feature separates exactly the orbit types')

if __name__ == '__main__':
    main()
