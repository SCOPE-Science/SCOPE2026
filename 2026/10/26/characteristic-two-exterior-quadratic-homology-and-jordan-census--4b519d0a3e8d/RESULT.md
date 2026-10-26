# Characteristic-two exterior-quadratic homology and Jordan census

## Finding
For a vector space \(V\) of dimension \(n\ge2\) over \(\mathbb F_q\), with \(q=2^e\), let \(E=\bigwedge V\). For each \(\omega\in\bigwedge^2V\), let \(L_\omega:E\to E\) denote left multiplication. Write \(2r\) for the rank of the alternating coefficient matrix of \(\omega\); thus \(0\le r\le\lfloor n/2\rfloor\).

Then \(L_\omega^2=0\). Define graded homology at exterior degree \(k\) by
\[
H^k_\omega=\ker(L_\omega:\bigwedge^kV\to\bigwedge^{k+2}V)/\operatorname{im}(L_\omega:\bigwedge^{k-2}V\to\bigwedge^kV).
\]
Its complete Hilbert polynomial is
\[
\sum_{k=0}^n\dim H^k_\omega\,t^k=2^r t^r(1+t)^{n-2r}.
\]
In particular \(\dim\ker L_\omega/\operatorname{im}L_\omega=2^{n-r}\), and the nilpotent Jordan form has \(2^{n-1}-2^{n-r-1}\) blocks of size two and \(2^{n-r}\) blocks of size one (when \(r=0\), the two-block multiplicity is zero).

Exactly
\[
A_{n,r}(q)={n\brack 2r}_q\,q^{r(r-1)}\prod_{i=1}^r(q^{2i-1}-1)
\]
quadratic forms have the indicated type, where \({n\brack k}_q=\prod_{j=0}^{k-1}(q^{n-j}-1)/(q^{k-j}-1)\), and an empty product is one. Hence the complete Jordan-rank enumerator is
\[
\sum_{\omega\in\bigwedge^2V}X^{\operatorname{rank}L_\omega}
=\sum_{r=0}^{\lfloor n/2\rfloor}A_{n,r}(q)X^{2^{n-1}-2^{n-r-1}}.
\]

## Assumptions and scope
Every statement concerns homogeneous degree-two elements of the exterior algebra, not arbitrary radical elements. All finite fields have characteristic two; no claim is made about odd characteristic. Exterior algebra is taken over the given field, with the usual graded wedge product. The rank of a bivector means the rank of its alternating coefficient matrix, not the rank of the multiplication map. Every possible even coefficient-matrix rank occurs. Jordan form is taken as an ordinary linear operator on the ungraded vector space \(E\) of dimension \(2^n\).

## Proof
**1. Square-zero differential.** Express an arbitrary bivector as a sum of decomposable degree-two wedges. Each such wedge squares to zero; distinct degree-two terms commute. In characteristic two the cross terms in their square cancel in pairs. Hence \(\omega\wedge\omega=0\), so \(L_\omega^2=0\). Therefore the displayed graded quotients are defined.

**2. Alternating normal form.** Symplectic Gram-Schmidt elimination over any characteristic-two field gives a basis \(e_1,f_1,\ldots,e_r,f_r,z_1,\ldots,z_{n-2r}\) such that
\[
\omega=\sum_{i=1}^r e_i\wedge f_i.
\]
The coefficient matrix is a direct sum of \(r\) nonsingular alternating two-by-two blocks and a zero block, giving rank \(2r\). This canonical form is valid also at \(r=0\).

**3. Graded homology.** Let \(E_i=\bigwedge\langle e_i,f_i\rangle\). The four basis vectors \(1,e_i,f_i,e_i\wedge f_i\) have degrees \(0,1,1,2\). Local wedge multiplication by \(e_i\wedge f_i\) sends \(1\) to \(e_i\wedge f_i\) and kills the other three vectors. This two-term contractible pair contributes no homology, while \(e_i,f_i\) survive as two degree-one homology vectors. Thus the local graded homology polynomial is \(2t\). As a graded vector space, \(E\cong E_1\otimes\cdots\otimes E_r\otimes\bigwedge\langle z_1,\ldots,z_{n-2r}\rangle\); the operator is the sum of the local degree-two differentials. In characteristic two their tensor sum squares to zero without sign complications. The field Kunneth decomposition, or direct splitting of every local contractible pair, gives total graded homology polynomial \((2t)^r(1+t)^{n-2r}\). This is \(2^r t^r(1+t)^{n-2r}\), as claimed. In particular the degree-\(k\) homology has dimension \(2^r\binom{n-2r}{k-r}\) if \(r\le k\le n-r\), and zero otherwise.

**4. Nilpotent Jordan blocks.** A linear operator with square zero has only Jordan blocks of lengths one and two. Writing \(a\) and \(b\) for their numbers, the total dimension is \(2a+b=2^n\), and \(b=\dim\ker L_\omega/\operatorname{im}L_\omega=2^{n-r}\). Hence \(a=(2^n-2^{n-r})/2=2^{n-1}-2^{n-r-1}\). Distinct \(r\) yield distinct \(b\), so no different alternating-form rank classes have the same Jordan type.

**5. Counting forms.** Choosing the radical of an alternating matrix of rank \(2r\), of dimension \(n-2r\), gives the Gaussian coefficient \({n\brack 2r}_q\) choices. On the \(2r\)-dimensional quotient the induced alternating form must be nondegenerate. The number of nondegenerate alternating forms is the classical ratio \(|\mathrm{GL}_{2r}(q)|/|\mathrm{Sp}_{2r}(q)|=q^{r(r-1)}\prod_{i=1}^r(q^{2i-1}-1)\), since the general linear group acts transitively on these forms and the stabilizer is the symplectic group. Choosing the radical and quotient form is bijective with choosing the original alternating form. All counts include the zero form at \(r=0\). This proves the joint distribution.

## Verification
A standalone deterministic checker, `verify_exterior_quadratic.py`, constructs the alternating coefficient matrices and wedge-multiplication operators independently, computes their ranks by Gaussian elimination in \(\mathbb F_2\) and \(\mathbb F_4\), and compares against the general formula. Exhaustive checks cover dimensions two through five over \(\mathbb F_2\), two through four over \(\mathbb F_4\), and additional normal-form instances in dimensions six and seven over \(\mathbb F_2\). It checks both the per-rank fiber counts and the corresponding multiplication ranks, totaling 5270 tested bivectors. Its expected concluding line is `ALL_EXTERIOR_QUADRATIC_CHECKS_PASSED 5270`. These finite checks supplement, but do not replace, the general proof.

For instance, at \(n=4,q=2\), the respective counts for coefficient rank \(0,2,4\) are \(1,35,28\). The corresponding operator ranks are \(0,4,6\), and every such operator has square zero. Over \(\mathbb F_4\), the corresponding fiber counts are \(1,1071,3024\).

## Relationship to prior work
Alternating-form normal forms and symplectic orbit counts are classical and are used here as known ingredients, not claimed as discoveries. Korhonen (first preprint January 5, 2021) describes Jordan forms of **induced nilpotent endomorphisms** on the exterior square and symmetric square; this is not the same action as multiplication by a bivector on the full exterior algebra. The result here assembles a degree-by-degree differential-homology and all-field finite census for the latter multiplication action. The elementary normal-form and tensor-complex steps are fully displayed so that no originality is claimed for those background techniques.

## Limitations
Only degree-two homogeneous elements and characteristic-two fields are treated. The proof relies on classical alternating-form classification and elementary homological tensor arguments. No corresponding classification for odd characteristic or arbitrary inhomogeneous elements is asserted. Priority risk remains that this exact full-exterior multiplication-homology refinement could have been recorded in earlier symplectic-complex literature, including literature not indexed by the searches conducted. No independent audit has been performed.

## References
1. M. Korhonen, *Decomposition of exterior and symmetric squares in characteristic two*, arXiv:2101.01365v1 (first public January 5, 2021), https://arxiv.org/abs/2101.01365. Journal DOI 10.1016/j.laa.2021.04.018. Related but distinct induced-operator Jordan problem.
2. Standard symplectic normal form for alternating bilinear forms and the order identity \(|\mathrm{GL}_{2r}(q)|/|\mathrm{Sp}_{2r}(q)|\); these are classical facts reconstructed in the proof where used.
