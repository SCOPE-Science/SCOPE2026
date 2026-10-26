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

# Reproduction of the finite census

Execute `python3 verify_lcf.py`, `python3 verify_bipartite.py`, and `python3 verify_orbits.py` from the directory containing the three scripts. They use the Python 3 standard library only; no external input, randomness, internet access or graph package is required.

The first two independently constructed implementations exhaust all \(495\) four-subsets and \(792\) five-subsets of the twelve original vertices. Their parallel bitmask and serial set-based forcing closures agree: no forcing four-set, exactly \(324\) forcing five-sets. Both construct and exhaust the complete one-exchange relations, verifying \(2910\) token-jump edges, \(534\) token-slide edges, connectivity in both relations, diameters \(5\) and \(13\), and the exact eccentricity and pair-distance histograms. They independently obtain a maximum token-slide distance of \(9\) among token-jump-adjacent pairs and the same concrete example. The separate automorphism enumerator computes \(48\) automorphisms and nine minimum-set orbits, including the representative degrees and eccentricities.

The three `*_output.json` files contain recorded successful outputs. The included checks have been rerun from these exact three script paths; output comparison matched. The proof concerns only this finite graph, and its exhaustive computations should not be interpreted as an infinite-family theorem. The available material does not constitute independent external auditing, and the literature check does not guarantee priority against unindexed sources.
