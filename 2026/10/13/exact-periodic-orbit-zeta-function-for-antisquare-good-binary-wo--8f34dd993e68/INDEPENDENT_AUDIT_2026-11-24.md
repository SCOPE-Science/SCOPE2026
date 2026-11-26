# Independent mathematical audit

## correctness

PASS

Baranwal et al. Proposition 18 excludes 001011 from periodic good points (an occurrence forces the nonperiodic exceptional configuration); complementation excludes 110100. The proof of their Theorem 19 supplies the exact remaining finite forbidden set F and its equivalent difference windows G. The local equivalence works for periodic windows even at lengths shorter than the forbidden words. Each allowed cyclic difference code is all zero or has one-runs of length two or four separated by at least two zeros; the all-one code is forbidden. Its parity is even, so integration by XOR gives exactly two complementary origin-marked periodic lifts. The independently reconstructed ten-state code graph has det(I-zA)=1-z-z^4-z^6 by exact signed-subset determinant and agrees with exhaustive cyclic counts through n=12. Alternatively, independently count codes with k>0 one-runs by marking a run start. Each length-n code can be marked in k ways, and there are n coordinate choices for the mark followed by k blocks of generating function W=(z^4+z^6)/(1-z). Thus nonconstant codes contribute sum_{k>=1} W^k/k to sum C_n z^n/n, and all-zero codes contribute -log(1-z). This gives -log(1-z-z^4-z^6), and the two lifts square the zeta denominator. Formal logarithmic differentiation and inversion of P_n=sum_{d|n}d O_d give the stated enumerators. The first 16 counts agree. Only zero difference codes occur at lengths 1–3, and 11 followed by n-2 zeros has least period n for n>=4 (one cyclic one-run start); a lift's period would also be a period of its differences. This proves the claimed least periods for all n. Replay: the frozen verify.py and certificate.json specify the finite graph/count checks; the independent computation constructed the length-four graph directly from G and used a signed-subset determinant rather than Newton identities. The separate F-matrix certificate was inspected, not required for the all-n proof above.

## originality

PASS

Credit the published finite forbidden sets, exceptional-point result, Pansiot runs and the characteristic polynomial. The distinct checked result is the all-period periodic-point zeta with the two-lift normalization and the complete least-period set. Exact and refined reappearances in later-dated indexed findings are material overlaps, but the inspected evidence does not establish that they were prior to this finding.

## value

PASS

Marked periodic points and primitive periods are natural invariants of this two-sided avoidance shift. The exact rational zeta and least-period support answer questions the finite-word growth rate alone cannot answer: which orbit lengths occur and how many marked or primitive orbits there are at every length. The cyclic lifting multiplicity and the separation of exceptional nonperiodic words make the calculation specific to this shift, rather than a restatement of its published growth polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
