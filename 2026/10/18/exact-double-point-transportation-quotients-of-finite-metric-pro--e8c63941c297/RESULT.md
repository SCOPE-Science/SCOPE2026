# Exact double-point transportation quotients of finite metric products

## Finding

Let \((X_i,d_i)\), for \(1\le i\le s\), be finite real metric spaces with \(|X_i|\ge2\). Endow \(X=\prod_{i=1}^s X_i\) with the sum metric \(d(x,y)=\sum_i d_i(x_i,y_i)\). Write \(V_0(Y)=\{\mu\in\mathbb R^Y:\sum_{y\in Y}\mu(y)=0\}\). On \(V_0(Y)\) use the **double-point transportation seminorm**
\[
 N_{\mathrm{DP},Y}(\mu)=\frac12\max_{u,v\in Y}\left|\sum_{y\in Y}\mu(y)\bigl(d_Y(u,y)-d_Y(v,y)\bigr)\right|.
\]
For each coordinate define the signed marginal \(\mu_i(a)=\sum_{x:x_i=a}\mu(x)\). Then **for every** \(\mu\in V_0(X)\),
\[
 \boxed{N_{\mathrm{DP},X}(\mu)=\sum_{i=1}^s N_{\mathrm{DP},X_i}(\mu_i).}
\]
Consequently the marginal map induces a canonical surjective linear isometry
\[
 \boxed{V_0(X)/\ker N_{\mathrm{DP},X}\ \cong\ \bigoplus_{i=1}^s{}_{\ell_1}\bigl(V_0(X_i)/\ker N_{\mathrm{DP},X_i}\bigr).}
\]
If \(r_i=\dim\bigl(V_0(X_i)/\ker N_{\mathrm{DP},X_i}\bigr)\), the product kernel has dimension
\[
 \boxed{\dim\ker N_{\mathrm{DP},X}=\prod_i|X_i|-1-\sum_i r_i.}
\]
In particular, as soon as \(s\ge2\) the double-point seminorm of \(X\) is never a norm, irrespective of whether the factor seminorms are norms.

For the weighted Hamming product, where \(X_i\) has \(q_i\ge2\) points, all distinct points in factor \(i\) have distance \(\lambda_i>0\), and \(s\ge1\), the quotient is exactly the \(\ell_1\)-sum of the centered oscillation spaces
\[
 \left(\left\{z\in\mathbb R^{q_i}:\sum_a z_a=0\right\},\quad
 z\longmapsto\frac{\lambda_i}{2}\left(\max_a z_a-\min_a z_a\right)\right).
\]
Its dimension, kernel dimension, numbers of unit-ball vertices, and numbers of unit-ball facets are respectively
\[
 \boxed{\sum_i(q_i-1),\qquad \prod_iq_i-1-\sum_i(q_i-1),\qquad
 \sum_i(2^{q_i}-2),\qquad \prod_iq_i(q_i-1).}
\]
In the binary case with unit coordinate distances, the quotient is isometric to \(\ell_1^s\), while the kernel has dimension \(2^s-s-1\); its unit ball is the \(s\)-dimensional cross-polytope.

## Assumptions and scope

All spaces and scalars are real. Every metric factor is finite and nonempty, with at least two points. The sum metric is used, not the maximum or Euclidean product metric. The term **double-point** refers to the distance-function-difference seminorm above, not the usual Kantorovich--Rubinstein norm. Quotients are by their exact zero seminorm subspaces; they are complete because finite-dimensional. A facet means a codimension-one face of the indicated quotient unit ball, in its own linear span. No statement here concerns the facet count of the ordinary Lipschitz-free unit ball.

## Proof

**1. Distance profiles and oscillation.** For any finite metric \(Y\) and zero-mass \(\nu\), define \(A_{Y,\nu}(u)=\sum_y\nu(y)d_Y(u,y)\). Because the maximum over ordered pairs includes both orientations,
\[
 N_{\mathrm{DP},Y}(\nu)=\tfrac12\bigl(\max_u A_{Y,\nu}(u)-\min_u A_{Y,\nu}(u)\bigr).
\]
The coordinate marginals have total mass zero. Additivity of the product distance gives, for every \(u\in X\),
\[
 A_{X,\mu}(u)=\sum_{i=1}^s\sum_{a\in X_i}\mu_i(a)d_i(u_i,a)
                  =\sum_{i=1}^s A_{X_i,\mu_i}(u_i).
\]
Since the coordinates \(u_i\) may be chosen independently, the maximum (respectively minimum) of the last sum is the sum of its separate maxima (respectively minima). Taking half its oscillation proves the boxed seminorm identity for all zero-mass \(\mu\).

**2. Surjectivity and dimension.** Fix arbitrary basepoints \(b_i\in X_i\). Given \(\nu_i\in V_0(X_i)\), define the lift \(L_i\nu_i\in V_0(X)\) supported on the coordinate line through \((b_1,\dots,b_s)\), with value \(\nu_i(a)\) at the position whose \(i\)-th coordinate is \(a\). Its \(i\)-th marginal is \(\nu_i\), and every other marginal vanishes because \(\sum_a\nu_i(a)=0\). Hence \(L=\sum_iL_i\) is a linear right inverse of the marginal map \(T\). The identity in Step 1 says exactly that \(T\) is an isometry after quotienting both the domain and factors by their zero seminorm subspaces. Surjectivity yields the asserted direct-sum isometry. Since \(\dim V_0(X)=\prod_i|X_i|-1\), rank-nullity gives the kernel dimension.

For \(s\ge2\), select different points \(a_i,b_i\) in each of two factors, hold all other coordinates at their basepoints, and take the signed four-point rectangle \((\delta_{a_1}-\delta_{b_1})\otimes(\delta_{a_2}-\delta_{b_2})\otimes\bigotimes_{i\ge3}\delta_{b_i}\). This is nonzero, has zero total mass and all one-coordinate marginals zero, and so belongs to the double-point kernel. This establishes the sharp non-norm conclusion independently of the ranks of the factors.

**3. Hamming marginal spaces.** In factor \(i\), the distance matrix has entries \(\lambda_i\) off the diagonal and zero on it. Thus, for zero-sum \(\nu_i\),
\[
 A_{X_i,\nu_i}(a)=\lambda_i\sum_{b\ne a}\nu_i(b)=-\lambda_i\nu_i(a).
\]
The factor seminorm is therefore \(\lambda_i/2\) times the coordinate oscillation, which is a genuine norm on zero-sum vectors and has dimension \(q_i-1\). The asserted quotient and kernel dimensions follow. More explicitly, the kernel is precisely the signed measures with every one-coordinate marginal zero. A basis consists of products of coordinate differences supported in any subset of at least two coordinates, with basepoint Dirac masses in the other coordinates; the number of these products is \(\prod_iq_i-1-\sum_i(q_i-1)\).

**4. Exact facial geometry.** For one equilateral factor of cardinality \(q\) and edge length \(\lambda\), its unit ball in the zero-sum hyperplane is
\[
 B_{q,\lambda}=\{z:\textstyle\sum_a z_a=0,\ z_a-z_b\le 2/\lambda\text{ for all }a\ne b\}.
\]
Each ordered pair inequality defines a distinct facet: a vector with value \(1/\lambda\) at \(a\), value \(-1/\lambda\) at \(b\), and zero elsewhere makes only that ordered-pair inequality tight (for \(q=2\), the same conclusion holds in dimension one). Therefore there are \(q(q-1)\) facets.

The vertices are exactly
\[
 z^{S}=\frac2\lambda\left(\mathbf1_S-\frac{|S|}{q}\mathbf1\right)
 \quad\text{for }\varnothing\ne S\subsetneq\{1,\ldots,q\}.
\]
Indeed, at any vertex the tight ordered-pair inequalities must determine every zero-sum coordinate. Tight pairs connect exactly maximum-valued to minimum-valued coordinates; if any coordinate has an intermediate value, it belongs to no tight pair and can be perturbed while preserving all inequalities. If all coordinates have the same value, the vector is interior. Thus every vertex has exactly two levels, with gap \(2/\lambda\), and conversely every stated two-level vector has a complete bipartite tight-pair graph across its two levels and is uniquely determined by these equalities together with zero sum. There are \(2^q-2\) vertices.

Finally the unit ball of a finite \(\ell_1\)-direct sum has as its vertices exactly the embedded vertices of its summand balls. Its polar is the Cartesian product of the summand polars; vertices of a Cartesian product are products of factor vertices. By polarity the number of facets of the direct-sum ball is the product of the facet numbers of its summands. This gives \(\sum_i(2^{q_i}-2)\) vertices and \(\prod_i q_i(q_i-1)\) facets. For \(q_i=2\) and \(\lambda_i=1\), each factor is an interval with its standard absolute-value norm, giving precisely \(\ell_1^s\) and its cross-polytope unit ball.

## Verification

The standalone executable file `verify_dp_product.py` compares both sides of the seminorm identity by exact rational arithmetic, for every zero-mass vector with entries in \(\{-1,0,1\}\) on products of sizes \((2,2)\), \((2,3)\), \((3,3)\), \((2,2,2)\), and a weighted \((2,3)\) product, and for 350 deterministic signed vectors in each of three additional products. Exact centered-distance-matrix ranks agree with the sum of factor ranks in all eight examples. The script separately enumerates vertices of the equilateral factor unit balls for \(q=2,3,4,5\) from the exact defining inequalities, obtaining \(2,6,14,30\) vertices and verifying their explicit two-level form. The finite tests corroborate, but are not substitutes for, the general proof above. Run `python verify_dp_product.py` with Python 3 and SymPy.

## Relationship to prior work

Melleray, Petrov, and Vershik introduced the double-point compatible norm/seminorm using differences of metric distance functions; this definition is the starting point here. Ostrovska and Ostrovskii's 2019 paper treats the possible nontrivial double-point kernel (including the four-cycle), as well as the Banach geometry of double-point spaces over finite trees. The present result is about exact **normed-quotient tensorization under finite sum-metric products**, not the preexisting four-cycle example. The known Cartesian-product formula for graph distance matrices, and work on the ranks and spectra of such matrices, explain part of the linear-algebraic dimension phenomenon, but do not themselves give the factorwise \(\ell_1\)-isometry or the resulting double-point unit-ball vertex/facet counts. The ordinary Lipschitz-free geometry of Hamming products concerns a different, generally much higher-dimensional normed space.

## Limitations

The theorem requires a finite full Cartesian product equipped with the sum metric. It does not claim an analogous exact direct-sum law for a subset of a product, a maximum-metric product, or any infinite product without additional hypotheses. The vertex and facet formulas apply to the double-point quotient and not to the original transportation-cost unit ball. Structural conclusions are proved, but novelty against every unindexed source cannot be certified by finite bibliographic searching. No independent scientific validation is claimed.

## References

- J. Melleray, F. V. Petrov, and A. M. Vershik, *Linearly rigid metric spaces and the embedding problem*, arXiv:math/0611049 (first posted 2006), section 1.2.2 and Definition 4; *Fundamenta Mathematicae* 199 (2008), 177–194.
- S. Ostrovska and M. I. Ostrovskii, *Generalized transportation cost spaces*, arXiv:1902.10334 (first posted 2019-02-27), especially sections 1.2, 4, and 5.
- R. B. Bapat and H. Kurata, *On Cartesian product of Euclidean distance matrices*, *Linear Algebra and its Applications* 562 (2019), 135–153, DOI:10.1016/j.laa.2018.10.008.
- D. Sarma, *On Cartesian product of matrices*, arXiv:1901.01904 (2019), sections 1–4.
- I. Doust and R. Wolf, *A problem on distance matrices of subsets of the Hamming cube*, arXiv:2109.07052 (2021), sections 1–3.
