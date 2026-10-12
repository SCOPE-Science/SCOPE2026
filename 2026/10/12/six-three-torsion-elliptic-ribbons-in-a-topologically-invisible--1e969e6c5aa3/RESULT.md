# Six three-torsion elliptic ribbons in a topologically invisible critical scheme

## Finding
Consider the specific morphism \(g:Y\to\mathbb P^1\) from a smooth projective fivefold of Corrêa--Kollár--Schreieder--Wang, Theorem 1 and Example 23 of [1], formed by blowing up their embedded quotient threefold. Its scheme-theoretic critical locus (the zero scheme of \(dg\)) consists of exactly six disjoint, *split square-zero elliptic ribbons*. More precisely, with \(A\) the elliptic curve in the degree-six del Pezzo surface of [1], \(\tau\) its translation of exact order six, and \(B=A/\langle\tau\rangle\), there is a nontrivial line bundle \(\mathcal M\in\operatorname{Pic}^0(B)\) of **exact order three** such that
\[
 \operatorname{Crit}(g)\simeq\coprod_{i=1}^{6}\operatorname{Spec}_B(\mathcal O_B\oplus\mathcal M),\qquad \mathcal M^{\otimes3}\simeq\mathcal O_B\ne\mathcal M.
\]
In each summand, \(\mathcal M\) is a square-zero ideal: \((a,m)(a',m')=(aa',am'+a'm)\). Thus every reduced component is a smooth elliptic curve, the critical scheme has generic length two along it, and the ideal of its reduction has nontrivial three-torsion conormal. Nevertheless reduction induces isomorphisms
\[
 H^i(\operatorname{Crit}(g),\mathcal O_{\operatorname{Crit}(g)})\xrightarrow{\sim}
 H^i(\operatorname{Crit}(g)_{\mathrm{red}},\mathcal O_{\operatorname{Crit}(g)_{\mathrm{red}}})
\]
for every \(i\): both sides are \(\mathbb C^6\) for \(i=0,1\) and zero for \(i\ge2\).

## Assumptions and scope
Work over \(\mathbb C\). Use a section \(s\in H^0(\mathbb P^1,\mathcal O(6))\) with six distinct zeros, as in [1, Section 5.2]. The rational elliptic surface is the smooth Weierstrass surface
\[
 S:\quad z y^2+x^3+s z^3=0
 \quad\text{in}\quad
 \mathbb P_{\mathbb P^1}(\mathcal O\oplus\mathcal O(2)\oplus\mathcal O(3)).
\]
The cyclic group of order six acts on its plane coordinates by \([x:y:z]\mapsto[\xi^2x:\xi^3y:z]\), where \(\xi\) is primitive of order six. It acts freely by translation \(\tau\) of order six on the smooth invariant elliptic curve \(A\) inside the degree-six del Pezzo surface \(T\) from [1, Example 23]. Put \(V=(S\times A)/\mu_6\). Let \(P\to\mathbb P^1\) be the smooth ambient fivefold from that example, whose resolution is an isomorphism near \(V\), and put \(Y=\operatorname{Bl}_V(P)\). The morphism \(g\) is the induced projection. This is a theorem about this specified model, not about all morphisms with homotopy-invisible critical points. The critical *scheme* is defined by the ideal generated locally by the coefficients of \(dg\), not merely by the set of singular fibers.

## Proof
**1. The complete local critical ideal.** Choose a simple zero of \(s\), an affine coordinate near it, and a trivialization of the line bundles. On the cyclic étale cover before quotienting, the ambient fibration is smooth and the center has local equations \(F=x^3+y^2-t=0\) and \(w=0\), where \(w\) is a local normal parameter for \(A\subset T\) and the omitted parameter is a coordinate along \(A\). The resolution used in [1, Example 23] is an isomorphism here because the cyclic action on \(A\) is free.

On the blow-up chart \(F=uw\), the total space has independent coordinates \((x,y,u,w,a)\), with base map
\[
 t=x^3+y^2-uw.
\]
The critical ideal is exactly
\[
 \left(\frac{\partial t}{\partial x},\frac{\partial t}{\partial y},
 \frac{\partial t}{\partial u},\frac{\partial t}{\partial w},
 \frac{\partial t}{\partial a}\right)
 =(3x^2,2y,-w,-u,0)=(x^2,y,u,w).
\]
Hence the critical scheme on the cover is \(A\times\operatorname{Spec}\mathbb C[x]/(x^2)\), with no embedded components. It lies scheme-theoretically in \(t=0\). On the opposite chart \(w=vF\), the base map is \(t=x^3+y^2-F\), whose derivative in \(F\) is \(-1\), so no further critical points arise. Away from the cusp points, the center is smooth over the base; blowing up a relative smooth center in a smooth family remains smooth over that base. Because \(s\) has exactly six simple zeros, these charts exhaust the critical scheme and yield six disjoint components.

**2. Equivariant descent and the order-three conormal.** The weight-two coordinate \(x\) is the *global* plane coordinate from the \(\mathcal O(2)\)-summand, not an arbitrarily chosen analytic normal-form coordinate. Along each zero of \(s\), the cyclic generator acts on the above double structure by
\[
 (a,x)\longmapsto(\tau(a),\xi^2x).
\]
Let \(\pi:A\to B=A/\langle\tau\rangle\) be the connected cyclic étale isogeny of degree six. Descend \(\mathcal O_A\cdot x\) with precisely this linearization, and call the resulting invertible sheaf \(\mathcal M\) on \(B\). Equivariant descent of the square-zero algebra gives \(\mathcal O_B\oplus\mathcal M\), proving the displayed scheme isomorphism, including its splitting as an algebra. The character \(\xi^2\) has order three, so \(\mathcal M^{\otimes3}\simeq\mathcal O_B\), and consequently \(\deg\mathcal M=0\). If \(\mathcal M\) were trivial, it would have a nonzero global section. Pulling such a section back to \(A\) would produce a nonzero regular function transforming by a nontrivial character of the translation action, which is impossible since \(H^0(A,\mathcal O_A)=\mathbb C\). Thus \(\mathcal M\) has exact order three and is not trivial. Since the nilradical squares to zero, \(\mathcal M\) is also its conormal \(\mathcal I/\mathcal I^2\) relative to the ribbon.

**3. Invisible coherent cohomology.** The connected quotient \(B\) is elliptic. For a nontrivial degree-zero line bundle on an elliptic curve, \(H^0(B,\mathcal M)=H^1(B,\mathcal M)=0\): the first vanishing is the degree-zero section criterion, and the second follows by Serre duality and \(\omega_B\simeq\mathcal O_B\). Thus the split algebra \(\mathcal O_B\oplus\mathcal M\) has precisely the same structure-sheaf cohomology as \(\mathcal O_B\), on each of the six disconnected ribbons, proving the claim.

## Verification
The included \(\texttt{verify.py}\) evaluates the Jacobian ideal in the blow-up chart by exact Gröbner-basis arithmetic over \(\mathbb Q\), checks that the other chart has a nonzero base derivative, and confirms that the cubic and quadratic monomials are invariant under the cyclic weights while the nilpotent coordinate has character of order three. Run \(\texttt{python3 verify.py}\) with SymPy 1.14 or later; success prints \(\texttt{ELLIPTIC_CRITICAL_RIBBON_LOCAL_OK}\). The global étale descent, exact torsion order, absence of other critical points and cohomology are justified by the mathematical arguments above, not inferred from the checker.

## Relationship to prior work
Corrêa--Kollár--Schreieder--Wang [1, Theorem 1, Example 23, Remark 24] prove that the morphism is a homotopy fiber bundle despite six singular fibers, exhibit the local analytic transverse type, and report that its critical locus is one-dimensional. They do not calculate the scheme-theoretic critical locus, its globally twisted nilpotent line bundle, or its coherent-cohomology comparison with the reduction. The key additional step is keeping the weight-two cyclic linearization through the blow-up and descending it via a connected degree-six elliptic isogeny; a pointwise analytic singularity type alone does not determine this line bundle. Ciliberto--Grassi--Miranda--Verra--Zanardini [2] classify the supporting six-cusp rational elliptic surface, not the critical scheme of the fivefold quotient blow-up. Standard ribbon theory [3] addresses general double structures rather than this specific fibration.

## Limitations
The description assumes the particular global quotient embedding and six simple zeros specified above and characteristic zero. It does not describe all smooth projective homotopy fiber bundles or other degenerations of the elliptic surface; it does not compute the entire derived critical locus, vanishing-cycle sheaves, or analogous ribbons for different cyclic weights. The cohomological invisibility is only for structure-sheaf cohomology of this critical scheme, not a claim that all coherent sheaf functors or derived invariants are unchanged by reduction. The closest primary papers give the construction and local type; independent exhaustive historical novelty verification has not been performed.

## References
[1] M. Corrêa, J. Kollár, S. Schreieder and B. Wang, *Invisible singularities in complex algebraic geometry*, arXiv:2608.10973v1, posted 2026-08-11, especially Theorem 1, Example 23, Eq. (13), and Remark 24. Full text: https://www.researchgate.net/publication/412164280_Invisible_singularities_in_complex_algebraic_geometry .

[2] C. Ciliberto, A. Grassi, R. Miranda, A. Verra and A. Zanardini, *Rational elliptic surfaces with six singular double fibres*, arXiv:2602.11725v1, 2026, Section 3. Author-hosted full text: https://www.math.colostate.edu/~miranda/preprints/2602.11725v1.pdf .

[3] D. Bayer and D. Eisenbud, *Ribbons and their canonical embeddings*, Trans. Amer. Math. Soc. 347 (1995), 719--756; background on ribbons, not on the present fibration.
