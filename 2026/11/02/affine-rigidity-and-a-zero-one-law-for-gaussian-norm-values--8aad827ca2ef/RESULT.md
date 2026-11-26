# Zero density of positive affine shifts of Gaussian norms in lattice boxes

## Finding

Let \(\mathcal S_2=\{x^2+y^2:x,y\in\mathbb Z\}\). For fixed positive integers \(a,b\), put
\[
G_{a,b}(H)=\#\{(x,y)\in\{0,\ldots,H\}^2:a(x^2+y^2)+b\in\mathcal S_2\}.
\]
Then \(G_{a,b}(H)=o((H+1)^2)\) as \(H\to\infty\).

More precisely, for every prime \(q\equiv3\pmod4\) with \(q\nmid ab\), exactly \(q(q^2-1)\) ordered pairs modulo \(q^2\) give
\(v_q(a(x^2+y^2)+b)=1\). For any finite set \(Q\) of these primes, the fraction avoiding these valuation-one conditions uniformly modulo \(\prod_{q\in Q}q^2\) in each coordinate is exactly
\[
\prod_{q\in Q}(1-q^{-1}+q^{-3}).
\]
The same product is an upper bound on \(\limsup_{H\to\infty}G_{a,b}(H)/(H+1)^2\).

## Scope

The density weights ordered lattice pairs, not distinct Gaussian norm values. The parameters are fixed as the nonnegative integer \(H\) tends to infinity. The local count is only at primes not dividing \(ab\). The product counts survivors of the valuation-one tests, not all pairs with representable output.

## Proof

For an admissible prime \(q\), the equation \(x^2+y^2=-b/a\) over \(\mathbb F_q\) is a nonzero norm fiber in \(\mathbb F_{q^2}=\mathbb F_q[i]\), since \(-1\) is nonsquare. The norm on the multiplicative group is the \((q+1)\)-power map, so the cyclicity of that group gives exactly \(q+1\) solutions. No solution is the zero pair. Write a lift of any solution as \((x+qu,y+qv)\), with \(u,v\) modulo \(q\) and with \(x,y\) fixed representatives. Among the \(q^2\) lifts, divisibility of the output by \(q^2\) imposes one affine linear equation with nonzero coefficient vector \((2ax,2ay)\) modulo \(q\). Exactly \(q\) lifts obey it. The other \(q^2-q\) lifts have valuation one, so in total there are \((q+1)(q^2-q)=q(q^2-1)\) bad pairs out of \(q^4\).

By the two-square criterion, a positive integer with valuation one at such a prime is not in \(\mathcal S_2\). For a fixed finite \(Q\), the Chinese remainder theorem gives the exact surviving fraction displayed above, and the coordinates in the growing boxes become equidistributed modulo this fixed product modulus. This proves the upper bound on the limsup. The reciprocal-prime sum for \(q\equiv3\pmod4\) diverges, and excluding the finitely many primes dividing \(ab\) does not change this. Since \(q^{-1}-q^{-3}\ge(8/9)q^{-1}\), the finite products can be made arbitrarily small. The nonnegative limiting proportion is therefore zero. No moving-modulus equidistribution or infinite independence assumption is needed.

## Relationship to prior work

Matijasevick already classifies affine self-maps of the two-square value set in Proposition 7.10(c) of *Retriangular numbers and affine maps between polygonal numbers* ([arXiv:2610.36284v1](https://arxiv.org/abs/2610.36284v1)); in particular his argument uses a valuation-one obstruction to rule out an everywhere-preserving shift. The finding here is not that classification. It gives the exact frequency of this obstruction on ordered lattice pairs and shows that the shifted pairs that remain representable have density zero. Radomskii's Theorem 1.1 ([arXiv:2604.20653](https://arxiv.org/abs/2604.20653)) concerns gaps for simultaneous primitive two-square values of \(n\) and \(an+b\) under a divisibility restriction. It does not count pairs representing the input norm. The two-square criterion, finite-field norm count, linear lifting and Chinese remainder theorem are standard ingredients. No quantitative decay rate or assertion about density among distinct values is made.

## Verification

The proof covers all positive parameters and all indicated primes. The companion `verify_affine_norms.py` supplies finite checks for fourteen admissible local parameter triples at \(q=3,7,11,19\), and for the simultaneous \(q=3,7\) tests at \(a=b=1\) over the coordinate residues modulo \(441\). Its additional self-map examples are ancillary, not a priority claim. These tests do not prove the limiting statement.
