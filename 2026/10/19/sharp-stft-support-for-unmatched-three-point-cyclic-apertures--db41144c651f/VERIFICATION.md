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

Run `python3 checker.py` from the directory containing the standalone script. The script requires only the Python standard library. It exhaustively examines all nontranslated three-element support pairs in the prime cyclic groups of orders \(5,7,11,13\), creates the nine product-to-time incidences, counts double-overlap slices, and evaluates the binary cancellation feasibility by exact Gaussian elimination over \(\mathbb F_2\). It checks the reflection/nonprogression criterion and the exceptional-pair multiplicities, prints the class distributions, and terminates with `CHECK_PASS` on success.

Checked ordered support-pair totals are \(50\), \(980\), \(25{,}410\), and \(78{,}078\). Exceptional reflected nonprogression counts are \(0\), \(98\), \(1{,}210\), and \(2{,}704\). The checker also directly evaluates exact cyclotomic Fourier vanishing for all \(64\) sign patterns in each of four examples: unmatched \(p=5\), ordinary unmatched \(p=7\), reflected nonprogression \(p=7\), and ordinary unmatched \(p=11\). The exact arithmetic verifies the finite combinatorial classification and these sign witnesses, not all possible complex coefficients. The proof in `RESULT.md` independently establishes the coefficient-uniform lower bound using each two-term Fourier slice and the odd-prime cross-ratio obstruction; the sign-system argument constructs coefficient choices attaining it. Neither a finite enumeration nor the checker constitutes an infinite-family certificate or an independent review.
