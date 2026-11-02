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

The analytical verification consists of (i) solving the two-state stationary transport equations to recover the Beta prior, (ii) the exact tilted-moment integration-by-parts identity, (iii) checking the sign \((1-b)/z\) of the critical crossing derivative, (iv) monotone likelihood-ratio ordering in the Beta shape parameter, (v) the Gaussian sign-variation bound giving a global mode count, and (vi) direct Gaussian derivative and Taylor calculations for the critical normal form. The new result uses established physical formulas only as independently checked premises, not as a claimed new solution of the stationary law.

Run `python3 verify_pitchfork.py` with Python 3 and its standard library. The included checker carries out 41 finite numerical assertions for representative shape parameters and widths; these checks are not an infinite proof. Numerically the critical variances are approximately 0.53856358 at shape parameter 0.25, 0.31646434 at 0.50, and 0.18327382 at 0.75.

The exact position-density phase boundary and elementary Gaussian heat-flow scaling properties are present in the literature. The verified contribution is the rigorous uniqueness/ordering, exhaustive global mode classification, and explicitly normalized amplitude identities. Publication priority has not been independently certified.
