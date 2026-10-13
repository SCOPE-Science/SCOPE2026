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
# Reproduction and verification boundaries

Run `python3 verify.py` using Python 3 and its standard library. The exact-arithmetic test independently compares the bi-unitary divisor definition to the multiplicative prime-power formula for each integer up to 256, checks 26 rational prime-tail witnesses, the local-scale set \(\{1,17/16,9/8,153/128,5/4,4/3,45/32,3/2\}\), maximum adjacent ratio \(16/15\), and the rational inequality deduced from \(\pi>223/71\).

Expected result:

`EXACT_CERTIFICATE_OK definition_checks=256 finite_tail_primes=10 witness_factors=26 boundary_intervals=8 max_ratio=16/15 endpoint=pi^2/6`

The statement for all primes \(p\ge41\) is proved with the fifth Ramanujan-prime theorem \(R_5=41\), not with a finite numerical test. The binary-series lemma and Euler product are supplied explicitly in RESULT.md. Finite execution alone establishes neither the infinite prime bound nor originality. No external independent audit is represented as complete.
