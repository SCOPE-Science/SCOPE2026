# The Hurwitz-to-Chow degree ratio of every Pluecker Grassmannian
## Finding
Let
\[
X=\operatorname{Gr}(k,n),
\qquad
2\le k\le n-2,
\]
be the Grassmannian of \(k\)-dimensional subspaces of \(\mathbb C^n\), in its Pluecker embedding. Put
\[
d=k(n-k)
\]
and let
\[
D=\deg X.
\]
Then the degree of the Hurwitz form of \(X\) is
\[
\operatorname{Hdeg}(X)
=
(k-1)(n-k-1)D.
\]

Equivalently, if
\[
\delta_0(X),\delta_1(X),\ldots
\]
are the polar degrees in the convention
\[
\delta_0(X)=\deg X,
\]
then
\[
\delta_1(X)
=
(k-1)(n-k-1)\delta_0(X).
\]
Thus the first polar-degree ratio is the elementary symmetric factor
\[
\frac{\delta_1(X)}{\delta_0(X)}
=
(k-1)(n-k-1).
\]

The Pluecker degree is
\[
D
=
\frac{(k(n-k))!\prod_{j=1}^{k-1}j!}
{\prod_{j=n-k}^{n-1}j!},
\]
so the Hurwitz degree has the explicit closed form
\[
\operatorname{Hdeg}(\operatorname{Gr}(k,n))
=
(k-1)(n-k-1)
\frac{(k(n-k))!\prod_{j=1}^{k-1}j!}
{\prod_{j=n-k}^{n-1}j!}.
\]

The sectional genus of the Pluecker Grassmannian is
\[
g
=
1+\frac{(k(n-k)-n-1)D}{2}.
\]

In particular,
\[
\operatorname{Hdeg}(X)=D
\]
if and only if
\[
(k,n-k)=(2,2).
\]
Hence, up to the standard duality
\[
\operatorname{Gr}(k,n)\simeq\operatorname{Gr}(n-k,n),
\]
the Klein quadric
\[
\operatorname{Gr}(2,4)
\]
is the unique non-linear Pluecker Grassmannian whose Hurwitz and Chow forms have equal degree. Every other non-linear Pluecker Grassmannian satisfies
\[
\operatorname{Hdeg}(X)\ge2D.
\]

For example,
\[
\operatorname{Gr}(2,4):\quad D=2,\quad \operatorname{Hdeg}=2,
\]
\[
\operatorname{Gr}(2,5):\quad D=5,\quad \operatorname{Hdeg}=10,
\]
\[
\operatorname{Gr}(2,6):\quad D=14,\quad \operatorname{Hdeg}=42,
\]
and
\[
\operatorname{Gr}(3,6):\quad D=42,\quad \operatorname{Hdeg}=168.
\]

## Assumptions and scope
The ground field is \(\mathbb C\). The Grassmannian is embedded by the Pluecker line bundle
\[
\mathcal O_X(1)=\det S^\vee,
\]
where \(S\) is the tautological rank-\(k\) subbundle.

The restriction
\[
2\le k\le n-2
\]
excludes the projective-space cases
\[
\operatorname{Gr}(1,n)\simeq\mathbb P^{n-1}
\]
and their duals, whose projective degree is \(1\) and which fall outside the non-linear hypothesis in the standard Hurwitz-form theorem.

The Hurwitz degree means the degree of the Hurwitz hypersurface in the Pluecker coordinate ring of the Grassmannian parametrizing complementary linear spaces. By the coisotropic-polar correspondence, this is the first polar degree.

## Proof
Let \(S\) and \(Q\) be the tautological subbundle and quotient bundle on
\[
X=\operatorname{Gr}(k,n).
\]
The tangent bundle is
\[
T_X\simeq S^\vee\otimes Q.
\]
Write
\[
H=c_1(\det S^\vee).
\]
From
\[
0\longrightarrow S\longrightarrow\mathcal O_X^{\oplus n}\longrightarrow Q\longrightarrow0
\]
we have
\[
c_1(Q)=H
\]
and
\[
c_1(S^\vee)=H.
\]
Therefore
\[
c_1(T_X)
=
(n-k)c_1(S^\vee)+k\,c_1(Q)
=
nH.
\]
Hence
\[
K_X=-nH.
\]

Take a general complete intersection curve
\[
C=X\cap H_1\cap\cdots\cap H_{d-1}
\]
of \(d-1\) Pluecker hyperplanes. Its degree is
\[
\deg C=H^d=D.
\]
Adjunction gives
\[
K_C
=
\left(K_X+(d-1)H\right)|_C
=
(d-1-n)H|_C.
\]
Taking degrees yields
\[
2g-2
=
(d-1-n)D.
\]
Thus
\[
g
=
1+\frac{(d-n-1)D}{2}.
\]

The general Hurwitz-degree theorem states that for an irreducible projective variety of degree \(D\) and sectional genus \(g\), regular in codimension one,
\[
\operatorname{Hdeg}(X)=2D+2g-2.
\]
The Grassmannian is smooth, so substituting the preceding genus formula gives
\[
\operatorname{Hdeg}(X)
=
2D+(d-1-n)D
=
(d+1-n)D.
\]
Since
\[
d+1-n
=
k(n-k)+1-n
=
(k-1)(n-k-1),
\]
we obtain
\[
\operatorname{Hdeg}(X)
=
(k-1)(n-k-1)D.
\]

The coisotropic-polar theorem identifies the degree of the first coisotropic hypersurface, which is the Hurwitz hypersurface, with
\[
\delta_1(X),
\]
while
\[
\delta_0(X)=D.
\]
This proves the polar-degree ratio.

Finally,
\[
(k-1)(n-k-1)=1
\]
with both factors positive if and only if
\[
k-1=n-k-1=1,
\]
that is,
\[
(k,n)=(2,4)
\]
up to Grassmannian duality. Otherwise the integer factor is at least \(2\).

## Verification
The bundled checker evaluates the hook-length product for the Pluecker degree over
\[
4\le n\le120,
\qquad
2\le k\le n-2.
\]
It verifies Grassmannian duality of the degree, checks that
\[
(k(n-k)-n-1)D
\]
is always even, reconstructs the sectional genus, and confirms
\[
2D+2g-2
=
(k-1)(n-k-1)D.
\]

The checker also reproduces the calibration values
\[
\deg\operatorname{Gr}(2,4)=2,
\quad
\deg\operatorname{Gr}(2,5)=5,
\quad
\deg\operatorname{Gr}(2,6)=14,
\quad
\deg\operatorname{Gr}(3,6)=42.
\]

These finite calculations are regression evidence only. The infinite result follows from the tangent-bundle computation, adjunction, and the general Hurwitz-degree theorem.

## Relationship to prior work
Sturmfels proves that the Hurwitz degree of a projective variety of degree \(D\) and sectional genus \(g\) is
\[
2D+2g-2
\]
under the codimension-one regularity hypothesis, and emphasizes its role in the conditioning of linear-section computations.

Kohn proves that the degree of the \(i\)-th coisotropic hypersurface equals the \(i\)-th polar degree; in particular, the Hurwitz hypersurface has degree
\[
\delta_1.
\]
Her paper also records
\[
\delta_0=\deg X.
\]

The inspected papers formulate these general theorems but do not state the specialization
\[
\delta_1(\operatorname{Gr}(k,n))
=
(k-1)(n-k-1)\delta_0(\operatorname{Gr}(k,n)).
\]
Claim-specific searches for the Hurwitz degree of Pluecker Grassmannians, the first polar-degree ratio, the sectional-genus specialization, and the factor
\[
(k-1)(n-k-1)
\]
did not locate an equivalent statement.

The formula is obtained by combining the general Hurwitz theorem with the intrinsic tangent-bundle geometry of the ordinary Grassmannian, rather than by computing a Hurwitz polynomial.

## Limitations
The statement concerns ordinary Grassmannians in their minimal Pluecker embeddings. It does not assert the same ratio for isotropic Grassmannians, flag varieties, Veronese re-embeddings, or other homogeneous embeddings.

The result determines only the first two polar degrees. Higher polar degrees can contain substantially more information.

The derivation is short once the general Hurwitz-degree theorem and the canonical class of the Grassmannian are combined, so an unindexed source could contain the same specialization even though it was not located in the targeted searches.

## References
Bernd Sturmfels, *The Hurwitz Form of a Projective Variety*, arXiv:1410.6703, first submitted 24 October 2014.

Kathlén Kohn, *Coisotropic Hypersurfaces in Grassmannians*, arXiv:1607.05932, first submitted 20 July 2016.
