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

# Verification and reproducibility

Run `python3 verify.py` on a standard Python 3 installation. The verifier generates all labelled partial orders on 1, 2, 3 and 4 points by enumerating pair orientations and testing transitivity, then enumerates every upset, every subset-indexed nucleus, and each ordered pair of nuclei. It reconstructs composition directly on upsets and separately checks every alternating-path bridging statement. It checks idempotence and the optimal uniform exponent. Its expected successful terminal line is `VERIFY_OK 242 labelled-posets 57332 nucleus-pairs 120468 power/path identities`.

The finite checks are exhaustive only in the specified bounded domain. For arbitrary finite posets the proof uses exact quantified formula expansion, explicit separating upsets, and strict-chain height pigeonhole. No formal theorem prover and no independent audit is claimed.
