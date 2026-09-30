# Linearized localization obstructions for the hyperbolic–hyperbolic transverse Poisson structure in dimension four

## Setup

In coordinates x=(x0,x1,x2,x3), let C1=x0*x1 and C2=x2*x3 and let Pi be the associated rank-at-most-two Nambu Poisson bivector. Its nonzero components are `Pi02=-x0*x2`, `Pi03=x0*x3`, `Pi12=x1*x2`, `Pi13=-x1*x3`. Write

`d_ij := partial_{x_i} wedge partial_{x_j}`

for the constant bivectors. (The original record incorrectly wrote `dx_i wedge dx_j`, which is a 2-form.)

## Verified results

**A. Constant cocycles.** A constant bivector `nu=sum n_ij d_ij` satisfies `[Pi,nu]=0` exactly when `n02=n03=n12=n13=0`; hence the constant cocycle space is `span{d01,d23}`.

**B. Global rank jump.** `Pi_t=Pi+t d01` is Poisson for every t and, for t nonzero, has no zeros and rank exactly two everywhere. The (0,1) entry is t and the Pfaffian vanishes identically.

**C. Single-component cutoff obstruction.** No nonzero compactly supported C1 function phi makes `phi d01` a Poisson cocycle. Vanishing of the bracket forces invariance along the hyperbolic flow `(x0,x1)->(e^s x0,e^-s x1)`; any nonzero value off the fixed plane propagates along an unbounded orbit, contradicting compact support, and smoothness excludes support only on that plane.

**D. Radial ansatz obstruction.** For a C1 radial coefficient ansatz `nu^{ij}=f_ij(|x|^2)`, the cocycle equations force all admissible coefficients to be constant and the only spherewise directions are d01,d23. The exact certificate contains a 10x10 minor `-36 s^6`, nonzero for every s>0. Thus no radial transition localizes d01.

**E. Degree-at-most-two slice.** In the 90-dimensional space of bivectors with polynomial coefficients of degree at most two, the cocycle equations have rank 56 and kernel dimension 34. Coboundaries of affine vector fields have rank 16, leaving an 18-dimensional quotient in this finite slice; d01 is not in the affine coboundary image. Independently, every smooth coboundary `[Pi,X]` vanishes at the origin because Pi is quadratic, while d01 does not.

## Scope

These statements give explicit first-order obstructions for two natural localization ansätze and a finite polynomial cohomology slice. They **do not solve the general linearized compact-support localization problem**: a nonradial, multicomponent smooth cocycle is not ruled out. They also do not settle the nonlinear fixed-ball persistence/rank-change problem. This corrects the original prose that described the entire linearized localization problem as decided.

## Reproducibility

From the record directory run:

- `python3 artifacts/verify_target_routes.py`
- `python3 artifacts/verify_radial_exact.py`
- `python3 artifacts/verify_loopholes.py`
- `python3 artifacts/verify_cohomology.py`
- `python3 artifacts/verify_polydeg2.py`

The 2026-09-29 audit independently reconstructed the constant Schouten equations and the degree-at-most-two/affine linear systems, reproducing nullity 34, affine coboundary rank 16, and essentiality of d01.

## References

- J.-P. Dufour, N. T. Zung, *Poisson Structures and Their Normal Forms*.
- P. Monnier, computations of Nambu–Poisson cohomologies (adjacent, different complex).
- V. Guillemin, E. Miranda, A. Pires, work on b/log-symplectic Poisson geometry (adjacent setting).
