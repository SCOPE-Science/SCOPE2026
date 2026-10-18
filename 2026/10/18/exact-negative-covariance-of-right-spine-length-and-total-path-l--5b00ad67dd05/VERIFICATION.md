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

# Reproducibility and boundaries

Run `python3 verify.py` from this directory. The script uses only Python's standard library and requires no network connection or third-party package.

It checks \(\operatorname{Cov}(P_n,R_n)=3n+H_n-2(n+1)H_n^{(2)}\) against exact arithmetic derived from enumerating every insertion order for \(1\le n\le8\) and independently derives all mixed moments by the split recurrence for \(1\le n\le100\). Every insertion path length is recomputed by simulating child-pointer traversal; every spine length is recomputed as the strict record count. It checks first moments separately, the joint moment, and the strict covariance differences in a diagnostic range. Expected output: `VERIFY_OK 46563 exact checks`.

The script's finite exhaustive checks do not establish the formula for unbounded tree sizes. The general result is established by the root-decomposition, generating-function solution, harmonic coefficient identity and strict-sign argument presented in `RESULT.md`. The leading correlation normalization uses the classical random-BST path-length variance. No independent audit has been performed.
