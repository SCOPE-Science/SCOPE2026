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

# Verification

Reproduce finite tests from an extracted package containing `check_unbalanced.py` using `python check_unbalanced.py`. The program reconstructs graph paths directly by breadth-first search, compares group-constant matrices entrywise, finds determinant roots and verifies centered powered-distance signs for 25 unequal parameters, and checks the analytic thin-side asymptotic against four large-parameter probes. It prints `CHECK_OK` when complete. At exponent zero the diagonal is explicitly reset to zero, as required by the definition of negative type. Numerical eigenvalues and numerical root finding are finite consistency checks, not certificates for every integer size.

The proof of the universal claim is in RESULT.md: a complete invariant-space decomposition, a strictly positive minor certificate for every nonconstant block on the needed interval, an explicit mixed-form obstruction at the pre-subdivision exponent, strict interpolation excluding later admissible exponents, and a uniform first-order asymptotic expansion. The dimension statement is obtained from the nullity of the centered form and the Euclidean distance-matrix identity.

The critical scientific limitations are the implicit rather than elementary least-root description, restriction to uniformly subdivided unequal bicliques, bounded literature coverage, and the absence of independent validation.
