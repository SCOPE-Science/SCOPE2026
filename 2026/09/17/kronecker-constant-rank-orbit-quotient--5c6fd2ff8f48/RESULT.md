# Correct orbit quotient for constant-rank models of Kronecker elementary modules

## Result

Let \(k\) be an algebraically closed field and let \(K_n\) be the \(n\)-Kronecker quiver with fixed arrows
\[
\gamma_1,\ldots,\gamma_n:1\longrightarrow 2.
\]
Let \(n=x+y-1\), assume \((x,y)\) is in the usual fundamental domain and \(x<n\), and define
\[
\mathcal C_{x,y}
=
\left\{
H\le M_{n\times y}(k):
\dim H=x,\quad \operatorname{rank}A=y\ \text{for every }0\ne A\in H
\right\}.
\]
The group \(GL_y(k)\) acts on \(\mathcal C_{x,y}\) by right multiplication,
\[
H\cdot Q=\{AQ:A\in H\}.
\]

Then ordinary isomorphism classes of elementary \(K_n\)-modules of dimension vector \((x,y)\) are naturally in bijection with
\[
\boxed{\mathcal C_{x,y}/GL_y(k).}
\]

Moreover, changing the basis of the arrow space by \(P\in GL_n(k)\) corresponds to left multiplication
\[
H\longmapsto PH.
\]
Consequently the further quotient by arrow-space changes is
\[
\boxed{
GL_n(k)\backslash \mathcal C_{x,y}/GL_y(k),
}
\]
which is the usual left-right equivalence relation for matrix spaces. Thus standard matrix-space equivalence classifies elementary modules only after allowing a change of arrow basis; it is strictly coarser than ordinary module isomorphism for the fixed quiver.

This distinction gives an explicit counterexample to the literal fixed-arrow classification in Theorem 4.2 of Jie Liu, *Dimension vectors of elementary modules of generalized Kronecker quivers* (Communications in Algebra 51 (2023), 4223--4233), and supplies the precise equivalence relation needed in Theorem 3.11 of the 2026 preprint *Elementary modules of the generalized Kronecker quivers \(K(n)\)*.

## Why the quotient is \(GL_y\), not \(GL_n\times GL_y\)

For a representation \(M\) and \(m\in M_1\), choose a basis of \(M_2\) and form the \(n\times y\) matrix
\[
A_m=
\begin{bmatrix}
(\gamma_1m)^t\\
\vdots\\
(\gamma_nm)^t
\end{bmatrix}.
\]
For an elementary module in the regime above, Liu's full-rank criterion gives
\[
\operatorname{rank} A_m=y\qquad (m\ne0).
\]
The map
\[
T_M:M_1\longrightarrow M_{n\times y}(k),\qquad m\longmapsto A_m
\]
is therefore injective, so
\[
H_M:=T_M(M_1)
\]
has dimension \(x\) and belongs to \(\mathcal C_{x,y}\).

A change of basis in \(M_1\) only changes a basis of the image \(H_M\); it does not change the subspace itself. A change of basis \(Q\in GL_y(k)\) in \(M_2\) right-multiplies every \(A_m\) by the same invertible matrix, so it sends \(H_M\) to \(H_MQ\).

More invariantly, identify \(A_n=k^n\) with the arrow space using the fixed ordered arrow basis. The same construction is the image of
\[
\widetilde T_M:M_1\longrightarrow \operatorname{Hom}_k(A_n,M_2),
\qquad
m\longmapsto\left(
\sum_i \lambda_i\gamma_i\mapsto \sum_i\lambda_i\gamma_i m
\right).
\]
An ordinary representation isomorphism \((S,Q):M\to N\) satisfies
\[
N(\gamma_i)S=QM(\gamma_i)
\]
for every fixed arrow \(\gamma_i\). Hence
\[
\widetilde T_N(Sm)=Q\circ\widetilde T_M(m),
\]
so ordinary module isomorphism changes the image only at the \(M_2\)-end. There is no \(GL_n\)-action here because the arrows are fixed.

Conversely, given \(H\in\mathcal C_{x,y}\), choose any vector-space isomorphism
\[
\theta:k^x\stackrel{\sim}{\longrightarrow}H.
\]
For \(m\in k^x\), let the \(i\)-th row of \(\theta(m)\) be the coordinate row of \(\gamma_i m\in k^y\). This defines a \(K_n\)-representation \(M_H\). Replacing \(\theta\) by \(\theta\circ S^{-1}\) changes only the source basis and gives an isomorphic module; replacing \(H\) by \(HQ\) changes only the sink basis and also gives an isomorphic module. Since every nonzero matrix in \(H\) has rank \(y\), every nonzero \(m\in (M_H)_1\) generates the full sink, and Liu's criterion implies that \(M_H\) is elementary. These constructions are inverse on the stated orbit sets.

Finally, an arrow-space basis change \(P\in GL_n(k)\) takes linear combinations of the fixed arrow maps. On the stacked matrices it acts by left multiplication. Therefore the \(GL_n\)-orbit on module isomorphism classes is exactly the additional left quotient of \(\mathcal C_{x,y}/GL_y\).

## Explicit \(K_3\) counterexample

Take \(x=y=2\), so \(n=3\), and let
\[
H=
\left\{
A(a,b)=
\begin{bmatrix}
a&0\\
b&a\\
0&b
\end{bmatrix}
:\ a,b\in k
\right\}.
\]
The three \(2\times2\) minors of \(A(a,b)\) are
\[
a^2,\qquad ab,\qquad b^2.
\]
Thus every nonzero \(A(a,b)\) has rank \(2\), so \(H\in\mathcal C_{2,2}\).

The associated \(K_3\)-module \(M\) has arrow maps
\[
G_1=
\begin{bmatrix}1&0\\0&0\end{bmatrix},\qquad
G_2=
\begin{bmatrix}0&1\\1&0\end{bmatrix},\qquad
G_3=
\begin{bmatrix}0&0\\0&1\end{bmatrix}.
\]
This is precisely the standard module \(X(2,2)\) from Liu's construction. Let \(P\) swap the first two rows and put
\[
H'=PH.
\]
The corresponding representation \(M'\) has arrows
\[
(G_2,G_1,G_3).
\]
Both \(M\) and \(M'\) are elementary because the corresponding stacked matrix has full rank for every nonzero source vector.

However,
\[
(\operatorname{rank}G_1,\operatorname{rank}G_2,\operatorname{rank}G_3)
=(1,2,1)
\]
for \(M\), while the rank triple for \(M'\) is
\[
(2,1,1).
\]
An isomorphism of representations of the fixed quiver preserves the rank of each individual arrow map, so
\[
M'\not\cong M.
\]
On the other hand, \(H'=PH\), so \(H\) and \(H'\) are equivalent in the standard left-right sense for matrix spaces. This proves that standard matrix-space equivalence is too coarse for ordinary \(K_3\)-module isomorphism.

It also disproves the literal fixed-arrow reading of the 2023 claim that every elementary module with \(x+y=n+1\) is of the single form \(X(x,y)\): \(M'\) is elementary of dimension \((2,2)\) for \(K_3\), but is not isomorphic to \(X(2,2)\).

## Relation to the recent literature

The 2023 paper's proof of its Theorem 4.2 passes from the fact that two maximal constant-rank spaces have the same dimension to an asserted vector-space isomorphism and then writes the basis of one as an invertible linear combination of the basis of the other inside the ambient matrix space. Equal abstract dimension does not imply that relation between two distinct embedded matrix subspaces. The \(K_3\) example above exhibits the resulting failure concretely.

The 2026 preprint replaces the unique-model claim with a correspondence between elementary modules and maximal fixed-rank spaces, stated "under the isomorphisms." The preprint does not specify an equivalence relation on the embedded matrix spaces. The theorem above separates the two natural possibilities:

- ordinary module isomorphism for the fixed arrows corresponds to right \(GL_y\)-orbits;
- standard left-right matrix-space equivalence corresponds to ordinary module isomorphism together with the natural \(GL(A_n)\) action changing the arrow basis.

This agrees with Daniel Bissinger's 2025 treatment of the natural \(GL(A_n)\)-action on elementary Kronecker representations, where arrow-space changes are explicitly kept distinct from representation isomorphism.

## Limitations and originality

The linear-algebraic orbit argument itself is elementary, and left-right equivalence of matrix spaces is standard. The claimed contribution is the precise orbit-level correction of the constant-rank correspondence for elementary Kronecker modules, together with the explicit \(K_3\) counterexample to the published fixed-arrow classification.

To the best of our knowledge, targeted searches found no published correction or erratum to the 2023 theorem and no source stating this exact \(GL_y\) versus \(GL_n\times GL_y\) correction for the 2026 correspondence. The 2026 manuscript is very recent, so an author revision or concurrent correction remains possible. The full text of Westwick's 1987 paper on fixed-rank matrix spaces was not inspected; its relevance is to matrix-space equivalence and dimension bounds rather than to the Kronecker-module quotient, but it remains a residual prior-literature risk.

## References

1. J. Liu, *Elementary modules of the generalized Kronecker quivers \(K(n)\)*, arXiv:2609.14238v1 (2026).
2. J. Liu, *Dimension vectors of elementary modules of generalized Kronecker quivers*, Communications in Algebra **51** (2023), 4223--4233. DOI: 10.1080/00927872.2023.2203243.
3. D. Bissinger, *Shift orbits for elementary representations of Kronecker quivers*, Journal of the London Mathematical Society **111** (2025), e70122. DOI: 10.1112/jlms.70122.
4. R. Westwick, *Spaces of matrices of fixed rank*, Linear and Multilinear Algebra **20** (1987), 171--174. DOI: 10.1080/03081088708817751.
