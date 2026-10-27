# Sharp \(d-1\)-round two-marker refinement in nonbinary Hamming graphs

## Finding
Let \(d\ge1\), \(q\ge3\), and let \(H(d,q)\) be the simple graph on \([q]^d\), joining two words exactly when they differ in one coordinate. Choose two distinct vertices \(A,B\) with Hamming distance \(t\), where \(1\le t\le d\), and initially assign different singleton colors to \(A\) and \(B\), leaving every other vertex in one common color. At each synchronous color-refinement round, the new color is the old color paired with the multiset of neighbor colors. Initial coloring has index \(0\).

**Theorem.** The least stable round is exactly \(d-1\), independently of \(q\) and \(t\). The stable partition equals the pointwise-stabilizer orbit partition. In particular, it has exactly
\[
\binom{t+2}{2}(d-t+1)
\]
classes. The result includes \(d=1\), when the initial partition is already stable. The nonbinary hypothesis is sharp for the dimension-only round law: on \(H(3,2)\) with antipodal marks, the stable round is \(1\), not \(2\).

For a vertex \(x\), let \(I=\{i:A_i\ne B_i\}\), \(J=[d]\setminus I\), and define
\[
 a=|\{i\in I:x_i=A_i\}|,\quad b=|\{i\in I:x_i=B_i\}|,\quad
 s=|\{i\in J:x_i\ne A_i\}|.
\]
The stable color of \(x\) is determined exactly by \((a,b,s)\), with \(a,b\ge0\), \(a+b\le t\), \(0\le s\le d-t\). Its class has size
\[
\frac{t!}{a!b!(t-a-b)!}(q-2)^{t-a-b}
\binom{d-t}{s}(q-1)^s.
\]

## Assumptions and scope
All words are distinct vertices of the undirected unweighted Hamming graph. The two marked vertices receive different colors, and all others receive the same third color. Refinement is synchronous, counts neighbors with multiplicities, and retains the old color in every update. The theorem concerns within-graph orbit recovery and strict refinement rounds, not identification among arbitrary graphs. No assumption that \(q\) is a prime power is made.

## Proof
**1. Automorphism orbits.** The graph is the Cartesian product of \(d\) copies of \(K_q\). For \(q\ge3\), the complete coordinate fibers are intrinsic maximal cliques, and the opposite-edge relation in Cartesian squares propagates each coordinate direction throughout the graph. Thus any automorphism permutes the coordinate directions and independently permutes the symbols in each coordinate; conversely every such operation is an automorphism. After fixing both \(A\) and \(B\), coordinate permutations preserve the two blocks \(I,J\). In each coordinate of \(I\), symbols other than the two marked symbols can be interchanged; in each coordinate of \(J\), symbols other than the common marked symbol can be interchanged. Hence the pointwise stabilizer is transitive exactly on the classes labeled by \((a,b,s)\) above. Choosing their coordinate positions and unmarked symbols gives the class-size formula and the stated class count. Every color-refinement class is a union of these automorphism orbits.

**2. Distance information in refinement colors.** Write \(\delta_A(x)=d_H(x,A)\) and \(\delta_B(x)=d_H(x,B)\). At round \(r\ge0\), a vertex's color determines both quantities
\[
 \min\{\delta_A(x),r+1\},\qquad
 \min\{\delta_B(x),r+1\}.
\]
For \(r=0\), the two marked vertices are individually identified. Inductively, because the old color is retained, all previously resolved distances remain resolved. A vertex first reaches exact distance \(r+1\) from a marker precisely when it has a neighbor at the already distinguished distance \(r\), whereas any vertex at distance greater than \(r+1\) has no such neighbor. The neighbor-color multiset therefore resolves the next distance shell. This proves the induction for each marker separately.

**3. The upper bound.** The distances are expressed in the three orbit parameters by
\[
 \delta_A=t-a+s,\qquad \delta_B=t-b+s.
\]
At round \(d-1\), step 2 reveals both exact distances. If either equals \(d\), then \(t-a+s=d\) or \(t-b+s=d\). As \(a,b\ge0\) and \(s\le d-t\), this forces \(s=d-t\). Otherwise both distances are at most \(d-1\). At round \(d-2\), neighbor colors already reveal exactly whether a neighbor \(y\) satisfies
\[
 \delta_A(y)=\delta_A(x)-1,\qquad
 \delta_B(y)=\delta_B(x)-1,
\]
because the two target distances lie in \(\{0,\ldots,d-2\}\), below the truncation threshold. There are precisely \(s\) such neighbors: a one-coordinate move can reduce the distances to two different marked symbols simultaneously only in a coordinate of \(J\) where \(x\) differs from their common symbol, and in each such coordinate precisely one move does so. Thus the neighbor-color multiset at round \(d-1\) reveals \(s\). Reconstruct
\[
 a=t+s-\delta_A,\qquad b=t+s-\delta_B.
\]
The round \(d-1\) colors therefore distinguish all stabilizer orbits. Because an automorphism-orbit partition is equitable, no later refinement can split it, proving stability. For \(d=1\), the initial colors already give the three possible orbit categories, and the same conclusion holds without invoking a negative-index round.

**4. The lower bound.** Assume \(d\ge2\). Since \(q\ge3\), choose a word \(x\) that differs from both marked symbols in every coordinate of \(I\) and from their common symbol in every coordinate of \(J\). Then both marker distances are \(d\). Choose \(j\in I\), and obtain \(y\) from \(x\) by setting coordinate \(j\) equal to \(A_j\). Now \(\delta_A(y)=d-1\) and \(\delta_B(y)=d\), so \(x,y\) belong to different pointwise-stabilizer orbits. Yet neither vertex is within distance \(d-2\) of a marked vertex. Every \((d-2)\)-round refinement computation around either vertex sees only the original background color: because the graph is regular, all vertices with no initially marked vertex within their radius-\(r\) neighborhoods receive the same round-\(r\) color. Consequently \(x,y\) have equal colors through round \(d-2\). They split by round \(d-1\), proving that the least stable round is exactly \(d-1\).

## Verification
Run the accompanying standalone Python 3 checker with `python verify.py`. It constructs the actual \(q^d\) vertices and independently executes synchronous color refinement for \(46\) combinations with \(q\in\{3,4,5\}\), using maximum dimensions \(6,5,4\), respectively, and all marker separations; it checks orbit equality, class sizes, and strict previous-round failure. It also executes an independently weighted orbit-quotient refinement for \(630\) configurations with \(3\le q\le8\), \(1\le d\le14\), and all \(1\le t\le d\). All checks passed. The finite checks are corroboration; steps 1–4 prove the infinite statement.

## Relationship to prior work
The Hamming graphs are Cartesian powers of complete graphs, and counting color refinement is a standard invariant of vertex-colored graphs. Kersting, Mladenov, Garnett, and Grohe (2014) analyze color refinement in an algorithmic setting, while Arvind, Köbler, Rattan, and Verbitsky (2015) study when stable colors recover automorphism orbits. Those sources do not furnish the distance-independent sharp two-marker Hamming round formula in their examined sections. The proof here exploits an additional simultaneous-distance-decrement count to sharpen the generic distance-propagation argument. Previously examined related Hamming configurations include binary marked pairs and multiple marked vertices, but their stated results do not assert the present all-nonbinary sharp two-marker round count.

## Limitations
The theorem assumes exactly two differently individualized markers; it does not address arbitrary many markers, alternate initial colors, or directed and weighted Hamming graphs. The number of rounds is counted from the given three-class initial partition. The proof does not assert that its formulation is absent from every article, appendix, or unindexed source. No independent mathematical audit is claimed.

## References
1. K. Kersting, M. Mladenov, R. Garnett, and M. Grohe, *Power Iterated Color Refinement*, AAAI 2014, DOI: `10.1609/aaai.v28i1.8992`, first published 2014-06-21. Full text: `https://ojs.aaai.org/index.php/AAAI/article/view/8992/8851`.
2. V. Arvind, J. Köbler, G. Rattan, and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (first posted 2015-02-04), `https://arxiv.org/pdf/1502.01255`.
