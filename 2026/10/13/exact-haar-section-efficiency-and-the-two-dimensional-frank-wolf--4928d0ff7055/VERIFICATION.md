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

For unit u,v, Gamma=(||Pu||||Pv||-<Pu,Pv>)/(1-<u,v>) equals d/n minus the projected norm-difference square divided by 2(1-<u,v>). Along any great circle h(t)=||P(cos t u+sin t w)|| belongs to periodic H^1. Fourier Parseval and |e^{iktheta}-1|<=|k||e^{itheta}-1| bound finite-chord squared differences by the expected squared tangential derivative. For Haar rank-d projector Q=P^T P, idempotence and rotational invariance give E|hprime|^2=(n-d)/(n(n-1)), proving sharp chordal constant. Dominated convergence for coalescing directions proves sharpness and inf E Gamma=(d-1)/(n-1), including d=1 and d=n endpoints. Exact Euclidean ball section oracle calculation yields matching optimization witness; transfer to general strongly convex sets relies on existing source comparison-ball hypotheses, not an unrestricted arbitrary-domain claim. Independent rational/all-dimension and small-angle checks passed.

## originality

PASS

Sharp (d-1)/(n-1) Haar section efficiency, optimal chordal norm contraction, d=2 positivity and exact ball-oracle witness quantitatively improve weaker coefficients in original random-subspace Frank–Wolfe paper. Related sparse stochastic subspace descent Haar moments concern gradient-projection steps rather than linear minimization on boundary ball sections.

## value

PASS

The exact uniform expected section-oracle coefficient is an intrinsic sharp algorithmic-geometry invariant, yields a strict dimension-two progress guarantee, and improves a published coefficient by large multiplicative factors. Coalescing-direction witnesses establish optimality even for a Euclidean ball with linear objective, so the enhancement is not a routine normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
