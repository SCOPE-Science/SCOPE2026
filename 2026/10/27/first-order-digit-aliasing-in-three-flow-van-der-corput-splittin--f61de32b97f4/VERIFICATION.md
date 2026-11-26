---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The leading binary digit forces the second swap and restricts the first swap; the completed orders are (3,1,2) below the 1/3 tail threshold and (2,1,3) otherwise. A dyadic cylinder corresponds to one residue class, so a truncated binary decomposition of [0,1/3) gives a uniform O(1+log N) prefix discrepancy. The local h² coefficients are K/2 and −K/2, averaging to −K/6. Telescoping changes the left propagator to the exact one with total error O(Nh³); summation by parts for the centered coefficients uses O(h) adjacent propagator variation. The constant term is the stated Riemann integral up to O(h²). For the witness K=−E13, E13 commutes with the sum, and its spectral norm is one, giving Te^T/6. Independent exact word and matrix calculations can be replayed with python /workspace/review_evidence/reproduce_1234.py 2; they corroborate but do not prove the all-N asymptotic. The conclusion concerns the specified indexing and descending shuffle with bounded generators.

## originality

PASS

The serial shuffle recipe is prior. The supported distinct contribution is the binary-digit aliasing analysis for its fully specified descending three-flow instance and the resulting sharp first-order transported commutator, not the algorithm, generic discrepancy facts or local product expansion.

## value

PASS

This isolates a concrete implementation failure of an actual proposed quasi-random splitting recipe: low discrepancy of individual inputs does not balance the pair of shuffle draws. The arbitrary-generator leading error and exact nonzero witness say what fails and by how much, rather than merely showing that a permutation histogram is unbalanced. It is not a claim against all quasi-random methods or against the motivating PDE experiments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
