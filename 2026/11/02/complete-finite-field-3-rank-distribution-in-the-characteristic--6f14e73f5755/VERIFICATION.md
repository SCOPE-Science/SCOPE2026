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

# Reproducibility and exact verification

The standalone Python standard-library verifier `verify_ciani3.py` uses explicit polynomial-basis models of \(\mathbb F_3\), \(\mathbb F_9=\mathbb F_3[t]/(t^2+1)\), and \(\mathbb F_{27}=\mathbb F_3[t]/(t^3-t-1)\). It enumerates every coefficient triple, computes the smoothness discriminant and number of vanishing elliptic Hasse coefficients, and compares complete totals and all four strata to the exact polynomial formulas. The accompanying `ciani3_output.txt` is the output from an actual successful execution and ends with `VERIFY_OK`.

The exact quartic smoothness criterion, the character-\(2\) Jacobian decomposition, the characteristic-three elliptic Hasse invariant, and the all-extension quadratic-character-sum proof appear in `RESULT.md`; these are mathematical arguments that the finite enumeration does **not** replace. In particular, verification at the three displayed fields is not itself proof for every extension.

No independent scientific audit has been performed.
