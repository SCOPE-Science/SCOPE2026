# The sharp frame-operator perturbation bound is \(B+R\), not \(R+\sqrt B\)

## Finding
Corollary 2 of the final journal version of Rahimlou--Sadri--Ahmadi, *Weighted Riesz bases in \(g\)-fusion frames and their perturbation* (Corollary 6 in the original preprint), gives a false universal upper frame bound.

Let
\[
S_\Lambda
=
\sum_{j\in J}
v_j^2P_{W_j}\Lambda_j^*\Lambda_jP_{W_j}
\]
be the \(g\)-fusion frame operator of a family with bounds \(A,B\). Suppose another family satisfies
\[
\sum_{j\in J}v_j^2
\left\|
\left(
P_{W_j}\Lambda_j^*\Lambda_jP_{W_j}
-
P_{W_j}\Theta_j^*\Theta_jP_{W_j}
\right)f
\right\|
\le R\|f\|
\]
for every \(f\in H\), where
\[
0<R<A.
\]

The paper claims that the perturbed family has upper bound
\[
\min\left\{
B+R\sqrt{\frac BA},
\;
R+\sqrt B
\right\}.
\]
The second alternative can be smaller than the perturbed frame energy and is therefore invalid.

An exact one-dimensional witness is
\[
H=\mathbb R,\qquad
W_1=H,\qquad
v_1=1,\qquad
\Lambda_1=2I,\qquad
\Theta_1=\sqrt5\,I.
\]
The original system is tight with
\[
A=B=4.
\]
Moreover,
\[
\|(\Lambda_1^*\Lambda_1-\Theta_1^*\Theta_1)f\|
=
\|f\|,
\]
so the hypothesis holds with
\[
R=1.
\]
The published upper bound is
\[
\min\{5,3\}=3,
\]
but
\[
\|\Theta_1f\|^2=5\|f\|^2.
\]
Hence the claimed bound \(3\) is false.

The sharp universal replacement is
\[
A-R
\quad\text{and}\quad
B+R.
\]

## Assumptions and scope
The result uses exactly the source's frame-operator-difference hypothesis. The index set may be finite or infinite. The displayed summed norm condition guarantees convergence of the perturbation series on each vector once the original frame-operator series is known to converge.

No extra commutation assumption is needed. The correction is an operator-order consequence of self-adjointness and the norm bound on the frame-operator difference.

The claim concerns this specific perturbation corollary. It does not alter the distinct analysis-operator perturbation theorem later in the same paper, whose hypothesis and squared constants are different.

## Proof
For finite \(F\subset J\), put
\[
D_Ff
=
\sum_{j\in F}v_j^2
\left(
P_{W_j}\Theta_j^*\Theta_jP_{W_j}
-
P_{W_j}\Lambda_j^*\Lambda_jP_{W_j}
\right)f.
\]
The hypothesis implies
\[
\|D_Ff-D_Ef\|
\le
\sum_{j\in F\triangle E}v_j^2
\left\|
\left(
P_{W_j}\Theta_j^*\Theta_jP_{W_j}
-
P_{W_j}\Lambda_j^*\Lambda_jP_{W_j}
\right)f
\right\|,
\]
so the perturbation series is absolutely convergent in \(H\) for each \(f\). Its sum \(Df\) satisfies
\[
\|Df\|\le R\|f\|.
\]
Thus \(D\) is bounded and
\[
\|D\|\le R.
\]

The original frame-operator series converges strongly. Therefore
\[
S_\Theta=S_\Lambda+D
\]
is well defined. Each finite partial sum defining \(S_\Theta\) is positive and self-adjoint, hence the strong limit \(S_\Theta\) is positive and self-adjoint. Consequently \(D=S_\Theta-S_\Lambda\) is self-adjoint.

For a self-adjoint operator of norm at most \(R\),
\[
-RI\le D\le RI.
\]
Since
\[
AI\le S_\Lambda\le BI,
\]
we obtain
\[
(A-R)I
\le
S_\Lambda+D
=
S_\Theta
\le
(B+R)I.
\]
Taking quadratic forms gives
\[
(A-R)\|f\|^2
\le
\sum_{j\in J}v_j^2\|\Theta_jP_{W_j}f\|^2
\le
(B+R)\|f\|^2.
\]
Because \(R<A\), the lower constant is positive, so the perturbed family is a \(g\)-fusion frame.

For sharpness, use a one-point measure-free \(g\)-fusion system with
\[
W_1=H=\mathbb R,\qquad v_1=1,\qquad \Lambda_1=\sqrt c\,I.
\]
Then \(A=B=c\). If
\[
\Theta_1=\sqrt{c-R}\,I,
\]
the perturbation norm is exactly \(R\) and the perturbed exact frame bound is \(c-R\). If instead
\[
\Theta_1=\sqrt{c+R}\,I,
\]
the perturbation norm is again exactly \(R\) and the exact bound is \(c+R\). Thus both universal endpoints are attained.

## Verification
The original preprint and final journal PDF were inspected at the \(g\)-fusion-frame definition, frame-operator formula, the general perturbation theorem, the target corollary, and its complete proof.

The final article prints
\[
A-R
\]
as the lower bound and
\[
\min\left\{
B+R\sqrt{\frac BA},
R+\sqrt B
\right\}
\]
as the upper bound. Its proof estimates the norm of the perturbed frame operator and then invokes the preceding general perturbation theorem.

The scalar witness was checked exactly:
\[
A=B=4,\qquad R=1,\qquad S_\Theta=5I.
\]
The two printed upper candidates are \(5\) and \(3\); taking their minimum produces the contradiction.

The corrected proof does not rely on a numerical experiment. It uses only convergence of the operator series, self-adjoint operator order, and the exact norm bound
\[
\|S_\Theta-S_\Lambda\|\le R.
\]

## Relationship to prior work
Najati--Faroughi--Rahimi's earlier \(g\)-frame stability paper proves a different perturbation result based on the \(\ell^2\)-norm of the analysis-coefficient difference. Its corresponding bounds have the standard squared form
\[
(\sqrt A-\sqrt R)^2,
\qquad
(\sqrt B+\sqrt R)^2.
\]
The target paper reproduces the analogous analysis-operator perturbation result separately from the frame-operator-difference corollary corrected here.

The present hypothesis is stronger in a different direction: it controls the summed action of the positive coefficient operators themselves. That control directly bounds the frame-operator difference and therefore gives the order interval
\[
S_\Lambda-RI\le S_\Theta\le S_\Lambda+RI.
\]

Exact-title, DOI, preprint-identifier, published-bound, and \(B+R\) searches did not locate an indexed erratum or a checked source stating this sharp correction.

## Limitations
The result gives the best universal constants obtainable from \(A,B,R\) and the stated frame-operator-difference hypothesis. A particular family can have better bounds.

The correction does not claim that the source's first printed upper candidate
\[
B+R\sqrt{\frac BA}
\]
is always false; the problem is that the published minimum may select the invalid second candidate. The universal bound \(B+R\) is both simpler and sharp.

No assertion is made about perturbation hypotheses that control analysis operators rather than frame operators.

## References
1. G. Rahimlou, V. Sadri and R. Ahmadi, *Weighted Riesz bases in \(g\)-fusion frames and their perturbation*, arXiv:1806.03596v1, 10 June 2018; Problems of Analysis. Issues of Analysis 9(27)(1) (2020), 110--127, DOI 10.15393/j3.art.2020.7470.
2. A. Najati, M. H. Faroughi and A. Rahimi, *\(g\)-frames and stability of \(g\)-frames in Hilbert spaces*, Methods of Functional Analysis and Topology 14(3) (2008), 271--286.
