# The qutrit Schatten-four exception in nonexpansivity of nearest-density-matrix projection

## Finding

For \(n\ge1\), let \(\mathcal H_n^1\) be the real affine space of trace-one Hermitian \(n\times n\) complex matrices, with distance \(d_p(A,B)=\|A-B\|_{S_p}\), where \(1<p<\infty\). Let \(\mathcal D_n=\{B\in\mathcal H_n^1:B\succeq0\}\), and let \(\Pi_{p,n}(A)\) be the unique closest point of \(\mathcal D_n\) to \(A\).

**Theorem.** For every \(n\ge1\) and \(1<p<\infty\), \(\Pi_{p,n}\) is independent of \(p\). The map is nonexpansive in its ambient Schatten-\(p\) metric **if and only if**
\[
 n\le2\quad\text{or}\quad p=2\quad\text{or}\quad(n,p)=(3,4).
\]
The optimal Lipschitz constant equals \(0\) for \(n=1\) and equals \(1\) in the remaining nonexpansive cases. For all other dimension/exponent pairs it is **strictly greater than** \(1\). This is a sharp qualitative classification, not a closed formula for the expansive constants.

In particular, the trace-normalized three-level case has an exceptional non-Hilbert exponent: Schatten \(4\) becomes Hilbertian on *differences of trace-one Hermitian \(3\times3\) matrices*, despite not being Hilbertian on the whole matrix space.

## Assumptions and scope

Matrices are complex Hermitian, regarded as a real vector space. The target consists of positive semidefinite trace-one matrices, and **inputs are restricted to have trace one**, but need not be positive. The norm is \(\|H\|_{S_p}=(\operatorname{Tr}|H|^p)^{1/p}\), with strictly convex \(1<p<\infty\). The theorem excludes the nondifferentiable endpoint exponents \(p=1\) and \(p=\infty\); all assertions about nonexpansivity are for distances between inputs in \(\mathcal H_n^1\), not arbitrary Hermitian matrices.

## Proof

**1. Exact nearest-point map.** Diagonalize \(A=U\operatorname{diag}(\lambda_1,\ldots,\lambda_n)U^*\). The eigenvalue-difference majorization inequality for Hermitian matrices implies that, if \(B\) has eigenvalues \(\mu_i\) in the same decreasing order, then
\[
 \|A-B\|_{S_p}^p\ge\sum_{i=1}^n|\lambda_i-\mu_i|^p.
\]
Equality is attained by choosing \(B\) diagonal in the eigenbasis of \(A\). Strict convexity makes the closest \(B\) unique. The scalar Karush–Kuhn–Tucker equations for \(\mu_i\ge0\) and \(\sum_i\mu_i=1\) show that, on every positive coordinate, \(\mu_i=\lambda_i-\tau\), with a common scalar \(\tau\), and on the other coordinates \(\lambda_i\le\tau\). Hence
\[
 \Pi_{p,n}(A)=U\operatorname{diag}((\lambda_i-\tau)_+)U^*,\qquad\sum_i(\lambda_i-\tau)_+=1.
\]
This expression is independent of \(p\), including in the presence of repeated eigenvalues. For \(\operatorname{Tr}A=1\), \(\tau\ge0\). 

**2. All nonexpansive cases.** When \(p=2\), \(\Pi_{2,n}\) is metric projection onto the closed convex set \(\mathcal D_n\) in a real Hilbert space. Its variational inequality proves \(\|\Pi_{2,n}(A)-\Pi_{2,n}(B)\|_{S_2}\le\|A-B\|_{S_2}\). For \(n=2\), every traceless Hermitian difference has eigenvalues \(r,-r\), so all \(S_p\) norms on these differences are constant multiples of the Hilbert–Schmidt norm. For \(n=3\), all eigenvalue triples \(\lambda_1+\lambda_2+\lambda_3=0\) obey
\[
 \lambda_1^4+\lambda_2^4+\lambda_3^4=\tfrac12(\lambda_1^2+\lambda_2^2+\lambda_3^2)^2.
\]
Consequently every traceless Hermitian \(3\times3\) matrix obeys \(\|H\|_{S_4}=2^{-1/4}\|H\|_{S_2}\). Since the nearest-point map is the same for both exponents, \(\Pi_{4,3}\) is nonexpansive. For \(n\ge2\), the map fixes two distinct states, so its Lipschitz constant is at least \(1\). For \(n=1\), both domain and target consist of one matrix, and the Lipschitz constant is \(0\).

**3. Expansion for \(n\ge4\) and \(p\ne2\).** Work with diagonal matrices, padding with zeros after the fourth diagonal entry. Let
\[
 Y=\operatorname{diag}(1,1,-2,0),\quad Z=\operatorname{diag}(1,1,1,-3),\quad H_t=Y+tZ.
\]
These are traceless. Direct differentiation gives
\[
 \left.\frac{d}{dt}\|H_t\|_{S_p}^p\right|_{t=0}=p(2-2^{p-1})\ne0
\]
whenever \(p\ne2\). Choose sufficiently small nonzero \(t\) of opposite sign to this derivative; then \(\|H_t\|_{S_p}<\|Y\|_{S_p}\). For small \(\delta>0\), put
\[
 A_\delta=\operatorname{diag}((1+\delta)/3,(1+\delta)/3,(1+\delta)/3,-\delta,0,\ldots,0).
\]
The spectral threshold is \(\delta/3>0\), so exactly the first three indices are active. Keeping the active set unchanged by a sufficiently small perturbation \(\varepsilon H_t\), with \(\varepsilon>0\), gives the **exact** difference
\[
 \Pi_{p,n}(A_\delta+\varepsilon H_t)-\Pi_{p,n}(A_\delta)=\varepsilon Y,
\]
where zeros are padded beyond the fourth coordinate. The input difference is \(\varepsilon H_t\), hence its image has strictly larger \(S_p\) norm. Thus nonexpansivity fails for every \(n\ge4\) outside \(p=2\).

**4. Expansion for \(n=3\) and \(p\notin\{2,4\}\).** Set
\[
 Y=\begin{pmatrix}1&0&1\\0&-1&0\\1&0&0\end{pmatrix},\qquad Z=\operatorname{diag}(1,1,-2),\qquad\varphi=(1+\sqrt5)/2.
\]
Both matrices are traceless. The eigenvalues of \(Y\) are \(\varphi,-1,-\varphi^{-1}\). Evaluating the derivative of the Schatten-power at \(Y\) in direction \(Z\) by spectral calculus yields
\[
 \frac1p\left.\frac{d}{dt}\|Y+tZ\|_{S_p}^p\right|_{t=0}
 =\operatorname{Tr}\big(\operatorname{sgn}(Y)|Y|^{p-1}Z\big)
 =\frac{\varphi^{p-3}+\varphi^{3-p}}{\sqrt5}-1.
\]
Here the first and third coordinates form the \(2\times2\) block \(\begin{psmallmatrix}1&1\\1&0\end{psmallmatrix}\), whose eigenvalues are \(\varphi,-\varphi^{-1}\); interpolation of \(\operatorname{sgn}(s)|s|^{p-1}\) on these two eigenvalues gives the displayed trace. Because \(z\mapsto\varphi^z+\varphi^{-z}\) is strictly increasing in \(|z|\), the derivative vanishes precisely when \(|p-3|=1\), namely at \(p=2\) and \(p=4\). For any other \(p\), choose sufficiently small nonzero \(t\) of opposite sign, so that \(H=Y+tZ\) obeys \(\|H\|_{S_p}<\|Y\|_{S_p}\).

Now choose \(0<\delta<1/6\) and
\[
 A_\delta=\operatorname{diag}(1/3,\ 2/3+\delta,\ -\delta),\quad
 \Pi_{p,3}(A_\delta)=\operatorname{diag}(1/3-\delta/2,\ 2/3+\delta/2,\ 0).
\]
The active eigenvalues are simple and the threshold \(\tau=\delta/2\) is strictly separated from all three eigenvalues. The spectral projection map is differentiable at \(A_\delta\). For the traceless direction \(H=Y+tZ\), differentiation of the two active eigenvalues followed by common-threshold subtraction gives diagonal derivative \((1,-1,0)\). The sole nonzero off-diagonal derivative comes from the \((1,3)\) and \((3,1)\) entries: the standard two-eigenvalue divided difference of the spectral threshold map gives
\[
 D\Pi_{p,3}(A_\delta)[H]=
 \begin{pmatrix}1&0&c_\delta\\0&-1&0\\c_\delta&0&0\end{pmatrix},
 \qquad c_\delta=\frac{1/3-\delta/2}{1/3+\delta}\longrightarrow1
 \quad(\delta\downarrow0).
\]
The derivative is obtained directly by first-order eigenvector perturbation in the \((1,3)\) plane; it does not invoke a differentiability assertion at \(\delta=0\). Therefore \(\|D\Pi_{p,3}(A_\delta)[H]\|_{S_p}\to\|Y\|_{S_p}>\|H\|_{S_p}\). Choose sufficiently small positive \(\delta\) with strict inequality, and then sufficiently small positive \(\varepsilon\). The two distinct trace-one Hermitian inputs \(A_\delta\) and \(A_\delta+\varepsilon H\) then satisfy
\[
 \|\Pi_{p,3}(A_\delta+\varepsilon H)-\Pi_{p,3}(A_\delta)\|_{S_p}
 >\varepsilon\|H\|_{S_p}.
\]
This establishes all remaining expansive cases and completes the proof.

## Verification

The accompanying `verify_density.py` uses the actual spectral threshold formula and `numpy.linalg.eigh`. It checked \(25\) explicit complex-Hermitian traceless quartic identities, \(150\) randomly sampled nonexpansive inequalities across six valid dimension/exponent cases, and \(14\) strict expansive finite-pair witnesses covering seven exponents in dimension three and seven in dimension four. The output was `DENSITY_PROJECTION_CHECK_OK exact-polynomial=25 numerical-nonexpansive=150 numerical-expansive=14`. The quartic polynomial evaluations use exact Gaussian-integer arithmetic; the other checks use floating-point approximations. The theorem rests on the analytic proof above. Run `python verify_density.py` with Python 3.10+ and NumPy 1.24+ from the directory containing the supplied file. These finite tests do not prove the statements for all parameters: the proof is analytic.

## Relationship to prior work

Cheung, Drusvyatskiy, Li, Pelejo, and Wolkowicz study projections involved in quantum-channel semidefinite feasibility, using Euclidean/Frobenius geometry; this supplies motivation and the familiar Hilbert-space case, not an all-exponent nonexpansivity classification. Scalar probability-simplex projections already have common-threshold formulas; the matrix nearest-point formula here is **background machinery rather than the claimed novelty**. Johnston and Li investigate approximation of a state by states of bounded rank, beginning with positive inputs and optimizing over a nonconvex target. Their problem differs from the present projection of arbitrary trace-one Hermitian matrices onto all density matrices. The theorem's focus is the noncommutative input-metric phase boundary and the dimension-three Schatten-four exception.

## Limitations

Only real-valued exponents strictly between one and infinity are covered, and the domain is the trace-one Hermitian affine space. No exact numerical formula for global Lipschitz constants in the expansive cases is claimed; only their strict excess over one and explicit local witness construction are proved. Arbitrary non-Hermitian inputs, unrestricted-trace inputs, positive semidefinite cones without trace constraints, and rank-constrained nonconvex targets are not covered. Repeated eigenvalues pose no difficulty for the nearest-point formula, but the counterexample derivative is evaluated only at matrices with simple eigenvalues.

## References

1. Y.-L. Cheung, D. Drusvyatskiy, C.-K. Li, D. C. Pelejo, and H. Wolkowicz, *Projection methods in quantum information science*, first public posting 2014-07-23, https://optimization-online.org/2014/07/4458/ ; arXiv:1407.6604v1 (2014-07-24), https://arxiv.org/abs/1407.6604 .
2. N. Johnston and C.-K. Li, *Approximating quantum states by states of low rank*, arXiv:2510.08463, https://arxiv.org/abs/2510.08463 .
3. R. Bhatia, *Matrix Analysis*, Springer, 1997, spectral eigenvalue majorization inequality, Chapter IV.
