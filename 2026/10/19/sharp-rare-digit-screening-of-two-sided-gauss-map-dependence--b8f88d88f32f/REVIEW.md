# Independent mathematical audit

## correctness

PASS

With x=1/(k+u) the Jacobian cancels the numerator from the natural-extension density. The stationary event probability is log(1+1/N)/log 2 and integration in v telescopes to the stated conditional marginal. Write z=1/N and s=u+v. The branch sum divided by z is 1+(1/2-s)z+(s²-s+1/6)z²+O(z³), uniformly by Euler–Maclaurin on s∈[0,2]. Multiplication by log(1+z)/z and (1+uz)(1+vz) gives first-order cancellation and second-order coefficient (u−1/2)(v−1/2). The marginals are uniformly 1+O(z). For KL relative to their conditional product the linear term integrates to exactly zero, and the uniform quadratic expansion gives 1/288; the L¹ integral with a factor 1/2 gives 1/32. On any pair of digit bins the likelihood ratio is a product-measure conditional average before taking the expansion; the relative uniform error therefore survives on the full countable alphabet. Digit 1 is exactly the positive half of u−1/2 and all other bins lie in the negative half, preserving the TV coefficient. Independently, the variance of the bin means is 1/12 minus the within-bin variance sum ∑[k(k+1)]⁻³/12=(10−6ζ(2))/12, giving π²/12−3/4 and hence the reported digit KL coefficient. This checks both constants, the Lebesgue-digit limit, and the use of conditional marginals and natural logarithms. The frozen checker was inspected, not executed; the separate `python3 /workspace/checks/frozen_math_checks.py 3` checks the trigamma ratio at nine sample points and the exact within-bin variance identity. These tests do not establish the uniform remainder or the infinite-alphabet limit, which are analytic.

## originality

PASS

The Gauss invariant kernel is established and the branch-conditioned joint density is its direct consequence, not a standalone originality claim. The supported distinct contribution is the sharp second-order interaction and the resulting continuous and digit-level TV/MI laws. No inspected earlier statement gives these or a stronger result covering them without the new cancellation and projection computations.

## value

PASS

Rare central digits give a natural test of how much the immediate past and future continue to depend on one another beyond a limiting product law. The exact leading term makes the rates quantitative and reveals a useful distinction: the nearest-digit projection preserves the leading TV signal because it preserves its sign partition, but strictly reduces the leading information constant because it averages the interaction within bins. This is useful independently of any claim about longer windows, arbitrary initial laws, or other continued-fraction algorithms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
