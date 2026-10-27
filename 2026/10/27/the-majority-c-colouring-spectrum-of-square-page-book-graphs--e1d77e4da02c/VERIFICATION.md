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
# Reproduction and limits

Run `python3 verify.py` with Python 3.8 or newer and no third-party packages. The checker independently builds a graph on \(2b+2\) vertices with all spine and page edges; it exhaustively generates all set partitions of those vertices, not merely assignments of predetermined page patterns, and checks the actual open-neighbourhood majority inequality at each vertex. Exact enumerations cover \(b=1,2,3,4\) and reproduce the spectra \(\{1:1,2:2\}\), \(\{1:1,2:3\}\), \(\{1:1,2:19,3:6\}\), and \(\{1:1,2:31,3:10\}\). For these and \(5\le b\le20\), it separately computes both structural sums using exact integer Stirling-number recurrences and confirms the stated optimum and extremal binomial count. See `verify_output.txt` for the actual recorded output.

These finite checks cannot verify the theorem for arbitrary large \(b\); that assertion rests on the page-type proof in `RESULT.md`. The calculations do not establish literature priority or independent validation. All quantities refer to unlabelled set partitions unless explicitly multiplied by the number of permutations of the named colour palette.
