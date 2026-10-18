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
# Verification details

Run `python3 verify_crown_forts.py` using the standard Python 3 library. The program builds the graph adjacency directly, independently simulates all possible initial zero forcing subsets for \(3\le n\le9\), tests every potential fort for \(3\le n\le8\), checks each candidate's minimality against all proper subsets, and performs exact minimal-fort packing for \(3\le n\le7\).

The expected terminal output is recorded verbatim in `verification_output.txt`. The total of \(349{,}504\) forcing initial subsets is the sum of powers of two for the seven investigated graphs, not a claim of infinite exhaustive coverage. Explicit binomial and congruence checks are finite checks through order eighty. The general conclusions require the mathematical proof in RESULT.md, including its fractional linear-programming argument.

No independent scientific audit has been performed.
