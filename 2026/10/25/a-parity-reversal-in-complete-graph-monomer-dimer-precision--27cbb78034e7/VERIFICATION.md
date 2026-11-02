---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For matching measure t^|M| on K_n, edge indicators have covariance matrix (p-s)I-s A_line+(s-p²)J. The 3 line-graph Johnson-scheme eigenvalues L0=p-Hp²+Ds,L1=p-(n-3)s,L2=p+s are all positive by empty and singleton matchings. The inverse disjoint-edge entry is 2/[n(n-1)L0]-4/[n(n-2)L1]+2/[(n-1)(n-2)L2]. Low-t expansions cancel through t and give q_n(t)=-2t²+O(t³); high-t matching-defect expansions give q/t -> -2/(n-2) for even n and +6/(n-1) for odd n. Independent sympy exact rational limits for n=4..9 agree. Since partial correlation is -q/Q_ee, odd-n sign changes from positive to negative by continuity. Claims avoid uniqueness/intermediate even n.

## originality

PASS

Classical complete-graph matching partition function and Johnson-scheme eigenspaces are known tools; lattice dimer correlations and mean-field monomer–dimer density results do not entail finite-n full covariance *inverse* disjoint-edge sign reversal from their stated results. Published Resultary precision laws for permutation inversions or box indicators concern different random constraints, not matching hard-core law. No exact same parity crossover identified; prior exact inverse-covariance table might exist.

## value

PASS

Inverse covariance captures full-order linear partial correlations, mathematically distinct from ordinary pair covariances. Their sign flips with parity at high activity for a canonical Gibbs matching model, a meaningful structural boundary in graphical dependence and finite-size matching asymptotics, beyond a simple numeric table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
