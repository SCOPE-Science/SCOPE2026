# Independent mathematical audit

## correctness

PASS

The Möbius sum is multiplicative, with the stated positive prime-power factors. With x=1/p, r=kappa-1 and S_a=sum_{j=0}^a x^j, the factor Q(p^a)^r is the average of t^r on [S_(a-1),S_a]. This is strictly increasing with a and bounded above by (1-x)^(-r). Thus local scores tend to minus infinity as a grows, and only finitely many primes can compete with exponent zero at any epsilon>0. Choosing the largest local maximizer gives the largest integer. Expanding the same averages gives L_1=x/2+(kappa-5)x^2/24+O(x^3) and L_2=log(1+x)+x^2/(2(1+x))+O(x^4)=x+O(x^3). Comparing exponent one against zero permits equality, while comparison against two must be strict; the bound on Q excludes all a>=3 since the needed epsilon is asymptotic to 1/(4p log p), below s~1/(2p log p). This proves (s,t] with the stated width. The analytic extension T of t has T'(u)=-(1+o(1))/(2u^2 log u) and is eventually strictly decreasing. If p<q share a window, 0<T(p)-T(q)<t_p-s_p. For any fixed delta>0, q>=(1+delta)p would instead force a difference at least of order 1/(p log p); hence q/p tends to one uniformly along overlapping pairs. The derivative is then uniform on [p,q], giving the stated diameter. Strict increase of fixed-prime Q from a=1 to a=2 bounds any singleton parameter for that prime away from zero, so singleton primes all diverge uniformly as epsilon decreases to zero. Away from zero the upper bound on Q gives uniformly finite prime support. Large distinct primes differ by at least two, giving eventual uniqueness for 5<kappa<17; taking midpoint parameters gives unbounded endpoints divisible by the chosen primes and proves infinitude. An independent 95-digit finite check based on the binomial expansion of the local integral averages (checks/frozen_checks.py argument 4, checks/4.txt) tested fractional as well as integer kappa, with the expected scaled widths and both overlap/no-overlap at one twin-prime pair. This is a numerical consistency check, not certification of boundaries or an infinite proof.

## originality

PASS

Credit Molnar for the endpoint factorization, tie rule, fixed-real-parameter domain, and local asymptotic determining the window-width coefficient. The exact half-open window for sufficiently large primes is also a short consequence of his local formulas and bound, not credited here as a standalone novel result. The distinct supported contribution is the joint-prime localization at one common parameter and the resulting bounded support and eventual multiplicity law. The strongest inspected prior prime-support theorem controls a different, much wider range and does not supply this bound; the new comparison combines local width with the derivative in the prime variable.

## value

PASS

The common-parameter support problem is natural immediately above the known transition at kappa=5. Replacing coarse prime-range information by a constant-diameter cluster restriction determines a bounded multiplicity for the whole family and proves an infinite exactly-one regime with an explicit endpoint of the guaranteed range. This is meaningful information on the canonical extremizers, not a new Robin inequality or a claim of sharpness at kappa=17.

The dated certificate retains the supplied scientific assessment, sources and limitations.
