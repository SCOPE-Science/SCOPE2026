# The Klein-Jacobian \(H_{168}\)-quotient has five singular curves
## Finding
Let \(C\subset\mathbf P^2_{\mathbf C}\) be Klein's quartic, let \(J=\operatorname{{Jac}}(C)\), and let
\[
H=\operatorname{{Aut}}(C)\cong\operatorname{{PSL}}(2,7),\qquad |H|=168.
\]
Set \(Y=J/H\). Then
\[
\operatorname{{Sing}}(Y)_{{\mathrm{{red}}}}
\]
has exactly seven irreducible components: five curves and two isolated points. The five curve components have generic transverse ADE types
\[
A_1,\ A_1,\ A_1,\ A_2,\ A_3.
\]
More precisely, the reduced positive-dimensional non-free locus in \(J\) consists of exactly
\[
63+28+21=112
\]
elliptic curves. Their generic stabilizers in \(H\) are respectively \(C_2\), \(C_3\), and \(C_4\), and the corresponding families split into \(3\), \(1\), and \(1\) \(H\)-orbits. Thus the quotient has three curve components generically analytically \(\mathbf C\times A_1\), one generically \(\mathbf C\times A_2\), and one generically \(\mathbf C\times A_3\). In addition, \(Y\) has exactly two isolated singularities, both of cyclic type
\[
\frac1{{7}}(1,2,4).
\]

Writing \(G=\{{\pm1\}}\times H\) and \(X=J/G\), the natural degree-two quotient \(Y\to X\) sends two of the three generic \(A_1\) components and the generic \(A_2\) and \(A_3\) components into the smooth locus of \(X\), while the third generic \(A_1\) component maps onto the unique singular curve of \(X\). The two isolated order-seven points of \(Y\) are exchanged by \(-1\) and merge to the unique isolated \(\frac1{{7}}(1,2,4)\) point of \(X\).

## Assumptions and scope
All varieties are over \(\mathbf C\). The action of \(H\) is the standard action induced by the automorphism group of Klein's quartic on its Jacobian. The statement concerns the reduced irreducible-component structure of the singular locus and the generic transverse analytic type along each curve component. At the finitely many intersections and dissident points the local stabilizer can be larger, so the claim does not assert that every point of a given component has the generic product singularity.

The source classifies the stabilizers and fixed loci for the actions of \(H\) and \(G\). The sequel identifies \(Y\) as the index-two Calabi--Yau orbifold cover of \(X\) and notes that \(Y\) has non-isolated singularities, but does not enumerate their irreducible components or their generic ADE types.

## Proof
The representation of \(H\) on the tangent space of \(J\) is contained in \(\operatorname{{SL}}_3(\mathbf C)\). Therefore \(H\) has no nonidentity pseudoreflections: a nontrivial pseudoreflection in dimension three has eigenvalues \(1,1,\lambda\) with \(\lambda\ne1\), hence determinant \(\lambda\ne1\). By the local Chevalley--Shephard--Todd criterion, a point of \(Y\) is singular exactly when a lift to \(J\) has nontrivial \(H\)-stabilizer.

Markushevich--Moreau list the parabolic cyclic stabilizers in \(H\). There are \(21\) involutions, each an anti-reflection. Its fixed locus is a disjoint union of four elliptic curves. The connected component through zero is also the fixed curve of the unique cyclic subgroup \(C_4\) containing that involution. Hence, after removing those \(21\) axis curves, the involutions contribute
\[
21\cdot3=63
\]
distinct translated elliptic curves with generic stabilizer \(C_2\). Distinctness follows because a common curve for two different involutions would give a generic stabilizer containing both involutions, contradicting the source's generic stabilizer calculation.

The same source gives one conjugacy class of \(28\) cyclic subgroups \(C_3\), each fixing one elliptic curve, and one conjugacy class of \(21\) cyclic subgroups \(C_4\), each fixing one elliptic curve. Thus the reduced positive-dimensional non-free locus has
\[
63+28+21=112
\]
elliptic components, with generic stabilizers \(C_2,C_3,C_4\) in the indicated numbers.

It remains to count their images in \(Y\). For each translated \(C_2\)-curve, the subgroup of \(H\) preserving that curve has order \(8\) and is dihedral, so its orbit has length
\[
168/8=21.
\]
The \(63\) curves therefore form exactly three \(H\)-orbits. For a \(C_3\)-fixed elliptic curve the setwise stabilizer is \(S_3\) of order \(6\), giving orbit length \(168/6=28\), hence one orbit. For a \(C_4\)-fixed elliptic curve the setwise stabilizer is \(D_8\) of order \(8\), giving orbit length \(21\), again one orbit. Images of distinct curve-orbits cannot coincide in a finite quotient, so \(Y\) has exactly five positive-dimensional irreducible singular components.

The generic transverse types are read from the tangent representations. An involution is an anti-reflection with eigenvalues \(1,-1,-1\), so transversally the quotient is \(\mathbf C^2/\frac1{{2}}(1,1)=A_1\). A generic order-three stabilizer has one fixed tangent direction and, because it lies in \(\operatorname{{SL}}_3\), transverse eigenvalues \(\zeta_3,\zeta_3^{-1}\); hence its transverse quotient is \(A_2\). For the order-four generator displayed in the source,
\[
(z_1,z_2,z_3)\longmapsto(z_1,-z_3,z_2),
\]
the transverse eigenvalues are \(i,-i\), so the quotient is \(A_3\). Equivalently, for \(n=2,3,4\), the transverse invariant ring for \((u,v)\mapsto(\zeta_nu,\zeta_n^{-1}v)\) is generated by \(u^n,v^n,uv\) with relation
\[
(u^n)(v^n)=(uv)^n,
\]
the surface singularity \(A_{{n-1}}\).

The source also proves that the only zero-dimensional irreducible components of the non-free locus are the \(48\) nonzero points fixed by elements of order seven. They split into two \(H\)-orbits of length \(24\), and their images in \(Y\) are two isolated singularities of type \(\frac1{{7}}(1,2,4)\). This completes the component count.

Finally, the source's comparison with the full group \(G\) shows that, among the three translated \(C_2\)-families, two have generic \(G\)-stabilizer generated by reflections and therefore map to smooth points of \(X\), while the third retains cyclic stabilizer \(C_2\) and yields the singular curve of \(X\). The generic \(C_3\) and \(C_4\) stabilizers enlarge in \(G\) to reflection-generated groups and also map to the smooth locus. The central element \(-1\) exchanges the two order-seven \(H\)-orbits, giving the unique isolated order-seven singularity of \(X\).

## Verification
The orbit arithmetic and local cyclic-quotient models were replayed by the accompanying script `verification/verify.py`. It checks the counts \(63,28,21\), the orbit decomposition \(3+1+1\), the five generic ADE labels, the two isolated order-seven components, and the determinant/eigenvalue data for the order-two and order-four tangent actions. The script also verifies the relation \(ab=c^n\) for the transverse cyclic quotients \(n=2,3,4\) symbolically.

The computation is auxiliary: exhaustiveness comes from the source's classification of stabilizers and fixed loci, not from finite sampling. The local product descriptions are asserted only at generic points of the five curve components.

## Relationship to prior work
Markushevich--Moreau's first paper explicitly determines two isolated \(\frac1{{7}}(1,2,4)\) singularities of \(Y=J/H\) and gives the complete fixed-locus and stabilizer data needed above, but its global singularity theorem is stated for \(X=J/G\), not for \(Y\). Their sequel identifies \(Y\to X\) as a natural double Calabi--Yau orbifold cover and says that \(Y\) has non-isolated singularities, while leaving the study of this orbifold for future work. The present result extracts from the published stabilizer data the full irreducible-component count of \(\operatorname{{Sing}}(Y)_{{\mathrm{{red}}}}\) and its generic ADE profile.

Searches for the exact quotient, for the five-component/ADE formulation, for the \(112\)-elliptic-curve preimage, and for equivalent \(H_{{168}}\)-quotient terminology found no published statement implying this stratification. The closest literature inspected is the two Markushevich--Moreau papers themselves.

## Limitations
The result describes the reduced singular locus and generic transverse type of each curve component. It does not classify all finitely many dissident/intersection germs, compute a crepant resolution, or determine stringy/Hodge invariants of \(Y\). It also does not claim that the five curve components are mutually disjoint; special points can lie on several components and have larger noncyclic stabilizers.

## References
1. D. Markushevich and A. Moreau, *Action of the automorphism group on the Jacobian of Klein's quartic curve*, arXiv:2107.03745, first posted 2021-07-08; later published in *Birational Geometry, Kähler--Einstein Metrics and Degenerations*, Springer Proceedings in Mathematics & Statistics 409 (2023), DOI 10.1007/978-3-031-17859-7_29.
2. D. Markushevich and A. Moreau, *Action of the automorphism group on the Jacobian of Klein's quartic curve II: Invariant theta functions*, arXiv:2208.08737, first posted 2022-08-18; Épijournal de Géométrie Algébrique 8 (2024), Article 9, DOI 10.46298/epiga.2024.11511.
