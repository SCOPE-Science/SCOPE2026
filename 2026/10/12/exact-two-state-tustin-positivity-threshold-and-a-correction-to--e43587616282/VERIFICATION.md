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
The universal algebraic identity is
\[
T_h=2\left(I-\frac h2A\right)^{-1}-I.
\]
For a Hurwitz Metzler matrix, the inverse in this formula is nonnegative. Hence the all-dimensional positivity test reduces exactly to its diagonal entries being at least \(1/2\).

For
\[
A=
\begin{pmatrix}
-a&b\\
c&-d
\end{pmatrix},
\]
direct inversion gives the two diagonal numerators
\[
1\pm(d-a)\frac h2-(ad-bc)\frac{h^2}{4}.
\]
Their conjunction yields the claimed sharp threshold.

The embedded `verify.py` uses only exact rational arithmetic. It checks the published-condition counterexample, the coupled example with exact threshold \(h_\star=4\), the retained conservative bound, and a representative three-state resolvent identity.

Finite calculations are witness replays only. They do not substitute for the exact symbolic proof. Higher-order Padé maps and closed-form higher-dimensional sampling thresholds are not established here.
