# Scientific review: exact pointed-theory spectrum and optimal tests

## Correctness — PASS

The class and its language are fixed explicitly. Terminal flattening is a structural induction on every formula (including nested modalities). The depth-one indicator \(\neg\Delta\chi_a\) isolates each realized successor label whenever at least two labels are present; all smaller supports genuinely collapse, including no successors and arbitrarily many identically valued successors. There are exactly \(2^N-N\) support classes, independent of the root vector; the constructive mutually exclusive isolation formulas establish the complete Boolean algebra and depth bound. The information-theoretic lower bound is exact, with \(n=0,1\) treated separately. The included checker passed its stated finite checks, and none is represented as an infinite proof.

## Originality — PASS, with priority risk

The 2026 sequent-calculus paper fixes the recent motivation but does not enumerate pointed theories on rooted stars. Fan–Wang–van Ditmarsch (2014) is the closest conceptual predecessor: its general \(\Delta\)-bisimulation invariance result covers part of the qualitative indistinguishability mechanism. The present claim is deliberately not that general indistinguishability is new; it adds exact all-arity pointed-theory and formula-meaning counts, constructive isolation at depth one, and a sharp worst-case number of non-contingency tests. The S5 enumeration in Bradley–Swartz (1979) is a significant prior example of counting modal meanings; its underlying frame and operator differ, and direct substitution does not yield the claimed non-contingency-star count. Query comparisons found no identical quantitative classification, although unlocated finite modal-algebra literature could contain it. Priority is not certain.

## Value — PASS

For a standard uncertainty modality, the result determines exactly how much successor information survives language restriction, how many pointed semantic states remain, and the minimum number of independent observations required to identify them. The explicit normal form can be used for exact finite-variable formula synthesis and model minimization. It is a natural complete classification of a finite-depth frame family, not an isolated small case.

## Limitations

Only nonreflexive one-step stars and finitely many propositional letters are covered. The known bisimulation predecessor already supplies general qualitative insight. The checker verifies finite instances, while the unrestricted theorem follows from the written proof. No independent audit or priority certificate exists.

Self-review: passed. Independent audit: not yet performed.
