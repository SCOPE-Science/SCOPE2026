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

# Reproducibility and limits

Run `python3 artifacts/verify.py`; the saved output is `artifacts/verify_output.txt`. The script uses Python's standard library only. It enumerates ordered pair-sum fibers exactly in tested prime and quadratic-extension fields, tests monomial even maps and intentionally unequal-size even fibers, compares integer-arithmetic fourth moments against the proposed exact formula on pseudorandom Gaussian-integer data, checks sharp examples, and perturbs a maximizing phase to ensure strict loss. The finite tests do not prove the full theorem or independently audit it.

The proof is the field identity \(a^3+b^3=(a+b)^3-3ab(a+b)\), the exact convolution-fiber fourth-moment formula with cross coefficient four, a sharp phase/product-magnitude inequality within each antipodal fiber, and a positive mass-concentration inequality across fibers. Every transition is explained in RESULT.md. The character-orthogonality normalization is counting on the input and uniform probability on the output. No external certification is claimed.
