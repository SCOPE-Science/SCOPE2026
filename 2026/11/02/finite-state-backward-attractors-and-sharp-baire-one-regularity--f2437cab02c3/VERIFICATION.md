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

Run `python3 verify_example.py` with standard-library Python 3. The script constructs the exact rational four-branch map and endpoint-refined Markov graph, checks four slopes, 80 affine interior evaluations, three cyclic SCCs, and predecessor reachability for the sharp Baire-class-one example. Expected output starts `VERIFY_OK`.

General validity follows from the written proof: graph realization, SCC stabilization of every infinite reverse walk, cylinder diameter bounded by \(\lambda^{-k}\), and realized inverse periodic cycles. The checker does not certify arbitrary maps or infinitely many cycle words; it checks only the explicit sharpness example. Independent validation has not occurred.
