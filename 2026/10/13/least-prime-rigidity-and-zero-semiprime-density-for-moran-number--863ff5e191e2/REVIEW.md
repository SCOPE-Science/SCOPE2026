# Review

## Correctness
PASS. If \(\Omega(n)=2\), the only shapes are \(r^2\) and \(pq\). In the
prime-square case the Moran quotient forces \(S(r^2)=r\); modulo \(9\) and a
monotone digit-length inequality reduce this to \(r\in\{3,19,37\}\), all of
which fail. For distinct primes \(p<q\), the digit sum must be one of the two
prime factors. The branch \(S(pq)=q\) is reduced by the same size bound and a
modulo-\(9\) congruence to four explicit products, all of which fail. Hence
\(S(pq)=p\) exactly. The counting bound then follows uniformly from
\(p=O(\log x)\), a standard upper bound for \(\pi(x/p)\), Mertens' theorem
for prime reciprocals, and Landau's semiprime asymptotic.

## Originality
PASS. The fully inspected 2010 primary paper studies exactly the defining
class and gives constructions, numerical data, and open problems, but targeted
full-text checks find no semiprime or prime-square statement. OEIS A001101 is
the exact sequence database and likewise gives no multiplicative-layer
classification. The 2013 chain paper concerns a different iteration property
according to its available abstract. Indexed semantic searches over semiprime,
prime-square, Niven, and Moran formulations found no result implying the
least-prime rigidity or the zero relative semiprime density.

Residual risk remains because the original 1993 recreational-mathematics
problem was not available in full text and the 2013 chain paper was available
only through its abstract.

## Value
PASS. The definition itself already factors a Moran number as its digit sum
times a prime, so asking how that factorization interacts with the first
nontrivial multiplicative layer is intrinsic rather than arbitrary. The
result closes that entire layer, gives a sharp structural identity for the
digit sum, and turns it into an unconditional zero-density theorem relative to
all semiprimes. This goes beyond bounded enumeration or a reformulation of the
definition.

Self-review: passed. Independent audit: not yet performed.
