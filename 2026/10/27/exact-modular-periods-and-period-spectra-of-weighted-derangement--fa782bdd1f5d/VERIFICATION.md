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
# Reproducible finite checks

Run `python3 verify.py` from the extracted package directory, using only the Python standard library.

The verifier computes exact modular recurrences for all \(773\) unit-parameter pairs with \(2\le m\le50\), examines \(271888\) shift comparisons for the proposed period, and excludes \(5908\) proper-divisor candidates by explicit mismatches. It separately constructs the full period spectrum of every one of the \(49\) tested moduli and checks \(56\) direct weighted-permutation sums for sizes \(0\le n\le7\). The largest predicted period checked is \(2162\).

Observed output:

`VERIFY_OK: 773 coprime parameter/modulus combinations; 271888 shift comparisons; 5908 proper-divisor obstructions; 49 full modular period spectra; 56 direct weighted-permutation sums; maximum checked least period 2162`

The infinite least-period statement, Carmichael-exponent spectrum, and boundary conditions are proved symbolically in `RESULT.md`. Finite computations cannot prove results for unbounded moduli or all weights. The nonunit case is outside the claimed domain. Independent audit status: not performed.
