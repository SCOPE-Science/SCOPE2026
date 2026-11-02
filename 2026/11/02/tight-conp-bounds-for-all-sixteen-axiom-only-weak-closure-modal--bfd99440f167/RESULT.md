# Tight coNP bounds for all sixteen axiom-only weak closure modal logics

## Finding
For every subset \(\Lambda\subseteq\{\mathsf M,\mathsf C,\mathsf N,\mathsf K\}\), consider the least uniform-substitution-closed extension of classical propositional logic by the indicated modal axiom schemes, **without** replacement of equivalents or necessitation as inference rules. The formula-validity problem is \(\mathrm{coNP}\)-complete and the formula-satisfiability problem is \(\mathrm{NP}\)-complete. All sixteen systems, including the one with all four schemes, admit a linear-size certificate of propositional modal atom truth values and polynomial-time checking via Horn closure.

## Assumptions and scope
Modal formulas are finite parse trees built using ordinary Boolean connectives and \(\Box\). Implication and conjunction may be taken as primitive Boolean connectives or canonically expanded abbreviations: the four **syntactic** closure rules must be applied consistently to the chosen presentation. Let the schemes be

\[\begin{aligned}
\mathsf M&:\ \Box(\alpha\land\beta)\to(\Box\alpha\land\Box\beta),\\
\mathsf C&:\ (\Box\alpha\land\Box\beta)\to\Box(\alpha\land\beta),\\
\mathsf N&:\ \Box\top,\\
\mathsf K&:\ (\Box(\alpha\to\beta)\land\Box\alpha)\to\Box\beta.
\end{aligned}\]

The semantics is that of closure frames with arbitrary formula-set generation \(G(w)\) and an operation \(\operatorname{cl}\), where \(w\models\Box\psi\) iff \(\psi\in\operatorname{cl}(G(w))\). No extensive, monotone or idempotent assumption is imposed on general closure frames. By Nishimura's soundness and strong completeness theorem, these are precisely the logics \(L_\Lambda\); the canonical rule-generated closure defined below is an admissible closure operator for each indicated set of schemes. Formula satisfiability means existence of some closure model and world satisfying the formula. Complexity is measured in length of the formula; the chosen \(\Lambda\) is fixed.

## Proof
**Finite subformula Horn condition.** Let \(\varphi\) be the input formula. Let \(S\) contain \(\top\), and the complete syntactic subformula sets of every formula \(\psi\) immediately under an occurrence of \(\Box\) in \(\varphi\). Thus \(|S|\leq |\varphi|+1\). For each \(\sigma\in S\) introduce a Boolean bit \(b_\sigma\) recording generated membership. Impose exactly the following Horn implications whenever their displayed formulas belong to \(S\):

- If \(\mathsf N\in\Lambda\), impose \(b_\top=1\).
- If \(\mathsf M\in\Lambda\), impose \(b_{\alpha\land\beta}\Rightarrow b_\alpha\) and \(b_{\alpha\land\beta}\Rightarrow b_\beta\).
- If \(\mathsf C\in\Lambda\), impose \(b_\alpha\land b_\beta\Rightarrow b_{\alpha\land\beta}\).
- If \(\mathsf K\in\Lambda\), impose \(b_{\alpha\to\beta}\land b_\alpha\Rightarrow b_\beta\).

There is at most one set of constant-many clauses per syntactic binary connective in \(S\). Separately choose truth bits for the propositional atoms of \(\varphi\), and evaluate the full input Boolean syntax normally but replace each \(\Box\psi\) by \(b_\psi\).

**Necessity.** Given a satisfying closure model, set \(b_\sigma=1\) exactly when \(\sigma\in\operatorname{cl}(G(w))\); assign the propositional bits according to the valuation at \(w\). The four required semantic closure conditions entail all corresponding Horn clauses, and recursive evaluation gives truth of \(\varphi\).

**Sufficiency.** Suppose those finite bits exist and put \(H=\{\sigma\in S:b_\sigma=1\}\). Take one world, set \(G(w)=H\), and use the least closure \(\operatorname{cl}_\Lambda\) generated on all modal formulas by exactly the selected rules: from a conjunction project its two parts (M), form conjunctions from two premises (C), adjoin \(\top\) (N), or infer the consequent of an available implication from its antecedent (K). Crucially,
\[\operatorname{cl}_\Lambda(H)\cap S=H.\]
Here is the finite-support argument. A derivation of a member of \(S\) can be normalized by eliminating any projection of a conjunction just formed by C; that projection merely repeats one of the two earlier premises. Every remaining conjunction decomposition tracks a subformula of a formula already available, and every implication used by K must ultimately occur as a subformula of an initial member of \(H\), because none of M, C, or N introduces a new implication-head expression and K only extracts a consequent. All such relevant expressions lie in the subformula-closed set \(S\). Likewise a conjunction formed by C that is subsequently used as a K antecedent belongs to \(S\), because it is a subformula of the implication used; irrelevant extra conjunctions can be discarded. Hence membership in \(S\) is generated exactly by the restricted Horn rules, under which \(H\) is closed. The reverse inclusion holds by extensivity of this particular generated closure. The resulting one-world model has precisely the guessed truth values for every boxed subformula, so it satisfies \(\varphi\).

**Complexity.** A witness assigns \(O(|\varphi|)\) bits, each Horn constraint and Boolean gate check takes polynomial time, and the full formula can be evaluated in polynomial time. Thus satisfiability is in \(\mathrm{NP}\) for every \(\Lambda\), and validity belongs to \(\mathrm{coNP}\). Propositional formulas without boxes provide uniform many-one reductions from ordinary Boolean satisfiability and tautology, respectively. Modal axioms cannot alter their satisfiability because arbitrary propositional valuations are realized in one-world closure models. This proves the matching lower bounds.

## Verification
The accompanying standalone `checker.py` constructs the finite Horn closures and compares their intersection with bounded direct derivations of the four global generation rules on 1,568 small cases across all sixteen scheme subsets. It also checks basic modal-axiom consequences and satisfiable/unsatisfiable examples. The output is `ALL_CHECKS_OK`. These bounded tests illustrate the syntactic normal-form argument; the complexity theorem is proved by the preceding unrestricted reasoning and the established one-world completeness theorem, not by enumeration.

## Relationship to prior work
Nishimura (2026, Sections 2–3) introduced these closure frames and established soundness, strong completeness, one-world finite-model constructions and primitive-recursive decidability for exactly the sixteen rule-free combinations. This finding sharpens that decision bound to the optimal standard complexity classes using a uniform finite Horn certificate; it does **not** claim a new completeness theorem. Kudinov and Rybakov (2025) proved coNP results for familiar non-normal systems E, EM, EN and EMN which **include replacement of equivalents**; those statements do not cover the independent sixteen axiom-only systems, especially the combinations containing K. Kogure and Kurahashi (2026) study closure semantics in provability logics with modal inference rules and arithmetical completeness, rather than the present finite-certificate complexity classification.

## Limitations
This statement concerns ordinary formula validity and satisfiability, not uniform consequence from unbounded premises, addition of RE/Gen, frame-size complexity for arbitrary explicitly represented closures, or fixed-variable fragments. Priority beyond the identified papers may be affected by older abstract-consequence or weak-modal complexity literature under different terminology; an independent audit has not been performed.

## References
1. Y. Nishimura, *Closure Semantics for Weak Modal Logics: Completeness and Representations* (2026), arXiv:2610.01433v1, especially Definitions 3.7–3.8 and Corollaries 3.13–3.14; first posted 2026-10-01.
2. A. Kudinov and M. Rybakov, *Complexity of the variable-free fragments of non-normal modal logics* (2025), arXiv:2507.09136v1. Its systems include replacement of equivalents and are distinct from the rule-free systems here.
3. H. Kogure and T. Kurahashi, *Modal logics of conjunctively closed provability predicates* (2026), arXiv:2607.08730v1, especially Sections 2–3 on closure semantics and provability-oriented systems.
