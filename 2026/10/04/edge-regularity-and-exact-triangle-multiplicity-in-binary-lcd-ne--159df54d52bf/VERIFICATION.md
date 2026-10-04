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

The accompanying `verify_lcd_triangles.py` uses only the Python standard library. It enumerates every subspace of \(\mathbb F_2^n\) for \(2\le n\le6\), tests the LCD condition by exact binary Gram-matrix rank, constructs the neighbor graph in every dimension \(1\le k\le n-1\), and checks:

- every vertex has degree \( (2^k-1)(2^{n-k}-1) \);
- every edge has exactly \(2^k+2^{n-k}-4\) common neighbors;
- the exact triangle count equals \( |V|(2^k-1)(2^{n-k}-1)(2^k+2^{n-k}-4)/6 \).

Replay command: `python3 verify_lcd_triangles.py`. Expected final line: `VERIFY_OK`.

These finite checks are corroborative only. The theorem for arbitrary \(n\) and \(k\) is established by the symbolic proof in `RESULT.md`. Independent audit and independent validation have not been performed.
