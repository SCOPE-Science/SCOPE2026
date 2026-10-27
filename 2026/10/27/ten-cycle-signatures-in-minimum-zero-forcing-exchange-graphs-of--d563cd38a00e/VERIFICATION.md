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

Run `python3 verify.py` (Python standard library only). The program constructs \(H\), explicitly complements its edge set, computes ordinary zero-forcing success from all initial three-white-vertex sets, reconstructs all token-jumping edges and degree counts, and tests connectivity. The all-pair exchange distance bound is exhaustively checked for total orders at most \(20\). Tested component lengths: `[9]`, `[10]`, `[11]`, `[12]`, `[13]`, `[18]`, `[19]`, `[20]`, `[9,9]`, `[9,10]`, `[9,11]`, `[10,10]`, `[9,9,9]`, `[9,10,11]`. The terminal success sentinel is `VERIFY_OK`.

The all-order conclusion follows from the proof's first-force classification, counting by pair intersection, and explicit exchange paths. Tests do not establish infinite coverage by themselves. External independent audit has not been performed.
