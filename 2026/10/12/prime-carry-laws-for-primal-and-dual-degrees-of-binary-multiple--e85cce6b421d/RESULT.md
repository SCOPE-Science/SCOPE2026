# Prime-carry laws for primal and dual degrees of binary multiple-root loci
## Finding
Let
\[
\lambda=(1^{m_1}2^{m_2}\cdots q^{m_q})
\]
be a partition of an integer \(n\), and put
\[
d=\sum_{j=1}^q m_j.
\]
Thus \(d\) is the number of distinct linear factors of a general binary form in the multiple-root locus
\[
\Delta_\lambda\subset\mathbb P(\operatorname{Sym}^n\mathbb C^2).
\]

For every prime \(p\),
\[
\boxed{
\nu_p(\deg\Delta_\lambda)
=
\frac{\sum_j s_p(m_j)-s_p(d)}{p-1}
+
\sum_jm_j\nu_p(j)
}.
\]
Here \(s_p(a)\) is the sum of the base-\(p\) digits of \(a\). The first summand is the multinomial Kummer carry count: the total carry mass, counted with multiplicity, when the integers \(m_j\) are added in base \(p\).

Consequently,
\[
\boxed{
p\nmid\deg\Delta_\lambda
}
\]
if and only if both of the following hold:

1. every occurring part size \(j\) is prime to \(p\);
2. the addition
\[
\sum_jm_j=d
\]
is carry-free in base \(p\).

Now assume
\[
m_1=0,
\]
so that the projective dual \(\Delta_\lambda^\vee\) is a hypersurface. Define the shifted partition
\[
\lambda^-=(\lambda_1-1,\ldots,\lambda_d-1).
\]
Then
\[
\boxed{
\deg(\Delta_\lambda^\vee)
=
(d+1)\deg(\Delta_{\lambda^-})
}.
\]
Therefore
\[
\boxed{
\nu_p(\deg\Delta_\lambda^\vee)
=
\nu_p(d+1)
+
\frac{\sum_{j\ge2}s_p(m_j)-s_p(d)}{p-1}
+
\sum_{j\ge2}m_j\nu_p(j-1)
}.
\]

Equivalently,
\[
p\nmid\deg\Delta_\lambda^\vee
\]
if and only if:

1. \(p\nmid d+1\);
2. no occurring part size satisfies \(j\equiv1\pmod p\);
3. the multiplicities \(m_2,m_3,\ldots\) add carry-free in base \(p\).

For \(p=2\), this gives particularly concrete parity criteria. The primal degree is odd exactly when all occurring parts are odd and the binary supports of the nonzero multiplicities \(m_j\) are pairwise disjoint. The dual degree is odd exactly when \(d\) is even, all occurring parts are even, and those multiplicity supports are pairwise disjoint.

## Assumptions and scope
The base field is \(\mathbb C\). The multiple-root locus \(\Delta_\lambda\) is the closure of the set of binary forms having distinct roots with multiplicities prescribed by \(\lambda\).

The primal degree formula is Hilbert's classical formula
\[
\deg\Delta_\lambda
=
\frac{d!}{\prod_jm_j!}
\prod_jj^{m_j}.
\]

For \(m_1=0\), Oeding's binary dual-degree formula is
\[
\deg(\Delta_\lambda^\vee)
=
\frac{(d+1)!}{\prod_{j\ge2}m_j!}
\prod_{j\ge2}(j-1)^{m_j}.
\]

The statement does not concern defective duals, so the dual formula is asserted only in the case \(m_1=0\).

## Proof
Hilbert's formula immediately gives
\[
\nu_p(\deg\Delta_\lambda)
=
\nu_p(d!)
-
\sum_j\nu_p(m_j!)
+
\sum_jm_j\nu_p(j).
\]

Legendre's formula,
\[
\nu_p(N!)
=
\frac{N-s_p(N)}{p-1},
\]
and the identity
\[
\sum_jm_j=d
\]
give
\[
\nu_p(d!)
-
\sum_j\nu_p(m_j!)
=
\frac{\sum_js_p(m_j)-s_p(d)}{p-1}.
\]
This is the standard multinomial form of Kummer's theorem: it is the total base-\(p\) carry count in the addition of the multiplicities.

Every summand in the valuation formula is nonnegative. Hence the valuation vanishes exactly when the multinomial addition is carry-free and every occurring part size is prime to \(p\).

For the dual degree, assume \(m_1=0\). Subtracting \(1\) from every part of \(\lambda\) gives a partition \(\lambda^-\) with the same number \(d\) of parts, and with multiplicity of \(r\) equal to \(m_{r+1}\). Hilbert's formula for \(\lambda^-\) gives
\[
\deg\Delta_{\lambda^-}
=
\frac{d!}{\prod_{j\ge2}m_j!}
\prod_{j\ge2}(j-1)^{m_j}.
\]
Comparing this with Oeding's formula yields
\[
\deg(\Delta_\lambda^\vee)
=
(d+1)\deg(\Delta_{\lambda^-}).
\]
Taking \(\nu_p\) and applying the primal formula to \(\lambda^-\) proves the dual valuation identity.

The nondivisibility criterion follows because the three displayed contributions are again nonnegative.

For \(p=2\), carry-free addition of several nonnegative integers is equivalent to pairwise disjoint binary supports. In the primal case, the local factors force every occurring \(j\) to be odd. In the dual case they force every occurring \(j\) to be even, while \(2\nmid d+1\) is equivalent to \(d\) being even.

## Verification
The bundled checker enumerates every integer partition of
\[
1\le n\le28,
\]
reconstructs Hilbert's degree exactly, and compares direct prime-adic valuations with the digit-sum formula for every prime at most \(29\).

For every partition with no part equal to \(1\), it also evaluates Oeding's dual degree, verifies the shifted-partition bridge
\[
\deg(\Delta_\lambda^\vee)=(d+1)\deg(\Delta_{\lambda^-}),
\]
and checks the dual valuation and prime-avoidance criteria.

As an external normalization check, the partition
\[
(6,4,3,3,2)
\]
has
\[
\deg\Delta_\lambda=25920
\]
and
\[
\deg\Delta_\lambda^\vee=21600,
\]
matching the published software documentation for this coincident-root locus.

These finite computations are regression evidence only. The theorem for all partitions and primes is the symbolic consequence of Hilbert's formula, Oeding's formula, and Legendre's formula given above.

## Relationship to prior work
Fehér, Némethi, and Rimányi study coincident root loci in algebraic geometry, explicitly take Hilbert's degree formula as a starting point, and compute stronger equivariant Poincaré-dual classes.

Oeding computes the degree of the dual binary Chow variety when it is a hypersurface. Lee and Sturmfels later state both Hilbert's primal degree formula and Oeding's dual degree formula side by side in their study of multiple-root loci.

Those sources determine the degrees themselves, but the inspected full texts do not state the prime-adic digit-sum formulas, the carry-free divisibility criteria, or the shifted-partition bridge
\[
\deg(\Delta_\lambda^\vee)=(d+1)\deg(\Delta_{\lambda^-}).
\]

Targeted literature searches in coincident-root, multiple-root, Hilbert-degree, prime-divisibility, parity, Kummer, and carry language did not locate an equivalent all-prime statement.

## Limitations
The arithmetic formulas are consequences of known closed degree formulas; they do not compute new defining equations or new geometric components of the loci.

The dual statement applies only when \(m_1=0\), the classical hypersurface case.

The carry interpretation is classical number theory applied to geometric degree formulas, so an older or unindexed arithmetic remark may contain part of the result without coincident-root terminology.

## References
L. M. Fehér, A. Némethi, and R. Rimányi, *Coincident root loci of binary forms*, arXiv:math/0311312, first submitted 18 November 2003; *Michigan Mathematical Journal* 54 (2006), 375--392, DOI 10.1307/mmj/1156345601.

Luke Oeding, *Hyperdeterminants of Polynomials*, arXiv:1107.4659, first submitted 23 July 2011; *Advances in Mathematics* 231 (2012), 1308--1326, DOI 10.1016/j.aim.2012.06.023.

Hwangrae Lee and Bernd Sturmfels, *Duality of Multiple Root Loci*, arXiv:1508.00202, first submitted 2 August 2015; *Journal of Algebra* 446 (2016), 499--526, DOI 10.1016/j.jalgebra.2015.08.029.
