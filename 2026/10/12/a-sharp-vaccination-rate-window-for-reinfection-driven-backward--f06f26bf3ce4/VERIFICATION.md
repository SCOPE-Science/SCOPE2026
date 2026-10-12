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

These checks verify the stated vaccination-rate classification of the reinfection-driven backward-bifurcation threshold.

The claim is proved algebraically from the published reinfection-threshold formula. The essential checks are:

1. Substituting \(x=\alpha\sigma/\mu\) transforms the source ratio into \(1-(1-\sigma)x/(1+x)^2\).
2. Differentiation gives \((1-\sigma)(x-1)/(1+x)^3\), so for \(0<\sigma<1\) there is exactly one interior minimizer, \(x=1\).
3. The fixed-reinfection boundary \(r=f(x)\) reduces to \(qx^2+(2q-c)x+q=0\), with discriminant \(c(c-4q)\) and root product one.
4. The strict sign of \(r-f(x)\) follows from the unique minimum and the two limits \(f(x)\to1\).

`verify.py` uses exact rational arithmetic to replay the normalization and a nontrivial example \(\sigma=1/2\), \(r=8/9\), where the two boundary roots are \(1/2\) and \(2\). It prints `VERIFY_OK` only if all exact checks pass. This finite replay is a consistency check, not evidence for the general quantifiers.

The verification does not test global dynamics, compute \(R_0^C\), or establish any claim outside the stated local bifurcation threshold.
