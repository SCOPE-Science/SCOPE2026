# Minimum maximal total-visibility sets of \(Q_7\)

## Finding

Let \(Q_7\) be the unweighted simple graph on the \(128\) binary words of length seven, adjacent when they differ in one coordinate. A set \(X\) is **total mutually visible** if every two vertices of \(Q_7\) admit a shortest path whose internal vertices avoid \(X\). Such a set is **maximal** if no strictly larger total mutually visible set contains it. Let \(\mu_t^-(Q_7)\) be the smallest cardinality of a maximal total mutually visible set.

**Theorem.**
\[
\boxed{\mu_t^-(Q_7)=8.}
\]
There are exactly
\[
\boxed{1120^2=1\,254\,400}
\]
distinct minimum-cardinality maximal total mutually visible sets of the **labeled** seven-cube. More precisely, write \(E\) and \(O\) for the even- and odd-weight binary words. An eight-vertex set \(X\) is maximal total mutually visible if and only if \(X\cap E\) and \(X\cap O\) both have four elements, and in each four-element subset the six pairwise Hamming distances comprise exactly four \(4\)'s and two \(6\)'s. The two distance-six pairs must be disjoint, forming a perfect matching on those four elements. There are exactly \(1120\) such quadruples in each parity class.

For comparison, the (maximum) total mutual-visibility number is \(\mu_t(Q_7)=16\); its maximum-value determination is not asserted to be new here. Thus the total-visibility independence complex of the seven-cube is nonpure: it possesses facets of size eight and facets of size sixteen.

## Assumptions and scope

The ground graph is exactly \(Q_7\) with vertex labels \(\{0,1\}^{7}\); counts distinguish vertex subsets, not symmetry orbits. Hamming distance is the number of differing coordinates. A shortest path may have selected endpoints but no selected **internal** vertices. Maximality refers to inclusion, not maximum cardinality. The claimed number of minimum maximal sets is not a count of all maximal sets or of the entire independence polynomial.

Let \(H\) be the halved seven-cube on the \(64\) even-weight words, where two vertices are adjacent exactly when their Hamming distance is two. The odd-weight version is isomorphic. Write \(B(c)\) for the closed neighborhood of \(c\) in \(H\), i.e. the even words of Hamming distance zero or two from \(c\).

## Proof

**1. Distance-two avoidance characterizes total visibility.** Suppose \(u,v\in X\) have Hamming distance two. Their two common neighbors \(a,b\) in \(Q_7\) are themselves at distance two, and their only common neighbors are \(u,v\). Every shortest \(a,b\)-path has one of \(u,v\) internally, hence the pair \(a,b\) is not visible through \(Q_7-X\) with endpoints allowed. Conversely, suppose \(X\) contains no pair at Hamming distance two. Fix arbitrary endpoints \(a,b\). Whenever the current word has at least two coordinates still differing from \(b\), there are at least two distinct next vertices on shortest routes to \(b\); these candidate next vertices are pairwise at Hamming distance two, so at most one lies in \(X\). Choose another candidate and continue. When only one flip remains, enter endpoint \(b\), which is allowed even if selected. This constructs a shortest path with no selected internal vertex. Thus total-visibility sets are precisely the sets avoiding distance-two pairs. This familiar Hamming-graph criterion is included for completeness, not claimed as new.

Because distance two preserves weight parity, \(X\) is total mutually visible exactly when its intersections with \(E\) and \(O\) are independent sets in the two halved cubes. Inclusion-maximality holds exactly when both sections are maximal independent, equivalently independent dominating, sets.

**2. Intersection geometry of the seven-dimensional halved cube.** Each closed neighborhood \(B(c)\) has
\[
|B(c)|=1+\binom72=22.
\]
For distinct centers in an independent set, their distance is either four or six. If the distance is four, translating one center to the zero word shows that a word in both closed neighborhoods must have weight two and be supported on two of the four differing coordinates, giving an intersection of size \(\binom42=6\). If the distance is six, the two radius-two closed neighborhoods are disjoint by the triangle inequality. If three pairwise center distances are four, their three closed neighborhoods have exactly one common word: after translating one center to zero, the other two supports are four-subsets of seven coordinates intersecting in exactly two coordinates, and the common word is that two-subset. Any triple containing a distance-six pair has empty triple intersection.

A vertex can have at most one distance-six partner inside an independent set: after translating that vertex to zero, any two words of weight six in seven coordinates differ in exactly two coordinates. Hence distance-six pairs within an independent set form a matching.

**3. Minimum independent domination number of \(H\).** Three independent centers cannot pairwise be at distance six, so at least one pair is at distance four. Their three closed neighborhoods cover at most
\[
3\cdot22-6=60<64
\]
vertices. Thus no independent set of at most three centers dominates \(H\).

For four independent centers, let \(t\) be the number of their pairs at distance four. The remaining \(6-t\) distance-six pairs form a matching; hence \(t\in\{4,5,6\}\). Inclusion-exclusion using Step 2 gives:

- If \(t=4\), two disjoint pairs have distance six. Every triple contains a distance-six pair, so the union of the four closed neighborhoods has size \(4\cdot22-4\cdot6=64\).
- If \(t=5\), one pair has distance six. Exactly two triples have all pairwise distances four, and the other triple and quadruple intersections vanish. The union has size \(4\cdot22-5\cdot6+2=60\).
- If \(t=6\), every triple has common intersection of size one. Inclusion-exclusion gives union size at most \(4\cdot22-6\cdot6+4=56\).

Therefore an independent four-set dominates \(H\) **if and only if** the distance-six pairs form a perfect matching. Such a set exists, for instance the four words, written as seven-bit strings,
\[
0000000,\quad0111111,\quad1000111,\quad1111000.
\]
The two six-distance pairs are the first with the second and the third with the fourth. Consequently \(i(H)=4\), where \(i\) denotes independent domination.

**4. Classification and enumeration.** Translate a given even center to the zero word. It has exactly one partner at distance six among the other three centers; there are seven choices for this partner, one for the position of its zero coordinate. After permuting coordinates, that partner is \(0111111\). Each of the other two centers must have distance four from both of these, and hence must contain the distinguished coordinate and exactly three of the six other coordinates. For those two centers to be at distance six from one another, their three-subsets of those six coordinates must be complementary. The unordered pair can be chosen in
\[
\frac12\binom63=10
\]
ways. Thus exactly \(7\cdot10=70\) qualifying quadruples contain a fixed even center. Double counting incidences between the \(64\) even words and qualifying four-sets yields
\[
\frac{64\cdot70}{4}=1120
\]
quadruples. The odd parity class has the same count by single-coordinate translation. Any maximal total-visibility set must contain at least four vertices of each parity. An eight-vertex one is therefore exactly a union of independently chosen qualifying quadruples, and every such union is maximal. Hence the minimum is eight and its number of achievers is \(1120^2\).

**5. Comparison with the maximum.** Every independent set in either halved cube is a binary length-seven code of minimum distance at least four. If it has \(M\) codewords, the sum of all pairwise distances is at least \(4\binom M2\), while each coordinate contributes at most \(M^2/4\) to that sum. Hence \(4\binom M2\le 7M^2/4\), implying \(M\le8\). An eight-word example is obtained by evaluating all linear functionals on the seven nonzero points of \(\mathbb F_2^3\); its nonzero words have weight four and every pair is at distance four. Taking this code in the even class and a one-coordinate translate in the odd class yields sixteen total mutually visible vertices. Thus \(\mu_t(Q_7)=16\). This standard coding-theoretic comparison only witnesses nonpurity and is not the asserted original contribution.

## Verification

The standalone standard-library script `verify_q7.py` exhaustively enumerates independent triples and quadruples of the 64-vertex halved cube, computes closed-neighborhood coverage directly, checks the distance-pattern classification, and counts quadruples containing the zero word. It independently recomputes shortest-path visibility by breadth-first search in the underlying 128-vertex cube for an eight-vertex minimum maximal example and a sixteen-vertex maximum example. No finite test is used as a substitute for the exact counting proof above.

Run `python3 verify_q7.py`. The included `verification_output.txt` is the actual recorded successful result.

## Relationship to prior work

Brešar and Yero introduced lower total mutual-visibility numbers and explicitly posed determination of these numbers for hypercubes as an open problem (arXiv:2307.02951, Problem 1). Bujtás, Klavžar, and Tian proved the distance-two avoidance criterion for total mutual visibility in Hamming graphs (arXiv:2307.05168, Theorem 6); that known criterion is the first step, not an originality claim. The OEIS table A355226 (first posted in 2022) enumerates **all** independent sets of each size in halved cubes, including 36,400 independent four-sets for dimension seven, but it does not distinguish the 1,120 inclusion-maximal four-sets or state their distance-six matching classification. The later article *Visibility in Hypercubes* (DOI:10.1007/s00373-026-03025-9) provides bounds on maximum total-visibility numbers, not this lower invariant. Comparisons of these statements do not yield the exact minimum-maximal classification or the number of its achievers.

## Limitations

The exact minimum-maximal classification concerns dimension seven only. It does not give the lower total-visibility number in arbitrary dimension, nor does it classify maximal sets larger than eight. The count is for labeled seven-bit vertices; no quotient by automorphisms is taken. Although published accessible sources and indexed research claims were compared, an unindexed or differently phrased prior classification of distance-four partial binary codes could affect priority. Independent scientific validation has not been performed.

## References

1. B. Brešar and I. G. Yero, *Lower (total) mutual visibility in graphs*, first posted 6 July 2023, arXiv:2307.02951; published in *Applied Mathematics and Computation* 465 (2024), 128411. Problem 1.
2. C. Bujtás, S. Klavžar and J. Tian, *Total mutual-visibility in Hamming graphs*, first posted 11 July 2023, arXiv:2307.05168. Theorem 6.
3. C. Flippen, *Number of independent sets of size k in the n-halved cube graph*, OEIS A355226, initial posting 24 June 2022, https://oeis.org/A355226.
4. *Visibility in Hypercubes*, *Graphs and Combinatorics* (2026), DOI:10.1007/s00373-026-03025-9, Theorem 1.7 and Section 4.
