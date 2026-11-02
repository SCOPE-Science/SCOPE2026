"""Direct finite-field checks of three-block nilradical commuting-tuple counts.

No external dependencies. GF(4) uses the irreducible polynomial u^2+u+1.
"""
from itertools import product


def add(a, b, q):
    return a ^ b if q == 4 else (a + b) % q


def sub(a, b, q):
    return a ^ b if q == 4 else (a - b) % q


def mul(a, b, q):
    if q != 4:
        return a * b % q
    v = 0
    for _ in range(2):
        if b & 1:
            v ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7
    return v


def inv(a, q):
    for b in range(1, q):
        if mul(a,b,q) == 1:
            return b
    raise ValueError


def rank(mat, q):
    m = [list(x) for x in mat]
    if not m:
        return 0
    n = len(m[0]); h = len(m); row=0
    for col in range(n):
        pivot = next((i for i in range(row,h) if m[i][col]),None)
        if pivot is None: continue
        m[row],m[pivot]=m[pivot],m[row]
        s=inv(m[row][col],q)
        for j in range(col,n):m[row][j]=mul(m[row][j],s,q)
        for i in range(h):
            if i==row or m[i][col]==0:continue
            f=m[i][col]
            for j in range(col,n):m[i][j]=sub(m[i][j],mul(f,m[row][j],q),q)
        row+=1
        if row==h:break
    return row


def rank_matrices(m,r,q):
    out=[0]*(min(m,r)+1)
    for v in product(range(q),repeat=m*r):
        a=[v[i*r:(i+1)*r] for i in range(m)]
        out[rank(a,q)]+=1
    return out


def closed_rank_count(m,r,d,q):
    numerator=1; denominator=1
    for i in range(d):
        numerator *= (q**m-q**i)*(q**r-q**i)
        denominator *= (q**d-q**i)
    assert numerator % denominator == 0
    return numerator//denominator


def predicted(m,r,c,q):
    return q**(c*m)*sum(
        closed_rank_count(m,r,d,q)*q**(c*(m*(r-d)+d*(d+1)//2))
        for d in range(min(m,r)+1))


def direct(m,r,c,q):
    count=0
    for avec in product(range(q),repeat=m*r):
        A=[avec[i*r:(i+1)*r] for i in range(m)]
        for bvec in product(range(q),repeat=m*r*c):
            B=[bvec[i*r*c:(i+1)*r*c] for i in range(m)]
            valid=True
            for i in range(m):
                for j in range(i):
                    for k in range(c):
                        left=0;right=0
                        for h in range(r):
                            left=add(left,mul(A[i][h],B[j][h*c+k],q),q)
                            right=add(right,mul(A[j][h],B[i][h*c+k],q),q)
                        if left != right:
                            valid=False; break
                    if not valid:break
                if not valid:break
            if valid:count+=1
    return count*q**(c*m)


def main():
    tests=[(0,2,2,2),(1,2,2,2),(2,1,2,2),(2,2,1,2),(2,2,2,2),
           (3,2,1,2),(2,3,1,2),(2,2,1,3),(2,1,2,3),(2,2,1,4)]
    for m,r,c,q in tests:
        assert rank_matrices(m,r,q)==[closed_rank_count(m,r,d,q) for d in range(min(m,r)+1)]
        actual=direct(m,r,c,q)
        expected=predicted(m,r,c,q)
        assert actual==expected,(m,r,c,q,actual,expected)
        print('PASS',f'q={q},m={m},r={r},c={c}: {actual}')
    print('THREE_BLOCK_RANK_STRATIFIED_COMMUTING_OK',len(tests))

if __name__=='__main__':main()
