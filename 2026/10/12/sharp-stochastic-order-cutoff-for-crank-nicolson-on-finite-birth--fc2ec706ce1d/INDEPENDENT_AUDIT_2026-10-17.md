# Independent mathematical audit

## correctness

PASS

A direct symbolic adjacent-row subtraction establishes DQ=HD, and D maps all n-state functions onto all (n-1)-edge gradients. Rational functional calculus gives DT_h=(2R_h-I)D. Irreducible Metzler edge matrix H has a strictly positive resolvent for h>0, and is diagonally similar to a symmetric negative-definite matrix because its spectrum consists of the nonzero eigenvalues of irreducible reversible Q. Each R_h diagonal is sum_j u_ij^2/(1+h nu_j/2), strictly decreasing from one to zero. Thus all increasing gradients are preserved iff every diagonal is >=1/2, each has a unique crossing, proving exact all-rate cutoff. Direct 2x2 inversion yields displayed three-state expression. Independent Sympy exact arithmetic recreated both Q1 and Q2 CN transition matrices, both edge propagators, cutoff 2/sqrt3 and 2/sqrt7, and exact opposite ordering/nonnegative-entry witnesses. This algebraic check supports but does not replace all-dimension spectral proof.

## originality

PASS

The gradient intertwining is established in Chafaï–Joulin and the Q-resolvent CN Markov positivity frontier is previously available as a different Resultary theorem. The new boundary uses the killed edge generator H to characterize preservation of the increasing-function cone and gives exact opposite three-state separations, which are not implied by the Q-positivity threshold alone. A general monotonicity-preserving rational integrator theorem might contain the same test; that literature priority risk is noted.

## value

PASS

For ordered Markov chains, preserving order between initial-state distributions is a distinct physical and numerical requirement from keeping rows stochastic. The theorem gives an exact sharp stability frontier across every finite nonuniform birth–death generator, not a methodwide sufficient CFL heuristic; the two opposing three-state examples show why checking one property cannot substitute for the other. Both are naturally needed to select safe numerical time steps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
