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

At each x the degree-n binomial iteration is a martingale absorbed at the endpoints. For the difference with L, its interior masses are nonnegative and its endpoint masses are the negatives of their endpoint-interpolation weights. The total variation is twice survival and the continuous piecewise linear nodal sign function attains it. Survival begins at 1−x^n−(1−x)^n; the Bernstein second-difference formula preserves strict concavity, and reflection then gives the unique maximizer at 1/2. Positive one-step absorption from each interior node makes the norm strictly decreasing. On the polynomials vanishing at both endpoints, the eigenvalues λ₂,…,λ_n are distinct (the two affine eigenvalues are both 1) and the corresponding eigenfunctions restrict to a basis on the interior mesh. The Perron right vector is h_j=(j/n)(1−j/n), with projection of the constant vector h/H_n. The midpoint row gives b_n^T h=λ₂/4 and annihilates odd modes. This proves the exact coefficient, the O_n(λ₄^m) bound at fixed n and the vanishing remainder for n=2,3; it does not assert a nonzero λ₄ coefficient at every degree. The two symmetric modes at n=4 and survival values 1 at time zero and 7/8 after one step give the displayed closed form. An independent rational check at n=4, m=1,2 gave midpoint norms 7/4 and 171/128, with derivative sign switching only at 1/2 in each case. The frozen checker was inspected, not executed; its finite grid tests are not a proof of uniqueness. Analytic replay: frozen RESULT.md lines 37–62.

## originality

PASS

Pass for the sharp all-iteration C-to-C norm and its unique evaluation point, with the consequent exact leading amplitude and improved remainder. Convergence, polynomial eigenvalues and parity are prior results. On establishing the sharp midpoint norm, selecting the even modes from the known expansion is a consequence, not a separate new spectral theorem. No inspected earlier source supplies the all-iteration optimized norm.

## value

PASS

The uniform worst-case error of Bernstein iteration is a natural invariant of a canonical positive operator. The theorem determines it at every time without a continuous optimization, and shows exactly where to evaluate it. The normalized Perron coefficient and even-sector bound quantify long-time error, with the rate improvement realized at degree four. These conclusions go beyond computing the already-known Bernstein eigenvalues.

The dated certificate retains the supplied scientific assessment, sources and limitations.
