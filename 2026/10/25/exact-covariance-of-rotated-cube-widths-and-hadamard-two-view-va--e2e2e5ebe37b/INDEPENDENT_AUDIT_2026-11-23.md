# Independent mathematical audit

## correctness

PASS

For c=|a·b| and φ=arccos(c), represent the two Gaussian coordinates as T₂ cos u and T₂ cos(u−φ) in their plane. On one angular period [0,π], the signed product of the cosines has integral πc/2 and is negative on (π/2,π/2+φ), where its integral is (φc−sin φ)/2. Multiplying the resulting absolute angular mean by E T₂²=2 yields (2/π)(sqrt(1−c²)+c arcsin c); the endpoints follow by continuity. Dividing by the full Gaussian radius second moment d gives the spherical pair law. Summing the segment contributions and subtracting the common mean square gives exactly the stated covariance. The binomial expansion under the integral for g′ gives g=1+s/2+s²/24+… with all higher coefficients positive, hence g−s²/24 is strictly convex away from s=0 and the bound extends to s=1 by continuity. The quadratic gap is (sum R_ij^4−1)/(12πd), and strictness holds unless every squared entry is 1/d. Haar averaging gives covariance mean zero; since Cov(I)=Var(W₀)>0 on an open neighborhood by continuity, the flat lower bound must be strictly negative. The gamma ratio with z=d/2 is Γ(z)/Γ(z+1/2)=z^(−1/2)(1+1/(8z)+1/(128z²)+O(z^−3)), giving the stated asymptotic. Direct evaluation with three squared entries 1/9 and six 4/9 gives −0.009244693496 in dimension 3; with sixteen entries 1/4 it gives −0.010042530806 and paired/single variance 0.319603062451 in dimension 4. The variance comparison is with two independent directions at the same number of width evaluations. Numerical checks supplement rather than replace the analytic argument.

## originality

PASS

The classical absolute-Gaussian kernel, marginal width moments, Hadamard flattening principle and even the chosen three-dimensional reflection matrix are prior ingredients. The non-covered contribution is the quantified all-orientation optimization of the shared-direction two-Euclidean-cube covariance, with its negative minimum, dimension dependence and paired-estimator consequence. This is a bounded best-of-knowledge finding, not a priority guarantee.

## value

PASS

The distinguishing useful fact is that shared directions can outperform independent directions, even with identical width marginals, and that there is an exact optimum over relative orientations in every Hadamard order. The quantitative fourth-power defect measures the penalty for perturbing that orientation, and the baseline asymptotic shows the dimension scale of the advantage. These are usable estimator-design facts beyond a one-body second moment or an entrywise-norm equality criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
