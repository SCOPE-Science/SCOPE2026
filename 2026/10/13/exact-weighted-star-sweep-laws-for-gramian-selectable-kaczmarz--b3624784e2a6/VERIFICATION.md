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

Run `python3 verify.py` with a standard Python 3 interpreter. It uses exact rational arithmetic, not random simulations. The script checks the closed GSSRK and ordinary RK means against two separately written finite-state recurrence solvers for every \(m\in\{2,\ldots,10\}\) and each \(w\in\{1/4,1/2,1,3/2,2,5\}\), totaling 108 recurrence identities, plus 18 equal-weight identities and nine star-state walks. Expected first line: `PASS 126 exact closed-form/recurrence equalities; source transition states checked for m=2..10.`

The analytic proof is in RESULT.md, including the regeneration argument, generalized hockey-stick sum, probability of center being the last new type, and gamma-ratio asymptotics. The finite tests alone do not establish the quantified real-weight and arbitrary-dimension theorem. The certificate is an upper bound on possible exact-solution hitting time and is not an observation of actual earliest hitting. No independent validation has been performed.
