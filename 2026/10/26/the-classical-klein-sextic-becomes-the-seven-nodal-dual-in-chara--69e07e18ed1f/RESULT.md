# The classical Klein sextic becomes the seven-nodal dual in characteristic two

## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\). The smooth Klein plane quartic
\[
C=V(f),\qquad f=x^3y+y^3z+z^3x
\]
has reduced projective dual the irreducible sextic
\[
D=V(G),\qquad G=AB^5+BC^5+CA^5+A^2B^2C^2.
\]
This is exactly the coefficientwise characteristic-two reduction of Klein's classical integral sextic invariant \(AB^5+BC^5+CA^5-5A^2B^2C^2\). The singularities of \(D\) are precisely seven ordinary nodes
\[
\left\{[1:t:t^5]:t^7=1\right\}\subset\mathbb P^2(\mathbb F_8).
\]
The normalization of \(D\) is isomorphic to the Frobenius twist \(C^{(2)}\), and the Gauss map \(C\to D\) factors through relative Frobenius with purely inseparable degree \(2\). These seven nodes represent *all* seven geometric bitangents of \(C\), namely the lines \(x+ty+t^5z=0\) for \(t^7=1\).

## Assumptions and scope
All scheme and normalization assertions are geometric over any algebraically closed \(k\) of characteristic \(2\). The coordinates \([A:B:C]\) are dual to \([x:y:z]\). By the projective dual we mean the reduced Zariski closure of the tangent-line image of the smooth plane curve, not a special fibre of the characteristic-zero dual. An ordinary node means an ordinary geometric double point with two distinct tangent directions. The seven displayed node coordinates are already defined over \(\mathbb F_8\). No claim is made about the full integral relative dual family over the integers.

## Proof
**(1) Smoothness.** The partial derivatives of \(f\) are \(x^2y+z^3\), \(x^3+y^2z\), and \(y^3+z^2x\). A simultaneous zero in projective space cannot have a zero coordinate. Normalizing \(x=1\), write \(y=t\). The other equations imply \(z=t^{-2}\) and \(t^7=1\). At such a point, \(f=t+t+t=t\ne0\). Thus no gradient-zero point lies on \(C\), proving smoothness. The plane-quartic genus is \(3\).

**(2) Gauss image identity.** Write
\[
(a,b,c)=(x^2y+z^3,\ x^3+y^2z,\ y^3+z^2x).
\]
Direct polynomial multiplication in characteristic two gives the *exact identity*, in \(k[x,y,z]\),
\[
G(a,b,c)=f\,Q,\quad Q=x^{14}+y^{14}+z^{14}+x^8y^4z^2+x^4y^2z^8+x^2y^8z^4.
\]
Therefore the Gauss image lies in \(D\). It is a curve (the tangent lines at the three coordinate points of \(C\) are three distinct coordinate lines).

**(3) Complete singularity classification and irreducibility.** The three partials of \(G\) are
\[
G_A=B^5+A^4C,\quad G_B=C^5+AB^4,\quad G_C=A^5+BC^4.
\]
Their common projective zeros cannot have a zero coordinate. Normalize \(A=1\) and \(B=t\ne0\). The equations then give \(C=t^5\) and \(t^{21}=1\). At these critical points,
\[
G(1,t,t^5)=t^{12}(1+t^{14}),
\]
so membership in \(D\) is equivalent to \(t^7=1\). These are exactly seven distinct geometric points. On the affine chart \(A=1\), the mixed second partial \(G_{BC}=C^4\) is nonzero at each. Because the quadratic tangent cone in characteristic two has nonzero cross coefficient, each singular point is an ordinary node. In particular \(G\) is reduced, since its singular support is finite.

To see absolute irreducibility, suppose this reduced sextic were reducible. Splitting the factors into two groups of degrees \(d\) and \(6-d\), with \(2\le d\le4\), Bézout gives at least \(8\) units of intersection multiplicity, whereas at most seven ordinary nodes are available, each contributing exactly one. The remaining possibility is a line component meeting its degree-five complement in five distinct nodes, but no line contains five of the seven points. Indeed, restricting a line to the seven points gives \(a+bt+ct^5\) for the seven seventh roots of unity. If \(c\ne0\) and five distinct roots vanished, the absent \(t^4\) coefficient would force their sum to be zero. The sum of all seven roots is zero, so the other two distinct seventh roots would also sum to zero; in characteristic two this is impossible. If \(c=0\) the polynomial has degree at most one. Thus \(G\) is absolutely irreducible. Being an irreducible curve containing the one-dimensional Gauss image, it equals the reduced projective dual.

**(4) Frobenius and bitangents.** The normalization \(\widetilde D\) has arithmetic genus \((6-1)(6-2)/2=10\) minus seven node defects, hence genus \(3\). The Gauss morphism has \(\gamma^*\mathcal O_D(1)=\mathcal O_C(3)\) of degree \(12\). Since \(\deg D=6\), its degree over \(\widetilde D\) is exactly \(2\). If this degree-two morphism were separable, Riemann–Hurwitz between genus-three curves would require \(4\ge 2\cdot4=8\), a contradiction. The map is therefore purely inseparable; the unique degree-two purely inseparable subfield of \(k(C)\) is \(k(C)^2\), so \(\widetilde D\cong C^{(2)}\) and \(\gamma\) factors through relative Frobenius.

The normalization map is bijective away from the nodes and has exactly two geometric preimages over each node. Since the inseparable morphism \(C\to\widetilde D\) is radicial, those two branches correspond to two distinct points of \(C\) with the same tangent line. They give a bitangent, and no other bitangent is possible: a second tangent point would force a second normalization branch. Hence there are exactly seven bitangents with the displayed equations.

## Verification
Run \(`python3 CHECK.py`\) with any standard Python 3 installation. It checks the characteristic-two Gauss polynomial identity by sparse exact polynomial multiplication, builds \(\mathbb F_8\) from the irreducible polynomial \(t^3+t+1\), and verifies the seven-node incidence bound (in fact any line through two of the seven nodes contains exactly three). The source-level proof, not finite enumeration, establishes geometric completeness, irreducibility, genus and Frobenius factorization.

## Relationship to prior work
Elkies, *The Klein Quartic in Number Theory*, equations (1.9), (1.13), gives the integral Klein quartic and sextic \(\Phi_6=AB^5+BC^5+CA^5-5A^2B^2C^2\), and treats characteristic-two arithmetic in section 3.3. The displayed characteristic-zero Hessian formula involves division by \(54\), so it cannot be specialized to characteristic two to infer the present duality. Müller and Ritzenthaler (2004), Proposition 2.2, cite the established equivalence between ordinarity and exactly seven bitangents for smooth plane quartics; a general bitangent count is *not* claimed here as a new discovery. Pellikaan (1998) describes the Klein quartic/Fano-plane incidence over finite fields. The contribution here is the exact dual equation, its full seven-node classification, its identification with the classical integral sextic reduction, and its explicit Frobenius normalization. No inspected full text establishes those combined assertions. The possibility of an equivalent historical description under different coordinates remains open to external verification.

## Limitations
The conclusion is geometric in characteristic two; it does not classify the characteristic-zero dual of degree twelve or a relative dual scheme over mixed characteristic. The seven bitangents and the invariant sextic independently have classical antecedents. Searches cannot establish uniqueness in the literature; uninspected historical sources may cover the exact connection. No independent validation has been performed.

## References
- Noam D. Elkies, *The Klein Quartic in Number Theory*, in *The Eightfold Way*, MSRI Publications 35 (1998), pp. 51–102, especially pp. 56–57 and section 3.3. https://library.slmath.org/books/Book35/files/elkies.pdf
- Jürgen Müller and Christophe Ritzenthaler, *On the ring of invariants of ordinary quartic curves in characteristic 2*, arXiv:math/0405052v1, first submitted 2004-05-04, particularly §2. https://arxiv.org/abs/math/0405052
- R. Pellikaan, *On the Klein quartic, the Fano plane and curves representing designs*, in *Codes, Curves and Signals* (1998), pp. 9–20. https://research.tue.nl/en/publications/on-the-klein-quartic-the-fano-plane-and-curves-representing-desig/
