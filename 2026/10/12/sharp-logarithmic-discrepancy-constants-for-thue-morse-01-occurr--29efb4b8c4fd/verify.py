#!/usr/bin/env python3
from pathlib import Path
import json, math

def t(n):
    return n.bit_count() & 1

# Direct prefix discrepancy.  E_N = 3*A_N-N where A_N counts 01 starts < N.
LIMIT=4**9
E=[0]*(LIMIT+1)
for n in range(LIMIT):
    A01 = 1 if t(n)==0 and t(n+1)==1 else 0
    E[n+1]=E[n] + 3*A01 - 1

# Local four-block identities and global recurrences.
for n in range(LIMIT//4):
    q=t(n)
    a=[
        1 if t(4*n+r)==0 and t(4*n+r+1)==1 else 0
        for r in range(4)
    ]
    assert a[0]==1-q
    assert a[1]==0
    assert a[2]==q
    assert a[3]==(1 if t(n)==0 and t(n+1)==1 else 0)

    assert E[4*n]   == E[n]
    assert E[4*n+1] == E[n] + 2 - 3*q
    assert E[4*n+2] == E[n] + 1 - 3*q
    assert E[4*n+3] == E[n]

# A second evaluator reads base-4 digits from most significant to least,
# carrying only (E,t).  This uses the recurrence rather than prefix summation.
def E_fast(N):
    if N==0:
        return 0
    ds=[]
    x=N
    while x:
        ds.append(x%4)
        x//=4
    e=0
    q=0
    for r in reversed(ds):
        if r==0:
            pass
        elif r==1:
            e += 2-3*q
            q ^= 1
        elif r==2:
            e += 1-3*q
            q ^= 1
        else:
            pass
    return e

for N in range(LIMIT+1):
    assert E_fast(N)==E[N],(N,E_fast(N),E[N])

# Exact quartic prefix extrema and explicit witnesses.
extrema=[]
for k in range(1,10):
    B=4**k
    vals=E[:B]
    mx=max(vals); mn=min(vals)
    mx_expected=1+(k+1)//2
    mn_expected=-(k//2)
    assert mx==mx_expected,(k,mx,mx_expected)
    assert mn==mn_expected,(k,mn,mn_expected)

    if k%2:
        Nmax=(4**k-1)//3       # k base-4 digits, all 1
        Nmin=2*(4**(k-1)-1)//3 # leading 0, then k-1 digits all 2
    else:
        Nmax=(4**(k-1)-1)//3   # leading 0, then k-1 digits all 1
        Nmin=2*(4**k-1)//3     # k digits all 2
    assert E[Nmax]==mx
    assert E[Nmin]==mn
    extrema.append((k,Nmax,Nmin,mx,mn))

# Independently solve the two-state digit DP out to much larger depth.
# State q records the current Thue-Morse bit of the parsed base-4 prefix.
M=[0,0]
m=[0,0]
for k in range(1,101):
    oldM=M[:]; oldm=m[:]
    # For maximization, digit 1 is at least as good as digit 2 on a toggle.
    M=[
        max(oldM[0], 2+oldM[1]),
        max(oldM[1],-1+oldM[0])
    ]
    # For minimization, digit 2 is at most as good as digit 1 on a toggle.
    m=[
        min(oldm[0], 1+oldm[1]),
        min(oldm[1],-2+oldm[0])
    ]
    assert M[0]==1+(k+1)//2
    assert M[1]==k//2
    assert m[0]==-(k//2)
    assert m[1]==-(1+(k+1)//2)

cert=json.loads((Path(__file__).resolve().parent/"certificate.json").read_text(encoding="utf-8"))
assert cert["source_primary_msc"]=="68Q45"
assert cert["asymptotic_constants"]=={
    "limsup_D_over_log2N":"1/12",
    "liminf_D_over_log2N":"-1/12"
}

print(
    "VERIFY_OK "
    f"direct_prefix_N=0..{LIMIT} "
    f"four_block_n=0..{LIMIT//4-1} "
    "quartic_extrema_k=1..9 "
    "two_state_digit_DP_k=1..100 "
    "limsup=1/12 liminf=-1/12"
)
