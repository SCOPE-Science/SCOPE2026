# Independent mathematical audit

## correctness

PASS

The size-biased fixed-cycle count gives the stated beta-binomial law for the length of the cycle through label 1. Binomial parity projection followed by integration by parts gives the expectation: the endpoint evaluation is 1 and cancels the 1 outside the integral (the frozen wording that the boundary terms vanish is imprecise). Finite differentiation with respect to log θ gives the covariance. The kernel has one sign for even n; for odd n≥3 the L/R log derivative is strictly negative by the ordered supports, reflection and strict concavity give L(1)>R(1), and a fixed subinterval to the right of 1/2 bounds L/R by a decaying geometric factor as θ grows. For the moving root, rescale both endpoints by 2m, m=n−2. On θ∈[1,2], the left integrand after extracting log m/(2m)^(θ+1) is dominated by a constant times (x+x²)(1+|log x|)e^(−x) and converges uniformly in θ on fixed compact x-intervals away from zero. The right integrand after extracting (2m)^−2 is at most 2xe^(−x), using −log(1−u)≤2u for u≤1/2, and has limit xe^(−x). These give the required uniform relative o(1); an O(1/m) error for the full leading term on the left is not needed. The ratio asymptotic first confines the root to θ→1, then yields (θ_n−1)log n−log log n→0. At n=2 the sign is strict; at n=3 differentiating 6θ/((θ+1)(θ+2)) gives the stated sqrt(2) crossover. Independent exact enumeration (independent_check.py, check-log.txt) confirmed finite cycle-sum moments in 28 cases and both integrals in 14 cases; uploaded code was not executed. These checks do not prove uniqueness or the asymptotic.

## originality

PASS

Credit the classical expected cycle counts and the exact moments recoverable from them. The supported distinct claim is the strict parity-dependent sign classification and the location and logarithmic asymptotic of the unique odd-order crossover for total cycle count versus even-cycle label mass. No inspected statement gives that classification or an applicable general result already yielding it.

## value

PASS

The statistic compares how fragmented a permutation is with how much mass lies in even cycles, not with a count of such cycles. The global even/odd split, uniqueness, and log-log displacement of the odd threshold resolve a structural question about a standard model. This goes beyond a mean calculation or a few computed roots.

The dated certificate retains the supplied scientific assessment, sources and limitations.
