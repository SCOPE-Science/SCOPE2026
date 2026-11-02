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

Run `python3 verify.py` with Python 3 and its standard library. The saved output is `verify_output.txt`, and the final sentinel must be `VERIFY_OK`.

The script constructs \(Q_p(a)\) and \(P_p(a)\) by exact multinomial coefficients reduced modulo \(p\), then verifies the identity \(P_p=c_p(a^2-4)^{m+1}Q_p\), the relevant second-order differential equations, separability, and exclusion of \(a=\pm2\) for every applicable prime below 200. It also verifies the characteristic-17 and characteristic-23 examples and their rational roots where stated. The test was executed successfully against the exact packaged source, with 23 primes and final `VERIFY_OK`.

The uniform claim for all primes is established mathematically by the polynomial differential equation, recurrence uniqueness, and leading-term argument recorded in `RESULT.md`; no amount of finite testing alone proves the infinite result. The geometric claims additionally use the genus-three Picard differential basis, the interpretation of Cartier stable rank as \(p\)-rank, Newton slope symmetry, and the complete geometric invariant of the bielliptic Picard pencil.

A remaining literature-access limitation is that the 1991 Estrada-Sarlabous study was inspected by abstract, not by complete primary text; its implications for historical priority require independent review. No external scientific audit was performed.
