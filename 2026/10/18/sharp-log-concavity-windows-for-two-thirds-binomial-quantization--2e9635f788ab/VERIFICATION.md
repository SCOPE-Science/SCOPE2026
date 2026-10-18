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

# Reproducibility and verification

The paper's full proof uses the exact unnormalized binomial masses. The first critical identity is
\[
 b_1^2-b_0b_2=t^3\left[\binom n2^2t-(1+nt)\left(\binom n3+\binom n4t\right)\right],\quad t=p/(1-p)>0.
\]
The second critical identity is the discriminant formula (6), whose negative sign for all \(n\ge7\) is certified algebraically by expansion at \(n=7+m\). At \(n=6\), two incompatible necessary conditions conclude the remaining case. The complete small cases are checked symbolically.

The included `VERIFY.py` is self-contained apart from Python 3 and the public SymPy package. Run `python VERIFY.py` from the directory containing this file. Actual run outputs were:

```text
SYMBOLIC_IDENTITIES_PASS
EXACT_RATIONAL_GRID_PASS trial_counts=30 odds_grid=40 tests=1200
```

The program checks symbolic identities exactly and separately tests thirty sizes on forty strictly positive rational odds each, using Python rational numbers. It does not establish the infinite claim by enumeration: that part rests on the factorization and sign argument supplied in `RESULT.md`. No independent audit, external proof-assistant certificate, or arbitrary-precision infinite computation is claimed.
