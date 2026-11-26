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

Putting the two probability generating functions over a common denominator gives a positive constant times (1−tz)/[(1−qz)(1−rz)], with q<t<r. Thus the log jump intensities are (q^k+r^k−t^k)/k, positive and summable. In g(z)=−(1−z)G′(z)/G(z), the coefficient of z^k for k≥1 is d_k. If any is negative, the quotient for α=1−h has a negative coefficient to first order in small positive h (the expansion is uniform on a fixed sufficiently small circle about zero, so coefficient extraction is valid). If all d_k are nonnegative, they sum to q+r−t by telescoping; integrating g(1−β+βz)/β from α to 1 gives a compound-Poisson exponent by binomial expansion, proving sufficiency for every α. Dividing by (1−t)t^k gives Φ(k)−1, where Φ is a positive sum of decreasing and increasing exponentials. Its strictly positive second derivative gives a unique continuous minimum at the stated x_* and an interval of strict negative defects. Monotonicity on either side puts the integer minimum at the clipped floor or ceiling, also when x_*≤1 or is an integer. For the N-family the displayed weight lies strictly between zero and one and realizes t_N. Fixed k and k_N=floor(N/3) give respectively the positive limit 71/10 and a limit less than −2/5 for N d_k. Hence initial agreement can last beyond every fixed B, not merely the illustrated examples. Independently replayed the exact small witness and first negative indices 16, 32, 64 and 129 with python3 /workspace/review_evidence/check_geometric_defects.py. The frozen checker was read, not executed; its finite grid is support, not proof of the universal rule. No claim of minimality of the two candidate tests is needed.

## originality

PASS

The supported distinction is the explicit parameter-dependent finite reduction for two geometric components, with consecutive failure indices and the analytic family giving arbitrarily late first failure. Compound-Poisson structure and monotonicity of the all-index canonical sequence are already established. The strongest inspected direct corpus overlap supplies one genuinely non-self-decomposable two-geometric mixture, not a classification or unbounded-delay family. The exact-object 2025 article is an unresolved access risk, not negative evidence or a reason on its own to withhold the verdict.

## value

PASS

Ordinary thinning self-decomposability is a meaningful strengthening of compound-Poissonness for a basic mixture family. The finite rule replaces infinitely many conditions with parameter-dependent explicit tests, while the delayed-failure family proves that checking a fixed number of initial defects cannot replace them. The shape and obstruction are useful independent of the illustrative arithmetic cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
