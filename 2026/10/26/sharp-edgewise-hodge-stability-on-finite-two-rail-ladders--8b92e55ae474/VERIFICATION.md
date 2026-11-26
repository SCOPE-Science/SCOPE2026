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

The edge gradients split into orthogonal identical-rail data and the range of z -> (z,Dz/2,-Dz/2), whose Gram matrix is (2I+D^TD)/2. This recovers all blocks. For the tridiagonal inverse, left and right homogeneous solutions are alpha^(1-i)+alpha^i and its reversal; the endpoint conditions are reflection across the end half-steps, and the discrete Wronskian gives the factor rho/(1-alpha^(2n)) in 2G. Their strict monotonicity gives the exact rung row sum by telescoping the total variation. As a separate rail check, the consistently oriented square-cycle matrix C has Gram matrix T=4I-adjacency(P_{n-1}), so the cut projector is I-C T^-1 C^T. For a rail edge at h, positivity and unimodality of the Dirichlet Green row of J=T^-1 give the absolute row sum 1+2 sum_k J_hk=2-J_h1-J_h,n-1<2 (for n=2 the last two terms use the same index). The rung row is a decreasing function of alpha^(j-1)+alpha^(n-j) over the allowed range; its minimum argument occurs at the central rung(s). The exact small-n rail maxima are 3/2, 5/3 and 13/7 for n=2,3,4; for n>=5 the lower bound after discarding the positive quadratic is 2+29/627, proving global dominance and the threshold. The exact deficit identity has a strictly positive bracket, and substituting the central t_n gives both parity constants and the root rate. A sign vector of the extremal row attains the norm.

## originality

PASS

The preceding weighted-ladder kernel covers exactly the rung-to-rung Green block and is credited as such. The distinct October 26 contribution relative to the earlier and same-day sources inspected is the all-edge absolute row-sum optimization, rail-row competition, exact threshold and sharp parity defect. The November 2 record is a direct claim-level match (not a distinct theorem on these points), but the evidence places it later than the frozen October 26 record; this is not evidence of earlier coverage or of either record's independence from the other.

## value

PASS

Open two-rail ladders form a canonical bounded-width network. The exact worst edge amplification under Euclidean edge fitting answers whether and where this local geometry amplifies bounded noise. Strict sub-two rail rows, the first super-two ladder, and the boundary-sensitive sharp parity constants cannot be inferred from an infinite rung kernel or a global logarithmic estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
