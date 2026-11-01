# Exact singular-value fibers of nilpotent three-level numerical shadows

## Finding

For a complex matrix \(A\in M_3(\mathbb C)\) with \(A^3=0\) and \(A\ne0\), let \(\mu_A\) be the distribution of \(\langle AX,X\rangle\) for a Haar-uniform unit vector \(X\in\mathbb C^3\). Define the two shadow invariants
\[
\kappa=\operatorname{tr}(A^*A)>0,\qquad
\tau=\operatorname{tr}(A^2A^*),\qquad q=|\tau|^2.
\]
Two such nilpotent matrices have the same numerical shadow exactly when their \(\kappa\) and complex \(\tau\) coincide. The feasible parameter range is precisely \(0\le q\le\kappa^3/27\).

Let \(r_-\le r_+\) denote the smallest and largest roots in \([0,\kappa/2]\) of
\[
2r^3-\kappa r^2+q=0.
\]
(The endpoints are \(0,\kappa/2\) when \(q=0\), and both equal \(\kappa/3\) when \(q=\kappa^3/27\).) Then, **among all nilpotent matrices with this identical full numerical shadow**, the possible singular-value lists are exactly
\[
\left(\sqrt{\frac{\kappa+\sqrt{\kappa^2-4r^2}}2},
\sqrt{\frac{\kappa-\sqrt{\kappa^2-4r^2}}2},0\right),
\qquad r\in[r_-,r_+].
\]
Each list is attained. Equivalently, the attainable \(\|A^2\|_{\mathrm{op}}\) and Schatten trace norm are respectively the complete intervals
\[
\|A^2\|_{\mathrm{op}}\in[r_-,r_+],\qquad
\|A\|_{\mathcal S_1}\in[\sqrt{\kappa+2r_-},\sqrt{\kappa+2r_+}].
\]

The interval collapses to one point precisely at \(q=\kappa^3/27\). At the critical boundary define \(\delta=1-27q/\kappa^3\). As \(\delta\downarrow0\),
\[
 r_+-r_-=\frac{2\kappa}{3\sqrt3}\sqrt\delta+O(\kappa\delta^{3/2}),
\]
\[
\sqrt{\kappa+2r_+}-\sqrt{\kappa+2r_-}
=\frac{2\sqrt\kappa}{3\sqrt5}\sqrt\delta+O(\sqrt\kappa\delta).
\]
Thus the hidden singular-spectrum ambiguity has a sharp square-root collapse at the rigid-shadow boundary.

## Assumptions and scope

Matrices are complex \(3\times3\) nilpotents, including nilpotency index two and three, and the numerical shadow is the **full probability law**, not just its support/numerical range. The Haar measure on the complex unit sphere is normalized to probability one; \(\|\cdot\|_{\mathcal S_1}\) is the sum of singular values. The zero matrix, uniquely determined by its zero shadow, is omitted to avoid division by \(\kappa\). The complex phase of \(\tau\) is part of the fixed shadow data. Results concern invariants and **possible spectra**, not a claim that all matrices in one shadow class are unitarily equivalent.

## Proof

**Shadow-data reduction.** By the finite trace-moment criterion of Dunkl–Gawron–Holbrook–Puchała–Życzkowski, restated as Theorem 1.9 by Johnson, equality of \(3\times3\) numerical shadows is equivalent to equality of \(\operatorname{tr}((sA+tA^*)^j)\) for \(1\le j\le3\), as polynomials in independent complex variables \(s,t\). Since \(A\) is nilpotent, its pure traces vanish, and the remaining traces are
\[
 \operatorname{tr}((sA+tA^*)^2)=2\kappa st,
\quad \operatorname{tr}((sA+tA^*)^3)=3(\tau s^2t+\overline\tau st^2).
\]
The nilpotent shadow is therefore determined exactly by \((\kappa,\tau)\). In particular,
\[
\det(I-sA-tA^*)=1-\kappa st-\tau s^2t-\overline\tau st^2.
\]

**Triangle parametrization.** By unitary Schur triangularization, \(A\) has a representative
\[
 A=\begin{pmatrix}0&x&y\\0&0&z\\0&0&0\end{pmatrix}.
\]
Set \(u=|x|^2\), \(v=|y|^2\), \(w=|z|^2\). Direct multiplication gives
\[
 \kappa=u+v+w,\qquad \tau=xz\overline y,\qquad
 r:=\|A^2\|_{\mathrm{op}}=|xz|=\sqrt{uw}.
\]
Hence \(q=uvw\le((u+v+w)/3)^3=\kappa^3/27\). Conversely all feasible \(q\) are attained, for instance by continuously varying the positive entries of a triple with sum \(\kappa\) between \((\kappa,0,0)\) and \((\kappa/3,\kappa/3,\kappa/3)\); the phase of \(y\) supplies any phase of \(\tau\).

**Exact attainable interval.** For \(r>0\), the relations impose \(v=q/r^2\). Arithmetic–geometric mean gives \(u+w\ge2\sqrt{uw}=2r\), so
\[
\kappa\ge2r+\frac q{r^2}
\quad\Longleftrightarrow\quad
2r^3-\kappa r^2+q\le0.
\]
For \(0<q<\kappa^3/27\), the cubic decreases on \((0,\kappa/3)\) and increases on \((\kappa/3,\infty)\); it has exactly two roots in \((0,\kappa/2)\), and its nonpositive set for positive \(r\) is precisely \([r_-,r_+]\). The endpoint cases \(q=0\) and \(q=\kappa^3/27\) follow by direct factorization or the same inequality.

For sufficiency, take any permitted \(r>0\). Write \(S=\kappa-q/r^2\ge2r\), and define
\[
 u=\frac{S+\sqrt{S^2-4r^2}}2,\qquad
 w=\frac{S-\sqrt{S^2-4r^2}}2.
\]
Then \(u,w\ge0\), \(u+w=S\), \(uw=r^2\). With \(x=\sqrt u\), \(z=\sqrt w\), and \(y=\overline\tau/r\), the displayed triangular matrix has exactly the prescribed \(\kappa,\tau,r\). If \(q=r=0\), take \(x=\sqrt\kappa\), \(y=z=0\). Thus every \(r\) in the whole interval occurs. At nonzero interval endpoints, equality in arithmetic–geometric mean forces \(u=w=r\).

**Singular spectra and norms.** The two potentially nonzero squared singular values of the triangular matrix are the eigenvalues of its nonzero \(2\times2\) Gram block. Their sum is \(\operatorname{tr}(A^*A)=\kappa\), and their product is \(|xz|^2=r^2\). Consequently they are the two roots of \(\lambda^2-\kappa\lambda+r^2\), giving the displayed singular list. Moreover \((s_1+s_2)^2=\kappa+2r\), proving the sharp Schatten trace-norm interval. The operator norm is also explicitly determined by the larger displayed singular value; no additional degrees of freedom remain in the singular spectrum.

**Boundary asymptotics.** Substitute \(r=(\kappa/3)(1+h)\) and \(q=(\kappa^3/27)(1-\delta)\) into the endpoint equation. This gives exactly
\[
3h^2+2h^3=\delta.
\]
Its branches near zero satisfy \(h_\pm=\pm\sqrt{\delta/3}-\delta/9+O(\delta^{3/2})\). Subtracting yields the first expansion. Applying the smooth function \(r\mapsto\sqrt{\kappa+2r}\) around \(\kappa/3\) gives the second. Both leading coefficients are nonzero, so exponent \(1/2\) cannot be improved.

**A nonzero-third-moment example.** At \(\kappa=3\), \(\tau=1/\sqrt2\), the cubic factors with its positive roots \(r_-=1/2\) and \(r_+=(1+\sqrt3)/2\). Both are attained by the explicit endpoint matrices with \(x=z=\sqrt r\), \(y=\tau/r\). These matrices have the same full numerical shadow but respectively have trace norms \(2\) and \(\sqrt{4+\sqrt3}\). Thus nonuniqueness is not confined to the previously known \(\tau=0\) examples.

## Verification

The accompanying standalone standard-library program `check_shadow.py` checks the constructive parameter recovery, the trace-moment determinant identity, the singular-value equations, a factorizable nonzero-\(\tau\) example, and the leading boundary coefficients for deterministic finite test cases. Running `python check_shadow.py` produced `PASS 9612 supplementary finite checks`. These checks are reproducibility support; all quantified and asymptotic assertions are proved analytically above.

## Relationship to prior work

The complete finite-moment criterion for equality of numerical shadows and an explicit rank-one/rank-two equal-shadow example were previously established by Dunkl, Gawron, Holbrook, Puchała, and Życzkowski (arXiv:1010.4189). Neither is claimed as new. Gallay and Serre (arXiv:1009.1522) provide the foundational distribution/Radon-transform theory. Johnson (arXiv:2610.29675v1, public 2026-10-21) classifies rigid \(3\times3\) shadows and provides the triangular parametrization of the shadow invariants. The present claim specializes to nilpotent matrices and **solves the separate inverse problem of the full attainable singular spectrum at a fixed shadow**, including nonzero third moment, sharp extrema, and the exact critical square-root collapse. All earlier trace identities and rigidity assertions are credited as inputs rather than new discoveries.

## Limitations

The result neither classifies unitary orbits inside shadow fibers nor extends to non-nilpotent matrices or dimensions above three. The critical exponent concerns singular-spectrum ambiguity as measured by \(\|A^2\|\) or trace norm; it is not an estimate of distance between matrices modulo unitary conjugation. The proof relies on an established shadow moment criterion. Searches and close-source comparisons cannot establish absolute publication priority: an older equivalent singular-spectrum optimization could exist, and independent mathematical verification has not been performed.

## References

1. D. Johnson, *Numerical Shadow Rigidity for 3x3 Matrices*, arXiv:2610.29675v1 (2026), https://arxiv.org/html/2610.29675v1 .
2. C. F. Dunkl, P. Gawron, J. A. Holbrook, Z. Puchała, K. Życzkowski, *Numerical shadows: measures and densities on the numerical range*, arXiv:1010.4189 (2010), https://arxiv.org/html/1010.4189v1 .
3. T. Gallay, D. Serre, *The numerical measure of a complex matrix*, arXiv:1009.1522 (2010), https://arxiv.org/abs/1009.1522 .
