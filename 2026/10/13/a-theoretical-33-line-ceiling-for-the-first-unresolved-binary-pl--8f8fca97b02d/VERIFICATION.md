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
`artifacts/verify.py` uses only the Python standard library.

It reconstructs the points of
\[
\operatorname{PG}(4,2)
\]
as the nonzero vectors of \(\mathbb F_2^5\), then enumerates all projective lines and planes by binary spans. It verifies that there are \(31\) points, \(155\) lines, and \(155\) planes, and that every line contains \(3\) points and lies in \(7\) planes.

The script checks the numerical convexity bounds used in the proof:
\[
\min_{\sum d_P=102}\sum_P\binom{d_P}{2}=120
\]
over \(31\) point degrees, and, after fixing three degree-two points for a doubled line at \(m=33\),
\[
3\binom22+
\min_{\sum_{28}d_P=93}
\sum\binom{d_P}{2}
=114.
\]

It also checks the five possible plane-occupancy triples of a hypothetical simple \(33\)-line configuration.

Finally, an explicit set of \(32\) distinct projective lines is verified. Every one of the \(155\) planes contains either zero or two selected lines, with distribution
\[
43:112
\]
for occupancies \(0:2\).

Successful replay prints `VERIFY_OK`.
