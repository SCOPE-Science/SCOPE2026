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

# Verification of the exact finite moment identities

The standalone `verify.py` program works without external packages. Run `python3 verify.py`. It tests ten complete action-profile spaces: \(2\le n\le6\), each with \(q=1/3\) and \(q=2/5\). For each profile it computes the represented voters by explicitly following all delegation chains, uses exact integer profile probability weights, and compares two independent rational answers against the finite ancestral-path formula and backward two-path recurrence: the expected represented fraction and the probability that two distinct named voters are both represented.

Observed result: `EXACT_CHECKS_OK 10 ASSIGNMENTS 100136` (all ten exact comparisons passed). No confidence interval or approximate finite experiment is used for these comparisons. Numerical integral evaluation at \(c=1\) gives limiting mean about \(0.6556795424\), limiting variance about \(0.07008433765\), and limiting standard deviation about \(0.26473447\).

The finite program checks algebraic identities and boundary handling. It cannot certify a limit as the electorate size tends to infinity. The infinite result is proved by self-avoiding path exposure, dominated Riemann sums, a two-path collision hazard, and a strictly increasing absorption-probability function. A complete distributional weak limit and independent validation are not provided.
