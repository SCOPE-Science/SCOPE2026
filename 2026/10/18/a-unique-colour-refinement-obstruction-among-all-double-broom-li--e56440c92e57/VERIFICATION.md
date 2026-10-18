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

# Verification notes

The proof is the exhaustive symbolic case split in `RESULT.md`. The degree counts, orbit structure, and distance-neighbourhood arguments hold for arbitrary positive integer lengths subject to the stated lower bounds. They do not rely on experimental extrapolation.

Execute `python verify_structure.py` using only the standard library. It checks all integer triples \(2\le a\le b\le14\), \(1\le\ell\le30\), constructing the line graph directly from edge incidences and comparing refined classes to the intrinsic automorphism-orbit formula. Its recorded result is `PASS`, with 2,730 triples and just the triple \((2,2,4)\) marked exceptional.

Install `networkx==3.6.1` and execute `python verify_independent.py`. It constructs a tree and applies NetworkX line-graph construction, then identifies whether each stable-colour pair is automorphic by exact graph isomorphism with individualized vertices. It examines 63 triples in the indicated restricted ranges, confirms that \((2,2,4)\) alone fails, and independently recovers exceptional orbit sizes \(2,2,4\). Its recorded result is `PASS`.

The text files ending `_output.txt` record those executions. The scripts have no input downloads and do not require external graph data. Their finite ranges cannot prove the all-order theorem and are not used as substitutes for the case-split proof. Independent scientific validation has not been performed.
