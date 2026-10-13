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

The analytic derivation has three critical steps: the published four-mode Gaussian-fidelity normal form; substitution into the published exact vacuum/full-occupancy convolution purity; and elementary optimization on \(F_{\mathrm G}\in[1/2,1]\). No finite computation is used to prove a universal quantifier.

The accompanying `artifacts/verify.py` independently implements the balanced two-copy convolution for the canonical four-mode family by Jordan--Wigner Majoranas. It checks representative values of \(p\) against
\[
1-3p(1-p)+\frac32p^2(1-p)^2
\]
and separately checks the extremal value \(11/32\). Successful execution prints `VERIFY_OK`.

The replay does not establish the canonical normal-form theorem; that step is taken from Dias--Koenig Theorems 5.4 and 5.6. It also does not test higher-mode or mixed-state claims, which are outside the finding.
