# Arithmetic discontinuity of sharp singular-value residues for finite rotation sums

## Finding

For every real \(\alpha>0\), let \(\mathcal D_{1+2\alpha}\) denote the analytic coefficient Hilbert space with
\[
\left\|\sum_{k\ge0}f_kz^k\right\|_{\mathcal D_{1+2\alpha}}^2
=\sum_{k\ge0}(k+1)^{-2\alpha}|f_k|^2.
\]
Fix pairwise distinct rotations \(\rho_1,\ldots,\rho_r\in\mathbb T\) and nonzero coefficients \(a_1,\ldots,a_r\in\mathbb C\), with \(r\ge1\). Consider
\[
Tf(z)=\sum_{j=1}^r a_j f(\rho_jz):H^2(\mathbb D)\longrightarrow\mathcal D_{1+2\alpha}.
\]
Write \(\rho=(\rho_1,\ldots,\rho_r)\), \(G=\overline{\{\rho^k:k\in\mathbb Z\}}\subset\mathbb T^r\), and let \(\mu_G\) be normalized Haar probability measure. Define the positive constant
\[
M_\alpha=\int_G\left|\sum_{j=1}^r a_jz_j\right|^{1/\alpha}\,d\mu_G(z)>0.
\]
Then \(T\) is compact and its singular values satisfy the **sharp asymptotic**
\[
\boxed{\displaystyle\lim_{n\to\infty}n^\alpha s_n(T)=M_\alpha^\alpha.}
\]
Equivalently, if \(N_T(t)=\#\{n\ge1:s_n(T)>t\}\), then
\[
\lim_{t\downarrow0}t^{1/\alpha}N_T(t)=M_\alpha.
\]
For every \(p>0\), the sharp ideal criterion is \(T\in\mathcal S_p\) exactly when \(p>1/\alpha\). At \(p=1/\alpha\), the operator lies in \(\mathcal S_{p,\infty}\setminus\mathcal S_p\), where \(\mathcal S_{p,\infty}\) means \(\sup_{n\ge1}n^{1/p}s_n<\infty\) and
\[
\lim_{N\to\infty}\frac{1}{\log N}\sum_{n=1}^N s_n(T)^{1/\alpha}=M_\alpha.
\]

A particularly explicit arithmetic phenomenon occurs when \(\alpha=1\), \(r=2\), \(\rho_1=1\), \(\rho_2=e^{i\theta}\), and both coefficients equal \(1\). Put
\[
T_\theta f(z)=f(z)+f(e^{i\theta}z):H^2\longrightarrow\mathcal D_3,
\qquad c(\theta)=\lim_{n\to\infty}n\,s_n(T_\theta).
\]
The limit exists for every real angle and is
\[
\boxed{c(\theta)=
\begin{cases}
4/\pi,&\theta/(2\pi)\notin\mathbb Q,\\[2mm]
\dfrac{2}{b}\csc\bigl(\dfrac{\pi}{2b}\bigr),&\theta/(2\pi)=a/b\in\mathbb Q,\quad b\text{ odd},\\[3mm]
\dfrac{2}{b}\cot\bigl(\dfrac{\pi}{2b}\bigr),&\theta/(2\pi)=a/b\in\mathbb Q,\quad b\text{ even},
\end{cases}}
\]
where \(a/b\) is reduced and \(b\ge1\). Moreover,
\[
\|T_\theta-T_\phi\|_{H^2\to\mathcal D_3}\le|\theta-\phi|.
\]
Nevertheless \(c\) is discontinuous at **every rational** value of \(\theta/(2\pi)\) and continuous at **every irrational** value. Odd denominators give \(c(\theta)>4/\pi\); even denominators give \(c(\theta)<4/\pi\).

## Assumptions and scope

All spaces are complex Hilbert spaces of analytic functions on the unit disk, with the *exact coefficient norm* displayed above rather than any merely equivalent derivative or area-integral norm. The Hardy space \(H^2\) has its standard coefficient orthonormal basis \((z^k)_{k\ge0}\). The rotations are pairwise distinct; zero coefficients can instead be discarded. Singular values \(s_n\) are arranged nonincreasingly, including multiplicities. The parameter \(\alpha\) is arbitrary and positive. The two-rotation discontinuity is a statement about the sharp leading singular-value coefficient, **not** about discontinuity of the operators in norm.

## Proof

**1. Exact reduction to a scalar diagonal.** Put \(b_k=\sum_{j=1}^r a_j\rho_j^k\). On Hardy monomials,
\[
Tz^k=b_kz^k,
\qquad \|Tz^k\|_{\mathcal D_{1+2\alpha}}=(k+1)^{-\alpha}|b_k|.
\]
The images of different monomials are orthogonal. Thus the singular values of \(T\) are exactly the nonincreasing rearrangement of the values
\[
 d_k=(k+1)^{-\alpha}|b_k|\quad(k\ge0).
\]
Since \(|b_k|\le\sum_j|a_j|\), these diagonal values tend to zero, proving compactness.

**2. Haar equidistribution, including the moving cutoff.** The compact monothetic group \(G\) is the closure of the integer orbit of \(\rho\). For any continuous character \(\chi\) of \(G\), either \(\chi\equiv1\) or \(\chi(\rho)\ne1\), by density. The character Cesàro averages therefore converge to their Haar integrals by the elementary finite geometric-series formula. Finite linear combinations of characters are uniformly dense in \(C(G)\); consequently \((\rho^k)_{k\ge0}\) equidistributes for \(\mu_G\).

The needed strengthened form is as follows: for each \(B>0\) and continuous \(F:[0,B]\times G\to\mathbb C\),
\[
\lim_{L\to\infty}\frac1L\sum_{\substack{k\ge0\\k+1\le BL}} F((k+1)/L,\rho^k)
=\int_0^B\int_G F(x,z)\,d\mu_G(z)\,dx.
\]
First take \(F(x,z)=f(x)\chi(z)\). For the trivial character this is a Riemann sum; for a nontrivial character the geometric-series partial sums are uniformly bounded, so summation by parts gives zero for Lipschitz \(f\). Approximate arbitrary continuous \(f\) uniformly by Lipschitz functions. Products of continuous functions in \(x\) and characters in \(z\) are uniformly dense in the continuous functions on the product, establishing the asserted convergence.

Let \(g(z)=|\sum_j a_jz_j|\) and \(S=\sum_j|a_j|\). For \(L>0\), the inequality \(d_k>L^{-\alpha}\) is equivalent to
\[
 g(\rho^k)>((k+1)/L)^\alpha.
\]
There are no solutions when \(k+1>LS^{1/\alpha}\). Choose fixed \(B>S^{1/\alpha}\). The indicator of \(\{(x,z):g(z)>x^\alpha\}\) on \([0,B]\times G\) has a boundary of product measure zero: for fixed \(z\), equality determines at most one value \(x\ge0\). Continuous approximation to that indicator and the product equidistribution law therefore imply
\[
\begin{aligned}
\lim_{L\to\infty}\frac{N_T(L^{-\alpha})}{L}
&=\int_0^B \mu_G\{z:g(z)>x^\alpha\}\,dx\\
&=\int_G g(z)^{1/\alpha}\,d\mu_G(z)=M_\alpha,
\end{aligned}
\]
where the last identity is Tonelli's layer-cake formula. Replacing \(L\) by \(t^{-1/\alpha}\) proves the counting asymptotic for every real \(t\downarrow0\).

The constant is strictly positive. Indeed, the distinct rotations give
\[
\int_G g(z)^2\,d\mu_G(z)
=\lim_{K\to\infty}\frac1K\sum_{k=0}^{K-1}|b_k|^2
=\sum_{j=1}^r|a_j|^2>0,
\]
since the cross-term averages are nontrivial geometric progressions. Thus \(g\) is positive on a set of positive Haar measure, and \(M_\alpha>0\).

**3. Singular-value inversion and critical ideals.** From
\(N_T(t)\sim M_\alpha t^{-1/\alpha}\), the standard monotone counting inversion (apply the two-sided bounds with \(M_\alpha\pm\varepsilon\), and let \(\varepsilon\downarrow0\)) yields
\[
 s_n(T)\sim M_\alpha^\alpha n^{-\alpha}.
\]
Therefore \(\sum_ns_n(T)^p\) converges exactly when \(\alpha p>1\), and \(n^{\alpha}s_n(T)\) is bounded. At the critical exponent, \(s_n(T)^{1/\alpha}=M_\alpha/n+o(1/n)\); harmonic summation gives the displayed logarithmic average.

**4. Exact two-rotation coefficient and arithmetic discontinuity.** In the special case, the relevant orbit function is
\[
|1+e^{ik\theta}|=2|\cos(k\theta/2)|.
\]
If \(\theta/(2\pi)\) is irrational, the orbit is uniformly distributed on the circle, so
\[
 M_1=\frac1{2\pi}\int_0^{2\pi}2|\cos(t/2)|\,dt=\frac4\pi.
\]
For a reduced rational angle with denominator \(b\), the orbit visits each \(b\)-th root of unity once. Finite trigonometric progression sums yield
\[
\sum_{k=0}^{b-1}\left|\cos\frac{\pi k}{b}\right|
=\begin{cases}
\csc(\pi/(2b)),&b\text{ odd},\\
\cot(\pi/(2b)),&b\text{ even}.
\end{cases}
\]
(The identities follow by splitting the positive and negative cosine terms and summing each geometric progression.) This proves the stated finite-cyclic values, independent of the numerator. Writing \(x=\pi/(2b)>0\), the odd case has \(c=(4/\pi)(x/\sin x)>4/\pi\); the even case has \(c=(4/\pi)x\cot x<4/\pi\). Both expressions tend to \(4/\pi\) as \(b\to\infty\). Approximating any rational angle by irrationals proves discontinuity there. At an irrational angle, any convergent sequence of distinct rational angles has denominators tending to infinity, while the irrational values already equal \(4/\pi\); hence continuity holds there.

Finally the exact monomial diagonal of the difference gives
\[
\|T_\theta-T_\phi\|
=\sup_{k\ge0}\frac{|e^{ik\theta}-e^{ik\phi}|}{k+1}
\le\sup_{k\ge0}\frac{k|\theta-\phi|}{k+1}
\le|\theta-\phi|,
\]
proving norm-Lipschitz dependence despite the arithmetic discontinuity of \(c\).

## Verification

The accompanying standalone `checker.py` tests finite trigonometric sums for denominators \(1\le b\le100\), strict odd/even inequalities, finite-cutoff approximations to the singular-value constants for representative rational and irrational angles, and sampled norm-Lipschitz bounds. It has passed 3,209 finite assertions. Those checks are not used to infer the infinite asymptotics: the proof above uses exact diagonalization, a character argument, product equidistribution, and monotone counting inversion. A standard Python interpreter suffices to run `python checker.py`.

## Relationship to prior work

Sun and Liu [1, Section 9.2, Theorem 9.2] determine the singular values for individual monomial-weight, linear-symbol composition–differentiation operators between coefficient Dirichlet Hilbert spaces. The one-rotation diagonal is therefore prior mathematics. The present result concerns finite *superpositions*, their oscillatory cancellations, and the resulting sharp reordering asymptotic and arithmetic discontinuity; these are not supplied by the single-symbol theorem.

Du and Liu [2] analyze sums of two generalized weighted composition operators on Bergman spaces, focusing on boundedness, compactness, and norm/essential-norm behavior rather than exact singular-value residues of unit-circle rotation superpositions. Sen, Barik, and Paul [3] characterize mapping and Hilbert–Schmidt properties for composition–differentiation operators, not the two-scale asymptotic above. Classical almost-periodic Szegő-type results [4] address determinant asymptotics for finite sections of a different unweighted operator setup; broader almost-periodic spectral theory remains a possible indirect route to parts of the argument.

## Limitations

The theorem uses the exact coefficient Hilbert norm; equivalent norms do not preserve the displayed numerical constants. It concerns finite rotation sums and compact embeddings of \(H^2\) into the indicated Hilbert scale; it does not claim an analogous law for arbitrary nonlinear composition symbols or for infinite measures of rotations. No uniform rate of singular-value convergence in the angle or coefficients is established. Independence from older, general-purpose compact diagonal or almost-periodic rearrangement theorems is not certified; mathematical priority and independent validation remain open.

## References

[1] J. Sun and J. Liu, *Weighted composition--differentiation operators on mixed-norm, derivative Hardy and F(p,q,s) spaces*, arXiv:2610.19658, first public submission 2026-10-14, Theorem 9.2. https://arxiv.org/abs/2610.19658

[2] J. Du and Z. Liu, *Sums of two generalized weighted composition operators between Bergman spaces*, arXiv:2509.01094, first public submission 2025-09-01. https://arxiv.org/abs/2509.01094

[3] A. Sen, S. Barik, and K. Paul, *Composition-differentiation operators on weighted Dirichlet spaces*, arXiv:2605.00213, first public submission 2026-04-30. https://arxiv.org/abs/2605.00213

[4] T. Ehrhardt and Z. Zhou, *Asymptotics of determinants for finite sections of operators with almost periodic diagonals*, Journal of Functional Analysis (2019), arXiv:1811.09892. https://arxiv.org/abs/1811.09892
