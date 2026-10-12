# Finite unitriangular groups have an exact realizability dichotomy

## Finding

Let
\[
q=p^f
\]
be a prime power, and let
\[
\mathrm{UT}_n(q)
\]
be the group of upper unitriangular \(n\times n\) matrices over \(\mathbf F_q\).

For every \(n\ge2\),
\[
\boxed{
\mathrm{UT}_n(q)\text{ is the unit group of a finite ring}
}
\]
if and only if one of the following holds:

1. \(p=2\);
2. \(n=2\) and \(p\) is a Mersenne prime.

Thus for every \(n\ge3\),
\[
\boxed{
\mathrm{UT}_n(q)\text{ is realizable}
\iff
q\text{ is even}.
}
\]

When \(q\) is even, there is an explicit realization of the smallest order permitted by the general local-ring bound. Let
\[
N_n(\mathbf F_q)
\]
be the algebra of strictly upper triangular matrices and define
\[
R_{n,q}
=
\mathbf F_2 I_n\oplus N_n(\mathbf F_q)
\subseteq M_n(\mathbf F_q).
\]
Then
\[
\boxed{
R_{n,q}^{\times}=I_n+N_n(\mathbf F_q)=\mathrm{UT}_n(q).
}
\]
Moreover,
\[
|R_{n,q}|=2q^{\binom n2}=2|\mathrm{UT}_n(q)|.
\]
The ring is local, with Jacobson radical
\[
J(R_{n,q})=N_n(\mathbf F_q)
\]
and residue field \(\mathbf F_2\).

For \(n=2\),
\[
\mathrm{UT}_2(q)\cong (\mathbf F_q,+)\cong C_p^f.
\]
Ditor's classification of realizable groups of odd order therefore gives
\[
\boxed{
\mathrm{UT}_2(p^f)\text{ is realizable for odd }p
\iff
p\text{ is Mersenne}.
}
\]
When \(p=2^a-1\) is Mersenne, one concrete realization is
\[
\left(\mathbf F_{2^a}\right)^f,
\]
whose unit group is
\[
C_p^f.
\]

For \(n\ge3\) and odd \(p\), the group \(\mathrm{UT}_n(q)\) is nonabelian, while every realizable finite odd-primary \(p\)-group is elementary abelian. Hence no such group is realizable.

## Assumptions and scope

A finite group is called realizable if it is isomorphic to the unit group of a finite associative ring with identity.

The theorem concerns the standard finite unitriangular groups. The case \(n=1\) is trivial because \(\mathrm{UT}_1(q)\) is the trivial group, which is the unit group of \(\mathbf F_2\).

The result classifies realizability by arbitrary finite rings; commutativity of the realizing ring is not assumed.

## Proof

First assume that
\[
q=2^f.
\]
Let
\[
N=N_n(\mathbf F_q)
\]
be the strictly upper triangular algebra. Since \(N\) is closed under addition and multiplication and is nilpotent, the set
\[
R=\mathbf F_2 I_n\oplus N
\]
is a finite subring of \(M_n(\mathbf F_q)\) with identity \(I_n\).

Every element of \(R\) is uniquely either
\[
X
\]
or
\[
I_n+X,
\qquad X\in N.
\]
Every \(X\in N\) is nilpotent, so it cannot be a unit. Conversely,
\[
(I_n+X)^{-1}
=
I_n-X+X^2-\cdots+(-X)^{n-1},
\]
which belongs to \(R\). Therefore
\[
R^{\times}=I_n+N=\mathrm{UT}_n(q).
\]
The nonunits are exactly \(N\), so \(N\) is the unique maximal ideal. Thus \(R\) is local and
\[
R/N\cong\mathbf F_2.
\]
Since
\[
|N|=q^{\binom n2},
\]
we have
\[
|R|=2q^{\binom n2}=2|\mathrm{UT}_n(q)|.
\]
For a finite \(2\)-group realized in characteristic \(2\), the standard local reduction gives a realizing ring of order \(2|G|\), so this construction meets that general lower-size normalization exactly.

Now let \(q=p^f\) with \(p\) odd.

If \(n=2\), multiplication in \(\mathrm{UT}_2(q)\) is addition of the single upper-right entry, so
\[
\mathrm{UT}_2(q)\cong (\mathbf F_q,+)\cong C_p^f.
\]
Ditor's theorem says that a finite odd \(p\)-group is realizable if and only if it is elementary abelian and \(p\) is a Mersenne prime. Hence \(\mathrm{UT}_2(q)\) is realizable exactly for Mersenne \(p\). If
\[
p=2^a-1,
\]
then
\[
\mathbf F_{2^a}^{\times}\cong C_p,
\]
so the direct product ring
\[
(\mathbf F_{2^a})^f
\]
has unit group \(C_p^f\), giving an explicit realization.

Finally let \(n\ge3\). The matrices
\[
I_n+E_{12}
\qquad\text{and}\qquad
I_n+E_{23}
\]
do not commute, since their products differ by the nonzero \(E_{13}\) term. Thus \(\mathrm{UT}_n(q)\) is a nonabelian finite \(p\)-group. Ditor's odd-order classification, equivalently the later formulation that every realizable finite odd-primary \(p\)-group is elementary abelian, rules out realizability.

This proves the classification.

## Verification

The included replay checks the constructive even-characteristic half directly for
\[
(q,n)=(2,2),(2,3),(2,4),(4,2),(4,3).
\]
It builds the ring
\[
\mathbf F_2I_n\oplus N_n(\mathbf F_q),
\]
checks closure under addition and multiplication, enumerates all ring elements, and verifies by direct multiplication that the units are exactly the matrices \(I_n+X\) with \(X\in N_n(\mathbf F_q)\).

It also verifies the explicit noncommuting pair
\[
I_n+E_{12},\qquad I_n+E_{23}
\]
for odd fields of orders \(3\) and \(5\), confirming the family-side hypothesis used with the odd-primary realizability theorem.

The replay returns `VERIFY_OK`.

Finite computation is not used to prove the infinite classification.

## Relationship to prior work

Lockridge and Terkel study Fuchs' problem for linear groups and determine realizability for several special and affine general linear families. Their paper emphasizes that general linear groups are automatically realizable as matrix-ring unit groups and then asks what survives for closely related linear groups. The inspected full text contains no occurrence of “unitriangular” and no classification of \(\mathrm{UT}_n(q)\).

Chebolu and Lockridge give the decisive odd-primary input: a finite odd \(p\)-group is realizable exactly when it is elementary abelian and \(p\) is Mersenne. They also explicitly record the consequence that no nonabelian odd-primary \(p\)-group is realizable.

Swartz and Werner study realizable \(2\)-groups and show that characteristic-two realizability is subtle in general, especially beyond exponent \(4\). Their inspected full text contains no unitriangular-family theorem. The explicit ring
\[
\mathbf F_2I_n\oplus N_n(\mathbf F_q)
\]
shows that the whole even-field unitriangular family is realizable despite unbounded nilpotency class and, as \(n\) grows, unbounded exponent.

Targeted searches using “unitriangular group,” “Fuchs problem,” “group of units,” \(\mathrm{UT}_n(q)\), characteristic two, and finite-ring formulations did not locate the displayed if-and-only-if classification.

## Limitations

The theorem concerns unitriangular groups over finite fields, not unitriangular groups over arbitrary finite rings.

The odd-characteristic obstruction uses the established classification of realizable groups of odd order; that prior theorem is not reproved here.

The even-characteristic construction proves ordinary realizability, not full realizability in the stronger endomorphism-lifting sense.

Failed searches do not prove novelty.

## References

1. K. Lockridge and J. Terkel, “Fuchs' problem for linear groups,” arXiv:2401.11583v1, first public version 21 January 2024; *Communications in Algebra* 52 (2024), 2892–2902, DOI 10.1080/00927872.2024.2310166. Primary MSC 16U60.
2. S. K. Chebolu and K. Lockridge, “Fuchs' problem for \(p\)-groups,” arXiv:1901.10081v1, first public version 29 January 2019; *Journal of Pure and Applied Algebra* 223 (2019), 4652–4666.
3. E. Swartz and N. J. Werner, “Fuchs' problem for \(2\)-groups,” arXiv:1904.07901v1, first public version 16 April 2019; *Journal of Algebra* 556 (2020), 225–245; corrected in *Journal of Algebra* 608 (2022), 25–36.
