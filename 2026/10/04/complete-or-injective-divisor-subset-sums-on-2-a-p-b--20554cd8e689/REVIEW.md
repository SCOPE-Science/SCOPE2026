# Independent mathematical audit

## correctness

PASS

The divisor set of n=2^a p^b partitions into b+1 layers {2^i p^j:0<=i<=a}. Binary uniqueness gives layer digits 0<=c_j<=M=2^(a+1)-1. If p<=M+1, intervals from adding layer j meet because p^j<=1+M(1+...+p^(j-1)); induction fills [0,M(1+...+p^b)]=[0,sigma(n)]. If p>M+1, each digit is <p; ordinary base-p uniqueness makes all divisor subset sums injective, giving exactly (M+1)^(b+1) represented integers and sigma(n)+1-(M+1)^(b+1) omissions. At b=1 this is M(p-M-1)>=M; H_(b+1)-H_b=M[p^(b+1)-(M+1)^(b+1)]>0. All a,b>=1 and odd primes p are covered analytically; finite checker small cases corroborates only.

## originality

PASS

Weingartner restates the Stewart--Sierpinski practical-number iff boundary p<=2^(a+1) for 2^a p^b. That gives complete coverage but does not count distinct subset sums, give collision multiplicities, or assert injectivity on the complementary non-practical side. The new count follows separately from radix uniqueness and is not a corollary of merely knowing impracticality. Nearby Zumkeller and phi-practical records count a different property. Stewart 1954 full text was inaccessible after arXiv/OA search and authorized Oxford reported disconnected VPN; this is a named residual risk, not an automatic O failure.

## value

PASS

At the natural classical practical-number threshold the theorem identifies a sharp collision transition and exact number of representable and missing values over every exponent b. Representational multiplicity is a meaningful invariant of an entire arithmetically defined family, not an arbitrary parameter slice or a mere recalculation of the known practicality test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
