---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Writing \(x=\cos(2\pi r/N)\) and \(T_3(x)=4x^3-3x\), the proposed polynomial factors through the two adjacent sampled values \(u\le-\sqrt3/2\le v\). The sign of the third factor is fixed on \([-1,1]\), so the factorization proves feasibility on every grid point. Off contact, a positive two-point combination at \(u,v\) cancels the \(T_3\) coefficient and gives the matching upper bound; when \(12\mid N\), the sampled contact point itself gives the sharp bound. This is an all-\(N\) proof rather than an inference from the bundled finite verifier.

## originality

PASS

The primary Carathéodory–Fejér literature defines and reduces the finite cyclic extremal problem, and the known singleton result fixes the continuous value. The inspected finite-group source gives equivalence and convergence results, not the all-grid closed value for the isolated third harmonic. Relevant published SCOPE records include the no-loss divisibility criterion and a distinct Turán-mass problem on the same five-point support, but neither statement implies the off-contact coefficient optimum here.

## value

PASS

This is a natural exact invariant in a classical discretized extremal problem. It replaces a mesh-by-mesh linear program with a symbolic optimum, extremizer and dual certificate for every \(N\ge6\), and sharpens a known no-loss divisibility result into a complete finite-grid law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
