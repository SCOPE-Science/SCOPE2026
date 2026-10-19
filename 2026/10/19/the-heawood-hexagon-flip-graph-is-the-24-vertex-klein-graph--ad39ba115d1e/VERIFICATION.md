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

# Finite checks and reproducibility

Both verification scripts are standalone Python 3 programs requiring only the standard library. Extract the scripts and all three text data files into one directory; run `python3 verify_flips.py` and `python3 verify_binary.py` from that directory. `VERIFY_FLIPS_OUTPUT.txt` and `VERIFY_BINARY_OUTPUT.txt` record their actual output. Both scripts finished with all assertions satisfied.

The cyclic-model checker inspects each of the \(5040\) permutations of seven line labels, all six-cycle candidates, every matching--hexagon incidence, all \(576\) entries of the purported Klein graph isomorphism, and all rooted shortest-distance distributions and intersection-number conditions. Its inputs are the full reference matrix `KLEIN_ADJACENCY.txt` and the explicit bijection `ISOMORPHISM.txt`. A successful graph-isomorphism test is an exact adjacency equivalence, not an inference from equal degree or spectrum.

The independent binary-plane checker constructs the point--line relation using binary dot products, backtracks all incidence perfect matchings, produces flips through admissible three-partner permutations, and independently checks the \(24\)-vertex distance-regularity and antipodal quotient.

The certificate proves facts for the stated finite graph only. `KLEIN_ADJACENCY.txt` is a snapshot of the public matrix; its source link is in `RESULT.md`. The status in the JSON front matter accurately records that no independent external audit has been performed.
