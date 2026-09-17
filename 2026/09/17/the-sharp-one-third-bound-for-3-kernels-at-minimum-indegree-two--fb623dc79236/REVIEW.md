# same-model review

## Run identity

- Source run ID: `SCOPE-20260917T100642Z-01`
- Research start: `2026-09-17T10:06:42Z`
- Research end: `2026-09-17T10:23:32Z`
- Reported status: `SAME_MODEL_REVIEW_PASS`
- Result type: substantive target

## Correctness

**PASS (same-model assessment).**

The proof was checked against the structural properties supplied by Boyer et al.'s algorithm, including the bound `2|R| <= |B|`, the final-set outdegree condition in `A`, and the prekernel-to-kernel conversion. Boundary cases of the auxiliary pseudoforest lemma were checked separately, including isolated vertices, ordinary cycles, trees, and the two-vertex cycle formed by parallel edges.

The supplied verification script independently checks the theorem for every simple digraph with minimum in-degree at least two through order five, and the structural hitting-set lemma for every loopless partial functional digraph through order seven. No counterexample was found.

## Originality

**PASS, qualified to the best of our knowledge (same-model assessment).**

Fresh searches during the source run for the exact constant, equivalent formulations, minimum in-degree two plus 3-kernel terminology, and nearby transversal formulations found no prior coverage. The primary June 2026 paper still presents the `δ=2,q=3` case as unresolved.

The closest located neighboring work was Penev--Stein--Trujillo-Negrete on other q-kernel directions. No concrete inaccessible source was identified as likely to contain the same theorem.

Remaining threat: a recent unindexed manuscript, private draft, or newer revision resolving the same explicitly posed case.

## Value

**PASS (same-model assessment).**

If correct and novel, the result improves the first unresolved case highlighted by the primary paper from the known general upper bound `1/2` to the sharp `1/3`, proving the conjectured constant for `(δ,q)=(2,3)`. The proof also introduces a pseudoforest-incidence covering mechanism rather than only a finite computation.

## Independence correction preserved from the source report

The source report initially said there was no earlier run topic, then corrected that statement after locating an earlier SCOPE email on strong majority edge-colouring. The q-kernel result was still judged independent because it used a different problem, invariant, method, and target. This archive preserves that correction rather than the earlier narrower wording.

## Review disclaimer

This is not independent validation, peer review, or a guarantee of scholarly priority.
