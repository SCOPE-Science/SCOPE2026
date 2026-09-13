# Binary-cubic discriminant conormal excess at the triple-root orbit

## Context

Let `V = Sym^3(C^2) ≅ A^4` be binary cubics `a x^3 + b x^2 y + c x y^2 + d y^3`,
`G = SL_2(C)` acting by change of variables, `Y = [V/G]`, and
`X = T^*[0] Y = [T^*V/G]` with the PTVV 0-shifted symplectic form.
Let `Δ = b^2 c^2 − 4 a c^3 − 4 b^3 d − 27 a^2 d^2 + 18 a b c d` be the
binary-cubic discriminant, `D = {Δ = 0}/G` the discriminant substack, and
`O_3 = G·x^3` the closed triple-root orbit at `p = x^3 = (1,0,0,0)`.
Put `L_0 = Y` (zero-section) and `L_1 = N^*[0](D/Y)` the Calaque shifted
conormal of the derived discriminant, `W = L_0 ×_X L_1`.
This is the first non-trivial case of the admitted target on Lagrangian
certificates plus stabilizer-corrected excess intersection integers for
binary d-ics with singular discriminant stabilizer jump.

## Definitions

- `D_der = Spec_Y(Kos(Δ))`, `Kos(Δ) = (O_Y[ε], |ε| = −1, dε = Δ)`:
  derived zero locus of the `G`-invariant section `Δ` of the trivial line
  bundle; quasi-smooth (lci) of virtual codimension 1.
- `L_0`: PTVV zero-section Lagrangian in `T^*[0]Y`.
- `L_1 = N^*[0](D_der/Y)`: Calaque shifted conormal, canonical Lagrangian.
- `W ≃ Crit(Δ)/G`: homotopy fiber product of the two Lagrangians.
- Transverse slice at `p`: `{a = 1, b = 0}`, `S = Spec C[c,d]`,
  `f(c,d) = Δ|_slice = −4 c^3 − 27 d^2` (ordinary cusp, A2 type).
- Transverse excess cdga: `A^• = C[c,d,u,v]`, `|u| = |v| = −1`,
  `du = f_c = −12 c^2`, `dv = f_d = −54 d`, with residual `μ_3` weights
  `wt(c) = 2`, `wt(d) = 0 mod 3`.
- `w = length H^0(O_W)` at `O_3`; `ν: D̃ → D` normalization.

## Result

Both `L_0` and `L_1` carry `G`-equivariant Lagrangian structures, and at `O_3`:

1. **Stabilizer-corrected tangent.** Transverse tangent complex
   `T_W|_0 ≃ [T_0 S → T_0^* S] = [C^2 → C^2 via diag(0,−54)]` in degrees
   `0,1`; Tor-amplitude `[0,1]` with `h^0 = 1 = span(∂_c)`,
   `h^1 = 1`. Full stacky complex `[g → V → V^*]` in degrees `−1,0,1`
   adds `H^{−1} ≅ Lie(Stab(p)) ≅ C` of dimension 1.
2. **Excess virtual dimension.** `dim L_0 = dim L_1 = 1`, `dim X = 2`,
   so expected and virtual dimension `0`; classical truncation has
   dimension 0 with Zariski tangent `h^0 = 1`; excess rank
   `e = h^0 − vdim = 1 = h^1_transverse`.
3. **Finite length.** `w = length H^0(O_W)_{O_3} = 2`, basis `{1, c}`,
   from `C[c,d]/(−12 c^2, −54 d) ≅ C[c]/(c^2)`.
4. **Push-pull / PTVV reduction identity.**
   `w = 2 = length O_{ν^{−1}(O_3)} = 2δ − r + 1` with `δ = 1, r = 1`;
   `ν(t) = (−3 t^2, 2 t^3)` has scheme fiber `C[t]/(t^2)` of length 2,
   matching the derived excess length.

## Proof / evidence

- `∇Δ(p) = 0` by direct differentiation; Hessian at `p` is
  `diag(0,0,0,−54)`, rank 1, eigenvalues `0 (×3), −54`; independently
  reproduced in sympy.
- `sl_2` vector fields annihilate `Δ` (Lie derivatives zero); at `p` the
  infinitesimal action has rank 2 with 1-dimensional kernel, so
  `dim G·p = 2`, `dim Lie(Stab) = 1`; solving `g·x^3 = x^3` gives Borel
  with `α^3 = 1`, i.e. `Stab^∘ ≅ G_a`, `π_0 ≅ μ_3`; orbit tangent is
  `span(∂_a, ∂_b)`, so `{a=1,b=0}` is transverse.
- On the slice `f = −4c^3 − 27d^2`, `Hess_f(0) = diag(0,−54)`,
  kernel `span(∂_c)`, 1-dimensional cokernel; the only nonzero Hessian
  entry of `Δ` is `dd` while `im(α) = span(∂_a,∂_b)`, giving the
  stabilizer-corrected splitting.
- Buchberger on `(f_c, f_d) = (−12c^2, −54d)` yields Gröbner basis
  `{c^2, d}`; quotient is free of rank 2 with basis `{1,c}`.
  Euler relation `2 c f_c + 3 d f_d = 6 f` gives `(f) ⊂ (f_c,f_d)`.
- `f(−3t^2, 2t^3) ≡ 0`; normalization is bijective on points with
  `δ = 1`; fiber ring has basis `{1,t}`, length 2.
- `L_0` certificate: Liouville form vanishes on zero-section,
  `T_Y → T_Y ⊕ L_Y → L_Y` is the standard fiber sequence (PTVV Thm 2.5).
- `L_1` certificate: `D_der` is lci, so Calaque's shifted-conormal theorem
  applies verbatim; `dε = Δ` is equivariant since `Δ` is invariant.
- All equalities recorded in `output/artifacts/computation.json`
  (gradient, Hessian, α-rank, slice, Gröbner basis, Milnor basis,
  parametrization check, fiber length).

## Limitations

- The `L_1` certificate uses Calaque's theorem for the derived (lci)
  discriminant rather than a direct normal-bundle computation on the
  singular classical truncation.
- Symmetry analysis is at `p = (1,0,0,0)` with residual `μ_3` weights;
  global statements about `W` away from `O_3` rely on the standard
  `Crit(Δ)/G` identification, verified transversely at `O_3`.
- Theorem 4 (push-pull) is the proved numerical identity
  `w = length fiber = 2δ − r + 1`, i.e. the PTVV reduction weight at `O_3`,
  not a new general PTVV pushforward theorem.

## Reproducibility

Differentiate `Δ` and evaluate at `(1,0,0,0)`; compute the Hessian and its
rank; compute the `sl_2` action vector fields and their rank; substitute
`a = 1, b = 0` to get `f`; run Buchberger on `(−12c^2, −54d)`; verify
`f(−3t^2,2t^3) = 0` and the fiber length. Any computer algebra system
(e.g. sympy `hessian`, `groebner`) reproduces `computation.json`.

## References

- Pantev–Toën–Vaquié–Vezzosi, Shifted Symplectic Structures,
  arXiv:1111.3209 (PTVV zero-section, Lagrangian intersections).
- Calaque, Shifted cotangent stacks are shifted symplectic,
  arXiv:1612.08101; Ann. Fac. Sci. Toulouse 28 (2019), 67–90
  (shifted conormal Lagrangian).
- Classical binary-cubic discriminant
  `Δ = b^2c^2 − 4ac^3 − 4b^3d − 27a^2d^2 + 18abcd` and A2 cusp
  Milnor/Tjurina theory for comparison of the bare number 2.
