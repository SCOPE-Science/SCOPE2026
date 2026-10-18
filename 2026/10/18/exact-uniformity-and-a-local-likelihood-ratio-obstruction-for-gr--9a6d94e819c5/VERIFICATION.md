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

# Exact computational checks and their limits

Run `python verify_cycle_greedy.py` from a directory containing that standalone file. Its only dependency is Python 3.9+ standard library.

The program uses an exact rational dynamic program on induced subgraphs of a cycle, conditioning on the first vertex selected. It checks all output probabilities for cycles with \(3\le n\le15\), independently checks maximality of every supported set, and verifies that the probability distribution is normalized. For \(3\le n\le8\), it additionally enumerates every permutation and recomputes the greedy set without using the dynamic program: \(46{,}230\) orders in total. For every \(n=6\) or \(8\le n\le15\), it constructs the local \((2,2,2)\)- versus \((3,3)\)-gap pair and checks the factor-two inequality exactly.

The verification was executed on the packaged script and passed. The proof for all cycle lengths is the independent arrival-mark factorization and deterministic inequality in `RESULT.md`; the finite computation is supporting evidence only. The checks do not determine a uniform-in-size statistical-distance bound, nor do they prove originality.
