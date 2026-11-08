---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

At every nonzero equilibrium all vertices within group i have identical infection probability x_i because their force is equal, and no boundary equilibrium other than zero exists. Let h=n_i x_i²/(1−x_i)=λ∏n_j x_j; then x_i=u_i(h)=2/(1+sqrt(1+4n_i/h)), and λ(h)=h/∏n_i u_i(h). Its logarithmic derivative is 1−Φ(h) with Φ=Σ(1−u_i)/(2−u_i), strictly decreases from m/2>1 to0 for m>=3; λ→∞ at both h→0 and h→∞, so a unique nondegenerate fold gives zero/one/two positive equilibria. The group Jacobian is diagonally similar to 11^T−diag((2−x_i)/(1−x_i)); rank-one inertia shows one unstable lower branch, simple zero at the fold, and a stable upper branch, while within-group zero-sum modes have −1/(1−x_i)<0. DFE Jacobian −I. g_h(n)=n u_i(h)=(h/2)(sqrt(1+4n/h)−1) has strictly concave log, giving strict integer smoothing and balanced partition minimizing λ* at fixed N. Equal-size real bound (m−1)^(m−1)/[(m−2)^(m−2)(N/m)^(m−1)]. Independently recomputed class-matrix spectra for x=1/2 ({−3 twice,0}), x=1/3 ({1/2,−5/2 twice}), x=2/3 ({−1,−4 twice}); checked balanced n_i=3 threshold 4/9 and package finite verifier code. General result is analytic not finite extrapolation. Only local deterministic SIS closure, not exact stochastic extinction.

## originality

PASS

Qualified PASS for complete heterogeneous transversal m-partite equilibrium multiplicity, full-node inertia and strict total-population balancing threshold. The inspected broad higher-order SIS papers prove healthy/endemic existence and stability criteria or homogeneous simplicial mean-field folds; they do not explicitly or by inspected implication derive the exact all-size balancing law. Potential equivalent heterogeneous reduction under another normalization remains.

## value

PASS

Solves natural heterogeneous epidemic-closure bifurcation and allocation question: exact unique fold, full node stability and strict balancing over integer part sizes, a sharp structural result beyond the known homogeneous scalar fold. Natural parameter-independent extremal answer can guide mathematical model comparison without pretending to clinical prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
