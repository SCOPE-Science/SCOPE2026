"""Finite checks of subsequence-covering threshold and extremal word patterns.
No external packages; not a substitute for the uniform proof.
"""
from itertools import product,combinations
from math import comb
import sys


def words(m):
    return (''.join(x) for x in product('01',repeat=m))


def max_avoiding_subsequence(z, y):
    """Longest subsequence of z whose greedy matched prefix of y is proper."""
    m=len(y)
    dp=[-10**9]*m
    dp[0]=0
    for c in z:
        nxt=dp[:]
        for j,x in enumerate(dp):
            k=j+(c==y[j])
            if k<m and x+1>nxt[k]:
                nxt[k]=x+1
        dp=nxt
    return max(dp)


def subsequence(y,x):
    j=0
    for c in x:
        if j<len(y) and y[j]==c:
            j+=1
    return j==len(y)


def classify_dp(R,m):
    n=R+m;N=m+2*R
    outcomes={}
    for y in words(m):
        bad=None
        for z in words(N):
            if max_avoiding_subsequence(z,y)<n:
                bad=z
                break
        outcomes[y]=bad is None
    return outcomes


def classify_brute(R,m):
    n=R+m;N=m+2*R
    keep_masks=list(combinations(range(N),n))
    outcomes={}
    for y in words(m):
        witness_exists=False
        for z in words(N):
            if all(subsequence(y, ''.join(z[i] for i in keep)) for keep in keep_masks):
                witness_exists=True
                break
        outcomes[y]=not witness_exists
    return outcomes


def template(y,R):
    s=y
    if s == '0000':return '0'*(2*R+4)
    if s == '0001':return '0'*(R+3)+'1'*(R+1)
    if s == '0010':return '00'+'10'*(R+1)
    if s == '0011':return '0'*(R+2)+'1'*(R+2)
    if s == '0101':return '01'*(R+2)
    if s == '000':return '0'*(2*R+3)
    if s == '001':return '0'*(R+2)+'1'*(R+1)
    if s == '010':return '01'*(R+1)+'0'
    if s == '00':return '0'*(2*R+2)
    if s == '01':return '01'*(R+1)
    if s == '0':return '0'*(2*R+1)
    raise ValueError(s)


def symmetry_orbit(y):
    comp=lambda z:''.join('1' if c=='0' else '0' for c in z)
    return {y,y[::-1],comp(y),comp(y[::-1])}


def test():
    for R in range(1,6):
        for m in range(1,5):
            got=classify_dp(R,m)
            expected={'0110','1001'} if m==4 else set()
            positive={y for y,works in got.items() if works}
            assert positive==expected,(R,m,positive,expected)
            if R<=3:
                assert classify_brute(R,m)==got,(R,m)
            print('R',R,'m',m,'positive',','.join(sorted(positive)) or '-',flush=True)
    reps={1:['0'],2:['00','01'],3:['000','001','010'],4:['0000','0001','0010','0011','0101']}
    for R in range(1,51):
        for m,patterns in reps.items():
            for y in patterns:
                z=template(y,R)
                assert len(z)==m+2*R
                assert max_avoiding_subsequence(z,y)<m+R,(R,m,y,z)
    print('ALL_SYMBOLIC_TEMPLATES_DP_OK_R_1_TO_50',flush=True)
    for R in range(1,8):
        n=R+4
        for y in ('0110','1001'):
            actual=sum(not subsequence(y,x) for x in words(n))
            expected=sum(comb(n,j) for j in range(4))
            assert actual==expected,(R,y,actual,expected)
            # Every other 4-word is deletion-covered by the maximal family.
            for v in words(4):
                if v!=y:
                    assert any(subsequence(v,x) and not subsequence(y,x) for x in words(n))
        print('maximal_family_check_R',R,'size',sum(comb(n,j) for j in range(4)),flush=True)
    print('VERIFY_OK')

if __name__=='__main__':test()
