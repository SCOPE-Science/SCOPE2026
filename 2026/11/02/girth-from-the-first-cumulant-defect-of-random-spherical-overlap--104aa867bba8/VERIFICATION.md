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

Leaf stripping on any forest makes all edge inner-product variables mutually independent, since the conditional distribution of a leaf dot product is rotation-invariant and does not depend on other vertex spins. A simple j-cycle has product moment p^(1-j) by E[R R^T]=I/p. Proper nonempty cycle subsets are forests, so their mixed joint cumulant vanishes; cumulant multilinearity implies all lower-order mixed defects vanish, and at r=g exactly g! orderings of each shortest cycle contribute p^(1-g) times its weight product. Positivity precludes signed cancellation. For Haar qubit p=3, Bloch representation and fourth/fifth repeated-edge cumulants yield kappa_2=m/3, kappa_3=2c3/3, kappa_4=-2m/15+8c4/9, kappa_5=-8c3/3+40c5/27. Finite simple graphs, p>=2, nonzero real weights in the identity, positive weights to identify girth; no graph-isomorphism reconstruction is claimed.

## originality

PASS

Spin O(p) model high-temperature partition expansions have long encoded cycle contributions, so the general mechanism is established, not independently novel. The inspected published subgraph expansion does not state or tabulate the first *cumulant defect against independent edges* or inverse recovery of graph girth from one scalar law, nor the explicit low-order Bloch overlap cycle enumeration. These are nontrivial evaluations and a natural inverse-statistics interpretation, rather than a mere change of name. Older linked-cluster diagrams may prove the exact same consequence; qualification is essential.

## value

PASS

A graph-wide random spherical or qubit overlap sum reveals edge count, shortest-cycle girth, shortest-cycle multiplicity and low-order cycle counts without observing individual edges. This provides a natural structural link between graph topology and distributional dependence, at every dimension and graph size; positive weights identify the exact first defect, while signed cancellation is explicitly scoped.

The dated certificate retains the supplied scientific assessment, sources and limitations.
