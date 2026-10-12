# Curvature clipping destroys exact conjugacy in P2GM_CM, with an exact defect law and repair

## Finding
Consider the positive-curvature branch of the 2026 P2GM_CM construction on an exact quadratic
\[
f(x)=\frac12 x^\top Hx,\qquad H\succ0,
\]
with no nonsmooth term. For a nonzero direction \(v\), let
\[
r(v)=\frac{v^\top Hv}{\|v\|^2},
\qquad
q(v)=\max\!\bigl(c_1,\min(r(v),c_2)\bigr),
\]
where \(0<c_1\le c_2\). The latest Algorithm 1 forms
\[
\widetilde s
=
s-\frac{s^\top Hv}{q(v)\|v\|^2}v.
\]
Then the exact defect from \(H\)-conjugacy is
\[
v^\top H\widetilde s
=
(s^\top Hv)\left(1-\frac{r(v)}{q(v)}\right).
\]
Therefore
\[
v^\top H\widetilde s=0
\quad\Longleftrightarrow\quad
s^\top Hv=0
\ \text{ or }\
q(v)=r(v).
\]
On the positive-curvature clipping rule above, the second alternative is exactly \(r(v)\in[c_1,c_2]\). Thus clipping and the generic exact-conjugacy property are incompatible whenever the raw Rayleigh quotient leaves the clipping interval.

This mismatch occurs on an actual trajectory of the source algorithm. Take
\[
H=\operatorname{diag}(1,1/2),\qquad
x^0=(1,1),
\]
use identity preconditioning, no nonsmooth term, and Armijo parameter \(\sigma=1/2\). The first proximal-gradient direction is
\[
v_0=-Hx^0=(-1,-1/2).
\]
The unit step is accepted, because
\[
f(x^0+v_0)-f(x^0)=-\frac{11}{16}
\le
-\frac58
=
\sigma \nabla f(x^0)^\top v_0.
\]
Hence
\[
x^1=(0,1/2),
\qquad
s_1=v_0=(-1,-1/2),
\qquad
v_1=-Hx^1=(0,-1/4).
\]
Now
\[
r(v_1)=\frac12.
\]
With \(c_2=1/4\) and any \(0<c_1\le1/4\), upper clipping gives \(q(v_1)=1/4\). Since
\[
s_1^\top Hv_1=\frac1{16},
\qquad
\|v_1\|^2=\frac1{16},
\]
Algorithm 1 forms
\[
\widetilde s_1=(-1,1/2),
\]
and therefore
\[
v_1^\top H\widetilde s_1=-\frac1{16}\ne0.
\]
By contrast, the exact Hessian-conjugate coefficient from the source's theoretical subspace construction gives
\[
\widetilde s_1^{\,\mathrm{exact}}=(-1,0),
\qquad
v_1^\top H\widetilde s_1^{\,\mathrm{exact}}=0.
\]

The defect can be large rather than perturbative. If the same admissible trajectory uses upper cap \(c_2=\tau\in(0,1/2)\), then
\[
\widetilde s_\tau
=
\left(-1,-\frac12+\frac1{4\tau}\right).
\]
Writing
\[
a_\tau=-\frac12+\frac1{4\tau},
\]
its \(H\)-cosine with \(v_1\) equals
\[
\frac{v_1^\top H\widetilde s_\tau}
{\sqrt{(v_1^\top Hv_1)(\widetilde s_\tau^\top H\widetilde s_\tau)}}
=
-\frac{a_\tau}{\sqrt{2+a_\tau^2}},
\]
which tends to \(-1\) as \(\tau\downarrow0\). Thus the nominally conjugate direction can approach \(H\)-antiparallelity.

A minimal positive-curvature repair is to separate the two roles of curvature. Keep the clipped \(q(v)\) in the one-dimensional model weights, but compute the orthogonalization coefficient from the unclipped sampled curvature:
\[
\widetilde s^{\,\mathrm{repair}}
=
s-\frac{s^\top H(v)}{v^\top H(v)}v
\]
whenever \(v^\top H(v)>0\). On exact SPD quadratics, \(H(v)=Hv\), and this restores
\[
v^\top H\widetilde s^{\,\mathrm{repair}}=0
\]
identically.

## Assumptions and scope
The theorem concerns the latest public version of P2GM_CM and the positive-curvature branch of its finite-difference curvature rule. The exact defect identity is proved for symmetric positive-definite quadratic objectives, where the source finite-difference Hessian-vector sample is exact. The explicit trajectory also fixes the nonsmooth term to zero and the preconditioner to the identity.

The result does not claim that the source convergence theorem fails. The clipped curvature was introduced to keep scalar model coefficients inside prescribed bounds, and those descent safeguards can have a different purpose from exact subspace conjugacy. The repair above is asserted only for the positive-curvature orthogonalization step; no statement is made about negative sampled curvature or about global convergence after modifying the implementation.

## Proof
For an exact quadratic and any nonzero \(v\),
\[
H(v)=Hv,
\qquad
v^\top Hv=r(v)\|v\|^2.
\]
Substituting the source implementation formula gives
\[
\begin{aligned}
v^\top H\widetilde s
&=
v^\top Hs
-
\frac{s^\top Hv}{q(v)\|v\|^2}v^\top Hv\\
&=
s^\top Hv
-
\frac{s^\top Hv}{q(v)\|v\|^2}r(v)\|v\|^2\\
&=
(s^\top Hv)\left(1-\frac{r(v)}{q(v)}\right).
\end{aligned}
\]
Since \(q(v)>0\), this vanishes exactly under the stated alternatives. The clipping characterization follows directly from the definition of \(q(v)\).

For the concrete trajectory, direct substitution gives
\[
f(x^0)=\frac34,
\qquad
f(x^1)=\frac1{16},
\]
so the objective difference is \(-11/16\). Also
\[
\nabla f(x^0)^\top v_0
=
(1,1/2)\cdot(-1,-1/2)
=
-\frac54,
\]
and multiplication by \(\sigma=1/2\) gives \(-5/8\). Thus the source Armijo inequality accepts the unit step.

At the second iterate,
\[
Hv_1=(0,-1/8),
\quad
s_1^\top Hv_1=1/16,
\quad
v_1^\top Hv_1=1/32,
\quad
\|v_1\|^2=1/16.
\]
The raw Rayleigh quotient is therefore \(1/2\). With \(q(v_1)=1/4\), the implemented projection coefficient is \(4\), yielding
\[
\widetilde s_1=s_1-4v_1=(-1,1/2).
\]
The displayed defect is then
\[
v_1^\top H\widetilde s_1
=
(0,-1/4)\cdot(-1,1/4)
=
-\frac1{16}.
\]

For a general upper cap \(\tau\in(0,1/2)\), the same coefficient is \(1/\tau\), which gives the stated \(\widetilde s_\tau\). The \(H\)-cosine calculation uses
\[
v_1^\top Hv_1=\frac1{32},
\qquad
\widetilde s_\tau^\top H\widetilde s_\tau
=
1+\frac{a_\tau^2}{2},
\qquad
v_1^\top H\widetilde s_\tau=-\frac{a_\tau}{8}.
\]
Simplification gives
\[
-\frac{a_\tau}{\sqrt{2+a_\tau^2}},
\]
and \(a_\tau\to+\infty\) as \(\tau\downarrow0\).

Finally, replacing only the orthogonalization denominator by \(v^\top H(v)\) gives
\[
v^\top H\left(
s-\frac{s^\top H(v)}{v^\top H(v)}v
\right)
=
s^\top Hv-s^\top Hv=0
\]
on an exact quadratic.

## Verification
The bundled script `artifacts/verify_p2gm_clipping_conjugacy.py` checks the defect identity numerically on randomly generated SPD matrices, replays the explicit trajectory with exact rational arithmetic, verifies the repaired coefficient, and checks the approach of the \(H\)-cosine to \(-1\) as the upper clipping cap decreases.

These computations are consistency checks. The theorem itself follows from the exact algebra above.

## Relationship to prior work
Chen and Yang introduce P2GM_CM from a subspace viewpoint. Their exact-Hessian derivation orthogonalizes the two basis directions in the Hessian inner product, making the quadratic term diagonal. Their practical algorithm replaces the raw directional curvature by a clipped quantity \(q_k(v)\) in the implemented orthogonalization coefficient. The source presents both ingredients, but does not state the defect identity, characterize exactly when clipping destroys conjugacy, or exhibit a source trajectory on which the implemented basis becomes nonconjugate.

The related projected-gradient momentum literature studies low-dimensional search spaces and momentum directions, but does not use this clipped Rayleigh quotient inside an exact-conjugacy projection. Classical conjugate-gradient subspace analyses likewise motivate Hessian-conjugate bases without this clipping mechanism. Those results therefore do not imply the source-specific defect law above.

## Limitations
The finding is an exact structural statement for SPD quadratics and the positive sampled-curvature branch. It does not show divergence, loss of descent, or invalidity of the source's global convergence theorem. The proposed separation of unclipped projection curvature from clipped scalar-model curvature is algebraically exact on SPD quadratics, but its convergence properties for general composite nonlinear problems are not established here.

The literature comparison covers the latest source version, its immediately related projected-gradient momentum literature, classical conjugate-subspace context, and targeted searches. A later correction or an independent discussion of the same implementation detail could reduce originality.

## References
1. J. Chen and X. Yang, *Preconditioned Proximal Gradient Methods with Conjugate Momentum: A Subspace Perspective*, Optimization Online, first public version 2026-03-16; arXiv:2603.16573v4.
2. J. Chen and X. Yang, *Projected Gradient Methods with Momentum*, Journal of Optimization Theory and Applications, 2026, DOI:10.1007/s10957-026-03054-7.
3. Y. Yuan and J. Stoer, *A Subspace Study on Conjugate Gradient Algorithms*, Zeitschrift für Angewandte Mathematik und Mechanik, 1995.
