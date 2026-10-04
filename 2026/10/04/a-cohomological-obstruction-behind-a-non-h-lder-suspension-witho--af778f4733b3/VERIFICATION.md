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

The proof was checked directly from the stated symbolic metric and roof formulas. For the point with a single \(1\) at coordinate \(-1\), forward iteration sends that symbol to \(-1-k\), hence
\[
d(\sigma^k a,\underline 0)=\frac{2^{-k}}6.
\]
Substitution into the logarithmic roof yields
\[
\tau(\sigma^k a)-\tau(\underline 0)=\frac1{1+\ln6+k\ln2},
\]
whose partial sums diverge.

Under a hypothetical decomposition \(\tau=h+u-u\circ\sigma\), Hölder continuity of \(h\) makes the stable difference series absolutely convergent, and continuity of \(u\) makes the telescoping endpoint converge. These two facts are incompatible with the exact divergent series above.

For the contrasting family, \(0\le u_c\le c<1\) verifies positivity of \(r_c\). Points with one \(1\) at coordinate \(n\) give an exact roof difference of order \(n^{-2}\) at metric distance of order \(2^{-n}\), excluding every positive Hölder exponent. The standard cohomologous-roof coordinate change supplies a time-preserving topological conjugacy to the constant-roof suspension, so the local product structure furnished for the Hölder constant roof transfers to \(r_c\).

Limits: no converse classification is proved, and no claim is made beyond continuous cohomology over the same base shift. No numerical or finite-search evidence is used in the proof.
