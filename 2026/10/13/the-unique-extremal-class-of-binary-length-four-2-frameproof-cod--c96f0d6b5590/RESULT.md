# Equality classification for binary length-four 2-frameproof codes

## Finding

Let \(C\subseteq\mathbb F_2^4\) be a 2-frameproof code. The known maximum size is five. The equality classification is that every five-word such code is uniquely of the form
\[
C=C_*+s,\qquad C_*=\{1000,0100,0010,0001,1111\},\qquad s\in\mathbb F_2^4,
\]
and every such translate is 2-frameproof. In particular, there are exactly 16 labeled maximum codes and one class under independent alphabet-symbol swaps in the four coordinates.

Exactly five of these codes contain \(0000\). One consists of \(0000\) and all four weight-three words. In each of the other four, the nonzero supports are the three edges of a star with center \(i\) on the coordinate set and the three-element complement of \(i\).

Each maximum has six unordered word pairs at Hamming distance two and four at distance three. The XOR of its five words is exactly \(s\), recovering the translation parameter from the code.

## Assumptions and scope

For \(P\subseteq C\), its descendants are the words \(x\in\{0,1\}^4\) with \(x_i\in\{p_i:p\in P\}\) in each coordinate. The code is 2-frameproof if this descendant set intersects \(C\) exactly in \(P\) whenever \(|P|\le 2\). Addition means coordinatewise XOR; a labeled code is a literal subset, with no quotient by any permutation. Coordinate permutations can also be included in the equivalence group without changing the single-class conclusion.

## Proof

Translating by a codeword places \(0000\) in the code without changing frameproofness. Let \(\mathcal F\) be the supports of the nonzero words after this translation. If distinct supports satisfy \(B\subset A\), the word with support \(B\) is a descendant of \(0000\) and the word with support \(A\). If two supports are disjoint, \(0000\) is a descendant of those two words. Both are forbidden. Thus \(\mathcal F\) is a pairwise-intersecting antichain.

A singleton can occur in such a family only by itself: any other member would either contain it or be disjoint from it. A full support can also occur only by itself. Otherwise the members have sizes two and three. Without any two-sets there are at most four members, and equality uses all four triples. If there is exactly one pair, two triples avoid containing it. If there are exactly two pairs they intersect, and precisely one triple avoids containing both: the triple omitting their common point. In either case the family has at most three members. At most three two-sets can be pairwise intersecting on four points (the six two-sets split into three complementary pairs), and three such sets form either a triangle or a star. Every triple contains an edge of the triangle, whereas the only triple avoiding all edges of the star is the complement of its center. This recovers the upper bound five and forces exactly the five types containing \(0000\) described above.

For attainment, \(C_*\) is 2-frameproof: the descendants of two distinct unit words have support in those two coordinates, so contain no other word of \(C_*\). Descendants of a unit word and \(1111\) must have a one in the unit's coordinate, so contain no other unit word. The empty and singleton coalitions give the required intersections directly. Translation by \(1111\) gives the all-triples form containing \(0000\); translation by the unit word in coordinate \(i\) gives the star form centered at \(i\). All five forced types therefore occur. Translating back gives precisely the translates of \(C_*\).

There are six pairs of unit words at distance two and four unit-to-\(1111\) pairs at distance three. These distances are translation invariant. The XOR of the four unit words is \(1111\), so the total XOR of \(C_*\) is zero. Translating five words by \(s\) changes that XOR to \(s\), proving uniqueness of the parameter and the count 16. Coordinate permutations fix \(C_*\). In the group of 16 translations and 24 coordinate permutations, the orbit is still the same 16 codes and the stabilizer has order 24.

## Verification

The stand-alone Python 3 program `verify.py` checks the descendant condition on all subsets of the 16-word space of size at least five. This is sufficient to check the maximum once five-word codes exist. It also compares the maximum codes with the translation orbit, checks the five forms containing \(0000\), and tests the Hamming-distance profile, XOR index and stabilizer.

Expected output:

`VERIFY_OK vertices=16 maximum=5 labeled_maxima=16 normalized_maxima=5 translation_orbit=16 natural_group=384 stabilizer=24 hamming_profile=2x6,3x4 xor_index=true maxima_sha256=243c8672229ef0d1ab8c6599b28cebfcf77356c939433924a2f0647c4c1a5145`

## Relationship to prior work

The descendant set of a pair of binary words is exactly the interval of vertices on shortest paths between the two words in the hypercube. Binary 2-frameproof sets are therefore precisely hypercube general-position sets. Korže and Vesel [1, §4, Table 1 and the accompanying exactness statement] give \(\operatorname{gp}(Q_4)=5\) by computation. The maximum size is prior work, not a new numerical bound here.

The representative is also known: Guo, Stinson and van Trung [2, Lemma 2.1, Theorem 5.1] identify the separating-hash-family formulation and construct the columns of an identity matrix with an added all-ones column. At length four those columns are \(C_*\). The distinction of the equality result is the proof that every optimal code lies in this particular translation orbit, with the corresponding labeled and zero-containing counts. The cited maximum and construction do not by themselves establish that assertion.

## Limitations

This classification is only for binary words of length four and coalitions of size at most two. It does not address optimal codes at larger lengths or over larger alphabets. A prior equality classification in another source or under another name is not ruled out.

## References

1. D. Korže and A. Vesel, “General Position Sets in Two Families of Cartesian Product Graphs,” *Mediterranean Journal of Mathematics* 20 (2023), article 203. DOI: [10.1007/s00009-023-02416-z](https://doi.org/10.1007/s00009-023-02416-z).
2. C. Guo, D. R. Stinson, and T. van Trung, “On tight bounds for binary frameproof codes,” [arXiv:1406.6920](https://arxiv.org/abs/1406.6920).
