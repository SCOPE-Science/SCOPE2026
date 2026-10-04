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

The verification target is the explicit family \(C_t\) at \(t=\frac12\), \(t=\frac23\), and \(t=\frac34\). Run `python3 artifacts/verify.py` from the package root. The script uses only the Python standard library and exact integer arithmetic.

For each parameter it reconstructs the degree-eleven arrangement polynomial from its eleven linear factors, differentiates it, verifies one degree-five and two degree-six Jacobian syzygies, verifies their degree-seven relation, and computes modular ranks of the full syzygy coefficient matrices. The ranks force rational syzygy dimensions \(1\), \(5\), and \(11\) in degrees \(5\), \(6\), and \(7\). It then checks the intersections of the two linear relation entries and arrangement membership.

The replay confirms \(P_{1/2}=[7:9:8]\notin C_{1/2}\), reproduces \(P_{2/3}=[4:5:4]\in C_{2/3}\), and reproduces the source's first printed matrix and point at \(t=\frac34\). Successful replay prints `VERIFY_OK`.

The computation does not prove a formula for arbitrary \(t\), does not classify all special parameter values, and does not assess any independent audit channel.
