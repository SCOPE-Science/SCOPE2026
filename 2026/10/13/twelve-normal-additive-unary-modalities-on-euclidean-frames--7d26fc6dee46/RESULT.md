# Twelve normal additive unary modalities on Euclidean frames

## Finding

Let \(\mathsf{K5}\) denote normal propositional modal logic over the class of all Euclidean Kripke frames, with arbitrary (possibly infinite, nonserial, nontransitive) accessibility relations. In its one-variable language, precisely **twelve** equivalence classes of formulas \(A(p)\) are both normal and additive, meaning the following equivalences are valid on every Euclidean frame:
\[
A(\bot)\leftrightarrow\bot,\qquad
A(p\lor q)\leftrightarrow A(p)\lor A(q).
\]
Define \(E_0(p)=H_0(p)=B_0(p)=\bot\), and
\[
E_1(p)=p\land\Box\bot,\qquad H_1(p)=p\land\Diamond\top,\qquad
B_1(p)=\Diamond p,\qquad B_2(p)=\Diamond^2p.
\]
A complete irredundant list is
\[
\Phi_{\epsilon,\alpha,j}(p)=E_\epsilon(p)\lor H_\alpha(p)\lor B_j(p),
\quad (\epsilon,\alpha,j)\in\{0,1\}\times\{0,1\}\times\{0,1,2\}.
\]
Every such formula is in fact **completely additive** on every Euclidean frame: its induced operation commutes with arbitrary unions, including the empty union. Thus binary additivity plus normality collapses to complete additivity for unary, parameter-free \(\mathsf{K5}\) formulas.

More generally, the one-generated free modal algebra of \(\mathsf{K5}\) contains exactly \(2^{12}=4096\) elements: there are exactly twelve possible pointed one-variable truth signatures, each definable by a one-variable modal formula.

## Assumptions and scope

A Euclidean frame is \(F=(W,R)\) with \(W\ne\varnothing\) and \(xRy\land xRz\Rightarrow yRz\) for all worlds \(x,y,z\). A valuation \(P\subseteq W\) assigns \(p\) to precisely \(P\); Boolean connectives, \(\Box\), and \(\Diamond\) have ordinary Kripke semantics. A formula with no variables besides \(p\) is permitted to contain negation, arbitrary modal nesting, and Boolean constants. Equivalence means agreement under every valuation at every world of every Euclidean frame. Additivity uses a fresh variable \(q\), all valuations, and the displayed equivalence; neither finiteness of a frame nor any stronger frame conditions are assumed.

For a world \(r\), put \(C=R(r)\). If \(C\ne\varnothing\), put \(T=R^2(r)\), the set of worlds reached in two steps. For a nonempty set \(X\) and valuation \(P\), write \(s_X=1\) if \(X\cap P\ne\varnothing\), and \(a_X=1\) if \(X\subseteq P\). Otherwise the respective bit is \(0\).

## Proof

**1. Euclidean cluster lemma.** If \(C\ne\varnothing\), then \(C\subseteq T\), \(T\ne\varnothing\), and \(R(x)=T\) for every \(x\in T\). Indeed, for any \(y,z\in C\), Euclideanness gives \(yRz\); in particular \(yRy\). Mutual accessibility \(yRz,zRy\) implies \(R(y)=R(z)\), since each successor of one is, by Euclideanness, a successor of the other. Denote their common successor set by \(T\); thus \(T=R^2(r)\supseteq C\). For \(t\in T\), choose \(y\in C\) with \(yRt\). Since \(yRy\), Euclideanness gives \(tRy\), so \(R(t)=R(y)=T\). This reasoning uses no cardinality restriction.

**2. Twelve exhaustive pointed signatures.** Within \(T\), by induction on an arbitrary one-variable formula \(\psi\), its truth at \(x\in T\) depends only on \((1_{x\in P},s_T,a_T)\): the assertion is immediate for \(p\) and the constants, Boolean connectives preserve it, and quantification over the common complete successor set \(T\) needs only the existence of \(p\)-true and \(p\)-false points of \(T\). At a root with \(C\ne\varnothing\), a second structural induction shows that the truth of \(\psi\) depends only on
\[
(1_{r\in P},s_C,a_C,s_T,a_T).
\]
For the modal induction step, the truth of the inner formula at any \(c\in C\) depends only on \(1_{c\in P}\) and the shared \((s_T,a_T)\), so quantifying over \(C\) requires only \((s_C,a_C)\).

As \(\varnothing\ne C\subseteq T\), the ordered quadruple \((s_C,a_C,s_T,a_T)\) takes precisely these five possible patterns:
\[
(0,0,0,0),\quad (0,0,1,0),\quad (1,0,1,0),\quad
(1,1,1,0),\quad (1,1,1,1).
\]
Each occurs at the distinguished root \(r\) of the five-world frame \(G\) whose worlds are \(\{r,c_1,c_2,u_1,u_2\}\), where \(R(r)=C=\{c_1,c_2\}\) and \(R(x)=T=\{c_1,c_2,u_1,u_2\}\) for every \(x\in T\). The root's \(p\)-value can be assigned independently, giving ten serial-root signatures. If \(C=\varnothing\), every modality is vacuous at \(r\), leaving just the two cases \(p(r)=0,1\). Hence every one-variable formula has one of \(2^{12}\) truth tables on the twelve pointed signatures.

All twelve pointed signatures are distinguished by the six modal tests
\[
p,\qquad \Diamond\top,\qquad\Diamond p,\qquad\Box p,
\qquad\Diamond^2p,\qquad\Box^2p.
\]
At a serial root these reveal, respectively, \(1_{r\in P}\), seriality, \(s_C\), \(a_C\), \(s_T\), and \(a_T\); at a dead end, only \(p(r)\) varies. By taking Boolean conjunctions of tests or their negations, any individual signature is definable. Disjunctions therefore realize every subset of the twelve signatures; exactly \(4096\) equivalence classes of unrestricted one-variable formulas occur.

**3. The additive classification.** Let \(A(p)\) be normal and binary-additive on all Euclidean frames. Fix the root of \(G\) and define \(g(P)=1\) iff \(A(p)\) is true there under the valuation \(P\subseteq G\). Normality and additivity imply \(g(\varnothing)=0\) and \(g(P\cup Q)=g(P)\lor g(Q)\). Since \(G\) is finite, \(g(P)\) is the disjunction of the values on singleton subsets. Automorphisms interchanging \(c_1,c_2\) and interchanging \(u_1,u_2\) show that for some \(\alpha,\beta,\gamma\in\{0,1\}\),
\[
g(P)=(\alpha\land 1_{r\in P})\lor
(\beta\land 1_{P\cap C\ne\varnothing})\lor
(\gamma\land 1_{P\cap(T\setminus C)\ne\varnothing}).
\]
Valuations \(P=\{c_1\}\) and \(P'=\{c_1,u_1\}\) have the **same** six-test signature at \(r\); Step 2 forces \(g(P)=g(P')\), hence \(\gamma\le\beta\). The three possibilities \((\beta,\gamma)=(0,0),(1,0),(1,1)\) give, at a serial root, the three modal contributions \(\bot,\Diamond p,\Diamond^2p\), respectively, since \(C\subseteq T\). The coefficient \(\alpha\) controls \(p(r)\) independently; thus the six serial-root possibilities coincide with \(H_\alpha\lor B_j\).

On a one-world dead-end frame, normality forces the only two possible outputs \(\bot\) or \(p\), captured by \(E_\epsilon\). By Step 2, agreement on the ten signatures of \(G\) and the two dead-end signatures implies agreement on **every** Euclidean model. Therefore \(A(p)\) equals one of the twelve displayed forms.

**4. Converse, distinctness, and complete additivity.** Each displayed form preserves arbitrary unions because \(P\mapsto P\cap X\) for a fixed set \(X\), \(P\mapsto R^{-1}[P]\), and their compositions and finite pointwise unions do so. The fixed sets associated with \(\Box\bot\) and \(\Diamond\top\) do not depend on \(P\). Hence all twelve forms are normal and completely additive. Their triple \((\alpha,j)\) is distinguished at the root of \(G\) by singleton valuations at \(r,c_1,u_1\); the remaining bit \(\epsilon\) is distinguished at a dead-end world. There are exactly twelve, with no duplicates.

## Verification

Run `python3 verify.py` using Python 3 standard library. The script enumerates every accessibility relation with one through four worlds, selects all Euclidean frames, and checks the twelve normality/additivity identities for every valuation and every pair of valuations. It tests their distinctness on the five-world witness, all twelve pointed signatures, and all \(4096\) Boolean functions on those signatures against normality/additivity on the witness. It also checks several families of nested modal formulas for signature compatibility. Actual output: `VERIFY_OK`; \(354\) Euclidean frames, \(5240\) one-variable valuations, \(12\) admissible unary operations. The infinite-frame theorem is proved in Steps 1–4; finite exhaustion alone would not establish it.

## Relationship to prior work

Dvorkin's *On Interpretations of Normal Modal Logics* (arXiv:2606.31871, published with the EPTCS proceedings on June 29, 2026 (separate arXiv submission June 30)), especially Sections 2–6 and Corollary 4.6, classifies normal additive formulas for five logics: \(\mathsf K\), \(\mathsf{GL}\), \(\mathsf{Grz}\), \(\mathsf{S4}\), and \(\mathsf{S5}\). It gives exactly three classes \(\bot,p,\Diamond p\) in \(\mathsf{S5}\), but does not state the twelve-class result for the larger class of Euclidean \(\mathsf{K5}\)-frames. His general \(\mathsf K\)-classification does not on its own establish that **every** \(\mathsf{K5}\)-additive formula is equivalent on Euclidean frames to a \(\mathsf K\)-additive one; this is supplied by the current cluster/signature argument. Shapirovsky's *The one-variable fragment of a non-locally tabular modal logic can be finite* (2018 lecture, slides 6–7) notes that \(\mathsf{K5}\) is locally tabular; finiteness alone does not give the exact \(4096\) count or classify the normal additive operators.

## Limitations

The characterization is **parameter-free and monomodal**; it does not classify formulas with fixed additional propositional parameters, polymodal languages, or arbitrary frames outside the Euclidean class. The exact \(4096\) count concerns a **single propositional variable** and is not a claim about the size of all finitely generated free \(\mathsf{K5}\) algebras. Completeness is semantic over all Euclidean Kripke frames. Prior coverage under alternative algebraic presentations of one-generated free modal algebras remains a literature risk; exact external originality has not been independently certified.

## References

1. L. V. Dvorkin, *On Interpretations of Normal Modal Logics*, arXiv:2606.31871 (arXiv submission June 30, 2026; EPTCS proceedings publicly dated June 29, 2026); DOI: 10.4204/EPTCS.447.18. https://arxiv.org/abs/2606.31871; https://cgi.cse.unsw.edu.au/~eptcs/all.cgi
2. I. Shapirovsky, *The one-variable fragment of a non-locally tabular modal logic can be finite*, ToLo VI presentation (2018), slides 6–7 on local tabularity of \(\mathsf{K5}\). https://www.sambuz.com/doc/the-one-variable-fragment-of-a-non-locally-tabular-modal-presentation-823200
