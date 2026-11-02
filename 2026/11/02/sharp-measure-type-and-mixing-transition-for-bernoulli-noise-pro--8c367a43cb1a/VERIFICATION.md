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

Run `python3 verify.py` with Python 3.11+ (standard library only).

The verifier performs 18 exact rational checks of image geometry in the three parameter regimes, proves directly by rational endpoint propagation that the five-sign word `----+` sends every point in \([-3,3]\) to zero for the example \(q=2/3\), \(t=1\), \(b=2\), and computes the exact ten-step probability distribution from zero, including its zero mass \(83/512\). A successful invocation outputs:

`VERIFY_OK interval-regimes=18, exact-reset-word=----+, reset_probability>=1/32, exact-distribution-steps=10, mass_zero= 83/512 states= 205`

The checked example corresponds to \(a=1\), \(h=1/3\), \(\lambda=3\), \(\sigma=6\), and it gives an explicit uniform five-step reset probability at least \(1/32\). The ten-step mass is transient, not an exact stationary mass.

The general results are mathematical consequences of the proof in `RESULT.md`: contraction for existence and uniqueness, affine separation at \(q<1/2\), exact interval-halving at equality, and a common-atom minorization in the overlapping branch. The finite test does not certify the infinite assertions, generalize beyond the stated hypotheses, or constitute an independent audit.
