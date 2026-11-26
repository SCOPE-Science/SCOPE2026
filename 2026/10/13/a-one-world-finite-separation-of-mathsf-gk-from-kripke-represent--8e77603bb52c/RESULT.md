# A one-world finite separation of \(\mathsf{GK}\) from Kripke representability

## Finding
In Nishimura's closure semantics there is a singleton closure frame satisfying \(\mathsf G\) and \(\mathsf K\), with empty generator at its sole world, and a valuation on it whose closure model fails \(\mathsf{KRep}\). The model is finite in the sense defined below. Since closure frames have a nonempty world set, one world is the minimum possible world cardinality. This counterexample uses a non-identity closure and so does not replace the source's identity-closure example.

## Assumptions and scope
A closure frame is \(\mathcal F=(W,G,\operatorname{cl})\), with \(W\ne\varnothing\), \(G:W\to\mathcal P(\mathbf{MF})\), and an arbitrary map \(\operatorname{cl}:\mathcal P(\mathbf{MF})\to\mathcal P(\mathbf{MF})\). A closure model adds a propositional valuation. It is finite when \(W\) and every raw generator \(G(w)\) are finite; the sets \(\operatorname{cl}(G(w))\) need not be finite. A modal formula \(\Box\chi\) holds at \(w\) precisely when \(\chi\in\operatorname{cl}(G(w))\).

Frame condition \(\mathsf G\) requires every formula valid on the underlying closure frame (true under every valuation at every world) to belong to \(\operatorname{cl}(G(w))\) for every \(w\). Frame condition \(\mathsf K\) requires \(\operatorname{cl}(G(w))\) to be closed under modus ponens for every \(w\). Both conditions concern the closure of the generator, not the raw generator. Property \(\mathsf{KRep}\) requires at every world \(w\) and for every formula \(\varphi\) that
\[
\varphi\in\operatorname{cl}(G(w))\quad\Longleftrightarrow\quad
\bigcap_{\psi\in\operatorname{cl}(G(w))}\llbracket\psi\rrbracket\subseteq\llbracket\varphi\rrbracket,
\]
where truth sets are taken under the model valuation.

## Proof
Define a two-valued evaluation \(b\) on formulas by setting \(b(\top)=1\) and \(b(p)=0\) for every propositional variable \(p\), using ordinary Boolean truth functions, and setting \(b(\Box\chi)=b(\chi)\). Let \(H=\{\varphi:b(\varphi)=1\}\). Take \(W=\{w\}\), \(G(w)=\varnothing\), and \(\operatorname{cl}(X)=H\) for every \(X\subseteq\mathbf{MF}\). The frame has one world and the sole raw generator is finite.

For \(\mathsf G\), let \(V_b\) assign false to every propositional variable at \(w\). A structural induction shows that \((\mathcal F,V_b),w\models\varphi\) if and only if \(b(\varphi)=1\). The Boolean cases follow by truth functionality. In the modal case, \(\Box\chi\) holds if and only if \(\chi\in H\), that is, if and only if \(b(\chi)=1\), the same as \(b(\Box\chi)=1\). In particular a frame-valid formula is true at this valuation, so it belongs to \(H=\operatorname{cl}(G(w))\). For \(\mathsf K\), if \(\varphi,\varphi\to\psi\in H\), Boolean modus ponens gives \(b(\psi)=1\); thus \(\psi\in H\).

For failure of \(\mathsf{KRep}\), let \(V_*\) instead make one variable \(p\) true at \(w\) (all others may remain false). By construction, \(p\notin H\) but \(\neg p\in H\). Since \(\neg p\) is false at the sole world under \(V_*\), the intersection of the truth sets of all formulas in \(H\) is empty. It is therefore contained in \(\llbracket p\rrbracket\), although \(p\notin\operatorname{cl}(G(w))\). This violates \(\mathsf{KRep}\). The nonempty-world requirement makes the bound of one world sharp.

## Verification
The argument uses the definitions of finiteness, modal truth, frame conditions \(\mathsf G\) and \(\mathsf K\), and \(\mathsf{KRep}\) in [1]. Finiteness concerns \(W\) and \(G(w)\), not the size of the closure value \(H\). No finite search or computational certificate is needed.

## Relationship to prior work
Nishimura proves that \(\mathsf{KRep}\) implies \(\mathsf G\) and \(\mathsf K\), and exhibits a counterexample to the converse on \(W=\mathbb N\) with identity closure and cofinite truth-set generators. The singleton counterexample isolates failure within the source's class of finite closure models. It also exhibits the distinction between frame validity and truth in a chosen model: a valuation used to test frame validity may differ from the model valuation tested for representability.

## Limitations
The constant map \(X\mapsto H\) is monotone and idempotent. It is not extensive, since \(p\in\{p\}\) while \(p\notin\operatorname{cl}(\{p\})=H\), and it is not the identity. This construction therefore makes no separation claim with extensivity or the identity imposed.

## References
1. Yuki Nishimura, “Closure Semantics for Weak Modal Logics: Completeness and Representations,” arXiv:2610.01433v1, 1 October 2026. Definitions 2.2–2.3, Definition 2.5 and Figure 1, Definition 4.22, Lemma 4.23 and Example 4.24.
