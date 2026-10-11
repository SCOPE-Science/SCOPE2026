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

The proof was replayed from the definition and the displayed octagonal norm.

For \(x=(1,\sqrt2-1)\) and \(y_t=(-t/6,t)\) with \(0<t<12/35\), the exact active supports are
\[
N(x)=1,\qquad N(y_t)=t,
\]
\[
N(x-y_t)=1+t/6,
\qquad
N(x+y_t)=1+5t/(6\sqrt2).
\]
The interval inequalities establishing these supports are strict, so no hidden facet switch occurs before the limiting parameter.

Substitution gives
\[
D(t)=N(x)^2+N(y_t)^2-N(x-y_t)^2
=\frac{t(35t-12)}{36}<0,
\]
and
\[
A(t)=N(x)^2+N(y_t)^2-N(x+y_t)^2
=\frac{t(47t-60\sqrt2)}{72}<0.
\]
Hence every prelimit pair is admissible and
\[
\frac{A(t)}{D(t)}=\frac{47t-60\sqrt2}{2(35t-12)}\longrightarrow+\infty
\quad\text{as}\quad t\uparrow12/35.
\]

At \(t=12/35\), the denominator is exactly zero and \(N(x-y_t)=37/35\), while the numerator remains strictly negative. This identifies the excluded limiting Pythagorean-orthogonal pair and confirms the one-sided positive blow-up.

No numerical experiment is needed for correctness. Bibliographic search cannot certify absolute uniqueness; the remaining risk is only an unindexed prior observation, not a mathematical gap in the proof.
