---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

The central \(F\) CDF at \(\kappa\mathbb EX\) is exactly \(I_{q_\kappa}(a,b)\) with \(q_\kappa=\kappa a/(\kappa a+b-1)\). Assuming an infimum of one half produces a sequence on a discrete half-integer lattice; after subselection, each coordinate is constant or tends to infinity. The fixed/fixed case contradicts the published pointwise strict inequality. With fixed \(a\) and \(b\to\infty\), beta-to-gamma convergence and the positive gamma density make the \(\kappa>1\) limit strictly larger than the corresponding \(\kappa=1\) limit, which is at least one half; the reflected fixed-\(b\) case is analogous. When both parameters diverge, the exact threshold-minus-mean calculation gives a squared standardized separation bounded below by \(((\kappa-1)^2/(2\kappa^2))\min(a,b)\), so Chebyshev forces the CDF to one. These four cases exhaust all escape patterns. I independently checked the exact separation inequality on a representative half-integer lattice, while the package verifier checks the same algebra without substituting for the limit proof.

## originality

PASS

The complete Zhou--Lu--Hu primary paper was read at Theorem 1.1, the proof sections and Remark 2.4. It proves the finite-parameter strict inequality at \(\kappa=1\), the non-strict uniform lower bound for \(\kappa>1\), and then explicitly conjectures the strict uniform inequality, stating that a proof was unavailable. The submitted compactness/boundary-regime argument proves exactly that conjecture. The related gamma-family infimum paper concerns a one-parameter gamma problem and does not imply the two-parameter \(F\)-lattice escape analysis.

## value

PASS

The result closes an explicit conjecture in the exact source and resolves the only obstruction left by pointwise strictness: escape to infinity in the two degree parameters. The beta-to-gamma boundary classification is a motivated structural proof rather than a finite numerical improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
