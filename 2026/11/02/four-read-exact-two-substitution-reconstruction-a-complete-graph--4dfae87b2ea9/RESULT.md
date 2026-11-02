# Four-read exact-two-substitution reconstruction: a complete graph classification

## Finding

Let \(n\geq5\), let \(u\in\{0,1\}^{n}\), and let \(Y=\{y_1,y_2,y_3,y_4\}\) consist of four **distinct** binary words satisfying \(d_H(u,y_i)=2\). Form the simple graph \(G_Y\) on coordinate positions \([n]\): its four edges are the two-element error supports \(\operatorname{supp}(u\oplus y_i)\). Vertices unused by every edge are isolated.

The set of exact-two-substitution candidate sources
\[
U(Y)=\{v\in\{0,1\}^{n}:d_H(v,y_i)=2\text{ for all }i=1,2,3,4\}
\]
is the singleton \(\{u\}\) **if and only if** the nonisolated portion of \(G_Y\) is one of these graph types:

1. One triangle and one disjoint edge, \(K_3\sqcup K_2\), on five vertices.
2. One four-vertex path and one disjoint edge, \(P_4\sqcup K_2\), on six vertices.
3. One three-vertex path and two disjoint edges, \(P_3\sqcup2K_2\), on seven vertices.
4. Four pairwise disjoint edges, \(4K_2\), on eight vertices.
5. **Only when \(n=5\)**, one star with four leaves, \(K_{1,4}\).

Consequently the exact number of unordered four-read sets producing unique reconstruction of **a fixed** \(u\) is
\[
A_n=10\binom n5+180\binom n6+315\binom n7+105\binom n8+5\mathbf 1_{\{n=5\}},\qquad n\ge5.
\]
Here \(\binom nk=0\) for \(k>n\). The values at \(n=5,6,7,8,9\) are respectively \(15,240,1785,8225,28665\). Because a uniquely reconstructible read set determines its source, the total number of such sets over all binary sources is \(2^n A_n\).

Precisely \(10\binom n5+5\mathbf 1_{\{n=5\}}\) of these sets are **genuinely four-read**: no subset of three reads already determines \(u\). The irreducible configurations are \(K_3\sqcup K_2\) and the exceptional length-five star. For example, at length five the error supports \(\{\{1,2\},\{1,3\},\{1,4\},\{1,5\}\}\) determine the all-zero source uniquely, although coordinatewise majority returns the incorrect word with a one in position 1.

## Assumptions and scope

The channel is binary and each received word differs from its source in **exactly two** coordinates, not at most two. The four received words are distinct and unordered. No codebook restriction or stochastic distribution is assumed. An unknown candidate source must satisfy all four exact-distance equations. The source length is an arbitrary integer \(n\ge5\), and coordinate labels are retained in the enumeration. Equivalence under vertex permutation is used only to classify graph types.

## Proof

**1. Translate ambiguity into a two-vertex cut or four-vertex cover.** By bitwise translation take \(u=0^n\). Each read \(y_i\) has support equal to an edge \(e_i\) of the graph. Write \(D=\operatorname{supp}(v)\) for a proposed competing source. Because
\[
d_H(v,y_i)=|D|+2-2|D\cap e_i|,
\]
the four constraints \(d_H(v,y_i)=2\) are equivalent to
\[
|D\cap e_i|=|D|/2\quad\text{for every edge }e_i.
\]
For nonempty \(D\) the common value is a positive integer at most two, so \(|D|=2\) or \(|D|=4\). If \(|D|=2\), every edge joins a vertex of \(D\) to one of its complement (an *exact two-vertex transversal*). If \(|D|=4\), every edge is wholly contained in \(D\), which is possible precisely when the number of incident vertices is at most four: since \(n\ge5\), the incident set can always be extended to four vertices. Hence uniqueness holds precisely when the graph has at least five incident vertices and admits no exact two-vertex transversal.

**2. Classify four-edge graphs meeting the criterion.** Discard isolated vertices temporarily. Every nontrivial connected component contains an edge. If a component has an odd cycle, four edges and at least five incident vertices force the unique possibility \(K_3\sqcup K_2\). It has no exact transversal because the triangle is not bipartite. Otherwise the graph is a forest: since its edge count is four, a forest with \(c\) nontrivial components has \(4+c\) incident vertices. A set meeting every edge in exactly one endpoint is a choice of one color class from each component's bipartition, possibly together with isolated vertices. Its minimum size on the incident vertices is the sum of the smaller bipartition-class sizes.

For \(c=1\), the three trees on five vertices are \(P_5\), the degree-sequence \((3,2,1,1,1)\) tree, and \(K_{1,4}\). Their smaller color-class sizes are respectively two, two, and one. The first two admit an exact two-vertex transversal. The star admits one exactly when an isolated vertex is available; therefore it survives only at \(n=5\). For \(c=2\), the component edge counts are \((3,1)\) or \((2,2)\). The corresponding forests are \(P_4\sqcup K_2\), \(K_{1,3}\sqcup K_2\), and \(P_3\sqcup P_3\), whose minimum color-class sums are three, two, and two. Only the first survives. For \(c=3\) the sole forest is \(P_3\sqcup2K_2\), whose minimum color-class sum is three. For \(c=4\) it is \(4K_2\), with minimum sum four. These are exactly the claimed graph types.

**3. Count labeled read sets.** An edge set specifies four distinct reads around fixed \(u\). For \(K_3\sqcup K_2\), choose five vertices and then the three triangle vertices: \(10\binom n5\) possibilities. For \(P_4\sqcup K_2\), choose six vertices, choose the two on the isolated edge, then order the other four along a path modulo reversal: \(\binom n6\binom62(4!/2)=180\binom n6\). For \(P_3\sqcup2K_2\), choose seven vertices, the middle of the path, its two endpoints, and one of the three pairings of the remaining four vertices: \(\binom n7\cdot7\binom62\cdot3=315\binom n7\). For \(4K_2\), choose eight vertices and then one of the \(8!/(2^4 4!)=105\) perfect matchings, giving \(105\binom n8\). When \(n=5\) the extra star has five possible centers. These five disjoint classes prove the displayed formula.

**4. Distinguish genuinely four-read cases.** Any three pairwise disjoint two-element supports already determine the source uniquely: a competing nonempty \(D\) would need to intersect all three supports in \(|D|/2\) coordinates, impossible since the supports are disjoint. Each of the three surviving forest types other than the five-star contains three pairwise disjoint edges, while neither the triangle-plus-edge graph nor the five-star does. Conversely, no three-read set in the latter two types uniquely reconstructs its source: every triple from the triangle-plus-edge graph has a two-edge component admitting a two-vertex exact transversal or has at most four incident vertices, and every triple from the star has at most four incident vertices (so a four-vertex competing source exists). Thus exactly the first and last types are genuinely four-read. For the length-five star example, each of its reads has a 1 at the star center; majority decodes that position as 1, whereas the unique source is 0 there.

## Verification

Run the two standalone Python 3 standard-library scripts `verify_spheres.py` and `verify_graphs.py`. The first evaluates all intersections of four exact-radius-two spheres around fixed-zero error words by exact integer bitsets, and counts singleton intersections independently of graph structure. The second enumerates four-edge graphs, applies the cut/incident-vertex criterion, and independently groups surviving configurations by the size of their incident vertex set. Both perform exhaustive checks for each \(n\in\{5,6,7,8,9\}\) and reproduce the formula. The recorded terminal outputs are embedded in `verification_spheres.txt` and `verification_graphs.txt`. These finite checks support, but do not replace, the all-length combinatorial proof above.

## Relationship to prior work

Papadopoulou, Yehezkeally, Rameshwar, and Wachter-Zeh (2026, first public October 21) determine the **worst-case number** of distinct reads guaranteeing reconstruction under exact-weight substitutions and analyze decoding algorithms. Their threshold does not count or classify the uniquely reconstructible four-read configurations below it. Wang, Yaakobi, and Zhang (2026) characterize three-read uniqueness for the *at-most*-radius model (Theorem 10) and explicitly identify four-read characterization as a further problem; its disjoint-triple case also applies here. The three forest types with a three-edge matching are thereby already covered as sufficient conditions, while the triangle-plus-edge and length-five star classes are not covered. Junnila, Laihonen, Lehtilä, and Pavan (2026) give a general algorithmic formula for intersections of Hamming **balls** with arbitrary numbers of centers. Specializing that framework to exact spheres would require additional inclusion–exclusion and graph classification; it does not state the all-length four-read enumeration or the irreducible motifs. The present result is a closed structural enumeration for exact-radius-two *spheres*, not a general replacement for the earlier formulas.

## Limitations

The classification assumes four **distinct**, length-\(n\), binary observations, each at Hamming distance **exactly two** from the source, and \(n\ge5\). It does not classify the at-most-two model, nonbinary alphabets, more than four reads, other radii, or noisy reads with unequal corruption budgets. The method uses a four-edge graph and does not automatically extend to larger error weights. Priority over unknown equivalent graph-incidence formulations is not independently certified.

## References

- V. Papadopoulou, Y. Yehezkeally, V. A. Rameshwar, and A. Wachter-Zeh, *When Majority-Vote Fails: Sequence Reconstruction under Fixed-Weight Substitutions*, arXiv:2610.30001v1, first public 2026-10-21, https://arxiv.org/abs/2610.30001.
- C. Wang, E. Yaakobi, and Y. Zhang, *Sequence Reconstruction for Substitution Channel: New Sufficient Conditions and Algorithms*, IEEE Transactions on Information Theory 72 (2026), 2978–2992; https://arxiv.org/abs/2606.05454. See Theorem 10 and Section V.
- V. Junnila, T. Laihonen, T. Lehtilä, and P. P. Devaraj, *The Size of the Intersection of q-ary Hamming Balls*, arXiv:2606.09158v2, https://arxiv.org/abs/2606.09158.
- V. I. Levenshtein, *Efficient reconstruction of sequences*, IEEE Transactions on Information Theory 47 (2001), 2–22, DOI:10.1109/18.904499.
