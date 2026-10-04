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
The theorem is verified symbolically; no external computation is required.

The proof has four checkable steps.

First, a \(k\)-layered integer satisfies
\[
\frac{\sigma(n)}n\ge k.
\]

Second, Grönwall's maximal-order theorem implies that for every \(\varepsilon>0\), all sufficiently large \(n\) satisfy
\[
\frac{\sigma(n)}n\le(e^\gamma+\varepsilon)\log\log n.
\]

Third, the least existing \(k\)-layered values tend to infinity along any unbounded set of admissible \(k\), so the two inequalities apply simultaneously for all sufficiently large admissible \(k\).

Fourth, division by \(k\), a lower-limit passage, letting \(\varepsilon\downarrow0\), and two monotone exponentiations give exactly
\[
\liminf\frac{\log\log L_k}{k}\ge e^{-\gamma}
\]
and the stated double-exponential form.

The proof does not assume or infer that \(k\)-layered numbers exist for every \(k\). That remains outside the claim.
