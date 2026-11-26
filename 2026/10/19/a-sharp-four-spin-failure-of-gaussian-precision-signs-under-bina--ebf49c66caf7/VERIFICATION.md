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

Inspected RESULT.md:26–98, VERIFICATION.md and verify_ferromagnetic_precision.py. Full support gives strict variance in every nonzero direction. For d=2 the binary 2×2 determinant is the covariance, and for d=3 conditioning on the third coordinate preserves the nonnegative determinant. Because a binary conditioning variable spans all its functions together with the constant, the off-diagonal Schur complement is exactly the mean conditional covariance. The 2×2 inverse reverses its sign. In the four-spin model the log-mass has nonnegative pairwise mixed differences and no XY coupling. The conditional means depend only on k=Z+W; their nonlinear residuals after projection onto 1,Z,W are their discrete curvatures times the same residual of ZW. With q the positive four-cell marginal masses, the vector (1/q00,−1/q01,−1/q10,1/q11) spans the complement and has positive discrete mixed difference sum 1/q, giving the claimed residual variance. Independent expansion of the logistic second differences yields the strictly positive prefactor times (1−ar) or (1−bs); conditional independence kills the covariance of the conditional noises. The determinant of the residual covariance is positive, so the sign rule includes both exact zero hypersurfaces. Independent integer moment enumeration used weights 2^(3−3x+y+(x+y)(z+w)); sum 235, first moments 59,194,158,158, and XY moment 50. For C=235²Σ, det C=11393411432400000 and the minor deleting row 2 and column 1 is −795240000. Hence ΣXY=304/55225 and KXY=235/60966, as stated. Did not execute the source verifier.

## originality

PASS

Credit the established Gaussian characterization, binary Ising MTP2 criterion, ordinary versus augmented covariance distinction, and even a previously published four-cycle with spurious ordinary precision entries. The latter has negative entries at the nonedges; the supported distinct claims are the sharp cutoff for a positive entry within full-support binary MTP2, and the exact field-dependent positive/zero/negative classification for the specified subfamily.

## value

PASS

A known spurious nonzero precision entry is not enough to overturn the attractive Gaussian sign rule. This threshold and the sign-changing full-support model do: the marginal covariance is positive and the conditional pair independent, yet the linear partial correlation is negative. The field hypersurfaces and common omitted separator interaction identify when a practitioner can and cannot read the usual precision sign as attraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
