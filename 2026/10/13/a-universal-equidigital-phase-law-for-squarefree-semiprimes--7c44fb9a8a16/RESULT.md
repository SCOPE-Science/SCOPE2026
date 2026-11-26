# Equidigital proportions in two complete prime digit blocks

## Finding

Fix an integer base \(B\ge2\), and write \(\mathcal P_a(B)=\{p\text{ prime}:B^{a-1}\le p<B^a\}\). Among ordered pairs of distinct primes in \(\mathcal P_a(B)\times\mathcal P_b(B)\), the proportion whose product is equidigital tends, as \(\min(a,b)\to\infty\), to
\[
\rho_B=\frac{B(B-1-\log B)}{(B-1)^2}.
\]
For example, the limiting proportions in bases \(2\) and \(10\) are about \(0.61371\) and \(0.82684\), respectively. The blocks need not have equal lengths. This is a conditional proportion in two complete prime digit blocks, not a natural density of semiprimes ordered by product size.

## Assumptions and known digit criterion

For positive integers let \(\delta_B(m)=\lfloor\log_B m\rfloor+1\). Equidigital means the number and its prime factorization use the same number of digits. Exponents equal to \(1\) are omitted, so for distinct primes of lengths \(a,b\) the factorization uses \(a+b\) digits. Pinch's general product digit bounds and coprime additivity [1, Proposition 2.1(3),(5)] give the elementary criterion used here: the product is equidigital exactly if \(pq\ge B^{a+b-1}\). Indeed, \(B^{a+b-2}\le pq<B^{a+b}\) gives the only two possible digit lengths. In the other case the product has one fewer digit than its factorization. No new result is claimed for this finite criterion.

## Proof of the block limit

Let \(X=B^{a-1}\), \(Y=B^{b-1}\), and \(u=p/X\), \(v=q/Y\). The equidigital condition becomes \(uv\ge B\), with \(u,v\in[1,B)\). For fixed \(1\le s<t\le B\), the prime number theorem gives
\[
\frac{\#\{p\text{ prime}:sX\le p<tX\}}{\#\mathcal P_a(B)}
\longrightarrow\frac{t-s}{B-1}.
\]
In fact the numerator and denominator are asymptotic to \((t-s)X/\log X\) and \((B-1)X/\log X\), respectively; choices of closed endpoints affect counts by at most a constant. The same holds with \(Y,b\). For the product sample before requiring distinctness, rectangle probabilities converge to those of independent uniform coordinates on \([1,B]\) whenever both lengths tend to infinity. The indicator of \(uv\ge B\) is approximable from above and below by grid rectangles with arbitrarily small difference in area, because its boundary has area zero. Hence its probability converges to its normalized area. If \(a\ne b\), distinctness is automatic. When \(a=b\), deleting the diagonal changes any event probability by at most \(1/\#\mathcal P_a(B)\), which tends to zero.

At fixed \(u\) the allowed interval for \(v\) has length \(B-B/u\). The limiting probability is therefore
\[
\frac{1}{(B-1)^2}\int_1^B\left(B-\frac Bu\right)\,du
=\frac{B(B-1-\log B)}{(B-1)^2}.
\]
This derivation uses uniformity in the rescaled linear coordinate, not uniformity of the logarithmic mantissa.

## Verification and prior context

The argument from the prime number theorem and the boundary-area calculation establishes the limit. The packaged `verify.py` compares the elementary digit condition with direct finite counts and illustrates convergence in equal decimal blocks. Its finite counts are not an asymptotic proof. The value here is the quantitative proportion in the two-block sampling regime; the digit inequalities already follow from [1]. Global counts of economical numbers or global distributions of the factorization length concern a different sampling regime.

[1] R. G. E. Pinch, *Economical numbers*, arXiv:math/9802046v1, 1998, Proposition 2.1. https://arxiv.org/abs/math/9802046
