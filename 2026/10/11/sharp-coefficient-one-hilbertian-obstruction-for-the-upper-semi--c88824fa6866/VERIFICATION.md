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
The focal paper's Lemma 3.1 was checked for the exact identity between \(d_+(T)\) and the least perturbation norm producing an infinite-dimensional kernel. Theorem 5.1 and Section 6 were checked for the published coefficient \(1/2\) and for the definitions of the quantitative invariants.

For the new proof, the following points were recomputed directly:

- From \(\|(I-P)x\|\le s\|x\|\), the restriction \(P|_M\) is bounded below by \(1-s\), so its image is closed and \(\|(P|_M)^{-1}\|\le(1-s)^{-1}\).
- The error operator satisfies \(\|A-I\|\le s^2/(\varepsilon(1-s))\). The condition \(\varepsilon<1/(c(1+c))\) makes this strictly less than \(1\) whenever \(s<c\varepsilon\).
- The resulting projection obeys
\[
\|R\|\le B_\varepsilon(s)=\frac{s(1-s)}{\varepsilon(1-s)-s^2}.
\]
Direct differentiation gives
\[
B_\varepsilon'(s)=\frac{\varepsilon(1-s)^2+s^2}{\bigl(\varepsilon(1-s)-s^2\bigr)^2}>0.
\]
- Substituting \(s=c\varepsilon\) gives
\[
B_\varepsilon(c\varepsilon)=\frac{c(1-c\varepsilon)}{1-c(1+c)\varepsilon},
\]
and the second stated bound on \(\varepsilon\) is algebraically equivalent to this quantity being less than \(\Gamma\).
- Therefore every perturbation of norm below \(c\varepsilon\) avoids an infinite-dimensional kernel, so the focal infinite-kernel formula gives \(d_+(T_\varepsilon)\ge c\varepsilon\).

The proof is symbolic. It does not rely on numerical sampling, finite enumeration, or an unverified limiting computation. The literature comparison does not eliminate the stated residual risk from inaccessible older full text.
