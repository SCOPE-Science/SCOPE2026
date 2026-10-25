# A square-root edge-completion bound for consecutive cycle sums

## Finding
For every integer \(n\ge9\), label the vertices of the cycle \(C_n\) consecutively \(1,2,\ldots,n\). Define \(\mathrm{mEC}(n)\) to be the minimum number of non-cycle edges to add so that each integer from \(1\) to \(T_n=n(n+1)/2\) occurs as the sum of labels of a nonempty connected vertex set. Put
\[
 m=\min\{r\ge4:T_r\ge n+4\}=\left\lceil\frac{\sqrt{8n+33}-1}{2}\right\rceil.
\]
Then adding exactly \(m-1\) chords
\[
 \{\{1,j\}:3\le j\le m\}\cup\{\{1,m+2\}\}
\]
produces a sum-complete graph. Consequently
\[
 \mathrm{mEC}(n)\le\left\lceil\frac{\sqrt{8n+33}-1}{2}\right\rceil-1=\sqrt{2n}+O(1),
 \qquad\lim_{n\to\infty}\mathrm{mEC}(n)/n=0.
\]
The bound proves the sublinearity question posed for edge completion of consecutive labeled cycles.

## Assumptions and scope
All graphs are simple and undirected; each vertex \(j\) has weight \(j\). A vertex set is connected when the subgraph it induces is connected. Its weight is the sum of its vertex labels. The graph has cycle edges \(\{j,j+1\}\) for \(1\le j<n\) and \(\{n,1\}\); no relabeling is allowed. The construction is an upper bound, with no assertion of the exact minimum or of optimal order. For \(n\ge9\), \(T_{n-4}\ge n+4\), hence \(m\le n-4\), and all the displayed chords are distinct genuine non-cycle edges. The proof is uniform for all \(n\ge9\).

## Proof
**Subset-sum lemma.** For every \(m\ge4\), the sums of subsets of \(\{2,3,\ldots,m\}\) form precisely
\[
 \{0,T_m-1\}\cup\{2,3,\ldots,T_m-3\}.
\]
For \(m=4\), the possible sums are \(0,2,3,4,5,6,7,9\). Suppose the assertion holds for \(m\), and put \(a=m+1\). In the new subset-sum set, the unshifted interval \([2,T_m-3]\), its translate \([m+3,T_m+m-2]\), and the old endpoint \(T_m-1\) join into every integer in \([2,T_m+m-2]\): the translated interval begins no later than one after the old interval since \(m+3\le T_m-2\) for \(m\ge4\), and it overlaps the old endpoint. The additional endpoints are \(0\) and \(T_m+m=T_{m+1}-1\). Neither \(1\) nor \(T_{m+1}-2=T_m+m-1\) is achievable, since the smallest selected element is \(2\) and the total of all elements is \(T_{m+1}-1\). This proves the lemma inductively.

Write \(T=n(n+1)/2\). By the lemma, every integer \(q\) with \(3\le q\le T_m-2\) has the form \(q=1+\sum_{j\in J}j\) for a set \(J\subseteq\{2,\ldots,m\}\). Since each \(j\in J\) is adjacent to \(1\) after adding the first family of chords (using the original cycle edge for \(j=2\)), the set \(\{1\}\cup J\) is connected.

For each integer \(b\) with \(m+2\le b\le n\), put \(H_b=\sum_{j=m+2}^b j=T_b-T_{m+1}\). The added edge \(\{1,m+2\}\) connects the cycle interval \(\{m+2,\ldots,b\}\) to \(\{1\}\cup J\). Hence every integer in
\[
 I_b=[H_b+3,H_b+T_m-2]\cap\mathbb Z
\]
is the weight of a connected vertex set. Successive intervals meet or are consecutive: since \(H_{b+1}=H_b+b+1\), their endpoints obey
\[
 (H_{b+1}+3)-(H_b+T_m-2)=b+6-T_m\le1,
\]
because \(b+1\le n\le T_m-4\). Therefore their union contains all integers from \(H_{m+2}+3=m+5\) through \(H_n+T_m-2=T-m-3\).

Every integer \(1\le s\le m+4\) is the sum of a one-vertex connected set \(\{s\}\), since \(m+4\le n\). Every integer from \(T-m-2\) through \(T\) is represented by the full cycle (weight \(T\)) or by all vertices other than a single vertex \(r\) with \(1\le r\le m+2\), which leaves a connected path of weight \(T-r\). These three ranges cover \([1,T]\) without a gap, proving the assertion. The exact chord count is \((m-2)+1=m-1\). Finally \(m=\sqrt{2n}+O(1)\), giving the stated upper bound and limit.

## Verification
The accompanying standard-library script `verify.py` checks the subset-sum lemma, the exact constructive interval cover for all \(9\le n\le124\), direct connectivity and weights for every prescribed witness for \(9\le n\le22\), and independently enumerates all connected subsets for \(9\le n\le14\). Additional larger parameter checks use \(n=125,240,500,1000,2000\). Executing `python3 verify.py` returns `VERIFY_OK`. These are finite consistency checks; the proof above establishes the unbounded statement.

## Relationship to prior work
Marotti and Needleman, *Consecutive Cycle Sums* (arXiv:2610.08889v1, first public 2026-10-06), study consecutive labels around a cycle, show that the unaugmented cycles are incomplete for \(n\ge8\), define the minimum edge-completion parameter, and prove an upper bound linear in \(n\). They explicitly ask whether the parameter is sublinear; the bound here answers this question affirmatively with an explicit family of star-like chords. Cambie and Groenland (2026), *Note on extremal problems about connected subgraph sums*, study the same general connected-weight-sum operator but predominantly graph reconstruction from weight spectra and sum-distinct weight assignments, not the fixed consecutive weights or the minimum completion problem. Neither result implies the present construction.

## Limitations
Only an upper bound is established; no matching lower bound, asymptotic sharpness, or exact formula for \(\mathrm{mEC}(n)\) is asserted. The construction is designed for \(n\ge9\), and no new assertion about smaller orders is made. Mathematical novelty is assessed against identifiable accessible literature and may be superseded by uncatalogued work.

## References
1. Jessica Marotti and Jonathan Needleman, *Consecutive Cycle Sums*, arXiv:2610.08889v1 (2026-10-06), https://arxiv.org/abs/2610.08889.
2. Stijn Cambie and Carla Groenland, *Note on extremal problems about connected subgraph sums*, *Graphs and Combinatorics* **42** (2026), article 35, DOI:10.1007/s00373-026-03026-8, https://link.springer.com/article/10.1007/s00373-026-03026-8.
