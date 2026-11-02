"""Exact, standalone finite checks for the superfactorial three-square theorem.

Usage: python3 verify.py
Standard library only. These checks certify the stated finite matrix identity;
the universal mathematical deductions are supplied in RESULT.md.
"""

from collections import deque


def popcount(n):
    return n.bit_count()


def digit_codes(m):
    bits = [(m >> i) & 1 for i in range(m.bit_length() + 3)]
    a = (sum(bits[2:]) + sum(bits[i] * bits[i+1] for i in range(len(bits)-1))) % 2
    b = (sum(bits[i] * bits[i+1] for i in range(1,len(bits)-1))
         + sum(bits[i] * bits[i+2] for i in range(len(bits)-2))) % 2
    return a,b


def digit_obstruction(n):
    if n & 1:
        return n % 8 == 5
    m = n//2
    a,b = digit_codes(m)
    return popcount(m)%2 == 0 and a == 1 and b == 1


def states():
    return [(r,p,u) for r in range(4) for p in range(2) for u in (1,3,5,7)]


state_list = states()
index = {s:i for i,s in enumerate(state_list)}
O = (1,1,3,7)


def transition(s,d):
    r,p,u=s
    return ((2*r+d)%4, p^d, u * O[r] * (2*r+1 if d else 1)%8)


def make_matrix():
    a=[[0]*32 for _ in range(32)]
    for i,s in enumerate(state_list):
        for d in range(2):
            a[i][index[transition(s,d)]]+=1
    return a


def multiply(a,b):
    rows=len(a)
    n=len(b)
    cols=len(b[0])
    bt = list(zip(*b))
    return [[sum(x*y for x,y in zip(row,col)) for col in bt] for row in a]


def polynomial_times(p,q):
    z=[0]*(len(p)+len(q)-1)
    for i,v in enumerate(p):
        for j,w in enumerate(q):
            z[i+j]+=v*w
    return z


def annihilator():
    p=[1]
    for fac in ([0,0,0,1],[-2,1],[-2,0,1],[2,0,1],
                [2,-2,1],[4,0,-2,0,1],[4,-4,2,-2,1]):
        p=polynomial_times(p,fac)
    return p


def check_matrix():
    M=make_matrix()
    assert all(sum(row)==2 for row in M)
    assert all(sum(M[i][j] for i in range(32))==2 for j in range(32))
    start=index[(0,0,1)]
    assert M[start][start]>=1
    for reverse in (False,True):
        seen={start}; q=deque([start])
        while q:
            v=q.popleft()
            for w in range(32):
                c=M[w][v] if reverse else M[v][w]
                if c and w not in seen:
                    seen.add(w);q.append(w)
        assert len(seen)==32
    P=annihilator()
    ident=[[int(i==j) for j in range(32)] for i in range(32)]
    R=[[P[-1]*int(i==j) for j in range(32)] for i in range(32)]
    for c in reversed(P[:-1]):
        R=multiply(R,M)
        for i in range(32):R[i][i]+=c
    assert all(v==0 for row in R for v in row)
    # Check the 32-state automaton exactly reproduces the bit conditions.
    for m in range(1<<14):
        state=(0,0,1)
        for d in map(int,bin(m)[2:]):
            state=transition(state,d)
        a,b=digit_codes(m)
        assert state[0]==m%4
        assert state[1]==popcount(m)%2
        assert state[2]==pow(3,a,8)*pow(5,b,8)%8
    # Prove the exact sharp-error subsequence by Cayley--Hamilton.  For
    # T=M^8, the discrepancy between e_0 M^4 T^j times the acceptance
    # vector and 2*256^j+16^j is an output of a 34-dimensional linear
    # system (a block sum of T with scalar blocks 256 and 16).  Its first
    # 34 zero values force it to vanish at every j>=0.
    start_row=[0]*32
    start_row[index[(0,0,1)]]=1
    row=start_row[:]
    for _ in range(4):
        row=[sum(row[i]*M[i][j] for i in range(32)) for j in range(32)]
    T=[[int(i==j) for j in range(32)] for i in range(32)]
    for _ in range(8):
        T=multiply(T,M)
    for j in range(34):
        count=sum(row[i] for i,s in enumerate(state_list)
                  if s[1]==0 and s[2]==7)
        assert count == 2*256**j + 16**j,(j,count)
        row=[sum(row[i]*T[i][t] for i in range(32)) for t in range(32)]
    expected={3:1,4:3,5:4,6:8,7:16,8:36,10:128,12:528}
    for k,c in expected.items():
        count=sum(popcount(m)%2==0 and digit_codes(m)==(1,1) for m in range(1<<k))
        assert count==c,(k,count,c)
    return len(P)-1, sum(1 for x in M for y in x if y), len(state_list)


def check_arithmetic():
    # Compute the superfactorial valuation and odd unit independently via
    # the identity S(n)=S(n-1)*n!, keeping only the 2-adic data.
    factorial_v2=0
    factorial_odd=1
    super_v2=0
    super_odd=1
    hits=[]
    for n in range(4097):
        if n:
            v=(n & -n).bit_length()-1
            factorial_v2+=v
            factorial_odd=(factorial_odd*(n>>v))%8
            super_v2+=factorial_v2
            super_odd=(super_odd*factorial_odd)%8
        actual=(super_v2%2==0 and super_odd==7)
        expected=digit_obstruction(n)
        assert actual==expected,(n,super_v2,super_odd,actual,expected)
        if actual:hits.append(n)
    assert hits[:12]==[5,10,13,20,21,24,29,37,45,48,53,61],hits[:12]
    return len(hits)


def main():
    degree,nonzero,states=check_matrix()
    hits=check_arithmetic()
    print(f'VERIFY_OK states={states} matrix_nonzero_entries={nonzero} '
          f'annihilator_degree={degree} dyadic_Cayley_Hamilton_terms=34 checked_arithmetic_n=4097 '
          f'obstructions_in_range={hits} digit_cases=16384')


if __name__=='__main__':
    main()
