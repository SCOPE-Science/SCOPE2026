# Square legs in primitive Pythagorean triangles: an exact asymptotic and a two-to-one law

## Finding

Write \(P_o(X)\) and \(P_e(X)\) for the numbers of primitive positive integer right triangles, with the legs unordered and the hypotenuse at most real \(X\), whose unique odd leg or unique even leg, respectively, is a positive perfect square. Put
\[
G=\frac{\Gamma(5/4)^2}{\Gamma(3/2)}.
\]
Then, as \(X\to\infty\),
\[
P_o(X)=\frac{\sqrt2 G}{\pi^2}\sqrt X+O\!\left(X^{1/4}\log(2X)\right),\qquad
P_e(X)=\frac{2\sqrt2 G}{\pi^2}\sqrt X+O\!\left(X^{1/4}\log(2X)\right).
\]
A primitive right triangle cannot have both legs square (the classical theorem that two positive fourth powers cannot sum to a square). Thus the number \(P(X)\) of such triangles with **at least one** square leg satisfies
\[
\boxed{P(X)=\frac{3\sqrt2}{\pi^2}\frac{\Gamma(5/4)^2}{\Gamma(3/2)}\sqrt X+O\!\left(X^{1/4}\log(2X)\right)}.
\]
The leading constants are approximately \(0.13283498748960546\), \(0.26566997497921091\), and \(0.39850496246881637\), respectively. In particular, \(P_e(X)/P_o(X)\to 2\) and infinitely many triangles belong to each class.

## Assumptions and scope

All variables describing triangles are positive integers; primitiveness means the greatest common divisor of the three sides is \(1\). Each triangle is counted once, independently of leg order. Square means a positive integer square, not merely a squarefree part. Bounds are on the hypotenuse, not on the perimeter or leg size. The big-O constants are absolute; the statement is asymptotic for real \(X\ge 2\).

Euclid's unique parametrization of a primitive triangle with odd leg \(a\), even leg \(b\), and hypotenuse \(c\) is
\[
(a,b,c)=(m^2-n^2,2mn,m^2+n^2),\quad m>n\ge1,\quad\gcd(m,n)=1,\quad m\not\equiv n\pmod2.
\]

## Proof

**Odd-square branch.** Since \(m\) and \(n\) have opposite parity, \(m-n\) and \(m+n\) are coprime odd positive integers. Hence \(a=(m-n)(m+n)\) is a square precisely when there are unique odd integers \(1\le u<v\), with \(\gcd(u,v)=1\), such that
\[
m-n=u^2,\quad m+n=v^2,\quad m=\frac{u^2+v^2}{2},\quad n=\frac{v^2-u^2}{2}.
\]
Conversely, these conditions yield coprime oppositely-paritied \(m,n\), and every such pair gives a primitive triangle. The hypotenuse becomes \(c=(u^4+v^4)/2\). Thus
\[
P_o(X)=\#\{(u,v)\in\mathbb Z_{>0}^2:\ u<v,\ u,v\text{ odd},\ \gcd(u,v)=1,\ u^4+v^4\le2X\}.
\]

**Even-square branch.** Since \(m,n\) are coprime and one is even, \(b=2mn\) is a square precisely when the unordered pair \(\{m,n\}\) has the form \(\{2u^2,v^2\}\), uniquely with \(u,v\ge1\), \(v\) odd, and \(\gcd(u,v)=1\). The numbers \(2u^2\) and \(v^2\) cannot coincide. Ordering them as \(m>n\) recovers a unique primitive triangle; its hypotenuse is \(c=4u^4+v^4\). Thus
\[
P_e(X)=\#\{(u,v)\in\mathbb Z_{>0}^2:\ v\text{ odd},\ \gcd(u,v)=1,\ 4u^4+v^4\le X\}.
\]

**Lattice estimate.** For a bounded piecewise-smooth region \(R\) in the positive quadrant whose boundary has finite length, and \(t\ge2\), counting integer points in \(tR\) in parity classes and applying Möbius inversion over the **odd** common divisors gives
\[
\begin{aligned}
\#\{(u,v)\in tR\cap\mathbb Z_{>0}^2:\ u,v\text{ odd},\ (u,v)=1\}
  &=\frac{2}{\pi^2}\operatorname{area}(R)t^2+O_R(t\log(2t)),\\
\#\{(u,v)\in tR\cap\mathbb Z_{>0}^2:\ v\text{ odd},\ (u,v)=1\}
  &=\frac{4}{\pi^2}\operatorname{area}(R)t^2+O_R(t\log(2t)).
\end{aligned}
\]
Indeed, the unrestricted odd-odd and odd-second-coordinate grids have leading densities \(1/4\) and \(1/2\), with errors \(O_R(t+1)\). The exact multiplicative factor is
\[
\sum_{\substack{d\ge1\\d\text{ odd}}}\frac{\mu(d)}{d^2}
=\prod_{p\text{ odd prime}}(1-p^{-2})
=\frac{8}{\pi^2}.
\]
Truncate inversion at \(d\ll_R t\); the omitted area sum is \(O_R(t)\), and the boundary errors sum to \(O_R(t\log(2t))\).

Let \(Q=\{(u,v)>0:u^4+v^4\le1\}\). The beta integral gives
\[
\operatorname{area}(Q)=\frac{\Gamma(5/4)^2}{\Gamma(3/2)}=G.
\]
Both quartic regions at unit scale have the same area:
\[
\operatorname{area}\{0<u<v:u^4+v^4\le2\}
=\frac{\sqrt2}{2}G
=\operatorname{area}\{u,v>0:4u^4+v^4\le1\}.
\]
Apply the two lattice estimates to the respective regions, with \(t=X^{1/4}\). Their different parity densities supply exactly the factor \(2\) between the leading coefficients.

Finally, if **both** legs were squares, the Pythagorean equation would give positive integers \(r,s,c\) with \(r^4+s^4=c^2\), contradicting Fermat's classical fourth-power descent theorem. The two counted classes are therefore disjoint, and their asymptotics add.

## Verification

Run `python3 verify_square_legs.py`. This exact integer-arithmetic verifier builds all primitive triangles by Euclid's parametrization and separately by the two quartic parametrizations, checks exact equality of the resulting sets for six hypotenuse bounds up to \(10^7\), and checks nonoverlap. It outputs the branch counts \((1,3),(3,8),(13,27),(42,84),(132,269),(413,839)\). The symbolic lattice estimate and classical descent theorem, not the finite checks, prove the infinite statement.

## Relationship to prior work

Benito and Varona (2002) give asymptotics for primitive triangles with **both legs below a bound**, without a perfect-square restriction. Overmars and Ntogramatzidis (arXiv:1504.03163, submitted 2015-04-01) give a unique odd/even parametrization but no square-leg hypotenuse counting theorem. Zelator (arXiv:0805.1052, submitted 2008-05-07) proves obstructions for legs of the form \(s_1x^2,s_2y^2\) with specific odd squarefree multipliers \(s_1,s_2>1\), not the present unrestricted one-square-leg count. A publisher preview of an AMS chapter on Pythagorean triples (Chapter 4, §4.7, Theorem 4.10) establishes infinitude of each square-leg class by explicit constructions; it does not state a counting asymptotic in the available excerpt. These works motivate the question and supply comparison points; none of the inspected material is asserted to have proved the displayed constants.

## Limitations

The error estimate is elementary and is not claimed optimal. There is no uniformity assertion for varying square-power conditions or for a different height. The novelty comparison is limited to the literature and search records listed in the accompanying review, so an earlier unindexed version cannot be excluded. The verifier is a finite cross-check, not a replacement for the proof.

## References

1. K. H. Zelator, *Two Theorems on the structure of Pythagorean triples and some diophantine consequences*, arXiv:0805.1052v1 (public 2008-05-07), https://arxiv.org/abs/0805.1052.
2. A. Overmars and L. Ntogramatzidis, *A new parameterisation of Pythagorean triples in terms of odd and even series*, arXiv:1504.03163v1 (public 2015-04-01), https://arxiv.org/abs/1504.03163.
3. M. Benito and J. L. Varona, *Pythagorean triangles with legs less than n*, Journal of Computational and Applied Mathematics **143** (2002), 117–126, doi:10.1016/S0377-0427(01)00496-4.
4. Fermat's classical infinite-descent theorem: the equation \(r^4+s^4=c^2\) has no solution in positive integers; see standard treatments of the exponent-four case of Fermat's Last Theorem.
5. *Pythagorean Triples*, AMS publisher preview, Chapter 4, §4.7, Theorem 4.10 (infinitude for odd and even square legs), https://www.ams.org/bookstore/pspdf/clrm-55-prev.pdf. Only the available preview excerpt was accessible for inspection.
