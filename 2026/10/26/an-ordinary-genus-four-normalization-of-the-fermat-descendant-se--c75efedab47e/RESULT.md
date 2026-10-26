# An ordinary genus-four normalization of the Fermat-descendant sextic in characteristic three

## Finding
Let \(k\) be any field of characteristic \(3\), and let \(\lambda\in k^\times\). Consider the literal plane sextic
\[
D_\lambda:\quad X^6+Y^6+Z^6+\lambda X^2Y^2Z^2=0
\quad\subset\mathbb P^2_k.
\]
Its geometric normalization \(C_\lambda\) has genus \(4\), and \(D_\lambda\) is geometrically integral with precisely six geometric cusps, each with completed geometric local equation \(u^2+v^3=0\). The cusps form three pairs on the coordinate axes and each has \(\delta=1\).

Define the elliptic curves
\[
E_\lambda:\ U^3+V^3+W^3+\lambda UVW=0
\quad\subset\mathbb P^2_k,
\]
\[
F_\lambda:\quad y^2=x^3+2\lambda x^2+\lambda^2x-\lambda^2.
\]
Then over \(k\) there is an isogeny
\[
\operatorname{Jac}(C_\lambda)\ \sim_k\ E_\lambda\times F_\lambda^3.
\]
Both elliptic factors are ordinary for every nonzero \(\lambda\), so \(\operatorname{Jac}(C_\lambda)\) is ordinary, with \(3\)-rank \(4\), \(a\)-number \(0\), and Newton slopes \(0^{[4]},1^{[4]}\). There is no nonordinary parameter in this punctured pencil.

If \(\lambda\in\mathbb F_q^\times\), \(q=3^m\), and \(L_E(T),L_F(T)\) denote the usual degree-two Weil numerators, then
\[
Z(D_\lambda/\mathbb F_q,T)=Z(C_\lambda/\mathbb F_q,T)
=\frac{L_E(T)L_F(T)^3}{(1-T)(1-qT)}.
\]
In particular, the two \(\mathbb F_3\)-members have no \(\mathbb F_3\)-points, and their genus-four Weil numerators are
\[
\begin{aligned}
L_{C_1}(T)&=(1+2T+3T^2)(1-2T+3T^2)^3,\\
L_{C_2}(T)&=(1-T+3T^2)^4.
\end{aligned}
\]

## Assumptions and scope
All geometric claims are after extension to an algebraic closure of the characteristic-three base field. Every parameter \(\lambda\ne0\) is included, and \(\lambda=0\) is excluded because the sextic becomes the nonreduced cubic power \((X^2+Y^2+Z^2)^3\). Isogenies and the finite-field Weil-polynomial factorization are defined over the stated base field. The claim concerns the normalization of the literal plane equation, not the stable model of a characteristic-zero family and not classification up to isomorphism.

## Proof
**1. Six cusps and integrality.** The three partial derivatives of the sextic in characteristic \(3\) are \(2\lambda XY^2Z^2\), \(2\lambda X^2YZ^2\), and \(2\lambda X^2Y^2Z\). A geometric singular point therefore has at least one coordinate zero. On \(X=0\), the equation is \((Y^2+Z^2)^3=0\), giving two distinct geometric points (and similarly on the other two coordinate lines); no coordinate vertex lies on the curve. At a point with \(X=0\), take the local coordinate \(v=Y^2+Z^2\) and transverse coordinate \(u=X\) in an affine chart with a nonzero remaining coordinate. The equation becomes \(v^3+u^2\varepsilon(u,v)=0\), where \(\varepsilon\) is a unit since \(\lambda Y^2Z^2\ne0\) at the point. Over the algebraic closure, extracting a formal square root of this unit gives the completed equation \(v^3+u'^2=0\). Thus every singularity is a unibranch cusp of delta invariant one. The integral structure also follows independently from the connected Kummer covering constructed below. A plane sextic has arithmetic genus \(10\), hence geometric genus \(10-6=4\).

**2. The connected tame Klein-four cover.** Squaring coordinates gives a rational morphism from the normalization to \(E_\lambda\). Its function-field extension is obtained by adjoining square roots of \(U/W\) and \(V/W\). The plane cubic \(E_\lambda\) is nonsingular: its partial derivatives are \(\lambda VW,\lambda UW,\lambda UV\), and no coordinate vertex belongs to it. Its intersections with the three coordinate lines are the rational flexes
\[
P_U=[0:1:-1],\qquad P_V=[1:0:-1],\qquad P_W=[1:-1:0],
\]
each of contact multiplicity \(3\). Hence
\[
\operatorname{div}(U/W)=3P_U-3P_W,\qquad
\operatorname{div}(V/W)=3P_V-3P_W.
\]
The two square classes are independent: a square cannot have odd valuation at either \(P_U\) or \(P_V\). Thus the extension has degree \(4\), is geometrically connected, and has deck group \((\mathbb Z/2)^2\). It is tamely ramified precisely at \(P_U,P_V,P_W\), with two points of index \(2\) over each. Riemann--Hurwitz gives \(2g(C_\lambda)-2=4(2\cdot1-2)+3\cdot2=6\), hence \(g=4\), also proving geometric integrality.

**3. A genus-two quotient and its second elliptic quotient.** Each of the three order-two intermediate covers of \(E_\lambda\) has genus \(2\), and permutations of \(X,Y,Z\) identify them over \(k\). Consider the intermediate field defined by \(U=s^2\) in the affine chart \(W=1\), so that
\[
s^6+V^3+1+\lambda s^2V=0.
\]
Put \(w=V+s^2+1\) and \(t=w/s\). In characteristic \(3\), the displayed equation is equivalent in the function field to
\[
s^2-\left(\frac{t^3}{\lambda}+t\right)s+1=0.
\]
With \(r=2s-(t^3/\lambda+t)\), this becomes the smooth genus-two hyperelliptic model
\[
H_\lambda:\quad r^2=\left(\frac{t^3}{\lambda}+t\right)^2-1.
\]
The six zeros of the right-hand polynomial are simple because \((t^3/\lambda+t)'=1\). The involution \((t,r)\mapsto(-t,r)\) has genus-one quotient under \(x=t^2,\ y=\lambda r\), precisely
\[
y^2=x^3+2\lambda x^2+\lambda^2x-\lambda^2=F_\lambda.
\]
The commuting involution \((t,r)\mapsto(-t,-r)\) is the covering involution of \(H_\lambda\to E_\lambda\). The two elliptic quotient maps and the genus-two involution decomposition give \(\operatorname{Jac}(H_\lambda)\sim E_\lambda\times F_\lambda\). Applying the four character idempotents for the tame Klein-four cover \(C_\lambda\to E_\lambda\) and using the symmetry among its three genus-two intermediates gives \(\operatorname{Jac}(C_\lambda)\sim E_\lambda\times F_\lambda^3\). These idempotents are defined over \(k\) and have only powers of \(2\) in their denominators, so the decomposition is defined over \(k\).

**4. Ordinarity.** For the smooth plane cubic \(E_\lambda\) in characteristic \(3\), the Hasse invariant is proportional to the coefficient of \(U^2V^2W^2\) in \((U^3+V^3+W^3+\lambda UVW)^2\), namely \(\lambda^2\ne0\). For the elliptic cubic \(F_\lambda\), the Hasse invariant is the \(x^2\) coefficient \(2\lambda\ne0\); smoothness follows because the derivative of the cubic on its right is \(\lambda(x+\lambda)\), and its value at \(x=-\lambda\) is \(-\lambda^2\). Therefore both factors, and hence the genus-four Jacobian, are ordinary. This establishes the stated \(3\)-rank, \(a\)-number, and Newton polygon.

**5. Arithmetic.** A unibranch cusp of completed type \(u^2+v^3\) has one normalization point with the same residue field, so normalization induces a bijection on points over every finite extension. The isogeny then proves the zeta factorization. Direct counting over \(\mathbb F_3\) gives \(\#E_1=6\), \(\#F_1=2\), \(\#E_2=\#F_2=3\), so the displayed Weil polynomials follow from the traces \((-2,2)\) and \((1,1)\), respectively. In both cases, the total trace is \(4\), hence \(\#D_\lambda(\mathbb F_3)=0\).

## Verification
The standalone standard-library Python script `verify.py` independently enumerates projective points of the singular sextic and the cubic \(E_\lambda\), and affine points plus the point at infinity on \(F_\lambda\), over \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\). It verifies the predicted zeta-factor traces for both nonzero prime-field parameters, together with the rational singular-point distribution. Run `python verify.py` and expect `VERIFY_OK`. The code is a finite corroboration; the proof above supplies the arbitrary-field and arbitrary-extension assertions.

## Relationship to prior work
Badr and Bars, *The stratification by automorphism groups of smooth plane sextic curves* (first public preprint 26 August 2022), consider this Fermat-descendant subfamily within their smooth-sextic automorphism classification; their stated hypotheses are characteristic zero or characteristic greater than \(21\). Their Proposition 10.4 is the motivating equation and automorphism-group result, not a characteristic-three normalization or arithmetic statement. General character decompositions of abelian-cover Jacobians are established tools; the specific cusp geometry, ordinary elliptic factors, and uniform zeta factorization here require the explicit characteristic-three calculation. Related generalized-Fermat isogeny literature concerns a genus-zero quotient and does not immediately subsume this elliptic-base covering.

## Limitations
This is an isogeny decomposition, not a claim that the principally polarized Jacobian is an isomorphic product. It does not determine stable reduction of the characteristic-zero family, automorphism groups of the genus-four normalization, or isomorphism classes of distinct parameters. The finite-field formulas count points on the literal curve and its normalization, not on an arbitrary integral model. Earlier unindexed computations of this symmetric sextic or its elliptic quotients could overlap; an exhaustive novelty guarantee and independent audit are not claimed.

## References
- E. Badr and F. Bars, *The stratification by automorphism groups of smooth plane sextic curves*, arXiv:2208.12749 (first preprint 26 August 2022), specifically the Fermat-descendant family in Proposition 10.4; https://arxiv.org/abs/2208.12749 .
- E. Badr and F. Bars, journal version, *Annali di Matematica Pura ed Applicata* 204 (2025), 2005--2048, https://doi.org/10.1007/s10231-025-01558-z .
- M. Carvacho, R. A. Hidalgo and S. Quispe, *Isogenous decomposition of the Jacobian of generalized Fermat curves*, arXiv:1507.02903 (2015), https://arxiv.org/abs/1507.02903 .
