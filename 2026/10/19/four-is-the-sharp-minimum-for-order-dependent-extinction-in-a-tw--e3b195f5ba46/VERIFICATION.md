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

With E=exp(τA), the chronological convention gives D_last E⋯D_first E. The stated positive diagonal similarity makes A symmetric and commutes with each D_j. If Q is the symmetric positive definite square root of the transformed E, conjugation by Q changes each transformed D_j E to QD_jQ, a symmetric invertible matrix. Cyclic rotations preserve the characteristic polynomial by similarity and reversing the factors transposes the product. Together these yield every permutation for one, two or three labels, even when some pulse matrices repeat. For the four-pulse witness, A has the prescribed positive rates and (A+I/2)²=I, so τ=log 2 gives the claimed exact E by the hyperbolic power series. All four diagonal survival pairs are distinct and strictly interior. Independent integer propagation of both basis columns through each chronology, with common denominator 4·1600⁴, gave traces 101759121/102400000 and 4243977/4096000, common determinant 50787/16000000, and det(I−P) values 4829579/512000000 and −16871941/512000000. Each product has positive entries, real eigenvalues (positive discriminant), and positive determinant; both eigenvalues are positive and the smaller is below one because their product is below one. Hence the signs at one imply strict decay and growth respectively. Perron–Frobenius convergence gives the corresponding fate for every strictly positive starting vector at block times; the finitely many fixed interim propagations and the compact interval of each continuous flow preserve the limits between block times. The frozen verifier was inspected, not run. The private replay at /workspace/replay_5.py is independent and certifies only the finite witness, not the all-parameter statement.

## originality

PASS

The distinct contribution is the sharp boundary for the complete multiplier multiset and strict decay-versus-growth reversal in the specific common-flow, equal-spacing two-stage diagonal-pulse model, including four distinct strictly admissible classes. Cyclic similarity, reversal of symmetric factors, Perron thresholds, and the general observation that biological schedule order can matter are not new. The strongest inspected sources either hold the pulse fixed, study binary rearrangements without the common ecological generator and strict threshold witness, or operate in a different projection model. None of these inspected statements supplies the sharp result under the full frozen restrictions.

## value

PASS

The result identifies the first block length at which merely permuting the same fixed collection of survival pulses can change the long-run conclusion in this constrained continuous-flow model. Isospectrality is stronger than equality of Perron thresholds, and the strictly admissible rational comparison separates the schedules at the actual unit boundary, not only at the level of unequal trace or transient behavior. This gives a concrete limitation on when the order can safely be disregarded in the stated model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
