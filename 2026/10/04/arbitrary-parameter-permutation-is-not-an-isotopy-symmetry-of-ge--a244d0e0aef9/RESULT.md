# Arbitrary parameter permutation is not an isotopy symmetry of general pretzel knots
## Finding
The blanket generalization in Theorem 13 of Meng--Liu--Zhou is false. Their theorem correctly states that, for a three-parameter pretzel knot, interchanging parameters does not change the knot type, but it then says that the same conclusion holds for general pretzel links. For four or more parameters, arbitrary reordering can change ambient-isotopy type.

A direct four-strand witness is
\[
P(3,5,7,2)
ot\cong P(3,7,5,2).
\]
The two ordered parameter tuples have the same multiset of entries, so the second is obtained from the first by a permutation. Lecuona and Wand explicitly record this pair as nonisotopic.

There is also a certificate by a standard topological invariant. The five-strand pretzel knot
\[
P(3,-7,5,-5,8)
\]
is fibered, whereas the reordered mutant
\[
P(3,5,-7,-5,8)
\]
is not fibered. Since fiberedness is invariant under ambient isotopy, these two knots cannot be isotopic. Thus the failure is not merely a distinction in a chosen diagram or parameterization.

For nonunitary parameters, cyclic permutation of the ordered parameters and reversal of the order are universal isotopy symmetries. These generate a dihedral action. When there are three parameters, this dihedral action is all of \(S_3\), so every parameter permutation is covered. For \(m\ge4\), the dihedral group has order \(2m\), strictly smaller than \(m!\), and arbitrary reordering is mutation rather than a guaranteed isotopy.

## Assumptions and scope
The correction concerns the assertion in Theorem 13 of arXiv:2609.29127v1 that the three-parameter permutation property extends to general pretzel links. The counterexamples above are pretzel knots, hence also counterexamples to the broader link assertion.

The clean symmetry statement is made for nonunitary parameters, meaning \(|p_i|>1\). Parameters equal to \(\pm1\) can have additional flype symmetries, so cyclic permutation plus reversal is not asserted here to be a complete classification in every unitary exceptional case. Likewise, the result does not say that every non-dihedral permutation changes knot type; it says only that such a permutation is not universally an isotopy symmetry.

## Proof
The source claim says that the conclusion for three pretzel parameters extends to general pretzel links. A single pair of reordered general pretzel knots that are not isotopic disproves that extension.

Lecuona and Wand state that the nonunitary parameters of a pretzel knot may be cyclically permuted and their order reversed without changing knot type, but further permutations may yield nonisotopic knots. They give the explicit four-strand pair
\[
P(3,5,7,2),\qquad P(3,7,5,2),
\]
and state that the first is not isotopic to the second. The tuples are permutations of the same four entries. Therefore arbitrary parameter permutation is not an ambient-isotopy symmetry for general pretzel knots.

A second argument gives an invariant certificate. Lecuona and Wand, using Gabai's classification of fibered pretzel knots, identify
\[
K=P(3,-7,5,-5,8)
\]
as fibered and the reordered mutant
\[
K'=P(3,5,-7,-5,8)
\]
as nonfibered. Ambient-isotopic knots have homeomorphic complements carrying the same fibration property, so fiberedness cannot differ between isotopic knots. Hence \(K
ot\cong K'\).

The boundary between the valid three-strand statement and the invalid generalization is transparent. Cyclic permutation and reversal of an ordered \(m\)-tuple generate a dihedral group of order at most \(2m\). For \(m=3\), that group is \(D_3\cong S_3\), so it realizes all six permutations. For every \(m\ge4\), \(2m<m!\), so the same geometric moves cannot realize every permutation. The published counterexamples show that the missing permutations are not merely absent from this move set: some genuinely change knot type.

## Verification
The source PDF was inspected at the exact statement of Theorem 13. It says that interchanging any two parameters of a three-pretzel knot gives an equivalent knot and then asserts that the conclusion holds for general pretzel links.

The supporting pretzel literature was inspected at its parameter-reordering discussion and fiberedness examples. It explicitly states both the four-strand nonisotopy witness and the five-strand fibered/nonfibered mutant pair used above.

The bundled program `artifacts/verify_parameter_symmetry.py` checks only the finite group-theoretic bookkeeping: cyclic shifts and reversal give all six permutations for three distinct entries, but only \(8\) of \(24\) permutations for four entries and \(10\) of \(120\) for five entries. It also verifies that both published counterexample reorderings lie outside their corresponding dihedral orbits. Its output is:

`VERIFY_OK D3=S3; D4=8<24; D5=10<120; both published reordered witnesses lie outside their dihedral orbits`

This computation is not evidence for nonisotopy; nonisotopy comes from the cited topological results.

## Relationship to prior work
Meng, Liu and Zhou's September 2026 preprint studies dihedral-quandle coloring spaces and quivers of pretzel links. Its Theorem 13 states the correct three-parameter permutation fact and then extends it to general pretzel links without a restriction. Later, in the general-pretzel section, the paper explicitly invokes Theorems 13 and 14 while organizing general \(m\)-pretzel links. The correction here is therefore relevant to how parameter reorderings are interpreted topologically, even though it does not by itself invalidate a coloring formula that may be symmetric under mutation or permutation for independent algebraic reasons.

The counterexamples themselves are not new: Lecuona and Wand's work predates the September 2026 preprint and stresses that order matters for pretzel knots with more than three strands. The new contribution here is the pinpoint contradiction with the recent Theorem 13, together with the precise repair boundary: the three-strand statement works because cyclic permutation and reversal already generate \(S_3\); the general arbitrary-permutation extension does not.

Targeted published-finding corpus and web searches for the recent preprint together with “parameter permutation,” “counterexample,” “mutation,” and the explicit witness tuples did not locate an existing correction of Theorem 13.

## Limitations
This finding corrects a specific isotopy assertion. It does not re-audit every coloring-number or coloring-quiver theorem in arXiv:2609.29127v1. A formula depending only symmetrically on the parameters can remain valid even when two reordered pretzel knots are nonisotopic, because quandle-coloring data need not distinguish all mutants.

The repaired symmetry statement is deliberately conservative. Nonunitary parameters always admit cyclic permutation and reversal without changing knot type, while unitary parameters can have additional flype symmetries. No complete isotopy classification of all parameter permutations is claimed.

## References
1. Qinghui Meng, Ximin Liu and Boxin Zhou, *Quandle coloring quivers of pretzel links*, arXiv:2609.29127v1, first posted 2026-09-24. See Theorem 13 and Section 3.3.
2. Ana G. Lecuona and Andy Wand, *Fibered ribbon pretzels*, arXiv:2408.03644; published in *Bulletin of the London Mathematical Society* (2026), DOI 10.1112/blms.70271. See the discussion of parameter reorderings and the fibered/nonfibered mutant examples.
