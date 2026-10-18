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

# Reproduction and scientific limits

Run `python3 verify.py` in a directory containing this document and the verification program. The checker uses only the Python standard library and rational arithmetic. Successful output states that 103746 five-weight/parameter combinations were checked, including 1865 light-stake combinations, and that the exact polynomial identities and extremizing construction checks passed.

The analytical proof in `RESULT.md` establishes all real weights and parameters in the specified interval. Finite enumeration alone is not a proof for real weights, and the numerical checks cannot assess priority in the wider literature. The proof requires independent Bernoulli variables with a common parameter, at most five nonnegative normalized weights, and the weak threshold event; no other model is certified by these checks.

Independent audit: not performed.
