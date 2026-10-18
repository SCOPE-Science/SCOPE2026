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

# Reproducibility and scope

The combinatorial proof in `RESULT.md` covers all integers \(m\ge3\) in the five specified congruence classes. It uses only the stated rung/rail/twist graph definition and the exact zero/positive surplus identity, without relying on a finite search to extrapolate to an infinite family.

The supplied `checker.py` uses the Python standard library to build every graph edge and independently enumerate all feasible color assignments at the claimed optimum weight for \(m=3,4,5,6,8,9,10\). Its observed counts are, respectively, \(12,48,60,72,96,12,120\). A separate cyclic-word check for \(m=5,11\) fixes one doubly colored rung and enumerates every eligible singleton word, obtaining six assignments in either size. Invoke `python checker.py` to replay. The code does not attempt to infer global optimality, uniqueness or the infinite theorem from enumeration.

The known numerical ordinary three-rainbow optimum from Kuzman's 2019 result is prior work. The new claim is a complete classification **only** for the five stated residue classes and for independent-zero minima. The branch \(m\equiv1\pmod6\) is not assessed. No independent validation has been performed.
