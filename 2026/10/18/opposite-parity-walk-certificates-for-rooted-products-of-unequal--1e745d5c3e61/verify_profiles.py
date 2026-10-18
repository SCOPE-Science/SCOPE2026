"""Arithmetic injectivity of distance, geodesic count, and opposite-parity defect."""
from math import comb


def check():
    cases=profiles=0
    for m in range(5,202,2):
        for n in range(m+2,204,2):
            seen={}
            for a in range((m+1)//2):
                for b in range((n+1)//2):
                    d=a+b
                    sig=(d,comb(d,a),min(m-2*a,n-2*b))
                    assert sig not in seen, (m,n,seen.get(sig),(a,b),sig)
                    seen[sig]=(a,b)
            cases+=1;profiles+=len(seen)
    print(f'PROFILE_PASS cases={cases} distinct_profiles={profiles}')


if __name__=='__main__':
    check()
