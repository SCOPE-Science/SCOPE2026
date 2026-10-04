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

Run `python3 verify.py` from the directory containing this file and the verifier.

The verifier constructs all distinct subsequences directly. For every \(4\le n\le9\), it enumerates every binary word and all unordered pairs, tests \(\mathcal D_2(x)\cap\mathcal D_2(y)=\varnothing\), independently confirms the same eligibility by a longest-common-subsequence dynamic program, and maximizes \(|\mathcal D_3(x)\cap\mathcal D_3(y)|\). It checks the claimed maximizing witness at every length.

Expected terminal line:

`VERIFY_OK n=4..9 pair_checks=174216 eligible_pairs=94949 maximizing_pairs=20 boundary_n10=20`

The boundary check at \(n=10\) verifies the concrete pair \(1010101010\), \(0110011001\): its radius-two deletion balls are disjoint and its radius-three intersection has size \(20\).

The program does **not** certify the infinite tail by finite extrapolation. The statement \(N(n,3,3)=20\) for all \(n\ge10\) uses Theorem 4 and Proposition 5/Corollary 6 of arXiv:2111.04255v1. The finite verifier supplies an independent exact certificate only for the previously uncovered lengths and for the boundary witness.
