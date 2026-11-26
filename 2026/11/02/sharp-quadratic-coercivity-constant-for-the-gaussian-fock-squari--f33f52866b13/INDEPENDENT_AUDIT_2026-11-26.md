# Independent mathematical audit

## correctness

PASS

Gaussian orthogonality applied to the five coefficients of F² gives U; V=U+|a|⁴−(|a|²+|b|²+2|c|²)², and V>0 for a nonconstant polynomial. Thus the ratio strictly decreases with the relative-phase cosine when abc≠0; the optimum is anti-aligned. All nonconstant coefficient-zero cases have ratio at most 2. After |a|=1, completing the square in x=|b|² gives the deficit and quartic F_K in RESULT.md lines 52–68. An independent rational Horner calculation in Q[k] modulo the defining cubic returned zero for both F_K(u*) and its u derivative. Rational interval evaluation gives 0.176<u*<0.177 and β_K(u*)>0.3655; the cubic changes sign and has positive derivative on the specified K interval. As an alternative to the frozen quartic root exhaustion, divide F_K by (u−u*)². The quotient is a convex quadratic (positive leading coefficient), negative at both roots of β_K because there F_K=−4(K−2)[4(K−2)u²+(20K−24)u⁴]<0. Hence the quotient is negative on the entire interval where β_K>0. The unique zero there is u*, with x=β_K(u*)/[2(K−2)]; the phase condition yields exactly the stated scalar/rotation class. Constants give equality trivially. Independent numerics agree with K, sqrt(K), u*, and x*. CHECK.py and VERIFICATION.md were inspected; the uploaded script was not executed. The inequality is sharp on degree at most two; it only lower-bounds the unrestricted norm constant.

## originality

PASS

The closest primary theorem is exactly the same inequality with an unspecified uniform constant on a larger space, not an optimization. Neither it nor the inspected closely related finite-dimensional records imply the cubic, the strict gain over 2, or the complete equality class. The pass is limited to those exact degree-two results.

## value

PASS

Degree two is the first nonlinear polynomial section of a motivated square-restricted phase-retrieval inequality. The exact optimum exceeds the affine value and gives a rigorous unrestricted lower bound, while the unique nonconstant orbit identifies the phase cancellation responsible. These supply a concrete sharp benchmark for higher-degree or unrestricted bounds, not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
