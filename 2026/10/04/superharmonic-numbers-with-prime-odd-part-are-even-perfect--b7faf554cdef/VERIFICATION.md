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
# Verification

The unrestricted theorem is proved symbolically in `RESULT.md`. The proof uses exact formulas for \(\sigma(2^a p)\) and \(\tau(2^a p)\), Cohen's published prime-support/valuation criterion, multiplicative orders, and the standard lifting-the-exponent identity.

The bundled `verify.py` independently checks the original superharmonic divisibility condition for every integer \(1\le a\le20\) and every odd prime \(p\le200000\). It returns exactly the even-perfect cases in that domain and reports each with index \(1\). The expected output is:

`VERIFY_OK a_max=20 p_bound=200000 hits=[(1, 3, 1), (2, 7, 1), (4, 31, 1), (6, 127, 1), (12, 8191, 1), (16, 131071, 1)]`

This enumeration is only a finite consistency check. It is not used to infer the infinite classification. The theorem does not cover \(2^a p^b\) with \(b>1\) or odd superharmonic numbers.
