# Exponential rarity and exact modal-type census for converse-bisimulation-rigid regular trees

## Finding

Fix integers \(q\ge 2\), \(a\ge 1\), and \(h\ge 0\). Give the vertices of the complete rooted \(q\)-ary tree of height \(h\) a color from an alphabet of size \(a\). Regard its child relation and its parent relation as **two distinct, converse modal accessibility relations**. A coloring is *rigid* when the greatest color-respecting bisimulation for this two-modal Kripke model is equality: every vertex survives in its ordinary bisimulation contraction.

Let \(R_{q,a}(h)\) be the number of different **outward-only rooted modal types** among rigidly colored complete \(q\)-ary trees of height \(h\). Here the outward type of a root is specified recursively by its color and the *set*, not multiset, of its children's outward types. Then
\[
R_{q,a}(0)=a,\qquad R_{q,a}(h+1)=a\binom{R_{q,a}(h)}q,
\]
where a binomial coefficient is zero when its upper argument is less than \(q\).

The **exact number of rigid colorings**, with tree vertices treated as distinguishable positions, is
\[
G_{q,a}(h)=R_{q,a}(h)(q!)^{(q^h-1)/(q-1)}.
\]
For positive height, a rigid coloring exists **if and only if** \(a\ge q\). At the critical alphabet size \(a=q\), the recurrence has a fixed point and
\[
G_{q,q}(h)=q(q!)^{(q^h-1)/(q-1)}.
\]
In particular, for one propositional bit and binary branching,
\[
G_{2,2}(h)=2^{2^h},\quad
\Pr(\text{rigid})=2^{-(2^h-1)}.
\]
Thus a binary complete tree of height \(3\), with \(15\) worlds, has precisely \(256\) rigid two-colorings out of \(32768\) colorings.

There is an **exact exponential rate** for every fixed \(a\ge q\). Put \(N_h=(q^{h+1}-1)/(q-1)\) and define
\[
\begin{aligned}
\Phi_{q,a}(r)&=\log(a/q!)+\sum_{j=0}^{q-1}\log(1-j/r),\\
C_{q,a}&=\log a+\sum_{m=0}^{\infty}q^{-m-1}\Phi_{q,a}(R_{q,a}(m)),\\
\delta_{q,a}&=\log a-\frac{\log(q!)}q-\frac{q-1}{q}C_{q,a}.
\end{aligned}
\]
The series converges absolutely; \(C_{q,q}=0\), \(C_{q,a}>0\) for \(a>q\), and \(\delta_{q,a}>0\). Under independent uniform vertex colors,
\[
\Pr(\text{rigid})=\exp\bigl(-[\delta_{q,a}+o(1)]N_h\bigr)
\quad\text{as }h\to\infty.
\]
This quantifies the rarity of colorings that prevent **all** converse-modal bisimulation compression, despite their existence with only \(q\) colors.

## Assumptions and scope

A \(q\)-ary tree here is the set of words of length at most \(h\) over \(\{0,\dots,q-1\}\), with all \(q\) children present at every nonterminal vertex; positions are fixed, even though neither modal relation names child positions. Color equality is the atomic-observation condition in bisimulation. Child and parent are separate directed modalities. Standard bisimulation ignores multiplicity of equivalent successors. The claim concerns the **entire unpointed finite model**, not just bisimulation at the designated root; the root is recognizable because it lacks a parent. No graded modalities, sibling-position modalities, or arbitrary-tree asymptotic claim is asserted. The case \(h=0\) has \(G_{q,a}(0)=a\) for every \(a\), including \(a<q\).

## Proof

**Step 1: local rigidity criterion.** For a colored finite rooted tree, define the outward modal type of each vertex inductively as its color together with the set of outward modal types of its children. Two rooted descendant trees are outward-bisimilar exactly when their root types agree, by bottom-up induction. We claim that two-way bisimulation is equality exactly when **every sibling family has pairwise distinct outward modal types**.

If siblings have the same outward type, relate their roots and match descendants recursively by equal outward types, remembering the matched parents. This gives a parent-coherent color-respecting relation satisfying forth/back for both child and parent modalities; add the diagonal outside these descendant subtrees. Thus the two siblings are two-way bisimilar. Conversely, if all sibling families have distinct outward types, two two-way-bisimilar vertices must have the same depth: repeated parent moves eventually encounter the unique root, which has no parent successor. Induct on the common depth. At depth zero the vertices agree. At positive depth their unique parents must be two-way bisimilar and hence equal by induction; they are now siblings, so the outward component of the two-way bisimulation forces identical outward types and therefore the same vertex. This proves the criterion for arbitrary finite rooted trees.

**Step 2: enumeration of rigid outward types.** For a complete height-zero tree every color yields one type, so \(R_{q,a}(0)=a\). At height \(h+1\), the criterion requires each child subtree to be rigid and the \(q\) child outward types to be pairwise different. The root's outward modal type records only its root color and the *unordered set* of those \(q\) types; hence exactly \(a\binom{R_{q,a}(h)}q\) possibilities occur. If \(a<q\), the bottom \(q\) siblings cannot have different colors, so no positive-height rigid coloring exists. If \(a\ge q\), assigning distinct colors to each sibling family recursively gives one; equivalently the recurrence stays at least \(a\). At \(a=q\), it remains identically \(q\).

**Step 3: count actual colorings.** Each rigid outward type of height zero is represented by precisely one coloring of the fixed rooted singleton. Inductively, suppose every rigid type of height \(h\) has the same number \(W_h\) of colorings on the *positioned* tree. A fixed rigid height-\(h+1\) root type selects a \(q\)-element set of child types; there are \(q!\) ways to place those types at the \(q\) child positions and \(W_h^q\) ways to color their descendant trees. Thus \(W_0=1\) and \(W_{h+1}=q!W_h^q\). Induction gives \(W_h=(q!)^{(q^h-1)/(q-1)}\), and multiplication by \(R_{q,a}(h)\) proves the census. The critical binary formulas follow immediately.

**Step 4: entropy limit.** Assume \(a\ge q\), write \(r_m=R_{q,a}(m)\), and factor the recurrence as
\[
r_{m+1}=r_m^q\frac{a}{q!}\prod_{j=0}^{q-1}(1-j/r_m).
\]
Because \(r_m\ge a\), the correction \(\Phi_{q,a}(r_m)\) is uniformly bounded. Dividing its logarithm by \(q^{m+1}\), then telescoping, gives
\[
q^{-h}\log r_h=\log a+\sum_{m=0}^{h-1}q^{-m-1}\Phi_{q,a}(r_m)\longrightarrow C_{q,a}.
\]
When \(a=q\), \(r_m=q\), so the limit is zero. When \(a>q\), \(r_1>r_0\), and \(\binom rq/r=\binom{r-1}{q-1}/q\) increases with integer \(r\ge q\). Hence \(r_m\) grows without bound; for any sufficiently large \(r_m\), the logarithmic recurrence is at least \(q\log r_m-K\) with fixed \(K\), which eventually yields a strictly positive lower bound on \(q^{-h}\log r_h\). Thus \(C_{q,a}>0\).

Since \(q^h/N_h\to(q-1)/q\) and \(((q^h-1)/(q-1))/N_h\to 1/q\), substitution in the exact probability \(G_{q,a}(h)/a^{N_h}\) yields the claimed \(\delta_{q,a}\). It is strictly positive without relying on numerical estimates: write \(p=(a)_q/a^q\in(0,1)\). The event that *every* sibling family has pairwise distinct immediate colors has probability \(p^{(q^h-1)/(q-1)}\) and implies rigidity. Rigidity, in turn, forces this condition on all \(q^{h-1}\) bottom sibling families, an independent collection. Therefore
\[
p^{(q^h-1)/(q-1)}\le \Pr(\text{rigid})\le p^{q^{h-1}},
\]
so the limiting exponential rate is strictly negative. This completes the proof for all fixed \(q,a\).

## Verification

Run `python verify_converse_rigidity.py` using Python 3. The program independently computes greatest two-modal bisimulation through iterative partition refinement, rather than using the sibling criterion as its acceptance test. It compares that decision to the recursive outward-type criterion and the exact census on \(35447\) exhaustively enumerated colorings across nine parameter cases. It includes all binary two-color trees through height \(3\), binary three-color trees through height \(2\), and ternary trees of height \(1\) with several alphabet sizes. The verifier tests only finite cases; the proof above supplies the unrestricted height and asymptotic assertions.

## Relationship to prior work

Worrell's discussion of strongly extensional trees already provides the general *uncolored structural viewpoint* that distinct sibling subtrees should not be tree-bisimilar; **that structural concept is not claimed to be new**. The quantitative contribution here is the positioned-vertex coloring census, its exact modal-type recurrence under two converse modalities, and the sharp exponential rate and alphabet threshold for complete regular trees. Bolander and Burigana (2024) motivate studying contractions through finite-modal bisimulation; their paper studies bounded-depth minimal contractions and exponential examples, not this all-depth colored-tree census. Figueira and Goren-Roig (2023, revised 2024) supply related multimodal/tree-bisimulation semantics but no such regular-tree enumeration in the inspected treatment. The earlier forward-only rooted-type recursion counts arbitrary sets of child types, whereas a converse-bisimulation-discrete tree permits only pairwise distinct children and leads to the stricter \(q\)-subset recursion. This distinction is essential: the present theorem is **not** a forward-only bisimulation result.

## Limitations

The sharp formulas count colorings of fixed regular ordered positions, not isomorphism classes of unordered colored trees. The entropy constant is a convergent series, not generally a closed elementary constant. The proof concerns the greatest two-modal bisimulation relation, not bounded-depth contraction, graded modalities, or automorphism-only asymmetry. The exact counting statements and their asymptotic rates have been checked against targeted accessible literature, but an implicit antecedent in older coalgebraic/tree-enumeration literature remains possible. No independent mathematical audit has been performed.

## References

1. Santiago Figueira and Gabriel Goren-Roig, *Modal Logic with Relations over Paths: a Theoretical Development through Comonadic Semantics*, arXiv:2307.09679, first submitted 2023-07-18; https://arxiv.org/abs/2307.09679 . Primary MSC 03B45.
2. Thomas Bolander and Alessandro Burigana, *Better Bounded Bisimulation Contractions*, arXiv:2405.00480, first submitted 2024-05-01; https://arxiv.org/html/2405.00480v1 .
3. James Worrell, *On the Greatest Fixed Point of a Finitary Set Functor*, online slides, specifically the section “Tree bisimulations”; https://www.cs.ox.ac.uk/james.worrell/gfp.pdf .
