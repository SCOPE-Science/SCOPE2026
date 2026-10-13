# Eight fixed points in the canonical biquadratic double-sextic model
## Finding
Let \(X\) be a general \(L\)-polarized K3 surface in the canonical biquadratic double-sextic family of Clingher--Malmendier--Roulleau, with \(\rho_L>10\) and \(L\neq H\oplus D_8\oplus D_4\). Put \(n=\rho_L-10\). Their canonical equation is
\[
y^2=c_2(u,v)w^4+c_4(u,v)w^2+c_6(u,v),
\]
and its branch sextic has one \(A_{2n+1}\) singularity at \([u:v:w]=[0:0:1]\). The symplectic involution is induced by
\[
\iota:(u,v,w,y)\longmapsto(u,v,-w,-y).
\]
On the minimal resolution, the eight fixed points of \(\iota\) are exactly six Weierstrass points of the smooth genus-two curve \(y^2=c_6(u,v)\), together with two points on the central exceptional component above the \(A_{2n+1}\) singularity.

More precisely, the six smooth fixed points are
\[
w=y=0,\qquad c_6(u,v)=0.
\]
If \(E_1,\ldots,E_{2n+1}\) is the exceptional chain over the singular point, then
\[
\iota(E_j)=E_{2n+2-j}.
\]
Thus only \(E_{n+1}\) is preserved setwise. The induced involution on \(E_{n+1}\cong\mathbb P^1\) has exactly two fixed points.

## Assumptions and scope
The ground field is \(\mathbb C\). The surface is a general member of one of the lattices in Equation (1.1) of the source with \(\rho_L>10\), except \(H\oplus D_8\oplus D_4\), whose canonical branch sextic is reducible and is deliberately excluded from this statement. Proposition 2.3 of the source gives \(c_0=0\) in the canonical model, while Theorem 2.1 gives the unique branch singularity of type \(A_{2n+1}\). Equation (2.2) and the discussion following it identify the two antisymplectic involutions and their symplectic composition. The genus-two curve \(y^2=c_6(u,v)\) is smooth, so the binary sextic \(c_6\) has six distinct roots.

The claim localizes the fixed points of the symplectic involution in this canonical projective model. It does not classify fixed points for the separate \(H\oplus N\) model or for the excluded reducible-sextic case.

## Proof
First work on the singular double-sextic model away from the unique singular point. A point \([u:v:w:y]\) is fixed by \(\iota\) in the weighted projective space only if it is projectively equal to \([u:v:-w:-y]\). If \((u,v)\neq(0,0)\), the projective scaling factor is forced to be \(1\), hence \(w=y=0\). The surface equation then becomes \(c_6(u,v)=0\). Because the fixed genus-two curve \(y^2=c_6(u,v)\) is smooth, there are exactly six such points. They are its Weierstrass points. The branch sextic has no singularity at them, so all six are smooth points of the K3 model.

It remains to resolve the point \(p=[0:0:1:0]\). In the affine chart \(w=1\), weighted projective rescaling by \(-1\) shows that the local action is
\[
(u,v,y)\longmapsto(-u,-v,y).
\]
Let \(f(u,v)\) be the local branch equation. It is invariant under \((u,v)\mapsto(-u,-v)\) and has plane-curve type \(A_{2n+1}\). Since its Hessian has rank one, choose odd linear coordinates \((x,z)\) with \(x\) in the nondegenerate direction. Completing the square uses an odd correction to \(x\), because \(f\) is even. The remaining one-variable term is even and has order \(2n+2\). An odd analytic reparametrization of \(z\) therefore gives the equivariant normal form
\[
f=x^2+z^{2n+2},\qquad (x,z)\longmapsto(-x,-z).
\]
The double cover is consequently
\[
y^2=x^2+z^{2n+2}.
\]
Set \(U=y+x\) and \(V=y-x\). Then
\[
UV=z^N,\qquad N=2n+2,
\]
and the involution becomes
\[
(U,V,z)\longmapsto(V,U,-z).
\]
This is the \(A_{N-1}\) surface singularity. Its minimal resolution has exceptional chain \(E_1,\ldots,E_{N-1}\). The involution exchanges the two ends, hence sends \(E_j\) to \(E_{N-j}\). Since \(N\) is even, the unique setwise-fixed component is \(E_{N/2}=E_{n+1}\).

For an explicit local quotient description, write
\[
U=s^N,\qquad V=t^N,\qquad z=st
\]
modulo the \(\mu_N\)-action \((s,t)\mapsto(\zeta s,\zeta^{-1}t)\). The map
\[
T(s,t)=(t,-s)
\]
descends to the involution above; indeed \(T^2=(-s,-t)\) is the element \(\zeta=-1\) of \(\mu_N\). On the central exceptional curve the invariant ratio
\[
q=\frac{s^{N/2}}{t^{N/2}}
\]
is a rational coordinate, and
\[
q\longmapsto\frac{(-1)^{N/2}}{q}=\frac{(-1)^{n+1}}{q}.
\]
Its fixed equation is \(q^2=(-1)^{n+1}\), which has exactly two distinct solutions over \(\mathbb C\). The adjacent intersection points \(q=0\) and \(q=\infty\) are exchanged, so no additional fixed point occurs on the exceptional chain.

Thus the six smooth Weierstrass fixed points and the two central-resolution fixed points exhaust the fixed locus. Their total is eight, agreeing with the general Nikulin theorem for a symplectic involution on a K3 surface.

## Verification
The accompanying exact checker verifies for every \(n\in\{1,\ldots,8\}\) that \(N=2n+2\) is even, that \((U,V,z)\mapsto(V,U,-z)\) preserves \(UV-z^N\) and squares to the identity, that the induced permutation \(j\mapsto N-j\) of the \(A_{N-1}\) exceptional chain has the unique fixed index \(N/2=n+1\), and that the central-coordinate fixed polynomial \(q^2-(-1)^{n+1}\) has two simple roots. It also checks the resulting count \(6+2=8\). Running `python3 artifacts/verify.py` prints `VERIFY_OK`.

The checker is supplementary: the global identification of the canonical model, the smooth genus-two curve, and the branch singularity type comes from the cited source; the proof above supplies the local resolution argument.

## Relationship to prior work
Clingher--Malmendier--Roulleau give the canonical double-sextic equation, identify \(\iota\) as the symplectic composition of the two displayed antisymplectic involutions, identify the smooth genus-two fixed curve of one factor, and determine the branch singularity type. They do not state where the eight fixed points of \(\iota\) lie in the canonical double-sextic model.

Van Geemen--Sarti and the classical Nikulin theory imply that a symplectic involution on a K3 surface has eight fixed points. That general theorem supplies the expected total, but it does not imply the model-specific decomposition into six Weierstrass points and two points on the central exceptional curve. Searches using the exact source identifier, the biquadratic equation, Weierstrass-point language, \(A_{2n+1}\)-resolution language, and van Geemen--Sarti fixed-point terminology located no statement of this localization.

## Limitations
The argument assumes the general canonical irreducible-sextic case with \(\rho_L>10\) and excludes \(H\oplus D_8\oplus D_4\). It is characteristic-zero and analytic in the local normal-form step. The result localizes fixed points but does not compute the complete quotient surface \(X/\langle\iota\rangle\) in projective coordinates. Older literature on special Nikulin models may contain an equivalent localization in different coordinates; no such statement was found in the inspected sources.

## References
A. Clingher, A. Malmendier, X. Roulleau, *On projective K3 surfaces \(X\) with \(\operatorname{Aut}(X)=(\mathbb Z/2\mathbb Z)^2\)*, arXiv:2305.08959, especially Equation (2.2), Theorem 2.1, Remark 2.2, and Proposition 2.3.

B. van Geemen, A. Sarti, *Nikulin involutions on K3 surfaces*, Math. Z. 255 (2007), 731--753, arXiv:math/0602015, DOI 10.1007/s00209-006-0047-6.
