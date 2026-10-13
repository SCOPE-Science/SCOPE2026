# Exact dimensions of joint Higgs orbit-type strata
## Finding
Let
\[
p:\mathcal M\longrightarrow\mathcal T_g
\]
be the marked joint moduli space of degree-zero \(\mathrm{SL}_r(\mathbf C)\)-Higgs bundles studied by Cao, with \(g\ge2\) and \(r\ge2\). Let \(\mathscr S\) be a connected orbit-type stratum. At any point of \(\mathscr S\), write the stable isotypic decomposition as
\[
(E,\varphi)=\bigoplus_{\alpha=1}^{s}(E_\alpha,\varphi_\alpha)\otimes\mathbf C^{m_\alpha},
\qquad
\sum_{\alpha=1}^{s}d_\alpha m_\alpha=r,
\]
where the stable factors are pairwise nonisomorphic and \(d_\alpha=\operatorname{rk}E_\alpha\).

Then the vertical complex dimension is exactly
\[
\dim_{\mathbf C}T_{\mathscr S/\mathcal T_g}
=
2(g-1)\left(\sum_{\alpha=1}^{s}d_\alpha^2-1\right)+2(s-1),
\]
and therefore
\[
\dim_{\mathbf C}\mathscr S
=
3g-3+
2(g-1)\left(\sum_{\alpha=1}^{s}d_\alpha^2-1\right)+2(s-1).
\]

In particular, the dimension depends on the ranks of the distinct stable factors but not on their multiplicities \(m_\alpha\), apart from the feasibility constraint \(\sum_\alpha d_\alpha m_\alpha=r\).

Among all non-stable orbit types, the largest possible vertical dimension is
\[
2(g-1)(r-1)^2+2.
\]
It is attained by the type with two nonisomorphic stable factors of ranks \(r-1\) and \(1\), both of multiplicity \(1\). Since the stable vertical dimension is \(2(g-1)(r^2-1)\), the maximal non-stable stratum has codimension
\[
4(r-1)(g-1)-2
\]
inside the stable stratum, and the same codimension in the joint moduli space because every stratum maps submersively to the same Teichmüller base.

## Assumptions and scope
The base curve is a marked smooth projective complex curve of genus \(g\ge2\). The moduli problem is Cao's determinant-trivialized, trace-free degree-zero \(\mathrm{SL}_r(\mathbf C)\) problem. Orbit type means the conjugacy class of the full determinant-one stabilizer, including disconnected components.

The stable isotypic factors all have degree \(0\). No assertion is made for \(\mathrm{GL}_r\)-Higgs moduli, positive degree, parabolic or twisted Higgs bundles, unmarked curve moduli, or compactifications.

## Proof
Cao writes the isotypic decomposition
\[
(E,\varphi)=\bigoplus_{\alpha=1}^{s}(E_\alpha,\varphi_\alpha)\otimes V_\alpha,
\qquad V_\alpha\simeq\mathbf C^{m_\alpha},
\]
and identifies the algebra of Higgs endomorphisms acting on the multiplicity spaces as
\[
\mathcal A_x=\bigoplus_{\alpha=1}^{s}\operatorname{Id}_{E_\alpha}\otimes\operatorname{End}(V_\alpha).
\]
The coefficient bundle controlling the stabilizer-invariant deformation complex is
\[
\mathcal C_x=\operatorname{End}_0(E)^{K_x},
\]
the trace-free part of the commutant of \(\mathcal A_x\). The commutant is
\[
\bigoplus_{\alpha=1}^{s}\operatorname{End}(E_\alpha)\otimes\operatorname{Id}_{V_\alpha}.
\]
Taking trace on the total bundle imposes the single fiberwise equation
\[
\sum_{\alpha=1}^{s}m_\alpha\operatorname{tr}(u_\alpha)=0.
\]
Hence
\[
R:=\operatorname{rk}\mathcal C_x=\sum_{\alpha=1}^{s}d_\alpha^2-1.
\]
Each \(\operatorname{End}(E_\alpha)\) has degree \(0\), and the trace equation is a surjection to the trivial line bundle, so \(\deg\mathcal C_x=0\).

The restricted Higgs deformation complex is
\[
\mathcal C_x\longrightarrow\mathcal C_x\otimes K_X.
\]
Riemann--Roch gives
\[
\chi(\mathcal C_x)=R(1-g),
\qquad
\chi(\mathcal C_x\otimes K_X)=R(g-1),
\]
so the hypercohomology Euler characteristic is
\[
\chi_{\mathrm{Higgs}}=-2R(g-1).
\]
Cao's Lemma 5.5 proves
\[
\dim_{\mathbf C}\mathbb H^0(\mathcal C_x)
=
\dim_{\mathbf C}\mathbb H^2(\mathcal C_x)
=s-1.
\]
Therefore
\[
\dim_{\mathbf C}\mathbb H^1(\mathcal C_x)
=
2(s-1)+2R(g-1)
=
2(s-1)+2(g-1)\left(\sum_\alpha d_\alpha^2-1\right).
\]
Theorem B identifies this invariant harmonic degree-one space with \(T_{\mathscr S/\mathcal T_g}\). Theorem A says \(p|_{\mathscr S}\) is a holomorphic submersion, and \(\dim_{\mathbf C}\mathcal T_g=3g-3\), which gives the total dimension formula.

It remains to optimize over non-stable types. If \(s\ge2\), then \(\sum_\alpha d_\alpha\le r\). For fixed \(s\), convexity gives
\[
\sum_{\alpha=1}^{s}d_\alpha^2
\le
(r-s+1)^2+s-1,
\]
with equality when all multiplicities are \(1\) and the ranks are \(r-s+1,1,\ldots,1\). Put \(t=s-1\). Comparing this bound with the case \(s=2\), the difference after dividing the vertical dimensions by \(2\) is
\[
(t-1)\left((g-1)(2r-t-2)-1\right)\ge0,
\]
with equality only at \(t=1\). If \(s=1\) and the point is non-stable, then \(m_1\ge2\), so \(d_1\le r/2\), which gives a strictly smaller dimension. Thus the unique maximizing numerical type is \((r-1,1)\) with multiplicities \((1,1)\).

This type is nonempty: for \(r>2\), choose a stable degree-zero vector bundle of rank \(r-1\), pair it with the inverse determinant line, and take zero Higgs fields; for \(r=2\), choose a degree-zero line bundle \(L\) with \(L\not\simeq L^{-1}\) and use \(L\oplus L^{-1}\). The codimension formula follows by subtracting from the stable dimension.

## Verification
The source's Theorem A was checked for the holomorphic-submersion statement and Theorem B for the identification of invariant harmonic tangent spaces with the vertical tangent bundle. Its stable isotypic decomposition and full stabilizer were checked in Section 2.3. Proposition 5.3 was checked for the commutant description, and Lemma 5.5 was checked for the exact dimensions \(s-1\) in degrees \(0\) and \(2\).

The rank and degree of \(\mathcal C_x\) were recomputed directly from the commutant and trace equation. The hypercohomology Euler characteristic was then recomputed from ordinary Riemann--Roch, independent of the Higgs differential. The extremal non-stable type was proved by the displayed convexity inequality. As a finite stress test only, all positive rank/multiplicity data with \(2\le r\le7\) and \(2\le g\le5\) were enumerated; the maximizing non-stable vertical dimension always matched \(2(g-1)(r-1)^2+2\). The proof does not rely on that enumeration.

For \(r=2\), the formula gives non-stable fiber dimension \(2g\) and codimension \(4g-6\), agreeing with the familiar split-line locus in fixed-determinant rank-two Higgs moduli.

## Relationship to prior work
Cao proves that the connected orbit-type loci form complex Whitney strata, that every stratum maps submersively to Teichmüller space, and that the invariant harmonic spaces form the vertical tangent bundle. Lemma 5.5 determines the degree-\(0\) and degree-\(2\) invariant harmonic dimensions but leaves the degree-\(1\) rank as an abstract stabilizer-fixed dimension. The exact Riemann--Roch formula above is not stated there.

Fan proves the fixed-curve orbit-type Whitney stratification and complex symplectic structure. The inspected full text does not state an isotypic-rank dimension formula or a multiplicity-independence theorem.

Tirelli studies the different \(\mathrm{GL}_n\) degree-zero Higgs moduli problem and estimates the codimension of its strictly polystable locus by decomposing objects according to rank partitions. That argument neither treats the determinant-one trace-free deformation complex nor gives the joint-stratum formula above. It is nevertheless the closest inspected prior dimension calculation and makes the comparison with a partition-based approach explicit.

## Limitations
The dimension formula describes orbit-type strata, not their number of connected components or closure incidences. It does not determine local singularity types transverse to a stratum. The extremal statement is numerical and does not assert uniqueness of a connected component realizing the maximizing orbit type.

The formula is a short consequence once Cao's invariant deformation bundle is combined with Riemann--Roch. A dimension formula equivalent to this one could exist implicitly in representation-variety or fixed-determinant Higgs literature not located by the targeted searches.

## References
S. Cao, “Stratification of Joint Moduli Spaces of Higgs Bundles,” arXiv:2610.00378v1, first public 2026-09-30; especially Theorems A--B, Section 2.3, Proposition 5.3, and Lemma 5.5.

Y. Fan, “The Orbit Type Stratification of the Moduli Space of Higgs Bundles,” arXiv:2005.13649v1; published in Mathematische Annalen 383 (2022), 1033--1059.

A. Tirelli, “Symplectic Resolutions for Higgs Bundles,” arXiv:1701.07468; especially Lemma 4.5.
