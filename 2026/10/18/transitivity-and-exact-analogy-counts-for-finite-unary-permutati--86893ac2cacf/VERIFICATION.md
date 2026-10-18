---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Computational verification and proof boundaries

## Reproduction

Run `python verify.py` using Python 3.9 or newer. This script uses only the Python standard library. Expected successful result:

`VERIFY_OK compositions=127 tested_quadruples=207541 direct_justifications=YES exact_counts=YES transitivity=YES`

## What is checked

For every ordered composition of each total size from one through seven, the verifier builds a disjoint union of unary cycles, computes every finite-period residue representation of all term-witness justifications by evaluating \(f^u(w)\) and \(f^v(w)\) over every witness \(w\), implements both the trivial clause and target-maximality clause of the directed analogical proportion, and requires all four directed orientations for the complete proportion. For every ordered quadruple it compares the resulting semantic truth value with the gcd-cycle criterion. It also compares the total truth counts, equivalence-class sizes where transitive, and transitivity itself with the formulas. Enumerating exponent pairs modulo the permutation order is exact for these finite cyclic test instances: all term evaluations repeat periodically.

## Mathematical proof boundary

The infinite family theorem is not inferred from these finite checks. The explicit congruence description of every justification set, generalized Chinese remainder theorem, disjointness of target congruence classes, exact residue counting, and explicit unequal-cycle witness provide the mathematical proof. No external certificate or independent audit is claimed.
