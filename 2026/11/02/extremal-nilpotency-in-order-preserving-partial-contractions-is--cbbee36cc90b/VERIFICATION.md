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

# Reproducibility and scientific limits

Run `python3 verify.py` with Python 3 (standard library only). The script constructs every ordered pair of equal-size subsets of \([n]\) for \(0\le n\le12\). Each pair specifies the unique increasing injection. It tests contraction by consecutive gaps and then computes the least zero power by iterating that partial injection. The independently computed index is compared against the proposed condition \(\nu(\alpha)=\operatorname{rank}(\alpha)+1\).

For every chain size and rank, the program compares this direct enumeration to an independent integer-partition dynamic program. It also checks all total counts against the coefficients of the Euler-product generating function. The program reports `VERIFY_OK` after all checks pass. Representative full rank profiles are \([0,12,6,2,0]\) for \(n=4\), \([0,56,68,50,28,14,6,2,0]\) for \(n=8\), and \([0,132,250,272,218,148,90,52,28,14,6,2,0]\) for \(n=12\).

These are exhaustive **finite** tests, not an infinite proof. All-chain correctness is supplied by the directed-path classification and partition-counting argument in `RESULT.md`. The large-chain asymptotic uses the classical Hardy–Ramanujan partition-number asymptotic and a dominated Riemann-sum argument, not finite experiments. Independently conducted mathematical audit has not been performed.
