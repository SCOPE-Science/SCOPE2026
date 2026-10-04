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

For an independent set \(T\) of cube vertices, define
\[
K(T,\tau)
=
[-1,1]^n\cap
\bigcap_{t\in T}
\{x:\langle t,x\rangle\le n-\tau_t\},
\qquad 0<\tau_t<1.
\]

The analytic verification has four steps.

First, two truncating hyperplanes cannot meet in the cube. If \(t\ne s\) are selected, then their Hamming distance is at least two and
\[
\langle t+s,x\rangle\le2n-4
\]
for \(x\in[-1,1]^n\), whereas simultaneous equality in both cuts would force a value greater than \(2n-2\).

Second, every surviving cube vertex \(w\) keeps the full cube tangent cone, so its illuminating directions satisfy
\[
w_i d_i<0
\]
for every coordinate. Distinct surviving vertices therefore require distinct directions.

Third, a new cut vertex on the \(i\)-th edge from \(t\) has the untruncated neighbor obtained by flipping coordinate \(i\). The negative of that neighbor strictly decreases all active coordinate inequalities and the truncation inequality by
\[
-(n-2)<0.
\]
Thus all new vertices are illuminated by directions already assigned to surviving cube vertices.

Fourth, with \(\tau_{\max}\) the largest depth,
\[
\left(1-\frac{\tau_{\max}}n\right)[-1,1]^n
\subset K(T,\tau)\subset[-1,1]^n,
\]
which gives the stated Banach--Mazur estimate.

The embedded `verify.py` was replayed from its actual package path. It uses exact rational arithmetic, exhausts all subsets of a parity class in dimensions three and four, checks full parity-class constructions through dimension eight, and replays the local facet and sandwich inequalities.

The replay output was:

`VERIFY_OK independent cube-corner illumination spectrum`

Finite enumeration is not used as a proof of the all-dimensional theorem.
