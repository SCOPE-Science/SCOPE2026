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

The claim's proof is analytical; `check.py` performs finite consistency tests only. Use Python 3 standard library and run `python3 check.py` from this directory. On the checked source, all deleted-edge sets through six graph vertices and every ordering of the chosen pairwise-distinct scores were tested. The test also verifies the explicit uniform-score endpoint-spacing benchmark by a seeded simulation. Its assertions do not establish infinite-parameter claims or a literature uniqueness conclusion.

The critical proof checks independent of code are the rank-two order-statistic gap bound, the independence of sorting labels from values, the matching contact alternatives, the strict nonmatching witness, the intrinsic Gaussian radial factor, and convergence plus uniform integrability of the extreme gaps. The exact triple integral is obtained by conditioning on the sample endpoints and integrating the interior observations. All these arguments are stated in RESULT.md.

No computer-assisted infinite certification, external proof formalization or independent mathematical audit is claimed.
