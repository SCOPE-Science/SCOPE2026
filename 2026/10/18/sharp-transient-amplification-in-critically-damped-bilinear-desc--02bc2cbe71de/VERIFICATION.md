---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The real skew matrix J=M/a squares to −I and has conjugate complex eigenspaces, so the Euclidean product-norm computation splits into identical-norm B and conjugate B blocks. The real induced norm equals the complexified norm: writing a complex input as x+iy splits both squared norms into sums of real squared norms. Direct subtraction of λ=(1−i)/2 from B gives a nonzero rank-one N with N²=0, trace zero and Frobenius square 1. Thus B^k=λ^k(I+kN/λ), and the latter parenthesized matrix has determinant 1 and squared Frobenius norm 2+2k². Solving the quadratic for its squared singular values gives 1+k²+k√(k²+2), proving the exact power norm and the asymptotic coefficient 2. The finite candidates 0,1,2 are smaller than k=3; in particular 99>96 verifies the k=3 versus k=2 radical comparison. For k≥4 the monotone upper bound 2^(−k)(2k²+2) starts at 34/16, below the k=3 value. On a synchronized modal vector (w,w), the two components of N(w,w) are (λw, conjugate(λ)w); dividing by λ gives the stated primal and auxiliary powers, and the consecutive primal squared-gain ratio drops below 1 exactly when k≥2. The weak 3/4 bound from the DGDA reference is compatible. The sharper general inequality printed in the same reference, at its repeated-root endpoint, is not compatible; the frozen statement carefully refers to the weaker bound only.

## originality

PASS

The algorithm, chosen steps and spectral mode analysis are prior. The strongest inspected DGDA source does not give the exact Euclidean norm of every power, the two distinct sharp discrete peaks, or a correct pure-rate estimate at the defective boundary. Its displayed general rate would in fact imply the false pure 2^(−k) estimate there, even though its separately stated weaker rate is valid. The distinct contribution is the sharp amplification and finite-time contrast, not Jordan calculus or the spectral eigenvalues alone.

## value

PASS

This is the critical boundary of the recommended step choice at best conditioning, not an artificial slice. Exact gains quantify how much transient error is missed by asymptotic spectral reasoning, and the synchronized peak shows the effect can reach original variables under a standard initialization, not merely an adversarial auxiliary state. The formula identifies why one printed rate cannot hold at boundary equality and precisely separates it from the weaker valid one.

The dated certificate retains the supplied scientific assessment, sources and limitations.
