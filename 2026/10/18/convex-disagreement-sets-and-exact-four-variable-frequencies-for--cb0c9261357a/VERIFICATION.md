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

# Reproducibility and boundaries

The standalone checker `verify_positive_equations.py` uses only Python's standard library. It verifies, for each number of variables one through four, that the truth-table enumeration and recursive lower/upper-slice enumeration produce identical positive term-function sets; that the resulting disagreement masks are exactly the independently enumerated order-convex subsets avoiding the two constant assignments; and that the 166 four-variable term functions give the displayed 15-cell Hamming-distance distribution across all 27556 ordered pairs.

Run `python3 verify_positive_equations.py` and expect the final line `POSITIVE_EQUATIONAL_CONVEXITY_VERIFY_OK`. The checker is exhaustive only through four variables; the statements for arbitrary arity are established by the proof in `RESULT.md`. A finite check is not a replacement for that proof. Previously known sequence entries are cross-checks, not novel certifications. No independent audit has been performed.
