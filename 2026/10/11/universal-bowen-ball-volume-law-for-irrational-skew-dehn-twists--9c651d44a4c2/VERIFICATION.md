---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

C PASS: Reconstructed the lifted orbit difference v_j=eta+j k delta+delta*int_0^1 S_j psi'(x+s delta)ds. For C1 periodic psi the derivative is continuous with zero circle mean; uniform Fourier approximation and irrational geometric sums give sup_{u,j<n}|S_j psi'(u)|=o(n), including all prefixes. With epsilon<min(1/8,1/(8L)) each one-step lifted increment is under 1/8 while distinct integer-neighborhood bands are separated by over 3/4, precluding winding. End-index constraints bound n delta; the full sampled discrepancy converges uniformly to eta+k a t. Interior/exterior parallelogram sandwiches prove uniform center-independent n-area limit 4 epsilon^2/|k|, and Haar lower/grid upper entropy bounds give exponent one. No finite simulation is an infinite proof.

## originality

PASS

PASS: Earlier skew Dehn-twist and toral polynomial-entropy literature determines linear orbit-growth classes or entropy exponents, whereas the candidate determines a full fixed-resolution, center-uniform Haar Bowen-ball asymptotic with exact metric-dependent coefficient and limiting local parallelogram for every irrational rotation and C1 periodic perturbation. None of the materially read original growth/classification theorems implies this area coefficient or perturbation universality. No exact Bowen-ball volume predecessor identified in targeted skew-shift and metric slow-entropy searches; unindexed sources remain a risk.

## value

PASS

V PASS: The exact constant 4 epsilon^2/|k|, not just entropy exponent one, measures finite-resolution orbit distinguishability and is robust under every C1 periodic perturbation and any irrational base with no Diophantine assumption. The universal limiting parallelogram supplies a natural structural local limit; it is quantitatively meaningful even though coefficient depends on metric choice and no general theorem beyond the skew family is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
