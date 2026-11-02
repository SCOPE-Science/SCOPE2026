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

# Verification of the six-mer certificate

Run `python3 verify.py` with Python 3. The program prints `VERIFY_OK` after checking all finite premises used in the proof; no external packages, online services or solver certificates are required.

The checks are: the five special high-potential states and their reverse-complement low-potential partners; absence of a one-bit shift from any low-potential state to a high-potential state; antisymmetry of the potential; nonnegativity and reverse-complement invariance of all \(64\) six-bit edge costs; exactly eight reverse-complement-fixed six-mers with total cost \(18\); full edge-cost sum \(64\); exactly \(36\) classes with class-cost sum \(41\); coverage by the explicit \(44\)-bit word with \(39\) windows and three zero-cost duplicate classes; and the class-count-tight short witnesses at orders two and four. Two implementations compute the order-six classes, one using bitstrings and another using integers. The smaller equality cases are also enumerated directly.

The mathematical lower bound rests on a telescoping identity and the explicit nonnegative potential. It applies to all finite binary words of the specified type; finite tests alone would not prove that statement. The displayed witness independently supplies the upper bound.

Limits: only ordinary linear reverse-complement factor coverage is tested; no circular, multi-probe, higher-order, or DNA-alphabet claim follows. The review is not independent validation.
