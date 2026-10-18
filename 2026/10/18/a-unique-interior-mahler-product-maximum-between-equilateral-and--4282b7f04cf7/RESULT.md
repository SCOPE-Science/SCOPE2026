# A unique interior Mahler-product maximum between equilateral and four-cycle metric free spaces

## Finding
Let \(M_t=\{0,1,2,3\}\), for \(1\le t\le2\), have distances \(d_t(i,j)=1\) when \(i-j\equiv\pm1\pmod4\), and \(d_t(0,2)=d_t(1,3)=t\). Let \(P_t\) be the unit ball of the real Lipschitz-free space \(\mathcal F(M_t)\), and let \(Q_t=P_t^\circ\) under the evaluation pairing with the based Lipschitz functions.

The exact affine-invariant Mahler volume product is
\[
\boxed{\mathcal P(t)=\operatorname{vol}_3(P_t)\operatorname{vol}_3(Q_t)=\frac{8(t+4)}{9t}\bigl[4-(2-t)^3\bigr].}
\]
It is **strictly increasing** on \([1,t_*]\), and **strictly decreasing** on \([t_*,2]\), where \(t_*\) is the unique solution in \((1,2)\) of
\[
3t^4-4t^3-12t^2+16=0.
\]
Numerically \(t_*=1.121915780903\ldots\), with \(\mathcal P(t_*)=13.484844768269\ldots\), exceeding the equilateral value \(\mathcal P(1)=40/3\). The four-cycle endpoint has \(\mathcal P(2)=32/3\). For every \(1<t<2\), \(P_t\) has twelve vertices and eighteen facets, while its polar has eighteen vertices and twelve facets.

## Assumptions and scope
Everything is over the real scalars. Fix \(f(0)=0\), identify a based Lipschitz function with \((f(1),f(2),f(3))\in\mathbb R^3\), and identify a zero-total-mass measure with its last three coefficients. Euclidean coordinate volumes are computed in these dual coordinate systems; their product is independent of the choice of dual linear coordinates. At \(t=1\), the metric is equilateral. At \(t=2\), it is the unit-edge four-cycle's shortest-path metric. All intermediate values define genuine metrics because \(1\le t\le2\).

## Proof
**1. Explicit molecules and an affine cube model.** The molecule formula for finite Lipschitz-free spaces gives
\[
P_t=\operatorname{conv}\left\{\pm(e_1-e_0),\pm(e_2-e_1),\pm(e_3-e_2),\pm(e_0-e_3),\pm\frac{e_2-e_0}{t},\pm\frac{e_3-e_1}{t}\right\},
\]
where \(e_0=0\) and the remaining \(e_i\) form the coordinate basis. Each opposite-pair distance is \(t\); the four adjacent distances are one. Use the linear map
\[
T=\begin{pmatrix}1&2&1\\1&0&-1\\1&0&1\end{pmatrix},\qquad|\det T|=4.
\]
A direct substitution shows that the eight adjacent-edge molecules map to the eight vertices of \([-1,1]^3\), while the four opposite-pair molecules map to \(\pm\lambda e_1,\pm\lambda e_2\) with \(\lambda=2/t\). Consequently
\[
TP_t=K_\lambda:=\operatorname{conv}\bigl([-1,1]^3\cup\{\pm\lambda e_1,\pm\lambda e_2\}\bigr),\quad 1\le\lambda\le2.
\]

**2. Volume of the extended cube.** For \(1\le\lambda\le2\), the portion of \(K_\lambda\) outside the cube is exactly the union, with disjoint interiors, of the four square pyramids based on the faces \(x=\pm1\) and \(y=\pm1\), with apices \(\pm\lambda e_1,\pm\lambda e_2\). Here is an elementary containment check: all generating points satisfy \(x+(\lambda-1)|y|\le\lambda\) and \(x+(\lambda-1)|z|\le\lambda\), and the analogous inequalities for the other signed coordinate faces. These inequalities place every point with \(x>1\) within the pyramid over \(x=1\); similarly for the other three faces. Since \(\lambda\le2\), no point can have two of \(|x|,|y|\) greater than one (all generators satisfy \(|x|+|y|\le2\)). The reverse containment holds by convexity. Each pyramid has square base area four and height \(\lambda-1\), so
\[
\operatorname{vol}_3(K_\lambda)=8+\frac{16}{3}(\lambda-1).
\]
Thus \(\operatorname{vol}_3(P_t)=\operatorname{vol}_3(K_{2/t})/4=2(t+4)/(3t)\).

**3. Exact polar volume.** Polarity gives
\[
K_\lambda^\circ=\bigl\{(u,v,w):|u|+|v|+|w|\le1,\ |u|\le\lambda^{-1},\ |v|\le\lambda^{-1}\bigr\}.
\]
The three-dimensional \(\ell_1\) unit ball has volume \(4/3\). The four removed caps at \(u>\lambda^{-1}\), \(u<-\lambda^{-1}\), \(v>\lambda^{-1}\), \(v<-\lambda^{-1}\) have disjoint interiors because \(2/\lambda\ge1\) and \(|u|+|v|\le1\). Each cap has volume
\[
\int_{\lambda^{-1}}^1 2(1-s)^2\,ds=\frac23(1-\lambda^{-1})^3.
\]
Hence
\[
\operatorname{vol}_3(K_\lambda^\circ)=\frac43-\frac83(1-\lambda^{-1})^3=\frac{4-(2-t)^3}{3}.
\]
Dual linear changes multiply the two volumes by reciprocal determinants. Therefore \(\mathcal P(t)=\operatorname{vol}_3(K_{2/t})\operatorname{vol}_3(K_{2/t}^\circ)\), giving the stated closed formula.

**4. Unique interior maximum.** Differentiation yields
\[
\mathcal P'(t)=\frac{8}{9t^2}\,g(t),\quad g(t)=3t^4-4t^3-12t^2+16,
\]
with \(g(1)=3>0\), \(g(2)=-16<0\), and \(g'(t)=12t(t-2)(t+1)<0\) for \(1<t<2\). Thus \(g\) has exactly one zero in \((1,2)\); it is the unique strict maximizer. Substitution gives the endpoints and the numerical values above.

**5. Interior face counts.** For \(1<\lambda<2\), the cube's eight corners and the four added apices are all vertices. Each of the four raised cube faces is replaced by four triangular faces. The two unraised cube faces remain squares. The result has \(8+4=12\) vertices and \(2+4\cdot4=18\) facets. Polarity interchanges vertices and facets.

## Verification
The accompanying standard-library Python program `verify_square_volume.py` independently constructs both dual polytopes from the original twelve distance inequalities, enumerates their exact rational vertices and facets, and triangulates all faces using exact determinants. It checks the separate polar volumes and the two combinatorial counts at \(t\in\{101/100,11/10,6/5,3/2,9/5,199/100\}\). All six tests pass. The symbolic derivative and cap/pyramid calculations above, not the finite tests, establish the continuum theorem.

## Relationship to prior work
Alexander, Fradelizi, García-Lirola, and Zvavitch (2019), *Geometry and volume product of finite dimensional Lipschitz-free spaces*, study precisely this Banach-space volume product. Their Theorem 5.14 proves its lower bound \(32/3\) for all four-point metrics and characterizes equality by tree metrics or equal-edge cycles; their Sections 5.1–5.3 do not evaluate this two-diagonal deformation or its unique nonmonotone maximum. Gordon and Petrov (2016) characterize general combinatorial faces of finite Lipschitz polytopes; their classification does not determine this volume-product profile. The distinct family of cube–cross-polytope intersections uses symmetric caps in all coordinate directions, whereas this polar has caps in only two axes. These previously established statements are not claimed as new.

## Limitations
The claim applies only to this one-parameter family of four-point real metric spaces. It makes no claim about a global maximum among all four-point metrics. The algebraic optimizing parameter is implicit; its decimal value is approximate. Independent mathematical review and exhaustive bibliographic completeness are not claimed.

## References
1. M. Alexander, M. Fradelizi, L. C. García-Lirola, and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642, first posted 2019-11-24; especially Theorem 5.14. https://arxiv.org/abs/1911.10642
2. J. Gordon and F. Petrov, *Combinatorics of the Lipschitz polytope*, arXiv:1608.06848, first posted 2016-08-24. https://arxiv.org/abs/1608.06848
3. S. J. Dilworth, D. Kutzarova, and M. I. Ostrovskii, *Lipschitz-free spaces on finite metric spaces*, arXiv:1807.03814, first posted 2018-07-10. https://arxiv.org/abs/1807.03814
