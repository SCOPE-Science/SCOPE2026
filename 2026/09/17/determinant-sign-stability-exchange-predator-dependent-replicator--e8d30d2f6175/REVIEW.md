# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

### Claim checked

The claim is that the three numbered stability statements in Conjecture 6.2 of Cruz--Neves follow locally from their exact determinant formula for positive ABY equilibria together with the invasion eigenvalues of the AY, BY, and AB boundary equilibria, even though a standard Sotomayor transcritical condition fails.

### Main check

For a positive ABY equilibrium, the source derives
\[
\det J=\beta\delta(x)F(x)^2x(1-x)g(x)\kappa'(x),
\]
where \(g(x)=f_A(x,0)-f_B(x,0)\). All factors except \(g\kappa'\) are positive. At each nondegenerate boundary collision the zero eigenvalue is simple, while the two eigenvalues tangent to the relevant stable two-species subsystem are strictly in the left half-plane. Hence those two eigenvalues remain stable on the nearby ABY branch, and the unique small real eigenvalue has the same sign as \(\det J\).

At \(x=1\), positivity gives \(\operatorname{sgn}(a-c)=\operatorname{sgn}(a'-c')\). The ABY branch lies at \(x<1\), so \(\operatorname{sgn}(K-K_c)=-\operatorname{sgn}\kappa'(1)\). The AY B-invasion eigenvalue satisfies
\[
\lambda_B'(K_c)=\frac{a'-c'}{a'^2K_c^2}.
\]
Thus its sign on the ABY side is the negative of the sign of the ABY small eigenvalue.

At \(x=0\), positivity gives \(\operatorname{sgn}(b-d)=\operatorname{sgn}(b'-d')\). The ABY branch lies at \(x>0\), so \(\operatorname{sgn}(K-K_c)=\operatorname{sgn}\kappa'(0)\). The BY A-invasion eigenvalue satisfies
\[
\lambda_A'(K_c)=-\frac{b'-d'}{d'^2K_c^2},
\]
again giving the opposite sign from the ABY small eigenvalue.

At \(x=x_R\) in the reproduction-coexistence case \(a<c,d<b\), the affine function \(g\) has negative slope. Positivity of \(m=g/h\) on the ABY branch gives
\[
\operatorname{sgn}(K-K_c)=-\operatorname{sgn}(h(x_R)\kappa'(x_R)),
\]
while the ABY determinant has sign \(\operatorname{sgn}(h(x_R)\kappa'(x_R))\). The AB predator-invasion eigenvalue is
\[
\lambda_Y=\beta(K/K_c-1),
\]
so the signs are opposite. In the reproduction-codominance case \(a>c,d>b\), the AB equilibrium already has a strictly positive prey-plane eigenvalue, which persists on nearby ABY equilibria and forces instability.

### Adversarial checks

- A determinant sign by itself does not determine stability in three dimensions. The proof uses it only after isolating two eigenvalues that remain strictly in the left half-plane by spectral continuity.
- The small eigenvalue near a simple zero is real: a nonreal eigenvalue would require its conjugate to be nearby as well.
- The product of the two stable eigenvalues is positive, whether they are two negative real eigenvalues or a complex-conjugate pair.
- At \(x_R\), the sign argument uses positivity of the actual ABY branch and requires \(h(x_R)\ne0\). The coincident-zero case \(x_R=x_P\) is nongeneric and is excluded.
- The argument requires \(\kappa'\ne0\) at the collision. It does not cover a simultaneous fold/boundary degeneracy.
- The proof establishes the stability statements, not the missing Sotomayor condition. It therefore does not relabel the collision as a standard transcritical bifurcation.
- Stability is only local along the ABY branch. A later Hopf bifurcation is compatible with the theorem and is in fact numerically suggested in the source paper.

Correctness verdict: **PASS**.

## Originality

The primary source is H. M. Cruz and A. G. M. Neves, arXiv:2607.13281 (July 2026). Section 6 explicitly labels the stability-exchange statement as Conjecture 6.2, explains that the usual transcritical characterization fails because a Sotomayor condition is false, and states in the conclusion that proving Conjecture 6.2 is future work.

Originality searches covered the exact paper title, arXiv identifier, author names, “Conjecture 6.2”, “stability exchange”, predator-dependent replicator terminology, boundary ABY equilibria, and transcritical/Sotomayor terminology. No later proof, correction, or paper resolving this conjecture was located. Current discovery pages also showed no resolved citations to the July 2026 preprint, although such citation counts are not treated as exhaustive evidence.

The determinant identity, the AY/BY/AB stability criteria, and standard spectral-continuity facts are prior ingredients and are not claimed as original. The originality claim is specifically the sign-comparison argument that combines those ingredients to prove the numbered statements of Conjecture 6.2 for the source model.

No inaccessible paper was identified whose title or abstract gives concrete evidence that it already proves this source-specific conjecture. Residual risk remains that an uncited general bifurcation theorem could imply the same stability conclusion under different terminology; the public claim is therefore only **to the best of our knowledge**.

Originality verdict: **PASS, to the best of our knowledge**.

## Value

The result resolves a named open conjecture in a recent three-species dynamical-system paper. It also explains why stability exchange can be proved even though the standard transcritical nondegeneracy test used by the source fails: only a simple zero direction, a separated stable spectral pair, and an exact determinant sign are needed.

The proof is short enough to be reusable in other invariant-boundary population models where an interior equilibrium branch collides with a lower-dimensional boundary equilibrium but standard normal-form hypotheses are inconvenient or degenerate.

Value verdict: **PASS**.

## Review status

This is a same-model scientific review. It is not independent validation, formal verification, expert attestation, or journal peer review.
