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

## Checks performed

The proof derives the divisibility constraint \(k\mid n\), the composite-parameter bound \(n\le r^2\), and the prime-parameter identity \((p^{a-1}-1)N+(p^{a+1}-1)(\sigma(N)-N)=r(p-1)\) by direct algebra. The three consequent cases exclude all escapes other than distinct-prime semiprimes. For \(r\ge4\), \(r^2\le(r-1)^3\), and odd-prime cubes give equality at infinitely many offsets. No unbounded claim depends on an experiment.

`verify.py` independently enumerates integer solutions for \(n\le200000\) and \(1\le r\le35\), using a divisor-sum sieve, and tests all claimed branches as regression checks. The captured result is in `verification_output.txt`.

## Limits and validation status

The finite check has a stated finite range and cannot certify that no larger counterexample exists; that follows from the paper proof. Some finite exceptional sets below the explicit cutoff remain unclassified for individual offsets \(r\ge4\). This is a self-review only. Independent audit has not been performed.
