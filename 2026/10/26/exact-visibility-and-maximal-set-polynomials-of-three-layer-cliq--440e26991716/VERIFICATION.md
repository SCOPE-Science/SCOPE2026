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

# Reproduction of finite checks

Run `python3 verify.py` with Python 3.9 or later; no external packages are required. The script defines the Cartesian graph directly, computes shortest paths using breadth-first search, and compares the original mutual-visibility predicate (shortest paths in the graph versus shortest paths avoiding selected internal vertices) to the independently specified column classification. It also verifies inclusion-maximality by testing every possible one-vertex extension and compares all coefficients of the two asserted polynomials.

The tested graph orders are \(n=2,3,4,5\), corresponding to \(64,512,4096,32768\) subsets. The expected final line is `VERIFY_OK`. These finite checks are corroboration, not a proof of a claim for all \(n\); see the mathematical classification in `RESULT.md` for the infinite-family argument. No independent audit or external certification is claimed.
