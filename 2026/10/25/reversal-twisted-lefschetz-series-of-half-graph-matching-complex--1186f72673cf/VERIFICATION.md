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

# Reproducible verification

Run `python3 verify.py` with a standard Python 3 installation. The program uses integer arithmetic and no third-party packages.

The first computation enumerates every nonattacking-rook matching in the staircase board for each \(1\leq n\leq9\). It acts on each simplex by the graph involution, computes the parity of the induced ordering permutation, and sums the signed contributions by simplex size, including the empty face.

An independent integer recurrence assembles the contributions of self-reversed blocks and exchanged block pairs on labelled reversal pairs, and adds the central-block factor when needed. The verifier compares the complete coefficient dictionaries, not merely their values at \(y=-1\). Successful execution ends with `HALFGRAPH_REFLECTION_GRADED_TRACE_VERIFIED n=1..9`.

The enumeration is finite, whereas the universal formulas are proved by a bijection and the labelled exponential formula in `RESULT.md`. The recurrence and finite tests cannot establish the homology of the quotient in individual degrees or an independent audit.
