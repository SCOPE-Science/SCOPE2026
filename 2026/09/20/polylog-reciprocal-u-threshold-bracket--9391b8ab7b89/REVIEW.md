# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The upper-bound argument was rederived independently from the reciprocal
coefficients. The two required ingredients are separated: zero-freeness of
the smoothed reciprocal follows from a strict Rouché estimate for every
\(|z|<1\), while the defining \(\mathcal U\) inequality follows from a
different weighted Cauchy--Schwarz estimate. At the endpoint \(s_*\), the
Rouché majorant equals one only at the formal boundary radius \(r=1\);
inside the disk it is strictly smaller, so no endpoint gap is hidden.

The lower obstruction was checked from the starlike family
\(f_m(z)=z/(1-z^m)^{2/m}\). Its logarithmic derivative has positive real
part. The generalized-binomial coefficients of \((1-z^m)^{2/m}\) are
strictly negative after the constant term, and the transformed
\(\mathcal U\)-series has positive coefficients asymptotic to
\(C k^{-\sigma-2/m}\). Choosing \(2/m<1-\sigma\) forces divergence on the
positive radius. This gives a genuine failure of \(\mathcal U\), with the
zero-of-the-reciprocal case handled separately.

The numerical root is not used as an unproved equality: \(s_*\) is defined
exactly as the unique root of a strictly decreasing explicit series
function. The decimal localization follows from finite sums and an
integral remainder bound.

## Originality

PASS, to the best of our knowledge.

The 2013 Ali--Obradović--Ponnusamy paper was inspected at the theorem and
open-problem level. It proves the universal \(3/2\) result and ends with a
terse smallest-parameter question. Since \(F_0=f\), the present novelty
claim is restricted to the monotone universal \(\mathcal U\)-tail question
suggested by that theorem, rather than every literal reading of the final
sentence. Searches by DOI/title, exact reciprocal transform,
polylogarithm/Hadamard terminology, class-\(\mathcal U\) terminology, and
later polylogarithm operators did not locate the present bracket or the
root-transform lower obstruction.

The 2015 Ali--Alarifi \(\mathcal U\)-radius paper was also checked as a
close citation-chain candidate; it treats radius problems rather than this
polylogarithmic threshold. Later polylogarithm-operator papers found in
searches use different function classes/operators.

Residual risk: a result stated only as a multiplier-sequence,
fractional-integration, or reciprocal-transform theorem could imply the
same bound without using the paper's notation. No claim of exhaustive
literature coverage is made.

## Value

PASS.

The result narrows a documented open universal threshold from the
published upper bound \(3/2\) to an explicit \(1.41351950\ldots\) while
also supplying a universal lower barrier \(1\). The two sides use
different mechanisms and identify where further progress must occur:
coefficient correlations/zero-freeness on the upper side and possible
non-\(\mathcal U\) extremals at or above \(1\) on the lower side.

## Limitations

- The exact \(\mathcal U\)-tail exponent is not determined.
- The source's final problem is terse; this record treats only the monotone
  universal \(\mathcal U\)-tail formulation and does not determine a
  universal \(\mathcal S\)-tail threshold.
- The upper bound may be improvable using coefficient information beyond
  the area theorem and \(|b_1|\le2\).
- Terminology-equivalent prior coverage remains a residual risk.
