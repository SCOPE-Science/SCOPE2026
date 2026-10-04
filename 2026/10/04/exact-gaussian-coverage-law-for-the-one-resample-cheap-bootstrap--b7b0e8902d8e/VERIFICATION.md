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

The proof reduces the finite-sample law to multinomial occupancies and then derives the asymptotic coefficient analytically from exact collision moments. The standalone `verify.py` checks the finite combinatorics without external libraries.

Checks performed by the packaged script:

- exhaustive labeled bootstrap enumeration agrees with the occupancy recurrence for every \(2\le n\le4\);
- occupancy counts sum exactly to \(n^n\) for every \(2\le n\le30\);
- exact second, third, and fourth central-moment formulas for \(C_n\) agree with recurrence values for every \(2\le n\le30\);
- the quoted \(95\%\) coverages at \(n=2,10,20,30\) are reproduced to floating-point tolerance;
- the closed-form \(1/n\) coefficient at \(\alpha=0.05\) is reproduced and agrees with the finite-\(n\) trend.

The finite checks support the algebra but do not constitute an exhaustive proof for arbitrary \(n\). The all-\(n\) result rests on the Gaussian orthogonality argument, the exact occupancy identity, Jensen's inequality, and the explicit collision-moment expansion given in `RESULT.md`.
