---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For T SPD and W symmetric indefinite, direct multiplication of the specified two-factor P_{alpha,gamma} produces n zero error eigenvalues and the n real generalized eigenvalues of (alpha I-WT^{-1}W,T+alpha I); this block calculation was independently checked on a noncommuting instance at five gamma values. The Rayleigh quotient has strictly positive alpha derivative because T+WT^{-1}W is SPD; compactness yields uniform strict increase of BOTH extrema, including eigenvalue multiplicities. At alpha down to zero the extrema are nonpositive with a strictly negative minimum; as alpha tends to infinity both approach 1. The sum crosses zero once, making max(-ell_min,ell_max) strictly decrease then strictly increase; the extremal balance is the unique global minimum. The upper extreme is always <1 and the lower >-1 exactly when 2alpha>lambda_max(WT^{-1}W-T); no claim that alpha=0 is admissible. For n=2, vanishing trace in a T eigenbasis yields the stated positive quadratic root and explains b12 independence. Numerical recomputation (noncommuting T=diag(1,4), W=[[-2,1],[1,3]]) supports the exact formula but is not an infinite proof.

## originality

PASS

Best-of-knowledge original as an exact spectral-radius optimization of this PARTICULAR VBP stationary splitting, not as the generalized quotient, spectral analysis, or Chebyshev/equioscillation principle. The initiating 2026 arXiv work was located, but only metadata/abstract could be read through lawful sources; the accessible paper itself was not obtained, and authorized institutional access returned vpn_disconnected. Accordingly no whole-paper noncoverage claim is made. Huang-Chen 2018 full relevant sections give a DIFFERENT P2 block preconditioner and eigenvalues, not this family or optimal shift. Published related SCOPE/Resultary spectral records concern different iterative algorithms. Potential implicit overlap in the inaccessible source remains an explicit priority risk.

## value

PASS

For a natural noncommuting symmetric-indefinite block system, a unique constructive globally fastest stationary shift and exact convergence threshold distinguish rate optimality from Frobenius-distance tuning; a two-dimensional coupling-invariant location is a substantive structural consequence. It is not asserted to improve flexible GMRES or transient Euclidean amplification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
