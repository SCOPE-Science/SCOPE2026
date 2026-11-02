# An order-two toric extension at the double-tacnode boundary of a genus-three quartic pencil

## Finding
Over \(\mathbb C\), consider the family of plane quartics
\[
C_a:\quad X^4+Y^4+Z^4+aX^2Y^2=0,
\]
with \(a^2\ne4\), and its degeneration \(a=2+t^4\) over \(\mathbb C[[t]]\). Its Deligne–Mumford stable special fiber \(C_0^{\mathrm{st}}\) is the union of **two smooth genus-one curves** \(E_1,E_2\), joined transversely at exactly two nodes. Each \(E_i\) is isomorphic to the smooth completion of
\[
E:\quad w^2+v^4=1
\]
and has \(j(E_i)=1728\). The two nodes mark two distinct points \(P_i^+,P_i^-\) on each \(E_i\). The difference \(T_i=[P_i^+-P_i^-]\in\operatorname{Pic}^0(E_i)\) is **nonzero of exact order two**.

Consequently the identity component of the special-fiber Picard scheme has the exact semiabelian sequence
\[
1\longrightarrow\mathbb G_m\longrightarrow
\operatorname{Pic}^0(C_0^{\mathrm{st}})\longrightarrow E_1\times E_2\longrightarrow0.
\]
Its class in \(\operatorname{Ext}^1(E_1\times E_2,\mathbb G_m)\cong E_1^\vee\times E_2^\vee\) is \((T_1,-T_2)\), up to simultaneous reversal of the nodal labels. In particular it has **exact order two**, rather than zero or infinite order. Pullback by the multiplication-by-two isogeny on \(E_1\times E_2\) splits this extension; the extension itself is nonsplit.

The analogous assertion holds at \(a=-2\) by the coordinate change \(Y\mapsto iY\).

## Assumptions and scope
The base field is \(\mathbb C\). Stable reduction is taken after the specified base change \(a-2=t^4\); all assertions concern this explicit one-parameter degeneration and the identity component of the generalized Jacobian of its stable special fiber. A general member is smooth of genus three because the gradient equations for the homogeneous quartic have no simultaneous nontrivial solution when \(a^2\ne4\). The asserted order is in the group of extensions of algebraic groups over \(\mathbb C\), **not** a numerical conductor, monodromy exponent, or class in an integral Néron model. The two elliptic curves are treated with their two nodal attachments, not merely with their \(j\)-invariants.

## Proof
At \(a=2\), the quartic factors as
\[
(X^2+Y^2+iZ^2)(X^2+Y^2-iZ^2).
\]
Both factors are smooth conics. They have exactly two intersection points \([1:i:0]\), \([1:-i:0]\), of local intersection multiplicity two each. Thus the special plane quartic has exactly two tacnodes of type \(A_3\) and no other singularities.

In the affine chart \(X=1\), near **either** tacnode introduce \(u=1+Y^2\) and \(v=Z\). The differential of \(u\) at either tacnode is \(2Y\ne0\), so \(u,v\) are regular local coordinates. Setting \(a=2+t^4\) gives exactly
\[
u^2+v^4+t^4(u-1)=0.
\]
With \(U=u+t^4/2\) this becomes
\[
U^2+v^4=t^4(1+t^4/4).
\]
The invertible formal substitution \(r=t(1+t^4/4)^{1/4}\) makes the completed local family \(U^2+v^4=r^4\); in particular no further ramified extension is required after this base change.

Take the weighted blow-up of the three local coordinates \((U,v,r)\) with weights \((2,1,1)\). In the \(r\)-chart, write \(U=r^2w\), \(v=rV\); the proper transform is the smooth genus-one curve \(w^2+V^4=1\), with \(r\) a transverse parameter. In the \(v\)-chart, \(U=v^2w\), \(r=vR\), and the strict transform is
\[
w^2+1-R^4=0,\qquad r=vR.
\]
The chart is smooth at \(v=R=0\), where \(w=\pm i\), and \(r=vR\) exhibits ordinary transverse nodes between the exceptional genus-one curve \(v=0\) and the strict transforms of the two conics \(R=0\). The charts agree on overlaps, and away from the two tacnodes the original total family is already smooth. Consequently the semistable central fiber is made of the two original conics and the two exceptional elliptic curves, with four ordinary double points and incidence graph \(K_{2,2}\). Its arithmetic genus is \(1+1+(4-4+1)=3\), as required. Each conic is rational, meets the rest twice, and is unstable; contracting the two conics replaces their degree-two vertices by edges. The stable fiber therefore consists of \(E_1\) and \(E_2\) with two nodes.

To identify the marked points, take the smooth projective completion of \(w^2+V^4=1\). Near \(V=\infty\), set \(z=1/V\), \(h=w/V^2\). Its equation becomes \(h^2+1=z^4\). The two attachments are \(P^+=(z,h)=(0,i)\) and \(P^-=(0,-i)\). They are distinct. The involution \(\sigma:(V,w)\mapsto(-V,w)\) fixes both points, and has exactly four fixed points on the genus-one curve (the two points with \(V=0\), plus \(P^+,P^-\)). Taking \(P^+\) as the origin, \(\sigma\) is an order-two automorphism fixing the origin and having four fixed points, hence it is the inversion automorphism \([-1]\). Its fixed points are exactly \(E[2]\), so \(T=P^--P^+\) is a **nonzero element of \(E[2]\)**. The binary quartic defining \(E\) has invariant \(J=0\), \(I\ne0\), giving \(j=1728\); equivalently the automorphism \(V\mapsto iV\) supplies the complex multiplication symmetry.

Finally, normalize the stable curve at its two nodes. The normalization is \(E_1\sqcup E_2\), and a degree-zero line bundle on the nodal curve consists of two degree-zero line bundles together with two identifications of their fibers at the respective pairs of attachments. Modulo simultaneous rescaling, these identifications give a single \(\mathbb G_m\)-parameter, yielding the displayed semiabelian exact sequence. The standard gluing/Poincaré-bundle construction identifies its class with the difference of the two gluing evaluations on each elliptic factor, namely \(([P_1^+-P_1^-],[P_2^--P_2^+])\). Since both components are nonzero elements of order two, the extension class has exact order two and is nonzero. Pulling it back along \([2]:E_1\times E_2\to E_1\times E_2\) annihilates the class and splits the resulting extension.

## Verification
A standalone verifier (`verify.py`, executed with Python 3 and SymPy) checks the two conic factorizations, the smoothness criterion for general fibers, the exact local completing-the-square identity, both weighted-blowup chart equations, the nonsingular elliptic equation, its invariant \(j=1728\), the distinct transverse attachments, and the genus/graph count. These identities are exact symbolic calculations, not finite sampling. The proof of exact order two follows geometrically from the four fixed points of the involution and the standard line-bundle gluing description; this last argument is recorded above and is not outsourced to a black-box algebraic computation.

## Relationship to prior work
Badr and Saleem (first public arXiv submission 2012-12-12, arXiv:1212.2708) analyze smooth members of the symmetric Kuribayashi plane-quartic family, explicitly excluding the singular limiting parameters \(a=\pm2\); their flex classification does not determine the gluing class of the stable limiting Jacobian. Hassett and Hyeon (arXiv:0806.3444, 2008-06-20) supply the classical geometry connecting tacnodes to elliptic bridges, but not the marked elliptic data in this named pencil. Bouw, Coppola, Kılıçer, Kunzweiler, Lorenzo García and Somoza (arXiv:2003.07633, first submitted 2020-03-17) prove a much broader stable-reduction classification for Ciani curves and explicitly cover configurations with two isomorphic elliptic components of \(j=1728\) meeting twice (notably Lemma 13, Theorem 3 and Corollary 2). Therefore **the stable graph and component \(j\)-invariants are not claimed as new**. Their results identify such reduction types, whereas the present precisely marked limit computes the nontrivial order-two class in \(\operatorname{Ext}^1(E_1\times E_2,\mathbb G_m)\). Neither the abstract reduction type nor the unordered \(j\)-invariants alone determine this extension class. It may be recoverable as a special consequence of that paper's more detailed admissible-cover construction; historical priority for this precise extension-class formula therefore remains a residual risk.

## Limitations
No general classification of all Ciani degenerations, no claim to a new topological stable-reduction type, and no independently validated historical priority are asserted. The formula is for the explicit pencil and its specified degeneration. The order-two result concerns the geometric semiabelian special fiber, not the integral monodromy pairing or a global Néron model.

## References
- S. Badr and F. Saleem, *Flexes of smooth plane quartics with many automorphisms*, arXiv:1212.2708 (2012-12-12).
- B. Hassett and D. Hyeon, *Log minimal model program for the moduli space of stable curves: The first flip*, arXiv:0806.3444 (2008-06-20).
- I. Bouw, N. Coppola, P. Kılıçer, S. Kunzweiler, E. Lorenzo García, A. Somoza, *Reduction type of genus-3 curves in a special stratum of their moduli space*, arXiv:2003.07633 (2020-03-17), especially Lemma 13 and Corollary 2.
