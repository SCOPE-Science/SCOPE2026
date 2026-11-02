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

# Reproducible finite checks

Run `python3 verify_orbits.py` and `python3 verify_forest.py` with Python 3 and its standard library. Compare the resulting standard output byte-for-byte with `orbit_results.txt` and `forest_results.txt`. No downloaded input data, randomness, third-party software or external services are required.

The orbit program builds every root-ground-set permutation orbit of ordered graph-vertex tuples for variable widths \(2\), \(3\), and \(4\). It refines atomic equality/adjacency types under all possible replacement moves with **sets**, not multiplicities, until no further splitting occurs. Finite models tested are root orders \(3\)–\(7\), \(3\)–\(9\), and \(3\)–\(10\), respectively. It confirms exact partitions \(3\mid4,5,6,7\), \(3\mid4\mid5\mid6,7,8,9\), and \(3\mid4\mid5\mid6\mid7\mid8,9,10\). These are complete within the finite ranges studied and for arbitrarily many refinement rounds, not a proof of the infinite parameter statement.

The second program independently builds path forests for root-size thresholds \(s=4,\ldots,2p\) at widths \(p=2,3,4,5\). For each such adjacency diagram it checks existence on exactly \(s\) root points and nonexistence on \(s-1\) root points by a recursive exhaustive search of ordered edge configurations. Thirty-two finite truth checks pass. It is not an exhaustive verification for every width.

The general theorem rests on the written invariant and elementary path reconstruction lemma. No independence claim or external certificate is asserted.
