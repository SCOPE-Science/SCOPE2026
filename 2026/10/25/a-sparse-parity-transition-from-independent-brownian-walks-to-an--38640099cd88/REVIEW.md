# Independent mathematical audit

## correctness

PASS

Given the first n input signs, exactly 2^((n−X_n)/2) independent Bernoulli coefficients contribute. Consequently the conditional parity mean is (1−2p_n)^(2^((n−X_n)/2)). In the filtration revealing the first n input signs but only levels below n, this is the predictable cross-covariance of increment n+1 (increment 1 has cross-covariance 1), with both marginal predictable variances equal to 1. The factor p_n 2^((n−X_n)/2) is 2^((1/2−θ)n−X_n/2−2−δ_n) with 0≤δ_n<1. The strong law off criticality, and the O(n^−1/4) probability of |X_n|≤n^1/4 at criticality, give the respective L¹ approximations by 0, 1 and 1_{X_n>0}. The error in any partial bracket sum on [0,T] is bounded by the whole sum of absolute errors divided by N, which tends to zero in L¹ by Cesàro convergence. The occupation mapping is continuous at Brownian paths with Lebesgue-null zero set; using a step input rather than its interpolation makes a uniform O(N^−1/2) difference to the input path. Bounded jumps and bounded predictable variances give martingale tightness and the martingale and compensated-product identities pass to subsequential limits (uniform integrability on bounded time intervals follows from the bounded-increment fourth-moment bounds after scaling). For the critical limit write M=Y−∫1_{B>0}dB, orthogonal to B with bracket ∫1_{B≤0}ds. On an independent Brownian extension with U put W=M+∫1_{B>0}dU. Then (B,W) has bracket tI, so is standard planar Brownian motion by Lévy's characterization; M=∫1_{B≤0}dW, which proves uniqueness in law and identifies the full limit. The two constant-bracket limits and Lévy's occupation-time law yield the other assertions. Replay is by the displayed parity and bracket calculations and RESULT.md Steps 1–4; the inspected script and its recorded 122-check output corroborate the finite parity identities only and were not executed. The proof gives annealed weak convergence, not quenched convergence or a rate.

## originality

PASS

The supported distinction is the joint annealed phase diagram for exponentially rare, independently resampled full-subset coefficients. The input model architecture, Brownian stochastic-integral technology and occupation arcsine law are not credited as new.

## value

PASS

Exponentially many active subsets compete with exponentially rare perturbations, and at the threshold fluctuations of the input itself decide whether the motions synchronize. A random, explicitly arcsine-distributed cross-bracket separates this joint law from both independent and coincident Brownian pairs and from a fixed correlated Gaussian limit. The complete annealed classification is useful for this natural family even though its tools are classical.

The dated certificate retains the supplied scientific assessment, sources and limitations.
