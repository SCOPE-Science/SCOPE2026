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

The proof is symbolic and all-parameter. The standalone script `verify_johnson_degree2.py` is corroborative: with exact rational arithmetic it checks every \(4\le n\le120\), \(2\le k\le n/2\), including the hypergeometric kernel mean and second moment, the sign interval, the discrete antiderivative, and equality of the direct absolute sum with the boundary formula.

A replay from the packaged file returned:

`VERIFY_OK exact_cases=3481 target=0.483941449038 bulk=0.200:0.483807292964,0.333:0.483344970046,0.500:0.482266877316`

The finite replay is not used as proof for all parameters. The asymptotic limit rests on the standard hypergeometric central limit theorem and the exact identity \(\mathbb E Q_{n,k}(J)^2=d_2\), which gives uniform integrability after division by \(n\).
