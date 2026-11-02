# Sharp rank-two consistency and counting for indexed tense logic

## Finding
Fix integers \(p\geq0\) and \(r\geq1\). Consider classical propositional modal logic with \(p\) propositional letters and \(r\) named accessibility relations, each equipped with its converse modality, over **all** nonempty Kripke frames (finite or infinite). Put \(m=2^p\) and
\[
 t_1=m2^{2rm},\qquad t_2=m2^{r t_1}.
\]
There are exactly \(t_1\) pairwise inequivalent pointed modal-depth-at-most-one types and exactly \(t_2\) pairwise inequivalent pointed modal-depth-at-most-two types. Hence the Boolean algebra of equivalence classes of formulas of modal depth at most two has exactly \(2^{t_2}\) elements.

The stronger statement is a **complete satisfiability criterion** for arbitrary proposed two-step characteristic formulas. A root profile comprises an atomic colour \(c\), and for each relation \(i\), a set \(A_i\) of one-step types to appear among successors and a set \(B_i\) of one-step types to appear among predecessors. It is realizable exactly if every \(\tau\in A_i\) allows \(c\) among its \(i\)-predecessor colours, and every \(\tau\in B_i\) allows \(c\) among its \(i\)-successor colours. Every realizable profile admits an explicit finite model with at most
\[
 1+m+\sum_{i=1}^r(|A_i|+|B_i|)
\]
worlds.

Modal depth two is the **first depth at which the converse pairing can affect the type count**: depth zero sees only colours, and depth one independently records the two directional sets without testing their reciprocal consistency. For comparison, treating the \(2r\) modalities as independent, rather than paired as converses, yields \(m2^{2rt_1}\) depth-two types. Thus the converse axioms discard exactly a proportion \(1-2^{-rt_1}\) of the unrestricted second-stage profiles; the fraction left is \(2^{-rt_1}\). In particular, in the variable-free single-relation case the counts are \(t_1=4\) and \(t_2=16\), versus \(256\) unrestricted second-stage profiles. With one proposition and one converse pair the exact depth-two count is \(2^{33}\).

## Assumptions and scope
A model is \(M=(W,(R_i)_{1\leq i\leq r},V)\), where \(W\ne\varnothing\), each \(R_i\subseteq W^2\) is entirely unrestricted, the forward diamond \(\Diamond_i\) quantifies over \(R_i\)-successors, and the backward diamond \(\Diamond_i^{-}\) quantifies over \(R_i\)-predecessors. Boolean connectives are classical. Modal depth increases by one under either diamond or its dual box. A colour is the complete truth assignment to the \(p\) letters, chosen from an \(m\)-element set \(C\).

A one-step type is precisely a tuple \(\tau=(d,(S_i,T_i)_{i=1}^r)\), with \(d\in C\) and \(S_i,T_i\subseteq C\); its second coordinate records colours of immediate \(R_i\)-successors and predecessors. Let \(\mathcal T_1\) denote the set of all such tuples. A proposed two-step profile is \((c,(A_i,B_i)_{i=1}^r)\), where \(c\in C\) and \(A_i,B_i\subseteq\mathcal T_1\). Different accessibility relations may share worlds, but no such sharing is required. We count logical equivalence over the whole unrestricted frame class, not isomorphism classes of particular frames or equivalence of unrestricted modal-depth formulas.

## Proof
**Step 1 (one-step normal form).** Every choice of \((d,(S_i,T_i))\) is realized: place a root of colour \(d\), one distinct immediate \(i\)-successor for each colour in \(S_i\), and one distinct \(i\)-predecessor for each colour in \(T_i\), with no other root-adjacent edges. Thus \(|\mathcal T_1|=m(2^m)^{2r}=t_1\). The colour and these sets determine exactly which depth-one formulas hold. Conversely, characteristic formulas requiring each listed colour and excluding every unlisted colour in each direction distinguish all different tuples.

**Step 2 (necessary compatibility).** Suppose a world \(w\) of colour \(c\) has \(i\)-successor \(v\) of one-step type \(\tau\). Since \(wR_i v\), the colour \(c\) necessarily belongs to the recorded \(i\)-predecessor-colour set \(T_i(\tau)\). Likewise, if \(uR_i w\), then \(c\in S_i(\operatorname{type}_1(u))\). Thus any realizable two-step profile satisfies
\[
 \forall i\,\forall\tau\in A_i:\ c\in T_i(\tau),\qquad
 \forall i\,\forall\tau\in B_i:\ c\in S_i(\tau).
\]

**Step 3 (sufficiency, including the explicit size bound).** For every \(i\) and every type \(\tau\in A_i\), create a distinct successor witness \(a_{i,\tau}\) of atomic colour \(d(\tau)\) and insert only the root edge \(wR_i a_{i,\tau}\). Similarly, for every \(\tau\in B_i\), create a distinct predecessor witness \(b_{i,\tau}\) and insert \(b_{i,\tau}R_i w\). Create one further auxiliary world \(z_d\) of each colour \(d\in C\), not joined directly to the root in any relation. For every witness \(v\) assigned the type \(\tau\) and each relation \(j\), realize its prescribed outgoing colour set by edges \(vR_jz_d\) for the requisite colours, and its incoming colour set by edges \(z_dR_jv\). Omit the redundant edge to an auxiliary world when that same required colour is already realized by the root: for a forward witness along \(i\), omit auxiliary incoming colour \(c\) in relation \(i\); for a backward witness along \(i\), omit auxiliary outgoing colour \(c\) in relation \(i\). All requisite root-contributed colours are guaranteed by Step 2. The auxiliary worlds need satisfy no restrictions on their own one-step types. No auxiliary edge touches the root, so the root's neighbour-type sets remain exactly \(A_i,B_i\). The construction uses \(1+m+\sum_i(|A_i|+|B_i|)\) worlds and verifies every witness's full one-step type. There are no other compatibility conditions.

**Step 4 (exact counting).** Fix the root colour \(c\). For a given relation \(i\), exactly half of the \(t_1\) one-step types contain \(c\) in their \(i\)-predecessor-colour set, because the presence of \(c\) is one freely chosen Boolean coordinate. Thus \(A_i\) may be any of \(2^{t_1/2}\) subsets. Independently, exactly half of the types admit \(c\) as an \(i\)-successor colour, and \(B_i\) has \(2^{t_1/2}\) possibilities. With \(r\) independently chosen relation-pairs and \(m\) choices of \(c\), the number of realizable two-step profiles is
\[
 m\bigl(2^{t_1/2}2^{t_1/2}\bigr)^r=m2^{rt_1}=t_2.
\]
The characteristic formula of a profile conjoins its root colour formula with, for each \(i\), one diamond condition per listed one-step neighbour type and one box condition excluding all unlisted types, in both directions. It has depth at most two and holds exactly on worlds with that profile. Therefore the profiles are mutually distinguishable, and all disjunctions of their characteristic formulas are definable, proving the exact \(2^{t_2}\) formula-class count. In independent \(2r\)-modal logic, every one-step type may occur in every successor set independently, so there are instead \(m2^{2rt_1}\) second-stage profiles, proving the stated deficit.

## Verification
The standalone `checker.py` enumerates the complete one-step-type space for several small colour and relation counts, constructs finite models from the compatibility criterion, and recomputes their profiles directly from edge sets. It checks all \(16\) variable-free single-relation two-step profiles, samples additional cases with one or two converse pairs and up to three atomic colours, and independently exhausts all directed graphs on at most four labelled vertices in the variable-free single-relation setting, recovering respectively \(2,8,14,16\) distinct profiles by increasing the world bound from one to four. Running `python checker.py` prints `ALL_CHECKS_OK` on success. These finite computations test the construction; the general theorem depends on the symbolic proof above, not extrapolation from samples.

## Relationship to prior work
Sano, *Uniform Interpolation of Basic Tense Logic* (arXiv:2606.31887, first submitted June 30, 2026), proves uniform interpolation for converse modalities and, in Proposition 3.6 and Appendix A, states finite-rank local tabularity and canonical-form constructions. The paper also notes extension to multiple indexed converse pairs. The result here supplies a necessary-and-sufficient realizability test and closed cardinalities specifically for **depth two**, rather than re-proving uniform interpolation or local tabularity. Earlier canonical-form treatments by Fine (1975) and Moss (2007) provide the classical modal normal-form method, on which the distinguishing-characteristic-formula argument relies. The full accessible text of Sano (Sections 3, 8, and Appendix A) and Moss (Sections 1–2) was compared against these specific claims; no explicit formula for the admissible two-step **tense** profiles was identified there. This negative comparison is limited to the material actually read, not a claim of exhaustive priority.

## Limitations
The exact profile criterion and census are restricted to modal depth at most two. No recurrence at arbitrary depths, minimization of the size bound, algorithmic complexity lower bound, or full classification of uniform interpolants is proved. The models are unrestricted directed frames; symmetry, transitivity, linear time, or other axioms can introduce further obstructions. Published equivalences under alternative terminology may exist, so independent priority review is needed. 

## References
- Katsuhiko Sano, *Uniform Interpolation of Basic Tense Logic*, arXiv:2606.31887 (first submitted 2026-06-30), https://arxiv.org/abs/2606.31887.
- Lawrence S. Moss, *Finite Models Constructed From Canonical Formulas*, Journal of Philosophical Logic 36 (2007), 605–640, DOI 10.1007/s10992-007-9052-4, https://www.researchgate.net/publication/227095368_Finite_models_constructed_from_canonical_formulas.
- Kit Fine, *Normal Forms in Modal Logic*, Notre Dame Journal of Formal Logic 16 (1975), 229–237, DOI 10.1305/ndjfl/1093891703.
