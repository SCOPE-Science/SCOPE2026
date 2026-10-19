# The Grassmannian rank-drop stratification of inner derivations in the five-generator exterior algebra

## Finding
Fix an odd prime power \(q\), a five-dimensional \(\mathbb F_q\)-space \(V\), and the associative exterior algebra \(E=\bigwedge V\), of dimension \(32\). For \(a\in E\), let \(r(a)=\operatorname{rank}_{\mathbb F_q}([a,-])\). Set \(B_q=(q-1){5\brack2}_q\), where \({5\brack2}_q=\frac{(q^5-1)(q^4-1)}{(q^2-1)(q-1)}\). The exact rank enumerator is
\[
\sum_{a\in E}t^{r(a)}=q^{17}\left(1+B_qt^2+(q^{10}-1-B_q)t^4+q^{10}(q^5-1)t^8\right).
\]
Consequently the ordinary inner-derivation ranks are precisely \(0,2,4,8\). The centralizer of an element of rank \(r\) has \(q^{32-r}\) elements. The commuting probability is
\[
\operatorname{cp}(E)=q^{-15}\left(1+B_qq^{-2}+(q^{10}-1-B_q)q^{-4}+q^{10}(q^5-1)q^{-8}\right).
\]
Over an algebraic closure of odd characteristic, the reduced rank-\(\le2\) locus is an irreducible \(24\)-dimensional affine cone product whose singular locus is exactly the \(17\)-dimensional center; the rank-\(\le4\) locus is linear of dimension \(27\).

## Assumptions and scope
The field is \(k=\mathbb F_q\), with \(q\) odd, for the numerical formulas. Geometric statements hold over every algebraically closed field \(k\) of characteristic different from \(2\), using the reduced rank loci defined by matrix minors. The algebra is the unital associative Grassmann algebra on \(\dim V=5\) generators; the bracket is the ordinary commutator, not the supercommutator. Write \(E_{\mathrm{even}}=\bigoplus_{j\text{ even}}\bigwedge^jV\) and \(E_{\mathrm{odd}}=\bigoplus_{j\text{ odd}}\bigwedge^jV\), both dimension \(16\). Every element has the unique odd part \(u+\alpha+\tau\) with \(u\in V\), \(\alpha\in\bigwedge^3V\), and \(\tau\in\bigwedge^5V\). Its even part is arbitrary.

## Proof
**Step 1 (commutator reduction).** Graded commutativity and invertibility of \(2\) give \([a,b]=2a_{\mathrm{odd}}\wedge b_{\mathrm{odd}}\). The even part of \(a\) has no effect, and the map vanishes on even \(b\). The top-degree summand \(\tau\) acts trivially on every odd \(b\).

**Step 2 (nonzero linear part).** Suppose \(u\ne0\). Extend \(u\) to a basis \(u,v_2,v_3,v_4,v_5\) of \(V\). Sending the first exterior generator to the odd element \(u+\alpha+\tau\), and sending the other generators to \(v_2,v_3,v_4,v_5\), respects the exterior relations, because odd elements anticommute and have square zero. Its associated graded map on the augmentation filtration is induced by an invertible linear map, so it is an algebra automorphism. Consequently multiplication by the odd part is conjugate as a linear map to multiplication by \(u\). With \(W=\langle v_2,v_3,v_4,v_5\rangle\), the decomposition \(\bigwedge V=\bigwedge W\oplus u\wedge\bigwedge W\) shows that multiplication by \(u\) on the odd subspace has image \(u\wedge(\bigwedge W)_{\mathrm{odd}}\) of dimension \(2^3=8\). Thus \(r(a)=8\) for precisely \((q^5-1)q^{27}\) choices of \(a\).

**Step 3 (zero linear part).** For \(u=0\), only the degree-one input can contribute: \([a,b]=2\alpha\wedge b_1\in\bigwedge^4V\). Choose a nonzero volume form \(\nu\in\bigwedge^5V^*\) and define an alternating bilinear form \(\beta_\alpha(v,w)=\nu(\alpha\wedge v\wedge w)\) on \(V\). The induced map \(v\mapsto\alpha\wedge v\in\bigwedge^4V\) has exactly the rank of \(\beta_\alpha\), because \(\nu\) identifies \(\bigwedge^4V\) with \(V^*\). The linear correspondence \(\alpha\leftrightarrow\beta_\alpha\) is an isomorphism between the ten-dimensional spaces \(\bigwedge^3V\) and \(\bigwedge^2V^*\). Since alternating forms in dimension five have ranks \(0,2,4\), these are exactly the remaining possibilities for \(r(a)\).

**Step 4 (counting).** A rank-two alternating form has a uniquely determined two-dimensional row space \(U\subset V^*\), and is a nonzero element of its one-dimensional \(\bigwedge^2U\). Thus the number of rank-two forms is \(B_q=(q-1){5\brack2}_q\). Rank zero occurs once; rank four occurs \(q^{10}-1-B_q\) times. For \(u=0\), the independent even part and top-degree coefficient supply \(q^{16+1}=q^{17}\) lifts to each form. This proves all coefficients. Centralizer sizes follow from rank-nullity, and the displayed commuting probability follows by averaging \(q^{-r(a)}\) over all \(q^{32}\) choices of \(a\).

**Step 5 (geometry).** The equations \(r(a)\le4\) say precisely \(u=0\), yielding a linear affine \(27\)-space. Inside it, \(r(a)\le2\) says that the corresponding alternating form \(\beta_\alpha\) has rank at most two. Equivalently, its \(4\)-by-\(4\) Pfaffians vanish, defining the affine Pluecker cone over \(\operatorname{Gr}(2,5)\), multiplied by \(\mathbb A^{17}\) from the central coefficients. The Grassmannian is smooth irreducible of projective dimension \(2(5-2)=6\), so its affine cone has dimension \(7\), is irreducible, and is smooth away from its vertex; its vertex is singular since the quadratic Pfaffians have zero differentials there and the cone is proper in \(\mathbb A^{10}\). Hence the rank-\(\le2\) locus has dimension \(24\) and singular locus exactly the rank-zero center of dimension \(17\). The complement \(u\ne0\) is open and dense with rank eight.

For characteristic two the ordinary exterior algebra is commutative, and all inner derivations have rank zero.

## Verification
The companion program `verify_exterior_rank.py` builds the actual commutator matrix in the \(32\)-monomial basis, checks \(400\) sampled odd elements over each of \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\), and exhaustively classifies all \(3^{10}=59049\) trilinear-degree coefficient vectors in the zero-linear stratum over \(\mathbb F_3\). The latter yield rank frequencies \((1,2420,56628)\) for ranks \((0,2,4)\). The program also checks the first \(100000\) ternary-degree coefficient vectors over \(\mathbb F_5\), explicitly non-exhaustively. Its successful completion prints `VERIFY_OK`. Enumeration supplements rather than proves the all-field statements, which follow from the five steps above. The geometric assertions follow from the standard Pluecker cone structure, not from point counts.

## Relationship to prior work
D. Ž. Djoković, *Derivations and Automorphisms of Exterior Algebras* (1978), identifies the inner-derivation ideal and the grading structure; it does not formulate this five-generator centralizer-rank census. V. V. Bavula, *Derivations and skew derivations of the Grassmann algebras* (first arXiv version 2007-04-29), Theorem 2.1, identifies inner derivations as the odd derivation component, while its normal-element and automorphism results provide context for the nonzero-linear orbit. Neither inspected relevant section supplies the rank-two versus rank-four Grassmannian separation, its geometric singular locus, or the complete finite-field enumerator. Classical classification of alternating forms and Pluecker geometry are used, not claimed to be new. A separately available four-generator Grassmann-algebra commutator-fiber census addresses dimension \(16\) rather than this dimension \(32\) rank stratification; its formulas do not imply these dimensions and multiplicities.

## Limitations
This is a fixed five-generator result and does not classify rank spectra for arbitrary generator number, nor all derivations or full conjugacy orbit decompositions. The originality comparison may miss an implicit corollary of a more general theorem or an unindexed specialized source. The irreducibility statement is for the reduced determinantal locus. 

## References
- V. V. Bavula, *Derivations and skew derivations of the Grassmann algebras*, arXiv:0704.3850v1 (2007-04-29), especially Theorem 2.1 and the discussion of automorphisms: https://arxiv.org/abs/0704.3850.
- D. Ž. Djoković, *Derivations and Automorphisms of Exterior Algebras*, Canadian Journal of Mathematics 30 (1978), 1336–1344, DOI:10.4153/CJM-1978-111-5.
