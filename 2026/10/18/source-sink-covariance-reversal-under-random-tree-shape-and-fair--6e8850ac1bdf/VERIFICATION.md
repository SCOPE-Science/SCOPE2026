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

# Reproducibility and mathematical scope

Run the accompanying standard-library-only program with `python verify_oriented_trees.py`. It generates Prüfer trees, enumerates all unbiased orientations at orders two through seven, and compares exact rational source, sink, square, and mixed moments with the displayed formulas. The seventh order includes 16,807 trees and 1,075,648 oriented trees. It also checks fixed-path covariances for orders two through eleven, twelve weighted Prüfer edge-inclusion identities, and asymptotic correlation estimates using 45-digit decimal arithmetic. The most recent complete execution reported 70 passing checks.

Finite enumeration and decimal checks are not infinite proofs. The unrestricted moment and sign statements are established by the analytic conditional-incidence calculation and Prüfer identity in RESULT.md; the asymptotic claim follows from explicit expansions. This review is not an independent audit or a formal-machine proof.
