---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: reconstructed the 3-step affine return equations under each integer carry, the unique fixed-periodic solution when p=8(1+b)(1-b)^2 !=1, all strict branch tests and width-factorization signs, and the period-1/2 exclusion. For primitive right-right two-cycles with t=2(1-b)<1, (1+t)(y-x) is an integer of modulus <1, impossible. The rational witness (a,b)=(10/19,3/4), x=(9,43,71)/76 has multiplier 7/8. An independent SymPy reconstruction verifies width, collision boundaries and witness. The published Theorem 2.5 is conditional on a nonempty component; the submitted witness establishes this nonemptiness. Branch boundaries and other carry strips are not classified.

## originality

PASS

Qualified best-of-knowledge originality applies to the explicit +-- eye, first minimal primitive eye period, and sharp specified-carry parameter strip, not to the definition of an eye or its general conditional itinerary criterion.

## value

PASS

PASS: exhibits a previously conditional geometric phenomenon at the smallest possible primitive period and gives an exact sharp two-parameter region for a concrete lift. This is a natural minimal-period existence/parameter-classification question, not an arbitrary isolated test. It does not claim a complete census of every eye or a global circle-map theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
