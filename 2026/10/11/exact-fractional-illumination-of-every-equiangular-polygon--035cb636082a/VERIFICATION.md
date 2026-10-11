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

For an equiangular \(n\)-gon, write
\[
\delta=\frac{2\pi}{n},
\qquad
\alpha=\pi-\frac{2\pi}{n},
\qquad
r=\left\lfloor\frac{n-1}{2}\right\rfloor.
\]
The \(n\) vertex illumination sets are open arcs of length \(\alpha\) whose centers are \(\delta\)-spaced.

The exact lower certificate is
\[
\sum_{j=0}^{n-1}\mu(I_j)
\le
r\,\mu(S^1),
\]
because no direction belongs to more than \(r\) vertex arcs.

The exact upper certificate is the cyclic family of \(n\) blocks
\[
B_j=\{j,j+1,\ldots,j+r-1\}.
\]
Since
\[
(r-1)\delta<\alpha,
\]
each block has a nonempty common illumination direction. Weighting one such direction per block by \(1/r\) gives every vertex weight exactly \(1\).

`verify.py` checks the exact integer spacing and cyclic-incidence certificates for all \(3\le n\le500\). It separately sweeps every angular combinatorial cell geometrically for \(3\le n\le60\).

The finite sweep is diagnostic only. The universal proof is the exact spacing and double-counting argument in `RESULT.md`.
