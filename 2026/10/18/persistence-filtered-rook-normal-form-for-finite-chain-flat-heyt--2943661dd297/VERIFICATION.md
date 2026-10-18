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

# Reproducible checks and limits

Run `python3 verify.py` using an ordinary Python 3 installation; the script uses only its standard library. The expected trailing output line is `VERIFY_OK`; `checker_output.txt` contains the complete output of the executed program.

For every length \(1\leq n\leq6\), the script visits all \((n+1)^n\) possible row-threshold vectors for upward-flat relations. It independently evaluates \((p\rightsquigarrow q)\to\Box(p\rightsquigarrow q)\) for every ordered pair of persistent valuations, compares it with the rook exclusion criterion, verifies that equal last-occurrence maps have identical complete operation tables, and that distinct maps produce different tables. It also checks counts obtained by exhaustive rook enumeration against the closed product-sum for \(1\leq n\leq8\).

The script checks finite parameter instances only. The proof for arbitrary finite \(n\) is the symbolic argument in `RESULT.md`. The result is not asserted for infinite chains or general posets. Independent audit has not been performed.
