# Independent mathematical audit

## correctness

PASS

On an iid coupon tape independent of the Bernoulli burst indicators, the burst policy needs ceil(T_n/b) nonempty rounds. The mean conditional on the tape is b times that number, so the extra expectation is exactly the rounding residual. Each integer draw-count at least n is possible, giving both strict bounds on this expectation. For b=2 the residual is the odd-time indicator; the product of the independent geometric waiting-time generating functions at −1 is (−1)^n/binom(2n−1,n), giving the parity correction. For general fixed b, the modulus at every nontrivial bth root of unity is exponentially small because a positive fraction of parameters j/n lie in [1/4,1/2] and each corresponding factor is uniformly below one; Fourier inversion gives the exponential residue estimate. Before n rounds the burst process can complete with positive probability, whereas the fixed process cannot. In the large-round tail the single-missing coupon bases are α=1−1/n and β=1−1/b+(1−1/n)^b/b, with 0<α<β<1; all larger missed-set terms have strictly smaller bases, giving the reverse order eventually. In the window, the log of the burst/single miss-probability ratio is (b−1)(j/n)²/2+O_b((j/n)³). For j bounded by J=ceil(4 log n/log log n), the omitted Bonferroni terms are bounded by exp(O(J))/(J+1)!=n^(−4+o(1)), negligible after scaling by n/log n. On the same range the Taylor exponent of the ratio is O_b(j² log n/n) uniformly small, giving summable scaled domination C j² exp(C'j)/j!. Hence one may take termwise limits and sum, obtaining (b−1)/2 times the second derivative of the Gumbel CDF. At x=0 the scaled limit is zero, with no finite-size sign asserted there.

## originality

PASS

The pass is for the explicit signed, relative Gumbel-window limit for these equal-mean round policies, not for generic cover-time formulas, the use of inclusion–exclusion, or merely obtaining the burst mean. Ferrante–Frigo already give an exact repeated-type group expectation from which that mean follows by the mean interarrival time. Available related signed and approximation results use materially different sampling and comparison targets. No exact or stronger antecedent of the signed two-policy statement was established in the bounded checks.

## value

PASS

Matching the expected throughput leaves the mean, earliest possible coverage and completion probability in opposition. The signed leading term determines which policy has the greater completion probability at fixed points to either side of the cutoff center, even though their marginal Gumbel limits agree; its coefficient gives the magnitude of that difference. This yields concrete distributional information beyond the already available group expectation or an order-of-error estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
