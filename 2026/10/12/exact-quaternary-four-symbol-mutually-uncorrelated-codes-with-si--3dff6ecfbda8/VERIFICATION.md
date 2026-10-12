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

# Reproduction and exact limits

Run `python3 verify_primary.py` and `python3 verify_secondary.py` using Python 3 without installing dependencies. Both files implement their own eligibility criteria, graph construction, and exhaustive clique algorithms, and each ends with `VERIFY_OK` after all checks pass.

Primary verified partition count fourteen, \(45\) candidates for each \(1+3\) class and \(60\) for each \(2+2\) class; maximum clique sizes \(9\) (eight partitions) and \(12\) (six partitions), four maximizers per balanced partition, twenty-four distinct globally optimal codes, with orbit sizes \(12,12\) under the symmetric group on alphabet symbols.

Secondary counted \(24\) total twelve-vertex cliques and zero thirteen-vertex cliques, using a greedy coloring upper bound to prune an exact depth-first search. Its count per balanced partition was exactly four and was zero elsewhere.

The partition coverage lemma and clique/constraint equivalence appear in `RESULT.md`; together with the exhaustive finite enumeration they prove the asserted statement for four-letter words over four distinguishable symbols. No part of the computation verifies claims for other alphabets, lengths, Hamming distances, reversal, or reverse complements. Both implementations are reproducibility checks, not an external independent audit.
