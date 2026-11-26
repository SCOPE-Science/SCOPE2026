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

Walsh inversion gives the radial kernel with multiplier 1/(2j). Subtracting adjacent radial heat-integral entries gives the strictly positive integral in RESULT.md line 35. Translation invariance, symmetry and zero row sum then give both exact endpoint norms and the fixed positive Hamming ball in the time-integrated formula. For the lower bound, the ball with radius d/2−2 sqrt(dH), H=log log d, has stationary mass at most exp(−8H) and heat mass at least 1−exp(−8H) up to t_c−(log H)/4−O(1), by Hoeffding. For the upper bound, the central-shell entries are −(log d)/4+O(1) in the rescaled row. If N=d−1 and m=floor(d/2), the ratio of binomial coefficients at m−ell and m is the product of (m−i)/(N−m+i+1) for 0≤i<ell; the denominators are at least d/2 and the relative losses are at most (4i+2)/d. Using log(1−a)≥−2a for a≤1/2 and the central coefficient bound proves the local estimate in line 67. The incomplete-beta increment summed over floor(sqrt(dH)/8) shells is O(sqrt(H) exp(H/4+o(H)))=o(log d), placing the positive ball strictly inside d/2−sqrt(dH)/16. Hoeffding makes its heat mass exp(−cH) after t_c−(log H)/4+O(1) and before t_c, an interval of length O(log H). Beyond t_c the product chi-square bound yields an integrable, dimension-free exponential majorant. Doubling the integrals gives the coefficient −1/2 of log log log d and the bounded remainder. The verification notes and check.py were inspected but not executed; they cover exact finite checks, not these asymptotics. The conclusions use the unnormalized Laplacian on the full endpoint spaces.

## originality

PASS

Ellis's product Green theory supplies a prior spectral formula, and fixed-time cube cutoff is established. The supported distinct contribution is the sharp integrated endpoint norm with the triple-log displacement, obtained by controlling the common sign set; no inspected prior theorem supplies that correction.

## value

PASS

This is a sharp endpoint estimate for a natural operator on a basic graph family. The divergent negative correction distinguishes the norm from a bare cutoff-time approximation, and the common Hamming sign ball explains why optimizing the Green operator differs from integrating a fixed-time worst-case bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
