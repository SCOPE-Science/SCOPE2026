# Finite-world model-relative normality and exact Kripke representation census

## Finding
For every finite-world closure model, two **model-relative** normality conditions completely determine same-world Kripke representability. Moreover, the entire set of representing relations has a product description and a closed enumeration:
\[
\#\{R:\text{all modal truths are preserved}\}=
\prod_{w\in W}\prod_{T\in K_w/\sim}(2^{|T|}-1).
\]
The least and greatest edge counts among these relations are \(\sum_w|K_w/\sim|\) and \(\sum_w|K_w|\). This is a result about finite **world sets**, whether or not the closure generator has a finite presentation.

## Assumptions and scope
Fix a nonempty finite set \(W\), any propositional vocabulary, valuation \(V\), and closure-model interpretation \(\mathcal M=(W,G,\mathrm{cl},V)\). No algebraic restrictions are imposed on \(\mathrm{cl}\). Write \(H_w=\mathrm{cl}(G(w))\), \(\llbracket\theta\rrbracket=\{v\in W:\mathcal M,v\models\theta\}\). The semantics for \(\Box\theta\) is \(\theta\in H_w\), with ordinary classical propositional connectives.

We require precisely:

**(U), model-relative globality:** for every \(w\) and formula \(\theta\), if \(\llbracket\theta\rrbracket=W\), then \(\theta\in H_w\).

**(MP), local detachment:** for every \(w\) and \(\alpha,\beta\), if \(\alpha,\alpha\to\beta\in H_w\), then \(\beta\in H_w\).

In particular, (U) is **not** Nishimura's frame-relative condition (G), which only involves validity under all valuations on a fixed closure frame. Replacing (U) by (G) is not justified here.

Let \(u\sim v\) iff every modal formula has the same truth value at \(u\) and \(v\); each equivalence class is a modal truth type. Define
\[
K_w=\bigcap_{\theta\in H_w}\llbracket\theta\rrbracket,
\]
with the intersection over the empty family understood as \(W\).

## Proof
**Necessity.** If a relation \(R\) preserves the truth of every modal formula pointwise, then \(\theta\in H_w\) exactly when \(R[w]\subseteq\llbracket\theta\rrbracket\). This immediately implies (U). If both \(\alpha\) and \(\alpha\to\beta\) contain every successor, so does \(\beta\); hence (MP).

**Finite-intersection step.** Assume (U) and (MP). For each \(w\), the set \(H_w\) is closed under finite conjunction: the propositional tautology \(\alpha\to(\beta\to(\alpha\land\beta))\) is true at all worlds, hence belongs to \(H_w\) by (U); two uses of (MP) produce the conjunction. The same argument works for an arbitrary finite family, with the empty conjunction \(\top\) supplied by (U).

Since \(W\) is finite, there exist finitely many formulas \(\gamma_1,\ldots,\gamma_t\in H_w\) such that \(K_w=\bigcap_{i=1}^t\llbracket\gamma_i\rrbracket\). To see this, for each \(v\notin K_w\) choose one \(\gamma_v\in H_w\) false at \(v\). If \(K_w\subseteq\llbracket\theta\rrbracket\), then the implication \((\gamma_1\land\cdots\land\gamma_t)\to\theta\) is true at all worlds and so belongs to \(H_w\). Applying (MP) after forming the conjunction gives \(\theta\in H_w\). Conversely, \(\theta\in H_w\) certainly implies \(K_w\subseteq\llbracket\theta\rrbracket\). Thus, for every formula,
\[
\theta\in H_w\quad\Longleftrightarrow\quad K_w\subseteq\llbracket\theta\rrbracket.\tag{1}
\]

**Existence.** Put \(wRv\) exactly when \(v\in K_w\). Prove by induction on formula complexity that \((W,R,V),v\models\theta\) iff \(\mathcal M,v\models\theta\) for all \(v\). Boolean cases are immediate; for \(\Box\theta\), use the induction hypothesis and (1).

**All relations.** Finiteness of \(W\) ensures that every modal type \(T\) is definable by a single formula \(\delta_T\): for each of finitely many other types choose a formula true on \(T\) and false there, and conjoin. Consequently \(K_w\), an intersection of formula truth sets, is a union of modal types. A row \(S\subseteq W\) has precisely the same modal universal theory as \(K_w\) iff it contains no world outside \(K_w\) and meets each modal type lying inside \(K_w\). For necessity, the conjunction of the finitely many \(\gamma_i\) defining \(K_w\) excludes outside worlds. If a type \(T\subseteq K_w\) is missed, \(\neg\delta_T\) is true on \(S\) but not on \(K_w\). For sufficiency, a formula's truth is constant on each type, so \(S\subseteq\llbracket\theta\rrbracket\) iff \(K_w\subseteq\llbracket\theta\rrbracket\).

These choices are independent between rows. For each type \(T\subseteq K_w\), there are exactly \(2^{|T|}-1\) nonempty subsets of \(T\). Multiplication proves the census. One or all vertices per included type respectively achieve the minimum and maximum number of edges. When \(K_w=\varnothing\), its unique allowed successor set is empty. This completes the proof.

## Verification
The independent standalone script `checker.py` refines modal types by successor-color partition stabilization and compares all alternative relations with a separate joint-refinement modal-equivalence test. It covered 2,742 finite baseline models, including 1,310,720 exhaustive three-world alternative comparisons and 46,592 sampled four-world comparisons; all passed. In a three-world model with one singleton type and a two-element type, each world must have a nonempty subset of the two-element type as successors, giving exactly \(3^3=27\) representations, with between three and six edges. These finite tests validate instances of the census; they do not prove the universal closure-model statement.

## Relationship to prior work
Nishimura's *Closure Semantics for Weak Modal Logics* (arXiv:2610.01433, first public version 1 October 2026) introduces (G), (K), and the general semantic consequence closure (KRep) in Section 4.3, proving equivalence between (KRep) and a same-world Kripke representation. The present finite-world result identifies the **different, model-relative (U)** as exactly the additional finite-world requirement alongside (K) and enumerates **all** representations, including minimum and maximum edge costs. The cited result does not state this finite-world equivalence or census. Standard Hennessy–Milner and bisimulation contraction theory explains modal types of Kripke models but does not itself give the closure-model finite normality equivalence. General-frame compactness theory supplies related background, not an exact enumeration for the closure models studied here.

## Limitations
This does **not** prove the analogous (U)+(MP) criterion on arbitrary infinite world sets. The source paper's cofinite-model example satisfies model-relative (U) and (MP) yet fails (KRep), exhibiting the genuine loss of finite-intersection compactness. The enumeration counts **labelled binary relations on the fixed original world set**, not quotient frames or isomorphism classes. The logical vocabulary may be infinite; finiteness is required only of the world set. This has not undergone independent validation. Bisimulation literature may contain an equivalent representation census under different terminology.

## References
1. Yuki Nishimura, *Closure Semantics for Weak Modal Logics: Completeness and Representations*, arXiv:2610.01433v1 (1 October 2026), especially Definitions 2.5 and 4.22, Example 4.24 and Theorem 4.30; latest inspected revision v2 (13 October 2026).
2. Thomas Bolander and Alessandro Burigana, *Better Bounded Bisimulation Contractions*, arXiv:2405.00480 (2024), abstract and bibliographic record consulted as background.
3. Nick Bezhanishvili and Tim Henke, *A model-theoretic approach to descriptive general frames: the van Benthem characterization theorem*, Journal of Logic and Computation 30 (2020), 1331–1355, DOI:10.1093/logcom/exaa040, introduction and compactness discussion.
