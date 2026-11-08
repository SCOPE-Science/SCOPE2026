# Independent mathematical audit

## correctness

PASS

Every two-input Boolean function is an arbitrary 2×2 Boolean allowed-relation matrix, uniformly one of 16. Cyclic consistency is equivalent to a nonzero diagonal in the Boolean matrix product of n edge relations. Row/column permutations divide 16 relations into seven orbit types with representatives 0,1,3,5,6,7,15, and enumerating each of 16 right factors yields exactly the stated 7×7 integer T. The final accept vector has g_i=16−2^(4−w_i), w_i allowed pairs, and identity mask 9 falls into orbit rep 6. Direct exact integer verification of the polynomial annihilator (T−4I)(T−2I)(T²−17T+48I)g=0 proves all-n fourth-order recurrence; starting counts N1=12,N2=175,N3=2397,N4=32377 yield N_n=U_n−4^n−2^(n−1), U_n=17U_(n−1)−48U_(n−2). Direct independent exhaustive enumeration of 16^3=4096 and 16^4=65536 edge-table systems confirms N3=2397,N4=32377; separate orbit and annihilator reconstruction confirms unrestricted n by recurrence. Horak–Semaev's published Conjecture 20 instead predicts N3=2337; its different negative term is refuted, with general probability gap 15/(2·8^n). This relies on labelled simple cycles n>=3 and truly uniform truth tables; no finite experiment is substituted for exact annihilator identity.

## originality

PASS

Best-of-knowledge qualified: the final statement is not shown to be equivalent to, an implication of, or covered by the materially inspected prior primary statements. General background and known subcases are credited explicitly; inaccessible plausible primary literature is a documented priority risk, not automatic scientific failure.

## value

PASS

A mathematically natural exact correction to a recent explicit conjecture for independent random binary constraints on cycles. It supplies a closed all-length sequence, a seven-orbit Boolean-semigroup transfer and rigorous counterexample, not a tiny isolated numerical discrepancy; the recurrence has independent use in random CSP consistency probabilities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
