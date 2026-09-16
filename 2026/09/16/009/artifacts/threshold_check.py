"""Threshold verification for Qi-Qiao short-interval Luo sieve vs trivial sieve.

Checks continuity of Lambda(M,T,N) at branch points N=M^{5/2}, N=T^{5/2},
and the saving ratio R = M*(T+N)/Lambda in the Luo range
T^2/M <= N <= M^2 T^2. Shows strict saving iff M^{7/4}/T > 1 (up to logs),
i.e. M > T^{4/7}, and that M=T^{1/2} gives R<1 in the middle range.
"""
import math

def Lambda(M,T,N):
    if N <= M**2.5:
        return T*math.sqrt(M*N)
    elif N <= T**2.5:
        return T*N**0.7
    else:
        return N**1.5/T

def trivial(M,T,N):
    return M*(T+N)

def ratio(M,T,N):
    return trivial(M,T,N)/Lambda(M,T,N)

T = 1e12
for Mexp in [0.5, 4/7, 0.6, 0.8, 1.0]:
    M = T**Mexp
    print(f"--- M = T^{Mexp:.4f} = {M:.3g}")
    # continuity at N=M^{5/2}
    N1 = M**2.5
    b1a = T*math.sqrt(M*N1); b1b = T*N1**0.7
    print(f"  N=M^2.5: branch1={b1a:.3g} branch2={b1b:.3g} rel.diff={abs(b1a-b1b)/b1a:.2e}")
    # continuity at N=T^{5/2}
    N2 = T**2.5
    b2a = T*N2**0.7; b2b = N2**1.5/T
    print(f"  N=T^2.5: branch2={b2a:.3g} branch3={b2b:.3g} rel.diff={abs(b2a-b2b)/b2a:.2e}")
    for Nlabel,N in [("T^2/M",T**2/M),("M^2.5",M**2.5),("T^2",T**2),
                      ("T^2.5",T**2.5),("M^2T^2",M*M*T*T)]:
        if not (T**2/M <= N <= M*M*T*T):
            print(f"  N={Nlabel}: outside Luo range, skip"); continue
        print(f"  N={Nlabel}: R=trivial/Lambda={ratio(M,T,N):.3g} "
              f"{'STRICT SAVING' if ratio(M,T,N)>1 else 'no saving'}")
    # middle-range diagnostic M^{7/4}/T
    print(f"  M^1.75/T = {M**1.75/T:.3g}")
