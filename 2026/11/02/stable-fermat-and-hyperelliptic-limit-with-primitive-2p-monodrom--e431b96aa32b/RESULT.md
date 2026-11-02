# Stable Fermat-and-hyperelliptic limit with primitive \(2p\)-monodromy at \(t=-2\)

## Finding
For every prime \(p\ge5\), consider the plane pencil over \(\mathbb C\)
\[
C_{p,t}:\quad X^{2p}+Y^{2p}+Z^{2p}
+t(X^pY^p+X^pZ^p+Y^pZ^p)=0.
\]
For \(t\notin\{\infty,-1,-2,2\}\), these are smooth curves of genus \(g=(p-1)(2p-1)\). Make the local base change \(t=-2+s^{2p}\). The stable special fiber at \(s=0\) is a tree of smooth curves: a central Fermat curve
\[
F_p:\ A^p+B^p=C^p,\qquad g(F_p)=\frac{(p-1)(p-2)}2,
\]
and exactly \(3p\) leaves, each isomorphic to
\[
T_p:\ a^2=4b^p-1,\qquad g(T_p)=\frac{p-1}{2}.
\]
Each leaf meets the central curve once in a node, at a distinct preimage of a cusp, and no two leaves meet. Thus the stable special fiber is of compact type and its Jacobian is
\[
J(F_p)\times J(T_p)^{3p}.
\]
The degeneration consequently has potentially good Jacobian reduction. Its local geometric monodromy \(M\) on rational first cohomology has **exact order** \(2p\) and
\[
\det(\lambda I-M)=
(\lambda-1)^{(p-1)(p-2)}
\left(\frac{\lambda^p+1}{\lambda+1}\right)^{3p}
=(\lambda-1)^{(p-1)(p-2)}\Phi_{2p}(\lambda)^{3p}.
\]
The statement concerns the one-parameter smoothing at the specified boundary, not every deformation of the singular curve.

## Assumptions and scope
All curves and degenerations are over characteristic-zero complex fields; \(p\) is any odd prime at least five. The base change is taken over the formal disc \(\operatorname{Spec}\mathbb C[[s]]\), with generic fiber after the substitution \(t=-2+s^{2p}\). The stable curve means the uniquely determined Deligne--Mumford stable model after resolving the total-space surface and contracting unstable rational chains. The Jacobian product is the connected degree-zero Picard variety of the stable special fiber (an abelian variety, not an isomorphism of the generic Jacobian with this product). Monodromy is the geometric loop operator of the original punctured \(t\)-disc, acting on \(H^1\) of any nearby smooth fiber.

## Proof
**1. Central normalization and all singularities.** Set \(U=X^p,V=Y^p,W=Z^p\). The special equation is the pullback of the nonsingular conic
\[
Q_{-2}(U,V,W)=(U-V-W)^2-4VW=0.
\]
Its inverse image under the coordinatewise \(p\)-power map is smooth where all coordinates are nonzero, since that map is étale there. On each coordinate line, for example \(Z=0\), the equation is \((X^p-Y^p)^2=0\), so there are exactly \(p\) points \([\zeta_p^i:1:0]\); the other two coordinate lines give two additional disjoint sets. None of the coordinate vertices lies on the special curve. Therefore all singular points lie among these \(3p\) points.

The map
\[
\nu:F_p\longrightarrow C_{p,-2},\qquad
[A:B:C]\longmapsto[A^2:B^2:C^2]
\]
is well defined because \(A^p+B^p=C^p\) makes \(Q_{-2}(A^{2p},B^{2p},C^{2p})=0\). At a generic point no alternative choice of coordinate square-root signs satisfies the Fermat equation, modulo a common sign. Thus \(\nu\) is generically one-to-one. Since it is finite from a smooth projective irreducible curve, it is the normalization. Its genus is \((p-1)(p-2)/2\).

**2. Exact local smoothing equation.** Near any point \([\zeta_p^i:1:0]\), work in the \(Y=1\) chart and set
\[
A=X^p-1-Z^p,\qquad B=Z,\qquad \varepsilon=t+2.
\]
Because \(pX^{p-1}\ne0\) at the selected point, \((A,B)\) are regular analytic local coordinates. Direct substitution gives the **exact** equation
\[
A^2-4B^p+\varepsilon(1+A+3B^p+AB^p+B^{2p})=0.
\]
Hence each singularity is a single unibranch \(A_{p-1}\) cusp (\(A^2=4B^p\)) with \(\delta=(p-1)/2\), and the pencil supplies a transverse smoothing because the coefficient of \(\varepsilon\) is a unit. Permuting the projective coordinates establishes the identical local model at every one of the \(3p\) points. The genus identity
\[
(p-1)(2p-1)-3p\frac{p-1}{2}=\frac{(p-1)(p-2)}2
\]
checks that there are no unaccounted singularities or branches.

**3. Stable replacement of a cusp.** The standard stable-reduction calculation for a transverse \(A_{p-1}\) smoothing is visible directly in the local equation. Write \(\varepsilon=s^{2p}\), and in the weighted chart substitute \(A=s^p a\), \(B=s^2 b\). Divide by \(s^{2p}\). The special equation in the chart is
\[
a^2-4b^p+1=0.
\]
This affine curve is smooth and compactifies to a smooth double cover of \(\mathbb P^1_b\), branched at the \(p\) simple roots of \(4b^p-1\) and at infinity. Riemann--Hurwitz yields genus \((p-1)/2\). Because \(p\) is odd, it has **one** point above infinity. That point is the unique attachment point to the normalization branch of \(A^2=4B^p\). Resolving the toric quotient charts of the weighted modification introduces only genus-zero chains between the normalization and this smooth component; those chains are unstable and contract in the stable model. This local construction gives precisely one smooth hyperelliptic tail, attached at one node. Applying it at all \(3p\) disjoint cusps gives the stated star. The normalized central component has genus at least six and each tail has genus at least two, so the result is stable. The total genus check
\[
\frac{(p-1)(p-2)}2+3p\frac{p-1}2=(p-1)(2p-1)
\]
shows the model accounts for all vanishing cycles. The graph has no cycles, hence compact type; the product formula for the special Jacobian follows from the Picard functor of a compact-type nodal curve.

**4. Monodromy.** Let \(\xi\) be a primitive \(2p\)-th root of unity. Under one turn around \(\varepsilon=0\), the lifted base coordinate changes by \(s\mapsto\xi s\). Keeping the original local coordinates \(A,B\) fixed induces on each tail
\[
(a,b)\longmapsto(-a,\xi^{-2}b).
\]
The smooth central normalization is fixed because its original projective coordinates are fixed. A basis of holomorphic tail differentials is
\[
\left\{\frac{b^j\,db}{a}:0\le j\le\frac{p-3}{2}\right\}.
\]
The displayed automorphism has eigenvalues \(-\xi^{-2(j+1)}\) on this basis and their complex conjugates on antiholomorphic cohomology. They are precisely the primitive \(2p\)-th roots \(-\zeta_p^k\), for \(1\le k\le p-1\), each once on \(H^1(T_p)\). Separating nodes contribute no graph cohomology; the central component contributes \((p-1)(p-2)\) copies of eigenvalue one. Consequently the characteristic polynomial is the one stated in the finding, and the presence of primitive \(2p\)-th roots proves exact monodromy order \(2p\).

## Verification
Run `python3 verify.py` with Python 3 and SymPy. It performs exact symbolic substitutions for the conic factorization, normalization identity, local pencil deformation, and weighted scaling in prime characteristics used only as formal integer exponents, as well as genus and cyclotomic identities for \(p=5,7,11,13,17,19\). Its success marker is `VERIFY_OK`. These finite computations independently check the algebra but do not constitute a proof of the entire infinite-prime stable-reduction theorem; the geometric arguments above supply that proof. For example, \(p=5\) gives a genus-six central Fermat component, fifteen genus-two tails, total genus thirty-six, and monodromy order ten.

## Relationship to prior work
Moreno Vega and Reyes-Carocca introduced and classified the automorphism structure of this generalized pencil. Their §5.2 states that the \(t=-2\) member is not stable, but does not identify its stable replacement or give this monodromy spectrum. Díaz and González-Aguilera study topological boundary strata for equisymmetric loci with abelian group actions in general; their theorems do not state this pencil's explicit central Fermat component, hyperelliptic tail equations, Jacobian product, or monodromy polynomial. Costa and González-Aguilera study general limits of equisymmetric one-dimensional families; the complete text of that potentially relevant work was not accessible during the comparison, so an overlap risk remains. General local cusp stable-reduction theory provides a method, but not the global \(3p\)-tail identification or this precise monodromy decomposition without the calculations above.

## Limitations
The result fixes the boundary \(t=-2\) and the specified one-parameter transverse smoothing. It does not classify limits at \(t=2,-1,\infty\), all other deformations, the isogeny type of a generic Jacobian, or the polarization of the limiting product in explicit coordinates. The source-comparison search was not exhaustive and does not establish historical priority.

## References
1. V. Moreno Vega and S. Reyes-Carocca, *A generalisation of the pencil of Kuribayashi-Komiya quartics* (2025), arXiv:2507.03128v1, especially §3 and §5.2; https://arxiv.org/abs/2507.03128.
2. R. Díaz and V. González-Aguilera, *Boundary of equisymmetric loci of Riemann surfaces with abelian symmetry* (2024 preprint; 2026 journal), arXiv:2411.09836v1; https://arxiv.org/abs/2411.09836.
3. A. F. Costa and V. González-Aguilera, *Limits of equisymmetric 1-complex dimensional families of Riemann surfaces*, Math. Scand. 121 (2017), 26–48, DOI:10.7146/math.scand.a-26306. Full text not inspected; abstract and indexed excerpts only.
