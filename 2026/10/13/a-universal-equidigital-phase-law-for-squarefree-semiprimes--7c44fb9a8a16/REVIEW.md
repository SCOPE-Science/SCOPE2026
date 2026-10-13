# Review

## Correctness
PASS. For distinct primes with base-\(B\) digit lengths \(a,b\), the product
lies between \(B^{a+b-2}\) and \(B^{a+b}\), so it has exactly \(a+b-1\) or
\(a+b\) digits, while its squarefree factorization has exactly \(a+b\) digits.
This gives the exact threshold
\[
pq\ge B^{a+b-1}.
\]
The prime number theorem gives uniform limiting empirical measure on each
normalized digit block \([1,B]\). Product measure then gives uniform area on
the square, the boundary \(uv=B\) has area zero, and the area integral is
\[
B(B-1-\log B).
\]
When the two blocks coincide, deleting \(p=q\) is asymptotically negligible.

## Originality
PASS. The foundational Pinch paper contains the product digit inequalities,
general constructions of squarefree economical/extravagant numbers, and
finite global distribution data, but no semiprime statement or prime-block
limit. The complete De Koninck--Luca 2005 paper concerns consecutive economical
strings and contains no semiprime, squarefree, or density statement. The later
full distribution paper proves a Gaussian law over all integers and contains
no semiprime occurrence. Exact-database and semantic searches found no
equivalent squarefree-semiprime phase law.

The principal residual risk is the 2006 global counting paper, whose abstract
was available but whose full text was not inspected here; an unindexed short
observation in recreational-number literature is another residual risk.

## Value
PASS. Squarefree semiprimes are the first nontrivial multiplicative layer
beyond primes, and digit blocks are intrinsic to the definition of
equidigitality. The theorem converts the qualitative digit comparison into a
base-dependent limiting law with an explicit constant. It also separates the
semiprime layer sharply from the frugal constructions that dominate much of
the economical-number literature.

Self-review: passed. Independent audit: not yet performed.
