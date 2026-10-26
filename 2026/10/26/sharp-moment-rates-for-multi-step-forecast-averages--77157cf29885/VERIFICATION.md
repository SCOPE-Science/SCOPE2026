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
Proof checks and limits:
- Reconstructed the residue-class martingale-difference decomposition for every deterministic horizon \(K_N\).
- Checked the \(L^p\) exponent by applying martingale inequalities to each residue class and summing with Minkowski's inequality.
- Checked the uniform-integrability step by clipping, applying the bounded-variable result at fixed clipping level, and controlling the remainder in \(L^1\).
- Checked the lower examples algebraically: the exactly-one-spike probability is \((1-1/m)^{m-1}	o e^{-1}\); the Rademacher block example has the central-limit scale \(m^{-1/2}\).
- The constants \(C_p\) are not optimized. Uniform integrability is not claimed to be necessary for every individual sequence.
