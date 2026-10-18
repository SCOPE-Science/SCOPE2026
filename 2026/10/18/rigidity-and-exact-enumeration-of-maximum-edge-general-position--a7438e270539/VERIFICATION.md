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
# Reproduction of finite checks

Run `python3 theta_verify.py` using a standard Python 3 installation. The script is a standalone exact enumerator of vertex-pair geodesics and forbidden-three-edge intersections and requires no third-party modules.

Observed output:
```
PASS: full edge-subset maxima on 6 graphs
PASS: all two-per-arm candidates on 13 graphs
PASS: every predicted construction on 180 parameter/position instances
Checked 42027 geodesic masks (with repetitions across tests)
```

The full maximum-subset search uses graphs \((m,L)=(3,2),(3,3),(3,4),(4,2),(4,3),(5,2)\), and the armwise enumeration covers \(m=3,\ 2\le L\le7\), \(m=4,\ 2\le L\le5\), and \(m=5,\ 2\le L\le4\). Construction checks additionally cover \(3\le m\le7\) and \(2\le L\le12\). The all-integer theorem rests on the complete self-contained proof in `RESULT.md`. Exhaustive finite instances cannot certify untested infinite cases; independent scientific audit is not performed.
