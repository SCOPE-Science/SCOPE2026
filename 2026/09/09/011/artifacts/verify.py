#!/usr/bin/env python3
"""Independent replay verifier for lane-290 Dawson's Kayles durations 0..120.

Rule (Dawson's Kayles, octal .07): a move on a heap of size n>=2 chooses a
bowled pair and removes its immediate neighbours from play, leaving two
heaps (a, b) with a+b = n-2, a,b >= 0. Heaps 0,1 are terminal (no moves).
Total game length = number of moves to all-terminal. Then:
  L(n) = 0 for n<2; L(n) = 1 + max_{a+b=n-2} (L(a)+L(b))
  S(n) = 0 for n<2; S(n) = 1 + min_{a+b=n-2} (S(a)+S(b))
Also cross-checks Grundy prefix against OEIS A002187 values.

Usage: python3 verify.py  (run from its own directory; writes dawsdon csv)
Stdlib only. Pass = prints VERIFY_OK.
"""
import os

N = 120
HERE = os.path.dirname(os.path.abspath(__file__))

def compute():
    L = [0]*(N+1); S = [0]*(N+1)
    aL = [None]*(N+1); aS = [None]*(N+1)
    for n in range(2, N+1):
        bL = max((L[a]+L[n-2-a], a) for a in range(n-1))
        bS = min((S[a]+S[n-2-a], a) for a in range(n-1))
        L[n] = 1+bL[0]; aL[n] = (bL[1], n-2-bL[1])
        S[n] = 1+bS[0]; aS[n] = (bS[1], n-2-bS[1])
    return L, S, aL, aS

def argS_rule(n):
    if n < 2: return None
    if n % 3 == 1 and n >= 4: return (1, n-3)
    return (0, n-2)

def main():
    L, S, aL, aS = compute()
    # 1. closed forms
    for n in range(N+1):
        assert L[n] == n//2, (n, L[n])
        assert S[n] == (n+1)//3, (n, S[n])
    # 2. recurrence replay from logged-style witnesses
    for n in range(2, N+1):
        assert L[n] == 1+L[0]+L[n-2], n                      # argmax (0,n-2)
        a, b = argS_rule(n)
        assert S[n] == 1+S[a]+S[b], (n, a, b)                # argmin rule
        # full max/min agreement (no better split exists)
        assert L[n] == 1+max(L[a]+L[n-2-a] for a in range(n-1)), n
        assert S[n] == 1+min(S[a]+S[n-2-a] for a in range(n-1)), n
    # 3. extremal heaps
    assert max(L) == 60 and [n for n in range(N+1) if L[n]==60] == [120]
    assert max(S) == 40 and [n for n in range(N+1) if S[n]==40] == [119,120]
    # 4. maximal line 120 -> 118 -> ... -> 0 (60 moves)
    n, c = 120, 0
    while n >= 2:
        assert L[n] == 1+L[0]+L[n-2]
        n -= 2; c += 1
    assert (c, n) == (60, 0)
    # 5. minimal line from 120 via argS rule (40 moves)
    stack, moves = [120], 0
    while stack:
        k = stack.pop()
        if k < 2: continue
        a, b = argS_rule(k)
        assert S[k] == 1+S[a]+S[b]
        moves += 1; stack.extend([a, b])
    assert moves == 40, moves
    # 6. Grundy prefix cross-check (rule sanity) vs OEIS A002187 first 32 terms
    G = [0]*(N+1)
    for n in range(N+1):
        if n >= 2:
            r = set(G[a]^G[n-2-a] for a in range(n-1))
            g = 0
            while g in r: g += 1
            G[n] = g
    assert G[:32] == [0,0,1,1,2,0,3,1,1,0,3,3,2,2,4,0,5,2,2,3,3,0,1,1,3,0,2,1,1,0,4,5], G[:32]
    # 7. write certified table csv
    with open(os.path.join(HERE, "dawson_durations_0_120.csv"), "w") as f:
        f.write("n,S,L,argS_a,argS_b,argL_a,argL_b\n")
        for n in range(N+1):
            if n < 2: f.write("%d,%d,%d,,,\n" % (n, S[n], L[n]))
            else:
                a, b = argS_rule(n)
                f.write("%d,%d,%d,%d,%d,0,%d\n" % (n, S[n], L[n], a, b, n-2))
    print("VERIFY_OK: L(n)=floor(n/2), S(n)=floor((n+1)/3), maxL=60@120, maxS=40@{119,120}")

if __name__ == "__main__":
    main()
