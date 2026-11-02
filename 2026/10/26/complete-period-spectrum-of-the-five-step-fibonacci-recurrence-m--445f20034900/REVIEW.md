# Independent mathematical audit

## correctness

PASS

The final claim concerns all five-coordinate initial vectors modulo 2^k, every k>=1, and counts least-period cycles, not just primitive starting states. Directly rebuilt the 5x5 companion matrix and independently computed exact integer Smith normal forms: M-I valuations (0,0,0,0,2), M^3-I (0,0,1,1,2), (M^6-I)/2 and (M^12-I)/4 each (0,0,0,0,2). Exhaustively enumerated all 2^(5k) states for k=1,2,3: cycle histograms respectively {1:2,3:2,6:4}, {1:4,3:4,6:8,12:80}, and {1:4,2:2,3:4,6:18,12:160,24:1280}. The proof supplies the missing infinite step: Hensel lifting gives unique 2-adic eigenvalue alpha congruent 1 modulo 2 and v2(alpha-1)=2; the other rank-four factor has unit 2-power differences; scaling U_j=(M^(3*2^j)-I)/2^j has U_(j+1)=U_j(I+2^(j-1)U_j), hence Smith invariants stabilize from j>=2. Fixed-point inclusion/exclusion gives the exact least periods and the claimed C(k)=(257*16^k+960*k+1408)/720 for k>=2. The finite checks confirm finite Smith bases, not by themselves the all-k theorem.

## originality

PASS

The exact finite orbit totals 8,96,1468,23400,374292 are already tabulated in Noe 2005 OEIS A106287, and A106290 already lists the distinct orbit lengths, including six for modulus eight; none is newly discovered. The final claim is the complete multiplicity law at all 2-power levels and its all-k proof. Waddill 1996 broadly addresses higher-order recurrences modulo m, but only chapter abstract available; cannot assert it lacks equivalent multiplicity consequences. Searches of Resultary and primary sequences yielded no verified dominating published identity; best-of-knowledge originality is qualified by that priority risk.

## value

PASS

The natural full 2-adic orbit decomposition of a fixed canonical higher-order Fibonacci permutation is a useful exact dynamical invariant: it distinguishes individual cycle lengths and multiplicities rather than listing totals or extending a few table rows. The valuation/Smith mechanism controls every level uniformly. This would be an independently reusable all-k classification, not an arbitrary finite recomputation; significance is bounded to this specific recurrence and 2-power moduli.

The dated certificate retains the supplied scientific assessment, sources and limitations.
