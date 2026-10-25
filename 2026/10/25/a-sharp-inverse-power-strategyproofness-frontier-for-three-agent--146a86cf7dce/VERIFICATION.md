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

The analytical verification uses the three exhaustive nearest-distance regimes \(w\le u\le v\), \(u\le w\le v\), and \(u\le v\le w\). The potential inequality \(1-P+rP'\ge0\) integrates along a numerical (not necessarily geometrically realizable) interpolation between report-distance vectors. The proof does not depend on finite experiments.

The ancillary standard-library program `verify_inverse_power.py` tested 62,500 exact rational truthful/deviation comparisons on 15,625 weighted shortest-path metrics at exponents \(0,1,2,3\). The specified rational counterexample at exponent \(4\) has a strictly positive gain, and the cubic stationary root is bracketed by two exact rationals. Reproduce with `python3 verify_inverse_power.py`.

Limitations: finite checks do not certify the universal quantifiers, and a full independent mathematical audit has not been performed. The statement concerns exactly three agents and fixed exponents.
