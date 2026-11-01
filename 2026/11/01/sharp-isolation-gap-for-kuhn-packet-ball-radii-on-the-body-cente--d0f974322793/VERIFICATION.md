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

# Reproducibility and checks

Execute `python verify_bcc.py` with Python 3 and its standard library; no download or external data is needed. The checker enumerates the 14 lattice vectors of squared norm below two and all 364 unordered three-element combinations. It discards rank-deficient triples and inspects all 232 independent triples, each with six tetrahedral orderings. Minimum balls are computed as exact fractions from Gram systems over all candidate vertex support subsets; all four vertices are then checked for containment. The output records exactly eight unordered isolated optimizers, plus 48 other **short-vector** triples with squared packet radius \(1/2\). A particular sharp second-layer frame is independently checked.

These tests verify the finite short-vector consequence and sample exact extremizers, not a proof that frames involving longer vectors fail. The latter exclusion is the analytical subset-sum bound and classification in `RESULT.md`. The proof is fully elementary and self-contained for the stated all-frame assertion.

The research finding has undergone self-review only. No independent audit, external certification, or complete historical-priority proof has been performed.
