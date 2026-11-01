# Self-loop defect of two-sided zero-product bilinear forms

## Finding
Let \(K\) be an arbitrary field, \(Q\) a finite quiver with \(n\geq1\) vertices and \(m\geq0\) arrows (loops and parallel arrows allowed), and let \(A=KQ/\langle\text{paths of length two}\rangle\). Define \(\mathcal B_0(A)\) to be the vector space of \(K\)-bilinear forms \(\phi:A\times A\to K\) satisfying \(\phi(x,y)=0\) whenever \(xy=yx=0\). Define \(\mathcal B_{\mathrm{prod}}(A)\) to be the subspace of forms \(\phi(x,y)=\tau_1(xy)+\tau_2(yx)\) for linear functionals \(\tau_1,\tau_2:A\to K\). If \(\ell\) is the number of loops (counted with multiplicity), then
\[
\dim_K\mathcal B_0(A)=n+2m,\qquad
\dim_K\mathcal B_{\mathrm{prod}}(A)=n+2m-\ell,\qquad
\dim_K(\mathcal B_0(A)/\mathcal B_{\mathrm{prod}}(A))=\ell.
\]
In particular, \(A\) is **two-sided zero-product determined** if and only if its quiver has no loops; oriented cycles and parallel nonloop arrows cause no obstruction.

More precisely, write \(e_i\) for the trivial path at vertex \(i\), write \(a:i\to j\) for an arrow with the convention \(e_i a=a=a e_j\), and denote the coefficient of a basis element \(b\) in \(x\in A\) by \(x_b\). Every \(\phi\in\mathcal B_0(A)\) admits the **unique** expression
\[
\begin{aligned}
\phi(x,y)={}&\sum_i d_i x_{e_i}y_{e_i}\\
&+\sum_{a:i\to j,\ i\ne j}
\bigl[u_a(x_{e_i}y_a+x_a y_{e_j})+v_a(y_{e_i}x_a+y_a x_{e_j})\bigr]\\
&+\sum_{a:i\to i}\bigl[s_a x_{e_i}y_a+t_a x_a y_{e_i}\bigr],
\end{aligned}
\]
with coefficients in \(K\). If \(|K|=q\), there are exactly \(q^{n+2m}\) two-sided zero-product-preserving bilinear forms, of which precisely \(q^{n+2m-\ell}\) factor through the ordered products \((xy,yx)\). The excess ratio is \(q^\ell\).

The defect dimension is also the total number of self-extension arrows, \(\sum_i\dim_K\operatorname{Ext}^1_A(S_i,S_i)\), for the usual simple modules \(S_i\) of this split basic radical-square-zero algebra. This is an equality of dimensions, not a claim of a canonical isomorphism of the two constructions.

## Assumptions and scope
The quiver is finite. No assumption is made that it is acyclic, connected, loopless, or simply laced. The coefficient field is arbitrary, including characteristic two; the finite-field counts require finite \(K\). The path-length-two ideal annihilates every product of two arrow classes. The result concerns bilinear *scalar-valued* forms, not arbitrary nonlinear zero-product-preserving maps or higher radical powers.

## Proof
**1. A concrete algebra basis.** The algebra \(A\) has basis \(\{e_i\}\cup\{a:a\in Q_1\}\). The only nonzero products of basis elements are \(e_i e_i=e_i\), \(e_i a=a\) when \(i\) is the source of \(a\), and \(a e_j=a\) when \(j\) is its target. In particular, if \(a:i\to j\), the coefficient of \(a\) in \(xy\) equals \(x_{e_i}y_a+x_a y_{e_j}\), while its coefficient in \(yx\) equals \(y_{e_i}x_a+y_a x_{e_j}\).

**2. The zero-pair tensor span.** Let \(Z\subseteq A\otimes_K A\) be the span of all pure tensors \(x\otimes y\) with \(xy=yx=0\). The following tensors lie in \(Z\): \(e_i\otimes e_j\) for \(i\ne j\); every \(a\otimes b\) for arrows \(a,b\); and \(e_k\otimes a\) and \(a\otimes e_k\) whenever \(k\) is neither an endpoint of \(a\). If \(a:i\to j\) is not a loop, the two pairs
\[
(e_i+a,e_j-a),\qquad (e_j+a,e_i-a)
\]
have both ordered products zero. Expanding their pure tensors and removing tensors already listed in \(Z\), we obtain
\[
e_i\otimes a-a\otimes e_j\in Z,\qquad
e_j\otimes a-a\otimes e_i\in Z.
\]
Thus, modulo \(Z\), the tensor space is spanned by \(n\) diagonal tensors \(e_i\otimes e_i\), two representatives per nonloop arrow, and two representatives \(e_i\otimes a,a\otimes e_i\) per loop. Therefore \(\dim(A\otimes A)/Z\le n+2m\).

**3. Sharpness and normal form.** Every coefficient functional displayed in the formula in the Finding section vanishes on mutual zero products. For the diagonal functions this follows from the \(e_i\)-component of \(xy=0\). For a nonloop arrow the two displayed functions are precisely the arrow coefficients of \(xy\) and \(yx\). For a loop \(a:i\to i\), \(xy=0\) implies \(x_{e_i}y_{e_i}=0\) and \(x_{e_i}y_a+x_a y_{e_i}=0\); because \(K\) is a field, these force \(x_{e_i}y_a=x_a y_{e_i}=0\) *separately*. Indeed, if the first vertex coefficient is nonzero, the second is zero and then the arrow coefficient forces the first cross term to vanish; the other case is symmetric, and if both coefficients are zero there is nothing to prove. All \(n+2m\) displayed coordinate forms are linearly independent as functions on ordered basis pairs, because their nonzero basis-pair supports are distinct except for the intentionally grouped pairs of a nonloop arrow, which themselves give two disjoint supports. Hence \(\dim \mathcal B_0(A)\ge n+2m\). Duality with \((A\otimes A)/Z\) and Step 2 yields equality and the unique normal form.

**4. Product-form subspace.** Consider the linear map \(T:A\otimes A\to A\oplus A\) given by \(T(x\otimes y)=(xy,yx)\). Each diagonal idempotent contributes one independent image vector \((e_i,e_i)\). A nonloop arrow \(a:i\to j\) contributes independent vectors \((a,0)\) and \((0,a)\), realized for example by \((e_i,a)\) and \((a,e_i)\). A loop contributes only \((a,a)\). Different arrows and vertices occupy disjoint output coordinates. Consequently
\[
\operatorname{rank}T=n+2(m-\ell)+\ell=n+2m-\ell.
\]
The pullback image \(T^*(A\oplus A)^*\) is exactly \(\mathcal B_{\mathrm{prod}}(A)\), giving its dimension. Subtracting from Step 3 gives the defect \(\ell\). If \(\ell=0\), every zero-product-preserving form factors through products; if \(\ell>0\), for any loop \(a:i\to i\), the form \(\phi(x,y)=x_{e_i}y_a\) does not factor: it takes different values on \((e_i,a)\) and \((a,e_i)\), though both ordered products of those pairs equal \(a\).

**5. Relation to self-extensions.** For the radical-square-zero split basic algebra \(A\), its ordinary Gabriel quiver is \(Q\), and the multiplicity of self-extension arrows at \(i\) is \(\dim\operatorname{Ext}^1_A(S_i,S_i)=\dim e_i(J/J^2)e_i\). Since \(J^2=0\), summing equals the loop count \(\ell\). This standard identification is used only for interpretation, not in Steps 1–4.

## Verification
The included standalone \(\texttt{verify.py}\) builds every element of selected algebras over \(\mathbb F_2\) and \(\mathbb F_3\), enumerates all ordered pairs with both products zero, and independently computes the tensor-span rank and the rank of \(T\) by modular Gaussian elimination. It checks the predicted dimensions and defect for 18 configurations: isolated vertices, one or two loops, parallel arrows, bidirectional pairs, a directed triangle, and mixed loop/nonloop cases. Execution gives \(\texttt{VERIFY_OK: 18 exhaustive prime-field configurations}\). These tests are finite checks, not a proof of the unrestricted theorem; Steps 1–4 prove the general statement for arbitrary fields.

## Relationship to prior work
Bajuk and Brešar introduce two-sided zero-product determined algebras, give a tensor characterization and sufficient criteria involving Hochschild homology (arXiv:2209.13194, first arXiv version September 27, 2022). The present counting theorem explicitly computes that tensor obstruction for every radical-square-zero quiver algebra, including oriented cycles and loops. The earlier general criteria do not state the dimension formula or its relation to self-extension loops. Ghahramani and Hosseini treat triangular algebras (published online September 13, 2024); their abstract covers an important acyclic triangular subclass but does not state the quantitative formula for arbitrary quivers with oriented cycles and loops. The established zero-product determined criterion through idempotent generation (Brešar, 2015) concerns the one-sided property, and is not presented here as a new result. Gardella and Thiel's work on zero-product balanced algebras uses a related but different condition. The 2026 incidence-algebra literature is even further restricted to posets and does not directly decide the general cyclic quiver case.

## Limitations
This is a statement about the radical-square-zero quotient and scalar-valued bilinear forms; it does not extend here to higher radical powers, unsplit algebras, or maps not linear in each variable. The mathematical proof is exact, while novelty is assessed relative to the inspected published/accessible literature, not certified publication priority. A fuller unpublished or differently indexed quiver-specific result might exist; the 2024 triangular-algebra article was available only through its abstract/first-page preview for close comparison.

## References
1. Ž. Bajuk and M. Brešar, *Two-sided zero product determined algebras*, Linear Algebra and its Applications 643 (2022), 125–136; accessible author preprint arXiv:2209.13194v1 (September 27, 2022), https://arxiv.org/abs/2209.13194.
2. H. Ghahramani and D. Hosseini, *Two-sided zero product determined triangular algebras*, Journal of Algebra and Its Applications 25 (2026), article 2650006, first publisher-online September 13, 2024, https://doi.org/10.1142/S0219498826500064.
3. E. Gardella and H. Thiel, *Zero-product balanced algebras*, Linear Algebra and its Applications 670 (2023), 121–153; arXiv:2210.07891 (October 14, 2022), https://arxiv.org/abs/2210.07891.
4. M. Brešar, *Finite dimensional zero product determined algebras are generated by idempotents*, Expositiones Mathematicae (2015); used only as established background for the distinct one-sided condition.
5. H. Jia and Z. Xiao, *Functional identities of degree 2 at two-sided zero products on incidence algebras*, arXiv:2608.26853 (2026), abstract-only comparative context, https://arxiv.org/abs/2608.26853.
