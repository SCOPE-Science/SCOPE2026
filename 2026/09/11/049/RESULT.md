# Minimal-section barrier for 15-field generation of the twisted vertical 2-jet tangent bundle over the universal P^4 hypersurface

## Context

Siu's differentiation strategy for hyperbolicity of generic high-degree
hypersurfaces imports spanning frames of slanted vector fields for the
tangent bundle of the vertical jet space of the universal hypersurface,
with a pole-order ledger. The admitted lane target claimed that fifteen
displayed slanted fields of bidegree pole order (<=7, <=d0+2) span the
twisted tangent bundle at a general point, with non-generation locus a
single-minor Sigma = {Delta = 0} of codimension >= 2.

## Definitions

Let X_d \subset P^4 x P^{N_d} be the universal degree-d hypersurface,
N_d = C(d+4,4) - 1, M(d) = C(d+4,4) (affine-cone monomial count).
Let J^v_2(X_d) be its vertical 2-jet space (jets tangent to the fibres
of the projection to P^{N_d}). Twisting by O(7, d0+2) does not change
fibre rank.

## Result (headline claim)

For the universal degree-d hypersurface in P^4, any set of global
twisted vector fields spanning T_{J^v_2(X)} (any twist) at one smooth
2-jet point has cardinality >= N_d + 9 = C(d+4,4) + 8 (cone form
M(d) + 9). In particular no 15-field frame spans the fibre at a general
(indeed at the exhibited smooth) point for any d >= 2: d = 2 needs
23 (projective) / 24 (cone) sections. The d = 1 count (13 <= 15) fits
but is the hyperplane family, outside Siu-program scope.

Sigma repair: on the smooth locus, a nonempty principal locus
Sigma = {Delta = 0} has pure codimension 1 (Krull's Hauptidealsatz).
A "one-minor Sigma of codim >= 2" is therefore empty, i.e. it asserts
everywhere-generation, already excluded by the section count for d >= 2.

Non-claim: the bare pole-order inequality c_3(2) <= 7 is NOT disproved;
only the "fifteen fields + one codim-two minor" formulation is.

## Proof / evidence

Dimension: dim X_d = N_d + 3 (3-dimensional hypersurface fibres over an
N_d-dimensional parameter space; affine cone dim M + 3). Vertical 2-jets
add two 3-dimensional jet fibres, so on the smooth locus
dim J^v_2 = N_d + 9 (cone: M + 9). Rank is twist-invariant. Any spanning
set at a point has cardinality at least the rank. For d >= 2,
N_d + 9 >= 14 + 9 = 23 > 15.

Realization at an explicit point (d = 2): coordinates
(z,a,z',z'') in C^4 x C^15 x C^4 x C^4 (27 total). Take F = z_1
(coefficient of z_1 is 1, all others 0), z = 0, z' = (0,1,0,0),
z'' = (0,0,1,0). The three defining equations F = 0, dF = 0, d^2F = 0
have gradients dz_1, dz'_1, dz''_1, three independent rows (exact rank 3
over Q), so the Zariski tangent space has dimension 27 - 3 = 24
= M(2) + 9; projectivizing parameters gives 23. Any 15-row evaluation
matrix has rank <= 15 < 23.

Sigma: Krull's Hauptidealsatz applied to the regular function Delta on
the smooth locus: a nonempty proper principal closed subset of a regular
locus is pure codimension 1.

## Limitations

- Applies to full-tangent spanning (T_{J^v_2}), the literal target. A
  relative-tangent (rank-9) reinterpretation is a different claim and is
  not established here.
- Does not bound c_3(2) itself; a generation proof with >= N_d + 9
  fields (or a non-principal / codim-1 Sigma) remains open and would
  need its own pole-ledger certificate.
- d = 1 counting fits but the family is hyperplanes: rational,
  non-general-type, vacuous for the Siu program.

## Reproducibility

```
python3 output/artifacts/verify_obstruction.py   # prints OBSTRUCTION_VERIFIED
```

Stdlib only (`fractions`, `math`); deterministic; runs in milliseconds.
Certifies the section-count table d = 1..8 and the explicit d = 2 smooth
point (exact Jacobian rank 3, nullity 24).

## References

- J. Merker, Low pole order frames on vertical jets of the universal
  hypersurface, Ann. Inst. Fourier 59(3) (2009), 1077-1104.
  https://doi.org/10.5802/aif.2458
- L. Darondeau, Slanted Vector Fields for Jet Spaces, arXiv:1404.0212v3.
  https://arxiv.org/html/1404.0212v3
- Y.-T. Siu, Hyperbolicity of generic high-degree hypersurfaces in
  complex projective space.
  https://dash.harvard.edu/bitstreams/7312037d-e440-6bd4-e053-0100007fdf3b/download
