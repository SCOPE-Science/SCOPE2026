# Independent mathematical audit

## correctness

PASS

The hypersimplex is the uniform matroid base polytope in its intrinsic hyperplane 1-perp; the support-width identity is EXACTLY the top-k minus bottom-k Gaussian sample sums divided by centered chi length. The proof gives a uniform O_p(1) error when replacing empirical trimming quantiles by population normal quantiles for alpha=k/n in a fixed compact [epsilon,1/2]. Gaussian denominator expansion yields influence function psi_z= (|G|-z)_+ - 2[phi(z)-zQ(z)] - phi(z)(G²-1), whose variance is the displayed positive continuous V(z). A triangular-array Lindeberg theorem gives a CLT even if alpha_n oscillates. The limit is not claimed for sparse ranks or as finite-n variance. Inspected CHECK.py uses exact Fraction alternating-series brackets for normal phi/Q and pi to rigorously certify V(1/2)>V(1)<V(3/2)>V(2). Independent normal-integral calculation reproduced V at 0,1/2,1,3/2,2 as 0.0450703414,0.0148846190,0.0058140331,0.0087088534,0.0054190364; Gaussian integral formulas, not these floats, prove the all-rank CLT.

## originality

PASS

Best-of-knowledge: A single balanced value and generic asymptotic machinery do not logically yield the rankwise strict V inequalities without the explicit computation. A broader theorem on this exact studentized L-statistic might subsume the CLT and is a genuine risk. A general CLT can imply Gaussianity after calculating the exact influence function but does not by itself assert the nonmonotone V profile and its certified strict inequalities; the new quantitative specialization is the relevant survivor.

## value

PASS

The rank fraction indexes a canonical infinite family of uniform-matroid base polytopes. An explicitly normalized stochastic width CLT and a rationally certified decrease-increase-decrease variance profile refute a natural monotonicity expectation; it is a motivated geometric phenomenon, not a routine one-number variance tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
