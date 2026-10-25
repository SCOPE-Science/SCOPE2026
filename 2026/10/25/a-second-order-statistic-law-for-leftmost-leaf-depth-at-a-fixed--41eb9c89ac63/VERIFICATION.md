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

# Verification instructions and boundaries
Run `python3 verify.py` in the same directory using Python 3 and its standard library. The program enumerates all Dyck words through semilength 10, verifies every exact conditional count, the Narayana margins, conditional mean and variance, all conditional tails and finite adjacent stochastic inequalities. Independently, it checks second-order statistics over all uniform subsets through size 10 and every full permutation-coupling order through size 7. Successful output is `PASS: 7672 exact assertions, no random sampling`.

These checks are finite exact consistency tests. The proof for arbitrary tree size uses Lagrange inversion and a set/order-statistic bijection; the three limits follow from elementary finite-population sampling convergence. None of the limit theorems is claimed to be proven by running this code. A general previous enumeration might imply part of the result; that historical issue was not independently resolved.
