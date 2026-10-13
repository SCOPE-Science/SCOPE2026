# Signed Lagrangian surface representation in level-\(p\) Siegel cohomology

## Finding
Let \(p\ge 3\) be an odd prime, \(V=\mathbb F_p^4\) with its standard nondegenerate alternating form, and \(G=\operatorname{Sp}_4(\mathbb F_p)\). Write \(L_p\) for the genus-two tropical level-\(p\) link \(LA_2[p]^{\mathrm{trop}}\), equivalently the simplicial complex \(\Delta_2[p]\) described by Assaf--Brandt--Bruce--Chan--Vlad. Let \(P_0\subset V\) be a fixed Lagrangian plane. Set
\[
 H=\{g\in G:gP_0=P_0,\ \det(g|_{P_0})\in\{1,-1\}\},
 \qquad \varepsilon(g)=\det(g|_{P_0})\in\{1,-1\}.
\]
Then, as rational \(G\)-representations,
\[
 H^2(L_p;\mathbb Q)\cong
 \operatorname{Ind}_{H}^{G}\varepsilon,
 \qquad \dim_{\mathbb Q}H^2(L_p;\mathbb Q)=\frac{p^4-1}{2}.
\]
The same representation describes \(W_0H_c^3(\mathcal A_2[p];\mathbb Q)\), using the canonical tropical comparison. For any \(g\in G\), let \(N_{\pm}(g)\) denote the number of \(g\)-stable Lagrangian planes \(P\subset V\) for which \(\det(g|_P)=\pm1\). The complete character is
\[
 \chi_p(g)=\frac{p-1}{2}\bigl(N_+(g)-N_-(g)\bigr).
\]
In particular, for any nonidentity symplectic transvection \(T\), and any involution \(s\in G\) with two-dimensional symplectic eigenspaces of eigenvalues \(+1\) and \(-1\), respectively,
\[
 \chi_p(T)=\frac{p^2-1}{2},\qquad
 \chi_p(s)=-\frac{(p-1)(p+1)^2}{2}.
\]
The restriction to the cyclic transvection subgroup has exact rational isotypic decomposition
\[
 H^2(L_p;\mathbb Q)|_{\langle T\rangle}
 \cong\mathbb Q^{\,(p-1)(p+1)^2/2}\oplus
 \mathbb Q(\zeta_p)^{\,p(p^2-1)/2},
\]
where \(\langle T\rangle\) acts trivially on each \(\mathbb Q\)-summand and through multiplication by \(\zeta_p\) on each cyclotomic summand. In contrast, the full \(G\)-fixed part vanishes:
\[
 H^2(L_p;\mathbb Q)^G=0.
\]

## Assumptions and scope
All cohomology and representations are rational; the prime \(p\) is odd, including \(p=3\). The symplectic group action is induced by its action on level structures; a cohomological left action is understood using inverse pullback. A Lagrangian plane means a two-dimensional totally isotropic subspace of \(V\). A symplectic transvection has the form \(T_v(w)=w+\langle w,v\rangle v\), with \(v\ne0\). The involution \(s\) has distinct eigenvalues \(\pm1\) and two nondegenerate alternating eigenspaces, each of dimension two. The cyclotomic representation \(\mathbb Q(\zeta_p)\) has rational dimension \(p-1\). No assertion is made about level two, nonprime levels, other cohomological degrees, or irreducible decomposition under all of \(G\).

## Proof
**1. Oriented top-dimensional cycles.** Corollary 5.8 of Assaf et al. identifies subcomplexes \(S(P,[\omega])\subset L_p\), where \(P\) is Lagrangian and \([\omega]\) is a nonzero element of \(\bigwedge^2P\) modulo the sign relation. Each \(S(P,[\omega])\) is a triangulation of a connected closed oriented surface, and distinct such surfaces have no common edges or two-simplices. Hence the simplicial chain groups \(C_2(L_p;\mathbb Q)\) and \(C_1(L_p;\mathbb Q)\) split into surface terms (and an additional vertex-only gluing has no effect on the boundary \(\partial_2\)). There are no three-simplices. Consequently
\[
 H_2(L_p;\mathbb Q)=\ker\partial_2
 \cong\bigoplus_{(P,[\omega])}\mathbb Q[S(P,[\omega])],
\]
where the generator is an oriented surface fundamental cycle. The standard diagonal pairing on the oriented surface generators is \(G\)-invariant, so this signed permutation representation is self-dual and is also the representation on \(H^2(L_p;\mathbb Q)\).

**2. Number and transitivity.** Every one-dimensional subspace of \(V\) is isotropic. There are \((p+1)(p^2+1)\) such lines. Each lies in exactly \(p+1\) Lagrangian planes, and each Lagrangian plane contains exactly \(p+1\) lines. Double counting gives \((p+1)(p^2+1)\) Lagrangian planes. The nonzero \(\omega\in\bigwedge^2P\) have \((p-1)/2\) classes modulo \(\pm1\), giving \((p^4-1)/2\) surfaces. Symplectic basis extension makes \(G\) transitive on planes, and the Levi \(\operatorname{GL}_2(\mathbb F_p)\) in a Lagrangian stabilizer has surjective determinant, so \(G\) is transitive on pairs \((P,[\omega])\). The stabilizer of a fixed pair is exactly \(H\).

**3. The nontrivial orientation sign.** An element fixing \((P,[\omega])\) restricts to \(A\in\operatorname{GL}_2(\mathbb F_p)\) with determinant \(\pm1\). Since reduction \(\operatorname{SL}_2(\mathbb Z)\to\operatorname{SL}_2(\mathbb F_p)\) is onto, \(A\) lifts to an integral invertible matrix \(\widetilde A\in\operatorname{GL}_2(\mathbb Z)\) with determinant the corresponding integer \(\pm1\). Under the modular surface identification of Assaf et al., this lift induces exactly the prescribed permutation of the simplicial vertex classes. Its action on the three-dimensional real vector space \(\operatorname{Sym}^2\mathbb R^2\) has determinant \((\det\widetilde A)^3=\det\widetilde A\). Thus it acts on the oriented link surface with degree \(+1\) or \(-1\) according as \(\det(A)=+1\) or \(-1\). This establishes the character \(\varepsilon\) of \(H\). The signed-permutation action therefore equals \(\operatorname{Ind}_H^G\varepsilon\), over \(\mathbb Q\) as well as over \(\mathbb C\).

**4. The complete character.** A given Lagrangian \(P\) is fixed by \(g\) only if \(gP=P\). On its \((p-1)/2\) surface labels, \(g\) acts through multiplication by \(d=\det(g|_P)\). A label is fixed precisely when \(d=\pm1\); in that event every label is fixed with sign \(d\). Summing diagonal entries gives the stated universal character formula. This also shows that \(-I\) acts trivially, since its determinant on every plane is one.

**5. Transvections and their complete cyclic spectrum.** Let \(T=T_v\). If a Lagrangian \(P\) is fixed by \(T\) and some \(w\in P\) has \(\langle w,v\rangle\ne0\), then \(T(w)-w\in P\) forces \(v\in P\). If instead \(\langle P,v\rangle=0\), then \(v\in P^\perp=P\). Conversely, every Lagrangian containing \(v\) is fixed pointwise by \(T\). There are exactly \(p+1\) such planes, so \(\chi_p(T)=(p+1)(p-1)/2\). Every nonidentity power of \(T\) has the same fixed planes and trace. Put \(a=\dim H^2(L_p;\mathbb Q)^{\langle T\rangle}\) and let \(b\) be the multiplicity of the unique nontrivial rational irreducible representation \(\mathbb Q(\zeta_p)\) of \(C_p\). Averaging traces and comparing dimensions gives
\[
 a=\frac{1}{p}\left(\frac{p^4-1}{2}+(p-1)\frac{p^2-1}{2}\right)
 =\frac{(p-1)(p+1)^2}{2},
 \qquad b=\frac{1}{p}\left(\frac{p^4-1}{2}-\frac{p^2-1}{2}\right)
 =\frac{p(p^2-1)}{2}.
\]
This proves the rational cyclic-module statement.

**6. Symplectic involutions.** Suppose \(s\) has nondegenerate \(\pm1\)-eigenspaces \(U_\pm\), each of symplectic dimension two. Since \(p\ne2\), any \(s\)-invariant Lagrangian decomposes as \((P\cap U_+)\oplus(P\cap U_-)\). Isotropy forces each intersection to be a line. There are \((p+1)^2\) choices, and \(\det(s|_P)=-1\) for every one. The character formula yields \(\chi_p(s)=-(p+1)^2(p-1)/2\).

**7. No full invariants and modular cohomology.** The stabilizer \(H\) has elements with determinant \(-1\) on \(P_0\), so \(\varepsilon\) is nontrivial. Frobenius reciprocity gives \(\operatorname{Hom}_G(\mathbb Q,\operatorname{Ind}_H^G\varepsilon)=\operatorname{Hom}_H(\mathbb Q,\varepsilon)=0\). By the natural comparison between the tropical link and weight-zero compactly supported cohomology for \(\mathcal A_2[p]\), the same representation and trace formulas apply to \(W_0H_c^3\). No claim about the full mixed Hodge structure is required.

## Verification
The standalone Python 3 checker `artifacts/verify.py` enumerates all Lagrangian planes in \(\mathbb F_p^4\) for \(p=3,5,7\), checks their counts, verifies all fixed-plane determinant signs for an explicit transvection and a symplectic involution, and checks the resulting rational cyclic-invariant dimensions. It also verifies a sign-reversing action on the four vertices of the \(p=3\) tetrahedral surface. Its actual output ends with `VERIFY_OK`. The finite checks corroborate the independent proof for every odd prime; they are not an exhaustive check over all primes.

## Relationship to prior work
Assaf, Brandt, Bruce, Chan and Vlad construct the entire simplicial link and prove the decomposition into surfaces glued at vertices (Theorem 4.5, Corollary 5.8, Theorem 5.10, arXiv:2609.14895v1). Their Theorem 5.12 determines only dimensions of weight-zero compactly supported cohomology. The present result builds on that geometric description and refines the top-dimensional summand to the full finite symplectic-group character, with an explicit determinant orientation, transvection cyclotomic multiplicities and negative involution trace. Its asserted novelty is the equivariant calculation, **not** the previously established surface decomposition or dimension.

Assaf et al., *Tropicalizations of locally symmetric varieties* (arXiv:2505.10504v2, Section 4), give the general spectral-sequence and orientation formalism and top-weight dimensions, but do not give the stated \(\operatorname{Sp}_4(\mathbb F_p)\) character or special-element decomposition. Hoffman and Weintraub (2003, Theorem 2.13) compute representations in the ordinary cohomology of the geometric Igusa boundary; that is a different topological object from the boundary **dual complex**. In particular their top ordinary homology carries a permutation representation, with nonnegative character values, whereas the representation here has strictly negative trace on a symplectic involution. The general old boundary theorem is therefore not being rebranded as this dual-complex result.

## Limitations
Only the indicated \(H^2\) / weight-zero degree-three summand is described. The theorem is restricted to odd prime full level; neither nonprime levels nor the action on degree-one link cohomology is treated. It does not decompose the induced representation into irreducible \(G\)-modules. The existing structural surface theorem supplies indispensable input; the independent content here is the signed equivariance, character and subgroup spectra. Older equivariant boundary and automorphic-representation treatments may implicitly yield an equivalent character, even if not stated in the inspected work. Neither published novelty nor independent review has been externally certified.

## References
1. E. Assaf, M. Brandt, J. Bruce, M. Chan, R. Vlad, *Level structures on tropical abelian varieties*, arXiv:2609.14895v1 (first submitted 2026-09-14), Sections 4--5, especially Corollary 5.8 and Theorem 5.12. https://arxiv.org/html/2609.14895v1
2. E. Assaf, M. Brandt, J. Bruce, M. Chan, R. Vlad, *Tropicalizations of locally symmetric varieties*, arXiv:2505.10504v2, Section 4. https://arxiv.org/pdf/2505.10504
3. J. W. Hoffman, S. H. Weintraub, *Cohomology of the boundary of Siegel modular varieties of degree two, with applications*, Fundamenta Mathematicae 178 (2003), 1--47, Sections 2.2--2.3. https://doi.org/10.4064/fm178-1-1
4. T. Oda, J. Schwermer, *Mixed Hodge structures and automorphic forms for Siegel modular varieties of degree two*, Mathematische Annalen 286 (1990), 481--509, especially Propositions 5.3 and 5.5 as cited by reference 1. https://doi.org/10.1007/BF01453584
