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

Run `python3 verify_parsing.py` in the directory containing this document and the included script. The script uses only the Python standard library. It separately constructs generalized Cantor prefixes by substitution and by arithmetic on base-\(q\) digits, verifies their equality, and independently implements the shortest-new-factor exhaustive parsing with earlier occurrence positions allowed to overlap the phrase boundary. It compares the complete list of phrase starts with the theorem for \(q=3,\ldots,12\), over input lengths between 14,641 and 100,000 (with other selected depths included). The expected final line is `VERIFY_OK`.

The infinite proof uses the bound on internal zero runs and the two contiguous innovative phrase families; this finite test is not an exhaustive verification of all lengths or parameters. Any different interpretation of overlapping occurrences may give different phrase boundaries. Independent scientific audit has not been performed.
