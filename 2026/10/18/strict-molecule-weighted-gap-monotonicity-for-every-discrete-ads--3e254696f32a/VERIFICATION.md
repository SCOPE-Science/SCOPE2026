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

The proof directly derives the exact integral identity, changes variable \(y=s^k\), proves the strict reflected-kernel comparison by a logarithmic derivative, and checks the integrability and parameter boundaries \(k\ge2\) and \(0\le l\le k-2\). In particular, the calculation uses the exact sum \(\sum_{j=0}^{k-1}(y^{j/k}-(1-y)^{j/k})\) and does not rely on numerical estimates for large \(k\).

To reproduce the finite consistency tests, run `python3 check_gap.py` using Python 3. The recorded run completed with `PASS: 1554 exact/algebraic/numerical assertions`. The exact rational portion checks identities on finite grids, and the numerical portion compares finite integral approximations. Neither is represented as a machine proof for all natural parameters. No external proof certification or independent audit has been performed.
