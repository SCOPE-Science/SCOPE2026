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

The recent primary source was checked at its definition of spanning-surface complexity, its fixed-crossing ensemble, and Theorem 1.4. These establish that for the mirror-distinguishing set \(\mathcal K_c\),
\[
\overline\Gamma(c)=rac{c}{3}+rac{1}{9}+o(1).
\]
Its Definition 1.1 also gives the key interpretation: for a knot, an orientable genus-\(g\) spanning surface has first Betti number \(2g\), while \(\Gamma\) minimizes first Betti number without the orientability restriction.

Suzuki--Tran's exact average-genus theorem was checked with its convention discussion. On the same mirror-distinguishing ensemble,
\[
\overline g(c)=rac{c}{4}+rac{1}{12}+o(1).
\]
Therefore
\[
2\overline g(c)-\overline\Gamma(c)=rac{c}{6}+rac{1}{18}+o(1).
\]

For the density step, define \(X_c=(2g-\Gamma)/c\). The standard genus bound gives \(0\le X_c<1\). If \(p_c(\delta)=P(X_c\ge\delta)\), then
\[
E[X_c]\le\delta(1-p_c(\delta))+p_c(\delta).
\]
Since \(E[X_c]	o1/6\), the claimed liminf follows. At \(\delta=1/12\), the lower bound is \(1/11\).

The bundled arithmetic regression prints:

`VERIFY_OK mean_gap=c/6+1/18+o(1) threshold=c/12 density_lower_bound=1/11`

The regression checks arithmetic only; the topological inputs are the cited source theorems.

The independent-audit channel has not been performed.
