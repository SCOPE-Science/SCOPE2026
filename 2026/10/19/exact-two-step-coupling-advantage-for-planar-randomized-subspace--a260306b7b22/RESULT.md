# Exact two-step coupling advantage for planar randomized subspace Newton

## Finding
Let \(H\in\mathbb R^{2\times2}\) be symmetric positive definite, with spectral condition number \(\kappa\ge1\), and consider exact minimization of the quadratic \(f(x)=\tfrac12(x-x_*)^T H(x-x_*)\) along randomly selected one-dimensional subspaces. Define the line-minimization error map
\[
T_u e=e-u\frac{u^THe}{u^THu},\qquad u\ne0.
\]
In the independent experiment, let \(u,v\) be independent uniform directions on the Euclidean unit circle. In the paired experiment, choose only \(u\) uniformly and set \(v=Ju\), where \(J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\). Both experiments make two successive *exact line minimizations*, and in both, each direction separately is uniform on the circle. For every fixed deterministic \(e\in\mathbb R^2\),
\[
\boxed{\mathbb E_u\|T_{Ju}T_ue\|_H^2
=\left(\frac{\kappa-1}{\kappa+1}\right)^2
\mathbb E_{u,v}\|T_vT_ue\|_H^2.}
\]
Here \(\|e\|_H^2=e^THe\). Thus Euclidean-orthogonal pairing strictly improves the expected objective gap for every nonzero initial error when \(\kappa>1\); at \(\kappa=1\) it terminates exactly in two steps. The exact sharp worst-case contraction factors for two steps, measured in squared \(H\)-norm, are
\[
\rho_{\mathrm{iid}}(\kappa)=
\frac{\sqrt\kappa(2\kappa+\sqrt\kappa+1)}{2(\sqrt\kappa+1)^3},
\qquad
\rho_{\perp}(\kappa)=\left(\frac{\kappa-1}{\kappa+1}\right)^2\rho_{\mathrm{iid}}(\kappa).
\]
For example, at \(\kappa=4\) these are \(11/27\) and \(11/75\), respectively. No simultaneous two-dimensional Newton solve is performed: the second directional minimization does not preserve the first directional optimality condition.

## Assumptions and scope
The matrix is real, symmetric, \(2\times2\), and positive definite; the gradient and Hessian are exact; step lengths are the exact minimizers along the chosen lines. The matrix, initial point, and minimizer are fixed, while only directions are random. The first angle is uniform; in the independent experiment the second angle is independent and uniform, and in the paired experiment it differs by a right angle. The result covers every \(1\le\kappa<\infty\), including repeated eigenvalues. No conclusion is claimed for higher dimension, inexact line search, noisy finite differences, or other direction distributions.

## Proof
By Euclidean rotation, scaling of \(H\), and sign invariance of line updates, take \(H=\operatorname{diag}(t^2,1)\), where \(t=\sqrt\kappa\ge1\). Put \(y=H^{1/2}e\), \(w_u=H^{1/2}u/\sqrt{u^THu}\), and \(P_u=I-w_uw_u^T\). Then \(H^{1/2}T_ue=P_uy\), so the expected squared \(H\)-norm after two steps is the quadratic form of the matrix \(M=\mathbb E[P_uP_vP_u]\).

Write \(u=(\cos\theta,\sin\theta)\), with uniform \(\theta\). The tangent \(X=\tan\theta\) has the standard Cauchy distribution. Set
\[
W=\frac{t^2}{t^2+X^2}=w_{u,1}^2.
\]
Reflection symmetry forces all expected matrices below to be diagonal. Elementary Cauchy integrals yield
\[
\mathbb EW=\frac{t}{t+1},\quad
\mathbb EW^2=\frac{t(2t+1)}{2(t+1)^2},\quad
\mathbb E[W(1-W)]=\frac{t}{2(t+1)^2}.
\]
For independent \(v\), \(A=\mathbb EP_v=\operatorname{diag}(1,t)/(t+1)\), hence \(M_{\mathrm{iid}}=\mathbb E[P_uAP_u]\). Because \(P_u\) has rank one, \(P_uAP_u=[1+(t-1)W]P_u/(t+1)\). Taking the two diagonal entries and using the moments above gives
\[
M_{\mathrm{iid}}
=\frac1{2(t+1)^3}
\begin{pmatrix}t^2+t+2&0\\0&t(2t^2+t+1)\end{pmatrix}.
\]

For paired directions \(v=Ju\), the two transformed normals \(w_u,w_v\) have squared inner product
\[
R(X)=(w_u^Tw_v)^2
=\frac{(t^2-1)^2X^2}{(t^2+X^2)(1+t^2X^2)}.
\]
In the plane, the complementary rank-one projector identity gives \(P_uP_vP_u=R(X)P_u\). In particular, the two diagonal entries of \(M_{\perp}\) are \(\mathbb E[R(1-W)]\) and \(\mathbb E[RW]\). Direct integration against \(dx/[\pi(1+x^2)]\), for \(t>1\), gives
\[
\mathbb E R=\frac{(t-1)^2}{t^2+1},\quad
\mathbb E[RW]=\frac{t(t-1)^2(2t^2+t+1)}{2(t+1)(t^2+1)^2}.
\]
For clarity, these are ordinary rational integrals: with the even-integrand rule \(\mathbb E g(X)=2\pi^{-1}\int_0^\infty g(x)/(1+x^2)\,dx\), one explicit partial-fraction decomposition used in the second identity is
\[
\begin{aligned}
\frac{R(x)W(x)}{1+x^2}
={}&\frac{t^2}{(t^2-1)(1+x^2)}
-\frac{t^2(t^4+t^2+1)}{(t^2-1)(t^2+1)^2(t^2+x^2)}\\
&-\frac{t^4}{(t^2+1)(t^2+x^2)^2}
-\frac{t^6}{(t^2-1)(t^2+1)^2(1+t^2x^2)}.
\end{aligned}
\]
Integrate with \(\int_0^\infty dx/(x^2+a^2)=\pi/(2a)\) and \(\int_0^\infty dx/(x^2+a^2)^2=\pi/(4a^3)\). Subtraction yields
\[
\mathbb E[R(1-W)]
=\frac{(t-1)^2(t^2+t+2)}{2(t+1)(t^2+1)^2}.
\]
Consequently
\[
M_{\perp}=
\frac{(t-1)^2}{2(t+1)(t^2+1)^2}
\begin{pmatrix}t^2+t+2&0\\0&t(2t^2+t+1)\end{pmatrix}
=\left(\frac{t^2-1}{t^2+1}\right)^2 M_{\mathrm{iid}}.
\]
For \(t=1\), \(P_uP_{Ju}=0\) identically, so the same identity holds by direct inspection, without using singular partial fractions. The identity is preserved by the initial orthogonal change of coordinates and proves the displayed universal comparison for all errors.

Finally, \(t(2t^2+t+1)-(t^2+t+2)=2(t^3-1)\ge0\). Thus the top eigenvalue of \(M_{\mathrm{iid}}\) is its second diagonal entry, attained by transformed initial error along the smaller-eigenvalue mode of \(H\). The paired matrix is a scalar multiple, proving both sharp contraction formulas, including the equal-eigenvalue case.

## Verification
Run `python verify.py` after installing the two listed dependencies in `requirements.txt`. The script uses symbolic integration to verify the four Cauchy moments, the exact matrix identity, and the comparison of diagonal eigenvalues. It also performs seven 16,384-angle deterministic quadratures and 210 initial-error tests, including \(\kappa=1\) and ill-conditioned matrices. The included `verification_output.txt` records the actual passing run. These finite numerical checks are corroboration; the algebraic proof above establishes the all-matrix and all-initial-error statement.

## Relationship to prior work
Berglund, Khirirat, and Wang introduce the randomized subspace Newton update as a sketched exact Newton subproblem and analyze zeroth-order estimates and general convergence [1]. Gower, Kovalev, Lieder, and Richtárik analyze general randomized subspace Newton descent and convergence [2]. Kozak and coauthors analyze Haar-orthogonal directions for a *simultaneous* stochastic finite-difference gradient estimate [3]. Those constructions motivate, respectively, the update, the convergence metric, and orthogonally coupled randomness. The present result instead compares **two sequential rank-one exact line minimizations with orthogonal versus independent direction coupling**, giving an exact scalar relation between the full expected two-step error matrices and sharp worst-case constants. It neither claims that orthogonal sampling is new nor identifies sequential line minimization with a single full-dimensional Newton step.

## Limitations
The two-step identity is planar and uses an exactly quadratic objective and exact directional minimization. Orthogonal pairing in other dimensions, finite-difference errors, nonquadratic models, and longer coupled sequences are not analyzed. Published general random-pursuit and sketch-and-project frameworks may contain equivalent identities not retrieved in the targeted comparison; originality is therefore subject to future independent literature review. No independent audit has been conducted.

## References
[1] Erik Berglund, Sarit Khirirat, Xiaoyu Wang, *Zeroth-Order Randomized Subspace Newton Methods*, arXiv:2202.04612 (first public 2022-02-09), https://arxiv.org/abs/2202.04612.

[2] Robert M. Gower, Dmitry Kovalev, Felix Lieder, Peter Richtárik, *RSN: Randomized Subspace Newton*, arXiv:1905.10874, https://arxiv.org/abs/1905.10874.

[3] David Kozak, Cesare Molinari, Lorenzo Rosasco, Luis Tenorio, Silvia Villa, *Zeroth order optimization with orthogonal random directions*, arXiv:2107.03941, https://arxiv.org/abs/2107.03941.

[4] Robert M. Gower, Peter Richtárik, *Randomized Iterative Methods for Linear Systems*, arXiv:1506.03296 (2015), https://arxiv.org/abs/1506.03296.
