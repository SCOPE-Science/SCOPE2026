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

# Mathematical verification

Use `python -m pip install -r requirements.txt` and then `python verify_windmill.py` with Python 3 and SymPy. The program symbolically derives the single- and two-edge increases, checks comparison factorizations and both coincident-damage identities, and independently inverts full grounded Laplacian matrices over exact rationals on six sample parameter pairs. Recorded execution output:

`VERIFY_OK 57 independent exact grounded inverse comparisons, symbolic sign factorizations`

These 57 comparisons corroborate finite instances; they do not establish universal quantifiers. The analytic cut-vertex decomposition, rank-two inverse identity, complete orbit exhaustion, and exact positivity comparisons in `RESULT.md` establish the infinite-family statement. The derivative signs and integer parameter cutoff are proved algebraically there. This is not an independent audit or a formally certified proof.
