# Sharp four-point Gaussian sampling radius in the affine Bargmann–Fock space

## Finding
Let \(\zeta=e^{2\pi i/3}\). For \(r>0\), sample an affine entire function \(f(z)=a+bz\) at the origin and at the three vertices \(r,r\zeta,r\zeta^2\) with its natural Gaussian intensity:
\[
\mathcal I_r(f)=\bigl(|f(0)|^2,e^{-r^2}|f(r)|^2,e^{-r^2}|f(r\zeta)|^2,e^{-r^2}|f(r\zeta^2)|^2\bigr).
\]
Define the real linear lift on \(2\times2\) Hermitian matrices by
\[
(\mathcal L_r H)_0=H_{11},\qquad
(\mathcal L_r H)_{j+1}=e^{-r^2}(1,\overline{r\zeta^j})H(1,r\zeta^j)^{\mathsf T}\quad(j=0,1,2).
\]
Use the Frobenius norm on the real four-dimensional Hermitian domain and the ordinary Euclidean norm on the four outputs. Then \(\mathcal L_r\) is bijective for every \(r>0\), and its spectral condition number has a **unique global minimum** at \(r_*=\sqrt{u_*}\), where \(u_*\in(1,4/3)\) is the unique positive root of
\[
(u-1)e^{2u}=3(u^2-u+1).
\]
In fact
\[
u_*=1.3077030679082091939\ldots,\qquad
r_*=1.1435484545519744586\ldots,\qquad
\min_{r>0}\operatorname{cond}_2(\mathcal L_r)=\frac{e^{u_*}}{\sqrt3}=2.1348511463570939131\ldots.
\]
At this unique radius, the four squared singular values are exactly
\[
\left\{u_*,\,3u_*e^{-2u_*},\,3u_*e^{-2u_*},\,3u_*e^{-2u_*}\right\}.
\]
Thus the three least-amplified Hermitian directions are **exactly isotropic** at the optimal radius. The four intensity observations also recover every affine \(f\), up to global unimodular phase, because they determine its rank-one Hermitian lift.

## Assumptions and scope
The affine space \(\operatorname{span}\{1,z\}\) is equipped with the standard Bargmann–Fock inner product \(\pi^{-1}\int_{\mathbb C}f(z)\overline{g(z)}e^{-|z|^2}\,dA(z)\), in which \(1,z\) are orthonormal. All four intensity observations have **raw physical Gaussian weights**; no sample-dependent renormalization or noise weighting is introduced. The condition number concerns the linear map on all Hermitian matrices, not a signal-dependent local Jacobian or a statistical Fisher information matrix. The optimization is over the sole radius parameter with three equally spaced outer samples and the center fixed. No optimality over arbitrary four-point geometries or arbitrary measurement weights is claimed.

## Proof
Put \(u=r^2\) and \(s=e^{-2u}\). Write a Hermitian matrix as \(H=\bigl(\begin{smallmatrix}a&c\\\bar c&b\end{smallmatrix}\bigr)\), so \(\|H\|_F^2=a^2+b^2+2|c|^2\). The center sample is \(a\). The outer samples are \(e^{-u}(a+ub+2\sqrt u\operatorname{Re}(c\zeta^j))\). Applying the real orthogonal Fourier transform to the three outer outputs decomposes \(\mathcal L_r\) as the direct sum of
\[
B_u=\begin{pmatrix}1&0\\\sqrt3 e^{-u}&\sqrt3 u e^{-u}\end{pmatrix}
\quad\text{and}\quad \sqrt{3u}\,e^{-u}I_2.
\]
The squared singular values are therefore \(\lambda_+(u),\lambda_-(u),\lambda_0(u),\lambda_0(u)\), with
\[
T=1+3s(1+u^2),\quad
\lambda_\pm=\frac{T\pm\sqrt{T^2-12su^2}}2,\quad
\lambda_0=3us,\quad
\lambda_+\lambda_-=3u^2s.
\]
The upper eigenvalue obeys \(\lambda_+\ge 1+3s>\lambda_0\): for \(u\le1\) this is immediate; for \(u>1\) it follows from \(3(u-1)e^{-2u}\le\tfrac32e^{-3}<1\).

The characteristic polynomial of \(B_u^{\mathsf T}B_u\), evaluated at \(\lambda_0\), is
\[
\lambda_0^2-T\lambda_0+3u^2s
=3us\,h(u),\qquad
h(u)=u-1-3e^{-2u}(u^2-u+1).
\]
Since \(h'(u)=1+3e^{-2u}(2(u-1)^2+1)>0\), and \(h(1)<0<h(4/3)\), there is exactly one crossing \(u_*\in(1,4/3)\). The last strict inequality follows from \(e^{8/3}>13\). It follows that \(\lambda_-<\lambda_0\) for \(u<u_*\), while \(\lambda_0<\lambda_-\) for \(u>u_*\).

For \(0<u<u_*\), the squared condition number is \(\lambda_+/\lambda_-\). This ratio is an increasing function of \(T/\sqrt{3u^2s}\), which equals
\[
Q(u)=\frac{e^u+3e^{-u}(1+u^2)}{\sqrt3\,u}.
\]
The sign of \(Q'(u)\) equals the sign of
\[
e^{2u}(u-1)-3(u^3-u^2+u+1).
\]
For \(u\le1\) this is negative. For \(1<u<4/3\), its first term is less than \(e^{8/3}/3<5\), and its second term is at least \(6\), so it remains negative. Both exponential estimates \(13<e^{8/3}<15\) have elementary rational Taylor-series certificates (also checked in the accompanying program). Hence the condition number is strictly decreasing before \(u_*\).

For \(u>u_*\), the squared condition number is \(\lambda_+/\lambda_0\), the largest eigenvalue of the symmetric matrix
\[
K_u=\frac{B_u^{\mathsf T}B_u}{\lambda_0}
=\begin{pmatrix}(e^{2u}+3)/(3u)&1\\1&u\end{pmatrix}.
\]
Since \(u>u_*>1\), the derivative \(K'_u=\operatorname{diag}((e^{2u}(2u-1)-3)/(3u^2),1)\) is strictly positive definite. Its largest eigenvalue is thus strictly increasing. The unique global minimum occurs at the crossing. There \(\lambda_-=\lambda_0\), and the determinant relation gives \(\lambda_+=u_*\). This proves the claimed spectrum and sharp constant.

Finally, for outer values \(y_j=(\mathcal L_rH)_{j+1}\), the exact inverse is
\[
a=(\mathcal L_rH)_0,\quad
b=\frac{e^u(y_0+y_1+y_2)/3-a}{u},\quad
c=\frac{e^u}{3\sqrt u}\sum_{j=0}^2y_j\zeta^{-j}.
\]
This establishes bijectivity, and injectivity on rank-one positive lifts proves phase recovery up to global phase.

## Verification
Run `python CHECK.py` with Python, NumPy, SciPy, SymPy and mpmath. It checks the Gram determinant and crossing identity symbolically, the rational Taylor bounds, the predicted singular values against direct real sampling matrices, and 150 independently generated Hermitian reconstruction tests. The output reports the root, radius and sharp condition number. The global uniqueness claim follows from the analytic derivative arguments above, not from the finite tests.

## Relationship to prior work
Recent work on phase retrieval from uniformly discrete sets establishes existence of sampling sets for all square-integrable signals with polynomial-Gaussian windows [1]. Its original Theorem 1.1 and finite-dimensional discrete norming proposition concern existence and norm control, and do not imply the fixed four-point radius optimum. General minimum-measurement results concern almost-everywhere recovery in finite complex dimensions [2]. Broad optimal-tomography results [3] and the tetrahedral-qubit construction [4] supply relevant context, but their generic or normalized-observable settings do not directly identify the **raw Gaussian-weighted** four-sample affine-Fock condition-number minimizer here. In particular, the canonical regular tetrahedral qubit rays use outer squared radius \(2\) in affine coordinates, whereas the present minimizer has \(u_*\in(1,4/3)\). This is not an optimization over all quantum tomographic measurements.

## Limitations
The result is finite-dimensional and design-family-specific. Measurement noise levels are assumed equal in the four raw recorded intensities when using the Euclidean output norm; physically different noise models yield different optimization criteria. The original full texts of [1] and [3] were inspected in the parts relevant to the present comparison; some other relevant full texts remained unavailable, and an earlier equivalent specialist calculation cannot be excluded. No independent external mathematical audit is asserted.

## References
[1] J. de Dios Pont, J. Greilhuber, L. Liehr, M. A. Taylor, *Phase retrieval from a uniformly discrete point set*, arXiv:2609.28341 (first posted 2026-09-23), https://arxiv.org/abs/2609.28341.

[2] Z. Xu, *The Minimal Measurement Number for Almost-Everywhere Complex Phase Retrieval*, arXiv:2608.15003 (2026), https://arxiv.org/abs/2608.15003.

[3] J. Nunn, B. J. Smith, G. Puentes, J. S. Lundeen, I. A. Walmsley, *Optimal experiment design revisited: fair, precise and minimal tomography*, arXiv:0911.4310 (2009), https://arxiv.org/abs/0911.4310.

[4] IBM Quantum Learning, *General measurements*, tetrahedral qubit example, https://learning.quantum.ibm.com/course/general-formulation-of-quantum-information/general-measurements.
