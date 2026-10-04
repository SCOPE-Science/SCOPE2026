# Review

## Correctness

PASS. The six treatment effects sum exactly to \(0\), so the stated weak null holds. The test statistic is the treatment-control studentized statistic used by Wu and Ding, and comparing \(T\) is equivalent to comparing \(T^2\). Exact rational enumeration covers every one of the \(20\) realized assignments and, conditional on each, every one of the \(20\) sharp-null rerandomizations. The p-value multiplicities are \(7,3,3,7\) at \(1/10,1/5,9/10,1\), respectively, so the exact size at \(\alpha=0.1\) is \(7/20\). The minimum standard-error denominator over all \(400\) comparisons is \(246719/2250000>0\).

## Originality

PASS. The primary paper proves finite-sample exactness only for the sharp null and asymptotic weak-null control for the studentized statistic. Its finite-sample simulation section studies three- and four-arm designs rather than this balanced two-arm exact enumeration. A later prepivoting paper explains the general possibility of anti-conservatism when a sharp-null reference distribution is used for a weak null and recovers studentization as an asymptotic fix in completely randomized designs, but it does not state or imply this six-unit p-value law or exact \(7/20\) size. Focused semantic-database and web searches found no equivalent finite-sample witness. Residual risk remains that an older or obscure permutation-test example could contain an equivalent numerical construction.

## Value

PASS. The finding pinpoints a practically meaningful boundary of a standard recommendation: asymptotic weak-null validity does not prevent severe finite-sample inflation, even with balanced treatment allocation and a fully defined studentized statistic. The natural nominal level \(0.1\), tiny finite population, and exact full randomization calculation make the example a reusable stress test for weak-null randomization methods and finite-sample refinements.

## Closest literature and limitations

The closest source is Wu and Ding, arXiv:1809.07419, especially their treatment-control specialization and finite-sample simulation discussion. Cohen and Fogarty, DOI 10.1111/rssb.12439, gives broader conceptual coverage of sharp-versus-weak randomization inference but only asymptotic weak-null protection for the completely randomized studentized statistic. The present claim is not a worst-case or minimality result.

Same-model review: passed. Independent audit: not yet performed.
