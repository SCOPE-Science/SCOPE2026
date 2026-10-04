# Exact positivity defect and max norm of the affine least-squares projector on a simplex
## Finding
Let \(T\subset\mathbb R^d\) be any nondegenerate \(d\)-simplex, \(d\ge1\), and let
\[
\Pi_1:L^2(T)\longrightarrow \mathbb P_1(T)
\]
be the \(L^2\)-orthogonal projector onto affine functions. For every \(M>0\),
\[
\min_{\substack{0\le f\le M\\\text{a.e. on }T}}\ \min_{x\in T}(\Pi_1f)(x)
=
-M\,C_d,
\]
where
\[
C_d
=
(d+1)\left(\frac{d+1}{d+2}\right)^d-1.
\]
The constant is independent of the shape of the simplex.

The bound is attained at every vertex. If \(v_i\) is a vertex and \(\lambda_i\) is its barycentric coordinate, then
\[
f_i(y)
=
M\,\mathbf 1_{\{\lambda_i(y)<1/(d+2)\}}
\]
satisfies
\[
(\Pi_1 f_i)(v_i)=-M C_d.
\]
Strict positivity does not remove the effect: for
\[
f_{i,\varepsilon}(y)
=
M\left[
\varepsilon+(1-\varepsilon)
\mathbf 1_{\{\lambda_i(y)<1/(d+2)\}}
\right],
\]
one has \(f_{i,\varepsilon}\ge\varepsilon M>0\) and still
\[
(\Pi_1f_{i,\varepsilon})(v_i)<0
\]
whenever
\[
0<\varepsilon<\frac{C_d}{1+C_d}.
\]

The same calculation gives the exact \(L^\infty\)-operator norm:
\[
\|\Pi_1\|_{L^\infty(T)\to L^\infty(T)}
=
1+2C_d
=
2(d+1)\left(\frac{d+1}{d+2}\right)^d-1.
\]
In particular,
\[
\frac{C_d}{d}\longrightarrow e^{-1},
\qquad
\frac{\|\Pi_1\|_{L^\infty\to L^\infty}}{d}
\longrightarrow \frac2e.
\]
Thus positivity loss is not merely present: its sharp amplitude grows linearly with dimension. Already for \(d=3\),
\[
C_3=\frac{131}{125}>1,
\]
so a function taking values only in \([0,M]\) can have a projected vertex value below \(-M\).

## Assumptions and scope
The projector is the exact local \(L^2\)-orthogonal projection onto the full affine space on one simplex. The input \(f\) may be any essentially bounded measurable function; the extremizer is discontinuous, although strictly positive approximations with the same sign failure are given explicitly.

No global continuity constraints between elements are imposed. The theorem therefore concerns the element-local affine projector, not the global continuous finite-element \(L^2\) projector. It also does not claim the same constant for higher polynomial degree, tensor-product cells, mass-lumped projection, constrained projection, or positivity-preserving postprocessing.

Because an affine bijection maps barycentric coordinates to barycentric coordinates and multiplies every \(L^2\) inner product by the same Jacobian factor, the result is invariant under simplex shape and scale.

## Proof
Let \(\lambda_0,\ldots,\lambda_d\) be the barycentric coordinates on \(T\). Their Gram matrix is
\[
G_{ij}
=
\int_T\lambda_i(y)\lambda_j(y)\,dy
=
\frac{|T|}{(d+1)(d+2)}(1+\delta_{ij}).
\]
Hence, writing \(J\) for the all-ones matrix,
\[
G
=
\frac{|T|}{(d+1)(d+2)}(I+J)
\]
and
\[
G^{-1}
=
\frac{(d+1)(d+2)}{|T|}
\left(I-\frac{J}{d+2}\right).
\]

Therefore the reproducing kernel of \(\Pi_1\) is
\[
K(x,y)
=
\lambda(x)^{\mathsf T}G^{-1}\lambda(y)
=
\frac{d+1}{|T|}
\left(
(d+2)\sum_{i=0}^d\lambda_i(x)\lambda_i(y)-1
\right),
\]
and
\[
(\Pi_1f)(x)=\int_TK(x,y)f(y)\,dy.
\]
Since constants are reproduced,
\[
\int_TK(x,y)\,dy=1.
\]

Fix \(x\) and write
\[
a_i=\lambda_i(x),\qquad a_i\ge0,\qquad \sum_i a_i=1.
\]
For \(0\le f\le M\), the minimum at this fixed \(x\) is obtained by taking \(f=M\) where \(K(x,\cdot)<0\) and \(f=0\) where \(K(x,\cdot)>0\). Thus
\[
\min_{0\le f\le M}(\Pi_1f)(x)
=
-M\,c(a),
\]
where, if \(B=(B_0,\ldots,B_d)\) is uniformly distributed in barycentric coordinates on the simplex,
\[
c(a)
=
(d+1)\,
\mathbb E
\left[
\left(
1-(d+2)\sum_{i=0}^d a_iB_i
\right)_+
\right].
\]

Set
\[
\psi(s)=(1-(d+2)s)_+.
\]
This function is convex. Pointwise in \(B\),
\[
\psi\!\left(\sum_i a_iB_i\right)
\le
\sum_i a_i\psi(B_i).
\]
Taking expectations and using symmetry of the uniform Dirichlet distribution gives
\[
c(a)
\le
\sum_i a_i c(e_i)
=
c(e_0).
\]
Hence the largest negative mass occurs at a vertex.

At a vertex, say \(a=e_0\), the random variable \(B_0\) has density
\[
d(1-t)^{d-1},
\qquad 0\le t\le1.
\]
Therefore
\[
C_d=c(e_0)
=
d(d+1)
\int_0^{1/(d+2)}
(1-(d+2)t)(1-t)^{d-1}\,dt.
\]
Let
\[
q=\frac{d+1}{d+2}.
\]
Using
\[
\int_0^{1/(d+2)}(1-t)^{d-1}\,dt
=
\frac{1-q^d}{d}
\]
and
\[
\int_0^{1/(d+2)}t(1-t)^{d-1}\,dt
=
\frac{1-q^d}{d}
-
\frac{1-q^{d+1}}{d+1},
\]
one obtains
\[
C_d
=
(d+1)q^d-1.
\]
This proves the sharp positivity-defect formula and the indicator extremizer.

For the strictly positive perturbation, linearity and reproduction of constants give
\[
(\Pi_1f_{i,\varepsilon})(v_i)
=
M\left[
\varepsilon-(1-\varepsilon)C_d
\right],
\]
which is negative exactly under the stated condition.

Finally, for an integral operator,
\[
\|\Pi_1\|_{L^\infty\to L^\infty}
=
\sup_{x\in T}\int_T|K(x,y)|\,dy.
\]
Since \(\int_TK(x,y)\,dy=1\),
\[
\int_T|K(x,y)|\,dy
=
1+2c(a).
\]
The preceding vertex maximization therefore yields
\[
\|\Pi_1\|_{L^\infty\to L^\infty}=1+2C_d.
\]
The asymptotic statements follow from
\[
\left(1-\frac1{d+2}\right)^d\longrightarrow e^{-1}.
\]

## Verification
The accompanying `verify.py` uses exact rational arithmetic. For dimensions \(1\le d\le50\), it constructs the barycentric Gram matrix, verifies the stated inverse exactly, verifies the reproducing-kernel normalization, and evaluates the one-dimensional beta integral by exact polynomial expansion. The result is checked against
\[
C_d=(d+1)\left(\frac{d+1}{d+2}\right)^d-1.
\]
It also verifies the exact low-dimensional constants
\[
C_1=\frac13,\qquad
C_2=\frac{11}{16},\qquad
C_3=\frac{131}{125}
\]
and the corresponding operator norms.

The checker does not use finite-dimensional sampling to establish the vertex extremum. That step is the convexity argument in the proof and applies to every dimension and every point of the simplex.

## Relationship to prior work
The \(L^\infty\)-stability and max-norm of \(L^2\)-orthogonal projectors are classical numerical-analysis questions. De Boor studied \(L^\infty\) bounds for least-squares spline approximation and also obtained mesh-independent bounds for continuous piecewise polynomials. Foucart later studied exact-growth questions for max norms of orthogonal spline projectors and related them to polynomial projector Lebesgue functions. Those results establish the surrounding projector-norm theory and are not claimed as new.

Crouzeix and Thomée proved \(L^p\) and \(W^{1,p}\) stability for \(L^2\) projection onto standard finite-element spaces under mesh hypotheses. Duan, Lin, Saikrishnan, and Tan used a local or almost local \(L^2\) projector onto the linear finite-element space as a key ingredient of least-squares finite-element schemes. These sources establish that local linear \(L^2\) projection is a standard finite-element operation and that norm stability is a substantive issue.

The present result isolates the single-simplex affine operator and solves a different sharp question: the exact negative excursion on the cone \(0\le f\le M\), together with the exact \(L^\infty\) operator norm, in every spatial dimension. The proof also identifies the extremizing region and shows a dimension-linear positivity defect. The one-dimensional special case belongs to classical polynomial-projector theory; the all-dimensional simplex formula, positivity extremizer, and asymptotic law are the claimed contribution.

## Limitations
The theorem is local to one simplex and degree one. It does not determine the max norm or positivity defect of a globally continuous finite-element projection, where neighboring elements couple through the global mass matrix.

Orthogonal-projector norm literature is extensive. In particular, polynomial projection constants are often expressed through reproducing kernels or Lebesgue functions, so an equivalent multivariate simplex formula may exist under approximation-theory terminology not found in the searches performed here. The full 1987 Crouzeix--Thomée article was not recovered through the open or authorized institutional routes attempted, so it is retained as an access risk rather than used for a whole-document noncoverage claim.

## References
1. Huo-yuan Duan, Ping Lin, P. Saikrishnan, and Roger C. E. Tan, *L2-Projected Least-Squares Finite Element Methods for the Stokes Equations*, SIAM Journal on Numerical Analysis 44 (2006), 732--752, DOI: 10.1137/040613573.
2. Carl de Boor, *A Bound on the L-Infinity-Norm of L2-Approximation by Splines in Terms of a Global Mesh Ratio*, Mathematics of Computation 30 (1976), 765--771, DOI: 10.1090/S0025-5718-1976-0425432-1.
3. Michel Crouzeix and Vidar Thomée, *The Stability in Lp and W1p of the L2-Projection onto Finite Element Function Spaces*, Mathematics of Computation 48 (1987), 521--532, DOI: 10.1090/S0025-5718-1987-0878688-2.
4. Simon Foucart, *On the Value of the Max-Norm of the Orthogonal Projector onto Splines with Multiple Knots*, Journal of Approximation Theory 140 (2006), 154--177, DOI: 10.1016/j.jat.2005.12.004.
