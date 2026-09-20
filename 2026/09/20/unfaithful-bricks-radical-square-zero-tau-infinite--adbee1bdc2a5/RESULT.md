# Unfaithful bricks over minimal radical-square-zero τ-tilting-infinite algebras

Let $k$ be an algebraically closed field and let $A$ be a basic connected finite-dimensional $k$-algebra that is minimal $\tau$-tilting-infinite and satisfies $\operatorname{rad}^2 A=0$.

Mousavand--Paquette's classification reduces this situation to
\[
A\cong kQ,
\]
where $Q$ is a sink-source orientation of an affine Dynkin diagram. In particular, every arrow joins a source to a sink and there are no paths of length two.

Their 2023 paper asks whether, for a minimal $\tau$-tilting-infinite algebra, nondistributivity is equivalent to the existence of infinitely many unfaithful bricks. The theorem below answers this affirmatively for the complete radical-square-zero class and gives an exact classification of the unfaithful bricks.

## Theorem

Let $A=kQ$ be as above.

1. **Kronecker case $\widetilde A_1$.** If $Q$ is the Kronecker quiver with two parallel arrows, then the unfaithful bricks are exactly:
   - the two vertex simples; and
   - a $\mathbb P^1(k)$-family of sincere bricks of dimension vector $(1,1)$.

   In particular, there are infinitely many unfaithful bricks.

2. **Alternating affine cycle $\widetilde A_{n-1}$, $n\ge4$ even.** If the underlying graph is an $n$-cycle, then there are exactly
   \[
   n^2
   \]
   unfaithful brick isomorphism classes. More precisely, they consist of:
   - $n(n-1)$ nonsincere interval modules, one for each nonempty proper connected vertex interval of the cycle; and
   - exactly $n$ sincere bricks of dimension vector
     \[
     \delta=(1,\ldots,1),
     \]
     each obtained by setting exactly one arrow map equal to zero and every other arrow map nonzero.

   Consequently the remaining one-parameter family of $\delta$-bricks is faithful.

3. **Affine tree types $\widetilde D_n,\widetilde E_6,\widetilde E_7,\widetilde E_8$.** A brick is unfaithful if and only if it is nonsincere. Hence there are only finitely many unfaithful bricks, and every sincere brick--in particular every brick of dimension vector $\delta$--is faithful.

Therefore
\[
A\text{ is nondistributive}
\quad\Longleftrightarrow\quad
Q\text{ is Kronecker}
\quad\Longleftrightarrow\quad
A\text{ has infinitely many unfaithful bricks}.
\]

Thus the Mousavand--Paquette nondistributivity/unfaithful-brick question has an affirmative answer for every minimal $\tau$-tilting-infinite algebra with radical square zero.

## Proof

Write $J=\operatorname{rad}A$. Since $Q$ is sink-source, it has no oriented path of length two, so
\[
A=\bigoplus_{i\in Q_0}ke_i\oplus J,
\qquad
J=\bigoplus_{\alpha\in Q_1}k\alpha,
\qquad J^2=0.
\]

We repeatedly use two elementary observations.

### Lemma 1: annihilators of sincere modules

If $M$ is sincere, then
\[
\operatorname{ann}_A(M)\subseteq J.
\]
Indeed, if
\[
x=\sum_i\lambda_i e_i+r\in\operatorname{ann}_A(M),\qquad r\in J,
\]
then for every vertex $i$ the diagonal block $e_i x e_i$ equals $\lambda_i e_i$ because there are no loops. Since $e_iM\ne0$, annihilation forces $\lambda_i=0$.

If, moreover, $Q$ has no parallel arrows, then for every sincere $M$
\[
\operatorname{ann}_A(M)=
\bigoplus_{\substack{\alpha\in Q_1\\M_\alpha=0}} k\alpha.
\]
This is because the arrow spaces $e_{t(\alpha)}Je_{s(\alpha)}$ are one-dimensional and distinct arrows lie in distinct source-target blocks. Thus a linear combination of arrows can annihilate $M$ only componentwise.

### Lemma 2: a zero bridge decomposes a sincere representation

Suppose the underlying graph of $Q$ is a tree and $M$ is sincere. If some arrow $\alpha$ has $M_\alpha=0$, deleting the underlying edge of $\alpha$ separates the tree into two nonempty components. Since all vertex spaces are nonzero, restricting $M$ to those two components gives two nonzero subrepresentations whose direct sum is $M$. Hence a sincere indecomposable representation of an oriented tree has every arrow map nonzero.

We now treat the affine diagrams separately.

### 1. Kronecker

Let the arrows be $\alpha,\beta:1\to2$. Every nonsincere brick is a vertex simple: a representation supported at only one vertex is a vector space over $k$, and its endomorphism ring is $k$ only in dimension one.

Now let $M$ be sincere and unfaithful. By Lemma 1,
\[
0\ne\operatorname{ann}_A(M)\subseteq k\alpha\oplus k\beta.
\]
It cannot equal all of $k\alpha\oplus k\beta$, since then both arrow maps vanish and a sincere representation splits as the direct sum of its two vertex parts. Hence the annihilator is a line $L$ in the two-dimensional arrow space.

The quotient $A/L$ is the path algebra of the Dynkin quiver $A_2$. Since $M$ is a sincere brick over this quotient, it must be the unique sincere indecomposable $A_2$-module, with dimension vector $(1,1)$. Conversely, every $(1,1)$ representation given by a nonzero scalar pair
\[
(a,b)=(M_\alpha,M_\beta)
e(0,0)
\]
is a brick, and
\[
\operatorname{ann}_A(M)\cap J
=
\{x\alpha+y\beta:xa+yb=0\},
\]
a one-dimensional subspace. Isomorphism classes are parametrized by $[a:b]\in\mathbb P^1(k)$.

This proves the Kronecker classification.

### 2. Alternating affine cycles

Now assume the underlying graph is a cycle $C_n$. A sink-source orientation exists exactly when $n$ is even.

First consider a nonsincere indecomposable representation $M$. Its vertex support is connected, hence is a nonempty proper connected interval of the cycle. Such a support is a Dynkin graph $A_r$. The only indecomposable with all vertices of that support nonzero and compatible with a thin connected support is the interval module: every nonzero vertex space is one-dimensional and every arrow internal to the interval acts by a nonzero scalar, which can be normalized to $1$. It is a brick. Conversely, every such interval is annihilated by every omitted vertex idempotent and is therefore unfaithful.

There are $n$ cyclic intervals of each length $1,\ldots,n-1$, hence exactly
\[
n(n-1)
\]
nonsincere bricks.

Now let $M$ be sincere and unfaithful. By Lemma 1 and the absence of parallel arrows, some arrow map is zero. If two distinct arrow maps were zero, deleting those two underlying edges would disconnect the cycle into two nonempty components, and $M$ would decompose accordingly. Thus a sincere brick can have at most one zero arrow.

Fix an arrow $\gamma$. After imposing $M_\gamma=0$, the representation factors through the quotient obtained by deleting $\gamma$, whose underlying graph is Dynkin $A_n$. A sincere indecomposable representation of $A_n$ is unique and has dimension vector $(1,\ldots,1)$; equivalently, all remaining arrow maps are nonzero. It is a brick. Thus there is exactly one sincere unfaithful brick for each choice of $\gamma$, and therefore exactly $n$ of them.

Adding the nonsincere bricks gives
\[
n(n-1)+n=n^2.
\]

The standard homogeneous family of affine regular-simple bricks has dimension vector $\delta=(1,\ldots,1)$. Exactly the $n$ members just described are unfaithful, so all remaining members are faithful.

### 3. Affine trees

Assume the underlying graph is one of $\widetilde D_n,\widetilde E_6,\widetilde E_7,\widetilde E_8$. Every nonsincere module is unfaithful because an omitted vertex idempotent lies in its annihilator.

Conversely, let $M$ be a sincere brick. Since a brick is indecomposable, Lemma 2 shows that every arrow map is nonzero. There are no parallel arrows, so Lemma 1 gives
\[
\operatorname{ann}_A(M)=0.
\]
Thus every sincere brick is faithful.

It remains to see that there are only finitely many nonsincere bricks. The support of an indecomposable representation is connected. Every proper connected subgraph of an affine Dynkin tree is a finite Dynkin diagram, hence has only finitely many indecomposable representations. There are only finitely many proper connected subgraphs. Therefore the set of nonsincere bricks is finite.

Since every affine imaginary-root brick of dimension $\delta$ is sincere, every such brick is faithful in the affine-tree cases.

### 4. Distributivity

For Kronecker, every one-dimensional subspace of the two-dimensional arrow space $J$ is a two-sided ideal because $J^2=0$ and the two arrows have the same source and target. Since $k$ is infinite, this gives infinitely many ideals. By Jans's theorem, a finite-dimensional algebra is distributive if and only if it has only finitely many two-sided ideals. Hence the Kronecker algebra is nondistributive.

For every other sink-source affine Dynkin quiver in the theorem there are no parallel arrows. We show directly that $A$ has only finitely many two-sided ideals. Let $I\triangleleft A$. If an element
\[
x=\sum_i\lambda_i e_i+r\in I,\qquad r\in J,
\]
has $\lambda_i\ne0$, then
\[
e_i x e_i=\lambda_i e_i\in I,
\]
so $e_i\in I$. Meanwhile
\[
I\cap J=\bigoplus_{\alpha\in S}k\alpha
\]
for some subset $S\subseteq Q_1$, because multiplication by the primitive idempotents isolates every one-dimensional arrow block. Thus an ideal is determined by finitely many choices of vertex idempotents and arrow spaces, subject only to the obvious incidence closure conditions. In particular there are finitely many ideals, so $A$ is distributive by Jans's theorem.

Combining this with the brick classification proves
\[
A\text{ nondistributive}
\iff Q\text{ Kronecker}
\iff A\text{ has infinitely many unfaithful bricks}.
\]

## Context and relation to prior work

Adachi characterized $\tau$-tilting finiteness for radical-square-zero algebras using separated quivers. Mousavand--Paquette sharpened the minimal case: a minimal $\tau$-tilting-infinite algebra with radical square zero is the path algebra of a sink-source affine Dynkin quiver. They also observed that affine path algebras have one-parameter families of bricks of fixed length and noted that all regular bricks over the Kronecker algebra are unfaithful.

Their paper asks whether a minimal $\tau$-tilting-infinite algebra is nondistributive exactly when it possesses infinitely many unfaithful bricks. The theorem above settles that question for the entire radical-square-zero subclass, and adds the exact $n^2$ count for affine cycles together with the faithful/unfaithful dichotomy for sincere bricks in affine tree types.

The proof also separates two mechanisms that can create annihilators. With no parallel arrows, faithfulness of a sincere representation reduces to whether any individual arrow acts as zero. Parallel arrows create a different phenomenon: a nontrivial linear combination of nonzero arrow maps may vanish, and this is exactly what generates the projective family of unfaithful Kronecker bricks.

## Limitations

The result concerns minimal $\tau$-tilting-infinite algebras satisfying $\operatorname{rad}^2A=0$. It does not settle the Mousavand--Paquette question for arbitrary minimal $\tau$-tilting-infinite algebras.

Originality is asserted only to the best of our knowledge. The classification is elementary once the sink-source affine-Dynkin reduction is combined with standard quiver-representation facts, so an unindexed or differently phrased prior observation remains a meaningful risk. No independent validation, formal verification, or peer review is asserted.

## References

1. K. Mousavand and C. Paquette, *Minimal (τ-)tilting infinite algebras*, Nagoya Math. J. **249** (2023), 119--148. https://doi.org/10.1017/nmj.2022.28
2. T. Adachi, *Characterizing τ-tilting finite algebras with radical square zero*, Proc. Amer. Math. Soc. **144** (2016), 4673--4685. https://doi.org/10.1090/proc/13162
3. J. P. Jans, *On the indecomposable representations of algebras*, Ann. of Math. (2) **66** (1957), 418--429. https://doi.org/10.2307/1969899
4. W. Crawley-Boevey, *Regular modules for extended Dynkin quivers*, lecture notes, Section 3.7. https://www.math.uni-bielefeld.de/~wcrawley/17noncommalg2/Noncommutative%20Algebra%202%20v4.pdf
5. Y. A. Drozd, *On representations of algebras with radical square zero*, arXiv:2602.14171 (2026). https://arxiv.org/abs/2602.14171
