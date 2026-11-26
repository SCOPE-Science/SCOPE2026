# A two-switch covariance law for induced graph motifs and degree frequencies

## Finding

Let \(G\sim G(n,p)\), with \(n\ge h\ge3\) and \(0<p<1\), and let \(H\) be a fixed simple graph on \(h\) vertices. Let \(X_H\) count the \(h\)-vertex subsets of \(G\) that induce a graph isomorphic to \(H\), and let \(N_k\) count vertices of degree exactly \(k\), for \(0\le k\le n-1\). The contribution is the sign classification for compatible induced motifs, its quantitative regular-motif window, and its sharp induced four-cycle transition. The exact covariance identity used in the proof is an inclusion–exclusion consequence of the earlier non-induced identity [6]; its derivation is included for clarity.

Write \(d_v=\deg_H(v)\), \(e_v=h-1-d_v\), and \(A_v=\binom{n-h}{k-d_v}/\binom{n-1}{k}\), taking an out-of-range binomial coefficient as zero. Let \(b_{a,j}(p)=\binom ajp^j(1-p)^{a-j}\) for \(0\le j\le a\) and zero otherwise. The supporting identity is
\[
\operatorname{Cov}(X_H,N_k)=\mathbb E[X_H] b_{n-1,k}(p)
\left[\sum_{v\in V(H)}\frac{A_v}{p^{d_v}(1-p)^{e_v}}-h\right].
\tag{1}
\]
Suppose \(H\) has at least one edge and at least one nonedge, and \(d_v\le k\le n-h+d_v\) for every \(v\), so all \(A_v>0\). Then
\[
 R(p)=\sum_{v\in V(H)} A_vp^{-d_v}(1-p)^{-e_v}
\]
has strictly convex logarithm, tends to infinity at both endpoints, and attains a unique minimum. As \(p\) moves through \((0,1)\), the covariance has exactly two sign reversals (positive, then negative, then positive) if \(\min R<h\), is positive except for one tangential zero if \(\min R=h\), and is positive everywhere if \(\min R>h\).

For a \(d\)-regular motif with \(1\le d\le h-2\), put \(r=h-1\), \(e=r-d\), and \(N=n-1\). When \(d\le k\le n-h+d\), the common coefficient is
\[
 A=\frac{(k)_d(N-k)_e}{(N)_r},\qquad (a)_j=a(a-1)\cdots(a-j+1),\quad (a)_0=1,
\]
and two reversals occur if and only if
\[
 A< \left(\frac d r\right)^d\left(\frac e r\right)^e.\tag{2}
\]
Equality gives one tangential zero; strict inequality in the other direction gives positivity everywhere. Outside the compatible range all the \(A_v\) vanish and the covariance is strictly negative on \((0,1)\). For fixed \(H\), if \((k_N-(d/r)N)/\sqrt N\to t\in\mathbb R\), then compatibility holds eventually and
\[
 N\log\left(\frac{A_N}{(d/r)^d(e/r)^e}\right)
  \longrightarrow \frac r2-\frac{r^3t^2}{2de}.\tag{3}
\]
Thus for sufficiently large \(N\) the covariance is positive at all interior \(p\) when \(|t|<\sqrt{de}/r\) and has exactly two reversals when \(|t|>\sqrt{de}/r\). No assertion is made at equality.

For induced \(C_4\) and \(N_2\), (1) specializes to
\[
 \operatorname{Cov}(X_{C_4},N_2)
 =12\binom n4p^4(1-p)^{n-2}\left[1-\binom{n-1}{2}p^2(1-p)\right].\tag{4}
\]
For \(n=4,5\) it is positive for every interior \(p\). For every \(n\ge6\) it is positive, negative, then positive, with transitions at the two roots in \((0,1)\) of \(p^2(1-p)=2/((n-1)(n-2))\). Thus six vertices are necessary and sufficient for double reversal for this pair. At \(p=c/n\) for fixed \(c>0\),
\[
 \lim_{n\to\infty}\operatorname{Cov}(X_{C_4},N_2)
 =\frac{c^4e^{-c}}2\left(1-\frac{c^2}2\right),\tag{5}
\]
which changes sign at \(c=\sqrt2\).

## Assumptions and scope

Graphs are simple, undirected and labeled on \([n]\), with independent Bernoulli edges of the same probability \(p\). An induced copy is counted once per vertex subset, not per embedding. Identity (1) also holds for complete or empty motifs and incompatible degrees with the zero-binomial convention. The sign classification and criterion (2) require the stated edge/nonedge and degree-compatibility conditions. The scaling in (3) keeps the regular motif fixed.

## Proof

**Conditional degree identity.** For a fixed \(h\)-subset \(S\), let \(I_S\) be its induced-\(H\) indicator. A vertex outside \(S\) has a degree independent of \(I_S\). Conditional on any particular induced labeled realization of \(H\) on \(S\), each internal degree \(d_v\) receives an independent-of-the-internal-edges contribution with law \(\operatorname{Bin}(n-h,p)\). The sum of the conditional degree-\(k\) probabilities over vertices of \(S\) is therefore \(\sum_v b_{n-h,k-d_v}(p)\) regardless of the realization. Summing the covariances over \(S\) and over degree indicators gives
\[
 \operatorname{Cov}(X_H,N_k)=\mathbb E[X_H]\left[\sum_v b_{n-h,k-d_v}(p)-h b_{n-1,k}(p)\right].
\]
The ratio of the conditional binomial mass to \(b_{n-1,k}(p)\) is exactly \(A_vp^{-d_v}(1-p)^{-e_v}\) for a compatible role and is zero otherwise. This proves (1).

**Logarithmic convexity.** Let \(\phi_v=\log A_v-d_v\log p-e_v\log(1-p)\) and \(w_v=e^{\phi_v}/R\). Differentiating twice gives
\[
 (\log R)''=\sum_v w_v\big(d_v/p^2+e_v/(1-p)^2\big)
 +\sum_v w_v(\phi_v')^2-\left(\sum_v w_v\phi_v'\right)^2>0.
\]
The first term is positive since \(d_v+e_v=h-1>0\); the difference of the other two is a variance. Some \(d_v>0\) and some \(e_v>0\), with positive \(A_v\), give divergence at the two endpoints. The logarithm has one interior minimum, is strictly decreasing before it and increasing after it, and has positive second derivative there. Comparison with \(\log h\) and the positive factor in (1) yields the claimed signs and tangent case.

**Regular motifs.** The binomial coefficient ratio is \((k)_d(N-k)_e/(N)_r\). For compatible \(k\), the sign is that of \(A-p^d(1-p)^e\); the monomial has unique maximum at \(p=d/r\), giving (2). For (3), put \(u_N=k_N/N\) and \(u=d/r\). The fixed-order falling-factorial expansion, uniform for \(u_N\) in a compact subinterval of \((0,1)\), is
\[
 \log A_N=d\log u_N+e\log(1-u_N)+
 \frac{r(r-1)-d(d-1)/u_N-e(e-1)/(1-u_N)}{2N}+O(N^{-2}).
\]
The numerator of the correction at \(u\) is \(r\). The log monomial has first derivative zero and second derivative \(-r^3/(de)\) there. Since \(u_N=u+t/\sqrt N+o(N^{-1/2})\), (3) follows by Taylor expansion. The strict signs follow from (2).

**Four-cycle transition.** There are three labeled four-cycles on a fixed four-set, so \(\mathbb E[X_{C_4}]=3\binom n4p^4(1-p)^2\). For each of its four roles the conditional probability of degree two equals \((1-p)^{n-4}\); substitution gives (4). The cubic \(p^2(1-p)\) increases up to \(2/3\) and decreases thereafter, with maximum \(4/27\). The strict two-root criterion \(\binom{n-1}{2}>27/4\) is equivalent to \(n\ge6\); it is never an equality for integer \(n\). At \(p=c/n\), the prefactor of (4) converges to \(c^4 e^{-c}/2\) and the bracket to \(1-c^2/2\), proving (5).

## Verification

The accompanying `verify.py` is an exact finite check against labeled graph enumeration at three rational probabilities. It checks the covariance formula for induced four-cycles on four, five and six vertices and for induced four-vertex paths on five and six vertices. The finite enumeration is not the proof of the sign theorem, the critical window, or the sparse limit.

## Relationship to prior work

The earlier arbitrary-motif non-induced covariance identity [6] already implies (1). For each injective map of \(H\), the induced indicator is the product of required-edge indicators times the product of complements for internal nonedges. Expansion over subsets of the internal nonedges expresses it as a signed sum of non-induced embedding indicators of all supergraphs on the motif's vertex set. Multiplying the non-induced copy counts by their respective automorphism orders converts them to injection counts; dividing the final sum by \(|\operatorname{Aut}(H)|\) yields \(X_H\). Covariance with \(N_k\) is linear, so [6] determines the induced formula. The exact covariance and its direct substitutions are not separate originality claims.

The related same-date finding [7] proves a single-switch law for non-induced motifs and exhibits two switches for induced \(P_3\) against \(N_1\), from four vertices on. That pair is outside the hypothesis of the present classification, because its degree-two motif role is incompatible with \(k=1\). The six-vertex boundary here is specific to induced \(C_4\) and \(N_2\), not a smallest-size claim among all motifs. The two findings are compared by content, without a priority inference from their shared date. The regular non-induced transition in [6] has only one threshold and a fixed-\(p\), constant-width degree correction, not the two-root merger and \(\sqrt N\)-width degree scaling in (3).

The other checked work provides context: [1] treats approximation of non-induced embedding counts, [2] studies motif fluctuations under edge-density perturbations, [3] studies limit theory for subgraph counts, and [4] studies vertex-degree statistics. The checked main fluctuation theorem of [5] is non-induced, and its Remark 2.12 explicitly distinguishes induced counts. The specific compatible-role sign classification and critical-window calculation are distinct from these comparisons. Uninspected full texts or an unlocated equivalent analysis remain possible.

## Limitations

There is no sign classification here for general irregular motifs with incompatible roles, no claim at the boundary of the regular critical window, and no joint limit theorem. The sparse assertion is restricted to the displayed pair and the stated scaling. The model does not include fixed degree sequences or dependent edges.

## References

1. M. Fürer and S. P. Kasiviswanathan, *Approximately Counting Embeddings into Random Graphs*, arXiv:0806.2287, https://arxiv.org/abs/0806.2287.
2. C. Fretter, M. Müller-Hannemann, and M.-T. Hütt, *Subgraph fluctuations in random graphs*, Physical Review E 85 (2012), 056119, https://doi.org/10.1103/PhysRevE.85.056119.
3. S. Janson, *A functional limit theorem for random graphs with applications to subgraph count statistics*, Random Structures & Algorithms 1 (1990), 15–37, https://doi.org/10.1002/rsa.3240010103.
4. B. Bollobás, *Vertices of given degree in a random graph*, Journal of Graph Theory 6 (1982), 147–155, https://doi.org/10.1002/jgt.3190060209.
5. S. Bhattacharya, A. Chatterjee, and S. Janson, *Fluctuations of Subgraph Counts in Graphon Based Random Graphs*, arXiv:2104.07259, https://arxiv.org/abs/2104.07259.
6. *Regular motifs share a universal degree-count covariance threshold*, Resultary, 2026-10-13, https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-regular-motifs-share-a-universal-degree-count-covariance-thresho--788dc5430332/RESULT.md.
7. *A one-switch law for degree-class motif covariance, with induced two-switch examples*, Resultary, 2026-10-18, https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-a-one-switch-law-for-degree-class-motif-covariance-with-induced--f5e8e8fd4466/RESULT.md.
