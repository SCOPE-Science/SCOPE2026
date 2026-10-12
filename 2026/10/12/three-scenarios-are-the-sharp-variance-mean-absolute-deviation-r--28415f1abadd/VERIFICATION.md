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
For two equally weighted observations \(x,y\), the centered deviations are
\[
\pm\frac{x-y}{2},
\]
so
\[
M=\frac{|x-y|}{2}
\]
and
\[
V=M^2.
\]
This proves the universal support-two order agreement.

For the three-scenario witness
\[
A=(10,20,30),
\qquad
B=(14,15,31),
\]
the embedded verifier checks
\[
\bar A=\bar B=20,
\]
\[
M(A)=\frac{20}{3},
\qquad
M(B)=\frac{22}{3},
\]
and
\[
V(A)=\frac{200}{3},
\qquad
V(B)=\frac{182}{3}.
\]

For centered triples
\[
(-a,-b,a+b),
\]
it replays the exact identities
\[
M=\frac{2(a+b)}{3}
\]
and
\[
V=\frac{(a+b)^2}{2}+\frac{(a-b)^2}{6}.
\]

The persistent family is checked for every \(3\le n\le500\).

Run:

`python3 verify_mad_variance_minimal_scenarios.py`

The first output line must be:

`VERIFY_OK`

The universal support-two identity and all-support padding formulas are proved algebraically in `RESULT.md` rather than inferred from the finite replay.
