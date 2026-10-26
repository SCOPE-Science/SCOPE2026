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
# Verification

Execute `python3 pd_moment_checker.py` with Python 3.10 or later; the program prints a JSON certificate to standard output. Compare it bytewise or parse and compare structurally with `pd_moment_certificate.json`. The script generates non-plane full binary shapes by the complete unordered-child recurrence through 16 leaves; records the exact descendant-size and pairwise-clade-union histograms for each tree; asserts zero collisions for 2–15 tips and one for 16 tips; and asserts that this collision is precisely the displayed pair. It then enumerates all nonempty subsets of the 16 leaves in each tree, and directly checks equality of sums of rooted phylogenetic diversity and its square at every cardinality. For the 120 two-leaf selections it also checks the exact frequency distributions and cube sums (54370 versus 54376).

These are finite, reproducible exhaustive checks, not a computer proof of a universal theorem. The general equality of moments under equal-size subtree interchange and the extension to all larger tip counts are established by the explicit symbolic arguments in RESULT.md. No external validation or independent audit has been performed. The source-code interpreter and operating environment are not formal proof assistants.
