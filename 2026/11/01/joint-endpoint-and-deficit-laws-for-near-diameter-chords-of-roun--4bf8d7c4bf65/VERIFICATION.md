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

# Reproducibility and limitations

Run `python verification/verify_cylinder.py` using NumPy and SciPy in a standard Python environment. The script evaluates finite-deficit endpoint-pair integrals with exact distance, exact cap/side flux factors, and spherical surface weights, then compares with the predicted asymptotics for \(d=3,4,5\). It tests \((R,H)=(1,2)\) at each dimension and \((R,H)=(1,1)\) in dimension four, at deficits \(\varepsilon=0.025\) and \(0.008\). Results were within nine percent of the limiting coefficient and improved consistently at the smaller deficit. It checks that the summed four-type constant equals \(3/32\) at \(d=4,R=1,H=2\).

The numerical integrations use a deterministic seed but randomized quasi-Monte-Carlo nodes; they do not prove asymptotic orders or historical originality. The analytic proof, including localization, Jacobian and beta integrals, appears in RESULT.md. Independent review has not been performed; an inaccessible relevant 1980 full text remains a priority limitation.
