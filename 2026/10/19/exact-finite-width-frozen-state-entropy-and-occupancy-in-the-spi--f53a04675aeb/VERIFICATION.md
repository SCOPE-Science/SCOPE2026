---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

An occupied center bit survives iff both NE and SW are nonempty or both NW and SE are nonempty, yielding the printed mask predicate. On the labeled torus a trace term has one designated initial pair and forces all overlaps cyclically; it counts each eligible labeled word once and weights each column's popcount once. A separate reconstruction reproduced all occupancy coefficients for n=4,5,6 and totals 1738, 11303, 72790; its exact characteristic computation gives x^32 P Q on the 52-state SCC and x^12 from twelve loopless singleton SCCs. It verifies weighted P divides the characteristic polynomial and its z-derivative is R. The loop at (7,7) makes the 52-state block primitive for positive z. Descartes' rule applied to P(6+t), the opposite signs at 6 and 7 and Q(x)>0 for x≥6 identify the simple Perron root. Primitivity yields the same analytic dominant branch near z=1 and convergence of the normalized log moment-generating function. Its derivative at zero is α'(1)/α; Chernoff bounds at fixed positive and negative t sufficiently close to zero give concentration, with the factor 1/3 for density per site. Numerics give entropy 0.621833878228314746 and density 0.608926697310519878, the latter within 5e−16 of the printed approximation (the final displayed digit should not be taken as exact). Replay the independent script /workspace/branches/7aab3849-2c41-4d92-8366-019abbdb3ce3/reproduce.py separately with --all-small, --scc, --symbolic, --numeric. The uploaded verifier was inspected, not run.

## originality

PASS

The spiral rule and transfer-matrix approach are prior. The strongest inspected prior with the same rule studies random initial conditions and jamming dynamics, not the uniform fixed-point ensemble on the periodic three-row strip. The strongest earlier exact three-row record uses a different local predicate. The specific characteristic and weighted Perron data survive the comparison.

## value

PASS

Width three is a natural narrow periodic geometry retaining distinct Moore neighbors, rather than a list of small lengths. Its exact spectral and weighted data give an all-length census, an entropy benchmark, and a concentration density for a recognizable jamming rule. Those numbers are not inherited from the two-dimensional transition or from threshold-based counts on the same width.

The dated certificate retains the supplied scientific assessment, sources and limitations.
