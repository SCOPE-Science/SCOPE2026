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

The included `verify.py` is a standalone exact-arithmetic verification program. Run `python3 verify.py` in an environment containing SymPy as specified in `requirements.txt`. It checks the projector-entry formulas by direct multiplication of rational Laplacians for all integer partitions with at least two parts and total vertex count two through ten. It also checks all cited symbolic polynomial factorizations, discriminants and scalar inequalities.

Successful replay output:

`VERIFY_OK symbolic spectral identities, exact positivity certificates, 512 complete multipartite direct rational RK4 matrices, 16048 vertex-pair checks`

The proof for every network size and positive real timestep is in `RESULT.md`. Finite replay alone cannot certify an infinite-family assertion. The root enclosure is rational; its displayed decimal is descriptive only. Historical originality remains subject to inspection of further specialized sources. Independent mathematical audit has not been performed.
