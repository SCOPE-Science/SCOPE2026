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
Run `python3 verify.py`.

The checker tests every base
\[
8\le b\le200000.
\]
For every base satisfying
\[
3\nmid b
\]
and squarefreeness of
\[
b,\qquad b-2,\qquad 2b-3,
\]
it constructs
\[
x=b(2b-3),
\qquad
y=(b-2)(2b-3),
\]
computes both base-\(b\) digit sums by repeated Euclidean division, and verifies that \(x\) and \(y\) are distinct squarefree integers with
\[
xS_b(x)=yS_b(y).
\]

It also counts the qualifying bases in the subprogression
\[
b\equiv5\pmod{36}.
\]
This is only a regression check. The all-base collision theorem under the stated hypotheses and the lower-density bound \(7/900\) are proved symbolically in `RESULT.md`.

A successful replay prints `VERIFY_OK`.
