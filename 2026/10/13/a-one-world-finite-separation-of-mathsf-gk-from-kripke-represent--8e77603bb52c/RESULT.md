# A one-world finite separation of \(\mathsf{GK}\) from Kripke representability
## Finding
In Nishimura's closure semantics, the implication from conditions \(\mathsf G\) and \(\mathsf K\) to Kripke representability \(\mathsf{KRep}\) already fails on a finite closure model with exactly one world and an empty generator. Explicitly, there is a singleton closure frame satisfying \(\mathsf G\) and \(\mathsf K\) and a valuation on it whose closure model fails \(\mathsf{KRep}\). Since closure frames are required to have a nonempty world set, one world is the minimum possible world cardinality for such a counterexample. The construction uses a constant, generally non-identity closure, so it does not replace the source's stronger identity-closure counterexample along that separate axis.

## Assumptions and scope
Work in the closure semantics of Nishimura, where a closure frame is \(\mathcal{F}=(W,G,\operatorname{cl})\), with nonempty \(W\), a generator \(G:W\to\mathcal{P}(\mathbf{MF})\), and an unrestricted map \(\operatorname{cl}:\mathcal{P}(\mathbf{MF})\to\mathcal{P}(\mathbf{MF})\). A closure model adds a propositional valuation. A model is finite when \(W\) and every \(G(w)\) are finite. Condition \(\mathsf G\) requires every formula valid on the underlying closure frame to belong to every generated set; condition \(\mathsf K\) requires each generated set to be closed under modus ponens. Property \(\mathsf{KRep}\) requires, at every world \(w\) and formula \(\varphi\),
\[
\varphi\in\operatorname{cl}(G(w))
\quad\Longleftrightarrow\quad
\bigcap_{\psi\in\operatorname{cl}(G(w))}\llbracket\psi\rrbracket
\subseteq\llbracket\varphi\rrbracket.
\]
No claim is made here under the additional restriction that \(\operatorname{cl}\) be the identity.

## Proof
Define a two-valued map \(b\) on modal formulas recursively. Put \(b(\top)=1\), put \(b(p)=0\) for every propositional variable \(p\), use the ordinary Boolean truth functions for negation and implication, and put
\[
b(\Box\varphi)=b(\varphi).
\]
Let \(H=\{\varphi:b(\varphi)=1\}\). Take \(W=\{w\}\), \(G(w)=\varnothing\), and define the closure to be the constant map
\[
\operatorname{cl}(X)=H
\]
for every \(X\subseteq\mathbf{MF}\). This is a finite closure frame in the source's sense because the world set and the sole generator are finite.

First verify \(\mathsf G\). Let \(V_b\) be the valuation on the singleton world satisfying \(w\in V_b(p)\) exactly when \(b(p)=1\); with the present choice of \(b\), all propositional variables are false. A structural induction gives
\[
(\mathcal{F},V_b),w\models\varphi
\quad\Longleftrightarrow\quad b(\varphi)=1.
\]
The Boolean cases are immediate. In the modal case,
\[
(\mathcal{F},V_b),w\models\Box\chi
\Longleftrightarrow
\chi\in H
\Longleftrightarrow
b(\chi)=1
\Longleftrightarrow
b(\Box\chi)=1.
\]
If \(\mathcal{F}\models\varphi\), then in particular \((\mathcal{F},V_b),w\models\varphi\), so \(b(\varphi)=1\) and therefore \(\varphi\in H=\operatorname{cl}(G(w))\). Thus \(\mathsf G\) holds.

Next verify \(\mathsf K\). If \(\varphi\in H\) and \(\varphi\to\psi\in H\), then \(b(\varphi)=b(\varphi\to\psi)=1\). Classical truth functionality forces \(b(\psi)=1\), hence \(\psi\in H\). Thus \(\mathsf K\) holds.

Finally choose one propositional variable \(p\) and a model valuation \(V_*\) with \(V_*(p)=W\). Since \(b(p)=0\), we have \(p\notin H\) and \(\neg p\in H\). But \(\neg p\) is false at the sole world under \(V_*\), so
\[
\bigcap_{\psi\in H}\llbracket\psi\rrbracket_{(\mathcal{F},V_*)}=\varnothing.
\]
Consequently the right-hand side of \(\mathsf{KRep}\) is true for \(\varphi=p\), because the empty set is contained in \(\llbracket p\rrbracket\), while its left-hand side is false because \(p\notin H\). Hence \((\mathcal{F},V_*)\) is not Kripke-representable.

The source definition requires \(W\neq\varnothing\), so no counterexample can use fewer than one world. The world-cardinality bound is therefore sharp.

## Verification
The proof was checked directly against the source definitions of closure frame, finite closure model, conditions \(\mathsf G\) and \(\mathsf K\), and \(\mathsf{KRep}\). The only induction is on formula complexity and uses no unproved external lemma. The construction has one world and generator \(G(w)=\varnothing\); the closure itself is allowed to have an infinite image because the source's finiteness definition constrains the world set and generators, not the image of \(\operatorname{cl}\).

## Relationship to prior work
Nishimura proves that \(\mathsf{KRep}\) implies \(\mathsf G\) and \(\mathsf K\), and gives a counterexample to the converse on \(W=\mathbb{N}\) with the identity closure and cofinite truth-set generators. The present construction establishes a different sharp boundary: the converse already fails among finite closure models and at the minimum possible number of worlds. It trades away the source example's identity-closure feature by using a constant closure. Searches for the exact finite or singleton strengthening, its separation formulation, and aliases involving Kripke-representable closure models did not locate a published statement of this sharpening.

## Limitations
This result does not show that a one-world or finite counterexample exists when the closure is required to be the identity, monotone, extensive, or idempotent. In particular, it does not subsume the source's identity-closure example. It is a minimal-world separation result inside the unrestricted closure semantics defined in the source.

## References
1. Yuki Nishimura, “Closure Semantics for Weak Modal Logics: Completeness and Representations,” arXiv:2610.01433v1, 1 October 2026. See Definition 2.2 for closure models and finiteness, Definition 2.5 for \(\mathsf G\) and \(\mathsf K\), Definition 4.22 for \(\mathsf{KRep}\), Lemma 4.23, and Example 4.24.
