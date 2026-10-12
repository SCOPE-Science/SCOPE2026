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
The finite-size input is Theorem 2 of arXiv:2609.15059v1. The definitions used are
\[
r=\left\lfloor\frac{d_{\mathrm F}-3}{q-2}\right\rfloor,
\qquad
s=q\max\{g-r,0\},
\]
and
\[
t=\left\lfloor\frac{d_{\mathrm F}-(q-2)\min\{g,r\}-1}{2}\right\rfloor,
\]
with \(t\ge1\), together with the source fidelity bound
\[
F\le\left[1-H_2^{-1}\!\left(\frac{\max\{0,k-s\}}{\max\{n-s,n-k\}}\right)\right]^t.
\]

For gate density strictly below \(\Delta/(q-2)\), the inequality eventually has \(s=0\) and an exponent linear in \(n\); this gives the stated negative logarithmic fidelity rate. For gate density strictly above \(\Delta/(q-2)\) but below \(\Delta/(q-2)+R/q\), the core density tends to \(\sigma<R\) while \(t\ge1\); this gives the constant fidelity gap.

For the convergence-free threshold statement, a fixed deficit \(\eta\) below \(\Delta/(q-2)+R/q\) implies that the binary-entropy argument is eventually at least \(R/2\) in the branch \(g<r\), and at least \(q\eta/4\) in the branch \(g\ge r\). Therefore fidelity cannot tend to one. The contradiction-subsequence argument then gives the liminf gate-density bound.

No numerical calculation, finite enumeration, or unproved extrapolation is needed for the theorem. The proof does not establish achievability at the threshold and leaves both boundary-density cases outside the two explicit phase formulas.
