"""Cross-check: Fraction Gaussian elimination (I-Q)^{-1}1 vs recursion; tie census for top values."""
from fractions import Fraction

p0_opts = [(Fraction(1,4),Fraction(3,4)),(Fraction(1,2),Fraction(1,2)),(Fraction(3,4),Fraction(1,4)),(Fraction(1,1),Fraction(0,1))]
interior = [
 (Fraction(1,4),Fraction(1,4),Fraction(1,2)),
 (Fraction(1,4),Fraction(1,2),Fraction(1,4)),
 (Fraction(1,4),Fraction(3,4),Fraction(0,1)),
 (Fraction(1,2),Fraction(1,4),Fraction(1,4)),
 (Fraction(1,2),Fraction(1,2),Fraction(0,1)),
 (Fraction(3,4),Fraction(1,4),Fraction(0,1)),
]
p0f=[Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1,1)]

def H_recur(i0, js):
    p_list=[p0f[i0]]+[interior[j][0] for j in js]
    q_list=[Fraction(0,1)]+[interior[j][1] for j in js]
    d=Fraction(1,1)/p_list[0]; tot=d
    for i in range(1,7):
        d=(Fraction(1,1)+q_list[i]*d)/p_list[i]
        tot+=d
    return tot

def H_gauss(i0, js):
    # Build A=(I-Q) 7x7 Fractions, b=ones; solve via Gauss-Jordan
    p_list=[p0f[i0]]+[interior[j][0] for j in js]
    q_list=[Fraction(0,1)]+[interior[j][1] for j in js]
    r_list=[p0_opts[i0][1]]+[interior[j][2] for j in js]
    n=7
    A=[[Fraction(0,1)]*(n+1) for _ in range(n)]
    for r in range(n):
        A[r][r]=Fraction(1,1)-r_list[r]
        if r<6: A[r][r+1]=-p_list[r]
        if r>0: A[r][r-1]=-q_list[r]
        A[r][n]=Fraction(1,1)
    # elimination
    for col in range(n):
        piv=None
        for row in range(col,n):
            if A[row][col]!=0:
                piv=row; break
        assert piv is not None
        A[col],A[piv]=A[piv],A[col]
        pv=A[col][col]
        for k in range(col,n+1): A[col][k]/=pv
        for row in range(n):
            if row!=col and A[row][col]!=0:
                f=A[row][col]
                for k in range(col,n+1): A[row][k]-=f*A[col][k]
    return A[0][n]

# Canonical + top-5 representatives from exact_census
reps = {
 "H*=6544": (0,(2,2,2,2,2,2)),
 "2nd 5088": (0,(1,2,2,2,2,2)),
 "3rd 4608": (0,(2,1,2,2,2,2)),
 "4th 4464": (0,(2,2,1,2,2,2)),
 "5th 4358": (1,(2,2,2,2,2,2)),
}
for name,(i0,js) in reps.items():
    hr=H_recur(i0,js); hg=H_gauss(i0,js)
    print(f"{name}: recur={hr} gauss={hg} match={hr==hg} float={float(hr)}")

# Tie census: count patterns per top value (rows0..6 level), then x4 for q7
from collections import Counter
# Re-run quick count using recursion values for top-5 only (avoid storing all)
targets=[Fraction(6544,1),Fraction(5088,1),Fraction(4608,1),Fraction(4464,1),Fraction(4358,1)]
cnt=Counter()
for i0 in range(4):
    for i1 in range(6):
        for i2 in range(6):
            for i3 in range(6):
                for i4 in range(6):
                    for i5 in range(6):
                        for i6 in range(6):
                            js=(i1,i2,i3,i4,i5,i6)
                            H=H_recur(i0,js)
                            if H in targets:
                                cnt[H]+=1
print("pattern counts (rows0..6) for top values:", dict(cnt))
print("full-chain counts (x4 q7):", {str(k):v*4 for k,v in cnt.items()})
# Check aperiodicity of all max full chains: max pattern has r0=3/4 so all 4 aperiodic
# Also verify no periodic chain exceeds: max over periodic patterns
maxper=Fraction(-1,1)
for i1 in [2,4,5]:
    for i2 in [2,4,5]:
        for i3 in [2,4,5]:
            for i4 in [2,4,5]:
                for i5 in [2,4,5]:
                    for i6 in [2,4,5]:
                        H=H_recur(3,(i1,i2,i3,i4,i5,i6))
                        if H>maxper: maxper=H
print("max over periodic rows0..6 patterns (p0=1, interior r=0):", maxper, float(maxper))
