# Density-3/2 Y-rigidity for 2D bounded-mean-curvature varifolds in R^4

## Context
Branch-point regularity for area-minimizing and bounded-mean-curvature
varifolds in higher codimension (Almgren, Chang, De Lellis–Spolaor) is a
recognized benchmark. Density 3/2 is the first level where triple-junction
branching can appear: below it only multiplicity-one planes occur, while at
density 2 non-Y cones (e.g. two transverse planes) already exist. Fixing the
flat-versus-branched alternative at density 3/2 in codimension 2 decides the
lowest branched tangent-cone list for the drift-perturbed class.

## Definitions
- `V`: 2-dimensional integral varifold in `B_1(0) ⊂ R^4` with bounded
  generalized mean curvature `|H| ≤ Λ`.
- `Θ^2(V,0) = lim_{r↓0} ‖V‖(B_r)/(π r^2)`: 2-density at 0 (exists by drift
  monotonicity).
- Tangent cone: any subsequential blow-up limit `C = lim_{j} (η_{0,r_j})_# V`,
  `η_{0,r}(y)=y/r`, stationary integral 2-varifold cone.
- Standard `Y`: three half-planes meeting along a line at 120° dihedral
  angles; density 3/2.

## Result (headline claim)
Let `V` be a 2-dimensional integral varifold in `B_1(0) ⊂ R^4` with
`|H| ≤ Λ`. If `Θ^2(V,0) = 3/2`, then **every** tangent cone to `V` at 0 is,
up to an orthogonal rotation of `R^4`, the static triple half-plane `Y`
cone. In particular there is no stationary integral 2-cone in `R^4` of
density 3/2 outside the `O(4)`-orbit of `Y`. The argument works in `R^n`
for every `n ≥ 3`.

## Proof / evidence
Classical tools cited, not reproved: drift monotonicity (Allard 1972; Simon
Ch. 17), blow-ups kill drift (`H_r(x)=rH(rx)→0`) plus Allard compactness
giving stationary integral cones of the same density, Allard–Almgren
stationary 1-cone balancing `Σ m_i u_i = 0` with density `(Σ m_i)/2`,
monotonicity equality ⇒ conical (Simon Ch. 19), tangent cones of cones are
cylinders, Allard regularity (multiplicity-one plane ⇒ smooth disk).

New assembly:
1. **Sandwich.** For stationary integral 2-cone `C` with `Θ(C,0)=3/2`,
   `Θ(C,x) ≤ Θ(C,0)` for all `x≠0` via `B_R(x) ⊂ B_{R+|x|}(0)` and exact
   cone mass, `(R+|x|)^2/R^2→1`.
2. **Ladder.** At `x≠0`, any tangent cone splits `L×C''` (`L=span{x}`,
   `C''` stationary integral 1-cone), so `Θ(C,x)=k/2`, `k=Σm_i≥2`;
   sandwich gives `k≤3`, hence `{1,3/2}`. `k=2` forces opposite unit rays
   (multiplicity-one plane, smooth by Allard); `k=3` excludes `(2,1)`
   (`|u_2|=2`) and forces three distinct unit rays summing to zero, i.e.
   planar 120° triple (pairwise dots `−1/2`, Gram `3/2 I − 1/2 11^T`).
3. **Link length.** `‖C‖(B_r)=r^2·H^1(Γ)/2`, `Γ=C∩S^{n-1}`, so
   `Θ(C,0)=H^1(Γ)/(2π)`; here `H^1(Γ)=3π`.
4. **Equality ⇒ Y.** If `Θ(C,x)=Θ(C,0)=3/2` for some `x≠0`, the mass ratio
   at `x` is identically `3/2` (nondecreasing, `3/2` at 0, `limsup≤3/2` at
   ∞), so `C` is conical at `x` and at 0; the two dilations compose to
   translations along `x`, `C=L×C''` with `Θ^1(C'',0)=3/2`, hence `C=O·Y`.
5. **No all-regular cone.** If every `x≠0` were regular, `Γ` would be a
   compact smooth 1-manifold of closed geodesics of `S^{n-1}` (cone-minimal
   iff link-minimal), each component length `2πk`; total `3π∉2πN`
   (one component `3π≠2πk`, ≥2 give `≥4π`). Contradiction.

Hence any tangent cone `C` has some `x≠0` of density `3/2` and equals `O·Y`.

Elementary identities (Y density, 120° balance iff, `3π/2π=3/2∉Z`,
sandwich limits) machine-checked: `output/artifacts/verify_identities.py`
9/9 PASS, ALL_VERIFY_OK.

## Limitations
- Uniqueness of the tangent cone (common rotation across sequences) is NOT
  proved — only that each tangent cone lies in the `O(4)`-orbit of `Y`.
- No epiperimetric decay rate and no regularity of `V` beyond the cone list.
- Classical GMT inputs (P1–P6) quoted, not reproved.
- Stated case `R^4`; proof valid in any `R^n`, `n≥3`.

## Reproducibility
- Read `inputs/DRAFT.md` Lemmas 1–5 and verify cited GMT facts in
  Allard 1972 / Simon Lectures Chs. 17, 19 / Allard–Almgren 1-cones.
- Run `python3 output/artifacts/verify_identities.py` (stdlib only).

## References
- Allard, Ann. of Math. 1972 (interior regularity, compactness,
  monotonicity); Simon, Lectures on GMT, Chs. 17, 19.
- Allard–Almgren stationary 1-cone balancing.
- Taylor, Ann. of Math. 1976 (2D minimizing cones in R^3).
- White, arXiv:1912.00257 (stationary polyhedral varifolds minimize in a
  group sense).
- Colombo–Edelen–Spolaor, arXiv:1709.09957 (minimal varifolds near
  polyhedral cones, no-hole condition).
- De Lellis–Spadaro–Spolaor, doi:10.1002/cpa.21690 (uniqueness for
  almost-minimizing 2D currents).
- Minter, arXiv:2108.02614 (stable codim-one density-5/2).
- Stuvard–Tonegawa, arXiv:2510.02969 (forced-Brakke triple-junction
  epsilon-regularity, conditional/parabolic).
