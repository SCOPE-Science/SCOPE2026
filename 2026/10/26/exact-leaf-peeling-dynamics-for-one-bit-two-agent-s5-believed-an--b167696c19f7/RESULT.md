# Exact leaf-peeling dynamics for one-bit two-agent S5 believed announcements

## Finding

Fix two agents \(a,b\), one proposition \(p\), and the single modal-depth-one formula
\[
\psi=(p\land\Diamond_a\neg p\land\Diamond_b\neg p)\lor
(\neg p\land\Diamond_a p\land\Diamond_b p).
\]
In any finite initial \(\mathsf{S5}\) Kripke model in which each agent's equivalence classes have at most two worlds, form an edge-colored multigraph \(H\) by drawing an edge of color \(i\in\{a,b\}\) between the worlds in each two-point \(R_i\)-class **only when their truth values for \(p\) differ**. An edge may appear in both colors. Its components are alternating-color paths (singletons allowed) and alternating-color cycles (parallel two-edge cycles allowed).

Repeat the same **believed public announcement** of \(\psi\), deleting all arrows of both agents whose target does not satisfy \(\psi\) in the current model, without deleting worlds. Let \(s\) be the smallest \(t\geq0\) for which the updated model at time \(t+1\) equals that at time \(t\). Then
\[
s=\max\!\left(\{\lceil |V(P)|/2\rceil:P\text{ is a path component of }H\}\cup\{0\}\right).
\]
More precisely, every cycle component remains entirely as a set of accessible targets; on a path with vertices \(v_0,\ldots,v_{L-1}\) in order, the accessible target set at stage \(t\) contains exactly \(v_t,\ldots,v_{L-1-t}\) if \(2t<L\), and none otherwise. This is a complete exact description of the target-set dynamics on the stated class.

Consequently \(s\leq\lceil |W|/2\rceil\), sharply for every nonempty finite cardinality: take alternating two-point \(a\)- and \(b\)-classes along a path, and alternate the value of \(p\). Thus a **fixed one-variable modal-depth-one formula** has unbounded stabilization time on initially reflexive \(\mathsf{S5}\) models with two agents and binary information cells. No variable-free static modal formula on any initially \(\mathsf{S5}\) frame, and no purely propositional formula on any fixed-valuation model, can have such unbounded stabilization: each stabilizes within one update. These resource comparisons concern the same arrow-deleting announcement semantics.

## Assumptions and scope

A finite Kripke model is \(M=(W,R_a,R_b,V)\) with finite nonempty \(W\), valuation \(V(p)\subseteq W\), and each initial \(R_i\) an equivalence relation with all classes of cardinality at most two. Modal diamond has its usual existential successor semantics. Subsequent relations need not remain reflexive or serial. Define recursively \(M_0=M\) and
\[
R_i^{t+1}=\{(w,v)\in R_i^t : M_t,v\models\psi\}.
\]
Worlds and valuations never change; equality \(M_t=M_{t+1}\) means equality of both accessibility relations (and therefore the whole models). The first stabilization index counts strict updates before the first unchanged update; it can be zero.

For every \(t\), let \(S_0=W\), and recursively let \(S_{t+1}=S_t\cap\{v:M_t,v\models\psi\}\). The original reflexive arrows ensure each world is an initial possible target. No assumptions are made on connectedness or on the proportions of true and false \(p\)-worlds.

## Proof

**1. Common targets.** Induction on \(t\) gives \(R_i^t=R_i^0\cap(W\times S_t)\). At the base \(S_0=W\). Given the identity at \(t\), updating each original arrow removes precisely the targets failing \(\psi\) at that stage and gives the identity at \(t+1\). Since each original relation is reflexive, a strict change in \(S_t\) removes at least one self-arrow in both agents' relations, and different target sets give different models. Hence the first stabilized stage equals the first fixed point of \(S_t\).

**2. Opposite-truth partners.** At any world \(v\), the formula \(\psi\) holds exactly when, for each agent \(i\), an \(R_i^t\)-successor has the opposite value of \(p\) to \(v\). A class of size at most two has at most one such world, which exists precisely when \(H\) has the corresponding color-\(i\) edge at \(v\). Such an original neighbor is reachable at stage \(t\) precisely when it lies in \(S_t\). Thus
\[
S_{t+1}=\{v\in S_t: v\text{ has an }a\text{-edge neighbor and a }b\text{-edge neighbor in }S_t\}.
\]
This is simultaneous deletion of every vertex lacking at least one of the two edge colors. The intersection with \(S_t\) is essential: a previously removed target never reappears even if it later satisfies a different modal formula.

**3. Component structure.** At each vertex at most one edge of either color exists. Any connected component is therefore either a path, a cycle with alternating colors, or a single isolated vertex; parallel edges with both colors form a two-cycle. More explicitly, two consecutive edges of one color would put a vertex in an equivalence class of size at least three or violate unique pairing. Every non-endpoint of a path has both colors, because the two incident edges cannot share a color. Every path endpoint misses at least one color. Every cycle vertex has both colors.

**4. Exact iteration.** Since every cycle vertex has both-colored neighbors on that same cycle, all its vertices survive every step. On a path, the two endpoints are exactly the vertices deleted at the first step, and the remaining induced colored path has the same property. Induction removes one vertex at each end per round; the last singleton, if any, is removed in its own round. A path with \(L\) vertices therefore first becomes empty after \(\lceil L/2\rceil\) updates, and every preceding update removes at least one target. Taking the maximum over components proves the asserted exact stabilization formula and the upper bound.

**5. Sharp examples and resource boundary.** On \(W=\{0,\ldots,n-1\}\), make \(a\)-classes the adjacent pairs \(\{0,1\},\{2,3\},\ldots\) and \(b\)-classes \(\{1,2\},\{3,4\},\ldots\), with every unmatched endpoint a singleton class. Set \(p\) true on odd worlds. The colored graph is one alternating path of length \(n\), hence \(s=\lceil n/2\rceil\). For \(n=1\) the singleton model stabilizes after one arrow deletion, so the bound is also sharp.

A propositional formula's truth at each world depends only on the fixed valuation, so one announcement removes its initially false targets and the next announcement removes nothing further. For variable-free static modal formulas, every world of an initially \(\mathsf{S5}\) model satisfies exactly the same formulas: the universal relation \(W\times W\) is a bisimulation for the atom-free language, as every agent has some successor at every world. Thus such a formula is initially true everywhere, causing no deletion, or false everywhere, deleting all arrows at the first update; subsequent updates cannot restore arrows. This proves the two minimality statements without claiming that one agent and a single variable are universally sufficient for long transients.

## Verification

The accompanying `checker.py` independently constructs the two-agent equivalence relations using involutive partner maps, evaluates \(\psi\) by its modal semantics, executes the actual arrow-deletion update until stabilization, and compares the observed time with the predicted lengths of colored path components. It exhausts all labelled pairs of such partitions and all valuations of one atom on \(1\) through \(6\) worlds: respectively \(2,16,128,1600,21632,369664\) model/valuation combinations, totaling \(393042\). It also tests the sharp path construction at every size \(2\) through \(40\). All comparisons pass. The general claims follow from the proof, not from the finite census.

Run `python3 checker.py` with Python 3 and no external packages; expected terminal output ends in `ALL_CHECKS_OK`.

## Relationship to prior work

Yamada's September 2026 study of iterated believed public announcements provides the exact arrow-deletion update and studies eventual, strong-eventual, and transfinite stabilization properties on multi-agent \(\mathsf{K45}\) frames. Its Lemma 6 already bounds single-agent processes on \(k\) propositional letters by a valuation-type bound of \(2^k\); that single-agent fact is **prior work**, not asserted here as new. The earlier 2026 paper on classifications of \(\sigma\)-validity compares finite update truth patterns in multi-agent modal logics. A published result on finite believed announcements supplies a general sharp world-count bound using directed-cycle witnesses on arbitrary finite frames. None of these inspected statements gives the present exact colored-path/cycle dynamics or sharp half-world bound for two agents, one atom, a fixed formula and initial \(\mathsf{S5}\) binary information cells. The present proof uses elementary colored-graph pruning, which is not itself claimed new; the semantic classification and precise boundary in this natural modal fragment are the contribution.

## Limitations

The theorem is for a specific depth-one formula and initial \(\mathsf{S5}\) frames with every information cell of size at most two. It is **not** an upper bound for all announcements or arbitrary-size information cells. The resulting updated frames need not satisfy \(\mathsf{S5}\). The source on \(\sigma\)-validity was available only in abstract/secondary descriptions, leaving a priority risk for possible related claims in its full text; another older equivalently phrased two-color pruning result could also overlap. No independent audit has been conducted.

## References

- Eiji Yamada, *Eventual and Strong Eventual Notions in Public Announcements*, arXiv:2609.24006v1, first public preprint September 21, 2026, especially believed-announcement semantics, Lemma 6, and the discussion of multi-agent dynamics. https://arxiv.org/abs/2609.24006v1
- Eiji Yamada, *Classification of \(\sigma\)-validity*, arXiv:2607.04685 (2026). https://arxiv.org/abs/2607.04685
- H. van Ditmarsch and others, *The Ditmarsch Tale of Wonders* (background treatment of arrow-eliminating believed announcements; source text contains its Definition 6). https://www.researchgate.net/publication/252559847_The_Ditmarsch_Tale_of_Wonders
- *Sharp state-count stabilization bound for finite believed announcements*, 2026 public mathematical finding indexed by published-finding corpus (comparison to a general state-count theorem; present theorem specializes instead to a restrictive \(\mathsf{S5}\) class and identifies exact componentwise dynamics).
