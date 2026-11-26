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

A labeled word determines exactly one indexed closed walk by taking its length-five window at each residue. Conversely, overlapping successive windows on a closed walk forces every window coordinate to be the corresponding leading letter at a shifted index, even when n<5; thus the six-letter tests cover every cyclic forbidden square, including across more than one boundary. Hence c_n=tr(A^n), without any extra rotation factor. Independently ran python3 /workspace/cyclic_short_square_check.py (Python with SymPy): generated all admissible six-letter blocks and their five-letter overlaps, checked the complete state set (30 states, 42 edges), computed and factored the exact characteristic polynomial, reproduced every coefficient of the proposed det(I−zA) and the first twenty traces, directly counted n=1..9 by modular indexing, and tested the four stated loops at the common state 01210. The formal trace-log identity establishes the rational zeta expression for all n. The traces exclude exactly the six listed small candidates once the loop argument is applied: lengths 4 and 6 generate all even n≥4 and bases 11 and 13 plus the same semigroup give all odd n≥11. A rotation by j fixes exactly the repeats from a labeled word of length gcd(n,j), which proves Burnside's formula. Divisor inversion on least periods counts the primitive words, each giving one orbit per n distinct rotations. The source checker was inspected, not run. The stated positive spectrum concerns allowable circumferences, not an asserted spectrum of least periods.

## originality

PASS

The distinct exact result is the full periodic trace and zeta determination for this particular ternary constraint, including explicit witnesses for the circumference classification. The linear forbidden language, constrained graph method, growth root, general trace-log and orbit identities are not new. Neither the strongest matching indexed findings nor the inspected linear and fully square-free sources give the same periodic determinant or exact counts.

## value

PASS

The forbidden lengths are motivated independently by short tandem-duplication irreducibility. Exact periodic counts are needed for rotation and least-period orbit counts, which cannot be recovered from a linear growth rate. The evaluated determinant, coefficients and explicit all-length witnesses provide reusable exact information beyond the generic transfer-matrix recipe or the known existence of many fully square-free circles; the gap pattern does not merely track the full circular square-free exceptions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
