# Unit orbits determine relative rank in finite transformation wreath products

## Statement

Let \((S,Y)\) and \((R,X)\) be finite transformation monoids. Write
\[
H=U(S),\qquad G=U(R),
\]
let
\[
c=\operatorname{rank}(S:H),\qquad r=\operatorname{rank}(R:G),
\]
and let \(o_G(X)\) be the number of \(G\)-orbits on \(X\). For the transformation wreath product \(S\wr_X R=S^X\rtimes R\),
\[
\boxed{
\operatorname{rank}(S\wr_X R:H\wr_X G)
=
r+o_G(X)c.
}
\]

Thus the relative rank is controlled by the orbit decomposition of the **unit group** \(G\), not by transitivity of the whole monoid \(R\).

A recent preprint of Lu [1, Lemma 3.2] asserts, under the weaker assumption that \(R\) is transitive on \(X\), the upper bound
\[
\operatorname{rank}(S\wr_X R:H\wr_X G)\le r+c.
\]
The formula above gives the sharp repair. If \(c>0\), that bound holds exactly when \(G\) is transitive on \(X\). If \(c=0\), it reduces trivially to \(r\).

## Proof

Lu's multiplication convention is
\[
(a,r)(b,t)=((a_i b_{ir})_{i\in X},rt).
\]
By the standard unit calculation, also recorded as [1, Lemma 2.1],
\[
U(S\wr_X R)=H\wr_X G.
\]

### Upper bound

Choose \(a_1,\ldots,a_c\in S\) with
\[
S=\langle H,a_1,\ldots,a_c\rangle
\]
and \(b_1,\ldots,b_r\in R\) with
\[
R=\langle G,b_1,\ldots,b_r\rangle.
\]
For every \(G\)-orbit \(O\subseteq X\), fix \(x_O\in O\). For every \(j\), let
\[
\widehat a_{O,j}\in S^X
\]
have value \(a_j\) at \(x_O\) and identity elsewhere.

The wreath-product units contain \(H^X\) and the coordinate permutations induced by \(G\). Hence conjugating the \(\widehat a_{O,j}\) by units moves their unique nonunit coordinate to any point of the same \(G\)-orbit. Together with \(H^X\), these elements generate all of \(S^X\). Adding
\[
(\bar e,b_1),\ldots,(\bar e,b_r)
\]
generates the right-hand factor \(R\). Therefore
\[
\operatorname{rank}(S\wr_XR:H\wr_XG)
\le r+o_G(X)c.
\]

### Lower bound

We use the elementary finite-monoid fact
\[
uv\in U(M)\quad\Longleftrightarrow\quad u,v\in U(M)
\]
for a finite monoid \(M\).

Let \(Z\) be any relative generating set for \(S\wr_XR\) modulo \(H\wr_XG\), and project to \(R\). Split
\[
Z=Z_{\mathrm{nu}}\sqcup Z_{\mathrm{u}}
\]
according as the \(R\)-component is outside or inside \(G\).

Since the projection of \(H\wr_XG\) is \(G\), the set of nonunit projections of \(Z_{\mathrm{nu}}\) must generate \(R\) modulo \(G\). Hence
\[
|Z_{\mathrm{nu}}|\ge r.
\]

Now consider a word whose \(R\)-component is the identity. Since a product in the finite monoid \(R\) can be a unit only when every factor is a unit, such a word cannot use any element of \(Z_{\mathrm{nu}}\). Thus the whole base monoid \(S^X\times\{e\}\) must already be generated using wreath-product units and \(Z_{\mathrm{u}}\).

For \(a=(a_x)_{x\in X}\in S^X\), define its singular support by
\[
\sigma(a)=\{x\in X:a_x\notin H\}.
\]
For elements whose right components lie in \(G\),
\[
\sigma\big((a,g)(b,h)\big)
=
\sigma(a)\cup \sigma(b)g^{-1}.
\]
This is an equality because, in the finite monoid \(S\), a coordinate product is a unit exactly when both factors are units. Consequently singular support can move within \(G\)-orbits and can grow by unions, but it cannot cancel.

Fix a \(G\)-orbit \(O\) and \(x\in O\). For every \(s\in S\), the base element that has value \(s\) at \(x\) and identity at all other coordinates must be generated. If \(s\notin H\), its singular support is exactly \(\{x\}\). Therefore every nonunit relative generator that contributes to such a word must, after multiplication by units, have singleton singular support contained in \(O\). Generators supported in another \(G\)-orbit cannot contribute, and a generator whose singular support has size greater than one can never be reduced to a singleton.

Normalize an element of \(Z_{\mathrm{u}}\) by multiplying by a wreath-product unit so that its \(R\)-component is the identity. For a fixed orbit \(O\), take the unique nonunit coordinate values of all normalized relative generators having singleton singular support in \(O\). The preceding paragraph, applied to every \(s\in S\), shows that these values together with \(H\) generate \(S\). Hence there must be at least \(c\) such generators for each \(G\)-orbit. The orbit classes are disjoint, so
\[
|Z_{\mathrm{u}}|\ge o_G(X)c.
\]
Combining the two independent lower bounds gives
\[
|Z|\ge r+o_G(X)c,
\]
which proves the formula.

## Explicit counterexample to transitivity of the monoid being sufficient

Let \(X=\{1,2,3\}\). Let
\[
g=(12),\qquad
a:\ 1\mapsto3,\ 2\mapsto3,\ 3\mapsto1,
\]
and set
\[
R=\langle g,a\rangle\le\mathcal T_X.
\]
This monoid has six elements. Its unit group is
\[
G=\{1,g\},
\]
so \(G\) has two orbits, \(\{1,2\}\) and \(\{3\}\). Nevertheless \(R\) itself is transitive: from each point, elements of \(R\) reach all three points. Also
\[
R=\langle G,a\rangle,\qquad \operatorname{rank}(R:G)=1.
\]

Let \(S=\{1,z\}\) be the two-element transformation monoid in which \(z\) is a constant map. Then \(H=U(S)=\{1\}\) and
\[
\operatorname{rank}(S:H)=1.
\]
The theorem gives
\[
\operatorname{rank}(S\wr_XR:H\wr_XG)=1+2\cdot1=3,
\]
whereas the bound in [1, Lemma 3.2] gives \(2\). The compact verification artifact exhaustively computes the relative rank of this 48-element wreath product and obtains \(3\).

## Iterated wreath products

Let finite transformation monoids \((T_i,X_i)\) have unit groups \(G_i\). Define
\[
c_i=\operatorname{rank}(T_i:G_i),\qquad
o_i=o_{G_i}(X_i).
\]
Set
\[
V_1=T_1,\qquad
V_i=T_i\wr V_{i-1},
\]
with the usual imprimitive action on
\[
\Omega_i=X_i\times\cdots\times X_1,
\]
and let \(W_i=U(V_i)\).

The \(W_i\)-orbits on \(\Omega_i\) are obtained by choosing independently a \(G_j\)-orbit in every coordinate. Hence
\[
o_{W_i}(\Omega_i)=\prod_{j=1}^i o_j.
\]
Applying the one-step theorem recursively yields
\[
\boxed{
\operatorname{rank}(V_n:W_n)
=
\sum_{i=1}^n
c_i\prod_{j=1}^{i-1}o_j.
}
\]

This formula requires no transitivity assumption on the \(T_i\).

It also gives a counterexample under the exact hypotheses used in [1, Section 3]. Take \(T_1=R\) from the preceding example and \(T_2=\mathcal T_2\), the full transformation monoid on two points. Both monoids are transitive and both have relative rank \(1\) modulo their unit groups. But \(G_1\) has two orbits, so
\[
\operatorname{rank}(T_2\wr T_1:U(T_2\wr T_1))
=
1+2\cdot1=3,
\]
not \(2\). Thus the upper bound in [1, Lemma 3.4] and the equality in [1, Lemma 3.8] are false for the stated general class.

The main theorem of [1] is not contradicted by this correction. Its factors are full transformation monoids or symmetric groups, whose unit groups are symmetric groups acting transitively. Therefore every \(o_i=1\), and the weighted formula reduces to the unweighted sum used in that specialization.

## Verification

`artifacts/check_counterexample.py` exhaustively forms the six-element monoid \(R\), the 48-element wreath product \(S\wr_XR\), its two-element unit group, and searches relative generating sets. It returns relative rank \(3\), agreeing with the orbit formula and contradicting the transitivity-only bound \(2\). The recorded output is in `artifacts/verification.txt`.

## Scope and limitations

The theorem is stated for finite transformation monoids. Finiteness is used essentially in the support argument through the fact that a product is a unit only when every factor is a unit. No corresponding claim is made here for arbitrary infinite monoids.

The originality claim is restricted to the exact orbit-weighted relative-rank formula, its iterated version, and the correction of the general intermediate lemmas in [1]. Wreath-product structure, unit-group structure, relative rank, and the special full-transformation/symmetric cases are prior art.

## References

1. Jiaping Lu, *Generation of Iterated Wreath Products Constructed from Full Transformation Monoids and Symmetric Groups*, arXiv:2609.20521v1 (2026). https://arxiv.org/abs/2609.20521v1
2. João Araújo and Csaba Schneider, *The rank of the endomorphism monoid of a uniform partition*, Semigroup Forum 78 (2009), 498–510. https://doi.org/10.1007/s00233-008-9122-0
3. Jiaping Lu, *Generation of wreath products and their generalisation*, PhD thesis, University of St Andrews (2026). https://doi.org/10.17630/sta/1582
4. Alonso Castillo-Ramirez and Ramón H. Ruiz-Medina, *The relative rank of the endomorphism monoid of a finite G-set*, Semigroup Forum 106 (2023), 51–66. https://doi.org/10.1007/s00233-023-10340-7
