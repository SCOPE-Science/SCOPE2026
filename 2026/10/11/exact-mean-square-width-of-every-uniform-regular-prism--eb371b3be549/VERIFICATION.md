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

For
\[
P_n=B_n\times[-1/2,1/2]
\]
and
\[
U=(\sqrt{1-Z^2}V,Z),
\]
one has exactly
\[
w_{P_n}(U)=\sqrt{1-Z^2}\,w_{B_n}(V)+|Z|.
\]
The scalar expectations are
\[
\mathbb E(1-Z^2)=\frac23,
\qquad
\mathbb E Z^2=\frac13,
\qquad
\mathbb E(|Z|\sqrt{1-Z^2})=\frac13.
\]
Thus only the first two planar width moments remain.

The first moment is \(n/\pi\) by Cauchy's perimeter formula. The second moment is the squared-support moment of the difference body. For even \(n\), that difference body is \(2B_n\); for odd \(n\), its extreme differences alternate to form a regular \(2n\)-gon. Integrating the support function over one normal cone yields the exact formulas in RESULT.md.

`verify.py` reconstructs the regular base vertices, directly computes widths on deterministic angular grids, and independently samples the spatial prism width on a Fibonacci sphere. It checks both parity branches and the cube specialization.

These finite computations are diagnostics only. No finite sampling is used to justify the quantified theorem.
