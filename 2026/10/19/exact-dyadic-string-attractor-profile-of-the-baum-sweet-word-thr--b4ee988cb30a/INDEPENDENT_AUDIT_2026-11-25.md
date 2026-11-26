# Independent mathematical audit

## correctness

PASS

The frozen claim is exactly nine finite prefixes, with b(0)=1, zero-based indices, and maximal zero runs in the ordinary expansion. In an independent bitmask reconstruction (python3 /workspace/branches/audit_attractors.py), the digit test counted gaps between successive set bits, including trailing zeros, and each occurrence contributed its occupied positions to one union mask for its contiguous factor. Each factor mask intersected the supplied attractor mask. Distinct factor totals by length were 2, 8, 26, 97, 410, 1661, 6744, 27145, 108896. Every listed dual factor was distinct and in bounds; the maximum integer half-unit load at each length was 2. Total half-units were 2, 4, 4, 6, 10, 11, 14, 16, 18. Any attractor intersects every union at least once, so summed dual mass is bounded above by the sum of loads on selected positions, divided by 2, which is at most the attractor size. Ceilings give exactly 1,2,2,3,5,6,7,8,9, matching the upper witnesses. RESULT.md, the verification note, the full certificate data and the deposited verifier were inspected; the latter was not executed. No larger prefix or asymptotic formula follows.

## originality

PASS

No earlier same-word exact attractor profile, or theorem implying these nine values without new problem-specific computation, was established in the bounded comparisons. Same-word indexed results optimize different statistics; the closest exact same-measure indexed result uses a different word. This is a judgment about the nine certified values only, not a priority or novel-method claim.

## value

PASS

This is a useful finite exact benchmark for an established complexity invariant on a classical automatic word. Powers of two are natural levels of the word's digit-length and length-doubling structure, not arbitrary sampled positions. The contiguous prefix range spans the small plateau, the jump from 3 to 5, and the five tested levels of equality with m; general decidability does not tell where those features occur. Matching certificates make the precise cutoff values usable for checking automatic or morphic constructions, in particular the six-position minimum at 64 certified by rounding up 11/2. This value does not depend on extrapolating a law past 512.

The dated certificate retains the supplied scientific assessment, sources and limitations.
