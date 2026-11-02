# Independent mathematical audit

## correctness

PASS

With X=T=T*, Toeplitz–Hausdorff makes K=closure{(m_A(x),m_X(x))} compact convex. The vertical section at each A expectation has Chebyshev radius half its width, and hence E_A(X)=D0/2. Its symmetric difference K-K has vertical width D=D0 at first coordinate zero (closure is removable by mixing with a point of opposite horizontal sign unless A scalar). A supporting line of the concave upper profile of K-K gives real a for which X-aA has spectral width <=D; centering by real b yields ||X-aA-bI||<=D/2. The inverse estimate is immediate. Splitting T into selfadjoint real and imaginary parts and approximating separately gives d_A(T)<=2E_A(T). Exact two-dimensional nonnormal witness A=diag(1,-1), T=[[0,2],[0,0]] has fixed-observation target circle radius sqrt(1-t^2), E=1, while every complex affine pencil retains offdiagonal 2 so d=2. Infinite Hilbert dimension follows from numerical-range convexity and operator spectral intervals, not finite sampling. Independent symbolic checks verified the witness radius identity and 49 distinct affine perturbation obstructions.

## originality

PASS

PASS qualified: Johnson arxiv:2610.29826 Theorem 4.2 and Corollary 4.3, inspected in full, already prove the exact-zero case (a numerical response factors through A only if affine). They do not bound positive prediction error in terms of norm distance or provide sharp factor two; Weis 2025 analyzes openness of numerical-range restrictions, also without this quantitative inequality. Novelty is only the sharp uniform quantitative bound and selfadjoint exact radius formula, not qualitative affine factorization.

## value

PASS

A natural stability problem for recovering one operator expectation from the expectation of one observable; the exact selfadjoint minimax formula and optimal factor-two complex loss quantify robustness beyond qualitative exact factorization. Holds in arbitrary Hilbert dimension, with explicit sharp 2x2 obstruction. Its objective is mathematically motivated by numerical-range inverse problems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
