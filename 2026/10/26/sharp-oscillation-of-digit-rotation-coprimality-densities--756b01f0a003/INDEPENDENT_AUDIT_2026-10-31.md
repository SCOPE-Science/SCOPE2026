# Independent mathematical audit

## correctness

PASS

For base b>=2, m>=1, rotation satisfies N_{j+1}=bN_j-(b^m-1)a_j. From both divisibilities, G=gcd(all rotations)=gcd(N,(b^m-1)D), D=gcd(digits), so G=1 iff gcd(N,b^m-1)=1 and D=1. Mobius inversion on the m-digit interval bounds the totient approximation error by 2^omega(M)<=2sqrt(M); exceptional D>1 digit strings lie in at most pi(b-1) ceil(b/2)^m configurations. For m=d ell with ell prime>B-1 and B=b^d, every prime divisor of S_ell=(B^ell-1)/(B-1) has order ell and size>=ell+1, making sum reciprocal prime factors o(1). Thus each phi(b^d-1)/(b^d-1) is a subsequential limit, with limsup phi(b-1)/(b-1); taking m multiples of orders modulo all small primes forces liminf zero. The positive subsequential values approach zero, so infinitely many distinct. Independent direct digit-rotation tests checked all tested strings for bases 2..9 and lengths b^m<=100000.

## originality

PASS

OEIS A084433 and A387356 provide direct finite sequences; A287513 asks the strictly stronger pairwise-coprime question. MathPages establishes gcd(N,b^m-1) as one common divisor, not the full gcd with digit-gcd correction nor the asymptotic densities. Published circular-code and digit-reversal results are different objects. The all-base oscillation and error bound were not implied by inspected primary statements.

## value

PASS

The common-gcd-one sequence of all digit rotations is a documented and natural arithmetic object. An explicit all-base quantitative totient density law and sharp nonconvergent extremes (decimal upper 2/3, binary upper 1), plus infinitely many distinct accumulation values, convert a finite digit-sequence curiosity into a precise structural distribution theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
