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

# Reproduction

Run `python3 verify.py` using an ordinary Python 3 interpreter; the script uses only `fractions` and `math.factorial` from the standard library. It computes exact Gaussian-rational Taylor partial sums of order 80 at dimensionless times 8 and 10 and tests their rational squared moduli against the stated comparison values. The explicit factorial-majorant bound on all omitted terms is checked by an exact fraction comparison. It then verifies the two-qubit isotropic-state threshold and the resulting strict trace-distance and negativity margins.

The analytical proof that the evolution is CPTP at fixed time is based on the random-operational-clock description in [1]; the finite program tests specific algebraic inequalities, not that general theorem or any general numerical simulation. Two independent high-precision evaluations of the Kummer function gave modulus approximately 0.058517134592752596 and 0.111101945588866145. They are not used in the correctness decision. The reference qubit is inert. No independent audit has been performed.
