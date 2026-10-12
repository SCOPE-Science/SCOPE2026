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
# Computational verification

Run `python verify.py` in a Python 3 environment with SymPy installed. The script is self-contained and needs no third-party research data. It checks the elimination identity
\[\operatorname{Res}_T\bigl(T^3-2,(x-y)^2-T^2z(x+y)-2Tz^2\bigr)=(x-y)^6-16z^3F\]
over the integers. For the explicit rational degree-nine polynomial \(G=F((x-y)^6-16z^3F)\), it constructs the full degree-\(r\) Jacobian-coefficient matrix for \(r=1,2,3\), with sizes \((55,9)\), \((66,18)\), \((78,30)\), and exactly computes ranks \(9\), \(18\), \(29\). It prints `VERIFY_OK ...` upon success. The arithmetic field and Galois arguments in RESULT.md are formal deductions independent of finite sampling, including explicit coefficient recovery and label permutations. Their premises are verified against the cited original conic equation. This computation does not independently certify completeness of published geometric singularity calculations or search every possible prior publication. External independent audit is not performed.
