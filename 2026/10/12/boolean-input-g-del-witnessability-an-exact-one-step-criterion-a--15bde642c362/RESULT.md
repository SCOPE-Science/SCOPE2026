# Boolean-input Gödel witnessability: an exact one-step criterion and a depth-two obstruction

## Finding

Let \(F=(W,R)\) be an arbitrary nonempty fuzzy Gödel Kripke frame, where \(R:W\times W\to[0,1]\). A **Boolean-input valuation** sends each propositional variable at each world to \(0\) or \(1\), but modal formulas are evaluated in the full Gödel algebra \([0,1]\). A modal occurrence is **witnessed** when the infimum defining a box or the supremum defining a diamond is attained by one of the worlds in \(W\); zero-accessibility worlds are included in the defining infimum/supremum.

For \(w\in W\), let \(G_w=\{R(w,u):u\in W,\ R(w,u)>0\}\). The following conditions are equivalent:

1. For every Boolean-input valuation, at every world, each modal subformula of every formula of modal depth at most one is witnessed.
2. For every Boolean-input valuation and every world, \(\Diamond p\) is witnessed, where \(p\) is one fixed propositional variable.
3. Every nonempty subset of \(G_w\) has a greatest element, for every \(w\in W\); equivalently, the positive values in every accessibility row are reverse well-ordered by their usual real order.

**The one-step characterization does not compose.** There is a countably infinite acyclic fuzzy Gödel frame of directed height two satisfying (3), in which each accessibility row has at most **one distinct positive weight** and the set of all positive edge weights is reverse well-ordered, together with a Boolean-input valuation for which \(\Box\Diamond p\) at a designated root equals \(0\) but none of its defining terms equals \(0\). Thus depth two is the first possible modal depth for failure on this frame. Moreover, the witnessed-logic schema \(\Box\neg\neg\alpha\to\neg\neg\Box\alpha\), with \(\alpha=\Diamond p\), has value \(0\) at the root.

## Assumptions and scope

All statements use ordinary real-valued infima and suprema, Gödel conjunction \(a\wedge b=\min(a,b)\), disjunction \(a\vee b=\max(a,b)\), and residuum \(a\Rightarrow b=1\) if \(a\le b\), otherwise \(b\). The modal clauses are

\[
 e(w,\Box\varphi)=\inf_{u\in W}\bigl(R(w,u)\Rightarrow e(u,\varphi)\bigr),\qquad
 e(w,\Diamond\varphi)=\sup_{u\in W}\min\{R(w,u),e(u,\varphi)\}.
\]

No reflexivity, seriality, transitivity, cardinality bound, or fixed global range restriction is imposed. Modal depth is the maximum number of nested modal operators; Boolean-input does not mean that derived modal formula values stay Boolean. The witnessing notion here is exactly **attainment** in the displayed clauses, including empty positive-support rows: since \(W\ne\varnothing\), every such row has box value \(1\) and diamond value \(0\), both attained through zero-weight terms. The countable example has precisely the nodes and edges specified below and no others.

## Proof

**(1) implies (2).** The single formula \(\Diamond p\) is of modal depth one.

**(2) implies (3).** Fix \(w\in W\) and suppose some nonempty \(T\subseteq G_w\) has no greatest element. Assign \(p\) the Boolean value \(1\) exactly at worlds \(u\) with \(R(w,u)\in T\), and \(0\) elsewhere. At \(w\), the set of diamond contributions is \(T\) together with at most the value \(0\), so its supremum is \(s=\sup T>0\). Since \(T\) lacks a greatest element, no contribution equals \(s\); hence \(\Diamond p\) is not witnessed. This contradicts (2).

**(3) implies (1).** At each world, a modal-free formula \(\alpha\) has value in \(\{0,1\}\) under a Boolean-input valuation, by induction through \(\wedge,\vee,\Rightarrow,\bot\). A box contribution \(R(w,u)\Rightarrow e(u,\alpha)\) therefore belongs to \(\{0,1\}\). Its infimum is attained because the set of contributions is a nonempty subset of \(\{0,1\}\). For the diamond, the contributions are \(0\) or \(R(w,u)\); the set of positive contributions is either empty, in which case every contribution is \(0\), or is a nonempty subset of \(G_w\), hence has a greatest element by (3). In either case its supremum is attained. This applies to every modal occurrence in every formula of modal depth at most one, including occurrences inside propositional combinations.

**Sharp depth-two obstruction.** Put

\[
W=\{r\}\cup\{a_n,b_n:n\in\mathbb N,\ n\ge1\},
\]

and define the only positive accessibility values by

\[
R(r,a_n)=1,\qquad R(a_n,b_n)=\frac1{n+1}\qquad(n\ge1).
\]

Assign \(e(b_n,p)=1\) for all \(n\ge1\), and \(e(r,p)=e(a_n,p)=0\). All other atomic letters may be assigned \(0\). Each row has either no positive weight or exactly one distinct positive weight. The **global** positive-weight set is \(\{1\}\cup\{1/(n+1):n\ge1\}\), every nonempty subset of which has a greatest member (choose the least index when the subset omits \(1\)). Thus (3) holds, and all one-step modalities are witnessed under **every** Boolean-input valuation.

Yet the only positive contribution to \(e(a_n,\Diamond p)\) comes from \(b_n\), giving

\[
e(a_n,\Diamond p)=\frac1{n+1}>0.
\]

For the outer box at \(r\), the contribution of \(a_n\) is \(1\Rightarrow 1/(n+1)=1/(n+1)\), and every other world's contribution equals \(1\), since its accessibility weight from \(r\) is zero. It follows that

\[
e(r,\Box\Diamond p)=\inf\bigl(\{1/(n+1):n\ge1\}\cup\{1\}\bigr)=0,
\]

but all defining contributions are strictly positive: the infimum is not attained. The directed positive-edge graph is an acyclic tree of height two, so no deeper modal structure is involved.

Finally, \(e(a_n,\neg\neg\Diamond p)=1\) for every \(n\ge1\), whence \(e(r,\Box\neg\neg\Diamond p)=1\); on the other hand, \(e(r,\neg\neg\Box\Diamond p)=0\). Gödel implication thus gives the stated value \(0\) for the indicated witness schema. Since (1) holds, the depth-two failure is minimal in modal depth. The construction uses a countable infinity of worlds; every finite Gödel model is witnessed because the two indexing sets of extrema are finite and nonempty.

## Verification

A standalone exact-rational Python script, `verify.py`, computes the restrictions to the first \(N\) branches for \(N\in\{1,2,3,4,8,16,32,64,128\}\) using the full Gödel modal clauses, and obtains \(e_N(r,\Box\Diamond p)=1/(N+1)\) and \(e_N(r,\Box\neg\neg\Diamond p)=1\). It separately checks one-step finite prefixes of a row with increasing weights \(n/(n+1)\), which approach \(1\) without an attaining member in the infinite row. The test reports `VERIFY_OK`. These finite calculations do **not** establish nonattainment in infinite models; that conclusion follows from the displayed infinite sequences and exact proof above. Run using `python3 verify.py` (standard library only).

## Relationship to prior work

Ferrari, Fiorentini, Giardini, and Rodriguez (2026) define fuzzy Gödel modal witnessedness by attained infima/suprema and prove a terminating refutation procedure and the finite model property for the logic of witnessed models. Their exhibited nonwitnessed model uses infinitely many fuzzy truth degrees. The theorem here instead classifies *frames guaranteeing one-step attainment for all Boolean atomic valuations* and proves that this local guarantee fails at modal depth two, even with only one positive weight per row.

Ferrari, Fiorentini, and Rodriguez (2025) study witnessed **crisp** accessibility, where Boolean-input formula values remain Boolean at every modal depth. Bílková, Frittella, and Kozhemiachenko (2022) give frame-definability results for finite branching in a related but distinct two-component paraconsistent Gödel logic. Those results describe different valuations or semantics and do not entail the row-by-row reverse-well-order characterization or the depth-two example. These statement-level distinctions are essential; no claim of a comprehensive uniqueness certificate is made.

## Limitations

The equivalence concerns Boolean **atomic** valuations and modal depth one, not arbitrary fuzzy atomic valuations or the full modal language. The depth-two example shows failure of compositional witnessability but is not a classification of frames that guarantee witnesses for all depths. Reverse well-ordering is a condition on every subset of each positive-weight set, not merely existence of a greatest value in each whole row. The example assumes ordinary classical set theory and countably many worlds. No finite experiment proves the infinite assertion. Older equivalent formulations, especially in fuzzy Kripke semantics under other terminology, remain a literature risk. This work establishes mathematical consequences of the specified semantics but does not independently audit the cited papers.

## References

1. M. Ferrari, C. Fiorentini, P. Giardini, and R. O. Rodriguez, *A Gödel Modal Logic Over Witnessed Models*, EPTCS 447 (2026), pp. 355–373, arXiv:2606.31906, DOI: 10.4204/EPTCS.447.20. Earliest arXiv posting: 2026-06-30. Full text inspected at https://www.researchgate.net/publication/408180835_A_Godel_Modal_Logic_Over_Witnessed_Models.
2. M. Ferrari, C. Fiorentini, and R. O. Rodriguez, *A Gödel Modal Logic over Witnessed Crisp Models*, in TABLEAUX 2025, Lecture Notes in Computer Science 15980 (2025), pp. 141–160, DOI: 10.1007/978-3-032-06085-3_8. Open full text at https://link.springer.com/chapter/10.1007/978-3-032-06085-3_8.
3. M. Bílková, S. Frittella, and D. Kozhemiachenko, *Paraconsistent Gödel Modal Logic*, in IJCAR 2022, Lecture Notes in Computer Science 13385 (2022), pp. 429–448, DOI: 10.1007/978-3-031-10769-6_26. Open full text at https://link.springer.com/chapter/10.1007/978-3-031-10769-6_26.
