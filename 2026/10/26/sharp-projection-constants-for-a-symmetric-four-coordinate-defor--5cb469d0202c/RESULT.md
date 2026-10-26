# Sharp projection constants for a symmetric four-coordinate deformation

## Finding

For each real parameter \(0\le t\le1\), let \(X_t=(\mathbb R^2,N_t)\), where
\[
N_t(x,y)=\max\{|x|,|y|,|x+ty|,|tx+y|\}.
\]
Equivalently, \(X_t\) is the two-dimensional subspace
\[
V_t=\{(x,y,x+ty,tx+y):x,y\in\mathbb R\}\subset\ell_\infty^4(\mathbb R).
\]
Its **absolute projection constant** is exactly
\[
\boxed{\lambda(X_t)=\lambda(V_t,\ell_\infty^4)=\frac{2(1+t)}{2+t}=1+\frac{t}{2+t}.}
\]
An optimal projection is explicitly given below. For \(0<t<1\), it is the **unique** minimum-norm projection that commutes with simultaneous exchange of the first two and last two coordinates.

Writing \(d_t=d(X_t,\ell_\infty^2)\) for the Banach–Mazur distance, one also has the certified comparison
\[
\frac{2(1+t)}{2+t}\ \le\ d_t\ \le\ 1+\frac t2,
\qquad 0\le\left(1+\frac t2\right)-d_t\le\frac{t^2}{2(2+t)}.
\]
In particular, the exact first-order behavior is \(\lim_{t\downarrow0}(d_t-1)/t=1/2\). The displayed upper bound is **not** claimed to be the exact distance at interior parameters.

## Assumptions and scope

All vector spaces, operators, and projections are **real**. The parameter range is \(0\le t\le1\), with uniqueness asserted only for \(0<t<1\). The absolute projection constant is the supremum over isometric embeddings of the infimum of norms of bounded linear projections in the ambient Banach spaces; because \(\ell_\infty^4\) is injective, it agrees with the relative projection constant of this isometric four-coordinate realization. There are no infinite-dimensional limiting arguments.

Set
\[
B_t=\begin{pmatrix}1&0\\0&1\\1&t\\t&1\end{pmatrix},\qquad
A_t=\frac1{2+t}\begin{pmatrix}1+t&-t&1&0\\-t&1+t&0&1\end{pmatrix},\qquad P_t=B_tA_t.
\]
The subspace is \(V_t=\operatorname{ran}B_t\). Since \(A_tB_t=I_2\), the map \(P_t\) projects onto \(V_t\).

## Proof

**1. Exact upper certificate.** The four row vectors of \(P_t\) come in two exchange-symmetric pairs. The first is
\[
\frac1{2+t}(1+t,-t,1,0),
\]
and the third is
\[
\frac1{2+t}(1+t-t^2,t^2,1,t).
\]
For \(0\le t\le1\), every entry in the latter vector is nonnegative. Both absolute row sums equal \(2(1+t)/(2+t)\); the other two row sums are the same. Since the norm on \(\ell_\infty^4\) is the maximum absolute row sum, \(\|P_t\|=2(1+t)/(2+t)\).

**2. Symmetrization and universal lower certificate.** Let \(J\) interchange coordinates \(1\leftrightarrow2\) and \(3\leftrightarrow4\). It is an isometric involution with \(JV_t=V_t\). For an arbitrary projection \(P\) onto \(V_t\), the average \((P+JPJ)/2\) is again a projection onto \(V_t\), with norm no greater than \(\|P\|\). It therefore suffices to bound projections commuting with \(J\).

Every such projection has the form \(B_tA\), with
\[
A=\begin{pmatrix}a&b&c&d\\b&a&d&c\end{pmatrix},\qquad
 a+c+td=1,\qquad b+tc+d=0.
\]
Its first and third absolute row sums are
\[
L_1=|a|+|b|+|c|+|d|,\quad
L_3=|a+tb|+|b+ta|+|c+td|+|d+tc|.
\]
For \(0\le t\le1\), the coefficient \(2t-1\) belongs to \([-1,1]\). Consequently,
\[
L_1\ge a-b+c+(2t-1)d=1+t(c+d),
\]
while the sum of the four arguments of \(L_3\) gives
\[
L_3\ge(1+t)(a+b+c+d)=(1+t)(1-t(c+d)).
\]
Setting \(h=t(c+d)\), every such projection obeys
\[
\|P\|\ge\max\{1+h,(1+t)(1-h)\}\ge\frac{2(1+t)}{2+t}.
\]
The last inequality follows because the increasing and decreasing affine functions cross at \(h=t/(2+t)\), where each equals the claimed minimum. Combined with Step 1, this proves the exact formula for the relative projection constant. For completeness, equality with the absolute constant follows as follows: any isometric embedding \(I:V_t\hookrightarrow Y\) extends, coordinate by coordinate, through the injectivity of \(\ell_\infty^4\), to a contraction \(F:Y\to\ell_\infty^4\) with \(F(Iv)=v\). Then \(I P_t F\) is a projection onto \(I(V_t)\) of norm at most \(\|P_t\|\); the realization in \(\ell_\infty^4\) gives the reverse inequality.

**3. Rigidity in the exchange-symmetric class.** Assume \(0<t<1\) and a \(J\)-commuting projection attains the minimum. Equality in the maximum of the two affine lower bounds forces \(t(c+d)=t/(2+t)\). Equality in the first absolute-value inequality forces \(d=0\), because \(|2t-1|<1\) whereas the coefficient of \(d\) in \(L_1\) is \(|d|\). Thus \(c=1/(2+t)\). The two projection identities uniquely determine \(a=(1+t)/(2+t)\) and \(b=-t/(2+t)\). Hence the optimal \(J\)-commuting projection is exactly \(P_t\). No uniqueness assertion is made for arbitrary nonsymmetric projections or at the endpoints.

**4. Banach–Mazur comparison and exact first derivative.** The classical injectivity argument gives \(\lambda(X_t)\le d_t\). For the reverse estimate, put \(q=t/(2+t)\) and consider the invertible real matrix
\[
T_t=\begin{pmatrix}1&q\\q&1\end{pmatrix}:X_t\longrightarrow\ell_\infty^2.
\]
For \(t<1\), the unit ball of \(X_t\) is the convex hull of the eight signed points \((1,0)\), \((0,1)\), \((1,-1)\), and \(((1+t)^{-1},(1+t)^{-1})\); at \(t=1\), the latter point lies on an existing edge and is redundant. Evaluation at these vertices shows \(\|T_t\|=1\). Furthermore, the corners \((1,1)\) and \((1,-1)\) of the target unit square are sent by \(T_t^{-1}\) to \((1,1)/(1+q)\) and \((1,-1)/(1-q)\), whose \(X_t\)-norms both equal \(1+t/2\). Thus \(\|T_t^{-1}\|=1+t/2\), proving the upper bound. Subtraction gives the stated error interval, and dividing by \(t\) proves the first-derivative limit.

## Verification

The standalone `checker.py` performs exact rational-arithmetic verification for ten rational parameters, including both endpoints. It verifies \(A_tB_t=I_2\), all four row sums of \(P_t\), the two affine dual bounds on a finite rational grid of arbitrary symmetric left inverses, and the stated norm estimates for \(T_t\) and its inverse by exact vertex calculations. All checks passed. The analytic argument above, not the finite checker, proves the theorem for every real \(t\) in the interval. The code uses only Python's standard library and can be run as `python checker.py`.

## Relationship to prior work

Deregowska and Lewandowska (2026, arXiv:2610.06141v1, Theorem 2.4) bound the Banach–Mazur distance in terms of an already-known projection constant for arbitrary codimension-two subspaces; that theorem does not evaluate the constant in the present four-coordinate deformation. The classical sharp planar upper endpoint \(4/3\), with equality only for the affine-regular hexagon, is recalled by Chalmers, Franchetti, and Giaquinta (1996). The case \(t=1\) is the familiar affine-regular hexagonal endpoint, while \(t=0\) is the injective square; the explicit interior profile and the exchange-equivariant rigidity are the new statements being evaluated here. Lassak's work concerns the Banach–Mazur distance between a parallelogram and affine-regular even-gons, not this projection profile for nonregular interior octagons.

## Limitations

The uniqueness theorem is relative to projections commuting with the coordinate-swap involution; uniqueness over all projections is not asserted. The interior Banach–Mazur distance is bracketed, not claimed exactly determined. The results apply to real scalars only and do not assert the same projection formula for complexifications, other four-coordinate embeddings, or higher codimensions. Historical priority remains uncertain: equivalent planar projection constants could be buried in older convex-geometric calculations even when the coordinate presentation differs. Independent verification has not been performed.

## References

1. B. Deregowska and B. Lewandowska, *Projection Constants and Banach-Mazur Distance in Codimension Two*, arXiv:2610.06141v1, first submitted 2026-10-05. https://arxiv.org/html/2610.06141v1
2. B. Chalmers, C. Franchetti, and M. Giaquinta, *On the self-length of two-dimensional Banach spaces*, Bulletin of the Australian Mathematical Society **53** (1996), 101–107. https://doi.org/10.1017/S0004972700016762
3. M. Lassak, *Banach–Mazur Distance from the Parallelogram to the Affine-Regular Hexagon and Other Affine-Regular Even-Gons*, Results in Mathematics **76** (2021), article 62; arXiv:2008.01653. https://arxiv.org/abs/2008.01653
