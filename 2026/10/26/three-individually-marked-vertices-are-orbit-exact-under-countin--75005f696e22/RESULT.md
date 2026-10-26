# Three individually marked vertices are orbit-exact under counting refinement in nonternary Hamming graphs

## Finding

**Theorem.** Let \(q\ge4\), \(d\ge3\), and let \(a,b,c\) be any three distinct words in \([q]^d\). In the undirected Hamming graph \(H(d,q)=K_q^{\square d}\), give \(a,b,c\) three distinct initial colors and every other vertex one common initial color. Synchronous one-dimensional counting color refinement reaches **exactly** the orbit partition of the pointwise stabilizer of \(a,b,c\), in at most \(d\) strict refinement rounds.

For each coordinate \(i\), let \(\pi_i\) be the partition of \(\{1,2,3\}\) in which labels are together precisely when their marked words have equal symbols at coordinate \(i\). For each of the five possible set partitions \(\pi\) let \(n_\pi=|\{i:\pi_i=\pi\}|\). The exact number of stable colors is
\[
 N(a,b,c;q,d)=\prod_{\pi\vdash\{1,2,3\}}\binom{n_\pi+|\pi|}{|\pi|}.
\]
This formula is independent of \(q\) once \(q\ge4\), but the sizes of its color classes depend on \(q\).

More explicitly, for a test word \(x\), define \(c_{\pi,S}(x)\) as the number of coordinates of marker partition \(\pi\) at which \(x\) agrees with the common marked symbol of the block \(S\in\pi\). Let \(c_{\pi,\varnothing}(x)\) count coordinates at which \(x\) agrees with none of the three markers. The stable color of \(x\) is determined exactly by the whole vector of these nonnegative counts. The size of its color class equals
\[
 \prod_{\pi\vdash\{1,2,3\}}
 \left(\frac{n_\pi!}{\prod_{S\in\pi\cup\{\varnothing\}}c_{\pi,S}(x)!}
 (q-|\pi|)^{c_{\pi,\varnothing}(x)}\right).
\]
Every vector satisfying \(\sum_{S\in\pi\cup\{\varnothing\}}c_{\pi,S}=n_\pi\) is realized. These are labeled-graph color classes, not classes of triples of markings modulo ambient automorphism.

## Assumptions and scope

The alphabet is an arbitrary set of \(q\) symbols, not necessarily a field. A Hamming edge changes exactly one coordinate to a different symbol. The three marks are distinct and individually colored, not given a common marker color. All five partition types may occur, with zero counts permitted. Refinement at round \(t+1\) records the round-\(t\) color and the full multiset of colors of adjacent vertices. The final partition is independent of color names. A **strict round** splits at least one class; a terminal unchanged recoloring is not counted. The theorem does not claim a sharp depth for every triple, nor any statement for four or more marked vertices.

## Proof

**1. Automorphism orbits.** For \(q\ge3\), the maximal cliques of size at least three in \(H(d,q)\) are precisely its coordinate lines. Label an edge by the coordinate in which its endpoints differ. Edges with the same label are connected, through the graph, by chains of relations consisting of belonging to a common triangle and being opposite edges in an induced four-cycle; neither relation changes the coordinate label. Thus every automorphism globally permutes these \(d\) intrinsic edge directions. After undoing that permutation, the image of output coordinate \(i\) depends only on input coordinate \(i\), because all other coordinate changes leave it unchanged. Therefore every automorphism is a permutation of the coordinates followed by a separate permutation of the \(q\) symbols in each coordinate. Conversely, every such transformation is an automorphism.

Fixing the three marked words forces a coordinate permutation to preserve each marker equality partition \(\pi_i\). A symbol permutation in a coordinate can map the chosen symbol \(x_i\) to another one while fixing the marked symbols precisely when both choices have the same status: agreement with the same marker block \(S\), or agreement with none (\(\varnothing\)). Therefore \(x,y\) lie in the same pointwise-stabilizer orbit if and only if their count vectors \(c_{\pi,S}\) agree. For each \(\pi\), one distributes \(n_\pi\) positions among \(|\pi|+1\) statuses. Because \(q\ge4>|\pi|\), every status is available. Stars and bars gives \(\binom{n_\pi+|\pi|}{|\pi|}\), independently for the five \(\pi\)'s. Choose coordinate statuses by a multinomial count, and for each empty status choose any of \(q-|\pi|\) unused symbols; this proves the class-size formula.

**2. Distance vectors arise within \(d-1\) rounds.** Put \(D(x)=(\operatorname{dist}(x,a),\operatorname{dist}(x,b),\operatorname{dist}(x,c))\). Initially, each marked word is a singleton color, so each initial color determines \(\min(\operatorname{dist}(x,a_j),1)\) for each marker \(a_j\). Inductively, if the round-\(t\) color determines the truncated distance \(\min(\operatorname{dist}(x,a_j),t+1)\), the next color determines whether \(x\) has a neighbor at distance \(t+1\) from \(a_j\): that holds for distance exactly \(t+2\) and not for larger distance, once the previous truncation is known. More explicitly, the previously identifiable distance-\((t+1)\) color union has positive neighbor count precisely for vertices at distance \(t+2\) among those previously known to be at distance at least \(t+2\). Hence round \(t+1\) determines all three distances truncated at \(t+2\). As the Hamming diameter is \(d\), the full \(D(x)\) is determined by the color after round \(d-1\).

**3. One further round reconstructs every orbit status count.** Write \(e_S\in\{0,1\}^3\) for the indicator of a set of marker labels \(S\), with \(e_{\varnothing}=0\). When a neighbor is obtained by changing one coordinate from status \(S\) to a different status \(T\) at that coordinate, its distance-vector displacement is exactly \(e_S-e_T\). Consequently, knowing the round-\((d-1)\) distance vectors of all neighbors lets round \(d\) determine every count \(W_\delta(x)\) of neighbors whose distance vector differs by \(\delta\).

Consider a two-block partition \(\pi=\{S,T\}\) of \(\{1,2,3\}\). The displacement \(e_S-e_T\) (with supports of sizes one and two) can only arise at coordinates of this very partition, when \(x\) is in status \(S\) and its symbol changes to the unique symbol for block \(T\). Therefore \(c_{\pi,S}=W_{e_S-e_T}\) and \(c_{\pi,T}=W_{e_T-e_S}\). The remaining status count is \(c_{\pi,\varnothing}=n_\pi-c_{\pi,S}-c_{\pi,T}\).

For the discrete three-block partition \(\pi=\{\{1\},\{2\},\{3\}\}\), the displacement \(e_{\{i\}}-e_{\{j\}}\), for distinct \(i,j\), can arise only at a coordinate of this discrete partition with initial status \(\{i\}\) and new status \(\{j\}\). Thus \(c_{\pi,\{i\}}=W_{e_{\{i\}}-e_{\{j\}}}\); the empty-status count is \(n_\pi\) minus the three recovered counts. The uniqueness assertions follow because any other marker partition necessarily changes an additional marker distance or cannot realize both required nonempty singleton blocks.

It remains to determine the one-block partition \(\pi_0=\{\{1,2,3\}\}\). All the counts for partitions with two or three blocks have already been recovered. The distance from \(x\) to \(a\), for instance, equals the sum over every partition and status not containing marker label \(1\). Subtract the known contributions from the two- and three-block partitions to recover \(c_{\pi_0,\varnothing}\); then \(c_{\pi_0,\{1,2,3\}}=n_{\pi_0}-c_{\pi_0,\varnothing}\). Hence the round-\(d\) color determines the complete orbit profile.

Every automorphism fixing all three marker colors preserves every round of counting refinement. Its orbit partition is therefore always at least as fine as the refinement partition. The preceding reconstruction gives the reverse inclusion at round \(d\). Equality follows, and this orbit partition is equitable, so no further strict round is possible.

## Verification

The standalone file `check_three_anchor.py` enumerates graph vertices and actual Hamming neighbours, directly iterates synchronous refinement, independently constructs orbit profiles from coordinate marker partitions, and verifies a separate inversion of the distance-displacement measurements. Its output `check_log.txt` records 3,240 completed cases: every ordered-as-set triple of distinct marks on \(H(2,4)\) and \(H(2,5)\), plus deterministic sampled triples in dimensions three through five and alphabet sizes four through six. The dimension-two checks test the boundary of the proof although the theorem is stated for \(d\ge3\). All tested stable color classes equal full orbit-profile classes, class-count and individual class-size formulas match, and strict rounds never exceed \(d\). One four-symbol, dimension-three triple requires three strict rounds, showing the uniform upper bound need not improve even in the smallest in-scope dimension.

Reproduce with `python3 check_three_anchor.py` (Python standard library only). Finite tests are corroboration, not the proof for arbitrarily large \(q,d\).

## Relationship to prior work

Kersting, Mladenov, Garnett and Grohe (2014) describe and analyze general color refinement and its coarsest-equitable-partition interpretation, without a specific three-marked Hamming orbit theorem. Brouwer's account gives the Hamming graph's underlying distance-regular structure. Bhattacharjee, Panse and Sarma (2026), Theorem 1.1, give an abstract equivalence between refinement of individualized graphs and pointwise-stabilizer orbit partitions but no concrete Hamming classification in their accessible full text.

A related ternary-alphabet statement establishes arbitrary-marker orbit exactness for \(H(d,3)\), not for \(q\ge4\). The present case has an additional "unmarked symbol" coordinate status even when all three marker symbols differ; it is neither a parameter specialization nor a logical corollary of that ternary statement. A related arbitrary-marking statement for rook graphs treats \(H(2,q)\); this theorem explicitly restricts to \(d\ge3\). General literature on equitable partitions and perfect colorings is related but not known to imply the stated canonical partition, exact orbit count, and \(d\)-round bound. No priority claim beyond the examined sources is implied.

## Limitations

The result assumes an alphabet of size at least four and exactly three **distinct, individually colored** marker vertices. It does not classify refinement from a single shared marker color, four or more markers, or unrelated distance-regular graphs. The upper depth bound is not asserted to be optimal for every parameter or triple. Only same-author mathematical checking and finite computational replay are supplied; independently performed mathematical validation and comprehensive publication-priority certification remain outstanding. Related Hamming perfect-coloring papers were examined through available arXiv primary texts; no exhaustive priority certification is claimed.

## References

- K. Kersting, M. Mladenov, R. Garnett, M. Grohe, *Power Iterated Color Refinement*, AAAI 2014, DOI: 10.1609/aaai.v28i1.8992, first published 2014-06-21; https://ojs.aaai.org/index.php/AAAI/article/view/8992/8851.
- A. E. Brouwer, *Hamming graphs*, https://aeb.win.tue.nl/drg/graphs/Hamming.html (online reference, publication date not asserted).
- S. Bhattacharjee, A. Panse, J. Sarma, *A Hierarchy of Tinhofer Graphs: Separations and Membership Testing*, arXiv:2605.19702v1, 2026-05-19; https://arxiv.org/html/2605.19702.
- A. Vasil'eva, *Local distributions for eigenfunctions and for perfect colorings of q-ary hypercube*, arXiv:1412.7357v1 (2014-12-23), later Designs, Codes and Cryptography 87 (2019), 509–516, DOI: 10.1007/s10623-018-0559-1.
- E. Bespalov, D. S. Krotov, A. A. Matiushev, A. A. Taranenko, K. V. Vorob'ev, *Perfect 2-colorings of Hamming graphs*, arXiv:1911.13151 (2019-11-29), Journal of Combinatorial Designs 29 (2021), 367–396.
