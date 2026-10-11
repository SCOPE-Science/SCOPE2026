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

The primary-source transfer operator is
\[
(K_sg)(x)
=
\sum_{a\ge1}4^{-a}(a+x)^{2s}
g\!\left(\frac1{a+x}\right).
\]
For
\[
s=847/1000
\]
and
\[
g(x)=1+(127/120)x,
\]
the included program evaluates the first twelve branches using outward interval arithmetic on an exhaustive partition of \([0,1]\) into \(2000\) cells.

The replay reports:

- interval-arithmetic library version: `1.3.0`;
- transfer branches: `12`;
- interval cells: `2000`;
- required excess floor: `1/25000`;
- smallest outward lower endpoint: `0.000051512874937209574`;
- worst cell index: `1005`;
- result: `PASS`.

Thus every cell satisfies
\[
K^{(12)}_{847/1000}g-g>1/25000.
\]
Because every omitted transfer branch is positive, the infinite operator satisfies the same inequality. Since
\[
g\le247/120,
\]
this yields
\[
K_{847/1000}g
\ge
\left(1+\frac3{154375}\right)g.
\]
Iteration proves that the spectral radius is strictly larger than one. The source's strict pressure monotonicity therefore gives
\[
D_2<847/1000.
\]

The interval computation is exhaustive over a finite cover of the continuum and encloses each elementary expression outward. It is used only to certify the displayed uniform inequality; positivity and the source theorems supply the infinite-operator and Fourier consequences.
