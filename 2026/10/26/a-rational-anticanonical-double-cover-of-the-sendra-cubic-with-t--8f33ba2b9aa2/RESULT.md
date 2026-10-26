# A rational anticanonical double cover of the Sendra cubic with transverse \(A_5\) and two equianharmonic \(\widetilde E_7\) jumps

## Finding
Let \(X\subset\mathbf P^4_{[w:a:b:c:d]}\) be the smooth complex cubic threefold
\[
F=w^2b+a^2c+b^3+c^3+d^3=0.
\]
The degree-two rational parametrization in Sendra-Arranz--Sendra--Sendra, Example 53, has function-field extension \(\mathbf C(X)(\sqrt{-b/c})\). Its normal projective double cover is the explicit complete intersection
\[
Y=V\bigl(F,z^2+bc\bigr)\subset\mathbf P^5_{[w:a:b:c:d:z]}.
\]
Then:

1. The finite map \(\pi:Y\to X\) has degree two and reduced branch locus \(D_b\cup D_c\), where \(D_b=X\cap\{b=0\}\) and \(D_c=X\cap\{c=0\}\). Each component is an irreducible projective cone over a smooth elliptic plane cubic. Their scheme-theoretic intersection is the curvilinear multiplicity-three thickening of the line \(L=\{b=c=d=0\}\subset X\), defined by \(b=c=d^3=0\) in the ambient projective space (not the full third infinitesimal neighborhood of \(L\)).
2. The threefold \(Y\) is integral, normal, and rational, with \(-K_Y\cong\mathcal O_Y(1)\) ample and \((-K_Y)^3=6\). Its singular locus, set-theoretically, is exactly \(\widetilde L=\{b=c=d=z=0\}\simeq\mathbf P^1\).
3. On every transverse analytic surface section to \(\widetilde L\) at a point with \(wa\ne0\), the singularity is the rational double point of type \(A_5\). At the two points with \(a=0\) or \(w=0\), there are transverse sections analytically equivalent to \(Z^2=u(u^3+v^3)\), of simple elliptic type \(\widetilde E_7\) with elliptic \(j\)-invariant \(0\). Thus the transverse singularity jumps at precisely those two points.

The singularity stratification, branch geometry, and anticanonical model here are the claimed contribution. The existence, degree, and unirationality of the original rational parametrization, and rationality of its tower variety, are **not** claimed as new.

## Assumptions and scope
All varieties are over \(\mathbf C\), and \(Y\) means the scheme-theoretic complete intersection of the displayed homogeneous cubic and quadric. A **transverse surface section** at a point of \(\widetilde L\) is a local analytic hyperplane slice that fixes a local coordinate along the line. A simple elliptic singularity of type \(\widetilde E_7\) is the quasi-homogeneous isolated surface germ \(Z^2=f_4(u,v)\), where \(f_4\) is a binary quartic with four distinct projective roots; its exceptional elliptic curve has self-intersection \(-2\). We make no claim that the threefold itself has isolated or canonical singularities.

## Proof
**Step 1: The source's quadratic function-field extension and its projective model.** In Example 53 of the cited article the coordinates \((a,b,c,d)\) are rational functions of \((s_1,s_2,s_3)\) satisfying \(-b/c=s_1^2\). As the map has degree two, its field extension is exactly \(\mathbf C(X)(s_1)\) with \(s_1^2=-b/c\). On \(c\ne0\), adjoining \(z=cs_1\) yields \(z^2=-bc\). Its homogeneous closure is the displayed \((2,3)\) complete intersection, which will be shown normal and integral below.

**Step 2: Smoothness of the base, branch geometry, and normality.** The five partial derivatives of \(F\), ordered \((w,a,b,c,d)\), are \((2wb,2ac,w^2+3b^2,a^2+3c^2,3d^2)\). They have no common nonzero projective zero: \(ac=0\) together with \(a^2+3c^2=0\) forces \(a=c=0\), while \(wb=0\) and \(w^2+3b^2=0\) force \(w=b=0\), and then \(d=0\). Thus \(X\) is smooth.

The hyperplane sections \(b=0\) and \(c=0\) have respective equations \(a^2c+c^3+d^3=0\) and \(w^2b+b^3+d^3=0\), with the unused coordinate \(w\), respectively \(a\). Both are projective cones over smooth degree-three plane curves: differentiating \(u^2v+v^3+h^3\) proves its projective smoothness. These are elliptic curves. Their vertices are the points \(A=[1:0:0:0:0]\) and \(B=[0:1:0:0:0]\) of \(X\), and both vertices lie on \(L\). Imposing \(b=c=0\) in \(F\) gives \(d^3=0\). Hence the schematic intersection of the two Cartier divisors in \(X\) is a curvilinear triple structure supported on \(L\), cut out by \(b=c=d^3=0\) in the ambient space. Its generic transverse length is three; it is not the thickening defined by the third power of the full ideal of \(L\).

The rational function \(-b/c\) is not a square in \(\mathbf C(X)\): its divisor has multiplicity one along each irreducible branch component. Consequently the double cover is integral. It is étale outside \(D_b\cup D_c\) and smooth at the generic point of either branch divisor. A local equation \(z^2=-bc\) shows possible singularities only at intersections or at singular points of the branch components, all contained in \(L\). Conversely, above any point of \(L\), \(z=0\) and the quadric \(z^2+bc\) has zero differential, so every point of \(\widetilde L\) is singular. The complete intersection \(Y\) is Cohen--Macaulay, hence \(S_2\); since its singular line has codimension two in the threefold, it is regular in codimension one, hence normal by Serre's criterion. The defining equations have degrees \(2\) and \(3\) in \(\mathbf P^5\), so adjunction gives \(K_Y=\mathcal O_Y(2+3-6)=\mathcal O_Y(-1)\), and \((-K_Y)^3=2\cdot3=6\).

**Step 3: Rationality by a birational inverse.** On \(w=1\), work on the dense open subset \(c\ne0\), and set \(t=z/c\), \(v=d/c\), and \(s=c/(a-t)\). The quadric forces \(b=-t^2c\). The cubic becomes \(a^2-t^2+B c^2=0\), where \(B=1-t^6+v^3\). Eliminating \(a\) and \(c\) produces, with \(D=1+Bs^2\),
\[
a=t\frac{Bs^2-1}{D},\qquad c=-\frac{2ts}{D},\qquad b=-t^2c,\qquad d=vc,\qquad z=tc.
\]
Direct substitution gives \(F=z^2+bc=0\), and on the dense open sets on which the rational functions are defined, applying \((t,v,s)=(z/c,d/c,c/(a-z/c))\) returns the original parameters. Thus \(\mathbf C(Y)=\mathbf C(t,v,s)\) and \(Y\) is rational. The origin of this rationality is consistent with, and partially implicit in, the rational tower of Example 53; the displayed rational inverse and the **projective** singular geometry are the useful output here.

**Step 4: Generic transversal type.** Fix a point of \(L\) with \(wa\ne0\). Normalize \(a=1\), and let \(w=\lambda\ne0\) be a fixed transverse analytic hyperplane. On the smooth surface \(X\cap\{w=\lambda\}\), the branch curves \(b=0\) and \(c=0\) are smooth at the chosen point because the derivative in \(c\), respectively \(b\), of \(\lambda^2 b+c+b^3+c^3+d^3\) is nonzero. Their local intersection multiplicity is exactly three: their common equations give \(d^3=0\). Two smooth analytic plane curves meeting with contact order three admit analytic coordinates in which their product is a unit times \(u(u-v^3)\). Taking an analytic square root of the unit and completing the square transforms \(z^2=-bc\) into \(UV=v^6\). This is the \(A_5\) surface rational double point.

**Step 5: Two special transversal types.** At \(A\), set \(w=1\), and take the transverse slice \(a=0\). The cubic equation is \(b+b^3+c^3+d^3=0\). The implicit-function theorem gives \(b=-(c^3+d^3)U(c^3+d^3)\), where \(U(0)=1\) is an analytic unit. In \(z^2=-bc\), absorb the square root of \(U\) into \(z\), yielding the germ \(Z^2=c(c^3+d^3)\). At \(B\), set \(a=1\), take the slice \(w=0\), and solve \(c+c^3+b^3+d^3=0\), obtaining \(Z^2=b(b^3+d^3)\). In each case the binary quartic \(u(u^3+v^3)\) has four distinct roots in \(\mathbf P^1\), so the germ is simple elliptic \(\widetilde E_7\), not a rational double point. Its binary-quartic invariant \(I\) is zero and discriminant is nonzero, giving \(j=0\). As \(L\simeq\mathbf P^1\) has precisely two points at which \(wa=0\), the stratification is complete.

## Verification
The accompanying `verify.py` provides exact symbolic identities for the rational parametrization and its inverse, the cubic equations of the cone bases and their smoothness, the order-three branch contact, and the squarefree binary quartic and vanishing invariant \(I\). Execute `python verify.py` with Python 3 and SymPy installed. A successful run prints `VERIFY_OK rational_inverse double_cover_cubic smooth_branch_elliptic j_zero special_quartic`. This checks key algebraic steps, but the normality, singular-locus and classification assertions follow from the proofs above, not a finite numerical sample.

## Relationship to prior work
Sendra-Arranz, Sendra and Sendra (2026), Example 53, give the smooth cubic, its degree-two rational parametrization, and the rationality of the associated tower variety; they do not specify a normal anticanonical projective closure of the double extension, its two cone branch components, the triple contact along a line, or its \(A_5\)-to-\(\widetilde E_7\) transverse singularity jumps. Ciliberto (2023/2024) treats rationality of certain Fano threefolds, including general genus-four \((2,3)\) intersections containing a plane; that result neither implies nor gives the presently specified rational double-cover model or transverse analytic types. Classical double-cover local analysis, complete-intersection adjunction, and the \(\widetilde E_7\) normal-form classification are used without novelty claims. Equivalent implicit special examples in earlier Fano classifications remain a priority risk.

## Limitations
The claim concerns this explicit complex cubic and its specific quadratic extension, not arbitrary smooth cubic threefolds, arbitrary degree-two parametrizations, or all degree-six Fano threefolds. The singular locus is nonisolated; no terminal, canonical or K-stability property is asserted. The two \(\widetilde E_7\) identifications are for the stated transverse surface slices, **not** a classification of the full threefold germs up to analytic isomorphism. No claim of unconditional historical priority or independent certification is made.

## References
1. J. Sendra-Arranz, J. R. Sendra and J. Sendra, *On the Structure of Radical Towers and their Parametrizations*, arXiv:2610.20404v1 (first public October 14, 2026), Example 53 and Section 6. https://arxiv.org/html/2610.20404v1
2. C. Ciliberto, *On the rationality of certain Fano threefolds*, Manuscripta Mathematica (online 2023), Section 4. https://doi.org/10.1007/s00229-023-01514-2
3. *Quartic surfaces up to volume preserving equivalence*, Selecta Mathematica (2024), Section 3.1, weighted normal forms for simple elliptic surface singularities. https://doi.org/10.1007/s00029-023-00890-7
4. Standard results used: Serre's normality criterion, the adjunction formula for complete intersections, and the classification of Du Val and simple elliptic surface hypersurface germs.
