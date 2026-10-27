# The four singular fibres of the Wiman–Edge pencil in characteristic three

## Finding
Let \(k\) be an algebraically closed field of characteristic \(3\). Put
\[
Q=x^6+y^6+z^6+(x^2+y^2+z^2)(x^4+y^4+z^4)-12x^2y^2z^2,
\qquad P=(x^2-y^2)(y^2-z^2)(z^2-x^2),
\]
and denote by \(D_t\subset\mathbb P^2_k\) the sextic \(Q+tP=0\), with \(D_\infty\) given by \(P=0\). Blow up the four points \(B=\{[1:\epsilon:\eta]:\epsilon,\eta\in\{1,-1\}\}\) to obtain the degree-five del Pezzo surface \(S\). The associated pencil on \(S\) consists of the divisors cut out by the strict-transform linear system \(6H-2\sum_{b\in B}E_b\), including exceptional components whenever their multiplicity is greater than two.

Exactly **four parameter values** give singular divisors in this characteristic-three pencil: \(t=0\), \(t=\infty\), and the two solutions of \(t^2+1=0\). More precisely:

* If \(t\ne 0,\infty\) and \(t^2+1\ne0\), then \(D_t\) is irreducible with precisely four unibranch cusps of local type \(h^2-u^3=0\) at \(B\); its strict transform on \(S\) is smooth of genus \(6\).
* If \(t^2+1=0\), then \(D_t\) is irreducible with those four cusps and **six additional ordinary nodes**, two on each coordinate axis, specified cyclically by \(x=0\), \(y^2=t z^2\). Its strict transform on \(S\) is an irreducible rational curve with precisely six nodes.
* \(D_0\) is the union of the smooth conic \(x^2+y^2+z^2=0\) and the four distinct lines \(x+y+z=0\), \(x+y-z=0\), \(x-y+z=0\), \(-x+y+z=0\). Each line is tangent to the conic at a different point of \(B\). There are six further ordinary nodes among the lines. On \(S\), the five proper transforms meet in exactly ten ordinary nodes with dual graph \(K_5\).
* \(D_\infty\) is the union of six lines \(x\pm y=0\), \(y\pm z=0\), \(z\pm x=0\). It has four ordinary triple points at \(B\) and three ordinary nodes at the coordinate vertices. On \(S\), its divisor comprises the six strict transforms and the four exceptional curves, with exactly fifteen ordinary nodes and Petersen dual graph.

Thus a classical characteristic-zero pencil with five singular divisors has a four-point singular-parameter support in characteristic \(3\), and its plane models change their four fixed ordinary nodes into wild cusps on every nonzero finite member.

## Assumptions and scope
All assertions are geometric over an algebraically closed field \(k\) of characteristic exactly \(3\). The chosen *integral equations and parameter normalization* matter; no claim is made that the same parameter labels apply to another choice of pencil generators. The four points of \(B\) are in general position, so \(S\) is a smooth quintic del Pezzo surface. At \(t=\infty\), "the divisor on \(S\)" includes components of the exceptional divisor left after removing the prescribed multiplicity two at each blown-up point.

## Proof
Set \(A=x^2\), \(B'=y^2\), \(C=z^2\), \(U=A+B'+C\), \(V=AB'+B'C+CA\), and \(\Delta=(A-B')(B'-C)(C-A)\). Exact reduction of the two classical integral generators modulo \(3\) gives
\[
F_t=Q+tP=U(V-U^2)+t\Delta.
\]
In the cubic polynomial \(G_t(A,B',C)=U(V-U^2)+t\Delta\), differentiation gives the characteristic-three identity
\[
\partial_A G_t+\partial_{B'}G_t+\partial_CG_t=-U^2.
\]
For \(t\ne0\), suppose a singular point of \(D_t\) has \(xyz\ne0\). Because \(2x,2y,2z\) are nonzero, its three partial derivatives imply \(\partial_AG_t=\partial_{B'}G_t=\partial_CG_t=0\). Therefore \(U=0\); the curve equation then forces \(\Delta=0\). In characteristic \(3\), \(U=0\) together with equality of any two of \(A,B',C\) forces equality of all three. Hence this point lies in \(B\), and direct substitution confirms all four are singular.

For singularities on an axis, cyclic symmetry reduces to \(x=0\). Write \(z=1\), \(b=y^2\ne0\). Then
\[
F_t(0,b,1)=-(b-1)(b^2+tb-1).
\]
The point is singular precisely when this binary cubic has a multiple root: \(b=1\) is simple for \(t\ne0\), whereas \(b^2+tb-1\) has repeated root if and only if \(t^2+1=0\), in which case it is \((b-t)^2\). Thus exactly two points on each axis arise at those two parameters. None of the three coordinate vertices lies on any finite member, since \(Q(1,0,0)=-1\ne0\) in characteristic \(3\).

At \([1:1:1]\), use affine local coordinates \(x=1+u\), \(y=1+h-u\), \(z=1\). Expanding modulo \(3\), the homogeneous term of order two is \(-h^2\), and the cubic term restricted to the tangent \(h=0\) is \(tu^3\). For \(t\ne0\), the blowup \(h=uw\) yields strict-transform equation \(-w^2+tu+\text{terms of order at least two}=0\), which is smooth at \((u,w)=(0,0)\). Weierstrass preparation in \(h\), completion of its square (since \(2\) is invertible), and absorption of the remaining unit by a square root put the completed local equation in the form \(h^2-tu^3=0\); rescaling gives \(h^2-u^3=0\). This is one unibranch cusp of delta invariant one. Coordinate sign changes carry this calculation to each point of \(B\).

At an additional axis point, take \(x=0\), \(z=1\), \(b=y^2=t\) and \(t^2=-1\). The coefficient of \(x^2\) is \(\partial_A G_t(0,t,1)=t\), nonzero. Meanwhile \(F_t(0,b,1)=-(b-1)(b-t)^2\), so the transverse quadratic coefficient along the axis is nonzero because \(t\ne1\). Its tangent cone is a nondegenerate binary quadratic, proving an ordinary node.

For \(t\ne0,\infty\), the listed local germs are unibranch cusps or ordinary nodes. Outside \(t^2=-1\) only cusps occur, so a reducible sextic would have to have an intersection of distinct components at a unibranch cusp, impossible by Bezout and uniqueness of the local branch. At \(t^2=-1\), if a reducible sextic had no linear component, one of its irreducible components would have degree \(d\) with \(2\le d\le3\); its intersection number with the complementary divisor would then be \(d(6-d)\ge8\). Yet all cross-component intersections must be among the six ordinary nodes, each contributing at most one. Hence a linear component must exist. It would have to meet the degree-five residual divisor at five of the six nodes. But the six nodes lie in pairs on the three coordinate axes, and no line contains more than three of them. Contradiction. Thus the exceptional sextics are also irreducible. The plane arithmetic genus is ten, so subtraction of four cusp delta invariants gives genus six generally, and subtraction of the six additional node invariants gives genus zero exceptionally.

For \(t=0\), the polynomial identity
\[
V-U^2=(x+y+z)(x+y-z)(x-y+z)(-x+y+z)
\]
holds after \(A=x^2,B'=y^2,C=z^2\) in characteristic \(3\). The conic \(U=0\) is smooth. Its intersection with each line is twice the appropriate point of \(B\), as substitution reduces the conic equation to a nonzero scalar times a square. The four lines have six distinct pairwise intersection points, all off the conic; they are ordinary nodes. A blowup at a conic-line tangency of order two changes it to a single transverse intersection. Thus the five strict transforms on \(S\) form a reduced nodal divisor with one edge between each pair, i.e. \(K_5\).

At infinity, \(\Delta=0\) is the six-line arrangement. Its four triple and three double intersections follow directly by checking the six equations, and exhaust their fifteen pairwise intersections. Each of the four triple points gives three distinct strict-transform contact points on its exceptional curve; because the original divisor has multiplicity three there, the pencil divisor on \(S\) also contains that exceptional curve once. Its ten components have precisely fifteen nodes; the six transforms of lines through pairs of blown-up points together with the four exceptional curves give the standard Petersen incidence graph. This completes the singular-fibre classification.

## Verification
Run `python verify.py` with Python 3 and SymPy installed. It checks the reduced coefficient identities, derivative identity, axis restriction, exceptional node coefficient, cusp Taylor coefficients, general position of the four blowup centers, and six distinct off-conic line-line intersections by exact polynomial arithmetic modulo \(3\). The execution produced `VERIFY_OK`. The argument for irreducibility and for completeness of the singular classification is mathematical and is explicitly proved above; the script is a check of its critical algebra, not a substitute for that proof.

## Relationship to prior work
W. L. Edge's classical paper *A pencil of four-nodal plane sextics* constructs the pencil and identifies its five singular members in characteristic zero. Inoue–Kato study the corresponding geometry over fields with characteristic different from \(2,3,5\). Candelas–de la Ossa–van Geemen–van Straten (arXiv:1206.4961, publicly submitted June 21, 2012) relate the same Wiman pencil to lines on the Dwork quintic and characterize the ordinary six-node degeneration. Dolgachev–Farb–Looijenga give equations and the two classical reducible five-component members. Giulietti–Kawakita–Lia–Montanucci (arXiv:1805.06317, 2018) explicitly note that the isolated Wiman sextic is reducible in characteristics two and three. These known facts are not the new contribution. The theorem above determines **every geometric fibre of the specifically reduced pencil in characteristic three**, including the fixed wild cusp germs, absence of further singularities, the exceptional parameters, irreducibility and genera, and the dual graphs after the four-point blowup.

## Limitations
This is a geometric classification of fibres of the specified integral model, not a claim about stable reduction of a total family over a mixed-characteristic DVR, not a description of relative automorphism schemes, and not a claim about the complete moduli-theoretic degeneration. The choice of reduction and parameter matters. An equivalent historical characteristic-three singular-fibre computation may be hidden in less accessible literature; the literature search establishes plausible independence from inspected statements but not global uniqueness. No independent scientific audit has been performed.

## References
1. W. L. Edge, *A pencil of four-nodal plane sextics*, Proc. Edinburgh Math. Soc., 1982 (original paper and equations). https://webhomes.maths.ed.ac.uk/cheltsov/edge2021/pdf/1982b.pdf
2. N. Inoue and F. Kato, *On the geometry of Wiman's sextic*, 2005 preprint. https://www.math.kyoto-u.ac.jp/preprint/2005/2inoue.kato.pdf
3. P. Candelas, X. de la Ossa, B. van Geemen, and D. van Straten, *Lines on the Dwork Pencil of Quintic Threefolds*, arXiv:1206.4961, first submitted 2012-06-21. https://arxiv.org/abs/1206.4961
4. I. Dolgachev, B. Farb, and E. Looijenga, *Geometry of the Wiman–Edge pencil, I: algebro-geometric aspects*, 2018. https://doi.org/10.1007/s40879-018-0231-3
5. M. Giulietti, M. Kawakita, S. Lia, and M. Montanucci, *An \(\mathbb F_{p^2}\)-maximal Wiman's sextic and its automorphisms*, arXiv:1805.06317, 2018. https://arxiv.org/abs/1805.06317
