from collections import Counter

def F(r,m):
    if m%2==0:
        return r*(r-1)*m*m//4
    return (r*(r-1)*m*m+r)//4

def cut_value(r,m,prefix_counts):
    t=sum(prefix_counts)
    N=r*m
    return t*(N-t)-sum(x*(m-x) for x in prefix_counts)

def cyclic_profile(r,m):
    return [i for _ in range(m) for i in range(r)]

def profile_dtc(r,m,spine):
    counts=[0]*r
    best=0
    for v in spine[:-1]:
        counts[v]+=1
        best=max(best,cut_value(r,m,counts)-1)
    return best

def gen_multiset_sequences(counts,last=None,prefix=None):
    if prefix is None: prefix=[]
    if sum(counts)==0:
        yield tuple(prefix); return
    for i,c in enumerate(counts):
        if c and i!=last:
            counts[i]-=1; prefix.append(i)
            yield from gen_multiset_sequences(counts,i,prefix)
            prefix.pop(); counts[i]+=1

def test_formula():
    for r in range(3,25):
        for m in range(2,31):
            seq=cyclic_profile(r,m)
            assert all(seq[i]!=seq[i+1] for i in range(len(seq)-1))
            counts=[0]*r; vals=[]
            for v in seq[:-1]:
                counts[v]+=1; vals.append(cut_value(r,m,counts)-1)
            assert max(vals)==F(r,m)-1,(r,m,max(vals),F(r,m)-1)
            t=(r*m)//2
            q,s=divmod(t,r)
            bal=[q+1]*s+[q]*(r-s)
            assert cut_value(r,m,bal)==F(r,m),(r,m,bal,cut_value(r,m,bal),F(r,m))
            for p in range(m+1):
                assert r*m-p>t

def exhaustive_profiles():
    cases=[]
    for r,m in [(3,2),(3,3),(4,2)]:
        target=F(r,m)-1
        minimum=10**9; profiles=0
        # Pure-spine profiles.
        for seq in gen_multiset_sequences([m]*r):
            profiles+=1; minimum=min(minimum,profile_dtc(r,m,seq))
        # Every branched DFS tree of a complete multipartite graph is a spine
        # ending in singleton leaves from one part. Exhaust those profiles too.
        for leaf_part in range(r):
            for p in range(1,m+1):
                cnt=[m]*r; cnt[leaf_part]-=p
                for seq in gen_multiset_sequences(cnt):
                    if not seq or seq[-1]==leaf_part: continue
                    profiles+=1; minimum=min(minimum,profile_dtc(r,m,seq))
        assert minimum==target,(r,m,minimum,target)
        cases.append((r,m,profiles,target))
    return cases

if __name__=='__main__':
    test_formula()
    cases=exhaustive_profiles()
    print('ALGEBRA_CHECKS_OK r=3..24 m=2..30')
    for r,m,n,t in cases:
        print(f'PROFILE_ENUM_OK r={r} m={m} profiles={n} optimum_DTC={t}')
    print('ALL CHECKS PASSED')
