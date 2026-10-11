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
The arbitrary-\(n\) proof is given in `RESULT.md`.

Critical checks:
- the zero-mean Lipschitz realization has facet inequalities \(x_i-x_j\le\rho(i,j)\);
- every corresponding normal is \(e_i-e_j\) and has Euclidean norm \(\sqrt2\);
- the published clock quasi-metric depends only on \(d=d(i,j)\) through
  \[
  \rho_d=d\frac{n^2-n+1}{n}-\frac{d(d+1)}2;
  \]
- \(\rho_{d+1}-\rho_d>0\) for every \(1\le d\le n-2\);
- summing the \(n\) shifted \(d=1\) facet inequalities proves the global inradius bound and equality forces the zero center;
- the polar vertices have norms \(\sqrt2/\rho_d\);
- the \(n\) outer \(d=1\) vertices sum to zero, so their average squared distance from any translated center is \(R^2+\|y\|^2\), proving the unique minimum-enclosing center;
- the two exact radii multiply to \(1\).

`verify.py` checks \(3\le n\le100\) using exact rational arithmetic for all quasi-metric shell values, their strict ordering and multiplicities, the nearest/farthest closed formulas, and the telescoping outer-vertex barycenter. Floating evaluation is used only to print representative Euclidean radii. Finite verification is corroborative only and does not assess originality.
