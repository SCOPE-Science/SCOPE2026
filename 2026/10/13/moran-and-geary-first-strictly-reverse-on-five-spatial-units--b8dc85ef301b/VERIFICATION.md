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
For symmetric adjacency weights, the exact identity used in the proof is
\[
C
=
\frac{n-1}{S_0}
\frac{\sum_i d_i z_i^2}{\sum_i z_i^2}
-
\frac{n-1}{n}I.
\]
On an \(r\)-regular graph this becomes
\[
C=\frac{n-1}{n}(1-I).
\]

For a binary field, the verifier independently uses the exact count formulas
\[
C=\frac{n(n-1)q}{2mk(n-k)}
\]
and
\[
I=\frac{2k^2m+n(n-2k)s-n^2q}{2km(n-k)}.
\]

The embedded `verify_moran_geary_minimal_reversal.py` generates every connected simple graph through five vertices and canonicalizes each graph under all vertex permutations. It checks every nonconstant binary field using exact `Fraction` arithmetic.

It recovers connected-unlabeled graph counts
\[
1,
2,
6,
21
\]
for orders \(2,3,4,5\), and reversal-admitting class counts
\[
0,
0,
0,
11.
\]

The exact \(P_5\) witness values are
\[
\left(-\frac1{16},\frac58\right)
\]
and
\[
\left(\frac1{24},\frac56\right).
\]

The script also checks the general degree-weighted identity on every enumerated graph, the regular-graph specialization on every enumerated regular graph, and the path-family formulas through \(n=500\) as a finite consistency test.

Run:

`python3 verify_moran_geary_minimal_reversal.py`

The first output line must be:

`VERIFY_OK`
