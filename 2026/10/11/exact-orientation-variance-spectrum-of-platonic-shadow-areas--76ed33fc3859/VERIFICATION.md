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

Run `python3 verify.py` with a standard Python 3 interpreter; only the standard library is used.

The script constructs all facet-normal representatives as coordinates in \(\mathbb Q(\sqrt5)\), computes their complete ordered absolute dot-product distribution, and asserts the five exact multiplicity tables. It also identifies the tetrahedron's four normal directions and the octahedron's eight as two antipodal copies, providing a direct check of their known normalized brightness equality.

For \(t\in[0,1]\), the exact spherical kernel is
\[
\mathbb E|U\cdot v|\,|U\cdot w|=
\frac2{3\pi}(\sqrt{1-t^2}+t\arcsin t),
\qquad t=|v\cdot w|.
\]
The code evaluates the resulting finite sum using rational interval arithmetic: square-root enclosures from integer square roots, a Machin-series interval for \(\pi\), and monotone positive-coefficient inverse-sine series with an explicit geometric-tail upper bound. It proves positive variance, all strict comparisons, and the exact smallest \(1\%\)-RMS view counts using the inequalities
\[
k-1<10^4V(P)\le k.
\]
A separate fixed-seed numerical simulation with \(60{,}000\) independent uniform views compares empirical normalized means and variances with the certified values. That finite sample is diagnostic and is not a proof or a confidence guarantee.

The verification does not certify optimal performance for nonuniform or correlated viewing distributions and does not evaluate variance outside the five Platonic shapes.
