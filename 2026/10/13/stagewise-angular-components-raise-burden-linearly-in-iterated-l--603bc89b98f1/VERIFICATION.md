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

The mathematical check has two layers.

1. **Laurent power quotients.** For characteristic \(0\), principal units \(1+tF[[t]]\) are uniquely \(p\)-divisible for every prime \(p\). Hence each Laurent extension contributes exactly one factor \(\mathbb Z/p\mathbb Z\) to \(F^\times/(F^\times)^p\). Starting from an algebraically closed field gives
\[
\left|F_r^\times/(F_r^\times)^p\right|=p^r.
\]
This verifies the finite-power-quotient hypothesis at every residue level.

2. **Burden recurrences.** The external model-theoretic inputs are Touchard's resplendent maximum formula without angular components and additive formula with an angular component. With residue and value burdens both initially \(1\), the recurrences are
\[
b_0=1,\quad b_r=\max(b_{r-1},1),
\]
and
\[
c_0=1,\quad c_r=c_{r-1}+1.
\]
Therefore \(b_r=1\) and \(c_r=r+1\).

The bundled `artifacts/verify.py` checks these arithmetic recurrences for several primes and tower depths and prints `VERIFY_OK`. It does not mechanize the cited model-theoretic transfer theorems; those remain literature inputs.
