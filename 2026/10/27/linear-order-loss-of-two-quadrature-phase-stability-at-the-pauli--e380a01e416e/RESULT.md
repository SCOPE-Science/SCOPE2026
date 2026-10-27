# Linear-order loss of two-quadrature phase stability at the Pauli angle in three Hermite modes

## Finding
Let \(h_0,h_1,h_2\) be the first three orthonormal Hermite functions, \(\mathcal F_\theta h_j=e^{-ij\theta}h_j\), and \(I_\theta(u)=|\mathcal F_\theta u|^2\). For coefficient vectors \(u,v\in\mathbb C^3\), put \(H=uu^*-vv^*\) and define the sharp global lifted-intensity stability constant
\[
s(\delta)=\inf_{uu^*\ne vv^*}\frac{\bigl(\|I_0(u)-I_0(v)\|_{L^2(\mathbb R)}^2+\|I_\delta(u)-I_\delta(v)\|_{L^2(\mathbb R)}^2\bigr)^{1/2}}{\|H\|_F}.
\]
There exist constants \(\varepsilon,c,C>0\) such that, for every real \(\delta\) with \(0<|\delta-\pi/2|<\varepsilon\),
\[
 c|\delta-\pi/2|\le s(\delta)\le C|\delta-\pi/2|,
\]
while \(s(\pi/2)=0\). Hence the global stability degradation has **exactly linear order** at the position/momentum (Pauli) pair. The coefficient is not claimed optimal.

## Assumptions and scope
All functions are on \(\mathbb R\), with Lebesgue measure, and the standard normalized Hermite basis
\[
h_0(x)=\pi^{-1/4}e^{-x^2/2},\quad h_1(x)=\sqrt2\,xh_0(x),\quad h_2(x)=\frac{2x^2-1}{\sqrt2}h_0(x).
\]
The fractional Fourier convention is specified by its Hermite eigenvalues. A common overall FrFT phase does not affect intensities. Coefficient vectors need not have norm one; the quotient is homogeneous of degree zero. The Frobenius norm is \(\|H\|_F=(\operatorname{tr}H^*H)^{1/2}\). The stability assertion concerns the pair of entire real-axis intensity functions in \(L^2\), not noisy point samples or reconstruction outside the three-mode subspace.

## Proof
**1. Exact linear measurement kernel.** For any Hermitian \(3\times3\) matrix \(H\), define
\[
\mathcal Q_\theta(H)(x)=\sum_{j,k=0}^2 H_{jk}e^{i(k-j)\theta}h_j(x)h_k(x),\qquad \mathcal M_\delta(H)=(\mathcal Q_0(H),\mathcal Q_\delta(H)).
\]
The identity \(\mathcal Q_\theta(uu^*-vv^*)=I_\theta(u)-I_\theta(v)\) is immediate. Divide by the strictly positive \(h_0(x)^2\), and set \(R_\theta=\Re(H_{02}e^{2i\theta})\). The resulting degree-four real polynomial is
\[
H_{00}+2H_{11}x^2+\frac{H_{22}}2(2x^2-1)^2
+2\sqrt2\Re(H_{01}e^{i\theta})x
+\sqrt2 R_\theta(2x^2-1)
+2\Re(H_{12}e^{i\theta})x(2x^2-1).
\]
For \(0<\delta<\pi\), vanishing at both angles forces, by the coefficients of \(x^4,x^3,x\), respectively \(H_{22}=H_{12}=H_{01}=0\); the remaining constant and quadratic coefficients require \(H_{00}=\sqrt2R_0=\sqrt2R_\delta\) and \(H_{11}=-\sqrt2R_0\). Since \(\sin\delta\ne0\), the real-linear equation \(\Re H_{02}=\Re(H_{02}e^{2i\delta})\) has solutions \(H_{02}=t e^{-i\delta}\) with real \(t\). Thus the entire kernel is one-dimensional:
\[
\ker\mathcal M_\delta=\mathbb RK_\delta,\qquad
K_\delta=\begin{pmatrix}\sqrt2\cos\delta&0&e^{-i\delta}\\0&-\sqrt2\cos\delta&0\\e^{i\delta}&0&0\end{pmatrix}.
\]
Direct evaluation yields \(\det K_\delta=\sqrt2\cos\delta\), \(\|K_\delta\|_F=\sqrt{2+4\cos^2\delta}\). The one-dimensional zero singular space is valid even at \(\delta=\pi/2\); the remaining eight singular values of \(\mathcal M_\delta\) are strictly positive.

**2. Uniform transverse lower bound.** By continuity in the eight-dimensional orthogonal complement of its kernel, the family of finite-dimensional maps \(\mathcal M_\delta\colon\operatorname{Herm}(3)\to L^2(\mathbb R)^2\) has a positive lower singular value \(m\), uniform for \(\delta\) in a sufficiently small compact neighborhood of \(\pi/2\), on \((\mathbb RK_\delta)^\perp\). Explicitly, for every Hermitian \(H\),
\[
\|\mathcal M_\delta H\|\ge m\operatorname{dist}_F(H,\mathbb RK_\delta).
\]
The smallest absolute eigenvalue of \(K_\delta\) is \(\sqrt2|\cos\delta|\) near \(\pi/2\): one eigenvalue is \(-\sqrt2\cos\delta\) and the other two are the eigenvalues of the \(2\times2\) block on coordinates zero and two, which approach \(\pm1\). Any difference \(H=uu^*-vv^*\) has rank at most two. Write its orthogonal decomposition \(H=tK_\delta+R\). By the Eckart--Young minimum-distance theorem, or directly Weyl's eigenvalue inequality, the Frobenius distance from \(tK_\delta\) to matrices of rank at most two is \(|t|\sqrt2|\cos\delta|\); hence \(\|R\|_F\ge |t|\sqrt2|\cos\delta|\). Consequently,
\[
\operatorname{dist}_F(H,\mathbb RK_\delta)=\|R\|_F\ge
\frac{\sqrt2|\cos\delta|}{\sqrt{2+4\cos^2\delta}+\sqrt2|\cos\delta|}\|H\|_F.
\]
Combining inequalities yields a positive lower multiple of \(|\cos\delta|\), which is comparable to \(|\delta-\pi/2|\) near the Pauli angle. No finite experiments enter this argument.

**3. Sharp-order upper witness.** Let \(u=(e_0+i e_2)/\sqrt2\) and \(v=(e_0-i e_2)/\sqrt2\) be coefficient vectors; both are unit vectors and not phase equivalent. Their lifted difference is \(H_*=uu^*-vv^*=K_{\pi/2}\), of Frobenius norm \(\sqrt2\). The first intensity difference vanishes. The second is exactly \(2\sin(2\delta)h_0h_2\). By Gaussian integration,
\[
\|h_0h_2\|_{L^2}^2=\frac{3}{8\sqrt{2\pi}}.
\]
Thus
\[
 s(\delta)\le\sqrt2\|h_0h_2\|_{L^2}|\sin(2\delta)|,
\]
which gives the matching upper multiple of \(|\delta-\pi/2|\), and vanishes at \(\delta=\pi/2\). For \(0<\delta<\pi\) with \(\delta\ne\pi/2\), \(K_\delta\) is invertible and therefore no nonzero difference of two rank-one matrices lies in the measurement kernel, establishing injectivity on pure states. This last qualitative fact is already implicit in earlier Hermite phase-retrieval theory; the **two-sided quantitative rate** is the claim here.

## Verification
The accompanying `checker.py` independently assembles the Hermitian measurement operator from normalized Hermite functions and Gauss--Hermite quadrature. It tests kernel rank and kernel vectors at six angles, the exact determinant formula, and the explicit witness at three distances from \(\pi/2\). For the tested values the eight nonzero singular values remain bounded away from zero, while the witness-to-distance ratio tends to a positive constant. These tests are finite corroboration only: the proof of the all-angle local bounds is above and does not depend on them.

## Relationship to prior work
P. Jaming, *Uniqueness results for the phase retrieval problem of fractional Fourier transforms of variable order*, arXiv:1009.3418v1 (17 September 2010), Theorem 5.5 and Remark 5.7, proves qualitative two-angle uniqueness for bounded Hermite expansions under nonresonant angular conditions, and discusses the exceptional Pauli geometry. Its proof does not give a sharp-order global intensity-stability law as the two angles approach \(\pi/2\).
D. Sych et al., *Informational completeness of continuous-variable measurements*, arXiv:1211.4967v1 (2012), Eq. (6) and Table I, give the mixed-state linear measurement rank for multiple quadrature settings; the two-setting three-mode rank is eight. This is consistent with the kernel calculation but not a quantitative pure-state stability bound near the Pauli angle. General finite-dimensional phase-retrieval stability principles (for example A. S. Bandeira et al., arXiv:1302.4618v1, 2013) motivate using a lifted norm but do not specify this Hermite angular singular limit. No claim of independent novelty certification is made.

## Limitations
The result concerns a precise three-dimensional Hermite truncation and two entire-intensity measurements in the specified \(L^2\) norm. It supplies the optimal **exponent one**, not the best multiplicative asymptotic constant, and does not classify stability for more Hermite modes, alternate observation norms, or finitely sampled/noisy data. Earlier equivalent quantitative treatments in other quadrature-tomography terminology cannot be excluded without a broader independent literature audit.

## References
- Philippe Jaming, *Uniqueness results for the phase retrieval problem of fractional Fourier transforms of variable order*, arXiv:1009.3418v1 (2010), especially Theorem 5.5 and Remarks 5.6--5.7, https://arxiv.org/pdf/1009.3418.
- D. Sych et al., *Informational completeness of continuous-variable measurements*, arXiv:1211.4967 (2012), Equation (6) and Table I, https://arxiv.org/pdf/1211.4967.
- A. S. Bandeira, J. Cahill, D. G. Mixon and A. A. Nelson, *Saving phase: Injectivity and stability for phase retrieval*, arXiv:1302.4618 (2013), https://arxiv.org/abs/1302.4618.
