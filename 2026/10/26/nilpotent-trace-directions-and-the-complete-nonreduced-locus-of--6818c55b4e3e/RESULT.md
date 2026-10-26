# Nilpotent trace directions and the complete nonreduced locus of three-dimensional square-zero representation schemes

## Finding
For every integer \(r\ge2\) and every algebraically closed field \(k\), consider the representation scheme \(\mathscr R_r\) of the local algebra \(A_r=k\langle t_1,\ldots,t_r\rangle/(t_it_j:1\le i,j\le r)\) on \(k^3\). Its equations for matrix generators \(X_1,\ldots,X_r\in M_3(k)\) are all entries of \(X_iX_j=0\). Write \(R_r=(\mathscr R_r)_{\mathrm{red}}\).

The reduced variety \(R_r\) consists of exactly two distinct rational irreducible components, both of dimension \(2r+2\). One component, \(C_{\mathrm{im}}\), comprises tuples whose images lie in one common line that every matrix kills; the other, \(C_{\mathrm{ker}}\), comprises tuples vanishing on a common plane that contains all their images. Their intersection \(Z\) is rational irreducible of dimension \(r+3\), of codimension \(r-1\) in either component, and consists exactly of tuples proportional to a fixed square-zero rank-one matrix (including the zero tuple).

**Scheme-level distinction:** the nonreduced locus of \(\mathscr R_r\), understood as points where its local ring is not reduced, is **exactly** \(Z\). The reduced variety has singular locus exactly \(Z\). The Zariski tangent dimension of the original representation scheme is \(2r+2\) outside \(Z\), \(4r+1\) at every nonzero point of \(Z\), and \(9r\) at the origin. The nilpotent structure is witnessed explicitly by trace functions that vanish on every geometric representation but survive infinitesimally along \(Z\).

For every finite field \(\mathbb F_q\), set \(s=q^2+q+1\). The exact rational-point counts are
\[
\#Z(\mathbb F_q)=1+s(q+1)(q^r-1),\qquad
\#R_r(\mathbb F_q)=1+2s(q^{2r}-1)-s(q+1)(q^r-1).
\]
The same component/intersection point descriptions and counts hold over every finite field, including characteristic two.

## Assumptions and scope
Matrices act on the left of the three-dimensional vector space \(V=k^3\). A tuple belongs to \(\mathscr R_r\) precisely when \(X_iX_j=0\) for all ordered pairs, including \(i=j\). The scheme is the affine scheme defined by the **quadratic** matrix-product ideal, not a scheme obtained by first adjoining trace equations or radicalizing that ideal. The term *nonreduced locus* refers to local rings of this scheme; all component and singular-locus assertions stated for \(R_r\) concern the underlying reduced variety. The geometric statements assume \(k\) algebraically closed; the finite-field counts concern the rational points of the corresponding reduced scheme.

## Proof
**1. The two components and their intersection.** Put \(I=\sum_i\operatorname{im}X_i\) and \(K=\bigcap_i\ker X_i\). The relations imply \(I\subseteq K\), so \(\dim I+\operatorname{codim}K\le3\). At any nonzero tuple, \(I\ne0\) and \(\operatorname{codim}K\ne0\); hence either \(\dim I=1\) or \(\operatorname{codim}K=1\). In the first case there is a line \(L\) with \(\operatorname{im}X_i\subseteq L\subseteq\ker X_i\) for all \(i\); in the second a plane \(W\) with \(\operatorname{im}X_i\subseteq W\subseteq\ker X_i\). The zero tuple belongs to both.

For each line \(L\), the tuples in the first incidence are the vector space \(\operatorname{Hom}(V/L,L)^r\) of dimension \(2r\). For each plane \(W\), the second incidence has fiber \(\operatorname{Hom}(V/W,W)^r\), also of dimension \(2r\). Both incidence spaces are rank-\(2r\) vector bundles over \(\mathbf P(V)\) and \(\mathbf P(V^*)\), respectively, thus irreducible and rational of dimension \(2r+2\). Their images in the affine matrix space are closed, because the incidence bases are proper; they are the two components. For \(r\ge2\), tuples \((E_{12},E_{13},0,\ldots)\) and \((E_{13},E_{23},0,\ldots)\) distinguish the components. Each nonzero tuple outside their intersection determines its incidence line or plane uniquely; on standard nonvanishing matrix-coordinate charts the inverse is regular, hence these open component strata are smooth.

Both incidence conditions hold precisely when all images lie in a line \(L\) and all matrices annihilate a plane \(W\supseteq L\). For fixed incident \((L,W)\), each matrix belongs to \(\operatorname{Hom}(V/W,L)\), a one-dimensional space. Consequently the nonzero intersection \(Z\setminus\{0\}\) is the complement of the zero section in a rank-\(r\) vector bundle over the complete flag variety \(\mathrm{Fl}(1,2;V)\), dimension \(3+r\). The flags are uniquely recovered from a nonzero tuple, so this description is an isomorphism on locally closed charts. Closure adds the origin. Thus \(Z\) is rational, irreducible, and smooth away from the origin. The reduced union is singular at every intersection point because it has two distinct local components, and smooth elsewhere as just shown. Hence \(\operatorname{Sing}(R_r)=Z\).

**2. Tangent dimensions of the original quadratic scheme.** At a tuple \(X=(X_i)\), first-order variations \(Y=(Y_i)\) satisfy
\[
 X_iY_j+Y_iX_j=0\quad(1\le i,j\le r).
\]
Simultaneous change of basis in \(V\) and invertible linear substitution among the generators preserve the equations. There are four relevant orbits of **rank profiles** sufficient for tangent dimension: the origin; a nonzero proportional tuple represented by \((E_{13},0,\ldots,0)\); a tuple on \(C_{\mathrm{im}}\setminus Z\) represented by \((E_{12},E_{13},0,\ldots,0)\); and its transposed analogue \((E_{13},E_{23},0,\ldots,0)\). Here \(E_{ab}\) is the matrix unit with entry one in row \(a\), column \(b\). Over any field these normal forms follow by elementary choices of bases in the one-dimensional image / one-dimensional quotient and in the span of the generators.

At \((E_{13},0,\ldots,0)\), the first variation \(Y_1\) is constrained by \(E_{13}Y_1+Y_1E_{13}=0\), equivalently \((Y_1)_{31}=(Y_1)_{32}=(Y_1)_{21}=0\) and \((Y_1)_{33}=-(Y_1)_{11}\), leaving \(5\) free entries. For every \(j\ge2\), both \(E_{13}Y_j=0\) and \(Y_jE_{13}=0\), meaning row three and column one vanish, leaving \(4\) free entries. The tangent dimension is therefore \(5+4(r-1)=4r+1\), in every characteristic.

At \((E_{12},E_{13},0,\ldots,0)\), the first two variations have the general form
\[
Y_1=\begin{pmatrix}-v&a&b\\0&v&0\\0&w&0\end{pmatrix},\qquad
Y_2=\begin{pmatrix}-w&c&d\\0&0&v\\0&0&w\end{pmatrix},
\]
where \(a,b,c,d,v,w\) are arbitrary. For each \(j\ge3\), only the entries in row one and columns two and three can be nonzero, giving \(2\) additional degrees of freedom per generator. The tangent dimension is \(6+2(r-2)=2r+2\). Transposition gives the same count on the opposite component. At the zero tuple every differential of the quadratic defining equations vanishes, giving tangent dimension \(9r\).

**3. Precise nonreduced support.** For each \(i\), the linear function \(\operatorname{tr}X_i\) vanishes on every geometric point: \(X_i^2=0\) implies \(X_i\) is nilpotent. Thus it lies in the radical of the ideal defining \(\mathscr R_r\). At \((E_{13},0,\ldots,0)\) the variation \(Y_1=E_{22}\) satisfies all first-order product equations but \(d(\operatorname{tr}X_1)(Y_1)=1\). Hence \(\operatorname{tr}X_1\) cannot vanish as an element of the scheme's local coordinate ring there: were it locally zero, its differential would annihilate all tangent directions. It is a nonzero nilpotent in that local ring. Invertible changes of basis and generator coordinates transport this nonreducedness to every nonzero point of \(Z\). At the origin the same trace functions are not in the homogeneous quadratic defining ideal, while vanishing set-theoretically, so the local scheme is nonreduced there too. At every point outside \(Z\), tangent dimension equals the local reduced component dimension \(2r+2\), hence the local scheme is regular (therefore reduced). This proves that its nonreduced locus is **exactly** \(Z\).

**4. Rational-point enumeration.** Put \(s=\#\mathbf P^2(\mathbb F_q)=q^2+q+1\). Every nonzero tuple on each component uniquely determines its line or plane and has \(q^{2r}-1\) possibilities in the corresponding vector-bundle fiber. Thus each component has \(1+s(q^{2r}-1)\) points. Every nonzero tuple in \(Z\) uniquely determines a flag, of which there are \(s(q+1)\), and has \(q^r-1\) nonzero fiber choices. Inclusion-exclusion gives the two displayed formulas.

## Verification
The bundled standalone file `verify.py` reconstructs all matrix products and tangent Jacobians directly from coordinates. It exhaustively checks all mutually annihilating \(3\times3\) matrix pairs over \(\mathbb F_2\) and \(\mathbb F_3\), yielding respectively \(148\) and \(1665\) pairs, and tests the four tangent-rank strata for \(r=2,3,4,5\) in characteristics \(2,3,5,7\). Execution terminates with `VERIFY_OK_RADICAL_SQUARE_ZERO_REP_SCHEME 68`. The symbolic geometric and tangent calculations above, rather than finite enumeration alone, prove the theorem for all indicated fields and \(r\).

## Relationship to prior work
Morrison's 1980 *The Scheme of Finite-Dimensional Representations of an Algebra* studies representation schemes, includes the two-generator square-zero algebra, describes irreducible components and develops a tangent/deformation framework. Schröer's 2002 *Varieties of pairs of nilpotent matrices annihilating each other* determines irreducible components for annihilating pairs; thus the \(r=2\) reduced component assertion alone is not new. Bleher–Chinburg–Huisgen-Zimmermann (2014) already classifies components of arbitrary radical-square-zero module varieties; the general two-component **reduced** classification is likewise prior work. The present scope is instead the **exact locus of nonreducedness of the natural quadratic representation scheme**, its uniform tangent-dimensional jumping profile and its arithmetic intersection formula in dimension three for all \(r\ge2\). The inspected component classifications do not assert these scheme-level results; historical implicit coverage cannot be categorically excluded.

## Limitations
The dimension of the representation is fixed to three, the algebra is local with radical square zero, and the geometric conclusions concern the specified quadratic scheme and its reduction, not schemes obtained by imposing extra radical equations. The results do not describe multiplicities or full local Artin structures of the nilpotent thickening. The nonreduced-support and tangent assertions are not claims of previously unknown irreducible components. Independent mathematical validation has not been performed; possible implicit coverage in older deformation-theoretic literature is a remaining priority risk.

## References
1. K. Morrison, *The Scheme of Finite-Dimensional Representations of an Algebra*, Pacific Journal of Mathematics 91 (1980), 199–221. https://msp.org/pjm/1980/91-1/pjm-v91-n1-p17-s.pdf
2. J. Schröer, *Varieties of pairs of nilpotent matrices annihilating each other*, arXiv:math/0211293 (first arXiv posting 19 November 2002). https://arxiv.org/abs/math/0211293
3. F. M. Bleher, T. Chinburg and B. Huisgen-Zimmermann, *The geometry of finite dimensional algebras with vanishing radical square*, arXiv:1407.3045 (11 July 2014). https://arxiv.org/abs/1407.3045
4. B. Huisgen-Zimmermann, *Irreducible components of varieties of representations I. The local case*, arXiv:1410.3166 (2014). https://arxiv.org/abs/1410.3166
