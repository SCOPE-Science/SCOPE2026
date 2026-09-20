# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** For homogeneous data, the stabilized CN/AB update in the primary source reduces exactly to a positive scalar prefactor times the Adams–Bashforth nonlinear combination. With g(x)=x(1-x^2), the first post-starter increment is negative if and only if 3g(b)<g(a). The exact Allen–Cahn starter b(h) is strictly increasing from a to 1. Since g increases up to 1/sqrt(3) and then strictly decreases to zero, the level g(a)/3 is crossed exactly once on the decreasing branch. Solving the exact-flow relation at that state gives h*=(1/2)log(3b*^3/a^3). The cubic root formula is the standard trigonometric solution of b^3-b+a(1-a^2)/3=0, with the chosen branch lying in (1/sqrt(3),1).

The threshold comparison is exact: the source's sufficient dimensionless bound is (1/2)log(3/a^3), so its excess is -(3/2)log b*>0. The excess is maximal at a=1/sqrt(3), because g(a) is maximal there and the selected inverse branch of g is decreasing. Differentiating the crossing function gives E'(h*)=(g(a)/2)(3b*^2-1)>0, excluding a tangential crossing.

The generalized alpha>1 result follows from the same sign calculation with q=(alpha-1)/alpha: the relevant level is qg(a), it is crossed uniquely on the decreasing branch, and substitution into the exact-flow identity yields h_q=(1/2)log(b_q^3/(q a^3)). Its near-equilibrium and small-a asymptotics follow from g(1-delta)=2delta+O(delta^2) and b_q->1. The standalone verification artifact checks the formulas and sign changes numerically for representative values without replacing the analytic proof.

For the active-diffusion corollary, the primary source's perturbation proof uses only a strict homogeneous sign margin together with continuous dependence of the exact starter and elliptic update. Replacing its conservative sufficient condition by any finite tau on either strict side of the exact homogeneous crossing is therefore valid. The record does not claim a universal threshold for arbitrary nonhomogeneous data.

## Originality

**PASS, to the best of our knowledge.** The full relevant portion of arXiv:2609.19023 was inspected. Its Theorem 4.11 derives the same homogeneous recurrence and exact starter, then bounds the ratio of cubic reaction terms to obtain the sufficient condition tau>(epsilon^2/2)log(3/a^3). It does not solve the exact level-crossing equation, state an if-and-only-if threshold, give the closed-form root, quantify the exact gap, or formulate the general over-extrapolation law. Its Proposition 5.2 proves persistence under nonhomogeneous perturbations only after imposing the sufficient threshold from Theorem 4.11, although its continuity argument applies whenever the homogeneous sign is strict.

The 2013 Feng–Tang–Yang paper was checked for the original stabilized CN/AB scheme and concerns energy stability and error estimates rather than this pointwise-reversal onset. Li–Wang's earlier asymptotic-stability paper studies critical step sizes and monotonicity for several other Allen–Cahn ODE discretizations, including standard Crank–Nicolson and modified Crank–Nicolson, but not the exact-starter stabilized CN/AB level-crossing result here. Searches combining Allen–Cahn, stabilized CN/AB, pointwise monotonicity, critical/exact threshold, Adams–Bashforth extrapolation, and the scalar level equation did not identify earlier inspected coverage.

No inaccessible paper was identified whose title or available description specifically suggests the exact threshold formula. The primary pointwise-monotonicity preprint is recent, so simultaneous or unpublished follow-up work remains a residual originality risk.

## Value

**PASS.** The result converts a qualitative/sufficient failure certificate into an exact one-parameter bifurcation law. For a prescribed exact monotone start, it determines precisely when the first stabilized CN/AB increment changes sign, proves that no choice of stabilization strength can shift that onset in the homogeneous test, and enlarges the source paper's active-diffusion perturbative failure regime to the exact boundary. The alpha>1 theorem isolates the mechanism as over-extrapolation of the cubic reaction rather than the particular AB2 coefficient choice.

The contribution is a sharp dynamical failure certificate, not an asymptotic-complexity improvement. It can be used to separate damping of a wrong-signed increment from genuine preservation of its direction and to benchmark modified-energy-stable phase-field integrators against a closed-form local-dynamics threshold.

## Limitations

The exact if-and-only-if threshold assumes the exact homogeneous starter used in the source theorem and concerns only the first post-starter increment. A numerical starter changes the threshold. Small smooth nonhomogeneous perturbations inherit either strict sign by continuity, but no global sharp threshold is claimed for arbitrary spatial data or later iterates. The alpha>1 extension assumes the extrapolated reaction combination is multiplied by a positive scalar factor in the homogeneous reduction. The cubic Allen–Cahn nonlinearity, positive branch 0<a<1, periodic/Neumann setting and exact arithmetic are part of the statement.
