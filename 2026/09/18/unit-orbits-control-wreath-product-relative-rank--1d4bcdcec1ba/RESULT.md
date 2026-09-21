# Unit orbits control relative rank in finite monoid wreath products

## Statement

Let \((S,Y)\) and \((R,X)\) be finite transformation monoids. Write
\[
H=S^\times,\qquad G=R^\times,
\]
and let \(q\) be the number of \(G\)-orbits on \(X\). Set
\[
b=\operatorname{rank}(R:G),\qquad c=\operatorname{rank}(S:H).
\]
For the transformation-monoid wreath product
\[
S\wr_X R=S^X\rtimes R
\]
with unit group \(H\wr_X G\), one has the exact formula
\[
\boxed{
\operatorname{rank}(S\wr_XR:H\wr_XG)=b+qc.
}
\]

Consequently,
\[
\boxed{
\operatorname{rank}(S\wr_XR)
=
\operatorname{rank}(H\wr_XG)+b+qc.
}
\]

Thus the transport parameter relevant to relative generation is not transitivity of the whole monoid \(R\), but the orbit decomposition of its unit group \(G\).

## Proof

Use the right-action convention
\[
(a,r)(b,t)=(a\,b^r,rt),\qquad (b^r)_x=b_{xr}.
\]

A standard finite-monoid fact will be used repeatedly: if a product is a unit, then every factor is a unit. Indeed, if \(uv\) is invertible, then \(u\) is right-invertible and \(v\) is left-invertible; in a finite monoid one-sided invertibility implies invertibility.

### Upper bound

Choose
\[
r_1,\ldots,r_b\in R,\qquad
s_1,\ldots,s_c\in S
\]
such that
\[
R=\langle G,r_1,\ldots,r_b\rangle,\qquad
S=\langle H,s_1,\ldots,s_c\rangle.
\]
Let \(x_1,\ldots,x_q\) be representatives of the \(G\)-orbits on \(X\).

For every \(i\), include the lift
\[
(\bar e,r_i),
\]
where \(\bar e\) is the identity of \(S^X\). For every pair \((j,k)\), include
\[
(u_{j,k},e),
\]
where \(u_{j,k}\) equals \(s_j\) at \(x_k\) and equals \(e\) at every other coordinate.

The subgroup \(H\wr_XG\) transports \(u_{j,k}\) throughout the \(G\)-orbit of \(x_k\). Together with the coordinatewise units \(H^X\), the \(c\) local generators attached to an orbit generate arbitrary \(S\)-entries independently at every coordinate of that orbit. Running over all \(q\) orbits generates the whole base \(S^X\). The \(b\) lifted top generators then generate all of \(R\). Hence
\[
\operatorname{rank}(S\wr_XR:H\wr_XG)\le b+qc.
\]

### Lower bound

Let \(C\) be any relative generating set modulo \(H\wr_XG\). Split it according to whether the \(R\)-component is a unit.

Projection onto \(R\) shows that at least \(b\) elements of \(C\) must have nonunit \(R\)-component.

Now consider elements of \(C\) whose \(R\)-component lies in \(G\). Multiplication on the right by a unit allows each such generator to be normalized to the form \((a,e)\) with \(a\in S^X\).

For \(a\in S^X\), define its singular support
\[
\sigma(a)=\{x\in X:a_x\notin H\}.
\]
If \(g\in G\), then
\[
\sigma(a\,b^g)=\sigma(a)\cup g^{-1}\sigma(b),
\]
because in a finite monoid a product is a unit exactly when both factors are units.

Fix a \(G\)-orbit \(O\) and \(x\in O\). For any \(s\in S\), consider the base element \(\delta_{x,s}\) which equals \(s\) at \(x\) and \(e\) elsewhere. If \(s\notin H\), then
\[
\sigma(\delta_{x,s})=\{x\}.
\]
Any word representing \((\delta_{x,s},e)\) can contain only factors whose top components are units, since its top product is the unit \(e\). Moreover, the support-union identity forces every nonunit base generator occurring in such a word to have singleton singular support contained in \(O\): a defect outside \(O\), or two defects in \(O\), can never disappear.

Let \(D_O\subseteq S\setminus H\) be the set of unique nonunit coordinate values supplied by relative generators with singleton singular support in \(O\). Since every \(\delta_{x,s}\) must be generated,
\[
S=\langle H\cup D_O\rangle.
\]
Therefore \(|D_O|\ge c\). Different \(G\)-orbits require disjoint singleton-support generators, so at least \(qc\) relative generators with unit top component are necessary. Together with the \(b\) generators forced by projection,
\[
\operatorname{rank}(S\wr_XR:H\wr_XG)\ge b+qc.
\]
This proves the formula.

The ordinary-rank formula follows from the standard decomposition
\[
\operatorname{rank}(M)
=
\operatorname{rank}(M:M^\times)+\operatorname{rank}(M^\times)
\]
for a finite monoid \(M\).

## Iterated wreath products

Let \((T_i,X_i)\), \(1\le i\le n\), be arbitrary finite transformation monoids. Let
\[
G_i=T_i^\times,\qquad
c_i=\operatorname{rank}(T_i:G_i),
\]
and let \(p_i\) be the number of \(G_i\)-orbits on \(X_i\).

Define
\[
V_1=T_1,\qquad
V_i=T_i\wr V_{i-1},
\]
with the induced action on
\[
\Omega_i=X_i\times\cdots\times X_1,
\]
and define the unit groups
\[
W_1=G_1,\qquad
W_i=G_i\wr W_{i-1}.
\]
Then
\[
\boxed{
\operatorname{rank}(V_n:W_n)
=
\sum_{i=1}^n
c_i\prod_{j=1}^{i-1}p_j.
}
\]

Indeed, the number of \(W_i\)-orbits on \(\Omega_i\) is
\[
\prod_{j=1}^i p_j:
\]
two points \((x,\omega)\) and \((y,\nu)\) lie in the same \(W_i\)-orbit exactly when \(x,y\) lie in the same \(G_i\)-orbit and \(\omega,\nu\) lie in the same \(W_{i-1}\)-orbit. Applying the two-factor formula recursively gives the displayed sum.

This removes both the transitivity assumption and the restriction
\(\operatorname{rank}(T_i:G_i)\le1\) from the relative-rank calculation.

## Correction to arXiv:2609.20521v1

Lu's Lemma 3.2 states that if \(R\) is transitive on \(X\), then
\[
\operatorname{rank}(S\wr R:H\wr G)
\le
\operatorname{rank}(R:G)+\operatorname{rank}(S:H).
\]
The proof moves a local base generator from one coordinate to all others using elements of \(R\). This step is not valid when the desired final element has unit top component: every factor in a word whose top product is a unit must itself have unit top component. Hence only \(G\), not arbitrary \(R\), can transport a local defect while returning to the base.

A smallest convenient counterexample is as follows. Let \(X=Y=\{0,1\}\),
\[
S=\{\mathrm{id},c_0\},
\qquad
R=\{\mathrm{id},c_0,c_1\},
\]
where \(c_i\) is the constant map with value \(i\). Then \(R\) is transitive on \(X\), while
\[
H=G=\{\mathrm{id}\},
\quad
\operatorname{rank}(S:H)=1,
\quad
\operatorname{rank}(R:G)=2,
\quad
q=2.
\]
Therefore
\[
\operatorname{rank}(S\wr R:H\wr G)=2+2\cdot1=4,
\]
whereas Lemma 3.2 predicts an upper bound of \(3\). The accompanying verification script exhaustively checks that the 12-element wreath product has relative rank \(4\).

The same issue affects the more general Lemma 3.8 as stated. For example, on \(X_1=\{0,1,2\}\), let
\[
G_1=\langle(0\,1)\rangle
\]
and let \(T_1\) be generated by \(G_1\) and the nonunit map
\[
a=(2,2,0).
\]
Then \(T_1\) is transitive, \(G_1\) has two orbits, and
\[
\operatorname{rank}(T_1:G_1)=1.
\]
Take \(T_2\) to be the full transformation monoid on two points. It is transitive and has relative rank \(1\) modulo its symmetric-group units. For
\[
V=T_2\wr T_1,\qquad W=G_2\wr G_1,
\]
the formula above gives
\[
\operatorname{rank}(V:W)=1+2\cdot1=3,
\]
whereas Lemma 3.8 gives \(2\).

The main Theorem 1.1 of arXiv:2609.20521v1 is not affected: every full transformation monoid and every symmetric group used there has a transitive unit group. Hence every \(p_i=1\), and the corrected iterated formula reduces to the relative-rank contribution used in the main theorem.

## Literature and originality boundary

Lu's paper introduced the iterated transformation-monoid setup and proved the advertised rank formula for iterated wreath products of full transformation monoids and symmetric groups. Araújo and Schneider previously computed the rank of the endomorphism monoid of a uniform partition, using the special wreath product of full transformation monoids. Araújo, Bentz, Mitchell and Schneider later treated arbitrary partitions.

The novelty claim here is restricted to:

1. the exact general two-factor formula
   \[
   \operatorname{rank}(S\wr_XR:H\wr_XG)
   =
   \operatorname{rank}(R:G)
   +(\#\,G\backslash X)\operatorname{rank}(S:H);
   \]
2. the orbit-weighted iterated formula;
3. the explicit counterexamples to Lemmas 3.2 and 3.8 of arXiv:2609.20521v1; and
4. the identification of transitivity of the unit group, rather than the whole transformation monoid, as the relevant transport condition.

Targeted searches for combinations of "relative rank", "wreath product", "group of units", and "orbits" did not locate this formula or an equivalent statement. The 2009 and 2015 partition papers are the closest prior rank literature found; their publicly indexed descriptions concern full transformation monoids and partition-preserving transformation semigroups rather than arbitrary finite monoids with nontransitive unit groups.

Originality is therefore only to the best of our knowledge. A residual risk remains that the two-factor formula occurs in older semigroup-generation literature or a monograph under different terminology. The full text of the 2009 partition paper was not text-searchable in the sources inspected here; its abstract and the relevant description in Lu's reference chain were inspected.

## Verification

`artifacts/verify_counterexample.py` uses exact finite enumeration and no external packages. It constructs the 12-element counterexample above, exhaustively searches generating sets, and verifies
\[
\operatorname{rank}(S\wr R:H\wr G)=4.
\]
The general theorem is proved above and does not depend on this finite check.

## References

1. J. Lu, *Generation of Iterated Wreath Products Constructed from Full Transformation Monoids and Symmetric Groups*, arXiv:2609.20521v1 (2026). https://arxiv.org/abs/2609.20521
2. J. Araújo and C. Schneider, *The Rank of the Endomorphism Monoid of a Partition*, Semigroup Forum 78 (2009), 498–510; arXiv:0807.1214. https://arxiv.org/abs/0807.1214
3. J. Araújo, W. Bentz, J. D. Mitchell and C. Schneider, *The rank of the semigroup of transformations stabilising a partition of a finite set*, Math. Proc. Cambridge Philos. Soc. 159 (2015), 339–353. https://doi.org/10.1017/S0305004115000389
