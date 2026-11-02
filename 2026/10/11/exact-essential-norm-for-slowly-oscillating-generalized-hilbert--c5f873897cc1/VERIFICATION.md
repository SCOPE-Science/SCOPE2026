---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For a=gamma+1/p in (0,1), decreasing-integrand comparisons yield both Schur supersolution inequalities for u_n=n^-1/p, v_n=n^-1/p′ with sharp C=pi/sin(pi a). Output coordinate truncation gives essential norm <=C limsup|g_k|. Direct algebra verifies k^(1/p)(H_gamma x)_k=sum_n n^-1 kappa_a(log(n/k)) for the logarithmic test vectors. Uniform Riemann-sum convergence, fixed-window slow oscillation at indices attaining limsup, and harmonic masses 2T and 2(T-A) give the reverse lower bound. Weakly null normalized vectors force compact perturbations to vanish. Limits N->infinity, then T->infinity, then A->infinity establish equality; L=0, arbitrary complex phases and parameter endpoints are handled appropriately. Proof inspected in RESULT.md; six Git blobs form the exact assigned tree.

## originality

PASS

The same generalized Hilbert matrix appears in Norrbo (arXiv:2609.13403v1), whose Theorem 2 requires convergence of subexponential-block p-means, while this claim covers bounded multiplicatively slowly oscillating moduli with nonconvergent means; full ten-page primary preprint examined, including Theorems 2 and 3, their proofs, and the operator definition. Searches for exact slowly-oscillating Hilbert-matrix and Mellin limit-operator versions produced no direct dominating theorem. General limit-operator technology remains a historical-overlap risk, not an established implication.

## value

PASS

The exact essential norm of a canonical dense operator family with bounded coefficients slow on multiplicative scales is a natural sharp infinite-dimensional invariant. It gives a full p,gamma parameter-class extension beyond convergence-of-means hypotheses, a sharp compactness criterion and a genuinely oscillatory example. The result is not only a numeric substitution and its claimed scope is narrower than arbitrary bounded multipliers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
