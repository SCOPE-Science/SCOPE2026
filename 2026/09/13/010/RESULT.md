# Milnor–Tjurina gap and Hochschild-vs-Behrend identity for a Newton-nondegenerate non-quasi-homogeneous dCrit surface germ

## Context

Let `U = A^3_C` with coordinates `x, y, z` and

```
f = x^5 + y^6 + z^7 + x^3 y^2 z,   X = dCrit(f).
```

The admitted target asks for the Lagrangian-intersection presentation and
isolated singularity of this derived critical locus, and with proof: the
Milnor number via the Kouchnirenko Newton-volume formula (not a
weighted-homogeneous table), the Tjurina number and the gap `mu - tau`,
the Hessian rank at `0`, the virtual dimension, and the
Hochschild-vs-vanishing-cycle (Behrend-weighted Euler) identity. The scope
is Newton-nondegenerate non-quasi-homogeneous surface singularities, as
illustrated by this germ. This germ is a minimal Fermat-plus-interior
model: principal part `x^5 + y^6 + z^7` with one interior exponent
`D = (3,2,1)` above the Newton face.

## Definitions

- `Jac(f) = (f_x, f_y, f_z)` with
  `f_x = 5x^4 + 3x^2y^2z`, `f_y = 6y^5 + 2x^3yz`, `f_z = 7z^6 + x^3y^2`.
- Local Milnor number `mu(0) = dim_C O_{C^3,0}/Jac(f)`;
  local Tjurina number `tau(0) = dim_C O_{C^3,0}/(f, Jac(f))`.
- Newton polyhedron `Gamma_+`, Newton number `nu`, Kouchnirenko formula:
  for convenient Newton-nondegenerate `f`, `mu(0) = nu`.
- `X = dCrit(f) = graph(df) x_{T^*[0]U} U`, the PTVV `(-1)`-shifted
  symplectic Lagrangian intersection of the zero section and `graph(df)`
  in the 0-shifted cotangent `T^*[0]U`.
- Darboux cdga `B = (C[x,y,z][xi_1,xi_2,xi_3], d)` with `|xi_i| = -1` and
  `d xi_i = partial_i f`; `pi_0(B) = C[x,y,z]/Jac(f)`.
- Milnor fibre `F` of the isolated hypersurface singularity at `0`;
  for `n = 3`, `chi(F) = 1 + mu(0)`.
- Behrend-weighted Euler number at `0`: `(-1)^{dim U}(1 - chi(F))`.

## Result

For `f = x^5 + y^6 + z^7 + x^3 y^2 z` on `U = A^3_C` and `X = dCrit(f)`:

1. `X = L_0 x_{T^*[0]U} L_1` with `L_0` the zero section and
   `L_1 = graph(df)` carries the canonical PTVV `(-1)`-shifted symplectic
   structure with Darboux model `B` above.
2. `0` is an isolated critical point. The total affine Jacobian colength
   is `136 = 120 + 16`; there are exactly 16 distinct nonzero critical
   points, each Morse (`mu = 1`).
3. Local Milnor number `mu(0) = 120`, proved both by Kouchnirenko Newton
   volume (`nu = 210 - 107 + 18 - 1 = 120`) and by a weighted local
   standard-basis certificate with monomial box
   `{x^a y^b z^c : a <= 3, b <= 4, c <= 5}`.
4. `f` is Newton-convenient, Newton-nondegenerate, and not
   quasi-homogeneous (no nonzero weights satisfy the system; equivalently
   `f not in Jac(f)`), hence of positive modality in the concrete
   non-quasi-homogeneous sense.
5. Local Tjurina number `tau(0) = 101`, with Tjurina locus `{0}`; hence
   `mu - tau = 120 - 101 = 19 > 0`.
6. `Hess(f)(0)` is the `3 x 3` zero matrix (order of `f` is 5), so Hessian
   rank `0`; `vdim dCrit(f) = 3 - 3 = 0`.
7. `chi(F) = 1 + 120 = 121`; total Hochschild-homology dimension `120`
   equals the Behrend number `(-1)^3(1 - 121) = 120`.

Proved integers: `mu = 120`, `tau = 101`, `mu - tau = 19`,
Hessian rank `0`, `vdim 0`, `chi(F) = 121`, HH total = Behrend number `120`.

## Proof / evidence

**Darboux model.** Standard PTVV construction: the derived intersection of
the two Lagrangians `L_0, L_1` in `T^*[0]U` has cdga
`O_U[shifted cotangent fibres]` with differential given by `df`, i.e. the
stated `B` with `d xi_i = partial_i f`. Its `pi_0` is the Jacobian algebra.

**Newton data and nondegeneracy.** The Newton boundary is the single compact
face `ABC` through `(5,0,0)`, `(0,6,0)`, `(0,0,7)` with equation
`x/5 + y/6 + z/7 = 1`. The extra exponent `D = (3,2,1)` has face-weight
`(126 + 70 + 30)/210 = 226/210 = 113/105 > 1`, hence lies strictly above
the face (interior to `Gamma_+`); the principal part is the Fermat
`x^5 + y^6 + z^7`. Face nondegeneracy: the Fermat face has partials
`5x^4, 6y^5, 7z^6` with no `(C*)^3` common zero. Edges are binomial and
vertices monomial, all nondegenerate. Thus `f` is convenient and
Newton-nondegenerate, so Kouchnirenko applies. With tetrahedron volume
`V = 5*6*7/6 = 35` and coordinate-face areas `15, 35/2, 21`,

```
nu = 6V - 2(A_xy + A_xz + A_yz) + (5 + 6 + 7) - 1
   = 210 - 107 + 18 - 1 = 120.
```

Non-quasi-homogeneity: `5w_1 = 6w_2 = 7w_3 = 3w_1 + 2w_2 + w_3` forces
`210s = 226s`, impossible for `s != 0`; only the trivial weight solution
exists.

**Local Milnor certificate.** Negative weighted order with weights
`(1/5, 1/6, 1/7)` cleared to `W = (42, 35, 30)`; leading terms
`5x^4, 6y^5, 7z^6`. All three S-polynomials `S(fx,fy)`, `S(fx,fz)`,
`S(fy,fz)` reduce to `0` in 2 steps each over `QQ` (divisions only by
5, 6, 7), verified by an exact from-scratch script. Hence
`{fx, fy, fz}` is a standard basis; standard monomials are the box
`a <= 3, b <= 4, c <= 5`, of count `4*5*6 = 120`. So `mu(0) = 120`,
agreeing with `nu`.

**Global Jacobian and critical locus.** Exact `QQ` Groebner computations
(sympy grevlex and lex) give Jacobian colength `136`; independent
modular from-scratch Buchberger count agrees (`136`). Lex elimination
yields the univariate `81z^20 + 13671875z^12 = z^12(81z^8 + 13671875)`,
so `z = 0` or `z^8 = -13671875/81` (8 distinct nonzero values). For
`z != 0`: `y != 0` (else `f_z != 0`), `x != 0` (else `f_y` forces
`y = 0`), `x^2 = -(3/5)y^2 z`, `x^3 = -3y^4/z`, hence uniquely
`x = 5y^2/z^2` and `y^2 = -(3/125)z^5` (2 values of `y` per `z`). This
gives exactly `8 * 2 = 16` distinct nonzero critical points. Since
`136 = 120 + 16`, each nonzero critical point has Milnor number 1
(Morse). In particular `0` is isolated.

**Tjurina number and gap.** Modulo `Jac(f)`:
`x^5 -> -(3/5)x^3y^2z`, `y^6 -> -(1/3)x^3y^2z`, `z^7 -> -(1/7)x^3y^2z`,
so `f = (1 - 113/105)x^3y^2z = -(8/105)x^3y^2z != 0` (the monomial
`x^3y^2z` is a standard-basis monomial); `f not in Jac(f)`, confirming
non-quasi-homogeneity via Saito. Exact Groebner computations of
`(f, fx, fy, fz)` give colength `101` in both lex (13 polynomials) and
grlex (10 polynomials). At each nonzero critical point,
`x^5 = (9/5)y^6`, `z^7 = (3/7)y^6`, `x^3y^2z = -3y^6`, so
`f(p) = (8/35)y^6 = (8/15)z^7 != 0`; the Tjurina locus is `{0}`. Hence
local `tau(0) = 101` and `mu - tau = 19 > 0`. Cross-check: known bound
`mu/tau <= 3` holds (`120/101 < 3`).

**Point invariants and weight identity.** `ord_0(f) = 5` so
`Hess(f)(0) = 0`, rank `0`. `vdim dCrit = 3 - 3 = 0`. For `n = 3`,
`chi(F) = 1 + (-1)^3(mu - 1)... ` in the standard normalization used here
`chi(F) = 1 + mu = 121`. The Koszul complex of the regular sequence
`(fx, fy, fz)` on the 120-dimensional Milnor algebra gives total
Hochschild-homology dimension `120`, while
`(-1)^3(1 - 121) = 120`. Hence `120 = 120`.

## Limitations

- Groebner certificates depend on exact rational/modular Buchberger runs
  reproduced by the artifact scripts.
- Newton nondegeneracy is verified face-by-face for this germ, not as a
  general classification.
- The Hochschild-vs-Behrend identity is proved at total-dimension/Euler-number
  level, not as a refined Hodge or categorical equivalence.
- Positive modality is used in the concrete non-quasi-homogeneous sense
  (no positive weights), not via full Arnold unimodal/bimodal identification.

## Reproducibility

- `local_buchberger_qq.py` (stdlib only): weighted local standard basis,
  S-polynomial reductions, box count `120`.
- `global_jac.py` (sympy): Jacobian Groebner in grlex and lex; staircase
  count `136`; lex univariate `81z^20 + 13671875z^12`.
- `global_tjurina.py` (sympy): Tjurina ideal Groebner in grlex and lex;
  staircase count `101` in both orders.

## References

- A. G. Kouchnirenko, Polyedres de Newton et nombres de Milnor,
  Invent. Math. 32 (1976).
- K. Saito, Quasihomogeneous isolated singularities (criterion
  `f in Jac(f)` iff quasi-homogeneous).
- Y. Liu, Milnor and Tjurina numbers for a hypersurface germ with isolated
  singularity, C. R. Math. 356 (2018) (bound `mu/tau <= n`).
- M. Anel, D. Calaque, Shifted symplectic reduction of derived critical
  loci (PTVV Lagrangian-intersection background).
- Behrend constructible-function / Donaldson–Thomas critical-locus
  background: value `(-1)^{dim U}(1 - chi(F))`.
- Singular Manual A.4.1, Milnor and Tjurina number (localization and
  `vdim` methodology reference).
