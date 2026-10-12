# All forcing subsets of perfect matchings in crown graphs
## Finding
For every integer \(n\ge 3\), let \(\operatorname{Cr}_n=K_{n,n}-\{a_i b_i:1\le i\le n\}\). Every perfect matching is uniquely
\[
M_\pi=\{a_i b_{\pi(i)}:1\le i\le n\}
\]
for a derangement \(\pi\in S_n\). For a subset \(F\subseteq M_\pi\), let
\[
U(F)=\{i:a_i b_{\pi(i)}\notin F\},
\]
and let \(t_2(\pi)\) be the number of \(2\)-cycles of \(\pi\).

Then \(F\) is a forcing set of \(M_\pi\) if and only if one of the following holds:

1. \(|U(F)|\le 1\); or
2. \(U(F)=\{i,j\}\) and \(\pi(i)=j\) or \(\pi(j)=i\).

In particular, no subset omitting at least three edges of \(M_\pi\) is forcing. Hence the complete forcing-subset enumerator of the fixed matching \(M_\pi\),
\[
\Phi_\pi(x)=\sum_{F\subseteq M_\pi\,\text{forcing}}x^{|F|},
\]
is
\[
\Phi_\pi(x)=x^n+n x^{n-1}+\bigl(n-t_2(\pi)\bigr)x^{n-2}.
\]
Thus every perfect matching has forcing number \(n-2\), but the number of minimum forcing sets is \(n-t_2(\pi)\), so the full forcing-set family still detects the number of transpositions in the derangement.

Let \(d_n\) denote the number of derangements of \([n]\). Summing over all perfect matchings gives the aggregate enumerator
\[
\sum_{\pi\,\text{derangement}}\Phi_\pi(x)
=d_nx^n+n d_nx^{n-1}+\left(n d_n-\binom n2 d_{n-2}\right)x^{n-2}.
\]
The standard forcing polynomial, which records only the minimum forcing number of each perfect matching, therefore collapses to \(d_nx^{n-2}\); the new statement is the complete classification and enumeration of all forcing subsets, together with the cycle-type-sensitive minimum-set count.

## Assumptions and scope
Graphs are finite and simple. A forcing set of a perfect matching \(M\) is a subset \(F\subseteq M\) that is contained in no other perfect matching. The statement is for every integer \(n\ge3\). The crown graph uses the fixed deleted matching \(\{a_i b_i\}\), and permutation notation is with respect to these labels.

The coefficient \(n-t_2(\pi)\) depends on the particular perfect matching through the number of \(2\)-cycles in its derangement. The aggregate coefficient counts pairs \((M,F)\), not distinct edge sets after forgetting which perfect matching they force.

## Proof
A perfect matching of \(\operatorname{Cr}_n\) chooses exactly one neighbor of each \(a_i\) and each \(b_j\), so it is a permutation matching \(M_\pi\). The deleted edges force \(\pi(i)\ne i\) for every \(i\), hence \(\pi\) is a derangement, and conversely every derangement gives a perfect matching.

Fix \(M_\pi\) and \(F\subseteq M_\pi\). Once the edges of \(F\) are fixed, any perfect matching containing \(F\) differs from \(M_\pi\) only on the omitted index set \(U=U(F)\). It is therefore a bijection from \(U\) onto \(\pi(U)\) avoiding the deleted diagonal edges \(a_i b_i\).

If \(|U|=0\) or \(|U|=1\), the completion is unique. Suppose \(U=\{i,j\}\). Besides the original assignments \(i\mapsto\pi(i)\) and \(j\mapsto\pi(j)\), the only possible completion swaps the two images. The swap is a valid matching exactly when both cross-edges exist, that is, exactly when \(\pi(j)\ne i\) and \(\pi(i)\ne j\). Therefore \(F\) is forcing precisely when \(\pi(i)=j\) or \(\pi(j)=i\).

Now suppose \(|U|\ge3\). Consider the undirected graph on \([n]\) obtained from the cycle decomposition of \(\pi\), with one edge for each adjacent pair in a permutation cycle; a \(2\)-cycle contributes one undirected edge. If \(U\) contains two vertices \(i,j\) that are not adjacent in this graph, then swapping \(\pi(i)\) and \(\pi(j)\) creates no fixed point, so it gives a second perfect matching containing \(F\). If every pair of vertices of \(U\) is adjacent, then \(U\) is a clique in a disjoint union of cycles. Such a clique has size at most three, and the only size-three case is exactly the vertex set of a \(3\)-cycle of \(\pi\). On those three vertices, replacing the cycle by its inverse gives a different derangement and hence a second perfect matching containing \(F\). Thus no \(F\) with \(|U|\ge3\) is forcing.

The forcing subsets of sizes \(n\) and \(n-1\) are therefore all such subsets, contributing \(1\) and \(n\), respectively. Minimum forcing subsets have size \(n-2\) and correspond exactly to adjacent unordered pairs in the cycle graph of \(\pi\). A cycle of length at least three contributes its length many adjacent pairs, while a \(2\)-cycle contributes one rather than two. Hence the number of adjacent pairs is \(n-t_2(\pi)\), proving the fixed-matching enumerator.

Finally, summing \(n-t_2(\pi)\) over all derangements gives \(n d_n\) minus the total number of occurrences of a \(2\)-cycle. For each unordered pair \(\{i,j\}\), forcing it to be a \(2\)-cycle leaves an arbitrary derangement on the remaining \(n-2\) points, so the total number of \(2\)-cycle occurrences is \(\binom n2 d_{n-2}\). This yields the aggregate formula.

## Verification
The accompanying `verify.py` independently enumerates every derangement for \(3\le n\le8\), every subset of every corresponding perfect matching, and directly counts how many derangements extend the selected matching edges. It checks the structural criterion without using it to compute the extension count, then checks each fixed-matching polynomial and the aggregate formula.

The replay output is:

`VERIFY_OK n_range=3..8 subset_checks=4053088 matching_checks=17007 aggregate_checks=6 cycle_type_checks=17007 max_order=16`

These finite computations are regression checks only; the proof above is the justification for all \(n\ge3\).

## Relationship to prior work
Klein and Randić introduced the equivalent innate-degree-of-freedom formulation for perfect matchings in 1987, and Harary, Klein, and Živković later used the forcing-number terminology. Pachter and Kim connected forcing sets to alternating-cycle hitting, and Adams, Mahdian, and Mahmoodian studied forcing numbers in bipartite graphs under MSC \(05C70\).

The 2015 forcing-polynomial paper defines the standard forcing polynomial by grouping perfect matchings according to their minimum forcing number. Under that definition the crown result here has the uninformative monomial \(d_nx^{n-2}\). The present statement refines that invariant by determining every forcing subset of every perfect matching and showing that the number of minimum forcing subsets is exactly \(n-t_2(\pi)\).

A later general theorem characterizes bipartite graphs whose minimum forcing number equals \(n-2\). That broader result can cover the scalar minimum for crown graphs, so the equality \(f(\operatorname{Cr}_n)=n-2\) is not claimed as the original contribution here. The new content is the all-subset classification, the per-matching cycle-type dependence, and the aggregate pair enumerator.

## Limitations
The result does not address global forcing sets, complete forcing sets, anti-forcing sets, or forcing subsets outside a fixed perfect matching. It does not claim that no equivalent all-subset formula exists in unindexed literature; the literature comparison found no such crown-graph statement under the aliases “complete bipartite graph minus a perfect matching,” “complete bipartite graph minus a \(1\)-factor,” or “bipartite Kneser graph \(H(n,1)\).”

The earliest exact-day source used for the archival date is the 1987 Klein–Randić article. A 1985 book chapter is cited in the 2011 survey as an earlier root of the same chemical notion, but the material inspected here did not provide a trustworthy day-level public date for that chapter, so no day was invented for it.

## References
1. D. J. Klein and M. Randić, “Innate degree of freedom of a graph,” Journal of Computational Chemistry 8 (1987), 516–521. DOI: 10.1002/jcc.540080432.
2. F. Harary, D. J. Klein, and T. P. Živković, “Graphical properties of polyhexes: perfect matching vector and forcing,” Journal of Mathematical Chemistry 6 (1991), 295–306. DOI: 10.1007/BF01192587.
3. L. Pachter and P. Kim, “Forcing matchings on square grids,” Discrete Mathematics 190 (1998), 287–294. DOI: 10.1016/S0012-365X(97)00266-5.
4. P. Adams, M. Mahdian, and E. S. Mahmoodian, “On the forced matching numbers of bipartite graphs,” Discrete Mathematics 281 (2004), 1–12. DOI: 10.1016/j.disc.2002.10.002.
5. Z. Che and Z. Chen, “Forcing on Perfect Matchings – A Survey,” MATCH Communications in Mathematical and in Computer Chemistry 66 (2011), 93–136.
6. H. Zhang, S. Zhao, and R. Lin, “The Forcing Polynomial of Catacondensed Hexagonal Systems,” MATCH Communications in Mathematical and in Computer Chemistry 73 (2015), 473–490.
7. Q. Liu and H. Zhang, “Some tight bounds on the minimum and maximum forcing numbers of graphs,” arXiv:2106.09209; later published in Discrete Applied Mathematics.
