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

# Mathematical verification

The exact theorem is proved by three independently inspectable steps: an alternating adjacency-matrix congruence giving binary rank \(2s\), an even-core obstruction ruling out perfect covers when \(o\) is odd, and a family of explicit bicliques achieving \(s+(o\bmod2)\) for all petal lengths. No empirical output is used to infer the infinite result.

Run the attached Python 3 program with `python verify_bouquets.py`. It generates 1,484 valid cycle bouquets (up to four petals; lengths three through eight; vertex order at most 24) and confirms both the claimed rank and complete symmetric-difference edge recovery. Its exhaustive small-graph check enumerates every biclique on the labeled vertex set and checks the exact optimum for ten small petals/combinations: `(3,)`, `(4,)`, `(5,)`, `(6,)`, `(7,)`, `(3,3)`, `(3,4)`, `(3,5)`, `(4,4)`, `(3,3,3)`. When the exact optimum is four, all smaller possibilities are excluded by its complete enumeration and four is supplied by the explicit construction.

Expected last output line: `all checks passed`.

Finite tests are not exhaustive over unbounded petal lengths. This documentation records a self-review; an independent audit has not been performed.
