---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and boundaries

Run `python verify.py` in the same directory as this file, with Python 3.9 or later. The program uses the standard library only. It passed the following checks on the packaged source:

- Exact enumeration of all \(2^6=64\) directed potential-contact graphs on three individuals, integrating the dependence between a single infective's two outgoing edges for four integer Gamma shapes; the result matches each entry of the closed final-size law in rational arithmetic.
- Exact rational example \(h=1/2\), \(q=3/7\), \(r=36/175\), \(\Pr(Z_2=2)=64/175\), and \(\mathbb E Z_2/2=82/175\).
- Round-trip numerical inversion for seven admissible parameter triples including both mixing-exponent endpoints.
- A distinct-shape reconstruction preserving exactly the two size-specific mean secondary case fractions, using the unique monotone root for a chosen second shape.
- Numerical checks of strict variance positivity and its leading \(\lambda^2/a\) coefficient at low contact intensity.

The global uniqueness, continuity, and structural nonidentifiability claims are proved analytically in RESULT.md. A finite graph enumeration is exhaustive only for the three-person contact graph, not for parameter-space uniqueness; numerical root finding is evidence of formula implementation, not a replacement for the monotonicity proof. No clinical estimation, finite-sample coverage guarantee, or independent audit is claimed.
