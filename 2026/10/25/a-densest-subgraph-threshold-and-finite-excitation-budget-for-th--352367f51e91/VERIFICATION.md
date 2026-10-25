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

# Reproducible checks and limitations

Run `python3 verify_density.py` with Python 3.9 or later; the complete output is included as `verification_output.txt`. The program uses exact rational arithmetic for maximum induced edge density, enumerates all \(11{,}259\) initial three-state configurations in nine small-graph test cases, checks separation of successive excitation times, checks matching of transmissions along each edge and verifies total activity and extinction bounds. It also checks an explicit nonzero four-cycle on \(K_{2q,2q}\) for \(q=1,2,3\). Recorded terminal marker: `VERIFICATION_OK`.

The computational work is finite; the theorem for every finite graph and every integer \(q\ge2\) is supported by the full event-matching and induced-level-set proof in RESULT.md, not by brute-force extrapolation. The all-graph claim does not assert tightness of its numerical lifetime bound for every graph, nor persistence for every graph at density \(q\). No independent audit is recorded.
