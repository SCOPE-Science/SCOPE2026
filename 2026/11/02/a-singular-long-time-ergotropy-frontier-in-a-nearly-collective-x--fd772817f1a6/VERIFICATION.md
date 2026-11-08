---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For specified two-qubit XX Hamiltonian J>h>0, finite-temperature Gibbs state and local/collective amplitude-damping interpolation α, the symmetric and antisymmetric jump operators yield an invariant four-level pure-death population sector. Exact ODEs have antisymmetric decay γ(1-α), symmetric decay γ(1+α), and doubly excited decay 2γ. With ε=1-α and u=γεt in compact subsets of (0,∞), a(t)=p_beta exp(-u)+O(ε), while fast s,e populations vanish uniformly. Energy passivation of the remaining |a>,|gg> mixture gives Δ[1-2p_beta exp(-u)]_+; trace-norm Lipschitz bounds make convergence uniform. The singular limits differ Δ vs Δ[1-2p_beta]_+, and p_beta=1/2 gives unique beta_c satisfying sinh(2 beta_c J)=cosh(2 beta_c h). Solve for critical u_c and target work u_w. Independent 20 population/ergotropy examples and 12 direct full Lindblad 16x16 propagators confirmed the four-population dynamics; not a general all-ε certificate.

## originality

PASS

Best-of-knowledge: A finite-time plot and strict collective stationary formula do not logically assert the uniform joint singular limit without further analysis; however the original full source was inaccessible, so the statement-vs-prior implication is provisional rather than a whole-paper exclusion.

## value

PASS

A mathematically exact metastable observation-time frontier separates apparent collective passivity from eventual full charge extraction for a natural weakly broken subradiant battery. Noncommuting infinite-time and weak-noncollectivity limits, sharp onset and target-work times are operationally meaningful natural invariants. Prior work established the bath, singlet decay mechanism, and collective critical temperature; these are not represented as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
