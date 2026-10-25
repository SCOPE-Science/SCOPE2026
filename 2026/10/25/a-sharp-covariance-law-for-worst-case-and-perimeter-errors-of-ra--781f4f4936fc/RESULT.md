# A sharp covariance law for worst-case and perimeter errors of random cyclic polygons

## Finding
Let \(X_1,\ldots,X_n\), \(n\ge3\), be independent uniform points on the Euclidean unit circle, and let \(K_n=\operatorname{conv}\{X_1,\ldots,X_n\}\). Define the Hausdorff approximation error \(H_n=d_H(K_n,B)\), where \(B\) is the closed unit disk, and the perimeter deficit \(D_n=2\pi-\operatorname{per}(K_n)\). Then the first nonvanishing mixed covariance has the exact sharp asymptotic
\[
\boxed{\lim_{n\to\infty}\frac{n^5}{(\log n)^4}\operatorname{Cov}(H_n,D_n)=\frac{\pi^5}{3}.}
\]
Yet, with \(G\) standard Gumbel and \(Z\sim N(0,40\pi^6)\) independent,
\[
\left(\frac{n}{\pi}\arccos(1-H_n)-\log n,\quad
n^{5/2}\left(D_n-\frac{2\pi^3}{n^2}\right)\right)
\ \Longrightarrow\ (G,Z),
\qquad \Pr(G\le t)=\exp(-e^{-t}).
\]
Consequently \(\sqrt{4\pi H_n/D_n}-\log n\Longrightarrow G\). The positive covariance describes a coupling that disappears at the separate natural fluctuation scales. The covariance coefficient is not a simulation-derived estimate.

## Assumptions and scope
The circle has radius exactly one. The points are independent with normalized arc-length law and \(n\) tends through the integers; the convex hull is formed in the standard Euclidean plane, and perimeter means the full boundary length. Almost surely the points are distinct and \(D_n>0\). All logarithms are natural. Covariance is with respect to the full joint sampling law, without conditional truncation. The result concerns this homogeneous circular boundary model, not arbitrary smooth convex bodies, general boundary densities, or samples from the disk interior.

Write the ordered circular gaps as fractions \(\Delta_1,\ldots,\Delta_n>0\) with sum one, and set \(\Delta_* =\max_i\Delta_i\). A standard exponential-spacing representation is
\[
(\Delta_1,\ldots,\Delta_n)\stackrel d=
(E_1/S,\ldots,E_n/S),\quad
S=\sum_i E_i,\quad E_i\stackrel{\mathrm{iid}}\sim\operatorname{Exp}(1).
\]
Let \(M=\max_i E_i\), \(B_3=\sum_iE_i^3\), \(U=S/n\), and \(F_3=(B_3/n)U^{-3}\). Different occurrences of these symbols below refer to the same sample.

## Proof
**1. Geometry and Taylor remainders.** In any unit direction the support of the polygon is the cosine of its least angular distance from a sample vertex. The maximum of this nearest-vertex distance is half of its longest circular gap, giving the *exact* identities
\[
H_n=1-\cos(\pi\Delta_*),\qquad
D_n=2\sum_{i=1}^{n}\bigl(\pi\Delta_i-\sin(\pi\Delta_i)\bigr).
\]
These identities remain valid even when a sample has a gap exceeding a semicircle. The alternating Taylor inequalities, applied for \(0\le \Delta_i\le1\), yield
\[
H_n=\frac{\pi^2 M^2}{2S^2}+R_H,
\quad |R_H|\le\frac{\pi^4M^4}{24S^4},
\]
\[
D_n=\frac{\pi^3 B_3}{3S^3}+R_D,
\quad |R_D|\le\frac{\pi^5}{60}\sum_i\Delta_i^5.
\]
For each fixed positive integer \(r\), \(\mathbb E\sum_i\Delta_i^r=n\,r!/[n(n+1)\cdots(n+r-1)]\). The corresponding joint Dirichlet moments give \(\|R_D\|_2=O(n^{-4})\). Exponential-maximal moments and inverse gamma moments imply \(\|R_H\|_2=O((\log n)^4n^{-4})\), \(\|H_n-\mathbb EH_n\|_2=O((\log n)n^{-2})\), and \(\|D_n-\mathbb ED_n\|_2=O(n^{-5/2})\). Thus Cauchy–Schwarz shows that replacing both errors by their leading Taylor terms changes their covariance by \(o((\log n)^4n^{-5})\). In particular,
\[
\operatorname{Cov}(H_n,D_n)
=\frac{\pi^5}{6n^4}\operatorname{Cov}(M^2U^{-2},F_3)
+o((\log n)^4n^{-5}). \tag{1}
\]

**2. First-order normal law.** Put
\[
\psi(x)=x^3-18x+12,\qquad Q_n=\sum_{i=1}^n\psi(E_i).
\]
Direct factorial moments of an exponential variable give \(\mathbb E\psi(E_1)=0\), \(\mathbb E\psi(E_1)^2=360\). Taylor-expanding the smooth function \((a,b)\mapsto a/b^3\) around \((6,1)\),
\[
F_3=6+Q_n/n+T_n,\quad\|T_n\|_2=O(n^{-1}). \tag{2}
\]
The usual bivariate sample-mean central limit theorem therefore gives \(\sqrt n(F_3-6)\Longrightarrow N(0,360)\). Since \(D_n=(\pi^3/3n^2)F_3+R_D\), the claimed perimeter normal law follows, including the exact variance \(40\pi^6\). The elementary mean \(\mathbb E F_3=6n^2/((n+1)(n+2))\) verifies that the deterministic centering \(2\pi^3/n^2\) is sufficient.

**3. Gumbel law and asymptotic independence.** For \(t>0\), \(\Pr(M\le t)=(1-e^{-t})^n\). Hence \(M-\log n\Longrightarrow G\). Since \(S/n=1+O_p(n^{-1/2})\) and \(M=O_p(\log n)\), the difference between \(n\Delta_*-\log n\) and \(M-\log n\) converges to zero. The exact support identity gives
\[
\frac{n}{\pi}\arccos(1-H_n)-\log n=n\Delta_*-\log n.
\]
To prove independence rather than merely separate convergence, fix \(z\in\mathbb R\) and condition on \(M\le \log n+z\). The variables \(E_i\) are then independent exponentials individually truncated at that threshold. For the powers \(1\) and \(3\), each truncated mean differs from its untruncated counterpart by \(O((\log n)^3/n)\), and the truncated covariance matrix converges to the ordinary exponential covariance matrix. The triangular-array bivariate CLT therefore has the same Gaussian limit under this conditioning, with no shift on the \(\sqrt n\) scale. Since \(\Pr(M\le\log n+z)\to e^{-e^{-z}}\), joint threshold probabilities factor for every \(z\). This proves independence of \(G\) and the Gaussian limit; the preceding negligible replacements give the stated pair.

**4. The leading covariance.** By \(\|M^2(U^{-2}-1)\|_2=O((\log n)^2n^{-1/2})\), \(\|F_3-\mathbb EF_3\|_2=O(n^{-1/2})\), and (2),
\[
\operatorname{Cov}(M^2U^{-2},F_3)
=\frac1n\operatorname{Cov}(M^2,Q_n)
+O((\log n)^2/n). \tag{3}
\]
The leading mixed moment can be computed from the *exact* conditional expectation of a sum of exponentials given their maximum. With \(m>0\),
\[
\mathbb E[Q_n\mid M=m]
=m^3-18m+12
-\frac{(n-1)e^{-m}}{1-e^{-m}}(m^3+3m^2-12m). \tag{4}
\]
Indeed the unique maximum contributes \(\psi(m)\), while the remaining variables have exponential law conditioned to be at most \(m\), and integration of \(\psi(x)e^{-x}\) above \(m\) produces \(e^{-m}(m^3+3m^2-12m)\). Set \(L=\log n\), \(G_n=M-L\). Formula (4), with \(n e^{-M}=e^{-G_n}\), implies in every fixed weighted moment needed for covariance
\[
\mathbb E[Q_n\mid M]=L^3(1-e^{-G_n})+O_{L^2}(L^2),
\]
where the remainder has \(L^2\)-norm \(O(L^2)\). The distributions of \(G_n\) have uniformly bounded polynomial moments, including moments weighted by \(e^{-G_n}\), and converge to standard Gumbel. Since \(M^2=L^2+2LG_n+G_n^2\),
\[
\frac{\operatorname{Cov}(M^2,Q_n)}{L^4}
\longrightarrow 2\operatorname{Cov}(G,1-e^{-G})=2. \tag{5}
\]
For the last equality, \(W=e^{-G}\) has unit exponential law, and \(\operatorname{Cov}(-\log W,W)=-1\), by the gamma integral \(\mathbb E(W\log W)=1-\gamma\). Combining (1), (3), and (5) yields the asserted positive sharp constant \(\pi^5/3\).

**5. Observable ratio.** Step 2 gives \(n^2D_n\to 2\pi^3\) in probability, and Step 3 gives \(n\Delta_* -\log n\Longrightarrow G\). Since \(H_n=(\pi^2/2)\Delta_*^2(1+O(\Delta_*^2))\), the difference between \(\sqrt{4\pi H_n/D_n}\) and \(n\Delta_*\) is \(o_p(1)\), proving the stated ratio limit.

## Verification
The standalone `verify.py` checks the exact exponential influence mean and variance by factorial arithmetic and evaluates the one-dimensional conditional covariance integral in (4) deterministically for three finite sample sizes. The observed normalized finite-size ratios decrease toward the proposed limit, but this *does not* prove convergence: the limiting arguments and quantitative remainder bounds above are the evidence for the theorem. The script uses only the Python standard library and can be executed with `python verify.py`.

## Relationship to prior work
Besau, Rosen and Thäle (arXiv:2005.10502, first posted 2020-05-21, primary MSC 52A22) prove general normal approximation results for volumes of random boundary-inscribed polytopes. Bélisle (2011) studies perimeter and area fluctuations for precisely the circular sampling model. Wang, Xu and Liu (2021) prove accelerated area/semiperimeter extrapolation CLTs by cancellation of leading circular-spacing moments; those results already cover an area–perimeter cancellation construction and are *not* claimed here. Schneider (1988) investigates almost-sure Hausdorff, area and perimeter approximation rates. The present result instead computes an explicit positive next-order *mixed covariance* of Hausdorff and perimeter errors, as well as an extreme-value/Gaussian joint law. These follow from the exact conditional maximum calculation (4), not from marginal CLTs or rate bounds alone.

## Limitations
The assertion is asymptotic as \(n\to\infty\), not a finite-sample closed formula or an assertion of positive covariance at every sample size. The proof is specific to independent uniform points on the unit circle. A complete scholarly priority judgment would require access to the full text of older potentially adjacent work on random convex-set approximation and spacing statistics. The mathematical derivation has not undergone an independent audit. Deterministic finite numerical checks are supplementary, not certificates of infinite asymptotics.

## References
1. F. Besau, D. Rosen, C. Thäle, *Random inscribed polytopes in projective geometries*, arXiv:2005.10502 (first public version 2020-05-21); *Mathematische Annalen* 381 (2021), 1345–1372, DOI: 10.1007/s00208-021-02257-9.
2. C. Bélisle, *On the polygon generated by n random points on a circle*, *Statistics & Probability Letters* 81 (2011), 236–242, DOI: 10.1016/j.spl.2010.11.012.
3. S. Wang, W.-Q. Xu, J. Liu, *Random Polygons and Optimal Extrapolation Estimates of Pi*, *Statistics, Optimization & Information Computing* 9 (2021), 241–249, DOI: 10.19139/soic-2310-5070-1193.
4. R. Schneider, *Random approximation of convex sets*, *Journal of Microscopy* 151 (1988), 211–227, DOI: 10.1111/j.1365-2818.1988.tb04682.x.
5. R. Pyke, *Spacings*, *Journal of the Royal Statistical Society, Series B* 27 (1965), 395–449.
