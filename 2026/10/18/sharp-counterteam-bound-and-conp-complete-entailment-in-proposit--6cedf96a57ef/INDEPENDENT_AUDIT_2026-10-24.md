# Independent mathematical audit

## correctness

PASS

For finite Γ, put φ=conjunction Γ and m=total NE atom occurrences. The published convexity and union-closure lemmas for lax PL(NE) hold for the exact literal/NE/constant/∧/split-∨ semantics. Structural induction yields a satisfying subteam A⊆T of size≤m: NE needs one valuation, other atoms none, and conjunction/split combine witnesses via convexity/lax splitting. Given Γ countermodel T not satisfying ψ, let U be the union of all ψ-models over the finite common valuation space. If no ψ-model exists, A is already a countermodel. Otherwise union closure makes U a ψ-model. If T⊆U, convexity forbids ψ on A; otherwise adjoin v in T minus U to A, and convexity of φ keeps the premise true while v excludes ψ. Bound |T′|≤m+1 includes m=0 and empty teams. The sharp example requires m distinct full-characteristic valuations through (χ_i∧NE) plus a split top, while ψ is their disjunction; every counterteam has those m plus an outsider. NP verification follows from polynomial team model checking and m+1 Boolean valuations; classical tautology reduces to entailment for coNP-hardness. Independent exhaustive semantic evaluation tested 105 two-variable syntax formulas, 20 truth-table classes, all 400 semantic entailment pairs, convexity, union closure and small models; explicit sharp counterteams independently checked for m=1..6.

## originality

PASS

Semantic consequence is genuinely different from validity and satisfiability for convex nonempty team formulas; the 2026 primary paper explicitly lists entailment as future work. The m+1 sharp guarantee and consequent coNP classification are best-of-knowledge new relative to checked published work.

## value

PASS

A finite-premise semantic entailment problem explicitly left open by the direct primary complexity paper is classified coNP-complete with an exact tight m+1 semantic certificate. The sharp counterteam bound is a usable structural theorem, not a rephrasing of the known validity classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
