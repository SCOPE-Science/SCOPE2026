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

`verify.py` checks the census in two independent ways. First, for every tested pair \((t,e)\) with \(t\le4\), it explicitly generates all choices of singleton-or-pair neighborhoods for every labeled depth-one point, forms the graph on top points induced by pair choices, and tests connectivity directly. Those exhaustive counts are compared to the partition-lattice Möbius formula.

Second, independently of brute-force connectivity, the script checks the connected-component recurrence equivalent to the two-sort exponential identity
\[
A(x,y)=\exp C(x,y)
\]
through \(t\le8\) and \(e\le10\), where \(A\) counts all incidence systems and \(C\) counts connected ones. It also verifies \(N_{2,e}=3^e-2^e\) and the stated globally labeled totals \(R_m\).

The recorded run is

```text
N(t,e) rows (e=1..7 where shown):
1 [1, 1, 1, 1, 1, 1, 1]
2 [1, 5, 19, 65, 211, 665, 2059]
3 [0, 6, 78, 690, 5190, 35826, 235158]
4 [0, 0, 96, 2472, 40800, 552360, 6705216]
5 [0, 0, 0, 3000, 131640, 3566400, 77322000]
R_m (distinguished root; m labeled nonroot points):
[2, 6, 34, 255, 2541, 31948, 482308]
VERIFY_OK 136 exact formula/recurrence assertions; exhaustive assignment grid through t=4
```

The replay verifies the finite combinatorics only. The geometric completeness theorem and finite-frame characterization are cited premises from the primary source.
