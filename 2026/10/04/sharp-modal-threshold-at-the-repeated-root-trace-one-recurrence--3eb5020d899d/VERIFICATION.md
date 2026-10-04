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

The proof is symbolic and covers every even \(N\ge10\). The finite checker is supplemental.

`verify.py` performs four exact checks:

1. It verifies the closed form \(G_n=n2^{1-n}\) against the repeated-root recurrence through index \(80\).
2. It checks the exact transition ratios \(10/3\), \(7/3\), and \(11/9\) at \(N=6\) and \(N=8\).
3. It proves the two numerical inequalities used by the universal descent argument after replacing \(\pi\) by the classical rational upper bound \(22/7\).
4. It independently reconstructs Bernoulli numbers with rational arithmetic and verifies the maximizing index for every even \(N\) from \(4\) through \(40\).

The replay output is stored in `verification_output.txt`. The finite range is not presented as evidence for the universal quantifier; that quantifier is discharged by the adjacent-ratio proof in `RESULT.md`.
