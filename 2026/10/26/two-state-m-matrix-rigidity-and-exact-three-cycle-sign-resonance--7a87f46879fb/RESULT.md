# Two-state M-matrix rigidity and exact three-cycle sign resonances of the inverse \(\varphi_1\) function

## Finding
Let \(\varphi_1(z)=(e^z-1)/z\), continuously extended by \(\varphi_1(0)=1\), and let \(Q\) be a finite-state continuous-time Markov generator (nonnegative off-diagonal entries, zero row sums). For any positive time \(t\), define the time-averaged transition matrix \(F_t=\varphi_1(tQ)=\int_0^1e^{stQ}\,ds\).

**Sharp minimal dimension.** For every generator on one or two states and every \(t>0\), \(F_t\) is invertible and \(F_t^{-1}\) is a nonsingular M-matrix: its off-diagonal entries are nonpositive, its diagonal entries are positive, and its inverse is entrywise nonnegative. There exists a three-state generator for which the assertion fails at every positive time: the irreducible directed-cycle generator \(Q=C-I_3\), where
\[
C=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix}.
\]

More precisely, for every \(t>0\) the circulant inverse has the form
\[
F_t^{-1}=b_0(t)I_3+b_1(t)C+b_2(t)C^2,
\qquad b_0(t)>0,\quad b_1(t)<0,\quad b_2(t)>0.
\]
Writing \(h=\sqrt3\,t/2\), the strictly positive two-jump coefficient has the exact formula
\[
\boxed{\displaystyle b_2(t)=\frac13-\frac{2h\sin h}{3\bigl(\cosh(\sqrt3h)-\cos h\bigr)}.}
\]
Consequently \(b_2(t)=1/3\) exactly at the discrete positive times \(t=2k\pi/\sqrt3\), \(k=1,2,\ldots\). Its deviation from \(1/3\) alternates sign on consecutive intervening intervals, and is \(O(t e^{-3t/2})\). Thus the inverse's two-jump sign stays positive at all times even as its excess over the limiting coefficient exhibits infinitely many damped resonances.

## Assumptions and scope
A real \(d\times d\) Markov generator satisfies \(Q_{ij}\ge0\) for \(i\ne j\) and \(Q\mathbf1=0\). No reversibility is assumed. All matrix functions, inequalities, and signs concern exact real arithmetic and \(t>0\). The two-state assertion allows zero jump rates (including the zero generator). The three-state assertion concerns the specified equal-rate directed cycle and includes all positive time scales. A nonsingular M-matrix here means a real Z-matrix (all off-diagonal entries nonpositive) with an entrywise nonnegative inverse; strict row diagonal dominance is sufficient but not assumed a priori. The coefficient \(b_2\) denotes the \(C^2\) term, i.e., the direct two-jump direction, not an arbitrary off-diagonal position.

## Proof
**Two states.** Write \(Q=\begin{pmatrix}-a&a\\b&-b\end{pmatrix}\) with \(a,b\ge0\), and put \(r=a+b\). If \(r=0\), then \(F_t=I_2\). Otherwise \(Q^2=-rQ\), so the functional calculus of a matrix with eigenvalues \(0\) and \(-r\) gives
\[
F_t^{-1}=I_2-\gamma_t Q,\qquad
\gamma_t=\frac{\frac{tr}{1-e^{-tr}}-1}{r}>0.
\]
Indeed the nontrivial eigenvalue of \(F_t^{-1}\) equals \((-tr)/(e^{-tr}-1)=tr/(1-e^{-tr})\). Therefore the off-diagonal entries of \(F_t^{-1}\) are \(-\gamma_t a\) and \(-\gamma_t b\); its diagonal entries are \(1+\gamma_t a\) and \(1+\gamma_t b\). Since \(e^{stQ}\) is entrywise nonnegative and stochastic for every \(s\ge0\), \(F_t\) itself is entrywise nonnegative. This establishes the M-matrix assertion. The one-state case is immediate.

**Three-state algebra.** Fix \(Q=C-I_3\) and write \(F_t=a_0I_3+a_1C+a_2C^2\). The representation \(e^{st(C-I)}=e^{-st}\sum_{n\ge0}(st)^nC^n/n!\) shows that the coefficients of \(e^{tQ}=p_0I+p_1C+p_2C^2\) satisfy \(p_j>0\) for all \(j\in\{0,1,2\}\). The matrix integral gives the exact identity
\[
F_t\,tQ=e^{tQ}-I.
\]
Comparing the \(C\) and \(C^2\) coefficients gives \(t(a_0-a_1)=p_1>0\) and \(t(a_1-a_2)=p_2>0\), so \(a_0>a_1>a_2>0\). Let \(\Delta=\det F_t\). The eigenvalues of \(tQ\) are \(0\) and \(z=-3t/2+ih\) and its conjugate, where \(h=\sqrt3t/2\). Because \(\operatorname{Re}z<0\), \(\varphi_1(z)\ne0\), hence
\[
\Delta=|\varphi_1(z)|^2>0.
\]
The adjugate of a three-by-three circulant now gives
\[
 b_0=\frac{a_0^2-a_1a_2}{\Delta}>0,\qquad
 b_1=\frac{a_2^2-a_0a_1}{\Delta}<0,\qquad
 b_2=\frac{a_1^2-a_0a_2}{\Delta}.
\]

**Exact two-jump coefficient and its strict sign.** Set \(\omega=e^{2\pi i/3}\), \(\rho=e^{-3t/2}=e^{-\sqrt3h}\), and note that \(C\) has eigenvalues \(1,\omega,\overline\omega\). At \(\omega\) the eigenvalue of \(F_t^{-1}\) is
\[
\psi(z)=\frac{z}{e^z-1}=\frac{\sqrt3h-ih}{1-\rho e^{ih}}.
\]
Recovering the three real circulant coefficients by the inverse discrete Fourier transform, and using \(1-2\rho\cos h+\rho^2=2\rho(\cosh(\sqrt3h)-\cos h)\), yields
\[
 b_2=\frac{\cosh(\sqrt3h)-\cos h-2h\sin h}{3(\cosh(\sqrt3h)-\cos h)}.
\]
The denominator is strictly positive. The numerator admits the globally convergent expansion
\[
\cosh(\sqrt3h)-\cos h-2h\sin h
=\sum_{k=2}^{\infty}\frac{3^k+(-1)^k(4k-1)}{(2k)!}\,h^{2k}.
\]
All coefficients are strictly positive: for even \(k\) this is obvious; for odd \(k\ge3\), \(3^k>4k-1\), starting at \(k=3\) and persisting inductively. Hence \(b_2(t)>0\) for every positive \(t\), not merely for small steps. It follows that \(F_t^{-1}\) has a positive off-diagonal entry and is not a Z-matrix, proving sharpness of the dimension-two theorem.

**Exact resonance set.** Since the denominator is positive, \(b_2(t)-1/3\) has sign \(-\operatorname{sign}(\sin h)\). It vanishes precisely when \(h=k\pi\) with positive integer \(k\). The elementary asymptotic \(\cosh(\sqrt3h)-\cos h\sim\tfrac12e^{\sqrt3h}\) proves \(|b_2(t)-1/3|=O(h e^{-\sqrt3h})=O(t e^{-3t/2})\). This proves all statements.

## Verification
Install dependencies from `requirements.txt` and run `python verify.py`. The standalone script builds \(\varphi_1\) independently via its convergent matrix Taylor series, inverts the resulting matrices at 13 positive parameter values, and checks the circulant coefficient identity, inverse residual, and strict signs at high precision. It also checks five exact resonance values, the first 20 coefficients in the analytic positivity series, and four two-state generators including absorbing cases. The script reports \(\texttt{VERIFY_OK 88}\). These finite checks independently test normalization and signs; the analytic series argument above, not their numerical coverage, proves positivity for every real \(t>0\).

## Relationship to prior work
Gemignani's 2023 study [1] treats inverse matrix \(\varphi\)-functions in general, including numerical inverse problems, and explicitly identifies the Bernoulli expansion for the reciprocal \(\varphi_1\)-function. Boito, Eidelman and Gemignani [2] previously constructed rational approximations for this reciprocal; their numerical experiments include cyclic permutation matrices, and their theorems cover approximation and entrywise magnitude decay for symmetric band matrices. Those results supply important foundations but do not state the all-time sign classification for inverse time-averaged Markov transitions, the universal two-state boundary, or the exact three-state oscillatory coefficient. The local positive two-jump Taylor coefficient follows from the classical Bernoulli series and is not asserted as independently new here. The contribution is the global strict sign together with the exact resonance set and minimal-dimensional characterization. Aceto and Gemignani's later work [3] develops efficient Bernoulli matrix-function action algorithms; the available full preprint and publisher overview do not identify these Markov sign results. A hidden equivalent application of earlier general matrix-function identities remains possible.

## Limitations
The positive two-jump formula is specific to the equal-rate three-cycle. It does not assert this precise oscillation for arbitrary three-state generators or larger cycle sizes. The theorem concerns signs of the **inverse** of an exactly evaluated positive averaged semigroup; it makes no claim about finite-precision stability or the sign of approximate inverses. The observed resonance around \(1/3\) is an exact algebraic/spectral feature, not a physical periodic orbit of the Markov chain. The calculation is not a theorem about all inverse \(\varphi_\ell\)-functions. Literature overlap has been evaluated on a best-knowledge basis, not independently certified.

## References
[1] L. Gemignani, *Efficient Inversion of Matrix \(\varphi\)-Functions of Low Order*, first publicly available 15 February 2023, arXiv:2302.07565, https://arxiv.org/abs/2302.07565 (especially §§1–3 and 5).

[2] P. Boito, Y. Eidelman and L. Gemignani, *Computing the Reciprocal of a \(\varphi\)-Function by Rational Approximation*, first publicly available 14 January 2018, arXiv:1801.04573, https://arxiv.org/abs/1801.04573 (especially §§1–3).

[3] L. Aceto and L. Gemignani, *Computing the Action of the Generating Function of Bernoulli Polynomials on a Matrix with An Application to Non-local Boundary Value Problems*, arXiv:2406.01437, https://arxiv.org/abs/2406.01437; journal version, *Advances in Computational Mathematics* 51 (2025), article 19.
