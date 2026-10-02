---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

Dense Pinwheel Packing remains NP-complete under unary encoding even when every period is odd and squarefree with at most five prime factors, the global least common multiple is odd and squarefree, and the global greatest common divisor is an odd prime.

## Correctness — PASS

The reduction was reconstructed from the source construction. Padding the sparse tripartite instance by disjoint forced triangles to a prime part size \(p\) preserves the degree/incidence promises and triangle-partition feasibility. The source marker construction then uses \(m_v\), a product of one to three distinct marker primes \(r_T>p\), and periods \(pm_v\) and \(3pm_v\). These are odd, squarefree, and have at most four/five prime factors. Every marker occurs in some witness period, \(3\) occurs in cell periods, and witness periods omit \(3\), so the LCM is \(3p\prod_T r_T\) and the GCD is \(p\). The per-vertex density is exactly \(1/(3p)\), and prime padding changes the source size only by a constant factor. The inspected arithmetic verifier confirms these identities on representative primes but is not used as the complexity proof.

**Checked sources.** assigned RESULT.md at the frozen tree; artifacts/verify_arithmetic.py and verify_output.txt; Kobayashi--Lin--Swernofsky, arXiv:2609.20075

**Residual risks.** The argument assumes the sparse source instance has at least one triangle incident to every vertex, exactly as in the source promise.

## Originality — PASS

The source hardness theorem establishes unary NP-completeness but does not state odd/squarefree or bounded-prime-support restrictions. Its published reduction exposes marker products \(m_v\) and periods \(nm_v,3nm_v\); the audited prime-padding step changes the source instance so that the common factor itself is a new odd prime. Searches for pinwheel hardness with odd/squarefree moduli and equivalent exact-covering restrictions found no earlier theorem.

### Equivalent formulations

Equivalent exact-covering-system language was searched; no hardness theorem with all audited restrictions was located.

### Broader coverage

Neither source dominates the restricted arithmetic hardness theorem.

### Exact database or table

The database/table check is inapplicable to a reduction theorem; only theorem-level coverage is relevant.

### Claim versus prior implication

This is a new reduction refinement, not a parameter substitution inside a fixed output instance.

**Source inspections.**
- Dense Pinwheel Packing Is Strongly NP-Complete: Primary abstract plus detailed public exposition of the marker-prime reduction. Assessment: Supplies the hardness backbone and periods \(nm_v,3nm_v\), but not the prime-padding arithmetic restriction.
- The Erdős--Selfridge problem with square-free moduli: Abstract and theorem context. Assessment: Structural covering-system theorem, not a pinwheel hardness result and typically concerns distinct moduli.

**Checked sources.** https://arxiv.org/abs/2609.20075; https://arxiv.org/abs/1901.11465; published-results semantic search

**Residual risks.** The source preprint is very recent and a later revision could independently add the same prime-padding observation.

## Value — PASS

The result removes three plausible arithmetic sources of hardness at once: parity, repeated prime powers, and large prime support. It places strong NP-completeness inside the divisor lattice of one odd squarefree integer with at most five prime coordinates per task, a natural structural boundary for the exact-covering interpretation.

**Checked sources.** Kobayashi--Lin--Swernofsky 2026; squarefree covering-system literature

**Residual risks.** The constant five is not shown optimal, and equal task periods remain essential.

## Limitations

- Equal periods remain allowed as distinct tasks, as in the source problem.
- The result does not address distinct-modulus covering systems and does not prove that five prime factors is optimal.
- The reduction is a refinement of a very recent hardness construction, so near-simultaneous priority is a material residual risk.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
