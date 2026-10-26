from itertools import combinations
from math import comb

def rank(rows):
    pivots = {}
    for value in rows:
        while value:
            pos = value.bit_length() - 1
            if pos in pivots:
                value ^= pivots[pos]
            else:
                pivots[pos] = value
                break
    return len(pivots)

def check():
    cases=0
    for n in range(2,11):
        N=1<<n
        for d in range(1,n+1):
            c0=comb(n,d)&1
            c1=comb(n-1,d-1)&1
            c2=(comb(n-2,d-2)&1) if d>=2 else 0
            if not(c1 or c2):continue
            terms=[]
            for ix in combinations(range(n),d):
                v=0
                for i in ix:v|=1<<i
                terms.append(v)
            rows=[]
            for x in range(N):
                row=(1<<x) if c0 else 0
                for v in terms:row^=1<<(x^v)
                rows.append(row)
            observed=rank(rows)
            expected=N//2 if c1 else N//2-(1<<((n-1)//2))
            assert observed==expected,(n,d,c0,c1,c2,observed,expected)
            cases+=1
    print('VERIFY_OK', 'all_eligible_hamming_shells_n_2_to_10=',cases)
if __name__=='__main__':check()
