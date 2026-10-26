# A logarithmic finite-sample correction for two-orbit pair correlations of expanding circle maps

## Finding
Fix an integer \(b\ge2\) and \(s>0\). Set \(\mathbb T=\mathbb R/\mathbb Z\), \(T_b(x)=bx\pmod1\), and let \(X,Y\) be independent Haar-uniform points of \(\mathbb T\). For each integer \(N>2s\) put \(r=s/N\) and
\[
Q_N=\frac1N\sum_{0\le i,j<N}{\bf1}\!\left\{\|T_b^iX-T_b^jY\|_{\mathbb T}\le r\right\},
\qquad \|u\|_{\mathbb T}=\min_{k\in\mathbb Z}|u-k|.
\]
Then \(\mathbb E Q_N=2s\), and, with \(B_2(t)=t^2-t+1/6\) periodically extended from \([0,1)\),
\[
\operatorname{Var}(Q_N)
=C_0(r)+2\sum_{h=1}^{N-1}\left(1-\frac hN\right)^2C_h(r),
\quad
C_h(r)=\frac{B_2(\{(b^h-1)r\})-B_2(\{(b^h+1)r\})}{b^h}.
\]
For fixed \(b,s\) and \(N\to\infty\), the **two-term finite-size law** is
\[
\boxed{N\operatorname{Var}(Q_N)=\frac{2s(b+1)}{b-1}
-\frac{8s^2\log_bN}{N}+O_{b,s}(N^{-1}).}
\]
In particular, the leading variance is inflated by \((b+1)/(b-1)\) relative to two independently resampled uniform samples; the logarithmic second-order term is absent from the independent-sample benchmark. A structural reason is the exact covariance selection rule: two cross-orbit close-pair events at indices \((i,j)\) and \((i',j')\) are uncorrelated unless \(i'-i=j'-j\).

## Assumptions and scope
The two starting positions are **independent**, but points within each orbit are deterministic iterates of the same position. Both are distributed according to Haar measure. The collision window uses **circular distance**; the index set includes all \(N^2\) ordered cross-orbit pairs, including equal index times (which still use independent positions). No conclusion is asserted for interval absolute distance or for correlated initial positions. The expansion factor is an integer at least two and the window radius parameter is fixed as \(N\) increases.

## Proof
**Step 1: exact covariance selection.** Write \(p=2r\), \(H_r(t)={\bf1}_{\{\|t\|_{\mathbb T}\le r\}}-p\). Its nonzero Fourier coefficients are
\[
\widehat H_r(k)=\frac{\sin(2\pi kr)}{\pi k}\quad(k\ne0).
\]
For integers \(0\le i,j,i',j'<N\), expand the covariance of \(H_r(b^iX-b^jY)\) and \(H_r(b^{i'}X-b^{j'}Y)\) in Fourier series. Independence and uniformity of \(X,Y\) force, for nonzero integer frequencies \(k,\ell\), the simultaneous equations
\[
k b^i+\ell b^{i'}=0,\qquad k b^j+\ell b^{j'}=0.
\]
These equations can hold only if \(i'-i=j'-j\). Otherwise the covariance vanishes **exactly**, not asymptotically. If the common difference has magnitude \(h\ge0\), the surviving Fourier series is
\[
C_h(r)=\int_{\mathbb T}H_r(t)H_r(b^ht)\,dt
=\sum_{k\ne0}\widehat H_r(k)\widehat H_r(b^hk).
\]
The series converges absolutely by Cauchy–Schwarz (or from the \(k^{-2}\) bound). There are exactly \(N^2\) ordered pairs of index-pairs at common shift zero, and \((N-h)^2\) at each signed common shift \(\pm h\). Expanding the variance of \(Q_N\) and grouping by the common shift proves the stated finite-sample identity.

**Step 2: closed covariance kernel.** For every positive integer \(m\), use the Fourier expansion of the periodically extended second Bernoulli polynomial,
\[
B_2(\{t\})=\frac1{\pi^2}\sum_{k=1}^{\infty}\frac{\cos(2\pi kt)}{k^2}.
\]
With the sine-product identity and \(m=b^h\), the series in Step 1 becomes
\[
C_h(r)=\frac{B_2(\{(m-1)r\})-B_2(\{(m+1)r\})}{m}.
\]
The periodic function \(B_2\) is globally one-Lipschitz; hence \(|C_h(r)|\le2r/b^h\). If \((b^h+1)r<1\), neither Bernoulli argument wraps and the formula simplifies **exactly** to
\[
C_h(r)=\frac{2r}{b^h}-4r^2.
\]
The special case \(h=0\) gives \(C_0(r)=2r(1-2r)\).

**Step 3: leading term and logarithmic correction.** Define \(H_N=\lfloor\log_b(N/(2s))\rfloor\), for all sufficiently large \(N\). Then \((b^h+1)s/N<1\) whenever \(0\le h\le H_N\), whereas \(b^{-H_N}=O_{b,s}(N^{-1})\). Use Step 2 for \(h\le H_N\) and its uniform geometric bound for \(h>H_N\). The exact finite-sample formula yields
\[
\begin{aligned}
N\operatorname{Var}(Q_N)
={}&2s-\frac{4s^2}{N}
+4s\sum_{h=1}^{H_N}\left(1-\frac hN\right)^2b^{-h}\\
&-\frac{8s^2}{N}\sum_{h=1}^{H_N}\left(1-\frac hN\right)^2
+O_{b,s}(N^{-1}).
\end{aligned}
\]
The omitted high-shift contribution is \(O_{b,s}(N^{-1})\) because \(2N\sum_{h>H_N}|C_h(r)|\le4s\sum_{h>H_N}b^{-h}=O_{b,s}(N^{-1})\). The geometric sum in the preceding display is \(1/(b-1)+O_{b,s}(N^{-1})\): the tail is geometric and \(\sum_{h\ge1}h b^{-h}<\infty\). Finally,
\[
\sum_{h=1}^{H_N}\left(1-\frac hN\right)^2
=H_N+O(H_N^2/N),\qquad
H_N=\log_bN+O_{b,s}(1).
\]
Substitution proves the claimed leading term and the precise negative coefficient of \(\log_bN/N\). Every remainder in the displayed expansion is \(O_{b,s}(N^{-1})\), since \((\log N)^2/N^2=O(1/N)\).

**Step 4: independent benchmark.** For two independent samples of \(N\) separately resampled uniform circle points, each of their \(N^2\) cross-collision indicators has success probability \(p=2s/N\). Distinct indicators are uncorrelated: those with disjoint endpoints are independent, and for a shared endpoint conditional uniformity makes their covariance zero. Their normalized sum therefore has variance \(p(1-p)\), not the expanded-map variance above.

## Verification
`CHECK.py` reconstructs the covariance kernel independently by exactly intersecting rational arcs \(\{\|t\|\le r\}\) and \(\{\|mt\|\le r\}\), and compares this geometric integral to the Bernoulli-polynomial expression. It also verifies finite-sample variances by exact fractions for small sizes and separately checks the leading and logarithmic asymptotics numerically. The recorded `CHECK_OUTPUT.txt` ends with `EXACT_RATIONAL_CHECKS_PASS 358`. The finite checks are diagnostic; the proof of the infinite limit and its error is Steps 1–4.

## Relationship to prior work
Baker and Todd (2026, arXiv:2606.17880, Theorem A) prove first-order almost-sure pair-correlation behavior for two orbits of suitably mixing interval maps. This result concerns a different, second-moment question and identifies both a sharp fluctuation coefficient and its logarithmic finite-size correction for a canonical expanding circle family. Rudnick and Zaharescu (1999), Rudnick and Technau (2020), and Chaubey and Yesha (2021) obtain Poissonian local-spacing laws for lacunary sequences, rather than the present sharp two-independent-starting-point cross-variance formula. A published companion computation, *Sharp second-moment inflation for expanding circle-map pair correlations* (2026), treats **pairs within one orbit** and finds a different leading coefficient; its one-orbit result does not imply the distinct two-orbit covariance selection rule or the logarithmic correction proved here.

## Limitations
No central limit theorem, limiting fluctuation distribution, or higher-order constant beyond the logarithmic correction is claimed. The \(O_{b,s}(N^{-1})\) term may oscillate with \(\log_bN\); no convergence of that remainder is asserted. Absolute-distance interval statistics, noninteger slopes, and dependent starting positions require separate analysis. Literature priority beyond the inspected sources is not guaranteed.

## References
1. S. Baker and M. Todd, *Pair correlation statistics for dynamical systems*, arXiv:2606.17880 (first submitted 16 June 2026), Theorem A and Sections 2–4. https://arxiv.org/abs/2606.17880
2. Z. Rudnick and A. Zaharescu, *The distribution of spacings between fractional parts of lacunary sequences*, arXiv:math/9912103 (1999). https://arxiv.org/abs/math/9912103
3. Z. Rudnick and N. Technau, *The metric theory of the pair correlation function of real-valued lacunary sequences*, arXiv:2001.08820 (2020), especially Section 2.2. https://arxiv.org/abs/2001.08820
4. S. Chaubey and N. Yesha, *The distribution of spacings of real-valued lacunary sequences modulo one*, arXiv:2108.00431 (2021). https://arxiv.org/abs/2108.00431
5. *Sharp second-moment inflation for expanding circle-map pair correlations* (published result, 2026), comparison of within-orbit variance with the present two-orbit result.
