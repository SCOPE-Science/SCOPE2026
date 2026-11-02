# The twelve characteristic-seven Cartier-rank jumps in the Wiman–Edge sextic pencil

## Finding
Work over an algebraically closed field \(k\) of characteristic \(7\). Define homogeneous sextics
\[
W=x^6+y^6+z^6+(x^2+y^2+z^2)(x^4+y^4+z^4)-12x^2y^2z^2,
\qquad Q=(x^2-y^2)(y^2-z^2)(z^2-x^2).
\]
For \(t\in k\) let \(C_t\) be the normalization of \(W+tQ=0\). Put
\[
\begin{aligned}
D(t)={}&(t^2-2t+3)(t^2+2t+3)\\
&\cdot(t^4-t^3+t^2+t+3)(t^4+t^3+t^2-t+3)\in\mathbb F_7[t].
\end{aligned}
\]
On the geometric smooth-fiber parameter set \(U=\{t\in k:(t^2-4)(t^2+1)\ne0\}\), every \(C_t\) is smooth connected of genus six, and
\[
\boxed{a(\operatorname{Jac}(C_t))=\begin{cases}3,&D(t)=0,\\0,&D(t)\ne0.\end{cases}}
\]
The polynomial \(D\) is squarefree of degree twelve and has no root among excluded parameters. Thus there are exactly twelve distinct rank-drop fibers over \(\overline{\mathbb F}_7\); all others in \(U\) are ordinary. Here the \(a\)-number is the dimension of the kernel of Cartier on \(H^0(C_t,\Omega^1)\). The finding does not claim the \(7\)-rank of the twelve exceptional Jacobians.

## Assumptions and scope
The base is an algebraically closed field of characteristic exactly \(7\); the pencil parameter \(t\) is finite and belongs to \(U\). The excluded fiber at \(t=\infty\) is the six-line arrangement \(Q=0\). The four assigned points \([\pm1:\pm1:1]\) are resolved by normalization. Statements on number of roots count geometric parameters with multiplicity one.

## Proof
**(1) Geometry and smooth-fiber locus.** The curve is even in each variable. With \(u=x^2,v=y^2,w=z^2\), its cubic in the square-coordinates is
\[
G_t=u^3+v^3+w^3+(u+v+w)(u^2+v^2+w^2)-12uvw+t(u-v)(v-w)(w-u).
\]
This cubic has an assigned singularity at \([1:1:1]\). In the chart \(w=1\), let \(u=1+a,v=1+b\). Its equation is the sum of the quadratic \(8(a^2-ab+b^2)\) and the homogeneous cubic
\[
2a^3+(1-t)a^2b+(1+t)ab^2+2b^3.
\]
The quadratic has nonzero discriminant modulo \(7\). Its resultant with the cubic, after putting \(a=1\), is a nonzero constant times \(t^2-4\); hence the cubic \(G_t\) is irreducible with an ordinary node and no other singularity when \(t^2\ne4\). The restricted cubics on the three coordinate axes have discriminants each a nonzero constant times \((t^2-4)(t^2+1)\). Thus, if \(t\in U\), the sextic has no singularity on the axes or off the four assigned points. Each assigned point is ordinary because squaring coordinates is étale where \(xyz\ne0\). Irreducibility follows by taking successive square roots of \(u/w\) and \(v/w\) in the function field of the irreducible nodal cubic: these two square classes are independent, as witnessed by simple zeros at points of distinct transverse coordinate-axis intersections (no coordinate-axis intersection is a vertex). Therefore its pullback under the degree-four squaring map is integral. The plane sextic has exactly four ordinary nodes, so its normalization has genus \((6-1)(6-2)/2-4=6\).

**(2) Cartier matrix.** The regular differentials on the normalization are the adjoint cubics divided by the customary plane-sextic differential. A basis of adjoints is \(b_{ij}=x_i^3-x_ix_j^2\) for ordered pairs \(i\ne j\), where \((x_0,x_1,x_2)=(x,y,z)\). These are six independent cubics and vanish at all four nodes, hence form a basis of \(H^0(C_t,\Omega^1)\). Index degree-three monomials by triples \(\alpha=(\alpha_0,\alpha_1,\alpha_2)\), \(|\alpha|=3\). Compute the coefficient-extraction matrix
\[
H_{\alpha\beta}=[x^{7(\alpha_0+1)-(\beta_0+1)}y^{7(\alpha_1+1)-(\beta_1+1)}z^{7(\alpha_2+1)-(\beta_2+1)}](W+tQ)^6,
\]
with coefficients in \(\mathbb F_7[t]\). Let \(B\) be the ten-by-six matrix whose columns are the cubic coefficients of \(b_{ij}\). The explicit finite polynomial multiplication verifies \(HB=BK\) with a six-by-six matrix \(K\) and
\[
\det K=D(t)^3\quad\text{in }\mathbb F_7[t].
\]
The displayed recipe specifies every entry, not merely a numerical interpolation. The matrix \(K\) is block diagonal with three two-by-two blocks, and each block contains, up to sign, an off-diagonal entry \(t(5t^4+4)\). Direct Euclidean computations show
\[
\gcd(D,D')=1,\qquad \gcd(D,t(5t^4+4))=1,\qquad
\gcd(D,(t^2-4)(t^2+1))=1.
\]
Consequently \(K\) is invertible off \(D=0\). At every root of \(D\), each two-by-two block has zero determinant but a nonzero off-diagonal entry, so each has rank one and the full matrix has rank three. The coefficient-extraction formula computes the Cartier matrix up to the inverse Frobenius on scalars, which does not affect rank. Hence the Cartier-kernel dimension is respectively zero or three. This proves the assertion.

## Verification
The standalone `verify_wiman7.py` evaluates \((W+tQ)^6\) by finite exact polynomial multiplication in characteristic seven, reconstructs the adjoint-basis matrix, confirms the coefficient identity \(HB=BK\), verifies \(\det K=D^3\) and squarefreeness, and checks the singular-fiber discriminants and exclusion coprimality. Run with `python verify_wiman7.py` and SymPy installed. It requires no external data. Its successful output ends with `VERIFY_OK`. These checks certify the finite algebraic identities only; the normalization/Cartier interpretation is proved above rather than inferred from finite experiments.

## Relationship to prior work
Wiman's classical sextic and Edge's 1981 pencil, including the six-line member, are known [1–2]. Inoue and Kato give this precise equation and a construction of its pencil [3]. Candelas, de la Ossa, van Geemen and van Straten relate the genus-six pencil to lines on the Dwork quintic [4]. Dolgachev, Farb and Looijenga comprehensively describe the complex-algebraic geometry and singular members [5]. Literature on the isolated Wiman curve's finite-field Jacobian [6] concerns a fixed parameter. None of the inspected results states the twelve-fiber characteristic-seven Cartier-jumping divisor or the simultaneous rank drop of three for this complete pencil. This is a priority assessment based on inspected material, not a claim to exhaustive historical uniqueness.

## Limitations
This is a characteristic-seven and finite-parameter classification of Cartier rank (equivalently \(a\)-number), not a determination of the \(7\)-rank, Ekedahl–Oort type, Newton polygons, stable reductions at excluded parameters, or any characteristic other than seven. The literature search does not prove absence of an equivalent statement in uninspected sources. Some early printed literature has not been exhaustively read in full.

## References
[1] W. L. Edge, “A pencil of four-nodal plane sextics,” *Math. Proc. Cambridge Philos. Soc.* 89 (1981), 413–421, DOI 10.1017/S0305004100058321. Cambridge online posting 24 October 2008.
[2] A. Wiman, nineteenth-century construction of the genus-six curve, as cited in [1], [3].
[3] N. Inoue and F. Kato, “On the geometry of Wiman’s sextic,” Kyoto preprint (2005), https://www.math.kyoto-u.ac.jp/preprint/2005/2inoue.kato.pdf.
[4] P. Candelas, X. de la Ossa, B. van Geemen, D. van Straten, “Lines on the Dwork Pencil of Quintic Threefolds,” arXiv:1206.4961, 21 June 2012.
[5] I. Dolgachev, B. Farb, E. Looijenga, “Geometry of the Wiman–Edge pencil, I,” *European Journal of Mathematics* 4 (2018), 879–930, DOI 10.1007/s40879-018-0231-3.
[6] “An F_{p^2}-maximal Wiman’s sextic and its automorphisms,” arXiv:1805.06317 (2018).
