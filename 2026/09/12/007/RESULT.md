# Outermost numerical tilt wall for the branch-fixed Kuznetsov class on a general special Gushel–Mukai threefold

## Setup

Let X be a general special Gushel–Mukai threefold with Pic(X)=Z H and H^3=10. For a branch-fixed point x, let `E_x=pr(O_x)` and use the sign convention `v=-ch(E_x)=(5,-2,-2,5/3)`. At beta=-3/2, `D(v)=55`, `A(v)=97/4`, and the classical H-discriminant is 600.

## Corrected numerical census

For half-integral factor classes w with `0<D(w)<D(v)` and with the classical Bogomolov discriminant nonnegative for both w and v-w, exact enumeration gives 18 oriented admissible factor records. Pairing a factor with its complement gives 9 unordered decompositions, but these 9 decompositions collapse to **six distinct numerical wall loci**.

The unique outermost wall locus meets beta=-3/2 at `alpha^2=13/10`. It is not realized by a unique decomposition: two unordered decompositions attain the same locus,

- `(1,0,-7) + (4,-2,5)`, and
- `(2,-1,5/2) + (3,-1,-9/2)`.

All four orientations define the same semicircle

`alpha^2 + beta^2 + (33/10) beta + 7/5 = 0`,

with endpoints `beta=-14/5,-1/2`, center `-33/20`, radius `23/20`, and section `alpha^2=13/10` at beta=-3/2. Therefore no candidate numerical wall from this complete two-factor BG census crosses the ray beta=-3/2 above `alpha=sqrt(13/10)`.

## Independent verification

The 2026-09-29 audit independently re-enumerated the admissible factor classes using exact rational arithmetic, obtained 18 oriented records, grouped them into 9 unordered decompositions and six normalized wall equations, and found four oriented top records corresponding to the two decompositions above. This corrects the original phrases “9 walls” and “attained uniquely up to swap.”

## Limitations

The census is numerical: it bounds possible walls from the stated integrality and classical-BG necessary conditions; it does not assert that every locus is an actual wall. Picard rank one and the special-GM numerical inputs use generality. The standard double-tilt/Serre-invariant transfer is background rather than a new theorem here.

## Reproducibility

Run `python3 artifacts/ku_lattice.py` and `python3 artifacts/wall_enumeration.py`. The repaired wall script explicitly checks 18 oriented records, 9 unordered decompositions, six distinct wall loci, two top decompositions, and the outermost semicircle.

## References

- L. Pertusi, E. Robinett, *Stability conditions on Kuznetsov components of Gushel–Mukai threefolds and Serre functor*, Math. Nachr. 296 (2023).
- A. Perry, L. Pertusi, X. Zhao, *Stability conditions and moduli spaces for Kuznetsov components of Gushel–Mukai varieties*, Geom. Topol. 26 (2022).
- O. Debarre, A. Kuznetsov, *Gushel–Mukai varieties: moduli*.
