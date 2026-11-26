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

Directly subtracting the two columns of M* weighted by j+1−ε gives B e_j = r_j on 0..j, r_j−1 on j+1, and zero thereafter. Its bounded Gram form has diagonals 1−r_j+εr_j² and off-diagonals εr_i r_j. The positive diagonal part of D is compact; the negative perturbation has rank one. A negative spectral point necessarily solves 1=ε〈r,(R+δI)⁻¹r〉, with a strictly decreasing continuous sum, divergent at zero and tending to zero at infinity. Partial fractions give the stated digamma equation, and the large-argument asymptotic gives the exponential constant. The normalized resolvent vector gives a shifted Riemann sum with integrable tail (1+t)⁻². Compression by the positive diagonal square root gives the strict harmonic-sum test; comparing it to the secular equation via strict digamma monotonicity even gives N*=floor(1/δ)+1 exactly, including equality at an integer. Row cancellation proves ML=I on finite supports, and L(c00) is dense because a vector orthogonal to every coordinate difference is constant. This proves BM=M* and the compact congruence M*DM; dense range transfers a negative test direction and the rank-one bound rules out a second. The commutator is not asserted to have the auxiliary eigenvalue. These are analytic checks; frozen numerical code was inspected, not executed, and no extrapolation from finite sections is used.

## originality

PASS

Retain the sharp order-one quantitative spectral, profile and detection laws. Ma's earlier general decomposition already gives precisely the order-one auxiliary defect and the factorization, not merely a similar identity; the qualitative index follows routinely. Those background consequences do not count as new. The bounded comparisons did not identify prior coverage of the quantitative collection for this operator.

## value

PASS

The exponential prefactor quantifies how positivity fails at a known threshold. The reciprocal compression dimension explains exactly why coordinate tests can miss the failure, and the eigenvector measure locates the mass at that same scale. These additions go beyond the routine index and factorization and concern a natural compact spectral defect, without claiming to identify the commutator eigenvalue itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
