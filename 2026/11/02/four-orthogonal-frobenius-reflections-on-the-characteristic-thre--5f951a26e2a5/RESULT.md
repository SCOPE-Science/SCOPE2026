# Four orthogonal Frobenius reflections on the characteristic-three Fermat double plane

## Finding
Let \(X/\mathbb F_3\) be the smooth degree-two del Pezzo surface in the weighted projective space \(\mathbb P(1,1,1,2)\) with equation
\[
w^2=x^4+y^4+z^4.
\]
Arithmetic Frobenius acts on \(\operatorname{Pic}(X_{\overline{\mathbb F}_3})\) as the product of reflections in four mutually orthogonal roots of square \(-2\) in the \(E_7\) root lattice. In particular, its characteristic polynomial on the rank-eight geometric Picard lattice is
\[
(T-1)^4(T+1)^4,
\]
and the integral Smith normal form of \(F-I\) is \(\operatorname{diag}(1,1,1,1,0,0,0,0)\). The arithmetic Picard rank is four, and
\[
H^1(\operatorname{Gal}(\mathbb F_9/\mathbb F_3),\operatorname{Pic}(X_{\overline{\mathbb F}_3}))=0.
\]
All 56 geometric exceptional curves are defined over \(\mathbb F_9\), but none is individually defined over \(\mathbb F_3\); their Frobenius cycle structure is \(2^{28}\). The 28 branch bitangents have Frobenius cycle structure \(1^4 2^{12}\). The complete zeta function is
\[
Z(X/\mathbb F_3,T)=\frac{1}{(1-T)(1-9T)(1-9T^2)^4},
\]
so, for every integer \(m\geq1\),
\[
\#X(\mathbb F_{3^m})=3^{2m}+1+4\,3^m(1+(-1)^m).
\]
In particular, the counts over \(\mathbb F_3\) and \(\mathbb F_9\) are 10 and 154. The novel object of the assessment is the explicit integral arithmetic Frobenius class and its consequences for the \(\mathbb F_3\) model, not the pre-existing geometric exceptional-curve configuration or the previously published \(\mathbb F_9\) count.

## Assumptions and scope
All geometry takes place in characteristic three. Put \(B=V(x^4+y^4+z^4)\subset\mathbb P^2\). It is the smooth Hermitian plane quartic over \(\mathbb F_9\). Its 28 \(\mathbb F_9\)-points are its 28 hyperflexes; the corresponding 28 tangent lines give all its geometric bitangents. The double cover \(X\to\mathbb P^2\), branched at \(B\), is a smooth del Pezzo surface of degree two. Write \(F\) for arithmetic coordinate Frobenius on geometric divisor classes (the inverse convention yields the same involution here).

For an explicit integral basis of the geometric Picard group, represent \(\mathbb F_9=\mathbb F_3[i]\) with \(i^2=-1\), encode \(a+bi\) as \(a+3b\), and lexicographically order the normalized \(\mathbb F_9\)-projective points \(q=(q_0,q_1,q_2)\in B(\mathbb F_9)\). For each point choose the first lexicographic normalized tangent direction \(v\) that has \(\sum v_j^4=1\) after the deterministic rescaling in the attached verifier. Order the two exceptional curves \(E_{q,+}\), \(E_{q,-}\) consecutively. The seven curves with zero-based indices \(0,3,9,10,28,40,53\) are pairwise disjoint; write their classes as \(e_1,\ldots,e_7\), and put \(L=(-K_X+\sum e_j)/3\). Thus \(L,e_1,\ldots,e_7\) is a basis of the unimodular intersection lattice with form \(\operatorname{diag}(1,-1,-1,-1,-1,-1,-1,-1)\). The enumeration rule and indices, not arbitrary output order, fix this basis.

## Proof
**1. Exhaustion of the exceptional curves.** For each \(q\in B(\mathbb F_9)\), the tangent line has equation \(q_0^3x+q_1^3y+q_2^3z=0\). Choose \(v\) on that line off \(B\), scaled so \(\sum v_j^4=1\). The Hermitian identity gives
\[
\sum_j(sq_j+tv_j)^4=t^4,
\]
since the coefficients of \(st^3\) and \(s^3t\) vanish by the tangent equation and its third power. Its inverse image in \(X\) therefore splits as the two exceptional curves \(w=\pm t^2\). These are 56 different exceptional curves: two over each of 28 different tangent lines. Every smooth degree-two del Pezzo surface in odd characteristic has exactly 56 geometric exceptional curves, corresponding two-to-one to the 28 bitangents, so this constructs all of them.

**2. Exact intersections and Picard coordinates.** The two curves over one bitangent have intersection multiplicity two. Two curves over different bitangents intersect in one point if and only if their explicit values of \(w\) agree at the transverse intersection of the two base lines; otherwise their intersection is zero. Every exceptional curve has self-intersection \(-1\). The attached verifier computes the resulting 56-by-56 integral matrix, finds the seven specified pairwise disjoint curves, and checks every entry against the standard unimodular blow-up form. Contracting those seven curves gives \(\mathbb P^2\) over the algebraic closure. For an exceptional class \(C=aL-\sum m_je_j\), its intersections with \(e_j\) give \(m_j=C\cdot e_j\) and anticanonical degree one gives \(3a-\sum m_j=1\), hence \(a=(1+\sum m_j)/3\). This recovers all 56 integral class vectors from the incidence matrix without numerical approximation.

**3. Frobenius and orthogonal roots.** Apply the coordinate cube map to the explicit parameterizations; it permutes all 56 exceptional curves, preserving the intersection matrix. The exact computed permutation has 28 transpositions and no fixed exceptional curve. Using its images of \(e_1,\ldots,e_7\), together with the fixed anticanonical class, determines the entire eight-dimensional integral matrix \(M\). In the basis \((L,e_1,\ldots,e_7)\), the four column vectors
\[
\begin{aligned}
r_1&=(2,-1,-1,-1,-1,0,-1,-1),\\
r_2&=(0,1,-1,0,0,0,0,0),\\
r_3&=(0,0,0,1,-1,0,0,0),\\
r_4&=(1,0,0,0,0,-1,-1,-1)
\end{aligned}
\]
have self-intersection \(-2\), are pairwise perpendicular, and are perpendicular to \(-K_X\). The exact certificate verifies the matrix identity
\[
M=\prod_{j=1}^{4}\bigl(I+r_jr_j^{\mathsf T}J\bigr),\qquad J=\operatorname{diag}(1,-1,-1,-1,-1,-1,-1,-1),
\]
where the factors are root reflections. Consequently \(M^2=I\), with four \(+1\) and four \(-1\) eigenvalues. The integral Smith calculation gives \(\mathrm{SNF}(M-I)=\operatorname{diag}(1,1,1,1,0,0,0,0)\), so the image of \(M-I\) is saturated in the \(-1\) eigensublattice. Hence \(\ker(I+M)=\operatorname{im}(M-I)\), proving the displayed cyclic Galois cohomology vanishes.

**4. Zeta and descent.** Four of the 28 Hermitian branch points are fixed by cubing, accounting for four fixed bitangents. For \(\mathbb F_3\), a 13-point enumeration of \(\mathbb P^2\) gives ten surface points. For \(\mathbb F_9\), the branch contains 28 points and every nonzero \(\mathbb F_3\) value is a square in \(\mathbb F_9\), hence the surface has \(28+2(91-28)=154\) points. Since \(X\) is geometrically rational, its second étale cohomology is the geometric Picard representation with Tate twist, and the other contributing cohomology is in degrees zero and four. Thus \(F\) has \(4\) eigenvalues each of \(+1,-1\) on Picard classes, yielding the zeta function and all extension-field counts.

## Verification
The self-contained exact finite-field and integer-lattice script `verify.py` uses Python 3 and SymPy 1.14.0 (`requirements.txt`). Run `python verify.py`. It enumerates all 91 projective \(\mathbb F_9\)-points, all 28 Hermitian points, the 56 exceptional curves, their 56-by-56 intersection matrix, a seven-curve disjoint basis, and the Frobenius images. It verifies the integral pairings, the four mutually orthogonal roots, reflection-matrix equality, Smith normal form, and both point counts. Its deterministic output is reproduced verbatim in `verification_output.txt`; a successful run ends with `VERIFY_OK`. The global completeness of the 56 curves uses the general degree-two del Pezzo bitangent theorem, not the finite enumeration alone.

## Relationship to prior work
Salgado–Testa–Várilly-Alvarado (arXiv:1304.6798, 2013, sections 2 and 4) explicitly treat this **same** Fermat double-plane equation **over \(\mathbb F_9\)** and establish its 126 generalized Eckardt points; their Lemma 4 supplies the exceptional curve/bitangent dictionary, and Remark 29 computes Galois cohomology for a distinct nonsquare twist over \(\mathbb F_9\). Kaplan's 2013 dissertation, Proposition 70, already gives the count of 154 points and the maximal-trace identification **over \(\mathbb F_9\)**. Neither result is claimed as new here. Festi–van Luijk (arXiv:1408.0269, 2014) establish unirationality of every degree-two del Pezzo over a finite field, not this specific integral Frobenius representation. Saito's classification of non-F-split degree-two del Pezzo surfaces (2015/2016) identifies the geometric characteristic-three Fermat model; geometric uniqueness is not claimed as new. Bergvall (arXiv:2211.12855, 2022) treats general Frobenius conjugacy classes and their population, which is distinct from identifying the integral class of this explicit \(\mathbb F_3\) equation. The claim assessed here is the concretely identified product of four perpendicular reflections, its primitive integral Smith invariant, Picard descent, and its forced zeta function over \(\mathbb F_3\).

## Limitations
This is an explicit computation-backed algebraic theorem, not an assertion of priority over all possible unindexed tables or code. The 2013 Kaplan thesis is available in full transcribed text but its original PDF was not directly inspected; its matching Fermat \(\mathbb F_9\) model was compared explicitly. Not all historical Weyl-group tables or every appendix in later arithmetic classifications could be examined, leaving a residual risk of equivalent implicit calculations. The arithmetic Picard description is for the exact displayed \(\mathbb F_3\) model; it does not claim the same Frobenius class for all twists over \(\mathbb F_3\). No independent audit has been performed.

## References
1. C. Salgado, D. Testa, A. Várilly-Alvarado, *On the unirationality of del Pezzo surfaces of degree two*, arXiv:1304.6798v1 (first posted 2013-04-25), especially Lemma 4, page 3 and Remark 29. https://arxiv.org/pdf/1304.6798
2. N. Kaplan, *Rational Point Counts for del Pezzo Surfaces over Finite Fields and Coding Theory*, Harvard doctoral dissertation (2013), Proposition 70, pages 122–123. https://dash.harvard.edu/entities/publication/73120378-b816-6bd4-e053-0100007fdf3b
3. D. Festi, R. van Luijk, *Unirationality of del Pezzo surfaces of degree two over finite fields*, arXiv:1408.0269 (2014). https://arxiv.org/abs/1408.0269
4. N. Saito, *Characterization of non-F-split del Pezzo surfaces*, Kyoto University symposium record (2015), DOI:10.14989/218272. https://doi.org/10.14989/218272
5. O. Bergvall, *Frobenius actions on Del Pezzo surfaces of degree 2*, arXiv:2211.12855 (2022). https://arxiv.org/abs/2211.12855
