---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed the upper count by placing a support of size s at the s cheapest exponents, multiplying 1+floor(n/2^(j+1)) over those exponents, then allowing at most 2^(k+1) supports. This gives log_2 b_{<=t} <= tk-t^2/2+O(k) for admissible t. The matching lower bound fixes consecutive exponents 0 through s-1, draws the multiplicity parameters at j>=1 from independent boxes of total cost <=n/4, and completes the sum at j=0. Oddness of n and of the baseline 2^s-1 gives an integer nonnegative parameter at j=0, and different boxed choices give different partitions. The log volume is sk-s^2/2+O(k log(k+2)) with the error uniform in the allowed s; use s=t for fixed epsilon and s=k-O(log k) for the total. Subtraction yields exactly the two-sided tail exponent with its stated error. The support weight 2^(J-1) then gives the claimed upper bound 2^k and lower bound 2^t(1-o(1)) for the mean on odd indices only. Independently checked exact support histograms for 1<=n<=255 by direct odd-multiplicity recursion against H(2m)=H(m) and H(2m+1)=H(2m-1)+zH(m), with H(0)=1 and H(1)=z. The finite replay is python3 /tmp/opencode/frozen_independent_checks.py (line beginning 3:).

## originality

PASS

The supported distinct result is the matching lower and upper logarithmic rate for sparse support. The strongest indexed comparison gives the same ratio exponent and the same leading support upper bound, so neither is credited as independently distinct. The dates of the two records do not establish historical priority. The matching lower bound is a material additional conclusion and the main frozen claim is not covered by the compared statements.

## value

PASS

The two-sided law measures how rarely a uniformly chosen odd-multiplicity partition uses a given small fraction of the available sizes. It goes beyond proving concentration near full logarithmic support, and reveals the statistic connecting two established self-similar sequences. This is a meaningful distributional result even after crediting the existing ratio and one-sided bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
