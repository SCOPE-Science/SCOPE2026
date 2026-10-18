# Parity-sensitive rare-event law for wild edges in balanced two-colour complete graphs

## Finding

For every integer \(n\ge4\), label the edges of \(K_n\) with two named colours, chosen uniformly among all colourings in which the two colour classes differ in size by at most one. Let \(W_n\) be the **wild number**: the minimum number of edges which, when simultaneously made available to both colours, make each colour class span a connected graph. Put \(N=\binom n2\), and let \(\varepsilon_n\in\{0,1\}\) be the remainder of \(N\) on division by two.

As \(n\to\infty\),

\[
\Pr(W_n=1)=\frac{4n}{e\,2^n}\left(1+\frac{1+6\varepsilon_n}{3n^2}+O(n^{-3})\right),
\]

\[
\mathbb E W_n=\frac{4n}{e\,2^n}\left(1+\frac{1+6\varepsilon_n}{3n^2}+O(n^{-3})\right),\qquad
\Pr(W_n\ge2)=O(n^2 4^{-n}).
\]

In particular, the first nonzero relative correction is \(1/(3n^2)\) when \(N\) is even, but \(7/(3n^2)\) when \(N\) is odd. The leading \(4/e\) factor and the parity-sensitive second-order term arise from the exact edge-balance constraint. The result is asymptotic; it does not assert the displayed expansion as an equality at small orders.

## Assumptions and scope

All graphs are finite, undirected and simple. A uniformly chosen equitable two-colouring gives each colouring satisfying \(|E_1-E_2|\le1\) equal probability. When \(N\) is odd, the two possible class sizes occur with equal total probability; choosing one of the two sizes first and then a uniformly random edge subset gives the same law for \(W_n\), since the colours can be interchanged. For a graph \(H\) on the fixed vertex set \([n]\), write \(\kappa(H)\) for its number of components, including isolated vertices. By the established two-colour wild-number identity,

\[
W_n=\kappa(H)+\kappa(\overline H)-2,
\]

where \(H\) is uniformly distributed over graphs with \(m=\lfloor N/2\rfloor\) edges. It suffices to use this fixed choice because \(W_n\) is invariant under exchanging the two colours.

## Proof

**1. Isolation probabilities.** Fix a vertex of a uniformly random \(m\)-edge graph \(H\). Since \(d=n-1\) potential edges touch that vertex, its isolation probability is

\[
p_m=\frac{\binom{N-d}{m}}{\binom Nm}
=\prod_{j=0}^{d-1}\frac{N-m-j}{N-j}.
\]

The corresponding isolation probability in \(\overline H\), which has \(N-m\) edges, is \(p_{N-m}\). The expected total number of isolated vertices in the two colour classes is exactly \(n(p_m+p_{N-m})\).

**2. Other disconnection mechanisms are exponentially smaller.** Write \(\theta_n=1/2+1/(2N)\). For either colour class, which has \(m\) or \(N-m\) edges, the probability that no edge crosses a particular nontrivial cut with \(a\) candidate cross edges is at most \(\theta_n^a\). Indeed, sampling without replacement gives \((N-M)_{\underline a}/(N)_{\underline a}\le((N-M)/N)^a\), with the probability interpreted as zero if too few absent edges are available.

The probability that a colour class contains two isolated vertices is at most \(\binom n2\theta_n^{2n-3}=O(n^2 4^{-n})\). If a disconnected colour class has a component of size at least two and at most \(n/2\), a union bound gives

\[
\sum_{k=2}^{\lfloor n/2\rfloor}\binom nk\theta_n^{k(n-k)}.
\]

The \(k=2\) term is \(O(n^2 4^{-n})\). For \(3\le k\le n/2\), the exponent is at least \(3(n-3)\), giving the bound \(2^n\theta_n^{3(n-3)}=O(4^{-n})\). These bounds hold uniformly for the two near-half edge counts. Thus, outside an event of probability \(O(n^2 4^{-n})\), each colour class is either connected or has exactly one isolated vertex and its other \(n-1\) vertices connected.

The complement of a disconnected graph is connected, since every pair of its components is completely joined in the complement. Consequently, outside the exceptional event, \(W_n\in\{0,1\}\), and \(W_n=1\) precisely when one of the two colour classes has an isolated vertex. Counting isolation with the union bound and controlling double isolation as above yields

\[
\Pr(W_n=1)=n(p_m+p_{N-m})+O(n^2 4^{-n}),
\quad \Pr(W_n\ge2)=O(n^2 4^{-n}).
\]

Since \(0\le W_n\le n-1\), it follows that

\[
\mathbb E W_n=n(p_m+p_{N-m})+O(n^3 4^{-n}).
\]

**3. Fixed-edge asymptotic and parity.** Put \(\delta=N/2-m\), so \(\delta=0\) when \(N\) is even and \(\delta=1/2\) otherwise. Define the positive auxiliary product

\[
p_0=\prod_{j=0}^{n-2}\frac{N/2-j}{N-j}.
\]

(The product is meaningful as a real product even when \(N\) is odd.) With \(r_j=j/N\), expansion of the logarithm gives

\[
\log p_0=-(n-1)\log 2-\sum_{h\ge1}\frac{2^h-1}{h}\sum_{j=0}^{n-2}r_j^h.
\]

For sufficiently large \(n\), this series is absolutely convergent. The first three power sums are

\[
\sum_j r_j=1-2/n,\quad
\sum_j r_j^2=4/(3n)-10/(3n^2)+O(n^{-3}),\quad
\sum_j r_j^3=2/n^2+O(n^{-3}).
\]

Their terms of order \(n^{-1}\) cancel exactly, while the sum over \(h\ge4\) is \(O(n^{-3})\). Therefore,

\[
p_0=2^{-(n-1)}e^{-1}\left(1+\frac{1}{3n^2}+O(n^{-3})\right).
\]

The two isolation products are

\[
p_m=p_0\prod_{j=0}^{n-2}\left(1+\frac{\delta}{N/2-j}\right),\qquad
p_{N-m}=p_0\prod_{j=0}^{n-2}\left(1-\frac{\delta}{N/2-j}\right).
\]

Set \(A=\sum_j(N/2-j)^{-1}=4/n+O(n^{-2})\) and \(B=\sum_j(N/2-j)^{-2}=O(n^{-3})\). Expanding the logarithms of the last two products and averaging cancels all odd powers of \(\delta\) and gives

\[
\frac{p_m+p_{N-m}}2
=p_0\left(1+\frac{8\delta^2}{n^2}+O(n^{-3})\right)
=p_0\left(1+\frac{2\varepsilon_n}{n^2}+O(n^{-3})\right).
\]

Combining with the preceding estimate for \(p_0\) yields

\[
n(p_m+p_{N-m})=\frac{4n}{e\,2^n}\left(1+\frac{1+6\varepsilon_n}{3n^2}+O(n^{-3})\right).
\]

The error terms from Step 2 are exponentially smaller than the last retained term, so the three claimed formulas follow.

## Verification

The standalone `verify.py` enumerates all balanced two-colour edge assignments for \(4\le n\le7\) and independently computes \(\kappa(H)+\kappa(\overline H)-2\). It checks the exact binomial isolation count against the exhaustive wild-number averages. It also tests the parity-sensitive asymptotic coefficients by high-order numerical comparisons for selected sizes through \(n=300\). See `verification_output.txt` for the recorded output. These finite tests corroborate but do not replace the unrestricted asymptotic proof.

## Relationship to prior work

Anders, Foster-Greenwood, Garcia and Krawzik established the two-colour identity expressing the wild number as the sum of monochromatic component deficits (arXiv:2508.06711, Theorem 6.4(2)). Dawkins, Nappo, Tong and Zimbizi studied uniformly random equitable two-colourings of complete graphs and proved only that their expected wild number tends to zero (arXiv:2610.22142, Section 3.2.1). Classical random-graph connectivity estimates, including those credited to Gilbert in the latter paper, motivate the isolation-first argument, but the qualitative bound used there does not yield the sharp \(4/e\) coefficient or the parity-sensitive \(n^{-2}\) correction. The claim here is exactly this detailed rare-event distributional and second-order quantitative refinement, not either established structural identity or the known qualitative limit.

## Limitations

The theorem concerns complete graphs with uniformly sampled equitable **two**-colourings, not arbitrary graphs, arbitrary colour balances or three or more colours. Neither the identity \(W_n=\kappa(H)+\kappa(\overline H)-2\) nor the qualitative decay \(\mathbb E W_n\to0\) is asserted as new. Published dense-random-graph connected-enumeration expansions might yield the fixed-size asymptotic via another route; exhaustive priority over such terminology has not been established. The proof is mathematical and independent human validation has not been performed.

## References

1. K. Anders, B. Foster-Greenwood, R. Garcia, N. Krawzik, *The Wild Number of an Edge-Colored Graph*, arXiv:2508.06711 (first submitted 2025-08-08), https://arxiv.org/html/2508.06711v1.
2. A. Dawkins, A. Nappo, J. Tong, C. Zimbizi, *Wild number for spanning trees in complete and complete bipartite graphs*, arXiv:2610.22142v1 (first submitted 2026-10-15), https://arxiv.org/html/2610.22142v1.
3. E. N. Gilbert, *Random graphs*, Ann. Math. Statist. 30 (1959), 1141–1144; cited for the qualitative random-graph connectivity estimate in Reference 2.
