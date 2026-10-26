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

Run `python3 verify.py` with Python standard library only. The program independently generates the period-doubling prefix from the substitution and from the \(2\)-adic valuation formula, verifies all factor languages up to length \(160\) by comparing their counts to the established factor-complexity formula, checks palindrome pairs by two mathematically equivalent but separately programmed methods, exhaustively compares \(\sigma(w)\) and \(w\) for all binary words to length \(12\), and evaluates the quoted palindromic-periodicity counts through \(32768\). It checks the two explicit length-seven non-pair factors. All finite checks passed on the packaged script before review.

The unrestricted characterization depends on the symbolic reflection and length-doubling proof and independently published factor-count theorem; finite computations do not by themselves establish infinitely many instances. There has been no independent scientific audit.
