# Adjacent-palette rigidity and exact generation census for finite S4.3 cluster chains

## Finding
Let \(h\geq1\) and let \(a_1,\ldots,a_h\geq1\). Write \(W=C_1\sqcup\cdots\sqcup C_h\), with \(|C_i|=a_i\), and give \(W\) the reflexive transitive relation
\[
xRy\quad\Longleftrightarrow\quad x\in C_i,\ y\in C_j,\ i\leq j.
\]
This is the finite rooted linear-preorder, or reflexive S4.3-cluster-chain, frame. Equip its full Boolean powerset algebra with the possibility operator \(\Diamond X=\{x:\exists y\,(xRy\land y\in X)\}\). Take an ordered tuple of \(r\geq0\) generating sets. Its Boolean truth pattern at each world is a color in an alphabet of \(q=2^r\) colors. Let \(S_i\) denote the set of colors used in \(C_i\).

**Theorem.** The tuple generates all of \(\mathcal P(W)\) under Boolean operations and \(\Diamond\) if and only if:

1. the colors inside each \(C_i\) are pairwise distinct; and
2. \(S_i\not\subseteq S_{i+1}\) for every \(1\leq i<h\).

Whenever these conditions hold, every singleton is defined by a modal formula of depth at most \(h-1\).

Put \(q=2^r\), and interpret binomial coefficients outside their ordinary ranges as zero. For \(q\geq\max_i a_i\), the exact number of **ordered** generating \(r\)-tuples is
\[
N_r=\left(\prod_{i=1}^{h}a_i!\right)\binom q{a_h}
\prod_{i=1}^{h-1}\left(\binom q{a_i}-\binom{a_{i+1}}{a_i}\right).
\]
For \(q<\max_i a_i\), the number is zero. Define
\[
q_* = \max\!\left(\max_{1\leq i\leq h}a_i,\ 1+\max_{\substack{1\leq i<h\\a_i\leq a_{i+1}}}a_{i+1}\right),
\]
where the second entry is omitted if its indexing set is empty. The minimum number of generators is exactly
\[
\operatorname{rank}(\mathcal P(W),\Diamond)=\left\lceil\log_2 q_*\right\rceil.
\]
These statements include the one-cluster frame and the zero-generator one-point case.

For equal cluster sizes \(a_i=a\) and \(h\geq2\), the threshold simplifies to \(q_*=a+1\) and the census to
\[
N_r=(a!)^h\binom qa\left(\binom qa-1\right)^{h-1}.
\]
This exhibits the strict extra-color requirement: distinct colors within each cluster alone do not suffice. For \((a_1,a_2,a_3)=(2,1,2)\), the smallest alphabet has three colors, hence two Boolean generators, and there are exactly \(288\) ordered generating pairs (four available colors).

## Assumptions and scope
All clusters are nonempty and finite, their order is fixed and named through the accessibility relation, and the relation is **reflexive** at every world. The language has ordinary Boolean connectives and the single forward possibility modality, with propositional constants. The enumeration counts ordered tuples of sets rather than tuples modulo permutations or Boolean transformations. The results do not assert the same criterion for irreflexive chains, arbitrary transitive frames, or strictly positive fragments lacking Boolean negation.

## Proof
A complete Boolean truth pattern \(c\) is definable at depth zero by the conjunction \(\chi_c\) of the corresponding positive and negative generator literals.

**Necessity within clusters.** Two distinct points of the same cluster with the same pattern are interchanged by a color-preserving frame automorphism. They therefore satisfy precisely the same generated formulas, ruling out the whole powerset algebra.

**Necessity between consecutive clusters.** Suppose \(S_i\subseteq S_{i+1}\). Fix a point \(x\in C_i\), and choose \(y\in C_{i+1}\) with the same color. The identity relation on \(W\), extended by all pairs of matching-color points between \(C_i\) and \(C_{i+1}\) and their reversals, is a color-preserving bisimulation. Indeed, any successor in \(C_i\) has a matching-color successor in \(C_{i+1}\), and all other successors are available on both sides. Thus \(x\) and \(y\) satisfy the same modal formulas and cannot be separated.

**Sufficiency and explicit formulas.** Assume both conditions. Choose a witness color \(c_i\in S_i\setminus S_{i+1}\) for each \(1\leq i<h\). Set \(T_{h+1}=\bot\). Working backward, define
\[
T_{i+1}:=\neg\Diamond\bigl(\chi_{c_i}\land\neg T_{i+2}\bigr),
\qquad i=h-1,h-2,\ldots,1.
\]
We claim that \(T_{i+1}\) denotes exactly \(C_{i+1}\cup\cdots\cup C_h\). This is proved by backward induction. On the later suffix beyond \(C_{i+1}\), the guard \(\neg T_{i+2}\) excludes every world. On \(C_{i+1}\), the chosen color \(c_i\) does not occur. Thus no world from cluster \(i+1\) onward sees a guard witness. Every world in a cluster at or before \(i\), however, sees the witness of color \(c_i\) in \(C_i\), which is outside the later suffix. Hence precisely the desired tail satisfies \(T_{i+1}\).

Put \(T_1=\top\). Then \(T_i\land\neg T_{i+1}\) defines exactly \(C_i\), and intersecting it with \(\chi_c\) defines each singleton because colors are injective within a cluster. A finite Boolean algebra containing all singletons is the full powerset algebra. As \(\chi_c\) has depth zero and each backward step introduces at most one \(\Diamond\), all these singleton formulas have modal depth at most \(h-1\).

**Enumeration.** For each cluster \(C_i\), a palette \(S_i\subseteq[q]\) of size \(a_i\) has exactly \(a_i!\) bijective assignments to its labeled worlds. Starting at the last cluster, there are \(\binom q{a_h}\) palettes. For a fixed next palette of size \(a_{i+1}\), exactly \(\binom q{a_i}-\binom{a_{i+1}}{a_i}\) palettes of size \(a_i\) fail to be its subset. This number does not depend on the particular next palette. Multiplying from right to left gives the census.

**Rank.** A generating coloring requires \(q\geq a_i\) for every cluster. If \(a_i\leq a_{i+1}\), strict noncontainment also requires \(q\geq a_{i+1}+1\). Conversely, these inequalities make every choice factor in the census strictly positive; the backward palette construction therefore exists. The least permitted alphabet has size \(q_*\), and the least available Boolean-pattern alphabet has size \(2^r\geq q_*\), giving the rank formula.

## Verification
Run the embedded standalone `VERIFY.py` using standard Python 3, with no dependencies. Its reported successful run was:

```
VERIFY_OK exhaustive_bisimulation_labelings 1035339 independent_complete_censuses 411 direct_modal_algebra_closures 5606 constructive_tail_formula_checks 3545 rank_feasibility_checks 411
```

The checker independently compares modal partition refinement against the criterion; enumerates all colorings for 411 small parameter cases and compares their totals with the product; explicitly closes generated Boolean modal algebras in 5,606 cases; evaluates the recursive tail formulas; and checks the positive-count rank boundary. It also samples larger chains. Those finite tests corroborate, but do not replace, the unrestricted proof.

## Relationship to prior work
Kurucz, Wolter and Zakharyaschev's publicly available 2023 work on interpolant existence in linear-frame logics develops bisimulation methods for linear chains of clusters. Its Lemma 2.4 gives the necessary per-cluster bound of at most \(2^r\) points in an \(r\)-generated descriptive frame, and Lemmas 2.5--2.6 concern definability of points and clusters under a finitely generated descriptive-frame hypothesis. Those results supply relevant theory but do not state the adjacent-palette criterion, exact generating-tuple product, or rank threshold with the possible extra color. These claims are about a fixed **full finite powerset** algebra and explicit given generators, not about interpolant existence or the general class of descriptive frames.

Kikot, Kurucz, Wolter and Zakharyaschev (2018) treat the strictly positive S4.3 fragment and its Kripke completeness and definability questions. That is a different fragment; only its published abstract could be inspected in the available access route, so a possible implicit antecedent remains a stated originality risk. General finite-model bisimulation and Boolean generation by singletons are standard tools, not new claims.

## Limitations
The classification is restricted to finite reflexive chains of complete clusters with one forward modality. No general lower bound matching \(h-1\) for defining depth is claimed here. Neither the originality search nor computational tests constitute an independent audit, formal proof certification, or exhaustive survey of unpublished work. Overlap with older modal-algebra or colored-word literature cannot be completely excluded.

## References
- A. Kurucz, F. Wolter, and M. Zakharyaschev, *A non-uniform view of Craig interpolation in modal logics with linear frames*, first public version 2023-12-10, arXiv:2312.05929, https://arxiv.org/abs/2312.05929. Full text examined particularly in Sections 2.2, 2.3 and the bisimulation framework.
- S. Kikot, A. Kurucz, F. Wolter, and M. Zakharyaschev, *On strictly positive modal logics with S4.3 frames*, Advances in Modal Logic 12 (2018), pp. 427–446, https://www.aiml.net/volumes/volume12/Kikot-Kurucz-Wolter-Zakharyaschev.pdf. Abstract and bibliographic description examined; full text could not be obtained during comparison.
