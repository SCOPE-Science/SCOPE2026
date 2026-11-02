# A height-two identifiability theorem for four intuitionistic modal operators

## Finding

For any **nonempty preorder** \((W,\leq)\), the four modal operations of Balbiani and Gencer, considered simultaneously on *all upsets* of \(W\), determine every binary accessibility relation \(R\subseteq W\times W\) uniquely **if and only if** \((W,\leq)\) is a partial order having no strict chain with three distinct points. No finiteness or accessibility-frame condition is assumed.

This conclusion is sharp in another sense: even for the two-point chain, no three of the four operations determine all accessibility relations. The proof supplies explicit one-step atomic valuations reconstructing each edge and explicit indistinguishable relation pairs for every obstruction.

## Assumptions and scope

A preorder means a nonempty set \(W\) with a reflexive and transitive relation \(\leq\). An *upset* is \(U\subseteq W\) satisfying \(x\in U\) and \(x\leq y\) implies \(y\in U\). The input \(R\subseteq W\times W\) is arbitrary, including nonserial, nonconfluent relations. Define the four operators on the complete lattice \(\operatorname{Up}(W)\) by

\[
\begin{aligned}
D_R(U)&=\{s:\exists t\leq s\ \exists u\in U\ (tRu)\},\\
B_R(U)&=\{s:\forall t\geq s\ \forall u\ (tRu\Rightarrow u\in U)\},\\
E_R(U)&=\{s:\forall t\geq s\ \exists u\in U\ (tRu)\},\\
F_R(U)&=\{s:\exists t\leq s\ \forall u\ (tRu\Rightarrow u\in U)\}.
\end{aligned}
\]

These are, in order, the Přenosil diamond, the usual intuitionistic box, the Wijesekera diamond, and its dual box from the cited semantics. Their values are upsets. For a fixed \((W,\leq)\), write \(\Phi(R)=(D_R,B_R,E_R,F_R)\), with equality meaning *pointwise equality of all four functions for every upset*, not merely equality of valid formulas or equivalence up to relabeling.

The height condition is: there are no three pairwise distinct points \(a,b,c\) with \(a<b<c\), where \(a<b\) abbreviates \(a\leq b\) and \(b\not\leq a\).

## Proof

**Sufficiency and an explicit inverse.** Suppose \(\leq\) is antisymmetric and has height at most two. Each point is minimal or maximal (possibly both). To recover an arbitrary edge \(sRv\), choose an upset according to the *target* \(v\):

* If \(v\) is maximal, \(U_v=\{v\}\) is an upset. If \(s\) is minimal, the only predecessor of \(s\) is \(s\), so
  \[
  sRv\quad\Longleftrightarrow\quad s\in D_R(U_v).
  \]
  If \(s\) is maximal, the only successor of \(s\) is \(s\), hence
  \[
  sRv\quad\Longleftrightarrow\quad s\in E_R(U_v).
  \]
* If \(v\) is minimal, \(U_v=W\setminus\{v\}\) is an upset. If \(s\) is minimal, then
  \[
  sRv\quad\Longleftrightarrow\quad s\notin F_R(U_v).
  \]
  If \(s\) is maximal, then
  \[
  sRv\quad\Longleftrightarrow\quad s\notin B_R(U_v).
  \]

When a point is both minimal and maximal, either applicable branch works; choose the maximal-target branch for such a target and the minimal-source branch for such a source. Each test is the truth of a *one-step modality* applied to an atom valued at the indicated upset. Therefore \(\Phi(R)=\Phi(R')\) implies \(sRv\Longleftrightarrow sR'v\) for every ordered pair, proving injectivity without any finiteness assumption.

**Failure of antisymmetry.** Suppose \(a\ne b\) and \(a\leq b\leq a\). Every upset contains \(a\) precisely when it contains \(b\). Choose any \(s_0\in W\), put \(R(s_0)=\{a\}\), \(R'(s_0)=\{b\}\), and make all other successor rows empty. For every upset \(U\) and every row \(t\), the two predicates
\[
R(t)\cap U\ne\varnothing,\qquad R(t)\subseteq U
\]
are unchanged when \(R\) is replaced by \(R'\). Each of the four displayed modal clauses is obtained from these row predicates using quantification over predecessors or successors. Hence \(\Phi(R)=\Phi(R')\) although \(R\ne R'\).

**Failure at a strict three-point chain.** Suppose \(a<b<c\). Choose \(s_0\in W\), set \(R(s_0)=\{a,c\}\), \(R'(s_0)=\{a,b,c\}\), and make all other rows empty. For every upset \(U\), membership of \(b\) forces membership of \(c\), so the rows meet \(U\) simultaneously; membership of \(a\) forces membership of \(b\), so the rows are contained in \(U\) simultaneously. All rowwise existential and universal tests therefore agree. Consequently \(\Phi(R)=\Phi(R')\) with \(R\ne R'\). This settles necessity for all preorders.

In both obstruction constructions, the propositional and co-implicational operations depend only on the unchanged preorder. By induction over formulas, *every formula in the full four-modal language* has the same truth set under the two relations for every common upset valuation. The claim is stronger than a coincidence of one-step observations on these witnesses, but it is not a claim that arbitrary differing relations must have identical frame-validity theories.

**Each of the four operations is necessary even on two worlds.** Fix \(W=\{0,1\}\) and \(0<1\). The following pairs of relations, specified by their complete successor rows \((R(0),R(1))\), have equal operators except at the named omitted coordinate:

| Omitted operation | First relation's rows | Second relation's rows |
| --- | --- | --- |
| \(D\) | \((\{0\},\varnothing)\) | \((\{0,1\},\varnothing)\) |
| \(B\) | \((\varnothing,\{1\})\) | \((\varnothing,\{0,1\})\) |
| \(E\) | \((\{1\},\{0\})\) | \((\{1\},\{0,1\})\) |
| \(F\) | \((\{1\},\{0\})\) | \((\{0,1\},\{0\})\) |

The full upset lattice here is exactly \(\{\varnothing,\{1\},W\}\), so direct evaluation on those three inputs checks the statement completely. In each row the omitted operation differs on some upset, and all three retained operations agree on every upset. A smaller set of operations cannot distinguish more than a triple containing it, proving necessity of the entire quartet in this minimal nontrivial setting.

## Verification

The included standalone `checker.py` evaluates the original four quantified clauses, rather than implementing the derived inverse formula as the definition of the operators. Execute `python3 checker.py` with standard Python 3, without third-party dependencies.

It exhaustively classifies all preorders on one, two, and three labelled points and every accessibility relation on each. The number of preorders and the number with injective four-operator signatures are respectively \((1,1)\), \((4,3)\), and \((29,13)\). It checks every edge-recovery formula for each height-at-most-two poset in those classes. It verifies all four indispensability witnesses on the two-point chain, the hidden-middle-edge example on the three-point chain, injectivity for all \(65{,}536\) relations on one four-point branching height-two poset, and three-chain obstructions across every four-point poset containing a three-point chain. The execution result was `ALL_CHECKS_OK`.

Finite exhaustive tests are *not* relied on to infer the universal quantifiers over arbitrary infinite preorders; those are established by the constructive proof above. No external or independent audit has been performed.

## Relationship to prior work

Balbiani and Gencer introduced the four operators and studied their noninterdefinability, correspondence and axiomatizations. Their Propositions 20–21 analyze eliminability and their Proposition 26 already supplies a nonantisymmetric, modally indistinguishable frame pair. Those facts are prior input, not new findings here. Přenosil developed compatibility principles relating distributive modal operations to common accessibility relations, which should not be confused with injectivity of the *specific* four-operator presentation on a fixed preorder.

An earlier finite-chain observational-fiber calculation determined exact finite-chain profiles and counts. In particular, its failure of injectivity on chains of length at least three and its faithful one- and two-point cases are **not new consequences claimed here**. The present classification quantifies over all finite and infinite nonempty preorders, including branching partial orders and nonantisymmetric preorders, and supplies the structural height-two reconstruction by all four operations together with the explicit minimality-of-four witnesses. A finite-chain normal form alone does not cover branching order types.

The related results in general modal relation saturation and canonical relational representations may yield reformulations; a negative search cannot establish historical priority.

## Limitations

The four-operator map is tested on *all persistent valuations* and observed at *all labelled worlds*. The result does not assert reconstruction from valid formulas alone, from one fixed valuation, from finite observations on infinite worlds, or under observational quotienting by frame isomorphism. No accessibility properties such as confluence or seriality are imposed; restricting \(R\) to a smaller class can alter the identifiability boundary and the necessity of four coordinates. The height-two condition concerns the given order, not any unknown accessibility relation. Independent historical-priority verification remains outstanding, particularly for equivalent formulations in distributive modal algebra.

## References

1. P. Balbiani and Ç. Gencer, *Four intuitionistic modal connectives*, arXiv:2606.07348, first arXiv submission June 5, 2026, https://arxiv.org/abs/2606.07348. The same work was publicly announced in a March 2, 2026 seminar: https://lirica.lis-lab.fr/.
2. A. Přenosil, *Compatibility between modal operators in distributive modal logic*, arXiv:2311.10017, first submission November 16, 2023, https://arxiv.org/abs/2311.10017.
3. Prior finite-chain observational-fiber calculation, *Four-modal observational fibers on finite intuitionistic chains* (unpublished research note; no public bibliographic identifier asserted).
