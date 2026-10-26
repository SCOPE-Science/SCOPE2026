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

# Reproduction and limitations

`verify.py` is a standalone Python program using `sympy` and `mpmath` (standard `math` is also imported). Run `python verify.py`; the output is `VERIFY_OK 91 exact symbolic identities and mesh/log-domain diagnostics`.

Symbolic identities checked: \(g'/g=2/\delta^3\) and \(g''/g=4/\delta^6-6/\delta^4\). Eleven mesh counts \(N\in\{4,5,6,8,12,16,32,64,128,256,512\}\) were checked for irrational-offset inclusion, shape-exponent sign, the rigorous logarithmic lower bound, and the full-step bounded remainder. For four small meshes, the original two-stage rule was evaluated directly at high precision and compared with the derived decomposition.

These finite checks do not certify any assertion for all mesh counts. The proof's symbolic inequalities, valid for every \(N\ge4\), supply that universal conclusion. No checks of a recursively propagated numerical solution or finite-precision overflow behavior were claimed. No independent audit was performed.
