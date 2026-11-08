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

# Verification record

`verify_cycles.py` is a standalone Python 3 standard-library script. Run it with `python3 verify_cycles.py`; the executed program returned `VERIFY_OK` on the actual file supplied with this proof. The program verifies exact integer polynomial differentiation; an exact rational greatest-common-divisor computation establishing squarefreeness; the nonzero value of the quartic and the relevant map denominator on each of five intervals; and an enclosure of the derivative throughout 64 consecutive exact rational subintervals of each orbit interval. It then bounds the rational image of each center, verifies every cyclic inclusion by the mean value theorem and checks the strict return-contraction bounds \(3/20<1\) and \(27/250<1\).

Every proof-relevant comparison uses rational integers and fractions. Diagnostics printed as decimals are not used as proofs. Existence of infinitely many orbit points, or dynamics outside the declared neighborhoods, is not inferred from a numerical sample; the fixed point and complex attraction follow analytically. Independent validation is not claimed. The proof does not establish a common open basin of the three algorithms, a minimal quartic degree, or stability under finite precision.
