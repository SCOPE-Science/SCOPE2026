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

# Reproducibility

Run `python verify_census.py` beside `maxima.json` using Python 3.9 or later; no third-party packages are required. This generates every balanced binary length-\(n\) candidate for \(n\in\{4,6,8,10\}\), discards the `000`/`111` forbidden triples, computes all exact length-\(n-1\) deletion descendants, and constructs the compatibility graph. A second descendant-to-parent construction validates every graph edge.

The checker then enumerates all maximal cliques by a bitset Bron–Kerbosch recursion with pivot, rechecks each stored maximum's deletion-shadow disjointness, compares the complete list of stored maximum codebooks in `maxima.json`, and verifies the length-eight/ten syndrome counts and length-ten reversal/complement orbit decomposition. The recorded observed terminal line is `VERIFY_OK`.

The observed universe sizes are \(6,14,34,84\), maximum clique sizes \(2,4,8,15\), counts of maximum cliques \(4,4,1,20\), and counts of all maximal cliques \(4,16,520,675239\), respectively. Independently, NetworkX `find_cliques` reproduced these counts on separately generated graphs; this is optional cross-checking and not an unrecorded requirement of the standalone verifier.

# Limits

The computation is exhaustive for the four designated lengths, not for larger lengths. Its proof of exhaustive coverage uses the recursion invariant and complete vertex generation; a partial sample or arbitrary timeout would not certify the result. Biological sequence constraints and arbitrary symbol errors are not modeled. Independent validation has not been performed.
