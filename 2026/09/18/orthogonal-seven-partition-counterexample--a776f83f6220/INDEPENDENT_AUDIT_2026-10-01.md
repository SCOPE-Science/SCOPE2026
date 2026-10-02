---
audit_date: 2026-10-01
status: passed
---

# Scientific audit

## Final claim

There exists a centrally symmetric 70-point integer set with no weak orthogonal \(7\)-partition into cyclic class sizes \(7,7,28,28\); hence the smallest counterexample parameter in the discrete orthogonal-partition problem is at most \(7\), improving the previously explicit value \(8\).

## Correctness — PASS

The finite reduction was independently replayed from the 70 listed integer points. Projection orders can change only when the line direction is parallel or perpendicular to a point difference. After projectivizing by central symmetry, there are exactly 2450 critical rays and 2450 open chambers. Exact integer sorting gives \(q=8\) in 2351 open chambers and \(q=9\) in 99; exhaustive tied-cutoff enumeration on critical rays gives 2331 rays with \(\{8\}\), 79 with \(\{9\}\), and 40 with \(\{8,9\}\). Thus the required \(q=7\) never occurs even under weak boundary assignment. The replay also verifies 70 distinct points and no collinear triple.

**Checked sources.** Assigned RESULT.md and artifacts/verify.py at source tree 9a3a4c6e2f6d3ae4f88d0b27a4d4e90bfe7833b5; Leonardo Martínez-Sandoval, Counterexamples and symmetry for uneven orthogonal mass partitions in the plane, arXiv:2609.16757v1

**Residual risks.** The exhaustive certificate proves only this finite configuration and this target parameter; it does not address lower parameters.

## Originality — PASS

The motivating primary paper gives a 96-point \(k=8\) counterexample and explicitly asks whether any counterexample exists for \(2\le k\le7\). Searches of the published mathematical corpus found the assigned 70-point \(k=7\) record but no earlier \(k=7\) construction or stronger theorem implying one.

### Equivalent formulations

The audited object is exactly the first next unresolved parameter singled out by the source, not a renaming of the \(k=8\) example.

### Broader coverage

The \(k=8\) existence theorem does not imply \(k=7\); the target counts and cutoff combinatorics change with \(k\).

### Exact database or table

This is a finite exact witness, so a database search for the same parameter and object is relevant; no known-table entry was found.

### Claim versus prior implication

No checked prior implication produces the k=7 counterexample.

**Checked sources.** https://arxiv.org/abs/2609.16757; public open-problem rendering for the source's smallest-k question; published-result search for orthogonal seven-partition counterexamples

**Residual risks.** The primary preprint is very recent, so parallel unindexed constructions remain possible.

## Scientific value — PASS

This is a motivated finite cutoff: it answers the explicit next-range existence question posed by the source and improves the known counterexample parameter from \(8\) to \(7\). The complete exact critical-direction sweep makes the witness self-contained even though lower parameters remain open.

**Residual risks.** The result is an upper-bound improvement on the smallest parameter rather than a complete classification.

## Limitations

- The construction does not decide whether counterexamples exist for \(k=2,3,4,5,6\).
- It does not prove 70 points are minimal for \(k=7\), nor uniqueness of the configuration.
- The certificate is an exact finite enumeration rather than a formal proof-assistant artifact.

## Disposition

PASSED. Acceptance requires all three scientific axes to pass.
