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

The proof in `RESULT.md` is the primary verification. It establishes the exact failed-state reset, the geometric-trial mean-time identity for this state, and the global one-variable extremum without finite enumeration.

`artifacts/verify.py` provides independent finite arithmetic checks. It bisects the unique root of \(\tan(x/2)=x\), checks \(\sin x_*=(1-\cos x_*)/x_*\), verifies the direct complete-graph transition formula and failed-state proportionality for several \((N,m,J,\tau)\), confirms the best exponential rate \(r=NJ\), and tests the sharp renewal inequality on a deterministic family of finite-support laws. The finite tests are corroborative only; they do not prove the universal quantifier over waiting-time distributions.

Scientific limits: the theorem assumes the uniform survivor state, projective detection of the fixed target subspace, iid renewal waiting times with finite positive mean, and the fully connected Hamiltonian. Adaptive schedules, non-renewal dependence, weak measurements, arbitrary initial bright states, and other Hamiltonians are not covered.
