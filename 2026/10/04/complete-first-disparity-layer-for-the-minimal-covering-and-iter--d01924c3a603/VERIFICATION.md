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
The embedded `verify_mc_ucinf_first_layer.py` performs a complete exact replay using only the Python standard library.

For every labeled tournament of orders \(1\) through \(6\), the uncovered set is computed independently from:
1. the covering relation;
2. directed reachability within two steps.

The two implementations are iterated separately to the same fixed point \(UC^{\infty}\).

The minimal covering set is computed independently from:
1. full internal and external covering stability over every nonempty subset;
2. external stability alone, followed by direct verification of internal stability of the unique inclusion-minimal set.

The verifier confirms:
- equality \(MC(T)=UC^{\infty}(T)\) for every tournament through order \(5\);
- exactly \(240\) strict cases among the \(32768\) labeled order-\(6\) tournaments;
- exact incidence \(15/2048\);
- complete order-\(6\) joint-size histogram
\[
(1,1):6144,\quad
(3,3):20240,\quad
(5,5):4704,\quad
(6,6):1440,\quad
(3,6):240;
\]
- \(UC(T)=UC^{\infty}(T)=A\) on every strict case;
- exactly one strict isomorphism class;
- canonical bit encoding `1332` under lexicographic pair order;
- orbit size \(240\) and automorphism-group order \(3\);
- canonical minimal covering set \(\{B,E,F\}\);
- outdegree partition \((2,3,2,2,3,3)\);
- unique external coverers \(B,F,E\) for \(A,C,D\), respectively.

Run:

`python3 verify_mc_ucinf_first_layer.py`

The first output line must be:

`VERIFY_OK`

The computation establishes only the stated first disparity layer.
