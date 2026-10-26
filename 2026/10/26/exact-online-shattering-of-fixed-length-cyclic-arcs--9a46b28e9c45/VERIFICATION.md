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

The complete proof is in `RESULT.md`. `cyclic_arcs_verify.py` implements the direct finite version-space recurrence and independently enumerates VC traces for every sample of size at most three, confirming 120 complete pairs with \(2\le n\le16\) for Littlestone dimension and 190 complete pairs with \(2\le n\le20\) for VC dimension. It additionally checks ten larger Littlestone cases and all root-to-leaf paths of six explicit complete binary trees; the largest tree has 128 leaves. `cyclic_arcs_witness_n128_k64.json` contains that certificate. The stdout transcript is `cyclic_arcs_verification_output.txt`.

Run `python3 cyclic_arcs_verify.py` in the directory containing these files. Python 3.9 or newer is sufficient; no third-party packages are needed. The recurrence is exhaustive over finite version spaces, while the general proof uses a uniform combinatorial argument and does not depend on finite extrapolation. Historical priority remains a literature-search limitation; no independent audit has been performed.
