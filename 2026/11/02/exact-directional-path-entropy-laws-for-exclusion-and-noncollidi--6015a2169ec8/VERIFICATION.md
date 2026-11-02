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

# Reproduction

With Python 3 and its standard library, run `python3 verify.py` from this directory. The full recorded output is:

```
PASS 8816 deterministic assertions; enumerated all unlabeled configurations for 3<=n<=10, 1<=k<n
PASS 8839 total deterministic assertions
```

The program independently constructs every legal exclusion edge and both finite Markov generators, computes their stationary traffic and direct path-rate divergences, checks Fourier-Vandermonde eigenrelations, and compares the resulting quantities to the proposed closed forms. Separate two-particle distance counts check the stationary entropy constants and the mesoscopic scaling estimates. The analytical proof in RESULT.md supplies the all-size and limiting assertions; no finite computation is treated as a proof of those assertions. These checks provide no independent mathematical audit or external certification.
