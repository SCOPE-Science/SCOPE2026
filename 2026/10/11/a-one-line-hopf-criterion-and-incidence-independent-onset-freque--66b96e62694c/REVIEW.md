# Review: A one-line Hopf criterion and incidence-independent onset frequency in a nonlinear-incidence SIRS model

## Correctness
PASS. The proof starts from the source's exact equilibrium relation and Jacobian trace/determinant. At \(B=B_H\), the determinant reduces exactly to \(r(1-p_cX_1)/X_1\), hence to \(rs\widetilde X/X_1-1\). The source's additional \(q>q_1\) inequality on its high-\(p\) branch is algebraically equivalent to this determinant being positive. Differentiating the exact trace gives the nonzero crossing speed. Substitution of the source reparametrization gives \(D=\omega_H^2\) identically. No finite experiment is used as an infinite proof.

## Originality
PASS. Searches by source identifier, threshold notation, frequency, transversality, incidence exponents, and the same SIRS family found no statement implication-equivalent to the combined branch simplification plus original-time frequency invariant. The motivating paper gives the ingredients but not this formulation: Proposition 3.1 retains two Hopf branches, and Section 5.1 reports the frequency after a positive time rescaling. The closest older SIRS papers study Hopf normal forms and generalized incidence but the inspected accessible material does not state the present exact invariant.

## Value
PASS. The onset period of epidemic oscillation is a natural observable at Hopf bifurcation. Identifying the paper's auxiliary \(D\) as the original squared Hopf frequency gives it direct dynamical meaning, while the one-line Hopf criterion removes an artificial case split and shows exactly which parameters set onset existence versus onset period. The result is structural over the full Hopf surface, not a special numerical slice.

## Closest literature and limitations
The closest source is arXiv:2609.38874v1 itself. Hu--Bi--Ma--Ruan (2011) and Alexander--Moghadas (2005) are earlier primary papers on Hopf bifurcation in SIRS models with nonlinear or generalized incidence. Cui--Zhao (2024) is the immediate same-family predecessor focused on saddle-node and Bogdanov--Takens bifurcations. Accessible older material does not cover the exact single-criterion/frequency statement, but inaccessible or differently normalized older derivations remain a residual originality risk. The present result is local and does not settle criticality or maximal cycle count.

Same-model review: passed. Independent audit: not yet performed.
