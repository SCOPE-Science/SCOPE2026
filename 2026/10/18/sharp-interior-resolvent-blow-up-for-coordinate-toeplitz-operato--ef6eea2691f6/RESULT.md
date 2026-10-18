# Sharp interior resolvent blow-up for coordinate Toeplitz operators on weighted harmonic Bergman spaces

## Finding

For every real \(\alpha>-1\), let \(T_\alpha\) denote the Toeplitz compression of multiplication by the coordinate \(z\) to the weighted complex harmonic Bergman Hilbert space \(\mathcal H_\alpha\) defined below. The spectrum is the unit circle. However, the resolvent norm has **different and sharp boundary orders on its two sides**:

\[
\lim_{r\uparrow1}(1-r)^{\alpha+2}\left\|(T_\alpha-r e^{i\theta}I)^{-1}\right\|=2^{-(\alpha+2)},\qquad
\left\|(T_\alpha-r e^{i\theta}I)^{-1}\right\|=\frac1{r-1}\quad(r>1).
\]

Both norm expressions are independent of \(\theta\). The first is a genuine asymptotic; the second holds exactly. The mechanism is an **exact rank-one analytic-to-anti-analytic resolvent block**, which dominates the within-side blocks. In particular, the inner radius of the small-\(\varepsilon\) pseudospectrum extends inward by \(\tfrac12\varepsilon^{1/(\alpha+2)}(1+o(1))\), while its exterior extends by exactly \(\varepsilon\).

## Assumptions and scope

Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) and let \(dA\) be planar Lebesgue area divided by \(\pi\). For a fixed real \(\alpha>-1\), put
\[
d\mu_\alpha(z)=(\alpha+1)(1-|z|^2)^\alpha dA(z).
\]
This is a probability measure. The Hilbert space \(\mathcal H_\alpha\) consists of **complex-valued harmonic functions** on \(\mathbb D\) that belong to \(L^2(\mu_\alpha)\), equipped with its inherited complex Hilbert norm. Let \(P_\alpha\) be its orthogonal projection from \(L^2(\mu_\alpha)\), and set \(T_\alpha f=P_\alpha(zf)\). Let \(P_+\) project onto the span of \(1,z,z^2,\ldots\), and \(P_-\) onto the span of \(\bar z,\bar z^2,\ldots\), so \(\mathcal H_\alpha=P_-\mathcal H_\alpha\oplus P_+\mathcal H_\alpha\). Resolvents are taken in the operator norm on \(\mathcal H_\alpha\).

Write \(m_n=\int_{\mathbb D}|z|^{2n}d\mu_\alpha\) for integers \(n\ge0\). The Euler gamma function gives
\[
m_n=\frac{\Gamma(n+1)\Gamma(\alpha+2)}{\Gamma(n+\alpha+2)},\qquad m_0=1.
\]
Use the orthonormal basis \(e_n=z^n/\sqrt{m_n}\) for \(n\ge0\) and \(e_{-j}=\bar z^j/\sqrt{m_j}\) for \(j\ge1\).

## Proof

**1. Two-ended weighted shift and spectrum.** Orthogonality of circular Fourier modes gives
\[
T_\alpha e_n=w_ne_{n+1},\quad
w_n=\begin{cases}
\sqrt{(n+1)/(n+\alpha+2)},&n\ge0,\\
\sqrt{j/(j+\alpha+1)},&n=-j\le-1.
\end{cases}
\]
Every weight is positive, bounded below and at most \(1\), and tends to \(1\) at both ends. Thus \(T_\alpha\) is invertible and \(\|T_\alpha\|=1\). Define positive scalars \(b_n=\sqrt{m_n}\) for \(n\ge0\) and \(b_{-j}=1/\sqrt{m_j}\) for \(j\ge1\); then \(w_n=b_{n+1}/b_n\), hence \(T_\alpha^{-k}e_n=(b_{n-k}/b_n)e_{n-k}\).

Let \(s=(\alpha+1)/2>0\). Since
\[
\frac{m_{n-1}}{m_n}=1+\frac{\alpha+1}{n}\quad(n\ge1),
\]
a product comparison gives \(1/m_n\le C_\alpha(n+1)^{2s}\). If the inverse shift of length \(k\) does not cross index zero, the coefficient is at most \(C_\alpha(k+1)^s\). If it crosses zero, write the initial index \(m\ge0\) and final index \(-j\) with \(m+j=k\); its coefficient is \(1/\sqrt{m_mm_j}\le C_\alpha(k+1)^{2s}\). Consequently \(\|T_\alpha^{-k}\|\le C_\alpha(k+1)^{\alpha+1}\), while \(\|T_\alpha^k\|=1\). The spectral radii of both \(T_\alpha\) and its inverse equal one, so \(\sigma(T_\alpha)\) lies on the unit circle. Conversely, since the weights approach one, arbitrarily long blocks far along the positive indices yield approximate eigenvectors for every unimodular \(\lambda\), by truncating the corresponding constant-weight bilateral shift eigenvectors. Thus \(\sigma(T_\alpha)=\{\lambda:|\lambda|=1\}\).

**2. The exact rank-one cross block.** For \(0<r<1\), subexponential inverse powers justify the operator-norm Laurent expansion
\[
R_\alpha(r):=(T_\alpha-rI)^{-1}=\sum_{k=1}^\infty r^{k-1}T_\alpha^{-k}.
\]
Its matrix coefficient from \(e_m\), \(m\ge0\), to \(e_{-j}\), \(j\ge1\), is
\[
\langle R_\alpha(r)e_m,e_{-j}\rangle
=\frac{r^{m+j-1}}{\sqrt{m_mm_j}}.
\]
It factors into the outer product of \((r^{j-1}/\sqrt{m_j})_{j\ge1}\) and \((r^m/\sqrt{m_m})_{m\ge0}\); hence \(B_{\alpha,r}:=P_-R_\alpha(r)P_+\) has rank one. The binomial series yields
\[
S_\alpha(r):=\sum_{n=0}^\infty\frac{r^{2n}}{m_n}=(1-r^2)^{-(\alpha+2)}.
\]
The two vector-norm squares are \(r^{-2}(S_\alpha(r)-1)\) and \(S_\alpha(r)\). Therefore, exactly,
\[
\boxed{\|B_{\alpha,r}\|=\frac{1}{r}(1-r^2)^{-(\alpha+2)}
\sqrt{1-(1-r^2)^{\alpha+2}}.}
\]

**3. All other blocks have strictly smaller order.** As \(T_\alpha^{-k}\) moves indices only downward, the remaining two diagonal blocks of \(R_\alpha(r)-B_{\alpha,r}\) stay on their respective half-lines. On either half-line, every length-\(k\) inverse-shift coefficient is bounded by \(C_\alpha(k+1)^s\). Indeed, each factor \(m_{n-1}/m_n=1+(\alpha+1)/n\) decreases with \(n\), and the maximal length-\(k\) product starts at the smallest permitted index. Summing their Laurent series gives
\[
\|R_\alpha(r)-B_{\alpha,r}\|
\le C_\alpha\sum_{k=1}^\infty r^{k-1}(k+1)^s
=O_\alpha((1-r)^{-(s+1)})
=O_\alpha((1-r)^{-(\alpha+3)/2}).
\]
Because \((\alpha+3)/2<\alpha+2\), the remainder is negligible relative to \(B_{\alpha,r}\). Since \(1-r^2\sim2(1-r)\), the rank-one formula proves
\[
\lim_{r\uparrow1}(1-r)^{\alpha+2}\|R_\alpha(r)\|=2^{-(\alpha+2)}.
\]

**4. Exterior resolvent and rotations.** For \(r>1\), \(\|T_\alpha\|=1\) implies \(\|(T_\alpha-rI)^{-1}\|\le(r-1)^{-1}\) by the geometric Neumann series. Since \(1\in\sigma(T_\alpha)\), the distance-to-spectrum lower bound gives equality. Rotating the basis by \(U_\theta e_n=e^{in\theta}e_n\) yields \(U_\theta T_\alpha U_\theta^*=e^{i\theta}T_\alpha\), and therefore both resolvent norms are independent of the argument of the spectral parameter.

**5. Pseudospectral interpretation.** With the convention \(\sigma_\varepsilon(T)=\sigma(T)\cup\{\lambda\notin\sigma(T):\|(T-\lambda I)^{-1}\|>\varepsilon^{-1}\}\), the boundary radius on the inner side satisfies \(1-r_\varepsilon=\tfrac12\varepsilon^{1/(\alpha+2)}(1+o(1))\), obtained by inverting the strictly increasing positive-matrix norm near \(r=1\). The outer boundary is at \(r=1+\varepsilon\) exactly. No global finite-\(\varepsilon\) formula is asserted.

## Verification

All identities are analytic, with no infinite-dimensional conclusion deduced from a finite truncation. The standalone `check.py` builds finite sections of the explicit resolvent matrix for several \(\alpha\) and \(r\), verifies that the cross block is rank one to floating-point precision, checks its predicted finite-section norm and the exact infinite-series normalization, and confirms that the finite-section full norm exceeds the cross norm. Run `python check.py` with NumPy and SciPy. Finite-section convergence slows as \(r\) approaches one, so the program is a consistency test, **not** a rigorous bound on the omitted tails. The estimate in Step 3 is the rigorous tail control.

## Relationship to prior work

Huang, Wang and Zhao (arXiv:2610.09638v1, first available 2026-10-07) study the *ordinary spectrum and Weyl's theorem* for analytic-polynomial Toeplitz symbols on the unweighted harmonic Bergman space. Their publicly accessible abstract is the motivating comparison; a full-text comparison could not be completed and is a residual priority risk. Their stated spectral-curve theorem does not by itself determine the resolvent norm or the order and coefficient of interior pseudospectral expansion. Guo and Zheng (2002) characterize compact Toeplitz operators and Toeplitz-algebra exact sequences, and Iqtaish, Louhichi and Yousef (2025) characterize commuting Toeplitz families. Their accessible statements do not imply the quantitative rank-one resolvent block or the weighted-parameter boundary law. The two-ended shift representation and elementary binomial generating function are methods rather than claimed novelty. The asserted contribution is their sharp **quantitative combination** for this natural family, not the qualitative spectral fact alone.

## Limitations

The theorem concerns the single analytic coordinate symbol and radial power weights \(\alpha>-1\). It does not classify general polynomial symbols, nonradial measures, or the singular Hardy endpoint \(\alpha=-1\). No assertion about publication priority is made beyond comparisons actually available; the initiating preprint and the 2002 article were not inspected in full owing to access failures. Independent mathematical assessment remains unperformed.

## References

1. M. Huang, J. Wang, X. Zhao, *The spectral structure of Toeplitz operators with polynomial symbols on the harmonic Bergman space*, arXiv:2610.09638v1 (2026-10-07), https://arxiv.org/abs/2610.09638 .
2. K. Guo and D. Zheng, *Toeplitz algebra and Hankel algebra on the harmonic Bergman space*, J. Math. Anal. Appl. 276 (2002), 213–230, https://doi.org/10.1016/S0022-247X(02)00429-8 .
3. H. Iqtaish, I. Louhichi, A. Yousef, *On the commuting problem of Toeplitz operators on the harmonic Bergman space*, AIMS Mathematics 10 (2025), 17232–17247, https://doi.org/10.3934/math.2025770 .
