# Extremal contranominal scales of open Hamming adjacency contexts

## Finding

**Theorem (sharp dimension, extremal rigidity, and the four-symbol transition).** Let \(q\ge2\), \(d\ge1\), and \(W=[q]^d\). Consider the formal context with distinct object and attribute copies of \(W\) and incidence \(xIy\) exactly when the Hamming distance \(\operatorname{dist}_H(x,y)=1\). A contranominal scale of dimension \(k\) is an induced subcontext on pairwise distinct \(x_1,\ldots,x_k\) and pairwise distinct \(y_1,\ldots,y_k\) satisfying \(x_iIy_j\) if and only if \(i\ne j\).

The maximum dimension is
\[
 b(q,d)=\begin{cases}q,&1\le d\le2,\\ \max\{q,4\},&d\ge3.\end{cases}
\]
Whenever \(q\ge5\), **every** maximum-dimensional scale consists of all \(q\) vertices of one coordinate line as both objects and attributes, matched identically. Its number of distinct maximal-dimensional subcontexts is exactly
\[
 C(q,d)=d q^{d-1}\qquad(q\ge5,\ d\ge1).
\]
When \(q=4\), every maximum-dimensional scale has dimension four, and the object sets form precisely three disjoint families: a full four-point coordinate line; two parallel coordinate-line pairs, using two coordinates and four different symbols along the pair direction; or one parity class of a binary three-dimensional coordinate face. Every such object set has a **unique** associated attribute set and matching. Hence
\[
 C(4,d)=d4^{d-1}+36d(d-1)4^{d-2}+432\binom d3 4^{d-3},
\]
with terms requiring more than \(d\) coordinates understood as zero. When \(q\in\{2,3\}\) and \(d\ge3\), every maximum scale is a parity-tetrahedron type, with unique attributes, and
\[
 C(q,d)=2\binom d3 q^{d-3}\binom q2^{3}.
\]
For the low-dimensional boundaries \((q,d)=(2,2)\) and \((3,2)\), the maximum dimensions are two and three respectively; no enumeration of these smaller maximum scales is asserted.

The family provides an exact separation between two natural complexity measures: the open-neighborhood VC dimension of Hamming graphs is at most three (a prior theorem), whereas the Boolean-suborder dimension of the corresponding concept lattices grows without bound with \(q\). The latter dimension is determined here by \(b(q,d)\).

## Assumptions and scope

A coordinate line fixes all but one coordinate and permits that remaining coordinate to take all \(q\) symbols. A binary three-dimensional coordinate face fixes \(d-3\) coordinates and restricts each of the remaining three to two symbols; its two parity classes each have four words. A two-parallel-pairs configuration uses two distinguished coordinates: in the first, each of the four symbols occurs exactly once, partitioned into two pairs; in the second, one symbol is shared by the first pair, a different symbol by the second pair. All other coordinates are fixed. Two scales are counted once when their selected object and attribute sets coincide, regardless of orderings; uniqueness of pairing is proved for the enumerated cases.

In the incidence context, the object and attribute copies are different even though both are indexed by \(W\). Thus nonincidence at equal indices, where \(\operatorname{dist}_H(x,x)=0\), is intentional. This **open**, exact-distance-one incidence differs from closed radius-one incidence.

## Proof

**1. Common-neighbor lemma.** Let \(N(v)=\{w:\operatorname{dist}_H(v,w)=1\}\). For distinct \(u,v\),
\[
 |N(u)\cap N(v)|=\begin{cases}q-2,&\operatorname{dist}_H(u,v)=1,\\2,&\operatorname{dist}_H(u,v)=2,\\0,&\operatorname{dist}_H(u,v)\ge3.\end{cases}
\]
At distance one, the common neighbors are precisely the other words on the connecting coordinate line. At distance two, they are precisely the two words obtained by changing one of the two differing coordinates. At larger distance there are none. This elementary lemma also appears as Lemmas 4.2–4.5 of Adler, Benediktsson, and Macpherson [3]; it is not claimed as new.

**2. Global upper bound and rigidity above dimension four.** In a scale of dimension \(k\), each pair of different attributes \(y_i,y_j\) has at least \(k-2\) common neighbors, namely the objects other than \(x_i,x_j\). The lemma gives \(k-2\le\max(q-2,2)\), hence \(k\le\max(q,4)\). When \(q\le4\), no scale of dimension five exists. Suppose instead \(q\ge5\) and \(k\ge5\). Each pair of attributes then has at least three common neighbors, which forces Hamming distance one between the attributes. Three or more pairwise adjacent words lie on one coordinate line, so all attributes lie on one line \(L\), giving \(k\le q\). Each object is adjacent to the other \(k-1\ge4\) attributes on \(L\). A word outside \(L\) is adjacent to at most one word on \(L\), so each object lies on \(L\). Distinct words on \(L\) are adjacent; to be nonincident with its matched attribute, an object must therefore equal that attribute. For \(k=q\), the scale is exactly \((L,L,\ne)\). Conversely this scale exists on every coordinate line, proving sharpness, uniqueness, and \(d q^{d-1}\) possibilities.

**3. Exhaustion of four-dimensional scales when \(2\le q\le4\).** Fix any scale of dimension four, and relabel so that its first attribute is \(y_1=0\), using independent permutations of the alphabet in each coordinate. The other three objects \(x_2,x_3,x_4\) are distinct open neighbors of \(0\). Classify them by how many coordinate directions they change. Write \(a_i\) for a word with the nonzero symbol \(a\) in coordinate \(i\), and \(a_i+b_j\) for the word that uses these two indicated symbols, with the other coordinates zero. These are not numerical sums.

*All three change one coordinate.* This requires \(q=4\): write \(x_2=a_i,x_3=b_i,x_4=c_i\) for the three nonzero symbols. Any attribute incident with \(x_3,x_4\) other than \(y_1\) must equal \(x_2\), hence \(y_2=x_2\); similarly \(y_3=x_3,y_4=x_4\). The only word incident with all three of these attributes is \(0\), so \(x_1=0\). This is exactly a full coordinate line with identity pairing.

*Two change the same coordinate, and the third changes another.* Put \(x_2=a_i,x_3=b_i,x_4=c_j\), where \(i\ne j\) and \(a\ne b\) are nonzero. Because \(y_2\) must be a common neighbor of \(x_3,x_4\) distinct from \(y_1=0\), necessarily \(y_2=b_i+c_j\); similarly \(y_3=a_i+c_j\). The fourth attribute \(y_4\) is a common neighbor of \(x_2,x_3\) distinct from \(0\). There are \(q-2\) common neighbors in total, so this is impossible when \(q\le3\). When \(q=4\), the only choice is \(y_4=t_i\), with \(t\) the fourth symbol distinct from \(0,a,b\). The common neighbors of \(y_2,y_3\) are \(c_j\) and \(t_i+c_j\); only the latter is adjacent to \(y_4\). Hence \(x_1=t_i+c_j\). This is exactly two parallel pairs using four different symbols in coordinate \(i\), with all witnesses uniquely forced. Its defining nonincidences follow from distance two.

*All three change different coordinates.* Put \(x_2=a_i,x_3=b_j,x_4=c_h\), with \(i,j,h\) distinct. The common-neighbor lemma forces \(y_2=b_j+c_h\), \(y_3=a_i+c_h\), \(y_4=a_i+b_j\). A word adjacent to all three is necessarily \(a_i+b_j+c_h\), so \(x_1\) equals that word. This is one parity class of a binary three-dimensional face, with the other parity class uniquely determining the attributes. Every one of the six object-pair distances equals two.

The three cases exhaust all triples of neighbors of \(y_1\), their constructions satisfy every prescribed incidence/nonincidence, and the cases are disjoint by pairwise object-distance signatures: respectively six distances one; two distances one and four distances two; or six distances two. No dimension-four scale exists for \(q=2\) or \(q=3\) when \(d\le2\), since only the third case is available and requires three coordinate directions.

**4. Counting.** For \(q=4\), choose a coordinate line in \(d4^{d-1}\) ways. For the two-parallel-pairs family choose an ordered pair of distinguished coordinates in \(d(d-1)\) ways; values of the other coordinates in \(4^{d-2}\) ways; two distinct symbols in the separating coordinate in \(\binom42=6\) ways; and partition the four symbols on the pair-coordinate into two (unlabeled) pairs in three ways, assigning the pairs to the selected separating symbols in two ways. This contributes \(36d(d-1)4^{d-2}\). For parity tetrahedra choose three coordinates, choose a two-symbol subset in each, fix the other coordinates, and select either parity class, contributing \(2\binom d3 4^{d-3}\binom42^3=432\binom d3 4^{d-3}\). The same parity count with \(q=2,3\) gives their formula. Unique witnesses ensure counts of supports equal counts of subcontexts.

**5. Sharpness in the remaining small cases.** A full coordinate line always gives a scale of dimension \(q\). For \(d\ge3\), a parity tetrahedron gives dimension four. These constructions and steps 2–3 prove the formula for \(b(q,d)\), except potentially \((q,d)=(2,2)\). Here the graph is a four-cycle with only two distinct open-neighborhood sets, while a dimension-three scale requires three different neighborhoods restricted to its objects. Hence the maximum is two. This completes all cases.

The standard correspondence between contranominal subcontexts and Boolean suborders of concept lattices is from [1,2]; together with this theorem it identifies the precise Boolean-suborder dimension. Adler, Benediktsson, and Macpherson [3] prove the separate uniform VC-dimension upper bound three for the same open-neighborhood relation. In particular, the unbounded Boolean dimension does not contradict their VC theorem: a contranominal scale realizes the \(k\) co-singleton traces on its \(k\) objects, not all \(2^k\) traces.

## Verification

Run `python3 verify.py` with standard Python 3. The checker computes incidence directly from Hamming distance, independently enumerates all object supports of predicted maximum dimension for fourteen parameter pairs, verifies the existence and uniqueness of matched attributes whenever dimension is at least four, verifies their geometric classification and the asserted enumerators, and exhaustively excludes the next larger scale dimension whenever the combinatorial search is moderate. It additionally checks 25,000 reproducibly sampled five-object supports for \((q,d)=(5,3)\). Exhaustive finite checking covers over four million candidate maximum-dimension supports. The all-parameter theorem depends on the preceding proof, not on finite extrapolation.

## Relationship to prior work

[1] Koyda and Stumme [1] introduce and analyze correspondences between Boolean subcontexts, Boolean suborders and sublattices for arbitrary finite formal contexts. Their results supply the interpretation of the extremal scales as Boolean suborders, but do not provide an open Hamming-specific extremal classification or counts.

[2] Dürrschnabel, Koyda, and Stumme [2] develop general algorithms to find contranominal scales and connect the problem to induced matchings in the complement bipartite graph. Their general algorithm is not an explicit evaluation of the open Hamming family.

[3] Adler, Benediktsson, and Macpherson [3] prove the exact pairwise Hamming open-neighborhood intersection formula (which is used here) and uniformly bound the open-neighborhood VC dimension by three. Their theorem does not identify the maximum co-singleton/contranominal family, the three geometric types at alphabet size four, the unique witnesses, or the formulas counting maximum scales. The distinction between VC dimension and Boolean suborder dimension is essential; neither invariant determines the other in this family.

The closed-radius-one Hamming incidence, previously studied separately, includes equality pairs and has a different extremal regime: for large alphabets the present exact-distance-one incidence supports arbitrarily large full-line scales. No closed-incidence conclusion is transferred without proof.

## Limitations

The classification counts maximum-dimensional *induced contranominal subcontexts*, not all Boolean sublattices, all lower-dimensional scales, or every minimal generator of the concept closure. The formulas for counts do not enumerate the special two- and three-dimensional maxima of \(H(2,2)\) and \(H(2,3)\). Literature searches and direct comparisons do not prove priority; equivalent results under bipartite crown, induced co-matching, or concept-lattice breadth terminology may exist. No independent scientific audit is asserted.

## References

[1] M. Koyda and G. Stumme, *Boolean Substructures in Formal Concept Analysis*, arXiv:2104.07159, first posted 2021-04-14. https://arxiv.org/abs/2104.07159

[2] D. Dürrschnabel, M. Koyda and G. Stumme, *Attribute Selection using Contranominal Scales*, arXiv:2106.10978, first posted 2021-06-21. https://arxiv.org/abs/2106.10978

[3] I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042, first posted 2020-07-31; in particular Hamming-graph Lemmas 4.2–4.5 and Theorem 4.6. https://arxiv.org/abs/2007.16042
