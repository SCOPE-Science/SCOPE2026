# Independent mathematical audit

## correctness

PASS

On the corrected claim, let the argument at a positive sink be pi/2+t modulo 2pi. The signed multiplier is -rho sin(t), and the positive sine and strict bound together are equivalent to -h<t<h. Then u=cos(t) and a lift of the phase is rho cos(t)-pi/2-t. Its derivative is -1-rho sin(t)<0 throughout; the image is exactly (c-h,c+h), with endpoints attained as t approaches +h and -h respectively and signed multipliers -1 and +1. The image width is less than pi, so projection introduces no duplicates. Reflection treats the negative sink independently, and zero has multiplier modulus rho whenever it is fixed. Since 2h<pi, only one circular separation can contribute to overlap, giving (2h-d)_+ and no bistability at tangency. The centers coincide iff c is an integer multiple of pi, and c> -pi/2 gives exactly the stated sequence. Local contraction gives open attraction neighborhoods with disjoint basins, not a global orbit classification. The endpoint sign test at rho=5/4 was independently checked (python3 /workspace/branches/independent_checks.py 2). The supplied finite scanner was inspected, not executed; it deliberately avoids bifurcation boundaries and cannot check the failed orientation.

## originality

PASS

The distinct claim is the all-rho phase census and exact coexistence length and resonance sequence for hyperbolic fixed sinks, not the sine model or its derivative criterion. The sign correction is a proof repair, not a novelty claim. No compared source verifies equivalence or stronger coverage of that classification. Full text of the originating article remains unverified independently and is a named risk.

## value

PASS

A phase sweep in the motivating model does not determine when two attracting fixed states can coexist. The corrected theorem gives a universal count, an exact phase-design measure, and infinitely many gains of maximal overlap with shrinking widths. These are useful even without a classification of neutral fixed points or other attractors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
