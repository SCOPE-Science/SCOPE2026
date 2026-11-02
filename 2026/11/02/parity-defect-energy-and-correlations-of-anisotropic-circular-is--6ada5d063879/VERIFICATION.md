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

# Reproduction and scope

Run `python3 CHECK.py` in a directory containing `CHECK.py` and `CHECK_OUTPUT.txt`. The standard library alone suffices. The script computes all \(2^{2n}\) labelled spin assignments for each \(n=3,4,5,6,7,8,9\), and couples \((J,K)=(1,1),(1,3),(2,1)\). It verifies the theorem's fixed-sector minimum for every absolute magnetization, the degeneracies at weak/intermediate/coexistence/saturation fields, and exact integer-cleared spin correlations for odd \(n=3,5,7\). The independent-set sequence is recomputed by direct combinatorial exclusion and matched with the Pell–Lucas trace formula.

The saved `CHECK_OUTPUT.txt` is a deterministic expected result. Each count and comparison is recomputed from the code and checked with exact integers; no numerical tolerances are used. This tests finite cases only, and does not prove the statements for arbitrary \(n\); the separate induced-edge extremal argument and domain-wall counting in `RESULT.md` supply that proof.

The saturated independent-set count is pre-existing transfer-matrix knowledge. Novelty and historical priority are provisional on the particular finite-size, anisotropic energy and correlation classification. Independent audit status is not performed.
