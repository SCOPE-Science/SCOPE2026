# Exact gcd law for degrees of three-dimensional coincident root loci
## Finding
For an integer \(d\ge3\), let \(\mathcal P_3(d)\) be the set of partitions
\[
\lambda=(a,b,c),
\qquad
1\le a\le b\le c,
\qquad
a+b+c=d,
\]
with exactly three parts. Let
\[
\Delta_\lambda\subset\mathbb P(\operatorname{Sym}^d\mathbb C^2)
\]
be the corresponding coincident root locus: the closure of binary forms with three roots having multiplicities \(a,b,c\). It has dimension \(3\).

Define the common degree divisor
\[
G_d=\gcd_{\lambda\in\mathcal P_3(d)}\deg(\Delta_\lambda).
\]

Then
\[
\boxed{G_d=2^{\alpha(d)}3^{\beta(d)}},
\]
where
\[
\alpha(d)=
\begin{cases}
0,&d\text{ odd},\\
1,&d\equiv0\pmod4,\\
2,&d\equiv2\pmod4,
\end{cases}
\]
and
\[
\beta(d)=
\begin{cases}
0,&\nu_3(d)=1,\\
1,&\nu_3(d)\ne1.
\end{cases}
\]

Equivalently, no prime greater than \(3\) divides every three-dimensional coincident-root-locus degree. The common factor \(3\) disappears exactly when \(3\) divides \(d\) but \(9\) does not. The exact common power of \(2\) is \(1\), \(2\), or \(4\) according as \(d\) is odd, divisible by \(4\), or congruent to \(2\) modulo \(4\).

## Assumptions and scope
The base field is \(\mathbb C\). Degrees are projective degrees in the standard projective space of binary forms
\[
\mathbb P(\operatorname{Sym}^d\mathbb C^2).
\]

The family is restricted to partitions of length exactly \(3\). If \(e_j\) denotes the number of parts of \(\lambda\) equal to \(j\), Hilbert's degree formula is
\[
\deg(\Delta_\lambda)
=
\frac{3!}{\prod_j e_j!}\prod_j j^{e_j}.
\]

Thus, for a three-part partition, the degree has one of three forms:
\[
6abc
\]
when the parts are distinct,
\[
3a^2b
\]
when the repeated part is \(a\), and
\[
a^3
\]
for the equal partition \((a,a,a)\).

## Proof
First, no common prime greater than \(3\) can occur.

For \(d\ge4\), the partition
\[
(1,1,d-2)
\]
has degree
\[
3(d-2).
\]
For \(d=5\), the partition \((1,2,2)\) has degree \(12\). For \(d\ge6\), the partition
\[
(1,2,d-3)
\]
has degree
\[
12(d-3).
\]
Hence, for \(d\ge6\),
\[
G_d\mid
\gcd\!\bigl(3(d-2),12(d-3)\bigr)
=
3\gcd(d-2,4).
\]
Therefore
\[
G_d\mid12.
\]
The cases \(d=3,4,5\) give \(G_d=1,6,3\), respectively, so they also have no common prime greater than \(3\).

We now determine the exact \(2\)-adic valuation.

If \(d\) is odd, then
\[
\deg(\Delta_{(1,1,d-2)})=3(d-2)
\]
is odd. Therefore
\[
\nu_2(G_d)=0.
\]

Suppose
\[
d\equiv0\pmod4.
\]
Every degree is even. Indeed, a distinct-part degree \(6abc\) is even. A two-equal degree \(3a^2b\) could be odd only if both \(a\) and \(b\) were odd, but then \(2a+b\) would be odd. An all-equal degree \(a^3\) has \(d=3a\), and \(4\mid d\) forces \(a\) even. Thus \(2\mid G_d\). On the other hand,
\[
3(d-2)
\]
has exactly one factor of \(2\), since \(d-2\equiv2\pmod4\). Hence
\[
\nu_2(G_d)=1.
\]

Finally suppose
\[
d\equiv2\pmod4.
\]
Every degree is divisible by \(4\). A distinct-part degree \(6abc\) has at least one even part because the sum of three odd integers is odd, so it has at least two factors of \(2\). For a two-equal degree \(3a^2b\), the relation
\[
2a+b=d
\]
forces \(b\) even. If \(a\) is even then \(a^2\) contributes at least two factors of \(2\); if \(a\) is odd then \(b\equiv0\pmod4\). For the all-equal case, \(d=3a\) and \(d\equiv2\pmod4\) imply \(a\equiv2\pmod4\), so \(a^3\) is divisible by \(8\). Thus \(4\mid G_d\). For every such \(d\ge6\),
\[
\deg(\Delta_{(1,2,d-3)})=12(d-3),
\]
and \(d-3\) is odd, so this degree has exactly two factors of \(2\). Therefore
\[
\nu_2(G_d)=2.
\]

It remains to determine the common power of \(3\).

If
\[
\nu_3(d)=1,
\]
then the equal partition
\[
\left(\frac d3,\frac d3,\frac d3\right)
\]
exists and has degree
\[
\left(\frac d3\right)^3,
\]
which is not divisible by \(3\). Hence
\[
\nu_3(G_d)=0.
\]

Assume now
\[
\nu_3(d)\ne1.
\]
If \(3\nmid d\), no equal partition exists, so every three-part degree carries the coefficient \(3\) or \(6\). If \(9\mid d\), the equal partition has degree \((d/3)^3\), which is divisible by \(3\), while every non-equal degree again carries a coefficient divisible by \(3\). Thus every degree is divisible by \(3\).

The common exponent is exactly one. If \(3\nmid d\) and \(d\equiv1\pmod3\), then
\[
3(d-2)
\]
has exactly one factor of \(3\). If \(3\nmid d\) and \(d\equiv2\pmod3\), then for \(d\ge5\) the degree of \((1,2,d-3)\) has exactly one factor of \(3\). If \(9\mid d\), then
\[
3(d-2)
\]
again has exactly one factor of \(3\). Therefore
\[
\nu_3(G_d)=1.
\]

Since no prime greater than \(3\) can divide \(G_d\), the stated formula follows.

## Verification
The bundled checker enumerates every three-part partition for all
\[
3\le d\le500,
\]
computes each degree directly from Hilbert's formula, takes the exact integer gcd, and compares it with the closed formula for \(G_d\).

The checker also verifies the special witness degrees used in the proof and records the total number of partitions tested.

This finite computation is regression evidence only. The theorem for all \(d\ge3\) is established by the symbolic divisibility argument above.

## Relationship to prior work
Fehér, Némethi, and Rimányi study coincident root loci as invariant subvarieties of the space of binary forms. Their paper records Hilbert's degree formula and develops the substantially richer equivariant Poincaré-dual theory of these loci.

Lee and Sturmfels later use the same multiple-root-locus framework in their study of projective duality, conormal varieties, real-rank boundaries, and Euclidean-distance degrees. Their paper again invokes Hilbert's formula for individual multiple-root-locus degrees.

The result here concerns a different invariant: the gcd of the degrees of all length-three strata at fixed binary degree. Targeted searches for common divisors, divisibility, gcds, and congruence classifications of coincident-root-locus degrees did not locate this uniform two-prime formula.

## Limitations
The theorem treats only partitions of length \(3\). Higher fixed lengths have richer symmetry-factor arithmetic and are not covered here.

The result concerns projective degree, not dual degree, Euclidean-distance degree, or the full equivariant class.

The originality check cannot exclude an unindexed arithmetic observation in older invariant-theory literature; the main archival and later multiple-root-locus sources inspected do not state the gcd classification.

## References
L. M. Fehér, A. Némethi, and R. Rimányi, *Coincident root loci of binary forms*, arXiv:math/0311312, first submitted 18 November 2003; Michigan Mathematical Journal 54 (2006), 375--392.

H. Lee and B. Sturmfels, *Duality of Multiple Root Loci*, arXiv:1508.00202, first submitted 2 August 2015; Journal of Algebra 446 (2016), 499--526.
