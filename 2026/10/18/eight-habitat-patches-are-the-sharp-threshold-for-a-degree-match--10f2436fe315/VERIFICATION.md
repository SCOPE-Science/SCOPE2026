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

# Reproducibility and verification limits

Run `python3 verify.py` with Python 3.9 or later; only the standard library is required. The command emits one line of sorted, compact JSON. Its output must equal `certificate.json` after stripping the trailing newline. That certificate records all tree class counts, every number of degree-matched comparisons, the unique incomparable pair at eight vertices, both fixed-survivor vectors, and the symbolic expectation difference.

The verifier generates all unlabeled trees of orders one through eight by exhaustive leaf attachment with a canonical rooted-tree word, then explicitly enumerates all subsets of their vertices. For the two exceptional eight-vertex trees it independently recalculates the 512 survivor subsets per tree using union-find rather than bitset flood filling. The algebraic deduction from their coefficient difference to the all-probability crossing follows exactly from the Bernstein identity in the proof.

The finite calculation is exhaustive only through eight vertices, not at larger orders. No independent audit or proof-assistant certification has been performed. The public source references support the ecological motivation and the scope comparison; a negative literature search does not prove historical uniqueness.
