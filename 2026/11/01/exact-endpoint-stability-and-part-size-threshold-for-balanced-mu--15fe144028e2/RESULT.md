# Exact endpoint stability and part-size threshold for balanced multipartite metric-graph splines

## Finding

Fix integers \(r\ge2\), \(m\ge1\). Let \(G_{m,r}\) be the complete \(r\)-partite graph with \(m\) vertices in each part. Replace every edge by a unit interval, identify its endpoints with the graph vertices, and equip this compact metric graph \(\Gamma_{m,r}\) with Lebesgue arclength on every edge. Let \(S_{m,r}\) consist of real continuous functions affine on each entire edge, and let \(P_{m,r}:L^2(\Gamma_{m,r})\to S_{m,r}\) be the orthogonal projector. Its canonical finite-rank extension acts on \(L^\infty(\Gamma_{m,r})\).

Then its exact attained endpoint norm is
\[
\boxed{\|P_{m,r}\|_{L^\infty\to L^\infty}=\frac{24mr^2-70mr+51m+4r-5}{3(2r-3)(2mr-3m+1)}.}
\]
Every graph vertex is a norming evaluation point. A norm-one, real, measurable input attaining the bound at any selected vertex is the sign of that vertex's reproducing kernel.

The sharp amplification transition is
\[
\|P_{m,r}\|\begin{cases}
<2,&m\le2\text{ or }(m=3,r\ge3),\\
=2,&(m,r)=(3,2),\\
>2,&m\ge4.
\end{cases}
\]
For fixed \(r\), the norm is strictly increasing in \(m\), and
\[
\lim_{m\to\infty}\|P_{m,r}\|=2+\frac{1}{3(2r-3)},
\qquad \lim_{r\to\infty}\|P_{m,r}\|=2\quad(m\text{ fixed}).
\]
Consequently, the entire balanced multipartite family has the sharp unattained supremum \(\sup_{m\ge1,r\ge2}\|P_{m,r}\|=7/3\); it is approached by balanced complete bipartite graphs \(K_{m,m}\) as \(m\to\infty\), even though these graphs have no degree-one vertices for \(m\ge2\).

The exact largest possible downward excursion of \(P_{m,r}f\) for \(0\le f\le1\) is \((\|P_{m,r}\|-1)/2\), attained by a measurable indicator function.

## Assumptions and scope

The underlying graph is simple and connected, all edges have length one and equal positive arclength density, and no internal finite-element nodes are introduced. There are \(rm\) graph vertices and \(\binom r2m^2\) edges. The edges are disjoint except at identified endpoints, which are arclength-null sets. The norm is the essential supremum of real functions. The projection is defined using ordinary, unweighted arclength \(L^2\); multiplying all edge measures by a common positive scalar leaves it unchanged. Integer cases \(r=2,m=1\) (a single interval) and \(m=1\) (complete graphs) are included.

## Proof

Write \(d=m(r-1)\) for the graph degree. For each vertex \(v\), let \(\phi_v\) be the continuous hat function equal to one at \(v\) and zero at every other vertex, and affine on edges. These \(rm\) functions form a basis of \(S_{m,r}\). Direct integration on a unit edge yields the Gram matrix
\[
G_{vv}=\frac d3,\qquad G_{vw}=\begin{cases}\frac16,&v\sim w,\\0,&v\not\sim w,\ v\ne w.\end{cases}
\]
In particular \(6G=2dI+A\), where \(A\) is the adjacency matrix.

Put \(T=m^2(r-1)(2r-3)\) and \(X=3m(2r-3)+1\). The exact inverse is
\[
(G^{-1})_{vw}=\frac1T\begin{cases}
X,&w=v,\\
1,&w\ne v\text{ in the same part},\\
-2,&w\text{ in a different part}.
\end{cases}
\]
To verify without a spectral assumption, multiply this candidate inverse by \(G\). At the distinguished row the numerator is \(2dX-2d=6T\). At another vertex in the distinguished part the numerator is \(2d-2d=0\). At a vertex of another part the numerator is \(X+(m-1)-2m(3r-4)=0\). Symmetry gives every column and therefore the asserted inverse. Here \(T>0\) for all allowed integers.

For fixed \(v\), the evaluation functional of \(P_{m,r}\) at \(v\) has edgewise kernel
\[
K_v|_{[a,b]}(t)=(G^{-1})_{va}(1-t)+(G^{-1})_{vb}t,\qquad 0\le t\le1.
\]
Its edge endpoint pairs, scaled by \(T\), are \((X,-2)\) on the \(d\) incident edges; \((1,-2)\) on the \(d(m-1)\) edges joining another vertex of \(v\)'s part to another part; and \((-2,-2)\) on the \(\binom{r-1}{2}m^2\) edges with neither endpoint in \(v\)'s part. This exhausts the entire edge set.

For positive \(a,b\), a linear function joining \(a\) to \(-b\) has absolute integral
\[
J(a,b)=\int_0^1|a(1-t)-bt|\,dt=\frac{a^2+b^2}{2(a+b)}.
\]
Consequently, since \(J(1,2)=5/6\), the exact absolute kernel integral is
\[
\begin{aligned}
\int_{\Gamma_{m,r}}|K_v|\,ds
&=\frac{dJ(X,2)+d(m-1)(5/6)+m^2(r-1)(r-2)}{T}\\
&=\frac{24mr^2-70mr+51m+4r-5}{3(2r-3)(2mr-3m+1)}=:R_{m,r}.
\end{aligned}
\]
For any \(\|f\|_\infty\le1\), \(|(P_{m,r}f)(v)|\le R_{m,r}\), and equality holds for \(f=\operatorname{sgn}K_v\) almost everywhere. Since the projected function is affine on every edge, its absolute value is bounded by the larger absolute endpoint value; thus \(\|P_{m,r}f\|_\infty\) is the maximum of the vertex values. Vertex transitivity proves the claimed global sharp norm and the norming status of every vertex.

Subtraction gives the exact difference
\[
R_{m,r}-2=\frac{m(2r-3)-8r+13}{3(2r-3)(m(2r-3)+1)}.
\]
At \(r=2\) the numerator is \(m-3\); for \(r\ge3\) it is \((m-4)(2r-3)+1\). This proves the three sharp cases. Moreover,
\[
R_{m+1,r}-R_{m,r}=\frac{4(2r-3)}{3(2mr-3m+1)(2mr-3m+2r-2)}>0.
\]
Taking limits in the rational expression proves both asymptotics. Since the expression increases strictly with \(m\) and its \(m\)-limit is at most \(7/3\), equality of that upper limit is approached only along the balanced bipartite subfamily \(r=2\), proving the sharp, unattained family supremum.

Finally \(P_{m,r}\mathbf1=\mathbf1\), hence \(\int K_v=1\). Thus the negative mass of \(K_v\) is \((R_{m,r}-1)/2\). For any \(0\le f\le1\), every projected vertex value is at least the negative of that number, and equality at a chosen vertex is achieved by the indicator of \(\{K_v<0\}\). Affine edge interpolation transfers the same bound to the whole metric graph. This proves the exact positivity defect.

## Verification

The included `verify_balanced_metric_graph.py` uses exact SymPy rational arithmetic, independently constructs the full hat-function Gram matrix directly from the graph edges, computes its inverse, checks every proposed inverse entry, and integrates the absolute kernel on each edge. It checks 26 separate parameter pairs with \(2\le r\le7\), \(1\le m\le5\), and \(rm\le24\): 4,690 exact assertions, plus symbolic algebra and limiting identities. Execute using `python verify_balanced_metric_graph.py` with SymPy installed. The finite test set is supplementary; the general integer-parametric claim is established by the preceding algebraic proof.

## Relationship to prior work

The classical endpoint-stability problem for one-dimensional spline orthogonal projection appears in Kayumov's 2004 study of second-order \(L\)-splines and the de Boor/Oskolkov estimates; that work studies subdivisions of an interval, not the balanced multipartite metric graphs here. Pesenson's 2005 paper treats graph splines defined by Sobolev-energy minimization and spectral approximation, rather than the present direct arclength \(L^2\)-projector onto edgewise-affine nodal functions. Arioli and Benzi's quantum-graph finite-element analysis develops nodal mass and stiffness matrices and PDE approximation, without stating the present exact graph-family \(L^\infty\) stability or the part-size transition in its examined sections. These approaches motivate the object, but they do not directly imply the displayed sharp rational formula.

The single-edge boundary instance \((m,r)=(1,2)\) has norm \(5/3\), consistent with classical affine interval projection. The result is not a claim of priority over any undiscovered equivalent graph projection calculation.

## Limitations

The formula is restricted to balanced complete multipartite graphs with one affine element per unit edge, real scalars, equal arclength density, and ordinary \(L^2\)-orthogonality. It does not determine sharp norms for unequal part sizes, general graph topologies, interior mesh refinement, or variable edge weights. The extremizing sign inputs are measurable and may be discontinuous inside edges. Nothing here establishes that this result was previously unknown in every unindexed source, or constitutes independent external validation.

## References

1. A. Kayumov, *Least-squares approximation by second-order L-splines*, arXiv:math/0408418, first publicly submitted 2004-08-30. https://arxiv.org/abs/math/0408418
2. I. Pesenson, *Polynomial splines and eigenvalue approximations on quantum graphs*, Journal of Approximation Theory 135 (2005), 203–220, doi:10.1016/j.jat.2005.04.007, available online 2005-06-23.
3. M. Arioli and M. Benzi, *A finite element method for quantum graphs*, Emory University technical report TR-2015-009 (2015); subsequent IMA Journal of Numerical Analysis 38 (2018), 1119–1163, doi:10.1093/imanum/drx029.
