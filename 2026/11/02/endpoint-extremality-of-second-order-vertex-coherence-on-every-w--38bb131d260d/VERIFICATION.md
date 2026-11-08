---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Let z_v=L^dagger e_v and s_k=z_{k+1}-z_k. Because L s_k=e_{k+1}-e_k and s_k has mean zero, s_k is the centered step potential with value -(n-k)/(n w_k) to the left and k/(n w_k) to the right. Direct coordinate multiplication gives the strictly positive Gram entry min(i,j)*(n-max(i,j))/(n w_i w_j). Column-sum zero then gives z_v=P_v-Q_v with positive left/right edge sums, z_1=-(V_v+Q_v), z_n=P_v+U_v. For v<=mid the left endpoint has V_v>=P_v coefficient-wise, making ||z_1||^2-||z_v||^2=||V||^2-||P||^2+2<V+P,Q> strictly positive. For v>=mid the right endpoint gives the reflected strict comparison. n>=3 makes both edge sets nonempty at every interior vertex. Spectral decomposition verifies (L^2)^dagger=(L^dagger)^2, independent of eigenvalue degeneracies.

## originality

PASS

Compared trace network coherence on prescribed tree families with local second-order vertex-coherence algorithms and biharmonic distance. The local diagonal quantity itself is prior, but the strict endpoint location for every order and every conductance vector is not implied by inspected trace formulas or local numerical approximation algorithms. The most relevant local-diagonal algorithm paper full text remained inaccessible; priority risk preserved.

## value

PASS

A natural individual second-order coherence statistic measures noisy-consensus vulnerability or mean squared biharmonic eccentricity. The structural location theorem reduces an arbitrary heterogeneous path worst-node scan to its endpoints and requires an all-weights positive cone argument, not a trace computation or routine first-order effective resistance formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
