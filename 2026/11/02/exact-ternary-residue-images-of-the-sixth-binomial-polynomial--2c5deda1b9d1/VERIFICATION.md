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
# Verification of the ternary binomial image theorem

The exact argument is contained in `RESULT.md`; `verify.py` supplies a separate standard-library implementation of finite consistency checks. It does not constitute an independent mathematical audit.

To replay, run `python3 verify.py` in a directory containing the standalone script. The script multiplies six integer linear factors into rational polynomials, checks all coefficientwise 3-adic branch identities, computes a unique critical-point lift by Hensel's digit rule, and compares predicted images and exact cardinalities against exhaustive direct evaluation for each modulus \(3^k\) with \(1\le k\le9\).

The checked residue counts, in order of increasing \(k\), are \(2,5,13,35,103,305,913,2735,8203\). The search over \(0\le n<3^{k+2}\) is complete for each *tested* modulus because \(\nu_3(6!)=2\). Completeness for every positive exponent follows from the branch proof, not from this finite experiment. The computational test also does not address priority in earlier publications.
