# No extinction for the equivariantly deformed Ammann-Beenker named eightfold shell

## Context

Consider the Ammann-Beenker cut-and-project set with its regular octagonal
window and the deformation

Lambda_a = {x + a u psi(x*)},   u=(1,0),
psi(y)=sin(2 pi y_1) sin(2 pi y_2),   0<=a<=1/4.

For Fourier-module wavevector k, write

A_win(k;a) = integral_O exp(2 pi i (k*·y + a beta psi(y))) dy,
beta = k·u,

with intensity I(a)=|A_win(k;a)|^2/16 in the normalization used here.

The record studies the eight vectors with
4|k|^2=17-12 sqrt(2), |k|=1-sqrt(2)/2.  Because the Fourier module is dense,
"first observable" is only an observational/conventional label, not a claim
that these are the smallest nonzero Fourier-module wavevectors.

## Result

For every member of the named eight-vector shell and every a in [0,1/4],

Re A_win(k;a) <= -0.0075.

Consequently |A_win(k;a)|>=0.0075 and

I(a) >= 0.0075^2/16 = 3.515625e-6 > 0.

Thus no member of this named shell is extinguished by the stated deformation
on the parameter interval.

The eight members split, for u=(1,0), into two axial members with
beta=±0.085786..., two frozen members with beta=0, and four diagonal members
with beta=±0.060660....  At a=0 the window amplitude is approximately
-0.01181160 for all eight.

## Proof / evidence

`artifacts/proof_A_symbolic.py` verifies exactly that the four-dimensional
cut-and-project generator matrix has MM^T=2I, obtains the Fourier-module
quadratic form, and checks the eight listed vectors on the shell
4|k|^2=17-12sqrt(2).

`artifacts/certify_ring1.py` expands the window integral in powers of a through
order three, computes the trigonometric moments by exact polygon plane-wave
integrals enclosed with interval arithmetic, and controls the fourth-order
remainder.  Its ten-subinterval certificate gives

- axial members: sup Re A <= -0.011678,
- frozen members: Re A = -0.011812...,
- diagonal members: sup Re A <= -0.011604.

These are all strictly below -0.0075.

A sign defect in the archived version of the moment expansion has been
corrected.  The coefficient routine represented i sin rather than sin in each
coordinate; for psi^j this contributes an extra factor (-1)^j.  The corrected
moment coefficient therefore includes (-1)^j.  Even moments and every real-part
bound above are unchanged.  For a representative diagonal member the corrected
first moment is

M1 = -0.03743...,

not +0.03743....  The corresponding imaginary phase changes sign, while the
non-extinction theorem does not.

Pure-point diffraction stability under equivariant deformations is standard
background for deformed model sets (Baake-Lenz).  The claim here is the
quantitative non-vanishing certificate for this named shell.

## Limitations

- The interval certificate is for the fixed direction u=(1,0).
- The phrase "first observable shell" is not an intrinsic minimal-wavevector
  property; Pell-unit shells approach zero wavevector in this dense Fourier
  module.
- The interval engine is audited software evidence, not a separate
  machine-checked proof of its own implementation.
- The theorem is a shell-specific non-extinction statement, not a classification
  of all Bragg peaks under all equivariant deformations.

## Reproducibility

Run:

- `python3 artifacts/proof_A_symbolic.py`
- `python3 artifacts/certify_ring1.py`

The corrected `artifacts/certify_ring1.log` records the resulting bounds.

## References

- M. Baake, D. Lenz, *Deformation of Delone dynamical systems and pure point
  diffraction*, arXiv:math/0404155.
- B. Sing, T. R. Welberry, *Deformed model sets and distorted Penrose tilings*,
  Z. Kristallogr. 221 (2006), DOI 10.1524/zkri.2006.221.9.621.
- M. Baake, U. Grimm, *Diffraction of a model set with complex windows*,
  arXiv:1904.08285.
