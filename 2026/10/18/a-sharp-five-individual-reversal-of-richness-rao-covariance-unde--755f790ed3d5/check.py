"""Exact enumerative cross-checks for a finite-rarefaction richness/Rao theorem.

Run: python check.py > certificate.json
All arithmetic uses integers and fractions; no optional packages.
"""
import itertools
import json
from fractions import Fraction
from math import comb


def compositions(n):
    if n == 0:
        yield ()
        return
    for first in range(1, n + 1):
        if first == n:
            yield (first,)
        else:
            for tail in compositions(n-first):
                yield (first,) + tail


def direct_covariance(abundances, distance, m):
    """Enumerate each equally likely subset of *labeled* individuals."""
    individuals = tuple(i for i,a in enumerate(abundances) for _ in range(a))
    values = []
    for index_set in itertools.combinations(range(len(individuals)), m):
        counts = [0] * len(abundances)
        for idx in index_set:
            counts[individuals[idx]] += 1
        richness = sum(1 for x in counts if x)
        q_numerator = sum(counts[i]*counts[j]*distance[i][j]
                          for i in range(len(counts)) for j in range(i+1,len(counts)))
        q = Fraction(q_numerator, comb(m,2))
        values.append((richness,q))
    nv = len(values)
    k_bar = Fraction(sum(k for k,_ in values),nv)
    q_bar = sum((q for _,q in values),Fraction(0))/nv
    return sum(((k-k_bar)*(q-q_bar) for k,q in values),Fraction(0))/nv


def single_duplicate_covariance(distance):
    """Formula based on omitting one of 2+r individuals, independently of subset enumeration."""
    r = len(distance)-1
    between = sum(distance[0][j] for j in range(1,r+1))
    within = sum(distance[i][j] for i in range(1,r+1) for j in range(i+1,r+1))
    return Fraction(4*(2*within-(r-2)*between),(r+2)**2*r*(r+1))


def ultrametric_matrix(r,h,ell):
    return [[0 if i==j else (h if i==0 or j==0 else ell)
             for j in range(r+1)] for i in range(r+1)]


def frac(x):
    return f'{x.numerator}/{x.denominator}'


def main():
    low_tests=0
    for n in range(2,5):
        for composition in compositions(n):
            r=len(composition)
            for m in range(2,n+1):
                for i in range(r):
                    for j in range(i+1,r):
                        d=[[0]*r for _ in range(r)]
                        d[i][j]=d[j][i]=1
                        cv=direct_covariance(composition,d,m)
                        assert cv>=0,(n,composition,m,i,j,cv)
                        low_tests+=1
    arbitrary_tests=0
    Hs=(1,2,3,4,7,13)
    Ls=(1,2,3)
    for r in range(2,12):
        a=(2,)+(1,)*r
        for h in Hs:
            for l in Ls:
                if h<l:continue
                d=ultrametric_matrix(r,h,l)
                got=direct_covariance(a,d,r+1)
                target=single_duplicate_covariance(d)
                simp=Fraction(4*((r-1)*l-(r-2)*h),(r+2)**2*(r+1))
                assert got==target==simp,(r,h,l,got,target,simp)
                arbitrary_tests+=1
    asym_tests=0
    for r in range(2,10):
        a=(2,)+(1,)*r
        # vary non-ultrametric entries: the general identity needs no metric assumption
        for key in (1,2,3,4,5):
            d=[[0 if i==j else (1+((7*i+11*j+key) % 13))
                for j in range(r+1)] for i in range(r+1)]
            for i in range(r+1):
                for j in range(i+1,r+1):
                    d[j][i]=d[i][j]
            assert direct_covariance(a,d,r+1)==single_duplicate_covariance(d)
            asym_tests+=1
    # At r=3, (2,1,1,1), distances between outgroup and singleton cluster = 3,
    # distances among singleton species = 1, covariance for m=2,3,4,5.
    d=ultrametric_matrix(3,3,1)
    example=[direct_covariance((2,1,1,1),d,m) for m in range(2,6)]
    assert example == [Fraction(21,100),Fraction(3,100),Fraction(-1,25),Fraction(0)]
    # For every fixed positive contrast, sufficiently many singleton tips suffice.
    small_contrast=[]
    for r in (4,5,7,12,32,102):
        h=Fraction(r-1,r-2)+Fraction(1,10**5)
        el=Fraction(1)
        c=Fraction(4*((r-1)*el-(r-2)*h),(r+2)**2*(r+1))
        assert c<0
        small_contrast.append({'singleton_tips':r,'threshold_ratio':frac(Fraction(r-1,r-2))})
    payload={
      'schema_version':1,
      'model':'uniform labeled-individual subsets without replacement; unbiased pairwise Rao statistic',
      'low_N_nonnegative_basis_tests':low_tests,
      'unrestricted_formula_ultrametric_exact_subset_tests':arbitrary_tests,
      'general_dissimilarity_exact_subset_tests':asym_tests,
      'five_individual_witness':{'abundances':[2,1,1,1],
                                 'distance_outgroup':3,'distance_within_cluster':1,
                                 'covariances_m2_to_m5':[frac(z) for z in example]},
      'thresholds':small_contrast,
      'observations':'The finite checks corroborate separately proved identities and do not establish their infinite quantifiers.'
    }
    print(json.dumps(payload,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':main()
