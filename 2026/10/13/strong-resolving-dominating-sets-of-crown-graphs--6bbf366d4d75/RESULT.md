# Strong resolving dominating sets of crown graphs
## Finding
For every integer \(n\ge3\), let \(\operatorname{Cr}_n=K_{n,n}-M\) be the crown graph with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and with the perfect matching \(a_ib_i\) deleted. A vertex set \(S\subseteq V(\operatorname{Cr}_n)\) is strong resolving and dominating if and only if it contains at least one endpoint of every deleted pair \(\{a_i,b_i\}\) and is not one of the following \(2n\) exceptional transversals:
\[
\{b_i\}\cup(A\setminus\{a_i\}),
\qquad
\{a_i\}\cup(B\setminus\{b_i\}),
\qquad 1\le i\le n.
\]

Thus, if
\[
R_{srD}(\operatorname{Cr}_n;z)=\sum_{S}z^{|S|}
\]
sums over all strong resolving dominating sets, then
\[
R_{srD}(\operatorname{Cr}_n;z)=z^n\bigl((z+2)^n-2n\bigr).
\]
In particular,
\[
\gamma_{sr}(\operatorname{Cr}_n)=n,
\]
and the number of minimum strong resolving dominating sets is
\[
2^n-2n.
\]

## Assumptions and scope
All graphs are finite, simple, undirected, and connected. A vertex \(w\) strongly resolves distinct vertices \(u,v\) if one of \(u,v\) lies on a shortest path joining the other to \(w\). A strong resolving dominating set is simultaneously a strong resolving set and a dominating set.

The crown graph \(\operatorname{Cr}_n\) has edges \(a_ib_j\) exactly when \(i\ne j\). For \(n\ge3\), its relevant distances are
\[
d(a_i,b_i)=3,
\qquad d(a_i,a_j)=d(b_i,b_j)=2\quad(i\ne j),
\qquad d(a_i,b_j)=1\quad(i\ne j).
\]

## Proof
We first characterize the strong resolving sets.

Suppose that neither endpoint of some deleted pair \(\{a_i,b_i\}\) belongs to \(S\). The two omitted vertices have distance \(3\). Any third vertex has distances \(1\) and \(2\) from this pair, so the absolute difference of those two distances is \(1\), not \(3\). Hence no third vertex strongly resolves \(a_i,b_i\). Therefore every strong resolving set meets every deleted pair.

Conversely, suppose that \(S\) meets every deleted pair. Any pair with an endpoint in \(S\) is strongly resolved by that endpoint. Consider two vertices \(u,v\notin S\). They belong to different deleted pairs. Let \(u^*\in S\) be the deleted-match partner of \(u\). If \(u=a_i\), then \(u^*=b_i\), and for every \(v\) from a different pair one has
\[
d(a_i,v)+d(v,b_i)=3=d(a_i,b_i).
\]
Indeed, the two summands are \(2\) and \(1\) when \(v\in A\), and \(1\) and \(2\) when \(v\in B\). Thus \(v\) lies on a shortest \(a_i\)-to-\(b_i\) path, so \(b_i\) strongly resolves \(u,v\). The case \(u=b_i\) is symmetric. Hence
\[
S\text{ is strong resolving}\quad\Longleftrightarrow\quad
S\cap\{a_i,b_i\}\ne\varnothing\text{ for every }i.
\]

It remains to impose domination. Let \(S\) meet every deleted pair but fail to dominate. If an omitted vertex \(a_i\) has no neighbor in \(S\), then
\[
S\cap B\subseteq\{b_i\}.
\]
Because the pair \(\{a_i,b_i\}\) must be met, \(b_i\in S\). For each \(j\ne i\), the absence of \(b_j\) forces \(a_j\in S\). Therefore
\[
S=\{b_i\}\cup(A\setminus\{a_i\}).
\]
Conversely, this set leaves \(a_i\) undominated. The symmetric argument gives the second exceptional family \(\{a_i\}\cup(B\setminus\{b_i\})\). These are the only failures of domination among strong resolving sets.

To count all sets, each deleted pair contributes three choices compatible with strong resolution: choose only \(a_i\), choose only \(b_i\), or choose both. Their generating factor is
\[
2z+z^2=z(z+2).
\]
Hence all strong resolving sets have enumerator \(z^n(z+2)^n\). Removing the \(2n\) exceptional non-dominating transversals, each of size \(n\), gives
\[
R_{srD}(\operatorname{Cr}_n;z)=z^n\bigl((z+2)^n-2n\bigr).
\]
The least exponent is \(n\), and its coefficient is \(2^n-2n>0\) for \(n\ge3\), proving both remaining assertions.

## Verification
The included checker constructs \(\operatorname{Cr}_n\), computes all-pairs distances, tests strong resolution from the defining shortest-path equality, tests domination directly, and compares every vertex subset with the theorem's membership criterion.

For every \(3\le n\le8\), all \(2^{2n}\) subsets are examined. The checker also compares every cardinality coefficient with the closed enumerator, the minimum value with \(n\), and the number of minimum sets with \(2^n-2n\).

## Relationship to prior work
The 2020 paper defining strong resolving domination studies the join and corona operations and records the general lower bounds inherited from domination and strong metric dimension. Its full text contains no crown, bipartite, or matching specialization.

Earlier strong-metric work on direct products is directly relevant because
\[
\operatorname{Cr}_n\cong P_2\times K_n.
\]
That work proves that the strong resolving graph of \(P_2\times K_n\) is a disjoint union of \(n\) copies of \(K_2\). Together with the standard vertex-cover characterization of strong metric generators, this already implies the precursor fact that strong resolving sets meet every deleted matched pair. It does not impose domination, identify the \(2n\) non-dominating transversals, or give the strong-resolving-domination enumerator above.

A 2023 continuation characterizes strong resolving domination for lexicographic products. A later paper studies the equivalent hybrid under the name dominant strong metric dimension for complete bipartite, fan, wheel, helm, join, corona, generalized-join, and comaximal graphs. The inspected full text of that later work contains no crown, direct-product, tensor-product, or matching specialization.

## Limitations
The theorem is specific to connected crown graphs \(\operatorname{Cr}_n\) with \(n\ge3\). The disconnected graph \(\operatorname{Cr}_2\) is excluded. No claim is made for deleting a nonperfect matching from \(K_{n,n}\), for unbalanced bipartite graphs, or for general direct products.

The strong-resolving half of the membership criterion is consistent with prior direct-product strong-metric theory; the new content assessed here is the exact interaction with domination, including the complete exception list and the all-cardinality enumerator. The exhaustive computation is corroborative only; the arbitrary-\(n\) result follows from the proof.

## References
1. G. B. Monsanto, P. L. Acal, H. M. Rara, “On Strong Resolving Domination in the Join and Corona of Graphs,” European Journal of Pure and Applied Mathematics 13(1) (2020), 170–179, DOI 10.29020/nybg.ejpam.v13i1.3625.
2. J. A. Rodríguez-Velázquez, I. G. Yero, D. Kuziak, O. R. Oellermann, “On the strong metric dimension of Cartesian and direct products of graphs,” Discrete Mathematics 335 (2014), 8–19, DOI 10.1016/j.disc.2014.06.023; arXiv:1307.4722v1.
3. G. B. Monsanto, P. L. Acal, H. M. Rara, “Strong Resolving Domination in the Lexicographic Product of Graphs,” European Journal of Pure and Applied Mathematics 16(1) (2023), 363–372, DOI 10.29020/nybg.ejpam.v16i1.4652.
4. M. Valiyanpour, K. Khashyarmanesh, M. Afkhami, “The dominant strong metric dimension of graphs,” AKCE International Journal of Graphs and Combinatorics (2025), DOI 10.1080/09728600.2025.2574313.
