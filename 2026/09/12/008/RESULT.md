# Rank-two equal-imaginary-part beta=0 wall exclusion for the conic-ideal projection class on a very general ordinary Gushel–Mukai threefold

## Setup

Let X be a very general ordinary Gushel–Mukai threefold with H^3=10 and let C be a smooth conic. In the Kuznetsov decomposition using the tautological bundle E, the projected conic-ideal class is

`G = pr(I_C) = (-1,1,-3,-1/3)`.

At beta=0, `Im Z(G)=10`. The class is primitive, has Euler square -1 and classical discriminant 40.

## Corrected numerical result

Assume G lies in the beta=0 tilt heart; the required restriction-map surjectivity remains a separate open point. Integrality gives the usual imaginary-part gap: a positive-imaginary-part subobject cannot have imaginary part strictly between 0 and 10.

For a rank-two candidate subobject `F=(2,1,d_F,*)` with the same imaginary part 10, slope equality with G forces

`alpha^2 = (d_F+3)/15`.

Checking only F gives the six one-sided algebraic possibilities `d_F=-3,-2,-1,0,1,2`. However, a Jordan–Hölder wall also requires the complementary quotient

`Q=G-F=(-3,0,-3-d_F,*)`

to satisfy the classical Bogomolov necessary condition. Its discriminant is

`Delta(Q) = -60(d_F+3)`.

Thus `Delta(Q)>=0` requires `d_F<=-3`, while `alpha^2>=0` requires `d_F>=-3`. The only simultaneous case is the boundary `d_F=-3`, `alpha=0`. **There is therefore no positive-alpha rank-two equal-imaginary-part numerical wall surviving the two-factor classical-BG test.**

In particular the previously highlighted `E^vee` candidate (`d_F=1`, `alpha^2=4/15`) has quotient `Q=(-3,0,-4,*)` with `Delta(Q)=-240`, so it cannot be a tilt-semistable Jordan–Hölder quotient. The original six “BG-admissible” wall table and the claimed above-1/2 no-go were based on checking the discriminant of F but not Q and are withdrawn.

## What remains open

This repair does not prove full beta=0 wall-freeness. The placement of G in the tilt heart is still conditional on a restriction-map surjectivity statement, and imaginary-part-zero torsion/null subobjects and other numerical sectors require separate analysis. No Serre-invariant Bridgeland transfer is claimed here.

## Reproducibility

Run `python3 artifacts/wall_census.py`; the repaired script prints the one-sided candidates, both discriminants, confirms that no positive-alpha case has both discriminants nonnegative, and prints `CORRECTED_CENSUS_OK`.

## References

- S. Zhang, *Bridgeland moduli spaces for Gushel–Mukai threefolds*, arXiv:2012.12193.
- L. Pertusi, E. Robinett, *Stability conditions on Kuznetsov components of Gushel–Mukai threefolds and Serre functor*, arXiv:2112.04769 / Math. Nachr. 296 (2023).
