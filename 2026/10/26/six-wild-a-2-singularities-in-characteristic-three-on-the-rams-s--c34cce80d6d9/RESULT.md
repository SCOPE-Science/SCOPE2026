# Six wild \(A_2\) singularities in characteristic three on the Rams–Schütt quartic \(\mathcal Z\) family

## Finding
Let \(k\) be algebraically closed of characteristic \(3\). In projective coordinates \([x:y:u:v]\), consider the natural quartic family
\[
X(q,g):\quad F=u x^3+v y^3+xyq(u,v)+g(u,v)=0,
\]
where \(q\) and \(g\) are homogeneous binary forms of degrees \(2\) and \(4\). Assume that \(q\) and \(g\) have simple projective roots, no common root, and that each of the two cubics \(P_r\) described below has three distinct roots. Then \(X(q,g)\) is geometrically integral and normal, and its singular support consists of **exactly six geometric points**, three over each projective zero of \(q\). Each has completed local equation
\[
\widehat{\mathcal O}_{X,P}\simeq k[[s,\xi,w]]/(s\xi+w^3).
\]
Thus all six are rational double points of type \(A_2\). In characteristic \(3\), however, each *Jacobian singular subscheme* is a curvilinear scheme of length \(3\), with completed local algebra \(k[[w]]/(w^3)\), so the entire Jacobian singular scheme has length \(18\). The minimal resolution is a K3 surface with six disjoint \(A_2\) exceptional chains (twelve exceptional \((-2)\)-curves).

These hypotheses define a nonempty parameter locus: the example
\[
q=uv,\qquad g=u^4+u^3v+2uv^3+v^4
\]
over \(\mathbb F_3\) satisfies them. Its six singular points are defined over \(\mathbb F_{27}\) and form two Frobenius orbits of length \(3\); none is \(\mathbb F_3\)-rational.

## Assumptions and scope
The assertion applies to the **coefficientwise characteristic-three members** of the displayed equation from the \(\mathcal Z\) family in Rams–Schütt's 2013 preprint. It does not assert that the smooth-characteristic definition of a line of the second kind remains unchanged in characteristic \(3\). The parameter conditions are explicit as follows.

At a simple zero \([r:1]\) of \(q\), use \(v=1\), put \(Q(t)=q(t,1)\), \(G(t)=g(t,1)\), and choose \(a,b\in k\) with \(a^3=r\), \(b^3=G(r)\). Require that
\[
P_r(X)=X^3+Q'(r)X(-aX-b)+G'(r)
\]
have distinct roots. At a zero \([1:r]\) examined in the chart \(u=1\), interchange \((x,u)\) with \((y,v)\) and use \(Q(t)=q(1,t)\), \(G(t)=g(1,t)\): require the analogous cubic
\[
P_r(Y)=Y^3+Q'(r)Y(-aY-b)+G'(r)
\]
to be separable. Either affine chart may be used when both coordinates are nonzero. Squarefreeness means no repeated projective root. These are checkable, open conditions (the cubic discriminants can be tested after a purely inseparable field extension), and the specified rational example proves nonemptiness.

The singular scheme is the intrinsic Jacobian/Fitting singular subscheme of the hypersurface, rather than just the set of geometric singular points. No claims are made about a complete line configuration or a quasi-elliptic fibration on the resolution.

## Proof
**Step 1: No singularity away from \(q=0\).** In characteristic \(3\), differentiation gives
\[
F_x=yq,\qquad F_y=xq,\qquad
F_u=x^3+xyq_u+g_u,\qquad F_v=y^3+xyq_v+g_v.
\]
On the line \(u=v=0\), the last two derivatives are \(x^3,y^3\), which cannot vanish together at a projective point. Off this line, if \(q(u,v)\neq0\), the first two derivatives force \(x=y=0\). The equation then gives \(g(u,v)=0\), but a simple zero of a binary quartic has nonzero projective gradient; thus such a point is smooth.

**Step 2: Exactly three points above each root of \(q\).** Fix a simple zero \([r:1]\) of \(q\) and work in \(v=1\). Set \(t=u\), \(s=t-r\), and \(w=ax+y+b\) with \(a^3=r\), \(b^3=G(r)\). Since \(Q(r)=0\), the restriction of \(F\) to \(s=0\) is \(w^3\), and exact polynomial division gives
\[
F=w^3+sH(s,x,w),\qquad H(0,x,0)=P_r(x).
\]
On \(s=0\), the equation \(F=0\) forces \(w=0\). Its other gradient equations reduce to \(P_r(x)=0\), because \(\partial_w(w^3)=0\) in characteristic three and the remaining partials have a factor \(s\). The cubic is monic and squarefree by hypothesis, so these are three distinct finite points. If the root of \(q\) lies at infinity, the identical argument in \(u=1\) gives three further points. Step 1 shows there are no other geometric singular points.

**Step 3: Exact local model and scheme length.** At any one of these points \(x=x_0\), separability says \(\partial H/\partial x\,(0,x_0,0)=P_r'(x_0)\neq0\). Consequently \((s,\xi=H,w)\) are regular completed local coordinates. In those coordinates \(F=s\xi+w^3\) **exactly**, not just modulo higher powers. This is the two-dimensional rational double-point equation of type \(A_2\). Its hypersurface Jacobian ideal in ambient coordinates is \((s,\xi,w^3)\): differentiation yields \(\xi,s,0\), and retaining the equation forces \(w^3=0\). The Jacobian subscheme therefore has local algebra \(k[[w]]/(w^3)\), length \(3\), and Hilbert function \((1,1,1)\). Six points yield total length \(18\).

**Step 4: Normality and resolution.** A reducible projective hypersurface of degree four in \(\mathbb P^3\) has a positive-dimensional singular locus where its positive-degree components intersect (including the nonreduced case). As the singular support here is finite, \(X\) is geometrically integral. Being a hypersurface it satisfies \(S_2\), and isolated singularities give \(R_1\), hence normality. The crepant minimal resolution of its six \(A_2\) rational double points has trivial canonical bundle and \(H^1(\mathcal O)=0\), as for a normal quartic with rational double points; thus it is K3, with one two-curve chain over each singularity.

**Step 5: Explicit witness.** For \(q=uv\), \(g=u^4+u^3v+2uv^3+v^4\), the dehomogenized quartic \(G(t)=t^4+t^3+2t+1\) has \(G'(t)=t^3+2=(t-1)^3\), whereas \(G(1)=2\neq0\); hence \(G\) has simple roots, and \(g\) is nonzero at both zeros of \(q\). In \(v=1\) near \(u=0\), with \(w=y+1\), the **exact** equation is
\[
F=w^3+u\bigl(x^3+xy+u^3+u^2+2\bigr).
\]
On \(u=w=0\), its three singular coordinates are the simple roots of \(x^3-x+2\); its derivative is \(-1\). In \(u=1\) near \(v=0\), with \(w=x+1\), the exact equation is
\[
F=w^3+v\bigl(y^3+xy+1+2v^2+v^3\bigr),
\]
and the other three singular coordinates solve \(y^3-y+1=0\), again with derivative \(-1\). Both polynomials have no \(\mathbb F_3\) root and are irreducible cubics, so the two sets form two Frobenius 3-cycles over \(\mathbb F_{27}\).

## Verification
Run `python3 verify_z3.py` (Python standard library only). It constructs \(\mathbb F_{27}=\mathbb F_3[t]/(t^3-t-1)\), enumerates every point of \(\mathbb P^3(\mathbb F_{27})\), evaluates the original homogeneous quartic and all four partial derivatives, and finds exactly six singular points in the two predicted groups. It also checks the local polynomial identities over characteristic three and the nonzero coordinate-change Jacobians for those points. The program returns `VERIFY_OK`.

Finite-field enumeration is a **witness consistency test**, not a proof that no singularities exist over larger algebraic extensions or for arbitrary parameters. The infinite-field and scheme-theoretic statements are established by Steps 1–4, where the polynomial factorizations and formal inverse-function criterion supply the proof. In particular, the wild Jacobian length is computed from the characteristic-three local equation, not extrapolated from the six-point enumeration.

## Relationship to prior work
Rams and Schütt, *On quartics with lines of the second kind*, arXiv:1303.1304v1 (first public 6 March 2013), §7 equation (7.2), introduce this \(\mathcal Z\) equation and analyze **smooth surfaces in characteristics different from \(2,3\)**. Their generic smooth-characteristic fibre analysis yields six \(I_3\) and six \(I_1\) fibres, and does not contain this bad-characteristic singularity calculation. Their 2014 *112 lines on smooth quartic surfaces (characteristic 3)* concerns smooth quartics and global line bounds, and does not entail the singular scheme here. Veniani's *Lines on K3 quartic surfaces in characteristic 3* (published online 2021), treats singular K3 quartics and bounds their lines, but gives no equivalent classification of the explicit \(\mathcal Z\) specialisation in its inspected statements/examples. Katsura and Schütt, *The 3-divisibility of divisors on K3 surfaces in characteristic 3* (2026), study abstract configurations of six or nine \(A_2\) chains; those general lattice statements neither single out this \(\mathcal Z\) equation nor imply its six singularity locations or local Jacobian length.

## Limitations
This is a conditional classification on the explicitly specified nonempty parameter locus, not every singular degeneration of \(\mathcal Z\). The six \(A_2\) points need not be rational over the ground field. The local scheme length \(3\) is for the Jacobian/Fitting singular scheme in characteristic \(3\), not the length of the exceptional divisor or the dimension of a smooth deformation space. A further historical occurrence of the same explicit normal-form calculation is possible; no independent audit has been performed.

## References
1. S. Rams and M. Schütt, *On quartics with lines of the second kind*, arXiv:1303.1304v1, 6 March 2013, esp. §7 (equation (7.2)); https://arxiv.org/abs/1303.1304.
2. S. Rams and M. Schütt, *112 lines on smooth quartic surfaces (characteristic 3)*, arXiv:1409.7485, 26 September 2014; https://arxiv.org/abs/1409.7485.
3. D. C. Veniani, *Lines on K3 quartic surfaces in characteristic 3*, published online 7 February 2021; https://doi.org/10.1007/s00229-021-01284-9.
4. T. Katsura and M. Schütt, *The 3-divisibility of divisors on K3 surfaces in characteristic 3*, arXiv:2604.25227v1, 28 April 2026; https://arxiv.org/abs/2604.25227.
