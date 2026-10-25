---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The real exponent-2 free Banach lattice/absolutely 2-summing norm representation reduces to the max over simplex weights of tr sqrt(sum w_e v_e v_e^T). Trace-square-root concavity and cube edge transitivity make the uniform old-edge Laplacian L/M optimal; strict concavity on the mean-zero support plus unique off-diagonal pair supports gives uniqueness even if a new chord is at equality. The first-order directional derivative for a chord of amplitude a is proportional to a^2 b^T L^{-1/2} b, so necessary and sufficient preservation is a^2 R_{d,k}<=R_{d,1} independently for each chord, not an assumption that optimizers are symmetric. The Walsh eigenvalues 2|S| prove the explicit R sum and base norm. The integral heat-kernel representation yields strictly increasing R_{d,k}; careful uniform Laplace expansion with tanh(s)^k<=s^2 for k>=2 gives T_{d,k}=1-1/(4d)+O(d^-2); shortest cube paths and x(u)=sum_i u_i prove the exact amplification d T_{d,d}. Independently reconstructed ordinary cube Laplacians for d=3,4,5, all pairwise spectral R values matched the Walsh sum to 1e-10, with strict order. Scope explicitly d>=3, finite arbitrary sets of nonedge rows and positive amplitudes, and real Euclidean generator; finite checks are corroboration, not proof.

## originality

PASS

Best-of-knowledge originality PASS after fresh published findings search and mathematical comparison of alias objects, stronger coverage, exact tables, and prior-result implications. Known general tools are credited, rather than claimed anew; risk remains documented: An earlier equivalent optimal-design calculation for hypercube graph gradients or graph Banach-lattice perturbation could imply the same thresholds without the word chord; no global novelty guarantee.

## value

PASS

An exact one-chord-at-a-time simultaneous screening criterion is mathematically useful for the stability of a nonlinear operator norm under arbitrarily many perturbations. The fact the admissible amplitude approaches 1 uniformly over every nonedge Hamming distance while the pointwise maximum may grow like dimension shows a genuine operator-vs-order gap, not a relabeling or tiny improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
