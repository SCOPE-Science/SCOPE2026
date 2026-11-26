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

Grouping Hardy coefficients by their residue j modulo k gives the orthogonal direct sum f(z)=sum_j z^j g_j(z^k). A unitary node DFT turns the evaluation map in sector j into two weighted evaluations of g_j at r^k and s^k exp(ikθ), the second with an irrelevant phase exp(ijθ). Their Gram matrix gives the claimed A_j,B_j,C_j and strictly positive determinant (the two sector points are distinct). After rephasing, each block is the previous one congruenced by diag(r,s). Its maximum decreases by the operator norm bound s²; testing the new block on the normalized inverse image of the old minimum eigenvector gives the same strict upper bound for its minimum. Thus sectors 0 and k−1 are extremal for all angles. At fixed diagonals both edges move strictly and oppositely with C_j, which is uniquely minimized at the half-step; the condition ratio follows. The minimum norm right inverse has norm λ_min^(−1/2), using the nonzero singular spectrum. At j=k−1 the top eigenvalue is asymptotic to B_j, and det/B_j is asymptotic to k(1−r²)r^(2k−2)s^(2k); at j=0 the matrix divided by k tends to a rank-one matrix of trace 2−r²−s². These prove the constants and the ratio for fixed distinct radii. The finite supplied checker was inspected, not run; its sampled comparisons are not needed for the proof.

## originality

PASS

Best of current knowledge, the simultaneous spectral-edge and condition-number optimization, the extremal Fourier sectors and sharp mixed-radius asymptotic constants distinguish this result. A distinct same-day record already gives the identical half-step as a determinant optimizer in the identical configuration, even with unequal orbit sizes allowed. The offset alone is not credited as new, and the shared date does not determine priority.

## value

PASS

For two prescribed radial sampling layers, worst-case minimum-norm interpolation and maximal evaluation gain are stricter objectives than a determinant. Their exact simultaneous optimum, and the sharp exponential conditioning that still remains there, matter for choosing and evaluating this natural design. The result does not optimize unrestricted node sets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
