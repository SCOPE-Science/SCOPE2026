---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For n=2^a p^b, a,b≥1, p odd prime >A+1 (A=2^a), cyclotomic factors have degree polynomial H_A(z)∏_{j=1}^b H_A(z^((p-1)p^(j-1))), H_A=(1+z)(1+...+z^(A-1))=1+2∑_{u=1}^{A-1}z^u+z^A. Since A<p-1, u0 is unique modulo p-1, and remaining uj∈[0,A] are unique base-p digits; all fibers and the binomial multiplicity histogram follow. Consecutive allowed digit blocks have differences Δ_k=p^k-A∑_{i<k}p^i, giving every gap length L_k=(p-1-A)p^k-1 with multiplicity A(A+1)^(b-1-k). Under scaling by Ap^b, reversed independent digit strings converge with coupling/Hausdorff error ≤p^-b to disjoint-map Cantor support dim log(A+1)/log p and Bernoulli measure of dimension [log A+(log 2)/A]/log p by cylinder masses and strong law. Independently multiplied cyclotomic degree factors as exact integers for (a,p,b)=(1,5,2),(2,7,2),(3,11,1); full predicted coefficient dict and all gap lengths matched. The all-parameter proof is digital/algebraic, not a finite extrapolation.

## originality

PASS

The φ-practical threshold and digital factorization technique are firmly prior; close published work explicitly handles the complementary p≤A+1 case, while another superficially similar digit theorem involves sums of integer divisors and different threshold. Actual source comparison supports a previously unreported exact family-wide gap/fiber distribution and support/measure limit in the non-practical regime, with qualified priority because it follows by elementary arithmetic once the layer generating polynomial is written.

## value

PASS

The arithmetic degree set of divisors of X^n−1 is the natural problem behind φ-practicality. In a complete infinite nonpractical regime this work gives all degree fibers, every omitted interval, number of uniquely represented interior degrees, and fractal distribution/dimension of a uniformly sampled divisor. These precise natural invariants can be used directly without requiring an unrelated downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
