# Exact Heinz-mean profile of the cut-square absolute norm family
## Finding
For the real plane \(X_\lambda=(\mathbb R^2,N_\lambda)\) with
\[
N_\lambda(s,t)=\max\{|s|,|t|,\lambda(|s|+|t|)\},\qquad \frac12\le\lambda\le1,
\]
and for every Heinz parameter \(0\le\nu\le1\),
\[
H_\nu(X_\lambda)=\max\{\lambda^{-1},2\lambda\}
=\begin{cases}
\lambda^{-1},&\frac12\le\lambda\le\frac1{\sqrt2},\\
2\lambda,&\frac1{\sqrt2}\le\lambda\le1.
\end{cases}
\]
Thus the Heinz-mean constant is independent of \(\nu\) on this family. Its minimum over the family is \(\sqrt2\), attained exactly at \(\lambda=1/\sqrt2\).

## Assumptions and scope
The field is real and the dimension is two. The Heinz mean is
\[
M_\nu(a,b)=\frac{a^\nu b^{1-\nu}+a^{1-\nu}b^\nu}2,
\qquad 0\le\nu\le1,
\]
with the usual continuous interpretation when one of \(a,b\) is zero. The geometric constant is
\[
H_\nu(X)=\sup_{x,y\in S_X}M_\nu(\|x+y\|,\|x-y\|).
\]
Only the cut-square family above is claimed. It is the mixed endpoint \((p,q)=(\infty,1)\) of the family \(\max\{\|\cdot\|_p,\lambda\|\cdot\|_q\}\) considered in the motivating source.

## Proof
Put \(a=\lambda^{-1}-1\), so \(0\le a\le1\). The unit ball of \(N_\lambda\) is the centrally symmetric octagon with vertices
\[
(1,a),(a,1),(-a,1),(-1,a),(-1,-a),(-a,-1),(a,-1),(1,-a),
\]
with the expected degeneracies at the two endpoint values of \(\lambda\).

First compute the arithmetic endpoint
\[
A_2(X_\lambda)=\sup_{x,y\in S_{X_\lambda}}
\frac{N_\lambda(x+y)+N_\lambda(x-y)}2.
\]
The displayed objective is a convex function of \((x,y)\) on the product of the unit ball with itself. A convex function on a polytope has a maximum at a vertex, so it is enough to inspect pairs of vertices. Signed-coordinate symmetries let us fix \(x=(1,a)\). Up to swapping \(x+y\) and \(x-y\), the four resulting values of the arithmetic objective are
\[
1,\qquad 2\lambda,\qquad \max\{\lambda^{-1},2\lambda\},\qquad \lambda^{-1}.
\]
For completeness, the third value comes from \(y=(-a,1)\). Indeed,
\[
x+y=(1-a,1+a),\qquad x-y=(1+a,a-1),
\]
and \(1+a=\lambda^{-1}\), \(1-a=2-\lambda^{-1}\). Hence both vectors have the same norm,
\[
N_\lambda(x+y)=N_\lambda(x-y)=\max\{\lambda^{-1},2\lambda\}.
\]
The other three vertex classes give the other three displayed arithmetic values directly. Therefore
\[
A_2(X_\lambda)=\max\{\lambda^{-1},2\lambda\}.
\]

For nonnegative \(r,s\), the scalar Heinz inequality gives
\[
M_\nu(r,s)\le\frac{r+s}2.
\]
Consequently \(H_\nu(X_\lambda)\le A_2(X_\lambda)\). On the other hand, the vertex pair
\[
x=(1,a),\qquad y=(-a,1)
\]
has
\[
N_\lambda(x+y)=N_\lambda(x-y)=m,
\qquad m=\max\{\lambda^{-1},2\lambda\}.
\]
Thus \(M_\nu(m,m)=m\) for every \(\nu\), giving the reverse inequality. This proves the formula.

Finally, \(\lambda^{-1}=2\lambda\) exactly when \(\lambda=1/\sqrt2\); the first branch decreases and the second increases, so the family minimum is exactly \(\sqrt2\).

## Verification
The proof is finite and exact. The only reduction is the standard convex-polytope fact that the maximum of a convex function over a compact polytope is attained at a vertex; applying it to the product ball reduces the arithmetic endpoint to the eight vertex classes above. The equality pair is explicit and works for every \(\nu\), so no numerical optimization is used to certify the result.

As a boundary check, \(\lambda=1/2\) gives the square norm \(\|\cdot\|_\infty\) and the formula gives \(H_\nu=2\). At \(\lambda=1\) the norm is \(\|\cdot\|_1\) and again \(H_\nu=2\). At the transition \(\lambda=1/\sqrt2\), the cut-square is the regular octagonal absolute norm and the formula gives \(H_\nu=\sqrt2\).

## Relationship to prior work
Zuo and Huang define \(H_\nu\) for absolute normalized norms and in their Example 4.10 treat
\[
\|z\|_{p,q,\lambda}=\max\{\|z\|_p,\lambda\|z\|_q\},
\qquad 1\le q\le p\le\infty.
\]
The displayed formula in that example has two cases: \(1\le q<p\le2\) and \(2\le q<p\le\infty\). The mixed regime \(q<2<p\), including \((p,q)=(\infty,1)\), is not covered by either displayed branch, although the subsequent remark describes the example informally as treating the general range. The present result supplies an exact mixed-endpoint profile and exhibits the phase transition at the Euclidean comparison threshold \(\lambda=1/\sqrt2\).

Targeted searches by the invariant name, the mixed endpoint aliases, the exact norm, and the candidate formula did not locate an equivalent or stronger published statement. A same-object database hit concerns a different octahedrality invariant and does not imply the Heinz-mean formula.

## Limitations
No formula is asserted here for the full mixed range \(1\le q<2<p\le\infty\); only the natural endpoint \((p,q)=(\infty,1)\) is settled. Literature search cannot prove absolute novelty, so an obscure equivalent statement under unrelated notation remains a residual risk. The scientific proof itself is independent of the literature search.

## References
1. Z. Zuo and Y. Huang, “Absolute normalized norms in \(\mathbb R^2\) and Heinz means constant,” *Topological Methods in Nonlinear Analysis* 60 (2022), 475–490. DOI: 10.12775/TMNA.2022.003.
