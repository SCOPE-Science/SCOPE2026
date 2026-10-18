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

Run `python3 verify_colored_partitions.py` with Python 3 and no third-party libraries. This directly constructs the elements of Hsiao's ordinary colored ordered-partition semigroup, multiplies each selected tuple, tests the pairwise commutation equations, groups tuples by their exact colored product and ordered vector of factor block counts, and compares each such fiber polynomial with the theorem.

The checked groups are cyclic groups of orders \(1,2,3\) for ordered pairs at \(n\le3\), cyclic groups of orders \(1,2,3\) for ordered triples at \(n\le2\), and both the cyclic and Klein four-groups for pairs at \(n=2\). The program separately reconstructs Stirling numbers from their recurrence and checks each total count, finishing with `VERIFY_OK` on success. For cyclic order two at \(n=3\), the pair total is \(1732\); for both groups of order four at \(n=2\), the pair total is \(784\).

The general theorem follows from a symbolic gap-by-gap bijection and group-product equations given in RESULT.md, not from the finite tests. This is a self-review and does not constitute independent validation.
