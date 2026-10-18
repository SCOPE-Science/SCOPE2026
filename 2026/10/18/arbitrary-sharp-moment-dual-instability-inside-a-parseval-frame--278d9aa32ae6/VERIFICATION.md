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

The frame is Parseval because its squared analysis coefficients satisfy \(c_j^2+d_j^2=1\). The sharp lower bound for all constrained duals is the coefficient identity \(d_N\langle U_1e_N,e_N\rangle=1\); the explicit finite-rank correction \(U_N\) attains \(\|U_N\|^2=b_N\). The infinite restriction is impossible because \(D\) is compact, injective and not onto. Compactness also proves the uniform moment-defect lower bound one, whereas the finite moment defects converge strongly to zero.

The accompanying `checker.py` uses rational coefficients from Pythagorean triples to verify finite Parseval and reconstruction identities, monotonic costs and the optimizers over several finite truncations. Run `python checker.py` with Python 3. It does not test the universally quantified lower bound over all nondiagonal duals, which is proved analytically. The residual scientific limitation is possible unrecognized prior realization coverage; independent audit and publication-priority validation are not performed.
