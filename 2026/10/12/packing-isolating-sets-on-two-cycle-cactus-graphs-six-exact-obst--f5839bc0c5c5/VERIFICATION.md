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

# Reproducibility and limitations

The data file `seed_table.csv` contains exactly 231 parameter triples. `build_seeds.py` constructs the table by complete backtracking of remaining edge coverage, choosing every potentially eligible center covering a currently uncovered edge subject to distance-two exclusions. `verify_seeds.py` independently reconstructs each graph; for each of the 225 positive rows it checks the exact displayed set, for each of the six negative rows it tests every vertex subset. Both scripts require only Python 3 and their own directory as working location.

To replay from a directory with all extracted files: `python3 build_seeds.py > build_seeds.out` then `python3 verify_seeds.py > verify_seeds.out`. The recorded outputs are embedded in this package. Successful verification must reproduce `FINITE_BASE_CERTIFICATE_OK`, with 225 accepted witnesses, six negative cases, and zero valid packing-isolating subsets in each of the six negative cases. The six packing-subset totals, in listed order, are 22, 31, 26, 66, 97, and 304.

The finite certificate establishes the base cases only. The proof's three-vertex subdivision lemma and reduction argument establish the theorem for all integer cycle lengths and bridge lengths. The theorem excludes attached trees, chords, and additional cycles. Independent audit has not been performed.
