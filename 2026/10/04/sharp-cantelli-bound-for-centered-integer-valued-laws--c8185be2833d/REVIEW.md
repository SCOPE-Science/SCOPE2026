# Review

## Correctness

PASS. The proof constructs a quadratic that majorizes the upper-tail indicator
on the entire integer lattice. Its two lower roots are consecutive integers,
which makes nonnegativity exact on all lattice points. Taking expectations uses
only the prescribed first two moments. The proposed three-point law has
nonnegative masses because \(j=\lfloor v/k\rfloor\), and direct moment
identities show that it attains the bound. Equality in the pointwise majorant
also gives the complete extremizer support and uniqueness. The exact gap from
Cantelli is an algebraic identity. Exact-rational replay covered 29040 moment/threshold cases.

## Originality

PASS, with an explicit historical-literature risk. The 2016 generalized-moment
source was inspected for its moment-duality framework, a 2002 survey-style
probability-inequality source was compared at abstract level, the 2019
exchangeable Cantelli-type paper was inspected through its definitions and main
theorem, and the closest published finite-sample exchangeable studentized
Cantelli result was read in full. None states or implies the centered
integer-support formula, its consecutive-root certificate, or its exact
three-point equality law.

Targeted searches using integer-valued, lattice-valued, discrete,
one-sided Chebyshev/Cantelli, consecutive integer roots, and the symbolic form
of the proposed denominator found no equivalent statement. This is evidence
against direct coverage, not a proof that no older equivalent exists.

## Value

PASS. Cantelli's inequality is a basic one-sided moment bound, while integer
support is a common structural restriction in count and lattice probability.
The theorem gives the exact cost of ignoring that structure, identifies the
sharp extremizer for every variance and threshold, and reduces the refinement
to a reusable consecutive-root polynomial certificate. The exact gap formula
also shows precisely when the classical continuous-support bound remains sharp.

Same-model review: passed. Independent audit: not yet performed.
