# The printed rice-blast finite-difference scheme converges to the wrong memory operator

## Finding

The rice-blast HLIR model defines its spore-production memory term as
\[
f(x,t)
=
\kappa\int_0^t
I(x,t-s)H(x,t-s)\alpha(s)\beta(s)\,ds.
\]
Let
\[
g(t)=I(x,t)H(x,t).
\]
The printed finite-difference formula instead uses
\[
f_{\Delta,i}^{\,j}
=
\kappa\Delta t\,
g_i(t_j)
\sum_{\ell=1}^{j}
\alpha(t_\ell)\beta(t_j-t_\ell).
\]

This is not a Riemann-sum approximation to the displayed continuous convolution. For fixed
\[
t_j=t,
\]
its continuum limit is
\[
\widetilde f(x,t)
=
\kappa g(t)\int_0^t
\alpha(s)\beta(t-s)\,ds,
\]
whereas the model requires
\[
f(x,t)
=
\kappa\int_0^t
g(t-s)\alpha(s)\beta(s)\,ds.
\]

The two operators are genuinely different. If
\[
\alpha\equiv1
\]
and
\[
g(t)=t,
\]
then a change of variable in the printed limit gives
\[
\widetilde f(t)
=
\kappa t\int_0^t\beta(s)\,ds,
\]
while
\[
f(t)
=
\kappa\int_0^t(t-s)\beta(s)\,ds.
\]
Hence
\[
\widetilde f(t)-f(t)
=
\kappa\int_0^t s\beta(s)\,ds.
\]
For the paper's nonnegative shifted-gamma sporulation family this difference is strictly positive once the kernel has positive mass.

For the explicit member
\[
\tau=1,\qquad a=1,\qquad b=2,\qquad t=3,
\]
the kernel is
\[
\beta(s)
=
\begin{cases}
0,&s<1,\\
(s-1)e^{-(s-1)},&s\ge1.
\end{cases}
\]
Then
\[
\frac{\widetilde f(3)}{\kappa}
=
3-9e^{-2},
\qquad
\frac{f(3)}{\kappa}
=
4e^{-2},
\]
and therefore
\[
\frac{\widetilde f(3)-f(3)}{\kappa}
=
3-13e^{-2}>0.
\]

Thus mesh refinement does not remove the error: the printed scheme converges to the wrong memory operator.

## Assumptions and scope

The comparison is between equation (2.18), the paper's continuous spore-production term, and equations (2.27)–(2.28), its printed finite-difference approximation.

The continuum-limit statement assumes the ordinary continuity needed for a Riemann sum. The strict counterexample uses a member of the same shifted-gamma kernel family as the source.

The result concerns the formulas in the publication. Source code was not available, so no claim is made about whether an unpublished implementation silently corrected the indices.

## Proof

Write
\[
g(t)=I(x,t)H(x,t).
\]
The continuous term is
\[
f(t)
=
\kappa\int_0^t
g(t-s)\alpha(s)\beta(s)\,ds.
\]

The printed equation (2.27) has the current-time factor
\[
g(t_j)
\]
outside the summation and evaluates the kernel at
\[
t_j-t_\ell.
\]
Therefore, for
\[
t_j=t
\]
and
\[
\Delta t\to0,
\]
the Riemann sum converges to
\[
\widetilde f(t)
=
\kappa g(t)
\int_0^t
\alpha(s)\beta(t-s)\,ds.
\]

These formulas agree only under special histories and weights. To prove that the numerical operator is not generally consistent, set
\[
\alpha(s)=1
\]
and
\[
g(t)=t.
\]
Then
\[
\widetilde f(t)
=
\kappa t\int_0^t\beta(t-s)\,ds
=
\kappa t\int_0^t\beta(s)\,ds,
\]
while
\[
f(t)
=
\kappa\int_0^t(t-s)\beta(s)\,ds.
\]
Subtraction gives
\[
\widetilde f(t)-f(t)
=
\kappa\int_0^t s\beta(s)\,ds.
\]
For any nontrivial nonnegative sporulation kernel, this is positive whenever the integration interval contains positive kernel mass.

The paper's kernel has the shifted-gamma form
\[
\beta(s)=0
\]
before the latent period and is positive afterward. Hence the discrepancy is strict after that time.

A consistent left-Riemann sum for the continuous formula keeps the delayed host product and the age weights at the same quadrature node:
\[
f_i^{\,j}
\approx
\kappa\Delta t
\sum_{\ell}
(IH)_i(t_j-t_\ell)
\alpha(t_\ell)\beta(t_\ell).
\]

## Verification

The bundled `verify.py` symbolically evaluates the strict shifted-gamma witness
\[
\tau=1,\qquad a=1,\qquad b=2,\qquad t=3.
\]
It checks
\[
\frac{\widetilde f(3)}{\kappa}
=
3-9e^{-2}
\]
and
\[
\frac{f(3)}{\kappa}
=
4e^{-2},
\]
with positive difference
\[
3-13e^{-2}.
\]

The general inconsistency is analytic and follows from the two distinct continuum operators. The checker is an exact witness, not an empirical convergence test.

## Relationship to prior work

The motivating paper states the continuous HLIR spore-production convolution in equation (2.18), prints the finite-difference approximation in equation (2.27), inserts it into equation (2.28), and states that equation (2.28) is used for the simulations and subsequent disease-severity calibration.

The direct 2022 predecessor by Tabonglek, Humphries, and Khan uses a related healthy-host/spore model. Its continuous spore-production term also contains a delayed host product, while its finite-difference section prints the same structural replacement by a current-time product multiplied by a history sum. Thus the indexing defect was already present in the numerical ancestor; that paper does not identify it as an inconsistency.

The standard correction is not a new quadrature method: it is simply the Riemann sum of the integral that the model itself displays. The new content is the source-specific diagnosis that the printed numerical method has a different continuum limit, together with an exact nonvanishing source-family witness.

Searches by DOI, article title, equation number, convolution terminology, delayed-product aliases, correction terminology, and the predecessor title did not locate a published correction of this point.

## Limitations

The finding does not reconstruct unavailable MATLAB code.

A corrected implementation could differ from the printed equation (2.28). If so, the mathematical issue would remain a publication-level reproducibility defect rather than necessarily an implementation defect.

The result isolates the spore-production quadrature. It does not re-evaluate every other discretized term or the statistical fitting procedure.

## References

1. S. Tabonglek, A. Khan, U. W. Humphries, “An extension of mathematical model for severity of rice blast disease,” AIMS Mathematics 8 (2023), 2419–2434. DOI: 10.3934/math.2023125.
2. S. Tabonglek, U. W. Humphries, A. Khan, “Mathematical Model for Rice Blast Disease Caused by Spore Dispersion Affected from Climate Factors,” Symmetry 14 (2022), 1131. DOI: 10.3390/sym14061131.
