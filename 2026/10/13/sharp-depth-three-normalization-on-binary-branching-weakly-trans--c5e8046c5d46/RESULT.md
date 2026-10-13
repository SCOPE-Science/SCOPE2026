# Sharp depth-three normalization on binary-branching weakly transitive frames

## Finding
Let \(\mathcal F_2\) be the class of all nonempty Kripke frames \((W,R)\), finite or infinite, satisfying
\[
R\circ R\subseteq R\cup\operatorname{Id}_W,
\qquad |R(w)|\le 2\quad\text{for every }w\in W.
\]
Self-loops are permitted and count toward the successor bound. In ordinary classical, one-agent propositional modal logic, **every formula is equivalent over \(\mathcal F_2\) to a formula of modal depth at most three**, using only the propositions already in the formula. This bound is sharp: there is a proposition-free depth-three formula not equivalent over \(\mathcal F_2\) to any formula of depth at most two.

Equivalently, on any pair of pointed models over frames in \(\mathcal F_2\), agreement on every formula of modal depth at most three implies full modal equivalence (and bisimilarity). Depth two does not suffice.

## Assumptions and scope
The accessibility relation is not presumed reflexive, irreflexive, symmetric, transitive, finite, or serial. Weak transitivity means \(xRy\land yRz\Rightarrow (xRz\lor x=z)\). The single unary modal operation \(\Diamond\) has ordinary existential-successor semantics, and \(\Box\) its Boolean dual. The modal depth of an atomic proposition is zero; each modal operation adds one. All formulas contain finitely many atomic propositions. The result concerns equivalence **over the specified frame class**, not logical equivalence over all Kripke frames.

## Proof
**1. Local reduction.** Weak transitivity implies \(R^*(w)=\{w\}\cup R(w)\). Indeed, any path of length two closes to a direct edge or returns to the initial point, and induction on path length proves the same for arbitrary paths. Thus the generated submodel of any pointed model contains at most three worlds. Restricting a model to this generated submodel preserves every modal formula and preserves the stated two frame conditions.

**2. Atom patterns.** To compare two pointed generated models, each with one, two, or three worlds, form their disjoint union. Two worlds receive the same *atomic color* precisely when they agree on every proposition in the formula's finite vocabulary. The actual names of distinct colors play no role in bisimulation. Hence all possible color assignments are represented by set partitions of at most six worlds, enumerated uniquely as restricted-growth words. This remains true for arbitrarily large finite vocabularies.

**3. Depth signatures.** For a colored directed graph \(G\), recursively define
\[
\sigma_0(w)=\operatorname{color}(w),\qquad
\sigma_{d+1}(w)=\bigl(\operatorname{color}(w),\{\sigma_d(u):wRu\}\bigr).
\]
A standard induction on modal depth, using finite conjunctions of characteristic formulas, says that two worlds have equal depth-\(d\) signatures if and only if they satisfy the same formulas of modal depth at most \(d\). Set-valued successor signatures reflect ordinary, non-counting modalities. If equality of the partitions given by \(\sigma_d\) and \(\sigma_{d+1}\) holds globally on a given disjoint union, it holds at every subsequent depth by the same recurrence.

**4. Exhaustive finite lemma.** The standalone file `verify_depth3.py` enumerates **all** one-, two-, and three-world directed relations with weak transitivity and at most two edges out of each world (including loops). Their labeled counts are respectively \(2,16,159\). Passing to graph-isomorphism representatives gives \(2,10,37\) types. For each ordered pair of representatives, the checker visits every partition of the combined vertex set into atomic-color classes and computes depth-zero through depth-four signatures. There are exactly **320315** such pairs of frame representatives and color partitions. In every case, the equivalence relation induced by \(\sigma_3\) is identical to that induced by \(\sigma_4\), for **all** worlds in the disjoint union, not only the selected roots. The source implements the entire bounded finite enumeration and asserts its exact coverage counts. As explained in steps 1–3, the finite lemma exhausts the possibilities in arbitrary, even infinite, frames; it is not extrapolation from samples of larger frames.

**5. Normal form.** By steps 1–4, agreeing on all depth-three formulas implies agreeing at every finite modal depth for any pair of pointed models in \(\mathcal F_2\). Fix the finite vocabulary \(P\) of a formula \(\varphi\). There are finitely many pointed, \(P\)-colored generated models on at most three worlds; their depth-three types therefore form a finite set. Each type has a depth-three characteristic formula, recursively constructed from its atomic literals, successor-type diamonds, and a box restricting successor types. The disjunction of the characteristic formulas of those types satisfying \(\varphi\) agrees with \(\varphi\) at every point of every model over \(\mathcal F_2\). If no type satisfies \(\varphi\), take \(\bot\). This completes the unrestricted normalization claim.

**6. Sharpness.** On \(\{a,b,c\}\), let \(P\) have arrows \(a\to b,a\to c,b\to c\), and let \(Q\) have arrows \(a\to b,a\to c,b\to a,b\to c\); all other arrows are absent. Both are weakly transitive and have at most two successors per world. At the pointed world \(a\), with all propositions constant, the depth-two signatures agree: the root sees one successor having successors and one dead end, and the same is true one level lower. However \(Q,a\models\Diamond\Diamond\Diamond\top\), while \(P,a\not\models\Diamond\Diamond\Diamond\top\). The required depth cannot be lowered.

## Verification
From the directory containing `verify_depth3.py`, run `python3 verify_depth3.py` (only the Python standard library is needed). It verifies the exact numbers of labeled and unlabeled admissible frames, proves completeness of the isomorphism representatives by directly checking all labeled frames, enumerates all restricted-growth color partitions, and asserts no discrepancy between depth-three and depth-four equality partitions. It additionally verifies the two sharpness models, their depth-two agreement, and the depth-three reachability formula. The run reported **320315** exhaustive cases, with depth partition changes occurring in **291034**, **27989**, and **68** cases respectively at refinement steps one, two, and three, and **zero** changes at step four.

## Relationship to prior work
Santschi and Vooijs (2026) study weakly transitive modal frames, define the weakly transitive relation used here, and prove finite-model and finite-width selection theorems. Their Theorems A–C and their modal-type/bisimulation discussion do not give this fixed-depth, outdegree-two normal form or its sharp lower bound. Bolander and Burigana (2024) study bounded bisimulation contractions generally; their results motivate the depth-indexed comparison but do not provide the class-specific exact stabilization threshold. This finding relies on standard modal characteristic formulas and does not claim those tools as new.

## Limitations
The statement is for one ordinary Boolean modality, not two-agent, graded, fixpoint, or quantitative modal languages. The outdegree restriction counts reflexive edges. No compact bound on the **length** of the normal-form formula is asserted. The finite certificate is an exhaustive proof only because weak transitivity first reduces every generated model to at most three worlds and equality partitions cover every atomic valuation pattern. Exhaustive computer execution is not independent validation; the reduction, code, and mathematical significance remain available for external review. Older equivalent presentations under bounded-morphism or filtration terminology cannot be categorically ruled out.

## References
1. Simon Santschi and Niels C. Vooijs, *Logics Containing wK4: Selection à la Fine*, 2026, arXiv:2606.31920, first public 2026-06-30. https://arxiv.org/abs/2606.31920 ; full text: https://www.researchgate.net/publication/408301639_Logics_Containing_wK4_Selection_a_la_Fine
2. Thomas Bolander and Alessandro Burigana, *Better Bounded Bisimulation Contractions*, 2024, arXiv:2405.00480. https://arxiv.org/abs/2405.00480
3. Simon Lemal, *Hereditary structural completeness of weakly transitive modal logics*, Master of Logic thesis, 2023. https://eprints.illc.uva.nl/id/eprint/2280/
