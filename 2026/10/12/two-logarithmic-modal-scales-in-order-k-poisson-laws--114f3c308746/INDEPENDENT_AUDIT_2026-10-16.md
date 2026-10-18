# Independent mathematical audit

## correctness

PASS

For X=sum_{j=1}^k jN_j, independent N_j~Pois(lambda), conditional on total count N~Pois(k lambda) the jumps are iid uniform 1..k; hence each positive mass ≤(1−exp(−k lambda))/k, establishing s_k≥log(k+1)/k. At lambda=(1+eps)log(k)/k, Chebyshev localizes ≥3/4 positive mass among O(k sqrt(log k)) integer sites while zero has mass k^(−1−eps), so s_k~log(k)/k. For x=k, unnormalized coefficient Q_k(lambda)=sum_{m=1}^k binom(k−1,m−1)lambda^m/m! rises strictly from zero and has unique positive root r_k with Q_k(r_k)=1; Q_(k+1)>Q_k implies r_(k+1)<r_k. Writing u=k lambda, F(u)=sqrt(u) I_1(2sqrt(u)), the exact nonnegative product-loss bound 0≤F(u)−kQ_k(u/k)≤(u/(2k))F(u) yields asymptotics from fixed-order Bessel I_1. Thus 2sqrt(k r_k)=log k−(1/2)loglog k+log(2sqrt(2pi))+o(1), r_k~(log k)^2/(4k), ratio r_k/s_k→∞. At lambda strictly between s_k,r_k, any positive winning x exceeds k by coefficient monotonicity for x≤k. Exact independent Fraction coefficients for k=15 and lambda=501/2000 show h15(15)<1<h15(25); finite diagnostics are not asymptotic proofs.

## originality

PASS

The mode literature provides fixed-order cases, bounds and conjectural numeric power fits, not the two sharp logarithmic asymptotic scales or second-order Bessel correction. Kwon–Philippou explicitly study r_k and ask related mode-crossing questions; Mane finds finite-order non-k transitions and numerical scaling conjectures. Neither those results nor standard Bessel asymptotic alone yields the uniform product comparison and s_k pigeonhole bound used here.

## value

PASS

The asymptotic separation resolves a structural misconception about the first departure of the zero mode: the x=k crossover is much later than the true first mode loss, by a diverging log(k)/4 factor. A second-order term and global strict r_k monotonicity give quantitative information relevant to order-k compound Poisson mode theory beyond finite illustrations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
