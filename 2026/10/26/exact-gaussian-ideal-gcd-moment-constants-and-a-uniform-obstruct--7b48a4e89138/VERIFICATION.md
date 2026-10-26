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
# Reproducibility and verification

Run `python3 verify_gaussian_gcd.py` using Python 3 and only the standard library. The expected success line is:

`VERIFY_OK: 10000 exact ideal-count inequalities and 4 complete Gaussian-gcd pair enumerations (moments 2..5).`

The script computes the Gaussian-ideal norm coefficients in a second way from the Dirichlet product \(\zeta(s)L(s,\chi_4)\), compares with every norm of a quadrant Gaussian-integer representative for norm cutoffs \(8,15,24,40\), and calculates all ordered-pair gcd norms by exact integer Gaussian Euclidean division. As a genuinely different combinatorial calculation, it uses the Dirichlet inverse of the ideal-norm coefficient sequence to recover coprime-pair counts and grouped positive-moment sums. All exact equalities matched for exponents \(2\) through \(5\).

The program also verifies \(A(k)\le k\) and coefficientwise comparison through \(k=10000\), including the gap at \(k=4\). Finite runs corroborate algebraic identities and normalization, but do not prove the all-index lattice bound, analytic asymptotic or literature originality. Those depend on the stated proof and scientific source comparisons. Independent external audit has not been performed.
