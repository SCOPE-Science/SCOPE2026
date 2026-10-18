---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Joint concavity of root Uhlmann fidelity reduces minimization over shared diagonal preparations to a localized vertex. For fixed vertex j, expanded classical e^(-tL) and dephasing double commutator: sigma_jj=1-s1*t+O(t²), rho_jj=1-gamma*s2*t+O(t²), neighbor Q-block of sqrt(sigma)*rho*sqrt(sigma) has leading rank-one gamma*t² v v^T with v_k=w_jk^(3/2). The separated eigenvalues give D_j(t)=[s1+gamma*s2-2sqrt(gamma*s3)]t+o(t). For unweighted d>=1, derivative of c_gamma(d)=(1+gamma)d-2sqrt(gamma*d) is >0. As t→∞ with gamma>0, quantum pinches into Laplacian eigenspaces and classical tends to I/N. Exact K_(a,b) vertex projection masses are 1/N, b/(aN),(a-1)/a, giving terminal D_a=1-[1/sqrt(N)+sqrt(b/(aN))+sqrt((a-1)/a)]²/N. T_N(a) is strictly decreasing for a>=2; hence for 2<=m<n early optimum m-part and late optimum n-part. Continuity forces finite crossover; star maximum and balanced minimum follow the same terminal comparison. Fresh standalone matrix pinching checks across six graph pairs and nine gamma cases corroborated formulas, not unique transition or arbitrary graphs.

## originality

PASS

The general root-fidelity distance, localized-input reduction, noiseless short-time degree law, energy-basis pinching, and star/complete asymptotic coincidence are credited to source authors. The weighted noisy slope and entire nonstar complete-bipartite initial-class reversal are genuine new implications of combining dynamics with a bipartite spectral calculation, not statements found in relevant primary source sections.

## value

PASS

A forced change of which vertex class maximizes a concrete quantum–classical distance is a nontrivial structural boundary in a natural solvable graph family, uniform in every positive decoherence rate. The short-time weighted power-sum invariant and exact bipartite terminal classification could be used to assess network topologies beyond numerical examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
