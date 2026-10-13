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
The theorem uses exact formulas in the equal-total two-tract setting.

If the smaller tract has total population \(t\) and absolute group imbalance \(d\), then
\[
D=\frac dN
\]
and
\[
I=\frac12+\frac{d^2}{2t(2N-t)}.
\]

The embedded `verify_dissimilarity_isolation_minimal_reversal.py` independently enumerates raw tract counts and the symmetry-reduced \((t,d)\) states.

For every raw configuration it verifies equality between:
- direct evaluation of the standard dissimilarity and isolation formulas;
- evaluation through the two closed forms above.

The exact canonical-state counts for \(N=1,\ldots,8\) are
\[
1,\ 3,\ 5,\ 8,\ 11,\ 15,\ 19,\ 24.
\]

The exact strict-reversal counts are
\[
0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 0,\ 1.
\]

At \(N=8\), the unique canonical reversal is
\[
(t,d)=(1,1)
\]
versus
\[
(t,d)=(8,2),
\]
corresponding to
\[
(1,0)+(7,8)
\]
and
\[
(5,3)+(3,5).
\]

The replay also verifies that the first weak-order difference occurs at \(N=3\) only by tie splitting and checks the explicit strict-reversal family through \(N=500\). The family for every \(N\ge8\) is proved algebraically in `RESULT.md`.

Run:

`python3 verify_dissimilarity_isolation_minimal_reversal.py`

The first output line must be:

`VERIFY_OK`
