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
# Reproducibility and verification

Run `python3 verify.py` with Python 3 and the standard library from the directory containing the checker. The recorded result is `verification_output.txt`:

```
PRIMITIVE_PREDICATES_CHECKED=935
CONSTRUCTION_LENGTH_CHECKS=55567
BIPARTITE_UNARY_NFA_EXHAUSTIVE_TESTS=214660
CHECKS_PASSED
```

The first two numbers refer to explicit deterministic witness tests across prime-power moduli \(2,3,4,5,7,8,9,11,16,25,27\), including all primitive residue sets for moduli up to nine and selected reproducible primitive sets above nine. Boundary cases are deliberately included as controls, even when the reviewed theorem concerns only genuinely multiresidue sets.

The last count enumerates transition relations on unary alphabets for all automata with one to four states whose simple underlying undirected graph is bipartite. Every accepting-state subset is tested; no such machine matches any of the six proper nonempty modulo-three predicates. A candidate accepted-length sequence is compared over the first \(3\cdot2^q\) lengths, sufficient to detect any difference via the product of its at-most-\(2^q\)-state subset automaton with the three-state residue counter.

These tests are finite and do not constitute proof for arbitrary prime powers, state counts, or alphabets. The general theorem follows from the accepting-cycle eventual-period lemma, prime-power divisibility, and explicit even-cycle construction in `RESULT.md`. No independent audit is claimed.
