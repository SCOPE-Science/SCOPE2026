# Exact finite-frame correspondence for antecedent disjunction in flat Heyting–Lewis implication

## Finding
Let \(F=(W,\preceq,R)\) be any nonempty **finite** flat frame, where \(\preceq\) is a preorder and \(R\) is an arbitrary binary relation. Write
\[
H_x=\uparrow R[x]=\{u\in W:\exists t\ (xRt\land t\preceq u)\},\qquad \uparrow v=\{u:v\preceq u\}.
\]
Then the following are equivalent.

**(i)** The flat strict implication validates the antecedent-disjunction law under every persistent valuation:
\[
\mathsf{di}:\quad ((p\mathbin{\rightsquigarrow}r)\wedge(q\mathbin{\rightsquigarrow}r))\to((p\vee q)\mathbin{\rightsquigarrow}r).
\]
Here \(\to\) is intuitionistic implication and \(\rightsquigarrow\) denotes the flat strict conditional.

**(ii)** The following relational **principal-cover condition** holds:
\[
\tag{PC}
\begin{aligned}
&\forall w,x,u\in W\quad
 [w\preceq x\ \land\ u\in H_x]\\
&\qquad\Longrightarrow\quad
\exists v,y\in W\quad
 [v\in H_x\ \land\ w\preceq y\ \land\ u\in H_y
 \ \land\ H_y\subseteq\uparrow v].
\end{aligned}
\]
This is a first-order condition in the original two relations: \(u\in H_x\) means \(\exists t(xRt\land t\preceq u)\), while \(H_y\subseteq\uparrow v\) means \(\forall t(yRt\Rightarrow v\preceq t)\).

Consequently, finite-frame validity of \(\mathsf{di}\) can be decided in \(O(|W|^5)\) time and \(O(|W|^2)\) space using Boolean relation matrices. Condition (PC) properly extends the published sufficient condition that every \(R[x]\) be downward directed: a three-world fork satisfies (PC) despite having a nondirected row, and three worlds are the smallest possible size for this separation.

## Assumptions and scope
A *persistent valuation* sends each propositional variable to an upset of the preorder. For formula truth sets \(A,B\) that are upsets, flat strict implication is interpreted by
\[
w\Vdash \varphi\rightsquigarrow\psi
\iff \forall x\succeq w\,[R[x]\subseteq A\Longrightarrow R[x]\subseteq B].
\]
No upward-flat assumption, antisymmetry, seriality, transitivity of \(R\), or nonempty-row assumption is imposed. Empty rows contribute no points to the unions below. The finite size assumption is used for the finite-join decomposition of arbitrary upsets into principal upsets; no assertion about infinite frames is made.

## Proof
For every world \(w\) and upset \(A\), define an upset-valued operator
\[
I_w(A):=\bigcup\{H_x:w\preceq x,\ H_x\subseteq A\}.
\]
The operator is monotone and contractive: \(I_w(A)\subseteq A\). As \(B\) is an upset, the truth clause above is equivalent to
\[
w\Vdash\varphi\rightsquigarrow\psi\iff I_w(A)\subseteq B.
\tag{1}
\]
Indeed \(R[x]\subseteq A\) iff \(H_x\subseteq A\), and similarly for \(B\).

Fix \(w\). The two premises of \(\mathsf{di}\) hold at \(w\) exactly when \(I_w(A)\cup I_w(B)\subseteq C\), while its strict-implication conclusion holds there exactly when \(I_w(A\cup B)\subseteq C\). All three sets are upsets. Since \(I_w\) is monotone, \(I_w(A)\cup I_w(B)\subseteq I_w(A\cup B)\). Thus choosing \(C=I_w(A)\cup I_w(B)\) when strict containment occurs proves that validity of \(\mathsf{di}\) under all valuations is equivalent to
\[
I_w(A\cup B)=I_w(A)\cup I_w(B)
\quad\text{for all } w\in W,\ A,B\in\operatorname{Up}(W).
\tag{2}
\]
The intuitionistic outer implication does not change this global condition: its validity at every world is equivalent to the absence of a counterexample at any world, because \(w\preceq w\).

Assume (2). Any upset \(A\) in a finite frame is a finite union of principal upsets, \(A=\bigcup_{v\in A}\uparrow v\). By (2) and \(I_w(\varnothing)=\varnothing\),
\[
I_w(A)=\bigcup_{v\in A}I_w(\uparrow v).
\tag{3}
\]
Given \(w\preceq x\) and \(u\in H_x\), the definition supplies \(I_w(H_x)=H_x\). Applying (3) to \(A=H_x\), obtain some \(v\in H_x\) with \(u\in I_w(\uparrow v)\). Unpacking the latter gives \(y\succeq w\) with \(u\in H_y\subseteq\uparrow v\), proving (PC).

Conversely assume (PC). For an arbitrary upset \(A\), if \(u\in I_w(A)\) there is \(x\succeq w\) with \(u\in H_x\subseteq A\). Condition (PC) gives \(v\in H_x\subseteq A\) and \(y\succeq w\) with \(u\in H_y\subseteq\uparrow v\). Hence \(u\in I_w(\uparrow v)\); the reverse inclusion is immediate by monotonicity. Therefore (3) holds, and splitting the index set for \(A\cup B\) proves (2). Thus (i) and (ii) are equivalent.

For strictness, take three vertices \(w,a,b\), with \(w\preceq a\), \(w\preceq b\), \(a,b\) incomparable, and no additional strict comparisons. Set \(R[w]=\{a,b\}\), \(R[a]=\{a\}\), \(R[b]=\{b\}\). The two singleton successor rows recover the two principal upsets inside \(H_w=\{a,b\}\), so (PC) is immediate for all \(w\preceq x\). Nevertheless \(R[w]\) has no lower bound in itself for \(a,b\). On at most two worlds, either the preorder compares the worlds (making every nonempty row downward directed), or they are incomparable; in the latter case a nondirected row is the two-element row, and (PC) fails because the only future world of its source is itself. Thus the three-point separation is minimal.

For complexity, compute all matrices \(H_x\) and \(\uparrow v\), together with the Boolean subset table \([H_y\subseteq\uparrow v]\), in \(O(n^3)\) time. Inspect all \(O(n^3)\) triples \((w,x,u)\) in the antecedent of (PC), testing at most \(n^2\) witness pairs \((v,y)\) per triple using the precomputed table. This costs \(O(n^5)\) time and \(O(n^2)\) stored Boolean data.

## Verification
Run `python3 verify_di.py` from the directory containing this document and the standalone checker. The checker constructs every preorder and every directed relation on one, two, and three labelled vertices, enumerates **all** persistent valuations of \(p,q,r\), and compares direct semantic validity of \(\mathsf{di}\) with (PC) and with the intermediate union identity (2). It also tests the three-point fork independently. Observed results: \(1,4,29\) preorders and \(2,64,14848\) total frames at sizes one, two, and three; \(2,57,9528\) validate \(\mathsf{di}\), respectively. The checker reports `VERIFY_OK` after checking all \(14914\) frames. This finite enumeration is a cross-check of the proof, not a proof for all finite sizes.

## Relationship to prior work
De Groot and Litak, *Relational Semantics for Flat Heyting-Lewis Logic* (2026), define this precise semantics in Definition 3.1, prove invariance under upward saturation in Proposition 3.10, and give pointwise downward-directedness as a sufficient condition for \(\mathsf{di}\) in Lemma 3.12. The principal-cover condition above is instead necessary and sufficient on finite frames, applies without an upward-flat restriction, and admits frames outside that sufficient subclass. Earlier work of Litak and Visser on constructive strict implication studies related axioms and sharp-style relational models rather than this exact finite flat-frame correspondence. The conditional Esakia semantics of Dufty and de Groot uses antecedent-indexed relations and likewise does not provide the present criterion for a single fixed \(R\).

## Limitations
The equivalence is established only for **finite** nonempty preordered carriers. The generic distributivity law is not claimed to have the same first-order correspondent over arbitrary infinite frames. The verification census stops at three worlds; it does not substitute for the all-size symbolic argument. The literature comparison cannot exclude every differently phrased older result in relational or algebraic logic.

## References
1. J. de Groot and T. Litak, *Relational Semantics for Flat Heyting-Lewis Logic*, arXiv:2603.28402, first version March 30, 2026; *Electronic Proceedings in Theoretical Computer Science* **447** (2026), 445–463, DOI:10.4204/EPTCS.447.25. In particular Definition 3.1, Proposition 3.10, Lemma 3.12.
2. T. Litak and A. Visser, *Lewis meets Brouwer: Constructive strict implication*, *Indagationes Mathematicae* **29** (2018), 36–90, DOI:10.1016/j.indag.2017.10.003.
3. B. Dufty and J. de Groot, *Filling in the semantics for intuitionistic conditional logic*, arXiv:2508.11972 (2025).
