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

`verify.py` reconstructs the seven-state transition table and performs two exact calculations over the complete nonempty power automaton. The first is forward breadth-first search with polynomial propagation on shortest edges. The second builds reverse adjacency, computes distance to the target singleton, retains exactly distance-decreasing edges, and recursively accumulates the letter-count polynomial. Both routes must equal the coefficient vector in `certificate.json`.

The script additionally checks the published witness \((ab^5)^5a\), the minimum length \(31\), the unique minimum-distance singleton \({2}\), the total count \(1{,}048{,}576\), and the factorization \(z^6(1+z)^{20}\).

The finite exhaustive check establishes only the stated seven-state claim. It is not evidence for an unproved all-\(n\) formula.
