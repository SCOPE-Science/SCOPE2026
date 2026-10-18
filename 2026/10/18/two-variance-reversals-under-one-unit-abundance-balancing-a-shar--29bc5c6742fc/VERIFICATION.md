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

# Reproducibility and evidence

The standalone `verify_rarefaction.py` and `bruteforce_census.py` both run on ordinary Python 3 without dependencies. Its primary checks, executed against the actual included program, are:

1. Generate every nonincreasing positive integer partition of totals \(N=2,\ldots,8\), including those with one species (which have no eligible transfers).
2. Deduplicate every eligible one-individual balancing transfer and compute exact integer signs of all sample-size variance differences. Confirm transfer counts \((0,0,1,2,5,9,17)\) and that the unique profile pair with at least two reversals is \((4,3,1)\to(4,2,2)\) at \(N=8\).
3. Enumerate every possible subset at each sample size of the eight-individual example; verify direct first and second moments equal the exact binomial-moment formulas.
4. Expand each all-size numerator difference for \(m=2,3,7\) as a polynomial in \(t=k-1\) with rational coefficients. Check their coefficientwise strict signs and compare evaluation with raw binomial moments at \(k=1,2,3,10,100,1000\).

Complete runs reported `ALL CERTIFICATES PASS` and `DIRECT FINITE-CENSUS CERTIFICATE PASS`, respectively. The alternate program derives all small-census variance values directly from individual samples instead of reusing the second-moment identity. No numerical tolerance, floating-point approximation or Monte Carlo test is used. The all-size conclusion rests on the symbolic coefficient signs, not on finitely many substitutions. The finite census is exhaustive only through eight individuals and is invoked only to establish the first-occurrence lower bound and uniqueness there.

The scientific assessment is a self-review; there is no independent audit, proof certification, empirical ecological test, or exhaustive survey of all published mathematical literature.
