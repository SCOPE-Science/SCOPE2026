# Independent mathematical audit

## correctness

PASS

This PASS is for /workspace/repairs/2/RESULT.md, not for the uncorrected derivation. Frozen lines 34 and 57 use br−aq=1 for a/q<b/r, which is false, for example for the first pair 0/1<1/n. The repair uses bq−ar=1 and supplies a direct proof of the critical no-other-speed interference assertion: write (p,k)=u(a,q)+v(b,r) in the unimodular basis of neighboring Farey vectors. Because 0<k≤n<q+r, exactly one coefficient is positive and the other is nonpositive. On the gap this gives |kt−p| at least the minimum of the two endpoint distances qt−a, b−rt; the endpoint vectors themselves realize the candidates. Thus the gap length under the common strict threshold is exactly the positive-part summand, for every nonnegative threshold. The ordered denominator reconstruction handles each wrap endpoint without duplication. All slope jumps are positive, and the odd-sum, even-m, and odd-m constructions exhaust attainable coprime sums except 2n−2 for even n; n=2 merely omits an index outside the range. At 1/(2n) there is no clipping, each center contributes twice to the slope sum, and Möbius inversion gives the totient limit. For the final segment only q+r=n+1 has positive length; the reciprocal partial fractions and reduced mediants yield the harmonic sum, separate open components, and the distinct points only in the non-strict critical set. The frozen checker was inspected, not executed. Independently subdividing the circle at exact rational events and testing intervening midpoints matched 143 measures for 2≤n≤14 and all 13 critical point sets in that range (python3 /workspace/review_checks.py); the proof gives the full domain.

## originality

PASS

The repaired result credits classical Farey geometry and does not claim priority for the scalar critical threshold or its equality case. The supported distinct finding is the finite distributional evaluation with its arithmetic slope-jump spectrum and benchmark. The closest inspected literature and indexed entries treat a uniform bound, unequal two-speed thresholds, deletions, or different Farey statistics; they do not give this full finite law with its kink classification. The claim is elementary, and unlocated equivalent weighted-gap analysis remains possible.

## value

PASS

In the canonical tight consecutive-speed family, the survivor measure at all thresholds is a natural refinement of peak separation and of a bound at one radius. The exact kink classification, including the missing reciprocal index only at even sizes, and the exact mass and limiting value at the benchmark give a useful calibration not captured by the scalar endpoint. The repair corrects the arithmetic proof without inflating the claim to general speeds or claiming the underlying classical geometry as a separate contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
