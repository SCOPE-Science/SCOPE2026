# Carrier–bandwidth law for sharp weighted Bergman hypercontractive cutoffs

## Finding

For analytic polynomials concentrated at a large carrier degree, the sharp weighted Bergman \(2\to4\) dilation cutoff is controlled jointly by the carrier, the bandwidth, and a circle Fourier fourth-moment invariant. The result is uniform over changing frequency patterns, not just fixed finite lists.

Write \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) and \(\mathbb T=\{|z|=1\}\), with normalized circle measure \(d\theta/(2\pi)\). For \(\alpha>1\), define the probability measure
\[
d\mu_\alpha(z)=\frac{\alpha-1}{\pi}(1-|z|^2)^{\alpha-2}\,dA(z),\qquad
\|f\|_{A_\alpha^p}^p=\int_{\mathbb D}|f|^p\,d\mu_\alpha.
\]
For nonempty \(S\subseteq\{0,\ldots,L-1\}\), put
\[
V_{m,S}=\left\{z^m\sum_{j\in S}a_jz^j:\ a_j\in\mathbb C\right\},\qquad
H(S)=\sup_{0\ne P\in\operatorname{span}\{z^j:j\in S\}}
\frac{\int_{\mathbb T}|P|^4}{\left(\int_{\mathbb T}|P|^2\right)^2}.
\]
Let \(R_{m,S}\) be the largest \(r\in[0,1]\) such that \(\|f(r\cdot)\|_{A_\alpha^4}\le\|f\|_{A_\alpha^2}\) for every \(f\in V_{m,S}\).

**Uniform sharp carrier–bandwidth law.** Given any sequence of supports \(S_m\) as above with \(L_m\ge1\) and \(L_m\log m/m\to0\), each cutoff is strictly between zero and one for all sufficiently large \(m\), is unique, and
\[
\boxed{4m\log\frac1{R_{m,S_m}}=(\alpha-1)\log m+\log H(S_m)
+\log\frac{2^{1-\alpha}}{\Gamma(\alpha)}
+O_\alpha\!\left(\frac{L_m\log m+1}{m}\right).}
\]
Here the implicit constant depends only on \(\alpha\), and the estimate is uniform over support patterns of the specified width for sufficiently large \(m\).

**A sharp bandwidth exponent.** For consecutive supports \(S_m=\{0,1,\ldots,L_m-1\}\), if \(L_m=m^{\delta+o(1)}\) with \(0\le\delta<1\), then
\[
\boxed{\lim_{m\to\infty}\frac{4m\log(1/R_{m,S_m})}{\log m}=\alpha-1+\delta.}
\]
Thus the carrier penalty and the Fourier bandwidth penalty add in the leading logarithmic scale.

**An exact arithmetic-resonance comparison.** For the fixed three-frequency sets \(S_{\rm AP}=\{0,1,2\}\) and \(S_{\rm Sidon}=\{0,1,3\}\), the classical circle synthesis constants are \(H(S_{\rm AP})=15/7\) and \(H(S_{\rm Sidon})=5/3\). Their distinct sharp Bergman cutoffs obey
\[
\boxed{\lim_{m\to\infty}4m\log\frac{R_{m,S_{\rm Sidon}}}{R_{m,S_{\rm AP}}}=\log\frac97.}
\]
The circle constants themselves are not claimed new; the sharp Bergman cutoff law and this limit are the finding.

## Assumptions and scope

The area and circle measures are probability normalized. \(\alpha>1\) is fixed, the operator is analytic dilation \(f(z)\mapsto f(rz)\), the exponents are precisely \(2\) and \(4\), and the lowest occupied Taylor degree is at least \(m\). No distinctness or nonresonance assumption is imposed on \(S_m\); the only width requirement is \(L_m\log m/m\to0\). If the maximum of \(S_m\) is less than \(L_m-1\), the same bounds remain valid. All coefficients are arbitrary complex numbers. For the limiting bandwidth exponent, \(L_m\ge1\) and \(\delta<1\). For the arithmetic comparison the two supports are fixed as \(m\to\infty\).

## Proof

**Step 1 — moments.** For each integer \(k\ge0\) radial integration gives the exact positive moment
\[
M_k=\int_{\mathbb D}|z|^{2k}d\mu_\alpha(z)=
\frac{\Gamma(\alpha)\Gamma(k+1)}{\Gamma(k+\alpha)}.
\]
For fixed \(\alpha>1\), this decreases with \(k\), and uniformly for \(0\le h\le2L\) with \(L=o(m)\),
\[
\log M_{m+h}=\log\Gamma(\alpha)+(1-\alpha)\log m+O_\alpha\!\left(\frac{L+1}m\right),
\]
\[
\log M_{2m+h}=\log\Gamma(\alpha)+(1-\alpha)\log(2m)+O_\alpha\!\left(\frac{L+1}m\right).
\]
These follow directly from the gamma-ratio asymptotic (or its logarithmic derivative) and are uniform on the stated window.

**Step 2 — two-sided radial comparison.** Let \(P(z)=\sum_{j=0}^d a_jz^j\) with \(d\le L-1\). Its fourth integral means satisfy, for \(0<u\le1\),
\[
u^{4d}\int_{\mathbb T}|P|^4\le\int_{\mathbb T}|P(uz)|^4\le\int_{\mathbb T}|P|^4.
\]
The upper bound is subharmonic monotonicity. For the lower bound, reverse the polynomial by \(Q(z)=z^d\overline{P(1/\overline z)}\). On the circle \(|Q|=|P|\), while \(\|P(u\cdot)\|_4=u^d\|Q(u^{-1}\cdot)\|_4\ge u^d\|Q\|_4\). Thus neither bound assumes nonnegative or aligned coefficients.

**Step 3 — sharp operator sandwich.** For \(f(z)=z^mP(z)\), Parseval and monotonicity of \(M_k\) give
\[
M_{m+L-1}\|P\|_2^2\le\|f\|_{A_\alpha^2}^2\le M_m\|P\|_2^2.
\]
Integrating the radial comparisons for \(P(rtz)\) against the radial Bergman measure gives
\[
r^{4(m+L-1)}M_{2m+2(L-1)}\|P\|_4^4
\le\|f(r\cdot)\|_{A_\alpha^4}^4
\le r^{4m}M_{2m}\|P\|_4^4.
\]
Define \(K_{m,S}(r)=\sup_{0\ne f\in V_{m,S}}\|f(r\cdot)\|_{A_\alpha^4}^4/\|f\|_{A_\alpha^2}^4\). Compactness of the finite-dimensional coefficient sphere attains the supremum, and the preceding inequalities yield the *uniform* sharp-coefficient sandwich
\[
H(S)r^{4(m+L-1)}\frac{M_{2m+2(L-1)}}{M_m^2}
\le K_{m,S}(r)\le
H(S)r^{4m}\frac{M_{2m}}{M_{m+L-1}^2}.
\tag{1}
\]
At each nonzero \(r\), \(K_{m,S}(r)\) is strictly increasing: if \(r_2>r_1\), radial monotonicity of the integral mean gives an improvement by at least \((r_2/r_1)^{4m}\). It is also continuous as a maximum over a fixed compact sphere. Since \(K(0)=0\), \(H(S)\ge1\), and \(M_{2m+2L-2}/M_m^2\asymp_\alpha m^{\alpha-1}\), one has \(K(1)>1\) for sufficiently large \(m\). Hence the unique \(R_{m,S}\in(0,1)\) satisfies \(K(R)=1\).

**Step 4 — take the cutoff.** Substitute \(r=R_{m,S}\) into (1), take logarithms, and use the gamma-ratio estimates. Both enclosing bounds reduce to
\[
4m\log\frac1{R_{m,S}}=(\alpha-1)\log m+\log H(S)
+\log\frac{2^{1-\alpha}}{\Gamma(\alpha)}
+O_\alpha\left(\frac{L+1}m+\frac{L\log m}{m}\right).
\]
Indeed, \(1\le H(S)\le L\) by Cauchy–Schwarz and \(\|P\|_\infty\le\sqrt L\|P\|_2\), so the radius bounds first imply \(|\log R|=O_\alpha(\log m/m)\); multiplying by the shift \(L-1\) contributes \(O(L\log m/m)\). The claimed uniform formula follows.

**Step 5 — bandwidth and resonance.** For consecutive frequencies, the Dirichlet polynomial \(D_L(z)=\sum_{j=0}^{L-1}z^j\) has
\[
\|D_L\|_2^2=L,\qquad\|D_L\|_4^4=\frac{2L^3+L}3.
\]
Consequently \((2L^2+1)/(3L)\le H(\{0,\ldots,L-1\})\le L\), whence \(\log H=\log L+O(1)\) uniformly for \(L\ge1\). This proves the bandwidth exponent.

For \(\{0,1,3\}\), all unordered pair sums are distinct; the fourth moment is \(2(\sum|a_j|^2)^2-\sum|a_j|^4\), with sharp normalized value \(5/3\). For \(\{0,1,2\}\), triangle inequalities permit phase alignment, and symmetry of the endpoint magnitudes is optimal because fixing their squared sum maximizes both their product and the balanced additive-collision term. With normalized center squared magnitude \(t\in[0,1]\), the maximal fourth moment becomes \(1+4t(1-t)+(1-t)^2/2\), uniquely maximized at \(t=3/7\), giving \(15/7\). These Fourier constants are established facts; inserting them into the proved cutoff formula gives \(\log((15/7)/(5/3))=\log(9/7)\), with the displayed ordering of radii.

## Verification

A standalone deterministic Python checker, `check.py`, evaluates exact gamma moments, the full coefficient-convolution fourth-moment formula, the spectral sandwich (1), and numerical cutoff comparisons for the two three-frequency models. It does not prove uniformity in \(m\); that is proved above. All critical infinite-parameter steps are mathematical inequalities and gamma asymptotics, not extrapolations from computations. Run `python3 check.py` with NumPy and SciPy.

## Relationship to prior work

Melentijević (first public 2022-11-07) proves the sharp global weighted Bergman hypercontractive radius \(\sqrt{2/4}\), governed by low-degree perturbations of the constant. Bayart and collaborators (2017) give related global contractive inequalities. Neither of those global theorems computes the *sharp radius on carrier-shifted finite-band spectral subspaces*: the present cutoff tends to one and quantitatively depends on bandwidth and additive resonance. Wang and Zhang (2025) derive global two-weight hypercontractivity and a degree-only Nikol'skiĭ bound. Their latter estimate is exponential in degree and does not yield the current asymptotically sharp radius for a translated narrow spectrum. Existing sharp circle fourth-moment constants, including \(15/7\) and \(5/3\), are supporting input and are not novel claims. No assertion is made that all possible priority literature has been exhausted.

## Limitations

The exponent pair is only \(2\to4\), \(\alpha>1\) is fixed, and the spectral width is sublinear by a logarithmic factor. The theorem does not determine finite-\(m\) radii in closed form, nor does it assert extension to wider supports, arbitrary \(p,q\), or general nonradial weights. Historical novelty is a best-knowledge assessment requiring independent expert verification.

## References

1. P. Melentijević, *Hypercontractive inequalities for weighted Bergman spaces*, arXiv:2211.03655 (first public 2022-11-07), primary MSC 30H20.
2. F. Bayart, O. F. Brevig, A. Haimi, J. Ortega-Cerdà, and K.-M. Perfekt, *Contractive inequalities for Bergman spaces and multiplicative Hankel forms*, arXiv:1701.06897 (first public 2017-01-24).
3. Z. Wang and K. Zhang, *Hypercontractive inequalities and Nikol'skiĭ-type inequalities on weighted Bergman spaces*, arXiv:2505.12760 (2025 supporting comparison only).
4. Classical circle Fourier fourth-moment estimates: the pair-sum convolution identity and its three-frequency additive-collision specialization.
