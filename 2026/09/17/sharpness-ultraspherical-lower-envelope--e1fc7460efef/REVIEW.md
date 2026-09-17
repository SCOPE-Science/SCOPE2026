# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.**

The source theorem states that for normalized ultraspherical/Jacobi polynomials
and \(\alpha\ge0\), the degree-\(k\) polynomial is the pointwise minimum on the
cell determined by consecutive largest zeros of
\(R_n^{(\alpha+1,\alpha)}\).

The negative-parameter obstruction was checked algebraically in all three
regimes.

- The first transition point follows from the exact degree-one Jacobi formula:
  \(\xi_1=-1/(2\alpha+3)\).
- Direct formulas for \(U_1,U_2,U_5\) give
  \[
  U_5(\xi_1)-U_1(\xi_1)
  =
  \frac{4\alpha(\alpha+2)(2\alpha+1)(2\alpha+7)}
       {(2\alpha+3)^5}.
  \]
  Its sign is strictly negative for every
  \(-1/2<\alpha<0\), while \(U_1(\xi_1)=U_2(\xi_1)\).
- At \(\alpha=-1/2\), normalized symmetric Jacobi polynomials are the
  first-kind Chebyshev polynomials. The point
  \(x=-1/\sqrt2\) lies in the first cell and satisfies
  \(T_4(x)=-1<T_1(x)\).
- For \(-1<\alpha<-1/2\), the exact central-value identity
  \[
  U_{2m}(0)=(-1)^m
  \frac{\Gamma(\alpha+1)\Gamma(m+1/2)}
       {\sqrt\pi\,\Gamma(m+\alpha+1)}
  \]
  and the standard gamma-ratio asymptotic imply alternating values whose
  magnitudes tend to infinity. Hence the pointwise infimum at \(0\) is
  \(-\infty\).

The three cases cover the entire negative part of the Jacobi parameter range.
Together with the published \(\alpha\ge0\) theorem, they establish the stated
sharp classification.

## Originality

**PASS, to the best of our knowledge.**

The September 2026 Castillo--Sadigova preprint was checked as the primary source
of the lower-envelope theorem. Searches using the paper title, arXiv identifier,
normalized-Jacobi and ultraspherical lower-envelope terminology, negative
parameters, and equivalent pointwise-minimum language did not locate a prior
statement of this sharp negative-parameter obstruction. No overlapping SCOPE
record was located.

The individual special-function identities used in the proof are classical and
are not claimed as original. In particular, standard Jacobi/Gegenbauer
references already contain the formulas from which the central-value growth
follows. The originality claim concerns their application to the new
lower-envelope theorem: the exact parameter sharpness, the explicit degree-five
first-cell defect throughout \((-1/2,0)\), and the resulting three-regime
classification.

Because the source theorem is very recent and older special-function literature
is extensive, residual originality risk remains that an equivalent
negative-parameter envelope observation appears under different terminology.
No specific inaccessible paper was identified as especially likely to contain
this exact classification.

## Value

**PASS.**

The result determines the maximal natural Jacobi parameter range of a newly
proved pointwise lower-envelope theorem rather than merely exhibiting an
isolated counterexample. It also identifies two distinct thresholds and failure
mechanisms: a finite-degree crossing immediately below \(\alpha=0\), the
Chebyshev transition at \(\alpha=-1/2\), and loss of any finite lower envelope
below that threshold.

The original motivating question was posed only for \(\alpha\ge0\), so this
finding does not revise the affirmative answer in that range. Its value is in
showing that the new theorem itself cannot be extended even infinitesimally
below zero and in explaining what replaces the lower-envelope picture as the
parameter decreases.

## Review status

This is a same-model scientific review, not independent validation, formal
verification, journal peer review, or a guarantee of first discovery.
