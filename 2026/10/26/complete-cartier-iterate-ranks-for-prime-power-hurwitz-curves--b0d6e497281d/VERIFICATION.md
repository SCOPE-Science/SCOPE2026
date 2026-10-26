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

# Exact verification and limits

`hurwitz_cartier_checker.py` is a standalone Python-standard-library check. It independently enumerates every coefficient of the relevant trinomial power in representative characteristics and reconstructs all nonzero Cartier matrix columns rather than assuming the asserted transition rule. It iterates these partial monomial maps, validates distinct targets, checks the rank formula at every power and compares the first-step rank with the independently published \(a\)-number formula. It also validates the nonnegative nilpotent-string length distribution and dimension sum.

The run was successful and returned `VERIFY_OK` for \(p=2,3,5,7,11\), with exponents through five, four, three, two and two respectively. One example is \(p=3,e=3\): computed ranks \((378,270,216,216,216)\), with nilpotent-string multiplicities \((54,54)\). The verifier’s finite examples are checks rather than a complete proof. The general argument appears in RESULT.md and covers every prime and positive exponent.

The public research files have no independent scientific audit or independent validation. The only review status recorded is a self-review. The possibility of prior logically equivalent work remains a limitation.
