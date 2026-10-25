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

# Verification record

The proof in `RESULT.md` establishes every universal assertion. The standalone program `verify.py` separately reconstructs exact rational projective eigenvector identities at \(s_*=28/45\), tests the gap sign on both sides of the threshold, and evaluates 12,000 admissible randomized parameter configurations.

**Actual executable check:** `python verify.py` completed successfully, reporting 10,469 strict-regime cases, 1,531 crossover cases, and threshold floating-point equality residual no larger than approximately \(2.22	imes10^{-16}\). No stochastic simulation, symbolic certificate, or finite enumeration is represented as an infinite proof.

The decisive algebraic conditions are \(0<b<c\), \(x_0>x_1>0\), \(0<y_0<y_1\), and \(u_1(x_0-x_1)>u_2(y_1-y_0)\). At the exact example parameters \(u=(1,1)\), \(v_0=(2,1)\), \(v_1=(1,19/10)\), \((b,c)=(1/4,3/4)\), the exact common eigenvalue and positive eigenvector are \(49/15\) and \((9,10)\).

**Limits:** Test counts are finite; rounding makes small near-threshold differences numerically delicate. The spectral-projector proof avoids this numerical issue. Priority has not been externally certified and empirical predictive validity was not tested.
