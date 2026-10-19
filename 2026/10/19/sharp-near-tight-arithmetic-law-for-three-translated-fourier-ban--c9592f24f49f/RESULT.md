# Sharp near-tight arithmetic law for three translated Fourier bands

## Finding
For any integer \(n\ge3\), set \(E_n=[0,1)\cup[1,2)\cup[n,n+1)\) and restrict to three frequency cosets
\[\mathcal E_{n,t}=\{e^{2\pi i(k+jt)x}:k\in\mathbb Z,\quad j\in\{0,1,2\}\}.\]
Let \(\rho_n\) denote the infimum over \(t\in\mathbb R/\mathbb Z\) of the optimal upper/lower **squared** Riesz-bound ratio, assigning infinity to singular systems. The perfect ratio \(\rho_n=1\) occurs when \(n\equiv2\pmod3\), by an existing root-of-unity criterion [2]. For the two non-perfect residue classes the new sharp first-order rate is
\[\boxed{\lim_{\substack{n\to\infty\\n\not\equiv2\ (\mathrm{mod}\ 3)}}n(\rho_n-1)=\frac{\pi(1+\sqrt3)}3.}\]
For \(s=-1\) if \(n\equiv0\pmod3\) and \(s=+1\) if \(n\equiv1\pmod3\), the explicit shifts
\[t_n=\frac13+\frac{s}{3n}+\frac{s}{6n^2}\]
achieve this asymptotic. The leading coefficient is optimal even among all continuously varying shifts, not only the displayed formula.

## Assumptions and scope
All Fourier integrals use Lebesgue measure and exponentials \(e^{2\pi i\xi x}\). The three unit intervals have disjoint interiors. A Riesz bound is a squared-norm bound for finite coefficient families, and the ratio uses its optimal upper and lower values. Frequencies are exactly the union of three translates of \(\mathbb Z\); no optimization over arbitrary non-coset bases is asserted. Write \(\omega=e^{2\pi i/3}\).

## Proof
**1. Exact fiber reduction.** Identifying \(L^2(E_n)\) with three copies of \(L^2([0,1))\), the exponentials at frequencies \(k+jt\) give the matrix
\[V_n(t)=(e^{2\pi i jrt})_{r\in\{0,1,n\},\ j\in\{0,1,2\}}.\]
Unitary Fourier synthesis on \([0,1)\), followed by multiplication by unitary phase factors, makes its optimal Riesz bounds the least and greatest eigenvalues of \(G_n(t)=V_n(t)V_n(t)^*\). Every diagonal element of \(G_n(t)\) equals \(3\). Therefore its trace is \(9\), and the ratio is \(\lambda_{\max}(G_n)/\lambda_{\min}(G_n)\).

**2. Known exact tightness criterion.** Put \(F(w)=1+w+w^2\). For distinct row positions \(r,r'\), their Gram entry is \(F(e^{2\pi i(r-r')t})\). Since the only unit-circle zeros of \(F\) are \(\omega\) and \(\omega^2\), all three off-diagonal entries vanish precisely when \(\{1,e^{2\pi it},e^{2\pi int}\}=\{1,\omega,\omega^2\}\). This is equivalent to \(n\equiv2\pmod3\); \(t=1/3\) works. This classification is the three-node instance of [2] and is not asserted as novel.

**3. Upper bound for non-tight congruence classes.** Fix \(n\equiv0\) or \(1\pmod3\). With the prescribed \(s\), put \(d=2\pi s/3\) and choose \(t_n=1/3+s/(3n)+s/(6n^2)\). Then the three circle nodes are \(1\), \(\omega e^{id/n+O(n^{-2})}\), and \(\omega^2e^{i(d/2)/n}\). The Taylor identities
\[F(\omega e^{i\varepsilon})=-\sqrt3\,\omega\varepsilon+O(\varepsilon^2),\qquad F(\omega^2 e^{i\varepsilon})=\sqrt3\,\omega^2\varepsilon+O(\varepsilon^2)\]
show, after fixed diagonal unitary conjugation, that
\[G_n(t_n)=3I+\frac{\sqrt3}{n}H(d/2,d)+O(n^{-2})\]
in operator norm, where
\[H(a,d)=\begin{pmatrix}0&-d&a\\-d&0&d-a\\a&d-a&0\end{pmatrix}.\]
At \(a=d/2\) its eigenvalues are \(d\), \(d(-1+\sqrt3)/2\), and \(d(-1-\sqrt3)/2\). Hence its spectral diameter is \((3+\sqrt3)|d|/2\). Eigenvalue continuity gives
\[n\left(\frac{\lambda_{\max}(G_n(t_n))}{\lambda_{\min}(G_n(t_n))}-1\right)\longrightarrow \frac{\sqrt3}{3}\cdot\frac{3+\sqrt3}{2}\cdot\frac{2\pi}{3}=\frac{\pi(1+\sqrt3)}3.\]

**4. Global optimality (no hidden favorable shifts).** The explicit construction yields \(\rho_n\le1+O(n^{-1})\). Choose an actual minimizing \(t_n^*\) (the ratio is continuous away from rank loss, diverges at rank loss, and a nonsingular shift exists). Since the three eigenvalues have mean \(3\), the bound \(\rho_n\le1+O(n^{-1})\) forces \(G_n(t_n^*)=3I+O(n^{-1})\) in operator norm. The three off-diagonal values of \(F\) are thus \(O(n^{-1})\). Since the two zeros of \(F\) on the circle are simple, the three nodes form an \(O(n^{-1})\) perturbation of an equilateral triangle. Complex conjugation permits choosing the orientation with \(t_n^*=1/3+O(n^{-1})\) and \(nt_n^*\equiv2/3+O(n^{-1})\pmod1\).

Let \(d_n=2\pi n(t_n^*-1/3)\). The equilateral constraint makes \(d_n\) a bounded sequence whose distance from the discrete arithmetic set \(2\pi(\mathbb Z+(2-r)/3)\) tends to zero, with \(r=n\bmod3\in\{0,1\}\). Every convergent subsequence therefore has a limit \(d\) with \(|d|\ge2\pi/3\). Choose an integer \(k_n\) so that \(\varepsilon_n=nt_n^*-2/3-k_n=O(n^{-1})\), and set \(a_n=2\pi n\varepsilon_n\); this sequence is bounded too. Passing to a subsequence, \(a_n\to a\), and the same Taylor expansion gives
\[n(\rho_n-1)\longrightarrow\frac{\sqrt3}{3}\bigl(\lambda_{\max}(H(a,d))-\lambda_{\min}(H(a,d))\bigr).\]
The spectral diameter of a real symmetric affine matrix is convex in \(a\), because largest eigenvalues are convex and smallest eigenvalues concave. The matrix \(H(d-a,d)\) is obtained from \(H(a,d)\) by swapping its first two coordinates. Thus its spectral diameter is symmetric about \(a=d/2\), and convexity implies it is minimized at \(a=d/2\). Using the eigenvalues already computed,
\[\lambda_{\max}(H(a,d))-\lambda_{\min}(H(a,d))\ge\frac{3+\sqrt3}{2}|d|\ge\frac{(3+\sqrt3)\pi}{3}.\]
This lower bound applies to any subsequential limit of minimizing shifts, hence to the full limit inferior along both residue classes. Combined with the upper construction it proves the claimed limit. \(\square\)

## Verification
The standalone `verify.py` uses NumPy to compare the actual singular-value ratios for multiple non-tight values up to \(n=1201\), checks exact orthogonality when \(n\equiv2\pmod3\), verifies the linearized spectral-diameter formula and the real symmetric minimax inequality at finitely many parameters. The checker emits `VERIFY_OK` on success. The proof of optimality for infinitely many \(n\) is analytic and does not rely on finite tests.

## Relationship to prior work
Asipchuk and De Carli [1] establish a matrix fiber criterion for exponential bases on multi-rectangles and motivate explicit control of conditioning. Berman and Feuer [2] give the **known** perfect-conditioning criterion for unit-circle Vandermonde matrices; it already settles the tight congruence class in this setting. The contribution here is the sharp **non-tight first-order deterioration constant** when perfect conditioning is arithmetically forbidden. General separated-node singular-value bounds, such as Kunis--Nagel--Strotmann [3], do not immediately compute the optimized family-specific coefficient. The non-tight asymptotic is compared to, but not logically implied by, existing finite-cycle three-site conditioning results, where the optimization is over discrete frequency sets rather than a continuous shift constrained by a growing geometric gap.

## Limitations
This is an asymptotic statement, not an exact formula for finite non-tight \(n\). The Riesz basis family is restricted to three equally spaced frequency cosets; better unconstrained spectra are not excluded. The theorem says nothing about perturbation/noise beyond the squared linear condition ratio. An unindexed equivalent asymptotic calculation remains a historical-priority risk. Independent verification has not been performed.

## References
1. O. Asipchuk and L. De Carli, *Methods of Construction of Exponential Bases on Planar Domains*, arXiv:2505.00870 (first public 2025-05-01); *Bull. Malays. Math. Sci. Soc.* 49, article 133 (2026), DOI: 10.1007/s40840-026-02112-7. Full journal text: https://link.springer.com/article/10.1007/s40840-026-02112-7.
2. L. Berman and A. Feuer, *On Perfect Conditioning of Vandermonde Matrices on the Unit Circle*, *Electronic Journal of Linear Algebra* 16 (2007), 157--161, DOI: 10.13001/1081-3810.1190. Full text: https://journals.uwyo.edu/index.php/ela/article/download/437/437/437.
3. S. Kunis, D. Nagel, and A. Strotmann, *Multivariate Vandermonde Matrices with Separated Nodes on the Unit Circle Are Stable*, *Applied and Computational Harmonic Analysis* 58 (2022), 50--59, DOI: 10.1016/j.acha.2022.01.001.
