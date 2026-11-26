# Independent mathematical audit

## correctness

PASS

Independent transfer calculation: let A_n and B_n be the signed expectations restricted to odd and even current last-packet length, respectively. Appending a card after a cut starts a new odd packet without changing sign. Without a cut, the sign flips exactly when the old last length was odd, since appending adds that many inversions to its reversal. Therefore A_{n+1}=p A_n+B_n, B_{n+1}=-q A_n, starting from (1,0). The transfer polynomial is r²-pr+q; the combined expectation at n=2 is p-q, compatible with epsilon_0=epsilon_1=1. The resulting formal series has numerator 1+qz and denominator 1-pz+qz². The discriminant vanishes once in (0,1), at 2(sqrt(2)-1); above it, 0<r_-<r_+<1 and (1-r_-)r_+^n>(1-r_+)r_-^n. At the repeated root r=sqrt(2)-1, the initial values give r^n(1+sqrt(2)n). Below the threshold the normalized expectation is a nonzero phased cosine for 0<theta<pi/2. An irrational orbit and each of its tails are dense and hit open arcs of both signs; at rational resonance the full-period sum is zero and the n=0 term is +1, so both signs recur infinitely often. Sign multiplicativity yields the exact all-pass parity law (at t=0 its power is 1), and parity projection gives the lower bound, not an equality claim, for full-deck TV. Global reversal has the stated deterministic sign. The fixed-p and n≥2 hypotheses matter, and the phase statement applies to in-place reversal without the physical correction. The proof is analytical; I inspected check.py but did not execute its finite tests.

## originality

PASS

The exact in-place sign-character sequence and its sharp deck-size sign dichotomy are distinct from the one-card spectrum or cutoff, the standard multiplicativity observation, and the close composition or covariance studies. No inspected earlier or same-day statement gives this evaluation or threshold. This is a bounded assessment; Pemantle's full paper could not be compared.

## value

PASS

Sign is a natural full-permutation observable not seen by a single-card projection. The result determines the exact parity bias for every fixed cut probability, deck size and pass count, and distinguishes all-size positivity from infinitely recurring biases in both directions. This gives a precise mode-specific contrast to full-deck mixing rather than a routine re-expression of the known cutoff or a claim that parity governs total mixing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
