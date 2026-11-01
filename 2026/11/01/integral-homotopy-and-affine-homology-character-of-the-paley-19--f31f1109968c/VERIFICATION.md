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

# Reproducibility

Run `python3 checks/paley19_neighborhood_verifier.py` from this package. Compare the resulting standard output byte-for-byte with `checks/verification_output.txt`. It uses only the Python 3 standard library. The code enumerates all nineteen neighborhoods and all \(2^{19}\) vertex-subset masks, checks the full 8246-face matching DAG (40014 incidences), computes a signed integral Morse boundary of size \(4\times81\), verifies a full-column row relation and a determinant-\(-1\) rank-three minor, independently reduces every simplicial boundary over \(\mathbb F_2\), and checks every group element's signed Lefschetz trace. The exact integral minor, not mod-two homology, supplies primitivity; the standard CW cell-attachment argument yields homotopy type.

No general-family theorem, full equivariant homotopy type, or independent external audit is claimed. The finite proof concerns only the explicit nineteen-vertex object.
