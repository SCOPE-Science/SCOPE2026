# A sharp three-leaf threshold for unary Gödel-modal stars

## Finding

Consider the finite, nonreflexive, one-step crisp Gödel-modal star \(S_m\) with a root \(r\) and exactly \(m\ge1\) terminal successors. The language contains exactly one propositional variable \(p\), constants \(\bot\), Gödel connectives \(\wedge,\vee,\to\), and modalities \(\Box,\Diamond\). All atomic truth values lie in \([0,1]\).

**Uniform reduction theorem.** Every valuation on \(S_m\) has a root-value-preserving induced substar with at most three terminal successors, simultaneously for **every formula** in the one-variable language. It suffices to retain a leaf of value \(0\) (if present), a leaf of smallest strictly positive \(p\)-value (if present), and a leaf of largest strictly positive \(p\)-value (if distinct). This bound is sharp even when the retained substar need only reproduce the complete rooted theory rather than each root truth value.

Writing \(L_m\) for the set of one-variable formulas valid at **all worlds, under all valuations** on \(S_m\), the complete finite-star hierarchy is
\[
L_1\supsetneq L_2\supsetneq L_3=L_4=L_5=\cdots.
\]
The first strict inclusion is witnessed by \(\Diamond p\to\Box p\). The second is witnessed by
\[
\neg\Box p\ \to\ \bigl(\Diamond p\ \to\ \Box(p\vee\neg p)\bigr),
\]
where \(\neg\alpha\) abbreviates \(\alpha\to\bot\).

## Assumptions and scope

In the Gödel algebra, \(a\wedge b=\min(a,b)\), \(a\vee b=\max(a,b)\), and \(a\Rightarrow b=1\) when \(a\le b\), otherwise \(b\). Every leaf has no successors, so its modal operators have respective constant values \(1\) and \(0\). At the root, box and diamond are respectively the minimum and maximum of scope values over its nonempty successor set. The accessibility relation consists **only** of root-to-leaf arrows; no world is reflexive, and no leaf sees another world. A formula is valid on the frame if it takes value \(1\) at every world for every assignment of \(p\) to worlds. Every model considered here is finite and therefore witnessed in the standard crisp Gödel sense.

The theorem is specific to one atomic variable and does not claim a universal three-leaf bound for two or more variables, arbitrary fuzzy relations, recursive trees, or frames with successor-to-successor edges.

## Proof

**1. Six possible terminal unary functions.** At a leaf, replace \(\Box\alpha\) by \(\top\) and \(\Diamond\alpha\) by \(\bot\), recursively. The resulting one-variable Gödel propositional term has one of precisely six functions on \([0,1]\):
\[
0,\quad 1,\quad x,\quad\neg x,\quad\neg\neg x,\quad x\vee\neg x.
\]
Indeed, at \(x=0\), each of these is \(0\) or \(1\); at every \(0<x<1\), each is uniformly \(0\), \(x\), or \(1\); and at \(x=1\) the same recipe applies with \(x=1\). The six displayed functions are pairwise distinct, include all propositional generators and modal-leaf constants, and are closed under min, max, and Gödel residuation. For an explicit closure check, represent their values on the three regions \(x=0\), \(0<x<1\), and \(x=1\) respectively as
\[
(0,0,0),\ (1,1,1),\ (0,x,1),\ (1,0,0),\ (0,1,1),\ (1,x,1).
\]
The operations act pointwise, and because \(0<x<1\), direct application of the three Gödel truth functions to every ordered pair stays within this list. Structural induction proves the exhaustion claim for all formulas, regardless of modal nesting.

**2. Extremal witnesses simultaneously suffice.** Fix a valuation on \(S_m\). Let \(P\) be the multiset of strictly positive leaf \(p\)-values. Retain a zero leaf when present and, when \(P\ne\varnothing\), a leaf with \(\min P\) and one with \(\max P\), counting identical leaves only once. This nonempty retained leaf set has size at most three. For each of the six leaf term functions, its minimum and maximum over all original leaves are preserved by these representatives: on positive values the function is uniformly \(0\), the identity, or \(1\), and its zero-value is separately represented if needed. Thus the values of **every** root modal subformula \(\Box\alpha\) and \(\Diamond\alpha\) are unchanged after restriction, since \(\alpha\) at a terminal leaf is a unary term function. A further induction on arbitrary formulas, keeping the root atomic value fixed, proves equality of the root value for every one-variable formula simultaneously. This argument does not use a formula-dependent selection of witnesses.

**3. Exact validity hierarchy.** If \(m\ge3\), every rooted \(S_m\) valuation compresses to at most three leaves. Duplicating a leaf to reach exactly three does not change any root modal extrema or root formula values. Conversely, every \(S_3\) valuation extends to any \(S_m\) by duplicating leaves. The set of possible root evaluations is consequently identical for \(m\ge3\). A formula false at a terminal leaf for some \(p\)-value can be made false at a terminal leaf on any \(S_m\), so leaf-world validity does not distinguish the frames. This proves \(L_m=L_3\) for all \(m\ge3\), and the same extension argument implies \(L_1\supseteq L_2\supseteq L_3\).

For \(S_1\), \(\Diamond p\) and \(\Box p\) agree at the root, while at the leaf their values are \(0\) and \(1\); hence \(\Diamond p\to\Box p\) is valid. It fails on \(S_2\) with leaf \(p\)-values \(0,1\), giving value \(0\) at the root.

Set \(B=\neg\Box p\to(\Diamond p\to\Box(p\vee\neg p))\). At any leaf, \(\neg\Box p=0\), so \(B=1\). In a two-leaf star, if both \(p\)-values are positive then \(\neg\Box p=0\) and \(B=1\). If both are zero then \(\Diamond p=0\), so again \(B=1\). In the remaining case the values are \(0,t\) with \(t>0\); hence \(\Diamond p=t\) and \(\Box(p\vee\neg p)=\min(1,t)=t\), yielding \(B=1\). Thus \(B\in L_2\). On \(S_3\) with leaf values \(0,a,b\) for \(0<a<b<1\), one has \(\neg\Box p=1\), \(\Diamond p=b\), and \(\Box(p\vee\neg p)=a\), whence \(B=a<1\) at the root. For example, \(a=1/4\) and \(b=3/4\). Thus \(B\notin L_3\), completing both strictness results and the sharpness claim.

## Verification

The supplementary pure-Python script `verify.py` constructs the six unary functions using finite-rational Gödel operations; exhaustively verifies their extremal preservation for all leaf tuples of length one through five over the grid \(\{0,1/4,1/2,3/4,1\}\); checks both explicit strictness witnesses; and tests random recursively nested modal formulas. Its verified output is `distinct_unary_leaf_term_functions 6`, `exhaustive_unary_extremum_comparisons 23430`, `nested_formula_comparisons 4000`, `VERIFY_OK`. These finite checks are **not** the proof for arbitrary real valuations or arbitrary formula complexity; the symbolic six-function classification and inductions above prove the theorem.

## Relationship to prior work

Ferrari, Fiorentini and Rodriguez introduce witnessed crisp Gödel models and establish decidability and a finite-model property (2025, DOI below). Ferrari, Fiorentini, Giardini and Rodriguez extend the witnessed-model approach in 2026 (arXiv below). These general semantic and finite-model results do not, in their inspected material, state the uniform three-successor reduction simultaneously preserving all one-variable formula values on nonreflexive stars or the exact strict two-transition validity hierarchy. Finite formula-dependent witness selections are conceptually related but do not imply this formula-independent sharp bound; conversely the present theorem applies only to its specified stars and language. The distinction is structural and by quantifier scope, not merely terminology.

## Limitations

The reduction is for full truth values at a designated root; deleting leaves does not preserve validity of arbitrary multiworld formulas at every deleted leaf. The resulting frame-logic equality explicitly accounts for terminal worlds. The claim does not include any independent mathematical audit, or establish novelty over every unindexed paper. The reproducibility checks are finite sanity tests; no finite grid can establish the continuum-valued theorem without the accompanying symbolic argument.

## References

1. Mauro Ferrari, Camillo Fiorentini, Ricardo Oscar Rodriguez, *A Gödel Modal Logic over Witnessed Crisp Models*, TABLEAUX 2025, first online 25 September 2025, DOI:10.1007/978-3-032-06085-3_8, https://link.springer.com/chapter/10.1007/978-3-032-06085-3_8.
2. Mauro Ferrari, Camillo Fiorentini, Paolo Giardini, Ricardo Oscar Rodriguez, *A Gödel Modal Logic Over Witnessed Models*, arXiv:2606.31906 (2026), https://arxiv.org/abs/2606.31906.
