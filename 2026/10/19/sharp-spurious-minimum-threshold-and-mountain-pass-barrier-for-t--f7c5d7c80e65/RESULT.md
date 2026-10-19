# Sharp spurious-minimum threshold and mountain-pass barrier for two-term SPD rank-one matrix approximation

## Finding

Let \(N\ge2\), \(t>1\), \(D=\operatorname{diag}(t,t^{-1},1,\ldots,1)\), and
\[
\kappa=\frac{t^2+t^{-2}}2>1,\qquad
\mathcal A(X)=\tfrac12(DXD^{-1}+D^{-1}XD).
\]
For \(a>b>0\), put \(F=\operatorname{diag}(a,b,0,\ldots,0)\) and minimize
\[
f(X)=\tfrac12\langle X,\mathcal A(X)\rangle_F-\langle F,X\rangle_F
\]
over real matrices \(X\in\mathbb R^{N\times N}\) of **rank exactly one**. The operator \(\mathcal A\) is symmetric positive definite with spectral condition number exactly \(\kappa\). The unique global minimum is \(X_a=a e_1e_1^\top\), while \(X_b=b e_2e_2^\top\) is another stationary point.

**Sharp false-minimum threshold:** \(X_b\) is a strict, nonglobal local minimum if and only if \(\kappa>a/b\). For \(1<\kappa<a/b\), it is a strict saddle; at equality it has a flat quadratic direction with a strictly decreasing quartic perturbation and therefore is not a local minimum.

When \(N=2\) and \(\kappa>a/b\), there are exactly four rank-one stationary matrices: \(X_a\), \(X_b\), and the two saddles
\[
S_\pm=\begin{pmatrix}x_*&\pm\sqrt{x_*y_*}\\ \pm\sqrt{x_*y_*}&y_*\end{pmatrix},\quad
x_* =\frac{\kappa b-a}{\kappa^2-1},\quad y_* =\frac{\kappa a-b}{\kappa^2-1}.
\]
For \(1<\kappa\le a/b\), the two axial matrices are the only rank-one stationary points in dimension two.

**Exact escape barrier in every dimension:** Whenever \(\kappa>a/b\), the minimum, over all continuous paths in the rank-one manifold from \(X_b\) to \(X_a\), of the maximum objective value along the path is
\[
\boxed{\displaystyle f(X_b)+\frac{(\kappa b-a)^2}{2(\kappa^2-1)}.}
\]
The infimum is attained by an explicit rank-one path. Thus an arbitrarily well-conditioned SPD matrix equation can have a strict nonglobal rank-one minimum with a positive mountain-pass barrier: choose \(1<a/b<\kappa\) with \(\kappa\) arbitrarily close to one. Here \(F\) has rank two, regardless of \(N\).

## Assumptions and scope

All matrices and paths are real; the operator acts on the full space \(\mathbb R^{N\times N}\) with Frobenius inner product. The constraint is rank **exactly** one, not rank at most one; all identified minima are nonzero and smooth points of that manifold. Parameters obey \(N\ge2\), \(t>1\), \(a>b>0\), and \(\kappa=(t^2+t^{-2})/2\). The two Kronecker terms have positive-definite factors: \(\mathcal A(X)=\tfrac12(DXD^{-1}+D^{-1}XD)\). Both the full forcing \(F\) and the exact unrestricted solution \(\mathcal A^{-1}F=F\) have rank two. The exact critical-point count is asserted only when \(N=2\); the false minimum and mountain-pass value hold for all \(N\ge2\).

## Proof

**1. Operator spectrum and global optimum.** Write \(d_i=D_{ii}>0\). On the standard matrix units, \(\mathcal A(E_{ij})=w_{ij}E_{ij}\), with
\[
w_{ij}=\tfrac12(d_i/d_j+d_j/d_i)\in[1,\kappa].
\]
The endpoints occur at diagonal units and \(E_{12}\), respectively. This proves SPD and condition number \(\kappa\). Moreover,
\[
f(X)=\tfrac12\|X-F\|_F^2-\tfrac12\|F\|_F^2
       +\tfrac12\sum_{i,j}(w_{ij}-1)X_{ij}^2.
\]
The rank-one Eckart–Young inequality for \(F\), whose two nonzero singular values are \(a>b\), yields \(\|X-F\|_F^2\ge b^2\); equality holds only at \(X_a\). All extra terms are nonnegative and vanish there. Hence \(X_a\) uniquely minimizes \(f\), with \(f(X_a)=-a^2/2\); \(f(X_b)=-b^2/2\) is strictly larger.

**2. A sharp local-Hessian test, including the boundary.** In a chart around \(X_b\), let \(y=X_{22}\), \(p_i=X_{i2}\), \(q_j=X_{2j}\) for \(i,j\ne2\). Every nearby rank-one matrix has \(X_{ij}=p_iq_j/y\) when \(i,j\ne2\), and conversely this parametrizes the rank-one manifold for \(y\ne0\). The quadratic Taylor term at \(y=b,p=q=0\) is
\[
\tfrac12(y-b)^2+\tfrac12\sum_{i\ne2}w_{i2}p_i^2
 +\tfrac12\sum_{j\ne2}w_{2j}q_j^2-\frac ab p_1q_1.
\]
The only potentially indefinite block has eigenvalues proportional to \(\kappa+a/b\) and \(\kappa-a/b\). Thus \(\kappa>a/b\) gives a positive-definite Hessian and a strict local minimum; \(\kappa<a/b\) gives a negative tangent direction, alongside a positive \(y\)-direction, so \(X_b\) is a strict saddle. At \(\kappa=a/b>1\), set \(p_1=q_1=z\), all other \(p,q\) zero, and \(y=b-\kappa z^2/b\). Direct expansion gives
\[
f(X(z))-f(X_b)=\frac{1-\kappa^2}{2b^2}z^4+O(z^6)<0
\]
for all sufficiently small nonzero \(z\). The boundary point is therefore not a local minimum.

**3. Exhaustive dimension-two critical points.** For \(N=2\), write \(X=\begin{pmatrix}x&u\\v&y\end{pmatrix}\). The manifold is \(xy-uv=0\), excluding the zero matrix, where this determinant constraint is regular. At a critical point some \(\lambda\in\mathbb R\) satisfies
\[
x-a=\lambda y,\quad y-b=\lambda x,\quad
\kappa u=-\lambda v,\quad\kappa v=-\lambda u.
\]
If \(u=v=0\), the rank-one constraint forces an axis and the equations give exactly \(X_a\) or \(X_b\). Otherwise \(\lambda=\pm\kappa\). With \(\lambda=+\kappa\), the equations give \(x,y<0\), while \(u=-v\) forces \(xy=-u^2\le0\), impossible. With \(\lambda=-\kappa\), the equations give \(x=x_*\), \(y=y_*\), \(u=v\), and \(u^2=xy\), yielding exactly \(S_\pm\) when \(x_*>0\), i.e. \(\kappa>a/b\). When \(\kappa>a/b\), the positive-semidefinite rank-one subfamily \(X(x,y)=\begin{psmallmatrix}x&\sqrt{xy}\\\sqrt{xy}&y\end{psmallmatrix}\), \(x,y>0\), has restricted energy
\[
\tfrac12(x^2+y^2)+\kappa xy-ax-by.
\]
At \((x_*,y_*)\), its Hessian \(\begin{psmallmatrix}1&\kappa\\\kappa&1\end{psmallmatrix}\) has one negative eigenvalue; the opposite-sign offdiagonal branch is identical. Thus both \(S_\pm\) are genuine saddles. (The nonzero determinant multiplier at \(\kappa=1\) cannot produce further solutions because \(a\ne b\); this follows by the same equations.)

**4. Sharp mountain-pass value in all dimensions.** Let \(\kappa>a/b\). Then \(x_*>0\), \(y_*=b-\kappa x_*>0\). Every continuous rank-one path from \(X_b\), whose \((1,1)\)-entry is zero, to \(X_a\), whose \((1,1)\)-entry is \(a>x_*\), crosses a matrix with \(X_{11}=x_*\). Put \(y=X_{22}\) there. The rank-one relation \(X_{12}X_{21}=x_*y\), positivity of all other quadratic terms, and \(u^2+v^2\ge2|uv|\) imply
\[
f(X)\ge\tfrac12x_*^2+\tfrac12y^2+\kappa x_*|y|-ax_*-by.
\]
The right-hand side is uniquely minimized over real \(y\) at \(y=y_*>0\), giving
\[
f(S_\pm)=-\tfrac12(ax_*+by_*)=-\tfrac12b^2
 +\frac{(\kappa b-a)^2}{2(\kappa^2-1)}.
\]
This is a lower bound for every such path's maximum, independent of dimension.

Conversely, set \(y(x)=(b-\kappa x)_+\) for \(0\le x\le a\), and let \(X(x)\) be zero outside its leading \(2\times2\) block, which is
\[
\begin{pmatrix}x&\sqrt{x y(x)}\\\sqrt{x y(x)}&y(x)\end{pmatrix}.
\]
This is a continuous path of nonzero rank-one matrices from \(X_b\) to \(X_a\). On \(0\le x\le b/\kappa\), its energy is
\[
f(X(x))=-\tfrac12b^2+(\kappa b-a)x-\tfrac12(\kappa^2-1)x^2,
\]
whose unique maximum occurs at \(x=x_*\). On \(b/\kappa\le x\le a\), its energy is \(x^2/2-ax\), convex and no larger than that maximum at either endpoint. Thus the lower bound is attained, proving the exact barrier. Taking \(\kappa=1+\varepsilon/2\) and \(a/b=1+\varepsilon/4\), with \(\varepsilon>0\), proves the arbitrarily small conditioning-gap assertion.

## Verification

The included `verify_landscape.py` reproduces exact symbolic identities for the critical-point equations, the barrier, the boundary quartic coefficient, and finite rational instances of the Kronecker operator and rank-one energy. Run `python verify_landscape.py` with SymPy installed. The finite checks support the algebra but do not prove critical-point exhaustiveness or the universal path lower bound; those follow from the arguments above. The identity \(\kappa>1\) is used throughout the nontrivial bifurcation. No finite-precision experiments are required.

## Relationship to prior work

Bioli, Kressner, and Robol (2024, arXiv:2408.16416, first submitted 2024-08-29) formulate the SPD multiterm matrix equation as a rank-constrained Riemannian optimization problem and develop preconditioned algorithms. The theorem here specializes to a two-term SPD operator but classifies its false minima, all two-dimensional stationary points, and an exact escape-energy barrier; algorithmic convergence of their specific method is **not** claimed.

Manton, Mahony, and Hua (2003) study weighted low-rank approximation and explain the possibility of nonglobal local minima. That general observation does not supply the exact conditioning-versus-singular-gap threshold or the dimension-independent mountain-pass value established here. Zhu, Li, Tang, and Wakin (2017/2021) analyze benign geometry for unweighted matrix factorization and for general problems under additional regularity hypotheses; those statements must not be transferred to this weighted, under-parameterized example without checking their assumptions.

## Limitations

The complete stationary-point classification is proved only in dimension two; in larger dimensions only the specified extrema and sharp barrier are classified. The forcing matrix has rank two, not rank one. The operator's factors commute and are diagonal, and the results concern exact rank-one constraints and exact arithmetic. The theorem does not say that a particular preconditioned Riemannian CG implementation necessarily converges to the nonglobal minimum; it describes a genuine obstacle in its optimization landscape. Classical weighted-approximation theory may contain equivalent special calculations not found in the sources compared here, so publication priority is not independently established.

## References

1. I. Bioli, D. Kressner, L. Robol, *Preconditioned Low-Rank Riemannian Optimization for Symmetric Positive Definite Linear Matrix Equations*, arXiv:2408.16416 (initial public submission 2024-08-29), especially its SPD matrix-equation formulation and fixed-rank objective.
2. J. H. Manton, R. Mahony, Y. Hua, *The Geometry of Weighted Low-Rank Approximations*, IEEE Transactions on Signal Processing 51 (2003), 500–514, doi:10.1109/TSP.2002.807002.
3. Z. Zhu, Q. Li, G. Tang, M. B. Wakin, *The Global Optimization Geometry of Low-Rank Matrix Optimization*, arXiv:1703.01256; IEEE Transactions on Information Theory 67 (2021), 1308–1331.
4. C. Eckart and G. Young, *The Approximation of One Matrix by Another of Lower Rank*, Psychometrika 1 (1936), 211–218.
