# Rank-refined nilpotent census and a square-root boundary for symmetric-inverse sandwich semigroups

## Finding
Fix a positive integer \(n\) and a partial bijection \(\sigma\) of an \(n\)-element set, of rank \(0\le r\le n\). Write \(\mathcal I_n\) for the symmetric inverse monoid of all partial bijections, including the empty map, and equip it with the sandwich product \(f\star g=f\sigma g\), with transformations composed left to right. An element is **nilpotent** if one of its positive powers under this product is empty. For every rank \(0\le k\le n\), the number of nilpotent rank-\(k\) elements is
\[
N_{n,r,k}=\binom nk^2k!-r\binom{n-1}{k-1}^{\!2}(k-1)!
=\binom nk^2k!\left(1-\frac{rk}{n^2}\right).
\]
The second term is defined to be zero when \(k=0\) or \(r=0\). Consequently, conditional on rank \(k\), uniform sampling gives the exactly linear probability \(1-rk/n^2\), and the polynomial \(\sum_{k=0}^n N_{n,r,k}z^k\) is the complete rank-refined nilpotent census. The result depends only on the rank of the sandwich element, not its domain, image, or specific arrows.

For uniform \(F\in\mathcal I_n\), let \(P_{n,r}=\Pr(F\text{ is nilpotent under }\star)\). If \(r/n\to\rho\in[0,1]\), then \(P_{n,r}\to 1-\rho\). At the sharp boundary, if \(r=n-s_n\), \(0\le s_n\le n\), and \(s_n/\sqrt n\to\tau\ge0\), then
\[
\sqrt n\,P_{n,n-s_n}\longrightarrow1+\tau.
\]
In particular, for the ordinary symmetric inverse monoid (\(r=n\)), the nilpotent proportion is asymptotic to \(1/\sqrt n\). The novelty claim concerns the full sandwich-rank census and the boundary transition, not the previously studied ordinary case by itself.

## Assumptions and scope
A partial bijection is a bijection between two subsets of the base set. Its rank is the size of its domain. The empty map is the zero of every variant. All formulas hold for every integer \(n\ge1\), \(r,k\in\{0,\ldots,n\}\), and every sandwich element of rank \(r\); no restriction on its cycle structure is imposed. The product \(f\sigma g\) means apply \(f\), then \(\sigma\), then \(g\), whenever all stages are defined. Counts are for labeled base sets. The limiting formulas concern sequences of such monoids as \(n\to\infty\).

## Proof
**Reduction to a partial identity.** Any rank-\(r\) partial bijection has the form \(\sigma=\alpha e_R\beta\), where \(\alpha,\beta\) are total permutations and \(e_R\) is identity on a fixed \(r\)-element subset \(R\) and undefined elsewhere. The rank-preserving bijection \(f\mapsto\beta f\alpha\) intertwines the \(\sigma\)-variant product with the \(e_R\)-variant product. It is therefore enough to count nilpotent elements for \(\sigma=e_R\).

**Cycle criterion.** Draw the arrows of a partial bijection \(f\) as a directed graph. Its connected components are directed paths and directed cycles. A sandwich power of \(f\) traces a sequence of \(f\)-arrows whose intermediate vertices must lie in \(R\). If any directed cycle lies wholly in \(R\), powers remain nonempty. Conversely, if arbitrarily long sandwich powers were nonempty, a repeated intermediate vertex would exhibit a directed cycle wholly in \(R\), because a partial bijection has at most one outgoing edge per vertex. Thus \(f\) is sandwich-nilpotent if and only if it has no directed cycle whose vertices all lie in \(R\).

**Signed cycle inclusion-exclusion.** There are \(\binom nk^2 k!\) rank-\(k\) partial bijections. A selected family of vertex-disjoint cycles wholly contained in \(R\) has a vertex union \(T\) of size \(t\) and is the cycle decomposition of some permutation \(\pi\in S_T\). Once its cycle edges are fixed, there are exactly \(\binom{n-t}{k-t}^{2}(k-t)!\) rank-\(k\) partial bijections extending them. Inclusion-exclusion therefore gives
\[
N_{n,r,k}=\sum_{t=0}^{\min(r,k)}\binom rt\binom{n-t}{k-t}^2(k-t)!\sum_{\pi\in S_t}(-1)^{c(\pi)},
\]
where \(c(\pi)\) is the number of cycles, including fixed points. The classical cycle-index identity \(\sum_{\pi\in S_t}u^{c(\pi)}=u(u+1)\cdots(u+t-1)\) makes the inner sum equal to \(1\) for \(t=0\), \(-1\) for \(t=1\), and \(0\) for every \(t\ge2\). Only the first two terms survive, proving the count. The quotient of the second term without \(r\) by the total count is \(k/n^2\), proving the conditional probability.

**Unconditional law and the boundary.** Let \(K=\operatorname{rank}(F)\), \(J=n-K\). Then \(\Pr(J=j)\) is proportional to
\[
w_{n,j}=\binom nj^2(n-j)!,\qquad \frac{w_{n,j+1}}{w_{n,j}}=\frac{n-j}{(j+1)^2}.
\]
The ratio is uniformly bounded above one on \(j\le(1-\epsilon)\sqrt n\) and below one on \(j\ge(1+\epsilon)\sqrt n\), for each fixed \(\epsilon\in(0,1)\) and sufficiently large \(n\). Comparing the resulting geometric tails to a weight at the modal index gives \(J/\sqrt n\to1\) in probability. Also, reindexing the ratio identity yields the exact moment relation \(\mathbb E[J(J+1)]=n\); hence the squared rescaled variables have uniformly bounded means. They are therefore uniformly integrable, and \(\mathbb E[J]/\sqrt n\to1\). Averaging the exact conditional formula gives
\[
P_{n,r}=1-\frac rn+\frac r{n^2}\mathbb E[J].
\]
The two asymptotic assertions follow immediately, substituting \(r/n\to\rho\) or \(r=n-s_n\), respectively.

## Verification
A standalone pure-Python checker enumerates every partial injection on labeled sets of sizes \(1\) through \(6\). For every sandwich rank, it tests nilpotency by actual repeated sandwich multiplication and compares each rank-stratum count with the formula. It also tests arbitrary noncanonical sandwich maps and the exact moment identity for larger \(n\) using integer arithmetic. Reproduce with `python3 verify.py`. The finite enumerations are consistency checks, not substitutes for the full proof.

## Relationship to prior work
Tsyaputa (2005) studies nilpotent **subsemigroups** and structural reductions of variants of symmetric inverse semigroups. The reduction of a sandwich element to rank-normal form and the relevance of nilpotence are inherited context, not claimed new. Ganyushkin and Mazorchuk (2004) treat nilpotents in the **ordinary** symmetric inverse semigroup, corresponding to the case \(r=n\). Đurđev, Dolinka, and East (2019) study structural properties of diagram-category sandwich semigroups, including the symmetric-inverse setting. Laradji and Umar (2022) count different combinatorial statistics of ordinary partial bijections. The all-rank, all-sandwich-rank conditional formula and its square-root boundary were not located in the materially inspected texts or the additional available research-record searches. That observation is evidence from examined coverage, not a proof of historical uniqueness.

## Limitations
This theorem addresses nilpotence of **individual elements** under a fixed sandwich product, not the classification of nilpotent subsemigroups, maximal nilpotent subsemigroups, or full nilpotency-index distributions. The parameter \(n\) must be finite. The formula is an exact enumeration, not a statement that an earlier combinatorial technique is independently new. The full 2004 ordinary-semigroup paper was not available for a complete text comparison, leaving residual priority risk for equivalent formulations; its original-case coverage is explicitly excluded from any independent novelty claim.

## References
1. G. Y. Tsyaputa, *Isolated and nilpotent subsemigroups in the variants of the symmetric inverse semigroup*, 2005, arXiv:math/0508387; accessible full text: https://arxiv.org/pdf/math/0508387.
2. I. Đurđev, I. Dolinka, and J. East, *Sandwich semigroups in diagram categories*, first publicly posted 2019-10-23, arXiv:1910.10286; accessible full text: https://arxiv.org/pdf/1910.10286.
3. A. Laradji and A. Umar, *Further combinatorial results for the symmetric inverse monoid*, Algebra and Discrete Mathematics 33 (2022), DOI:10.12958/adm1793; accessible full text: https://admjournal.luguniv.edu.ua/index.php/adm/article/viewFile/1793/pdf.
4. O. Ganyushkin and V. Mazorchuk, *Combinatorics of nilpotents in symmetric inverse semigroups*, Annals of Combinatorics (2004), DOI:10.1007/s00026-004-0213-7 (abstract-level comparison only).
