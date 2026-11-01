---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The three-term orthogonal basis (1,t,t²−1/q) has exact beta norms 1,1/q,2(q−1)/(q²(q+2)); this gives the displayed quadratic reproducing kernel and the integrated upper-tail step response F(z,a). For each cutoff a, maximizing the quadratic in z yields either z=1 or the interior vertex z=−1/((q+2)a), whose admissible range is a≤−1/(q+2). Independently refactoring K(1,a) and K(z*(a),a) gives critical thresholds u=1/(sqrt(q+3)+1) and v=−1/(sqrt(q+3)−1), and the only two global candidates E(q),I(q). At endpoint a=−1 the response is 1; both candidate branch maxima exceed 1 on the domain. The positive Stieltjes-mixture representation extends the sharp step bound to every bounded nondecreasing f. Reflection gives the lower envelope, with both stated equality cases and ties. q↓1 weight and q=3 radical limits have consistent beta-tail behavior. Independent SymPy identities verify both factorizations, and sampled high-precision quadrature across eight positive q values agrees with the analytic branch envelope; finite samples are not the all-q proof.

## originality

PASS

The distinctive assertion is the all-cutoff, all-input sharp quadratic range envelope in a continuous ultraspherical weight parameter with two extremal geometries, not the classical limiting Jacobi Gibbs overshoot. Kaber computes large-degree fixed-jump asymptotics; constrained monotone approximation chooses a different operator; Abel-Jacobi kernels concern another summability method. Fresh indexed Resultary search returned no directly matching theorem but nonhits cannot establish priority. Best-of-knowledge PASS with explicit risk from unindexed classical spectral approximation results.

## value

PASS

A natural finite-degree orthogonal spectral projector applied to monotone [0,1]-valued data need not preserve range; the exact worst overshoot controls amplitude safety and identifies all sharp cutoff/evaluation pairs. The two competing geometry branches and switch with the Jacobi weight are a mathematically meaningful classification rather than routine asymptotic Gibbs rephrasing; the unproved uniqueness of the crossing is not needed for value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
