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

Run `python3 verify.py` with a standard Python 3 interpreter. The checker computes Baum–Sweet bits from ordinary binary digit runs, the greedy-arch count and the closed formula independently; it scans all prefix lengths one to 1,048,576, checks accepted-adjacency and dyadic Fibonacci counts, and brute-tests all binary target subsequences for each prefix through length 29. Success gives `PREFIX_OK` and `BRUTE_OK`.

The finite checker is a consistency and regression aid, not a proof of the infinite theorem. The complete mathematical argument is in `RESULT.md` and covers the adjacency lemma, arch universal index, all-prefix boundaries, and Fibonacci digit count. The digital-DP formula is symbolic, and no runtime cost beyond stated arithmetic-operation complexity is claimed.
