"""Finite corroboration of the universal 2/3 weird-number abundance bound.
Run: python3 verify.py. Standard Python 3 only.
"""
from bisect import bisect_right

def primes_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[:2] = b'\x00\x00'
    for z in range(2, int(n**0.5) + 1):
        if sieve[z]: sieve[z*z:n+1:z] = b'\x00' * ((n-z*z)//z+1)
    return [z for z in range(n+1) if sieve[z]]

def witness(M, p, q, a):
    # Represents a with pairwise-distinct proper divisor blocks.
    for t in range(min(M, a//q) + 1):
        u = a - t*q
        s,r = divmod(u,p)
        if 0 <= s <= M and r <= M:
            return (r,s,t)
    return None

def main():
    ref=(1,1,5,3,10,23,29,53)
    Ms=[(1 << (k+1))-1 for k in range(1,9)]
    P=primes_upto(max(M*(M+1)//2+1 for M in Ms))
    candidate_pairs=0
    for k,(M,expect) in enumerate(zip(Ms,ref),start=1):
        weird=[]
        for p in P:
            if p <= M: continue
            if p >= 2*M: break
            x=p-M
            qmax=(M*(p+1)-M-1)//x
            if qmax <=p: continue
            lo=bisect_right(P,p)
            hi=bisect_right(P,qmax)
            for q in P[lo:hi]:
                a=M*(p+1)-x*q
                if a<=M: continue
                candidate_pairs+=1
                w=witness(M,p,q,a)
                if w is None:
                    weird.append((p,q,a))
                    assert 3*a < 2*M*M+3*M, (k,p,q,a)
                    assert q>2*M, (k,p,q,a)
                else:
                    r,s,t=w
                    assert a==r+s*p+t*q and 0<=r<=M and 0<=s<=M and 0<=t<=M
        assert len(weird)==expect,(k,len(weird),expect)
        print('k=%d weird=%d max_abundance=%d'%(k,len(weird),max(a for p,q,a in weird)))
    print('VERIFY_OK candidate_pairs=%d published_counts=%s'%(candidate_pairs,ref))

if __name__ == '__main__':main()
