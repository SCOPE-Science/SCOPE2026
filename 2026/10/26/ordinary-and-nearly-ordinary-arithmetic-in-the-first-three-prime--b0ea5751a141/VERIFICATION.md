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
# Reproducible verification

Use `python verify.py` under Python 3.10+ with SymPy 1.14.0 or a compatible version. The script contains the complete defining equations and all exact finite computations. It does not read any additional files or access networks.

For the geometrically smooth parameters \((p,k)=(3,2),(5,4),(7,1),(7,3)\), the computed genus and Hasse–Witt ranks are respectively \((10,10),(21,21),(36,35),(36,35)\); ranks of Hasse–Witt squares are equal in every case. Determinants are \(1\), \(4\), \(0\), \(0\) modulo their associated primes. For the two characteristic-seven matrices, the designated rank-35 minors have determinants \(4\) and \(4\), and their square-matrix minors have determinants \(3\) and \(4\). Groebner tests certify absence of singularities over algebraic closures on all affine charts.

The certificate is a self-contained finite-field calculation, not an independently conducted audit or verification of claims at other primes.
