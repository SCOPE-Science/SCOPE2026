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

The mathematical derivation is given in `RESULT.md`. Run `python3 CHECKER.py` using Python 3 and its standard library. The checker separately constructs finite fields of cardinalities \(5\), \(25\) and \(125\), loops through every ordered coefficient triple, eliminates singular members using the stated smoothness criterion, evaluates the three genus-one Hasse conditions and checks every predicted stratum and Hasse-intersection number. All tests completed successfully for the distributed package.

Finite tests do not certify all extensions: the proof for arbitrary \(5^n\) uses the quadratic-character identity \(\sum_u\chi(u^2-4)=-1\), explicit quadratic discriminants and the fractional-linear substitution displayed in the paper. Bibliographic overlap remains a separate judgment, and no independent audit has been performed.
