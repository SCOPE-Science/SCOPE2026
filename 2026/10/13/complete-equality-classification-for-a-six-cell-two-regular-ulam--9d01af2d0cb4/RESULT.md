# Complete equality classification for a six-cell two-regular Ulam multipermutation code
## Finding
Use the multipermutation convention of Farnoud and Milenkovic: a codeword assigns each of six labeled cells one of three ranks, with exactly two cells at each rank. Two codewords have \(2\)-regular Ulam distance equal to the minimum ordinary Ulam distance between permutations in their two rank-equivalence classes.

For this space,
\[
A_{\circ}(6,2,3)=5.
\]
Exactly \(72\) labeled five-codeword maxima exist. Every maximum is equidistant: each of its ten unordered pairs has \(2\)-regular Ulam distance \(3\).

If the ordering of the three rank classes in a codeword is forgotten, that codeword becomes a perfect matching of the six cell labels. For every maximum code, its five underlying perfect matchings are exactly the five one-factors in a \(1\)-factorization of \(K_6\). Conversely, the complete census consists of exactly \(12\) valid rank-orderings over each of the \(6\) labeled one-factorizations of \(K_6\).

Under common relabeling of the six cell labels by \(S_6\), the \(72\) maxima form one orbit. Since \(|S_6|=720\), every maximum has stabilizer order \(10\).

One representative, written as rank assignments to cells \(1,\ldots,6\), is
\[
\{112233,\ 132312,\ 232131,\ 312321,\ 322113\}.
\]

## Assumptions and scope
The ambient set consists of all
\[
\frac{6!}{(2!)^3}=90
\]
rank assignments with two cells in each of three ordered rank classes.

For a rank assignment \(m\), let \(R_2(m)\) be the eight ordinary permutations obtained by ordering the two cells arbitrarily inside each of the three consecutive rank blocks. For two rank assignments \(m,n\), the distance used here is
\[
d_{\circ}^2(m,n)=\min_{\pi\in R_2(m),\,\sigma\in R_2(n)} d_{\circ}(\pi,\sigma),
\]
where ordinary Ulam distance is six minus the longest-common-subsequence length. This is the 2013 Farnoud--Milenkovic convention based on cell-rank ordered set partitions.

A code has minimum distance at least \(3\) when the displayed distance is at least \(3\) for every pair of distinct codewords. No linearity assumption is made.

## Proof
The supplied verifier regenerates all \(90\) rank assignments from the multiset with multiplicities \((2,2,2)\). For every assignment it regenerates all \(8\) representative permutations.

For every unordered pair of ambient codewords, it computes the minimum representative-to-representative ordinary Ulam distance twice. The first implementation computes ordinary Ulam distance by dynamic-programming longest common subsequence. The second computes it through the longest increasing subsequence of the relative-position sequence of two permutations. The resulting \(90\times90\) distance matrices agree exactly. Their pair-distance distribution is
\[
1080,\ 1440,\ 1440,\ 45
\]
at distances \(1,2,3,4\), respectively.

Form the compatibility graph on the \(90\) rank assignments, joining two vertices when their \(2\)-regular Ulam distance is at least \(3\). An exact Bron--Kerbosch traversal enumerates the complete maximal-clique search tree and finds maximum clique size \(5\), with exactly \(72\) maximum cliques. A separate fixed-size backtracking search independently finds a five-clique and proves that no six-clique exists. A third nested adjacency-intersection census independently regenerates exactly the same set of \(72\) five-cliques.

Direct recomputation of all internal pair distances shows that every one of the \(72\) maximum codes has distance spectrum consisting of ten copies of \(3\).

For the structural statement, replace each rank assignment by the unordered set of its three two-cell rank classes. The verifier checks for every maximum that the resulting five perfect matchings are distinct and partition all \(15\) edges of \(K_6\). It also independently enumerates all perfect matchings of \(K_6\), then all one-factorizations, obtaining exactly \(6\). Each factorization supports exactly \(12\) members of the exhaustive maximum-code census.

Finally, all \(720\) common relabelings of the six cell labels are applied to a representative maximum. The orbit is exactly the full \(72\)-code maximum set, so orbit--stabilizer gives stabilizer order \(10\).

## Verification
Run `python3 verify.py` in the package directory. The script uses only the Python standard library and reconstructs every finite object from definitions.

The replayed terminal line is:

`VERIFY_OK maximum=5 labeled_maxima=72 equidistant=true factorizations=6 optima_per_factorization=12 S6_orbits=1 orbit_size=72 stabilizer=10`

The proof is exhaustive only for the stated \(90\)-point finite space. No extrapolation to larger blocklengths is used.

## Relationship to prior work
Farnoud and Milenkovic introduced the relevant \(r\)-regular multipermutation Ulam-code model for nonvolatile memories, defined the set-distance over representative permutations, and denoted the extremal quantity by \(A_{\circ}(n,r,d)\). Their general upper bound
\[
A_{\circ}(n,r,d)\le S(n-d+1,n/r,r)
\]
specializes here to the non-sharp value \(S(4,3,2)=54\). Their construction sections include a semi-Latin-square example at \(n=6,r=2\), but the displayed small construction is for distance \(2\), while the almost-disjoint-set construction for correcting one translocation requires \(2t<r\) and therefore does not cover \(r=2,t=1\).

Kong and Hagiwara later studied sphere sizes and code-size bounds for multipermutation Ulam codes. Their paper explicitly focuses on sphere analysis and resulting bounds; it does not state the finite value \(A_{\circ}(6,2,3)=5\), the \(72\)-code equality census, or the one-factorization classification. Their multipermutation correspondence convention also differs from the 2013 ordered-set-partition convention used in this finding.

Targeted exact-parameter searches using the aliases “multipermutation Ulam code,” “ordered set partition Ulam code,” and the parameter triple \((6,2,3)\) did not locate a published equality census or an implication-equivalent finite classification.

## Limitations
This is a finite exact result for the 2013 cell-rank convention, six labeled cells, rank multiplicity two, three ordered ranks, and minimum \(2\)-regular Ulam distance \(3\). It does not classify the alternative multipermutation correspondence convention used in later sphere-analysis work, other blocklengths, other multiplicities, or larger minimum distances.

A negative literature search cannot prove absolute novelty. The residual originality risk is an obscure or unindexed finite computation of this same \(90\)-point metric space. The inspected primary and directly related full texts do not contain the claimed equality census.

## References
1. Farzad Farnoud (Hassanzadeh) and Olgica Milenkovic, “Multipermutation Codes in the Ulam Metric for Nonvolatile Memories,” arXiv:1312.2163v1, first public 2013-12-08; later IEEE Journal on Selected Areas in Communications, DOI 10.1109/JSAC.2014.140512.
2. Justin Kong and Manabu Hagiwara, “Multipermutation Ulam Sphere Analysis Toward Characterizing Maximal Code Size,” arXiv:1701.03896v1, 2017.
