# Same-model review

## Correctness

**PASS.**

The proof reduces rank deficiency to the zero set of one nontrivial analytic
minor. The nontriviality step is explicit: for distinct real \(a_j,b_p\),
\[
\det[e^{i\varepsilon a_jb_p}]
=
\frac{(i\varepsilon)^{r(r-1)/2}}{\prod_{q=0}^{r-1}q!}
V(a)V(b)+O(\varepsilon^{r(r-1)/2+1}).
\]
This follows from the exponential power series and Cauchy--Binet, because the
unique exponent set of least total degree is \(0,1,\ldots,r-1\). The leading
coefficient is nonzero for distinct parameters.

For fixed angles, choosing clustered positive distinct delays makes the
selected minor nonzero, so its squared modulus is a nontrivial real-analytic
function of the delays. For fixed delays, clustering distinct angles near zero
gives the symmetric argument. Mityagin's zero-set theorem then implies that
the rank-deficient set has Lebesgue measure zero. The rectangular cases use an
\(r\times r\) minor with \(r=\min(\ell,m)\); the \(r=1\) case is immediate.

Adversarial checks included the half-open angular interval, conjugate-paired
nodes used in real linear systems, more rows than columns and more columns
than rows, clustered-but-distinct delays, and probability laws supported on
lower-dimensional sets. The last check is why the probability-one corollary
is stated for joint laws absolutely continuous with respect to Lebesgue
measure rather than for arbitrary random delays.

The clustered determinant asymptotic also correctly separates exact rank from
conditioning: as the delays coalesce, the matrix converges to repeated rows
and its least singular value tends to zero.

## Originality

**PASS, to the best of our knowledge.**

Ng and Kutz explicitly present the generalized-Vandermonde full-rank statement
as Conjecture 1, and their current arXiv abstract states that the nonuniform
stable-embedding extension is proved provided that conjecture holds. Searches
using the exact title and arXiv identifier, `Conjecture 1`, `generalized
Vandermonde`, `nonuniform Takens`, `uneven delays`, `almost surely full rank`,
and equivalent exponential/Fourier-matrix formulations found no later source
resolving that conjecture.

A September 2026 paper by Huang, Li, and Liu studies generalized Vandermonde
factors for nonuniform array processing and proves minimum-singular-value
bounds for structured segmented sampling geometries. Its abstract and indexed
problem summaries do not supply the source-specific almost-everywhere rank
closure here; it is treated as relevant quantitative prior literature rather
than as coverage.

The proof ingredients themselves are standard and are not claimed as new.
In particular, Mityagin records the classical fact that the zero set of a
nontrivial real-analytic function has measure zero, and the determinant
expansion is a direct Cauchy--Binet/Vandermonde computation. The originality
claim is limited to using these ingredients to resolve the 2026
nonuniform-Takens rank conjecture, strengthening it to fixed-frequency
conditional almost-sure rank, and recording the clustered-delay conditioning
obstruction.

The complete source PDF was not independently inspected. The current arXiv
abstract and an indexed quotation of Conjecture 1 were inspected. The full
48-page Huang--Li--Liu paper was likewise not independently inspected beyond
its abstract and indexed summaries. An unindexed theorem in either full text
that already gives the same source-specific generic-rank conclusion is the
principal residual originality risk.

## Value

**PASS.**

The rank conjecture is the explicit algebraic bottleneck in the recent
nonuniform stable-linear-Takens extension. The result removes that bottleneck
for the continuous sampling laws used in the intended applications, and does
so after conditioning on the system frequencies rather than randomizing the
dynamical system.

The clustered-minor asymptotic adds a practically relevant negative result:
almost-sure injectivity cannot be upgraded to a distribution-free conditioning
bound. It explains why the source paper's finite-sample lower-singular-value
problem remains substantive even after the rank conjecture is closed.

## Limitations checked

The record does not claim deterministic full rank for every distinct delay
tuple, quantitative finite-sample conditioning, robustness for singular or
discrete delay laws, or a nonlinear Takens theorem. Distinct frequency nodes
are required. The stable-embedding consequence retains every other
observability and asymptotic hypothesis of the source theorem.

**Same-model review: passed. Independent audit: not yet performed.**
