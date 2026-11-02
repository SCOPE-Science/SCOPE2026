# Sharp IID-shaping gap and unattainable support projection for two-map Cantor systems

## Finding
For a contracting two-map iterated function system whose images are separated by a gap, the unique independent-sampling choice best approximating uniform Lebesgue probability in \(W_1\) is the fair coin. Its exact error exceeds the best error among *all* probabilities supported by the same Cantor attractor by a factor which is arbitrarily large as the gap closes.

Fix \(0<r<1/2\), put \(g=1-2r\), and write \(\lambda\) for normalized Lebesgue measure on \([0,1]\). For the maps \(f_0(x)=rx\), \(f_1(x)=1-r+rx\), let \(\mu_p\) be the invariant law with independent \(f_1\)-choice probability \(p\in[0,1]\). Then
\[
W_1(\mu_p,\lambda)\ge \frac{1-2r}{4}+2r\left(p-\frac12\right)^2,
\qquad
\min_{0\le p\le1} W_1(\mu_p,\lambda)=\frac{1-2r}{4},
\]
with unique minimizing parameter \(p=1/2\). If \(C_r\) denotes the Cantor attractor, then
\[
\min_{\nu(C_r)=1} W_1(\nu,\lambda)=\frac{(1-2r)^2}{4(1-2r^2)}.
\]
The second minimizer is unique, is purely atomic, and cannot be stationary under even *state-dependent* choices of these same two maps. The ratio of the two displayed minima is exactly
\[
\frac{1-2r^2}{1-2r}\longrightarrow+\infty
\quad\text{as }r\uparrow1/2.
\]
For the classical middle-third Cantor system, the two minima are respectively \(1/12\) and \(1/28\), giving ratio \(7/3\).

## Assumptions and scope
The state space is \([0,1]\) with Euclidean distance, and \(W_1\) is the \(1\)-Wasserstein distance, equivalently the Kantorovich--Rubinstein transportation cost. The parameter \(r\) is any real number strictly between \(0\) and \(1/2\). The maps are strict contractions and their images are disjoint. The invariant probability \(\mu_p\) is unique, including at the endpoint probabilities, and is the law of
\[
X_p=(1-r)\sum_{j\ge1} B_jr^{j-1},
\quad\Pr(B_j=1)=p,
\]
where the digits are independent. The compact attractor \(C_r\) is the set of all such binary series with arbitrary digit sequences. An arbitrary supported probability need not arise from IID or state-dependent map selection.

## Proof
**Dual lower bound.** Since \(r<1/2\), the two first-digit intervals are entirely on opposite sides of \(1/2\). The stationary mean is \(\mathbb E X_p=p\). Conditional on the first digit, \(X_p=rX'_p\) for \(B_1=0\) and \(X_p=1-r+rX'_p\) for \(B_1=1\), where \(X'_p\) has the same law independently. For the \(1\)-Lipschitz function \(\phi(x)=|x-1/2|\),
\[
\mathbb E\phi(X_p)=\frac12-2rp(1-p),
\qquad \int\phi\,d\lambda=\frac14.
\]
Kantorovich--Rubinstein duality gives
\[
W_1(\mu_p,\lambda)\ge \frac14-2rp(1-p)
=\frac{1-2r}{4}+2r(p-1/2)^2.
\]
The strict quadratic surplus excludes all \(p\ne1/2\) from attaining the fair-coin value, once equality at the fair coin has been shown.

**Sharpness by monotone transport.** Let \(Q_r(u)\) be the fair-Cantor quantile, defined almost everywhere by replacing the binary digits of \(u\) with base-\(r\) Cantor digits:
\[
Q_r(u)=(1-r)\sum_{j\ge1}b_j(u)r^{j-1},
\qquad u=\sum_{j\ge1}b_j(u)2^{-j}.
\]
This nondecreasing function pushes uniform \(u\) to \(\mu_{1/2}\). Let \(\mathcal H\) act on bounded functions, away from irrelevant binary-dyadic endpoints, by
\[
(\mathcal Hh)(u)=
\begin{cases}
r h(2u),&0\le u<1/2,\\
1-r+r h(2u-1),&1/2<u\le1.
\end{cases}
\]
Its sup-norm contraction factor is \(r\), it preserves pointwise order, and its bounded fixed point is \(Q_r\) up to a null set. Set \(L=2(1-r)\) and \(h(u)=Lu\). Direct inspection on each half-interval gives \(\mathcal Hh\le h\): on the lower half this is \(2r\le1\), and on the upper half it reduces to \(2u\ge1\). Iterating and using uniform convergence gives \(Q_r(u)\le Lu\) almost everywhere. For \(u<1/2\),
\[
Q_r(u)=rQ_r(2u)\le4r(1-r)u\le u.
\]
Reflection symmetry gives \(Q_r(1-u)=1-Q_r(u)\) almost everywhere, hence \(Q_r(u)\ge u\) for \(u>1/2\). Thus the monotone coupling \((u,Q_r(u))\) moves each point outward from \(1/2\) and satisfies
\[
|Q_r(u)-u|=\phi(Q_r(u))-\phi(u)
\]
almost everywhere. It realizes the dual bound, and so
\[
W_1(\mu_{1/2},\lambda)=\frac{1-2r}{4}.
\]
This proves the sharp IID optimization and uniqueness.

**Unrestricted support benchmark.** For any supported probability \(\nu(C_r)=1\), every coupling with \(\lambda\) obeys \(|x-y|\ge \operatorname{dist}(x,C_r)\). The nearest-point projection \(P_{C_r}(x)\) is unique except at the midpoints of the countably many deleted open intervals; these midpoints have zero Lebesgue mass. Hence \((P_{C_r})_\#\lambda\) is the *unique* probability attaining
\[
\inf_{\nu(C_r)=1}W_1(\nu,\lambda)
=\int_0^1\operatorname{dist}(x,C_r)\,dx.
\]
At generation \(k\ge0\) there are \(2^k\) deleted gaps, each of length \(gr^k\). Integrating the triangular nearest-point distance over a gap of length \(\ell\) gives \(\ell^2/4\). Therefore
\[
\int_0^1 \operatorname{dist}(x,C_r)\,dx
=\frac{g^2}{4}\sum_{k\ge0}(2r^2)^k
=\frac{g^2}{4(1-2r^2)}.
\]
The attractor has zero Lebesgue measure since its level-\(k\) covering length is \((2r)^k\to0\). Each half-gap is projected to one endpoint, giving an atom of mass \(gr^k/2\) at each endpoint of every level-\(k\) gap. In particular, the optimum has mass \(g/2>0\) at \(r\) and at \(1-r\), and zero mass at \(0\) and at \(1\).

**Obstruction to state-dependent implementation.** Suppose a Borel probability \(\nu_*=(P_{C_r})_\#\lambda\) were stationary for some Markov kernel \(K(x,\cdot)=a(x)\delta_{f_0(x)}+(1-a(x))\delta_{f_1(x)}\) with measurable \(a:[0,1]\to[0,1]\). The point \(r\) can be reached by \(f_0\) only from \(1\), and cannot be reached by \(f_1\) from \([0,1]\). Consequently \((\nu_*K)(\{r\})\le\nu_*(\{1\})=0\), contrary to \(\nu_*(\{r\})=g/2\). No such kernel can have \(\nu_*\) as invariant law. In particular it is not any \(\mu_p\).

Finally, division of the two positive minima yields \((1-2r^2)/(1-2r)\). Because the numerator tends to \(1/2\) while the denominator tends to zero, the relative loss is unbounded. Both actual Wasserstein errors tend to zero as \(r\uparrow1/2\), so the divergence is multiplicative rather than an absolute-cost explosion.

## Verification
The standalone `verify.py` uses only the Python standard library. It checks the exact rational identities, endpoint atom normalization, and computed ratios for representative rational contractions, then approximates the fair-Cantor monotone coupling on deterministic binary grids. Quantile truncation and Riemann error are bounded explicitly in the checker; finite meshes are not claimed as a proof of the all-parameter theorem. Execute `python3 verify.py` from a directory containing that file.

## Relationship to prior work
Shafiei, Shorten, and Marecek (2026) formulate fixed-map inverse invariant-measure shaping in \(W_1\) and establish broad existence, regularity, and algorithmic results. Their exact ternary benchmark uses three consecutive contractions with a bimodal beta target; it is not the separated two-map Cantor system with uniform target solved here. Fraser (2014) gives exact \(W_1\) distances between *two stationary laws with different sampling probabilities* on the same two-map self-similar attractor. That formula does not compare a stationary Cantor law to Lebesgue measure, which has full interval support for \(r<1/2\), and it does not identify the optimal all-supported projection law. Kloeckner (arXiv:1909.01655v2) studies transport contraction, moment bounds and linear response for random IFS, including the same fair Bernoulli-convolution maps as functions of the contraction parameter; his general results do not provide this inverse choice-of-weights uniform-target optimum or the support projection obstruction. Standard one-dimensional monotone rearrangement and Kantorovich--Rubinstein duality are used as known tools, not claimed as new. The explicit shaping optimum, strict quadratic nonoptimality bound, sharp support-constrained gap, and state-dependent implementation obstruction constitute the present specific result.

## Limitations
The theorem is restricted to two symmetric positive-ratio affine contractions and the uniform target on \([0,1]\). The quadratic inequality for biased sampling need not equal the exact \(W_1\) objective away from the fair parameter. The support-constrained optimum is an unrealizable mathematical benchmark for this fixed-map dynamics, not a proposed practical sampling policy. No result is asserted for higher-dimensional or overlapping systems. Priority is judged against inspected sources and searches; specialized unindexed transport work could contain an equivalent formula. The comparisons are not independent scientific certification.

## References
- Allahkaram Shafiei, Robert Shorten, Jakub Marecek, *Shaping of invariant measures of iterated function systems*, arXiv:2610.34172v1 (publicly available October 25, 2026), https://arxiv.org/pdf/2610.34172.
- Jonathan M. Fraser, *First and second moments for self-similar couplings and Wasserstein distances*, arXiv:1401.1443v2, https://arxiv.org/html/1401.1443v2.
- Benoît R. Kloeckner, *Optimal transportation and stationary measures for iterated function systems*, arXiv:1909.01655v2, https://arxiv.org/pdf/1909.01655.
- Kantorovich--Rubinstein duality and the one-dimensional monotone rearrangement theorem are standard tools; the preceding papers also discuss their use in self-similar transport.
