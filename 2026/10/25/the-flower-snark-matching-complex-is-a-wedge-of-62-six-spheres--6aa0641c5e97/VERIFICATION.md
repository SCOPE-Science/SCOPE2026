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

The included `verify.py` is a standalone standard-library checker. It reconstructs the twenty-vertex, thirty-edge graph; enumerates all \(112827\) nonempty matching simplices; builds all \(677415\) nonempty face incidences; verifies that the reversed matched-arrow Hasse graph is acyclic; and derives the integral Morse boundaries of size \(1\times25\) and \(25\times86\).

It then checks a degree-one entry, the chain relation \(\partial_5\partial_6=0\), and a specified unimodular \(24\times24\) minor of \(\partial_6\). No stochastic sampling, external table, publisher data, cached matrix, external symbolic-algebra package or network request is used.

The topological deduction uses the discrete-Morse CW theorem and the identification \(\pi_5(\bigvee^{24}S^5)\cong\mathbb Z^{24}\), so the exact degrees control the remaining attaching maps. The finite computations are exhaustive for this graph. No assertion is made about larger members of the flower-snark family, and no independent audit has been performed.
