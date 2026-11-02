# Exactly two rank-five theories of finite Steiner quadruple systems

## Finding

Write \(\operatorname{SQS}(v)\) for a finite Steiner system \(S(3,4,v)\): a set \(V\) of \(v\) points and four-point blocks such that every triple of distinct points belongs to exactly one block. For all such systems with \(v\ge8\), in the point-only relational language described below:

**Theorem.** Every two systems agree on every first-order sentence of quantifier rank at most four. At rank five, two systems are equivalent if and only if both have eight points or both have at least ten points. Thus the entire infinite family has exactly two rank-five theories. The two smallest representatives have eight and ten points, and the sharp maximum of the least representative sizes is ten points.

A rank-five sentence separating the two classes asserts the existence of five pairwise distinct points \(a,b,c,d,e\) such that \(\neg B(a,b,c,d)\) and none of \(B(a,b,c,e)\), \(B(a,b,d,e)\), \(B(a,c,d,e)\), \(B(b,c,d,e)\) holds. This sentence is false in every system of order eight and true in every system of order at least ten.

## Assumptions and scope

The language consists solely of equality and one quaternary relation \(B\). Its interpretation is symmetric and irreflexive: \(B(a,b,c,d)\) holds exactly when the four arguments are distinct and form a block. Points, not blocks, are the domain. There are no named parameters or function symbols. Quantifier rank counts nested quantifiers; the displayed separator has rank five, notwithstanding the conjunction of quantifier-free conditions in its matrix.

All statements quantify over every finite nontrivial \(S(3,4,v)\) with \(v\ge8\), including nonisomorphic designs of the same order. Hanani's existence theorem ensures that the admissible orders in this range are precisely those satisfying \(v\equiv2\) or \(4\pmod6\). The exceptional class has order eight; the second starts at order ten. The cases of orders one, two and four are outside the stipulated domain.

## Proof

Let \(c(T)\) be the unique completion of a three-element point set \(T\): the unique point outside \(T\) for which \(T\cup\{c(T)\}\) is a block. This exists and is unique by the defining Steiner property.

**Extension lemma.** Let \(A\) be an ordered tuple with at most four distinct previously selected points. The complete atomic type of an additional selected point is determined by its equality to an existing point and by which three-element subsets of those earlier points it completes. If the tuple has three distinct points, then the unique completion realizes the distinguished new-point type, and all other unused points realize the generic new-point type. If the tuple has four distinct points forming a block, then all unused points realize one generic new-point type. If the tuple has four distinct points not forming a block, then each of its four triples has a completion outside \(A\), and these four completions are pairwise distinct; every further outside point realizes a generic new-point type.

To prove distinctness, suppose two distinct triples of the same four-point nonblock \(A\) had a common completion \(z\notin A\). The two blocks obtained would share the two points in the intersection of those triples and also \(z\), hence would share an entire triple. Unique triple completion forces the blocks equal; their unions would then force the original four points to form a block, contrary to the assumption. Consequently the number of generic outside points for a nonblock four-set is exactly \(v-8\). When only three points are selected, the number of generic outside points is \(v-4\); when four selected points form a block, it is \(v-4\). With fewer distinct selected points every fresh point has the same atomic relations to the previous selections, and a fresh point exists whenever fewer than five points have been selected.

**Four-round agreement.** Play the four-round Ehrenfeucht–Fraïssé game on any two systems in the stipulated domain. After the first three moves, the only distinction among possible fourth new points is whether it completes the previously selected triple; both possibilities occur because \(v\ge8\). The duplicated positions therefore preserve the complete atomic diagrams through four moves. Equality repetitions are matched exactly. Thus every pair of systems is \(\equiv_4\).

**Five-round agreement for orders at least ten.** Apply the same back-and-forth strategy through four moves. On the fifth move, compare the extension types from the lemma. Every equality type can be matched. For a preselected nonblock four-set, the four distinguished completion types each occur exactly once, and the generic type is realized \(v-8\ge2\) times. For a block four-set, the generic type occurs \(v-4\ge6\) times. For three or fewer distinct previously selected points, the completion and generic types available match across systems. Hence every atomic fifth-move extension on one side occurs on the other. Duplicator wins five rounds whenever both orders are at least ten.

**Sharp separation.** A nonblock four-set exists in every system of order at least eight: the number of blocks is \(\binom v3/4\), strictly less than \(\binom v4\). Its four distinct triple-completions occupy all four remaining points when \(v=8\), so the displayed rank-five sentence is false there. At each order \(v\ge10\) there are \(v-8\ge2\) additional points, so the sentence is true. Thus the two rank-five theories are different. Both \(\operatorname{SQS}(8)\) and \(\operatorname{SQS}(10)\) exist by the cited existence theorem and have explicitly checked representatives in the verification code. Since the second class has no member of order smaller than ten within this family, the sharp representative bound is ten. This completes the classification.

## Verification

The standalone `verify.py` constructs the Boolean affine systems on eight and sixteen points and an explicit 30-block system on ten points. It verifies unique triple completion, the four distinct triple-completions of every nonblock, and then independently calculates exact full first-order atomic-extension signatures through quantifier rank five. The reproduced trace in `verification_output.txt` gives a single class at rank four and exactly two at rank five. Run `python3 verify.py` with the standard library only. The finite check supports the proof but is not the basis for the theorem over arbitrary orders.

## Relationship to prior work

Linek (first public online 20 November 2006) studies colourings and chromatic spectra of Steiner quadruple systems; it supplies the defining setup and cites Hanani's existence theorem. Horan and Hurlbert (arXiv v1, 14 April 2012) study overlap cycles and recursive existence constructions for the same designs. Kaski, Östergård and Pottonen (2006) enumerate 1,054,163 isomorphism types at order sixteen, showing that ordinary isomorphism theory is vastly more discriminating than the two classes at rank five. None of those inspected mathematical results is a statement of the present point-only quaternary first-order equivalence theorem; this is a comparison of mathematical implications, not a global priority assertion.

## Limitations

The classification is only for the indicated point-only quaternary relational language and exactly ranks four and five, not for incidence languages with block elements, additional predicates, or higher quantifier ranks. The computational replay checks three finite representatives and does not replace the general extension proof. A comprehensive priority check over all historical and unindexed literature is not possible; mathematically equivalent treatments may exist. Independent validation has not been performed.

## References

1. V. Linek, *The spectrum of equitable, 4-chromatic Steiner quadruple systems*, Journal of Combinatorial Designs 15 (2007), 369–392, first published online 20 November 2006. DOI: 10.1002/jcd.20130.
2. V. Horan and G. Hurlbert, *Overlap Cycles for Steiner Quadruple Systems*, arXiv:1204.3215v1, 14 April 2012.
3. P. Kaski, P. R. J. Östergård and O. Pottonen, *The Steiner quadruple systems of order 16*, Journal of Combinatorial Theory A 113 (2006), 1764–1770. DOI: 10.1016/j.jcta.2006.03.017.
