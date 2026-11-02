# A root-type filtration proves finite models for mixed classical-intuitionistic necessity

## Finding

Let \(\varphi\) be a formula of the intuitionistic propositional modal language with one unary \(\Box\), and let \(\Sigma=\operatorname{Sub}(\varphi)\) have \(s\ge1\) distinct subformulas. Every pointed concrete mixed model in the sense of van der Giessen–Joosten–Mayaux–Navarro Arroyo admits a finite pointed concrete mixed model agreeing on the truth of every formula in \(\Sigma\) at the chosen point. The finite model has at most \(2^s\) outer worlds, at most \(2^s\) local intuitionistic worlds per outer world, and at most \(2^{2s}\) local worlds in total.

Together with the previously established completeness of \(\mathsf{iK}+\mathsf{bem}\) for concrete mixed models, this proves the finite model property of that logic. A non-theorem has a countermodel with at most \(2^{2s}\) local worlds. In particular theoremhood is decidable and belongs to \(\mathrm{coNEXPTIME}\) under the standard formula encoding. No matching lower complexity bound is claimed.

## Assumptions and scope

Work in ordinary classical metamathematics. An outer frame is any nonempty set \(W\) with arbitrary \(R\subseteq W^2\). For each \(w\in W\), a disjoint nonempty rooted intuitionistic Kripke model \(M_w=(X_w,\le_w,V_w)\) consists of a poset with root \(r_w\le_w x\) for every \(x\in X_w\) and persistent propositional valuation. For \(x\in X_w\), propositional connectives use intuitionistic forcing in \(X_w\), while
\[
 x\Vdash\Box\psi\quad\Longleftrightarrow\quad
 \forall v\in W\ (wRv\Longrightarrow r_v\Vdash\psi).
\]
Thus every \(\Box\)-formula is constant throughout each local component. Negation abbreviates implication to falsity. Constants \(\top\) and \(\bot\) behave as usual; no primitive diamond is used. The models may initially have arbitrary cardinalities.

## Proof

**1. Finite root signatures.** Fix an outer world \(w_0\) containing the distinguished point \(x_0\). For each original local point \(x\), define its \(\Sigma\)-type
\[
 t(x)=\{\theta\in\Sigma:x\Vdash\theta\}.
\]
Persistence gives \(x\le_w y\Rightarrow t(x)\subseteq t(y)\). All points in one component agree on which \(\Box\)-formulas belong to their type. Give outer \(w\) its root signature \(\rho(w)=t(r_w)\). There are at most \(2^s\) distinct root signatures. Choose one original component \(w_t\) for every occurring signature \(t\), taking \(w_{\rho(w_0)}=w_0\) so that the distinguished local point survives.

**2. Filter each chosen local component.** In \(M_{w_t}\), replace points by their distinct types \(u=t(x)\). Order the resulting types by set inclusion. This is a partial order with least element \(\rho(w_t)=t\), because the original root lies below all local points. Declare atom \(p\) true at \(u\) exactly when \(p\in u\), for atoms appearing in \(\Sigma\); unused atoms may be false. Atom persistence follows from inclusion. Each filtered component has at most \(2^s\) points.

**3. Finite outer accessibility.** For each selected signature \(t\), and each modal subformula \(\Box\psi\in\Sigma\) with \(\Box\psi\notin t\), choose one original successor \(v\) of \(w_t\) whose root falsifies \(\psi\). Such a successor exists by the original modal semantics. Put the edge \(tR'\rho(v)\) in the new outer frame. Put in no other edges. There are finitely many choices, and every target \(\rho(v)\) is among the selected signatures. If \(\Box\chi\in t\), every selected successor of \(w_t\) originally forces \(\chi\) at its root, hence the representative root with the same signature also has \(\chi\in\rho(v)\). Conversely, each absent \(\Box\psi\) has its designated counterexample edge.

**4. Simultaneous truth lemma.** By induction on \(\theta\in\Sigma\), a filtered point \(u\) in the component indexed by \(t\) forces \(\theta\) exactly if \(\theta\in u\). Atoms, constants, conjunction and disjunction are immediate. For implication \(\alpha\to\beta\): if it belongs to \(u\), then it belongs to every \(z\supseteq u\), and at every original representative of \(z\) the semantic implication plus the truth of \(\alpha\) forces \(\beta\); the induction hypothesis proves the filtered implication. If it does not belong to \(u\), take an original representative point of type \(u\) and an original extension witnessing failure, where \(\alpha\) holds and \(\beta\) fails. Persistence ensures that extension has type \(z\supseteq u\), which is retained and witnesses failure in the filtered component. For \(\Box\psi\), membership is constant across the chosen local component and equals membership in its root signature \(t\). Step 3 gives exactly the right successor-root truth values, with the induction hypothesis applicable at the selected target roots. Therefore the modal clause is preserved. This proves the induction.

The type \(t(x_0)\) occurs in the chosen component \(w_0\). Select its corresponding filtered point as the new distinguished point. The truth lemma preserves all of \(\Sigma\), including \(\varphi\). Counting root signatures and local signatures gives the stated bounds.

**5. Logical consequence.** The cited primary paper proves that \(\mathsf{iK}+\mathsf{bem}\) is sound and complete for these concrete mixed models (using its birelational semantics). Apply the filtration to a concrete countermodel of any non-theorem to obtain a finite countermodel. Given a formula of length \(n\), \(s\le n\), and finite witnesses can be encoded by at most exponentially many bits: enumerate at most \(2^s\) outer worlds, at most \(2^s\) local points per outer world, their two relations and atomic valuations, and a distinguished local point. Truth at all subformulas is computable in time polynomial in this explicit finite encoding. Thus non-theoremhood is in \(\mathrm{NEXPTIME}\), and theoremhood is in \(\mathrm{coNEXPTIME}\); exhaustive finite enumeration also yields decidability.

## Verification

The standalone `checker.py` independently constructs random finite rooted intuitionistic components with arbitrary outer relations, computes actual subformula types, performs the prescribed root-signature and local-signature filtration, and checks the full truth lemma at every retained filtered point. A deterministic random seed gives 250 models and 5,000 formula/model cases, returning `ALL_CHECKS_OK randomized_models=250 formula_model_cases=5000 root_local_truth_lemmas=all`.

The finite tests are diagnostic only. The argument above, rather than enumeration, establishes the result for arbitrary initial carrier cardinalities. Reproduce with `python3 checker.py` using a Python 3 standard-library installation.

## Relationship to prior work

Van der Giessen, Joosten, Mayaux and Navarro Arroyo introduced these concrete mixed models, established their soundness/completeness correspondence with \(\mathsf{iK}+\mathsf{bem}\), and expressly identified the finite model property as requiring further checking (conclusion, Section 4). The new step is an explicit, truth-preserving two-level filtration and its quantitative finite bound; the published completeness theorem is used rather than re-claimed. Generic intuitionistic propositional filtration handles only local components. Generic classical modal filtration handles only the outer layer. The interaction through successor roots is handled here by selecting one successor for every false modal subformula, with retained root types enforcing the true ones.

Other known finite-model results concern different modal axioms or semantic frame classes, including intuitionistic \(\mathsf{S4}\); they do not, on the inspected evidence, imply this particular unbounded-outer-frame theorem. A pre-existing result under an alternative label for decidable or classical necessity is a possible historical-priority risk.

## Limitations

No optimal small-model bound, lower complexity bound, primitive diamond, quantifiers, or non-rooted local components are claimed. The countermodel upper bound is not a syntactic proof-search procedure by itself. The coNEXPTIME corollary uses the established completeness theorem for this exact logic; the filtration theorem is self-contained under the stated semantic definitions. Computer testing covers only finite generated examples. Priority remains subject to broader historical review and independent mathematical assessment.

## References

1. I. van der Giessen, J. J. Joosten, P. Mayaux, and V. Navarro Arroyo, *On the Contingency of Logic in Possible World Semantics*, Logica Universalis **19** (2025), 721–737, doi:10.1007/s11787-025-00400-7, arXiv:2510.17302 (first arXiv version 2025-10-20); especially Definitions 2.2.1–2.2.2, Theorems 3.1.8 and 3.3.2, Section 4.
2. M. Girlando, R. Kuznets, S. Marin, M. Morales, and L. Straßburger, *Intuitionistic S4 is decidable*, arXiv:2304.12094 (2023), a different modal frame class.
3. A. Simpson, *The Proof Theory and Semantics of Intuitionistic Modal Logic*, PhD thesis, Edinburgh LFCS report ECS-LFCS-94-308 (1994), for broader finite-model methods.
4. *Admissible rules for six intuitionistic modal logics*, Annals of Pure and Applied Logic **174** (2023), 103233, doi:10.1016/j.apal.2022.103233, for finite-model methods in other modal systems.
