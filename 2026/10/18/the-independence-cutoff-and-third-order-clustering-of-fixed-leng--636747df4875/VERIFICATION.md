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

# Reproducibility and scope

Run the accompanying standalone standard-library script `python check_palindrome_count.py`. Its exact rational tests passed 2931 assertions: every small uniform word for selected alphabets and lengths; joint-success probabilities of all small start-subsets; covariance and third-cumulant identities; finite offset classification for palindrome lengths four and five; and direct nonuniform overlapping-window checks.

For arbitrary word lengths, the verification method is the proof: create reflection-equality edges for each selected window, count connected components, then use independent uniform component-label assignments. The pairwise forest argument and triple-rank lemma in RESULT.md support the all-parameter independence and cumulant claims. Exhausting finitely many word lengths does not establish the infinite-range claims on its own. External independent scientific audit and exhaustive historical-priority search are not performed. The full text of one plausibly related DNA-palindrome paper was unavailable.
