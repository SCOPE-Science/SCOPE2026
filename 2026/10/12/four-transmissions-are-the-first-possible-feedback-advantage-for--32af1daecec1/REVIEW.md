# Independent mathematical audit

## correctness

PASS

With uniform messages a basis code succeeds on S with probability equal to its number of projected words divided by M. For M=1 use one word, and for M=2 use opposite vertices (with the full-cube cases handled by repetition). At n=2 the three-word core covers both symbols in each coordinate. At n=3 the three-word core has distance two and both symbols at every coordinate, and the even-parity core projects bijectively on each pair. Adding distinct unused vertices after the latter core preserves saturation on each proper subset; after exhausting the cube, repetitions preserve all projection counts. This includes S empty and all M above the cube size. Thus one code saturates every pattern bound at once for any exogenous survivor-set distribution. Wilde's Corollary 4.3 gives the matching feedback optimum without initial shared entanglement; Theorem 6.1 supplies the strict quantum no-feedback gap at n=4, M=4 and 0<p<1. Its strictness follows because equality forces four mutually orthogonal, pure two-qubit marginals in every two-survivor sector, hence product codewords. Every message pair would need local orthogonality on at least three sites (18 incidences); each qubit site permits at most four orthogonal message pairs (16 total). The finite state/POVM optimum is attained by compactness. A separate exhaustive search over binary cube subsets found simultaneous saturators at every size through the full cube for n<=3 and no four-word binary saturator at n=4; this last check does not establish the quantum converse. Replay with python3 /workspace/branches/independent_checks.py 4. The source checker is in artifacts/verify.py and was inspected, not executed.

## originality

PASS

Credit Wilde for the feedback formulas and the four-use quantum example, and Rosati for the precedent for the no-feedback converse. The supported new content is the simultaneous patternwise no-feedback achievability for every short-block message count, and with it the sharp first-blocklength statement.

## value

PASS

The positive example alone left a concrete question about the minimum quantum channel blocklength. Proving simultaneous saturation identifies this sharp boundary even when the erasures at shorter lengths are correlated. It also establishes that classical basis encoding suffices for every message count at those lengths, rather than only for a few code parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
