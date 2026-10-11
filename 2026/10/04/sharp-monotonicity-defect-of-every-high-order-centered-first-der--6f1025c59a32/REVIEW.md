# Independent mathematical audit

## correctness

PASS

Writing monotone data as nonnegative increments converts the derivative functional to cumulative coefficient tails. The positive-side weights alternate with strictly decreasing magnitude, so every even tail is negative and A_2 is strictly the most negative tail. The exact beta-integral/binomial identity gives sum_j alpha_{m,j}=H_{2m}-H_m, hence A_2=-V_m. The displayed difference formula proves strict growth and the harmonic asymptotic gives 1-log(2). Independent exact-rational replay through m=20 reproduced the tail minimum and constants; the package verifier extends analogous finite checks through m=40, while the proof itself is all-order.

## originality

PASS

The standard centered weights and their accuracy are classical, and sign preservation is a recognized design goal in nonlinear reconstruction, but no inspected source or Resultary record gives the exact optimization of the classical centered derivative over the bounded monotone cone, the harmonic-number defect formula, the exact two step extremizers, or its monotone all-order limit. The theorem is therefore best-of-knowledge original as an exact stability boundary rather than as a new stencil construction.

## value

PASS

This is a motivated sharp stability boundary for a ubiquitous numerical differentiation family: it identifies exactly when monotone samples can produce the wrong derivative sign, quantifies the worst possible defect at every order, and shows that higher formal order worsens this cone-stability defect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
