"""Independent bit-vector matrix checks for synchronous neighbor-parity dynamics.
No external packages required. This is finite corroboration, not an all-size proof.
"""

def make_rows(p, q):
    n = 1 + 2*p + 4*q
    rows = [0] * n
    at = 1
    for length, count in ((3,p), (5,q)):
        for _ in range(count):
            vs = [0] + list(range(at,at+length-1))
            at += length-1
            for u,v in zip(vs,vs[1:]+vs[:1]):
                rows[u] ^= 1 << v
                rows[v] ^= 1 << u
    assert at==n
    return rows

def mul_rows(left, right):
    ans=[]
    for mask in left:
        y=0
        while mask:
            lsb=mask&-mask
            y ^= right[lsb.bit_length()-1]
            mask ^= lsb
        ans.append(y)
    return ans

def rank(rows):
    pivot={}
    for row in rows:
        while row:
            k=row.bit_length()-1
            if k not in pivot:
                pivot[k]=row
                break
            row ^= pivot[k]
    return len(pivot)

def run():
    n_tests=0
    max_n=0
    for p in range(13):
        for q in range(13):
            if p+q == 0:continue
            a=make_rows(p,q)
            n=len(a)
            max_n=max(max_n,n)
            identity=[1<<i for i in range(n)]
            assert rank(a)==n-1, (p,q,'rank A')
            power=identity
            ranks={}
            for t in range(1,8):
                power=mul_rows(power,a)
                if t in (1,2,3,6):
                    ranks[t]=n-rank([x^y for x,y in zip(power,identity)])
                if t==7:
                    assert power==a, (p,q,'A^7=A')
            expected={
                1:p+(p%2), 2:2*p,
                3:p+2*q+(p%2)+2*(q%2),
                6:2*p+4*q,
            }
            assert ranks==expected, (p,q,ranks,expected)
            n_tests+=1
    print('RANK_CHECK_OK: {} parameter pairs, 1 <= n <= {}, p,q <= 12,'.format(n_tests,max_n))
    print('    matrix identities A^7=A, rank A=n-1 and four fixed-space dimensions checked.')

if __name__=='__main__':run()
