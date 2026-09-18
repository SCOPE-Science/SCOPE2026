# Locally finite Schreier multilinear algebras collapse over finite fields

## Statement

Let \(k\) be a finite field, and let \(\mathcal V\) be a nontrivial locally finite
variety whose language contains the usual \(k\)-vector-space operations. Assume that
every additional basic operation of arity at least two is \(k\)-multilinear.

If \(\mathcal V\) is a Schreier variety, then every additional basic operation of
arity at least two is identically zero.

Consequently, if the only additional operations are \(k\)-multilinear operations of
arity at least two, then

\[
\mathcal V\text{ is Schreier}
\quad\Longleftrightarrow\quad
\mathcal V
\text{ is the variety of }k\text{-vector spaces with all additional operations zero}.
\]

In particular, for a finite field \(k\), the only nontrivial locally finite Schreier
subvariety of \(k\)-algebras with one bilinear multiplication is the zero-product
variety

\[
xy\approx 0.
\]

If a language additionally contains a distinguished unit and requires
\(1x=x=x1\), then there is no nontrivial locally finite Schreier variety of such
unital \(k\)-algebras.

The same vanishing conclusion applies simultaneously to any finite or infinite
family of multilinear products. Thus any locally finite Schreier subvariety of the
usual finite-field versions of associative, commutative, anticommutative, Lie,
Jordan, alternative, pre-Lie, or other multilinear algebra types must have all
higher-arity products zero (subject to the language conventions above).

## Proof

Kearnes, Moorhead, and Szendrei classify nontrivial locally finite Schreier
varieties. Because the present language has the constant \(0\), their
pseudoconstant exception is automatically harmless. Their main theorem says that
there is either

1. a finite group \(G\) such that every algebra in \(\mathcal V\) is polynomially
   equivalent to a \(G\)-set, or
2. a finite field \(F\) such that every algebra in \(\mathcal V\) is polynomially
   equivalent to an \(F\)-vector space.

The first alternative is impossible here. In a \(G\)-set every polynomial operation
depends on at most one variable, apart from constants. On every nonzero
\(k\)-vector space, the basic addition operation \((x,y)\mapsto x+y\) depends
essentially on both variables. Hence \(\mathcal V\) must be in the vector-space
alternative.

Fix \(A\in\mathcal V\), and use an \(F\)-vector-space structure whose polynomial
operations are exactly those of \(A\). Let \(z=0_A\), which need not be the chosen
\(F\)-vector-space origin. If
\(\omega:A^r\to A\) is an additional \(k\)-multilinear basic operation with
\(r\ge2\), then, as a polynomial operation of an \(F\)-vector space, it has affine
form

\[
\omega(x_1,\ldots,x_r)=a+\lambda_1x_1+\cdots+\lambda_rx_r
\]

for some \(a\in A\) and \(\lambda_i\in F\). Multilinearity with respect to the
original \(k\)-vector-space structure gives

\[
\omega(z,\ldots,z,x_i,z,\ldots,z)=z
\]

for every \(x_i\in A\). Since the displayed affine function is constant as \(x_i\)
varies, \(\lambda_i=0\). This holds for every \(i\), so all \(\lambda_i\) vanish.
Evaluating at \((z,\ldots,z)\) then gives \(a=z\). Therefore \(\omega\) is the
zero operation.

Suppose now that there are no additional nullary or unary operations beyond the
usual \(k\)-vector-space language. After the preceding vanishing, every algebra in
\(\mathcal V\) is simply a \(k\)-vector space with zero additional operations.
A nontrivial subvariety of \(k\)-vector spaces is the whole variety: every module
term is a linear combination of its variables, and any nonzero coefficient in an
additional identity would, by setting all other variables to zero, force every
element to vanish. Hence \(\mathcal V\) is exactly the zero-operation variety.

Conversely, the zero-operation variety is locally finite because \(k\) is finite,
and it is Schreier because its subalgebras are precisely vector subspaces; every
vector subspace of a free \(k\)-vector space is free.

For a unital algebra variety, the first part forces multiplication to be zero.
The identity \(1x=x\) then forces \(x=0\), contradicting nontriviality. This proves
the unital corollary.

## Why the finite-field hypothesis matters

The local-finiteness assumption is compatible with nonzero vector spaces only
because \(k\) is finite. Classical work on Schreier varieties of linear
\(\Omega\)-algebras instead largely treats homogeneous identities and, as a broad
classification consequence, infinite base fields. The present statement isolates a
different finite-field rigidity mechanism: once local finiteness and the Schreier
property are imposed together, every genuinely multilinear product disappears,
even when the defining identities are not homogeneous.

For example, this immediately rules out the Schreier property for any nontrivial
locally finite finite-field algebra variety with a nonzero multiplication, including
nonhomogeneous examples such as Boolean-ring-type varieties in characteristic two.

## Relation to prior work

Kearnes, Moorhead, and Szendrei (2026) provide the general classification of locally
finite Schreier varieties used in the proof; the polynomial-equivalence dichotomy is
their result, not claimed here.

Burgin (1974) studies Schreier varieties of linear \(\Omega\)-algebras over
commutative rings under homogeneous identities and obtains a classification over
infinite fields. Lewin (1968) also treats Schreier varieties of linear algebras over
infinite fields. These papers are important prior art for the linear-algebra
setting. The contribution here is the finite-field, locally finite specialization
for arbitrary identities, together with the resulting collapse of all multilinear
operations and the exact zero-product classification.

Recent characteristic-zero work shows that many nonzero-product
Nielsen--Schreier varieties exist when local finiteness is absent, emphasizing that
the collapse above is specific to the locally finite finite-field regime.

## Limitations

Originality is asserted only to the best of our knowledge. The main theorem is a
short but non-obvious specialization of the very recent general classification of
Kearnes--Moorhead--Szendrei. Burgin's 1974 paper is the closest older source; its
published abstract explicitly covers homogeneous identities over commutative rings
and all linear \(\Omega\)-algebra Schreier varieties over infinite fields. Different
terminology or a finite-field corollary inside older linear-algebra literature could
still overlap with part of the statement. No claim is made that the underlying
polynomial-equivalence classification is new.

## References

1. K. A. Kearnes, A. Moorhead, A. Szendrei, *Locally finite Schreier Varieties*,
   arXiv:2609.19651v1 (2026), https://arxiv.org/abs/2609.19651.
2. M. S. Burgin, *Schreier varieties of linear \(\Omega\)-algebras*,
   Math. USSR-Sb. 22 (1974), 561--579,
   https://doi.org/10.1070/SM1974v022n04ABEH001705.
3. J. Lewin, *On Schreier varieties of linear algebras*,
   Trans. Amer. Math. Soc. 132 (1968), 553--562,
   https://doi.org/10.1090/S0002-9947-1968-0224663-5.
4. V. Dotsenko, U. Umirbaev, *An effective criterion for Nielsen--Schreier
   varieties*, Int. Math. Res. Not. 2023 (2023), 20385--20432,
   https://doi.org/10.1093/imrn/rnad092.
