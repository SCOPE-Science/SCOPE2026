# Sharp height-three choice threshold for bundled modal witnesses

## Finding

Working in **ZF set theory**, consider the generated-neighborhood construction for unary bundle terms in Ding and Yang's propositional bundled semantics [1, Definitions 2.3--2.4 and 3.1]. The following three assertions form one sharp boundary theorem.

1. For every term with **relational modal nesting depth at most one**, the semantic truth-to-compatible-neighborhood direction of [1, Proposition 3.2] is provable in ZF, on every set-sized Kripke frame and for every valuation.
2. Fix the **single term** \(\tau=\Box\Diamond(+)\) and interpret both modalities over one reflexive, transitive, antisymmetric relation. Over ZF, the following assertion is equivalent to the **full axiom of choice**: on every nonempty rooted partial order of height at most three, if \(\tau\) is true at the root for a unary truth set \(P\), then a compatible member of its generated-neighborhood family exists.
3. On every rooted partial order of height at most two, that assertion for \(\tau\) is **already a theorem of ZF**.

Here height at most \(h\) means every strictly increasing chain has at most \(h\) elements. Consequently, both the relational nesting depth two and the rooted-frame height three in the choice-strength assertion are sharp. The result concerns **existence of a generated-neighborhood witness**, not ordinary Kripke truth, which has its usual recursive definition in ZF.

## Assumptions and scope

No choice principle is assumed in the base theory ZF. The underlying nonempty world set \(W\), its binary relation \(R\), and \(P\subseteq W\) are sets. In the language of [1], fix an index \(a\) of arity one distinct from the designated diagonal index, put \(R_a=R\), and use that index for both occurrences in \(\tau\). Other index relations required by [1] can be supplied independently; they do not occur in the term. Boolean connectives are interpreted by the designated diagonal indices as in [1].

For clarity, write terms using the equivalent grammar
\[
 t::=(+)\mid(-)\mid(t\wedge t)\mid(t\vee t)\mid\Box t\mid\Diamond t.
\]
Define relational modal depth \(d((+))=d((-))=0\), \(d(t\wedge s)=d(t\vee s)=\max\{d(t),d(s)\}\), and \(d(\Box t)=d(\Diamond t)=d(t)+1\). Its interpretation at \(w\) relative to \(P\) is the usual Boolean interpretation, with \((+)\) meaning \(w\in P\), \((-)\) meaning \(w\notin P\), \(\Box t\) quantifying universally over \(R[w]\), and \(\Diamond t\) existentially over \(R[w]\). 

For each term \(t\), the family \(\mathsf{Nbh}(w,t)\) consists of pairs of subsets of \(W\). For \((+)\) it is \(\{(\{w\},\varnothing)\}\); for \((-)\) it is \(\{(\varnothing,\{w\})\}\). For \(\vee\), take the union of the two families; for \(\wedge\), take coordinatewise unions of one pair from each family. For \(\Diamond t\), take the union of \(\mathsf{Nbh}(v,t)\) over \(v\in R[w]\). For \(\Box t\), take the set of coordinatewise unions of families \((X_v,Y_v)\in\mathsf{Nbh}(v,t)\), **one choice for every** \(v\in R[w]\). This last defining product is a set even when empty in ZF. A pair is compatible with \(P\) precisely when \(X\subseteq P\) and \(Y\subseteq W\setminus P\).

This is a restriction of the source's construction, not a new semantics. We denote semantic truth by \(S_t(w,P)\) and compatible-certificate existence by \(C_t(w,P)\).

## Proof

**Step 1 (soundness without choice).** By induction on \(t\), \(C_t(w,P)\Rightarrow S_t(w,P)\) holds in ZF. At a \(\Box\)-node a certificate is *defined* using an existing function on the successor set, so it supplies the necessary individual witnesses. At \(\Diamond\)- and Boolean nodes the corresponding witness is explicit. No new family of arbitrary choices is formed in this direction.

**Step 2 (depth at most one needs no choice).** For a depth-zero term \(u\), recursively list all elements of \(\mathsf{Nbh}(v,u)\) in a finite, syntactically ordered list: terminal terms have one entry, conjunction takes the finite Cartesian product of lists, and disjunction concatenates lists. There may be duplicate entries, which do not matter. A direct induction shows that \(S_u(v,P)\) is equivalent to the existence of a compatible entry on this finite list.

If \(S_{\Box u}(w,P)\) holds with \(d(u)=0\), then for each \(v\in R[w]\) the finite list for \(u\) contains a compatible entry. Choose **its least list index**, determined by \(v,P,u\), and collect the resulting pairs by Replacement; their coordinatewise union is a compatible certificate for \(\Box u\). No arbitrary choice function is invoked. If \(S_{\Diamond u}(w,P)\) holds, a single existential successor and the first compatible list entry suffice. An induction through finitely many outer Boolean nodes proves \(S_t\Rightarrow C_t\) for every \(d(t)\le1\). This argument does not assume that \(R\) is reflexive, transitive, serial, finite, or well orderable.

**Step 3 (the depth-two certificate is a selector).** Now let \(R=\le\) be a partial order with least element \(r\). Directly unfolding the above definitions gives
\[
 \mathsf{Nbh}(u,\Diamond(+))
 =\big\{(\{v\},\varnothing):u\le v\big\}.
\]
Since \(r\le u\) for all \(u\in W\), the outer \(\Box\) gives
\[
 C_{\Box\Diamond(+)}(r,P)
 \quad\Longleftrightarrow\quad
 \exists f:W\to P\ \forall u\in W\ (u\le f(u)). \tag{1}
\]
The function \(f\) is extracted from the choices appearing **inside the definition** of the generated family; conversely, any such \(f\) generates the compatible pair \((\operatorname{ran}(f),\varnothing)\). This equivalence is proved in ZF. In contrast, ordinary truth is
\[
 S_{\Box\Diamond(+)}(r,P)
 \quad\Longleftrightarrow\quad
 \forall u\in W\ \exists v\in P\ (u\le v). \tag{2}
\]
Thus the question is exactly when a family of nonempty upward witness sets admits a simultaneous selector.

**Step 4 (choice implies all height-three instances).** Under AC, choose \(f(u)\in P\cap\uparrow u\) from the nonempty sets supplied by (2). Then (1) holds. This works at every height, not only at height three.

**Step 5 (height-three instances imply full choice).** Work again in ZF. Let \(I\) be a nonempty set and \((A_i)_{i\in I}\) an arbitrary family of nonempty sets; the case \(I=\varnothing\) has the empty choice function. Form the three disjoint levels
\[
 W=\{r\}\ \sqcup\ \{m_i:i\in I\}\ \sqcup\ \{\ell_{i,a}:i\in I,\ a\in A_i\}.
\]
Give \(W\) the reflexive transitive order generated by \(r<m_i<\ell_{i,a}\), with no other strict comparabilities. This is a set-sized, rooted, height-three partial order, produced by Separation, Union and Replacement without choice. Put \(P=\{\ell_{i,a}:i\in I,a\in A_i\}\). Every leaf sees itself in \(P\), every middle point sees at least one leaf by nonemptiness of its own \(A_i\), and the root sees a leaf because \(I\ne\varnothing\). Hence (2) holds. Applying the asserted height-three certificate principle supplies \(f\) as in (1). For each \(i\), the only members of \(P\) above \(m_i\) are \(\ell_{i,a}\) with \(a\in A_i\). The unique \(a\) coded by \(f(m_i)\) defines a choice function \(i\mapsto a\) for the original family. As \(I\) and its members were arbitrary, AC follows. Together with Step 4 this proves ZF-equivalence.

**Step 6 (height two is choice-free).** Let \(W\) be any nonempty rooted partial order of height at most two and suppose (2). Every \(u\ne r\) is maximal, hence (2) at \(u\) forces \(u\in P\). Formula (2) at \(r\) supplies a single \(t\in P\). Define \(f(r)=t\) and \(f(u)=u\) for \(u\ne r\). Then (1) holds, with no choice. The contrast with Step 5 is sharp. ∎

## Verification

A standalone finite checker, `check_choice_height.py`, implements the unary generated-neighborhood families exactly for \(\Box\Diamond(+)\), evaluates (2) independently and checks compatibility of every enumerated neighborhood pair. It exhaustively tests the **51** rooted partial orders on labelled carriers of sizes one through five whose order respects the natural labelling and whose root is label zero (equivalently, all isomorphism types have a compatible listing), covering **1,414** valuations. All comparisons agree; the explicit height-two selector also passed every applicable test (`FINITE_VERIFY_OK`). Run with `python3 check_choice_height.py` using only Python's standard library.

**These finite experiments cannot establish the ZF-equivalence, the arbitrary-family construction, or independence of AC.** Those follow, to the extent stated, only from Steps 1--6.

## Relationship to prior work

Ding and Yang [1, Proposition 3.2] prove the semantic-to-generated-neighborhood implication **assuming AC**, and explicitly observe that AC is indispensable *for their proof*. Their argument uses choice at the universal branch of the certificate construction. The contribution here is the **reverse mathematical calibration**: a single fixed depth-two term forces full AC already over rooted partial orders of height three, while height two and every depth-one term are choice-free in ZF. The proof neither claims the original general representation result as new nor interprets proof-use alone as a logical necessity theorem.

Hansen, Kupke and Pacuit [2] study neighborhood semantics, bisimulations and model theory. The portions inspected are background on ordinary neighborhood models; they do not supply evidence of an earlier exact ZF/AC theorem for this particular generated-bundle construction. Related studies of weak forms of choice [3] concern choice principles as such, not this modal certificate. No claim of comprehensive literature uniqueness is made.

## Limitations

The theorem is a statement **over ZF** about when a particular certificate-existence implication can be proved; it does not say ordinary modal truth itself requires choice. The height comparison concerns rooted **partial orders**, not all frames and not arbitrary non-rooted finite-height preorders. The depth-one assertion uses a single unary non-diagonal accessibility relation with finite Boolean connectives as specified above. The fixed depth-two result already suffices for full AC but does not classify the exact strength of every other bundle term or every restricted branching class. Older equivalent formulations under the language of strategies, selections, or game semantics remain an originality risk. No independent external audit or proof-assistant certificate has been performed.

## References

[1] Y. Ding and Y. Yang, *A General Theory of Propositional Modal Bundled Modalities*, arXiv:2603.26268, first submitted 27 March 2026; especially v2, Definitions 2.3--2.4 and 3.1, Proposition 3.2, and Section 6. https://arxiv.org/html/2603.26268v2

[2] H. H. Hansen, C. Kupke, and E. Pacuit, *Neighbourhood Structures: Bisimilarity and Basic Model Theory*, Logical Methods in Computer Science 5(2:2), 2009, arXiv:0901.4430. https://arxiv.org/abs/0901.4430

[3] *Does DC Imply AC-omega, Uniformly?*, Journal of Symbolic Logic 90(4), 2025. https://doi.org/10.1017/jsl.2024.33
