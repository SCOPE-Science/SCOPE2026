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

# Verification details

The standalone `verify.py` uses only Python standard-library modules and accepts no arguments. Run it with `python3 verify.py` from the directory containing the extracted source. The check exhaustively enumerates every binary reduced row-echelon subspace in dimensions \(k\le4\), lengths \(s\le7\), imposing full-support and maximum-codeword-weight conditions directly. It independently enumerates every nonzero-column multiset of size \(s\) in \(\mathbb F_2^k\), computes span and all codeword weights, weights the multiset by its multinomial factor, and divides by the order of \(\operatorname{GL}(k,2)\). This second algorithm does not use reduced row-echelon forms.

The two exact enumerations were executed successfully and agreed on all forty support/rank cells. Output ends in `VERIFY_OK`. The support totals are \((1,1,2,6,26,91,100,30)\), and the rank-by-support values are in `RESULT.md`. Exact length totals checked include \(1,2,5,16,67,307,3811,10357,202567,134157337\) for lengths \(0,1,2,3,4,5,7,8,12,30\), respectively.

The infinite-length theorem depends on the proved \(k\le4\) and \(s\le7\) bounds and unique support decomposition, not on testing finitely many ambient lengths. The code verifies a finite exhaustive calculation, not the validity of arbitrary external literature or independent scientific certification. Independent assessment has not been performed.
