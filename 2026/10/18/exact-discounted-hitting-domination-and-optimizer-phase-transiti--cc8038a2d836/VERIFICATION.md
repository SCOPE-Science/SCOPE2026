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

# Reproduction and boundaries

The independent script `verify.py` requires Python 3 with standard-library modules only. Run `python3 verify.py` in the directory containing that file; expected terminal line: `TOTAL_EXACT_OK 132`.

For each graph tested it enumerates every nonempty vertex set, solves the Markov first-step equations for all unpinned supports over exact rational numbers, records the least support, and tests the exact optimizer census at all internal and external transition thresholds and at intermediate points. The test graph/discount pairs are \((m,q)\) equal to \((2,2),(3,2),(2,3),(3,3),(2,4)\), with \(\lambda\) equal to \(1/2\) or \(4/5\). There are 132 rational threshold checks. The verifier reconstructs matrix solutions directly from graph adjacencies; it does not use the proof's clique equations to compute those values.

Finite graph enumeration does not establish a claim for arbitrary \(m,q\). The infinite result follows from the equilibrium equations and the lower-bound and classification proof in `RESULT.md`. Input parameters for the theorem remain restricted to \(m,q\ge2\), \(0<\lambda<1\) and \(0<\tau\le1\); no statement is made for weighted or heterogeneous-fidelity networks.
