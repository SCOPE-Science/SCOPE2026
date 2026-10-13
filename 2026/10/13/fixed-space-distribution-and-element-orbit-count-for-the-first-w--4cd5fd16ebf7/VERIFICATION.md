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
The symbolic proof reduces every fixed-space computation to a triangular four-equation system. The critical exceptional branch \(a=-1\) was checked algebraically: the last constraint is \((b^2+c)x_2=0\). The root-of-unity counts use cyclicity of \(\mathbb F_{5^e}^\times\): there are always two elements of exact order \(4\), and two of exact order \(3\) exactly for even \(e\).

`verify.py` was replayed from the package itself. It exhaustively checks all automorphisms over \(\mathbb F_5\), directly constructs all element orbits there, and independently checks the complete fixed-space distribution over \(\mathbb F_{25}\). These finite computations test the formulas but do not prove the general \(e\)-parameter statement.
