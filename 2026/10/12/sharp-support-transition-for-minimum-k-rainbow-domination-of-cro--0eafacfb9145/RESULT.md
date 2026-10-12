# Sharp support transition for minimum \(k\)-rainbow domination of crown graphs

## Finding

Let \(k\ge3\) and \(n\ge2k\) be integers. The minimum weight of a \(k\)-rainbow dominating function on the crown graph \(\operatorname{Cr}_n\) is \(2k\). All functions attaining this value belong to precisely the following disjoint families.

**Common-support family.** Choose \(T\subseteq[n]\) with \(1\le t=|T|\le k\) and independently choose two surjections \(\alpha,\beta:[k]\twoheadrightarrow T\). Assign color \(c\) to the two vertices \(a_{\alpha(c)}\) and \(b_{\beta(c)}\). No other colors are assigned. Thus the nonempty-labeled vertices on the two shores have the same set of matched indices \(T\); each color occurs exactly once on each shore. Different choices give different functions.

**One-sided family.** This family exists only when \(n=2k\). Choose either shore, give each of its \(2k\) vertices a singleton color, and require every color to occur exactly twice. Give every vertex on the opposite shore the empty set. These are all the remaining minima.

If \({k\brace t}\) denotes the Stirling number of the second kind, the number of minimum functions is exactly
\[
M_{n,k}=\sum_{t=1}^{k}\binom nt\bigl(t!{k\brace t}\bigr)^2
+\mathbf1_{\{n=2k\}}\frac{2(2k)!}{2^k}.
\]
The common-support summand is valid for all \(n\ge2k\). The exceptional term is supported exactly on the boundary \(n=2k\). Examples are \(M_{6,3}=1446\) and \(M_{7,3}=2023\). For fixed \(k\), the leading growth is \(k!n^k+O_k(n^{k-1})\) as \(n\to\infty\), since the term \(t=k\) contributes \(\binom nk(k!)^2\).

## Assumptions and scope

The crown graph \(\operatorname{Cr}_n\) has vertices \(\{a_i,b_i:1\le i\le n\}\) and edges \(a_i b_j\) exactly when \(i\ne j\). A \(k\)-rainbow dominating function is a map \(f:V(\operatorname{Cr}_n)\to2^{[k]}\) with the property that, for each vertex \(v\) with \(f(v)=\varnothing\), the union \(\bigcup_{u\in N(v)}f(u)\) is \([k]\). Its weight is \(w(f)=\sum_v|f(v)|\), and \(\gamma_{rk}\) is the minimum weight. The theorem concerns all integers \(k\ge3\) and \(n\ge2k\), labeled graph vertices and fixed distinguishable colors. It does not identify functions modulo graph or color permutations.

## Proof

First, the labeling \(f(a_1)=f(b_1)=[k]\), with every other vertex assigned the empty set, has weight \(2k\). Every empty vertex has index different from \(1\) and sees the full set of colors at the opposite vertex of index \(1\), so it is valid.

For a lower bound, suppose a labeling has weight less than \(2k\). Each shore has \(n\ge2k\) vertices, so it has an empty-labeled vertex: occupying an entire shore would already cost at least \(n\ge2k\). An empty vertex on the left needs all \(k\) colors somewhere on the right, hence the total weight of the right shore is at least \(k\). By exchanging the shores, the left-shore weight is also at least \(k\), a contradiction. Therefore the minimum is \(2k\).

Now suppose \(w(f)=2k\) and both shores contain an empty vertex. The preceding color-cover argument gives shore weights at least \(k\) each, so both are exactly \(k\). Every color must occur at least once on each shore, hence exactly once there. Define \(\alpha(c)\) and \(\beta(c)\) as the unique indices of the vertices bearing color \(c\) on the left and right, respectively. If some \(a_i\) is labeled, then \(b_i\) cannot be empty: it is not adjacent to \(a_i\), so it would be missing every color assigned to \(a_i\), each occurring nowhere else on the left. Thus the support index set on the left is contained in that on the right. The symmetric argument proves equality. Calling this common set \(T\), both maps \(\alpha,\beta\) are surjective onto \(T\), so this is exactly the stated common-support family. Conversely, every empty vertex then has index outside \(T\); it is adjacent to every colored vertex on the opposite shore and sees all \(k\) colors. Therefore all described common-support functions work.

The only remaining possibility is that one shore has no empty vertices. As \(w(f)=2k\), this implies \(n=2k\), all \(n\) vertices of that shore have singleton labels, and every vertex of the other shore is empty. For an opposite-shore vertex of index \(i\) to see color \(c\), color \(c\) must occur somewhere other than index \(i\), so each color occurs at least twice. Because there are \(2k\) singleton labels in total, every color occurs exactly twice. This condition is also sufficient. It proves the disjoint, exhaustive two-family classification.

For any fixed \(t\), the nonempty set \(T\) can be chosen in \(\binom nt\) ways. There are \(t!{k\brace t}\) surjections from \([k]\) to \(T\) on each shore, independently. The one-sided family has \(2\) choices of shore and \((2k)!/(2!)^k\) assignments of the color multiset with two copies of each color. Summing the two disjoint families gives the formula. At \(n\ge2k+1\) the one-sided construction is impossible; at \(n=2k\) it exists, proving the sharp transition.

## Verification

A standalone C++17 exhaustive checker is included as `verify.cpp`. It considers every assignment of at most \(2k\) color incidences to the \(2n\) vertices, tests the defining condition directly at every empty vertex, independently tests the two structural families, and evaluates the Stirling-based prediction. It exhaustively checks \((k,n)=(1,2),(1,3),(2,4),(2,5),(3,6),(3,7)\). In particular, for \((3,6)\) the checker finds \(1446\) minima (\(1266\) common-support and \(180\) one-sided) among \(2391496\) tested incidence subsets; for \((3,7)\) it finds \(2023\), all common-support, among \(6220768\) tested incidence subsets. No smaller-weight function was found in these finite tests. These tests do not establish the infinite theorem; the argument under Proof does.

Reproduce with `c++ -O2 -std=c++17 verify.cpp -o verify && ./verify` and check the terminal line `VERIFY_OK`.

## Relationship to prior work

Rainbow domination was introduced by Brešar, Henning and Rall (2005). Their full 2008 treatment proves the weight-preserving correspondence with dominating sets of the Cartesian product \(G\square K_k\) and general inequalities; the general upper inequality supplies the known bound \(\gamma_{rk}(\operatorname{Cr}_n)\le2k\), not the matching lower bound or the minimum-optimizer count. Consequently the formula here also counts the minimum dominating sets of \(\operatorname{Cr}_n\square K_k\) through that correspondence.

The \(k=2\) crown minimum-function classification is already known, and is used only as a consistency check; this finding is restricted to \(k\ge3\). Sivagami's 2018 conference abstract explicitly concerns bounds for \(3\)-rainbow domination of crown graphs; the one-page published abstract does not specify its bounds or an optimizer classification. It is a relevant near source, not proof that a possible full treatment lacks the theorem here. This leaves a documented coverage risk.

## Limitations

No conclusion is claimed for \(n<2k\), or for variants such as independent, restrained or generalized rainbow domination. The primary literature comparison is necessarily non-exhaustive, especially for the 2018 crown-specific abstract for which a fuller manuscript was not located. The proof is a direct mathematical argument; the finite checker is a reproducible consistency test only. Independent external verification has not been performed.

## References

1. B. Brešar, M. A. Henning, D. F. Rall, “Paired-domination of Cartesian products of graphs and rainbow domination,” *Electronic Notes in Discrete Mathematics* 22 (2005), 233–237, https://doi.org/10.1016/j.endm.2005.06.059 (public issue dated 2005-10-15).
2. B. Brešar, M. A. Henning, D. F. Rall, “Rainbow Domination in Graphs,” *Taiwanese Journal of Mathematics* 12 (2008), 213–225, https://doi.org/10.11650/twjm/1500602498.
3. P. Sivagami, “On 3-Rainbow Domination in Crown Graphs,” *Proceedings of the Fourth International Conference on Science, Engineering and Technology* (2018), conference abstracts, p. 39, ISBN 978-93-86675-42-2, https://www.isca.co.in/SOUV_PROC/conference/ISBN%20978-93-86675-42-2.pdf.
