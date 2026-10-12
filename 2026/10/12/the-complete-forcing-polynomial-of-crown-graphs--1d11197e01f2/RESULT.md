# The complete-forcing polynomial of crown graphs

## Finding

For each integer \(n\ge3\), let \(G=\operatorname{Cr}_n=K_{n,n}-M\), with vertices \(a_i,b_i\) indexed by \([n]\), and edges \(a_i b_j\) precisely when \(i\ne j\). An edge set \(S\) is **complete forcing** when, for every perfect matching \(P\) of \(G\), the selected edges \(S\cap P\) belong to no other perfect matching. Put
\[
\mathcal F_n(t)=\sum_{\substack{S\subseteq E(G)\\S\text{ complete forcing}}}t^{|S|},\qquad h(z)=2z+z^2.
\]
Then the **entire cardinality distribution** of complete forcing sets is
\[
\mathcal F_n(t)=t^{n(n-1)}B_n(t^{-1}),
\]
where, for \(n=3\),
\[
B_3(z)=(1+z)^6-2z^3(1+z)^3+z^6;
\]
for \(n=4\),
\[
B_4(z)=1+6h(z)+4\sum_{k=2}^{3}\binom3k h(z)^k+4h(z)^3;
\]
and, for every \(n\ge5\),
\[
B_n(z)=1+\binom n2h(z)+n\sum_{k=2}^{n-1}\binom{n-1}{k}h(z)^k
+\binom n3\left(h(z)^3-2z^3(1+z)^3+z^6\right).
\]
More precisely, put \(T=E(G)\setminus S\), and identify its edge \(a_i b_j\) with a directed arc \(i\to j\). For \(n\ge4\), \(S\) is complete forcing exactly when the unordered two-element supports \(\{i,j\}\) of all arcs in \(T\) are pairwise intersecting, and (only when \(n\ge5\)) \(T\) contains neither orientation of a directed triangle. For \(n=3\), \(T\) must omit at least one edge of each of the two alternating perfect matchings of the six-cycle.

As consequences, \(\operatorname{cf}(\operatorname{Cr}_3)=2\), \(\operatorname{cf}(\operatorname{Cr}_4)=6\), and \(\operatorname{cf}(\operatorname{Cr}_n)=(n-1)(n-2)\) for \(n\ge5\). The numbers of minimum complete forcing sets are respectively \(9\), \(8\), and \(n\). The scalar extremal values agree with the previously studied minimum-number problem; the full distribution and all-set classification are the refinement asserted here.

## Assumptions and scope

All graphs are finite, simple and undirected. A perfect matching covers every vertex with exactly one edge. For a fixed perfect matching \(P\), a subset \(F\subseteq P\) is forcing when \(P\) is the only perfect matching containing \(F\). A **nice cycle** is an even cycle whose removal leaves a graph with a perfect matching. Each nice cycle has two alternating edge frames. Complete forcing sets meet both frames of every nice cycle (the standard nice-cycle criterion). Indices of arcs are labels, not vertices of an auxiliary directed graph; antiparallel arcs may both occur.

## Proof

**Step 1: unavoidable obstructions.** Assume \(n\ge4\). If \(T\) contains arcs \(i\to j\) and \(k\to\ell\) with four distinct indices, the two corresponding edges are one frame of the four-cycle on rows \(i,k\) and columns \(j,\ell\). It is a *nice* four-cycle: on the remaining \(n-2\) vertices of each bipartition class, the graph is complete bipartite with at most a partial matching of edges deleted. For any order at least two, such a graph has a perfect matching (a full deleted diagonal leaves its complementary derangement; deleting fewer edges cannot destroy that matching). Thus every complete forcing complement \(T\) has pairwise-intersecting unordered supports.

For \(n\ge5\), if \(T\) contains arcs \(i\to j\), \(j\to k\), \(k\to i\) on distinct indices, these arcs are one frame of the six-cycle on rows and columns indexed by \(\{i,j,k\}\). Its complement is \(\operatorname{Cr}_{n-3}\), which has a perfect matching because \(n-3\ge2\). Both directed orientations are therefore forbidden. When \(n=4\), the remaining row and column instead have the *same* index and are not adjacent, so this six-cycle is not nice.

**Step 2: no other obstructions.** An intersecting family of unordered two-element sets is a star or lies in the three edges of one triangle. Indeed, if two distinct sets meet at \(c\), any set avoiding \(c\) must consist of their two other elements; any further set meeting all three stays in that triangle. If \(T\) has star support, any matching of edges from \(T\) has at most two edges, since every arc uses the distinguished label at its tail or head. No two arcs of star support can form a frame of a four-cycle: two oppositely positioned arcs on adjacent index pairs have a missing diagonal cross-edge, while similarly positioned arcs share a graph endpoint. Thus \(T\) contains no complete frame of any nice cycle.

If \(T\) has triangle support, no two arcs form a four-cycle frame for the same missing-diagonal reason. Every matching of three arcs from \(T\) must use all three indices on both its row and column side, and, with loops prohibited, is exactly one of the two directed three-cycles. No matching of four arcs can occur. For \(n\ge5\), excluding these two directed three-cycles excludes every possible nice-cycle frame. For \(n=4\), their six-cycles are not nice, as shown above; therefore all triangle-support complements are allowed. For \(n=3\), the graph is one six-cycle, and its two perfect matchings are its two forbidden frames. The structural classification follows.

**Step 3: count every admissible complement.** For a given unordered index pair, there are two possible oriented arcs; choosing a nonempty subset has weight \(h(z)=(1+z)^2-1\). A support with exactly one unordered pair contributes \(\binom n2h(z)\). Supports having at least two distinct pairs and forming a star have a unique center; choosing \(k\ge2\) of its \(n-1\) spokes and nonempty arc orientations contributes \(n\binom{n-1}{k}h(z)^k\). Supports consisting of all three pairs of a triangle contribute \(\binom n3h(z)^3\) when \(n=4\). For \(n\ge5\), exclude the two directed three-cycle events: each contributes \(z^3(1+z)^3\) because its three mandatory arcs leave three optional reverse arcs. Their intersection contributes \(z^6\), restoring it once by inclusion–exclusion. The empty complement contributes \(1\). The six-cycle case is the same two-event inclusion–exclusion on six available edges, with each three-edge perfect matching disjoint from the other. This gives the asserted polynomials. Since \(|E(G)|=n(n-1)\), complementing \(T\) sends \(z^{|T|}\) to \(t^{n(n-1)-|T|}\) and proves the forcing-set enumerator.

**Step 4: extremal coefficients.** For \(n\ge5\), the unique largest support type is a full double-oriented star with \(2(n-1)\) arcs, and there are exactly \(n\) centers. For \(n=4\), a full double-oriented star and a fully oriented triangle both have six arcs, giving \(4+4=8\) extremizers. For \(n=3\), a largest admissible complement chooses exactly two of each of the two disjoint three-edge frames, giving \(3^2=9\) extremizers. Subtracting these complement sizes from \(n(n-1)\) yields the stated scalar values and counts.

## Verification

The standalone standard-library script `verify.py` reconstructs all perfect matchings as derangements and tests **ordered pairs of distinct perfect matchings**. A complement \(T\) is rejected whenever it contains \(P\setminus Q\) for such an ordered pair: this is exactly the direct definition that \(E(G)\setminus T\) fails to force \(P\). Thus these exhaustive checks do not assume the nice-cycle or star/triangle classification. They test all \(2^6\), \(2^{12}\), and \(2^{20}\) complements for \(n=3,4,5\), respectively, producing \(49\), \(343\), and \(1366\) admissible complements with full coefficient agreement. Separate direct enumeration of the proposed star/triangle support families agrees with the formulas for \(n=4,5,6,7\), yielding respective totals \(343,1366,6334,29023\). The captured output `verification_output.txt` ends `VERIFY_OK`. Run `python3 verify.py` from the extracted directory.

## Relationship to prior work

He and Zhang (2022, first public) establish general complete-forcing bounds and constructions within graph-theoretic edge-subset methods; He and Zhang (2023) determine minimum complete forcing *numbers* for complete and almost-complete multipartite graph classes including dense balanced bipartite graphs. That earlier numerical optimization already encompasses the scalar minimum in this family; the claimed refinement here is the if-and-only-if classification of **every** complete forcing subset of every size, together with its closed counting polynomial and minimum-set multiplicities. The publisher-accessible material reviewed for He and Zhang consists of an abstract and the first publisher-preview page, not their complete paper. This limits the historical comparison: an uninspected result in the full paper might overlap part of the classification. Ebrahimi, Nemayande and Tohidi (2024), whose arXiv HTML text was inspected, establish general upper and lower bounds and the nice-cycle criterion used here, not a crown-graph forcing-set enumerator.

## Limitations

The theorem is for the labeled crown family \(\operatorname{Cr}_n\) with \(n\ge3\), not for arbitrary balanced bipartite graphs. The enumerator counts distinct *edge subsets*, without quotienting by graph automorphisms. No independence audit is claimed. The exhaustive tests concern finite orders only; the infinite-family claim rests on Steps 1–4. Access to the complete He–Zhang 2023 primary text was restricted, so equivalence to unpublished or uninspected earlier classifications cannot be eliminated by the present literature comparison.

## References

1. X. He and H. Zhang, “Complete forcing numbers of graphs,” *Ars Mathematica Contemporanea* **23** (2023 issue), article P2.09, first publicly released 2022-12-13. DOI: `10.26493/1855-3974.2706.3c8`.
2. X. He and H. Zhang, “Complete forcing numbers of complete and almost-complete multipartite graphs,” *Journal of Combinatorial Optimization* **46** (2023), article 11, published online 2023-08-24. DOI: `10.1007/s10878-023-01078-7`.
3. J. B. Ebrahimi, A. Nemayande and E. Tohidi, “Bounds on the Complete Forcing Number of Graphs,” arXiv:2409.17306v1 (2024-09-25); see Section 2, Proposition 1, and Sections 1 and 3.
4. S.-J. Xu, H. Zhang and J. Cai, “Complete forcing numbers of catacondensed hexagonal systems,” *Journal of Combinatorial Optimization* **29** (2015), 803–814, source of the standard nice-cycle criterion as quoted in reference 3.
