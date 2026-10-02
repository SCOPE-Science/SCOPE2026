# Independent scientific audit — SCOPE-20260915-002

Audited at: 2026-10-01T04:13:22.005211Z

Disposition: **passed**

## Correctness — PASS

Independent exact binary-linear-algebra reconstruction gives length 13, ranks 6 and 3, four logical qubits, X-distance 2 and Z-distance 4, with baseline radius-one values 1 and 2. All seven unordered bipartitions of the selected weight-four X check fail the direct CSS-safety test. The inspected exhaustive verifier checks all repair solutions and all weight patterns needed for the two named repair partitions, reproducing 64 repairs with minimum added-fix weights 5 and 6, the stated surviving opposite checks, dressed radius-one collapse to zero on both sides, and stabilizer-convention values 0 and 2.

## Originality — PASS

The primary qLTC/weight-reduction papers give general constructions and tradeoffs but do not state this exact 13-qubit product-truncation certificate or its exhaustive single-ancilla repair obstruction. Resultary search found only the same record as an exact match.

### Equivalent formulations

The certificate is not a renamed asymptotic tradeoff theorem.

### Broader coverage

General weight-reduction theory motivates the obstruction but does not dominate this finite exact statement.

### Exact database or table

No published small-code table located contains the repair counts and soundness witnesses asserted here.

### Claim versus prior implication

The record is a narrow local obstruction, not a corollary or a claimed general impossibility.

## Value — PASS

The exact smallest-scale obstruction is motivated by an active construction route: it cleanly separates preserved distance from lost local testability under a concrete reduction move and supplies explicit blind witnesses. Its narrow scope is stated rather than inflated into a universal no-go result.

## Sources inspected

- Tradeoff Constructions for Quantum Locally Testable Codes — https://arxiv.org/abs/2309.05541. NOT_COVERING: Gives general constructions/tradeoffs, not the exact 13-qubit repair census.
- Weight Reduction for Quantum Codes — https://arxiv.org/abs/1611.03790. NOT_COVERING: Uses broader gadgets and parameter bounds; does not state the audited finite obstruction.

## Residual risks

- The obstruction concerns only the stated single-ancilla split-and-repair model and must not be read as a general no-go theorem for multi-ancilla or other locality-reduction gadgets.
- The original metadata pointed to an obsolete output/artifacts path; the actual inspected verifier is artifacts/verify_emergent.py.

## Limitations

- Only the stated finite code and single-ancilla split model are proved.
- No theorem over all constant-sized complexes or multi-ancilla reductions follows.
- The artifact inventory path is corrected to the actual repository path in the publication plan.
