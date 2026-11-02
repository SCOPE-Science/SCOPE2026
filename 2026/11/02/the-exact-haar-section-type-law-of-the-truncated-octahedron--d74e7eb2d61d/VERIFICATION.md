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

# Reproducibility and verification

Run `python verify.py` with Python 3. No third-party modules are needed. The program constructs all 24 integer-coordinate vertices and their 36 edges, verifies every vertex radius and edge-endpoint inner product, enumerates every vertex-orthogonality wall intersecting the fundamental direction chamber, checks rational representatives in all five open cells, and compares the solid-angle expression with an independent elementary integration formula. It also checks probability normalization, the exact Crofton first moment, and a 90,000-draw seeded Gaussian-direction simulation. The executed program reported `ALL_CHECKS_PASSED`.

The analytical proof in `RESULT.md` proves the full result for almost every orientation. The finite run verifies identities and algorithmic enumeration but is not a formal proof of infinite claims, nor does a successful literature search establish historical uniqueness. The orientation measure is Haar-uniform on central planes; no assertion is made for random offsets. An independent audit has not been performed.
