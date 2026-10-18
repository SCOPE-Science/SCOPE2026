# Independent mathematical audit

## correctness

PASS

With Haar U, integer b>=2 and fixed s>0, the collision count over ordered off-diagonal pairs has mean 2s(1-1/N) because multiplication by every integer b^i(b^d-1) preserves Haar. Fourier integration of circular arc indicators gives exact Bernoulli kernel C_r(a,c)=[B2({(a-c)r})-B2({(a+c)r})]/(ac) for reduced multipliers, and |C_r|<=2r/max(a,c). For distinct orbit lags d,e the gcd(b^d-1,b^e-1)=b^{gcd(d,e)}-1, with proper common divisor <=max(d,e)/2, forces normalized multipliers at least b^{max(d,e)/2}; summing displacements and lag maxima gives total O_{b,s}(1) unnormalized variance. For equal lag d=e, the h=|i-k| covariance reduces to C_r(1,b^h)=(2r/b^h)-4r² when (b^h+1)r<1; dominated convergence of the geometric series gives N Var R_N ->4s(1+2 sum_{h>=1} b^{-h})=4s(b+1)/(b-1). Splitting at h~log_b N gives O_{b,s}(log N/N) correction; exact iid pairwise uncorrelated collisions give 4s/N benchmark. Independently checked the Bernoulli kernel by disjoint exact rational interval partition for 1<=a,c<=7, two rational radii. Those finite checks only corroborate, not prove the asymptotic.

## originality

PASS

Best-of-knowledge new sharp leading variance coefficient for unsmoothed circular near-collisions, distinct from known almost-sure Poissonianity and nonsharp smooth-test variance decay. Primary lacunary variance propositions read and compared by normalization/implication; published corpus service failure and old unindexed calculations remain risks.

## value

PASS

Poissonian pair-correlation convergence is common for expanding dynamical systems, but its scale of fluctuations need not resemble independent samples. The exact factor (b+1)/(b-1) quantifies persistent dynamical dependence and gives a useful sharp second-moment benchmark for all integer expansions; this is a substantive unknown asymptotic coefficient, not simply a correct code run.

The dated certificate retains the supplied scientific assessment, sources and limitations.
