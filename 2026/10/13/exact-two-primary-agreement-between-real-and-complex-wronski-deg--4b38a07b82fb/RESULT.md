# Exact two-primary agreement between real and complex Wronski degrees
## Finding
Let
\[
a\ge b\ge2,
\qquad
a+b\ \text{odd}.
\]
Consider the Pluecker Grassmannian
\[
\operatorname{Gr}(a,a+b).
\]

Let
\[
D_{\mathbb C}(a,b)
\]
be the degree of an equidimensional complex central projection of the Grassmannian, equivalently the degree of the complex Wronski map. Let
\[
D_{\mathbb R}(a,b)
\]
be the absolute topological degree of the real Wronski map.

Then the two degrees have exactly the same two-primary content:
\[
\nu_2\!\left(D_{\mathbb C}(a,b)\right)
=
\nu_2\!\left(D_{\mathbb R}(a,b)\right).
\]

Writing \(s_2(n)\) for the number of ones in the binary expansion of \(n\), their common valuation is
\[
\boxed{
\sum_{j=0}^{b-1}s_2(a+j)
-
\sum_{j=1}^{b-1}s_2(j)
-
s_2(ab)
}.
\]

Equivalently,
\[
\frac{D_{\mathbb C}(a,b)}{D_{\mathbb R}(a,b)}
\]
is a unit in the two-adic numbers.

For \(b=2\), the complex degree is the Catalan number \(C_a\), while the real Wronski degree is \(C_{(a-1)/2}\). Thus every odd \(a\ge3\) satisfies
\[
\nu_2(C_a)
=
\nu_2\!\left(C_{(a-1)/2}\right).
\]

## Assumptions and scope
The ground fields are \(\mathbb C\) and \(\mathbb R\) for the complex and real maps respectively. The Grassmannian is in its Pluecker embedding.

The real topological degree is considered only in the nonzero branch
\[
a+b\ \text{odd}.
\]
In the complementary branch, the real Wronski degree is zero, so an equality of finite two-adic valuations is not meaningful.

By Grassmannian duality, the degrees are symmetric in \(a\) and \(b\); the convention \(a\ge b\) is used only to write the factorial formulas uniformly.

## Proof
Eremenko and Gabrielov record the complex degree
\[
D_{\mathbb C}(a,b)
=
\frac{
1!2!\cdots(b-1)!\,(ab)!
}{
a!(a+1)!\cdots(a+b-1)!
}.
\]

When \(a+b\) is odd, they also identify the absolute real Wronski degree with the rectangular-tableau sign imbalance and give the product formula
\[
D_{\mathbb R}(a,b)
=
\frac{
1!2!\cdots(b-1)!\,
(a-1)!(a-2)!\cdots(a-b+1)!\,
(ab/2)!
}{
(a-b+2)!(a-b+4)!\cdots(a+b-2)!\,
\displaystyle\prod_{t=(a-b+1)/2}^{(a+b-1)/2}t!
}.
\]

Let
\[
F(n)=\nu_2(n!).
\]
Because \(a+b\) is odd, the integers \(a\) and \(b\) have opposite parity, so \(ab\) is even. Put
\[
M=\frac{ab}{2},
\qquad
L=\frac{a-b+1}{2},
\qquad
U=\frac{a+b-1}{2}.
\]

Subtracting the two valuations cancels the common factor
\[
1!2!\cdots(b-1)!.
\]
The factorials
\[
(a-b+1)!,(a-b+2)!,\ldots,(a+b-1)!
\]
form one consecutive block. In the real-degree denominator, the first product contains exactly the odd arguments in this block, while the second product contains the half-arguments corresponding to the even members. Hence
\[
\nu_2(D_{\mathbb C})-\nu_2(D_{\mathbb R})
=
F(2M)-F(M)
-
\sum_{t=L}^{U}\bigl(F(2t)-F(t)\bigr).
\]

For every positive integer \(n\),
\[
F(2n)-F(n)=n.
\]
Indeed, the quotient \((2n)!/n!\) contains exactly one net factor of \(2\) for each integer from \(1\) through \(n\).

Therefore
\[
\nu_2(D_{\mathbb C})-\nu_2(D_{\mathbb R})
=
M-\sum_{t=L}^{U}t.
\]
There are \(b\) terms in the last sum and
\[
L+U=a,
\]
so
\[
\sum_{t=L}^{U}t
=
\frac{b(L+U)}2
=
\frac{ab}{2}
=
M.
\]
Thus
\[
\nu_2(D_{\mathbb C})
=
\nu_2(D_{\mathbb R}).
\]

For the explicit common value, Legendre's formula at \(2\),
\[
F(n)=n-s_2(n),
\]
applied to the complex degree gives
\[
\nu_2(D_{\mathbb C})
=
\sum_{j=0}^{b-1}s_2(a+j)
-
\sum_{j=1}^{b-1}s_2(j)
-
s_2(ab),
\]
because all linear terms cancel.

## Verification
The bundled checker evaluates both factorial formulas exactly for every pair
\[
2\le b\le a\le120,
\qquad
a+b\ \text{odd},
\]
and verifies equality of their two-adic valuations.

It separately evaluates the binary-digit formula for the common valuation and checks the Catalan specialization for every odd
\[
3\le a\le399.
\]

These computations are regression evidence only. The infinite theorem is proved by the factorial-block cancellation above.

## Relationship to prior work
Eremenko and Gabrielov identify the complex Wronski degree with the classical Pluecker degree of the Grassmannian and the real topological degree with the sign imbalance of rectangular standard Young tableaux. They give explicit product formulas for both quantities and prove that the real degree is nonzero exactly when the two rectangle dimensions have odd sum.

The sign-imbalance of Young-diagram posets has a substantial independent combinatorial literature. Later work studies sign imbalance and its extensions to skew shapes, but the inspected sources and targeted searches did not locate a statement comparing the exact two-adic valuation of the rectangular sign imbalance with the cardinality of all rectangular standard tableaux.

The result here is an arithmetic bridge between the two degrees: throughout the entire nonzero real-degree regime, passing from the total complex enumerative count to the signed real topological count removes no additional power of two.

## Limitations
The theorem compares only the prime \(2\). It does not assert equality of odd-prime valuations, and such equality is generally false.

The real Wronski degree vanishes when \(a+b\) is even, so the theorem deliberately excludes that branch.

The proof depends on the explicit product formula for the rectangular sign imbalance. A differently normalized sign convention may change the sign of the topological degree but not its absolute value or two-adic valuation.

There is a residual possibility that the same valuation identity appears in unindexed representation-theoretic or sign-imbalance literature, despite the targeted searches and source inspections reported in the review.

## References
Alex Eremenko and Andrei Gabrielov, *Degrees of real Wronski maps*, arXiv:math/0108133, first submitted 20 August 2001; published in *Discrete and Computational Geometry* 28 (2002), 331--347.

Dennis E. White, *Sign-Balanced Posets*, *Journal of Combinatorial Theory, Series A* 95 (2001), 1--38.

Jonas Sjostrand, *On the sign-imbalance of skew partition shapes*, *European Journal of Combinatorics* 28 (2007), 1582--1594.
