# The four-component singular locus of the characteristic-two binary Nash cubic

## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\). In the projective coefficient space \(\mathbb P^{11}_k\) of three binary bilinear forms on \((\mathbb P^1)^3\), the **reduced** mixed/Nash discriminant is an irreducible cubic \(D=V(Q)\). Its reduced singular locus has exactly four irreducible components: a five-dimensional component \(\Sigma\) of degree \(14\) and three pairwise-disjoint linear spaces \(L_A,L_B,L_C\cong\mathbb P^3\). Each \(L_i\) meets \(\Sigma\) in a smooth quadric surface. The primitive characteristic-zero sextic discriminant reduces modulo \(2\) to \(Q^2\); this elementary factorization was already implicit in the classical integral discriminant formula and is not asserted as a separate new contribution.

## Assumptions and scope
Use homogeneous coordinates \(([x_0:x_1],[y_0:y_1],[z_0:z_1])\) on \((\mathbb P^1)^3\). For three independent \(2\times2\) coefficient matrices \(A=(a_0,a_1;a_2,a_3)\), \(B=(b_0,b_1;b_2,b_3)\), \(C=(c_0,c_1;c_2,c_3)\), define
\[
F_1=(y_0,y_1)A(z_0,z_1)^T,\quad F_2=(x_0,x_1)B(z_0,z_1)^T,\quad F_3=(x_0,x_1)C(y_0,y_1)^T.
\]
The discriminant is the Zariski-closed locus of triples whose projective complete-intersection zero scheme is not transverse (including positive-dimensional zero schemes), with its **reduced** structure. Put \(J=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\), and define three new, invertibly related matrices \(U=AJ\), \(V=B^T J\), \(W=CJ\). Then
\[
Q=\operatorname{tr}(UVW)\in k[a_0,\ldots,a_3,b_0,\ldots,b_3,c_0,\ldots,c_3].
\]
This is a genuine multihomogeneous cubic of tridegree \((1,1,1)\) in the three coefficient blocks. All claims concern this algebraic coefficient space and do not impose positivity or a game-theoretic equilibrium interpretation in characteristic two.

## Proof
**1. Elimination and the reduced discriminant.** In the chart \(x_0=y_0=z_0=1\), set \(A_0(z)=a_0+a_1z\), \(A_1(z)=a_2+a_3z\), \(B_0(z)=b_0+b_1z\), \(B_1(z)=b_2+b_3z\). On the open locus where \(A_1B_1\ne0\), the first two equations solve as \(y=-A_0/A_1\) and \(x=-B_0/B_1\). The third equation becomes the quadratic
\[
P(z)=c_0A_1B_1-c_1A_0B_1-c_2B_0A_1+c_3A_0B_0=p_2z^2+p_1z+p_0.
\]
Expansion gives, modulo two,
\[
\begin{split}
\overline{p_1}=Q={}&(a_2b_3+a_3b_2)c_0+(a_0b_3+a_1b_2)c_1\\
&+(a_2b_1+a_3b_0)c_2+(a_0b_1+a_1b_0)c_3.
\end{split}
\]
This equals \(\operatorname{tr}(AJB^TJCJ)\) by an eight-term expansion. A quadratic in characteristic two has a repeated geometric root, over the degree-two finite part, exactly when its middle coefficient vanishes. The polynomial \(Q\) is irreducible: it is linear in the \(c\)'s, and its four coefficients have gcd \(1\). Indeed \(a_2b_3+a_3b_2\) is irreducible and does not divide \(a_0b_3+a_1b_2\). Thus \(V(Q)\) is an irreducible cubic.

To rule out additional discriminant components on boundary charts, consider the universal incidence of a common zero \(q\in(\mathbb P^1)^3\) where the \(3\times3\) local Jacobian has rank below three. At each \(q\), the three vanishing conditions are independent linear conditions on the twelve coefficients, and the six nonforced first derivatives can be chosen independently (each bilinear form has arbitrary value and two active partial derivatives). In those derivatives the Jacobian determinant is a sum of two squarefree monomials in disjoint sets of three variables. It is irreducible, so the total incidence is irreducible of dimension \(10\) (over the base of dimension \(3\)). Its proper image is therefore irreducible, and the elimination calculation identifies its dense hypersurface image with \(V(Q)\). For example \(F_1=y+z\), \(F_2=x+z\), \(F_3=xy\) has exactly the double zero \((0,0,0)\), no zero at infinity, proving the image has dimension \(10\). Hence the reduced discriminant equals \(V(Q)\), globally.

**2. Singular locus as a three-cycle of complexes.** The linear change \((A,B,C)\mapsto(U,V,W)\) is invertible. Differentiating \(Q=\operatorname{tr}(UVW)\) with respect to all twelve matrix entries yields
\[
\operatorname{Sing}(V(Q))_{\mathrm{red}}=V(UV,VW,WU)_{\mathrm{red}}.
\]
The Euler identity also ensures \(Q=0\) on this Jacobian locus (the degree \(3\) equals \(1\) in characteristic \(2\)). If one of \(U,V,W\) is invertible, the two adjacent composition equations force the other two matrices to vanish. This gives three irreducible linear components \(L_U,L_V,L_W\cong\mathbb P^3\). Otherwise all three matrices have rank at most one.

**3. The remaining component.** Regard the maps as a cycle \(V_2\xrightarrow{U}V_1\xrightarrow{W}V_3\xrightarrow{V}V_2\), with all vector spaces two-dimensional. When all ranks are at most one and all consecutive compositions vanish, choose lines \(\ell_i\subset V_i\) between the incoming image and outgoing kernel at each vertex. The maps then factor as \(V_i/\ell_i\to\ell_{i+1}\). Conversely every such triple has all consecutive compositions zero. Over \(T=(\mathbb P^1)^3\), with \(h_i\) denoting its three hyperplane classes, these factorizations form the projectivization of the rank-three bundle
\[
E=\mathcal O_T(-1,-1,0)\oplus\mathcal O_T(0,-1,-1)\oplus\mathcal O_T(-1,0,-1).
\]
The natural morphism \(\mathbb P_T(E)\to\mathbb P^{11}\) has image \(\Sigma\), is projective and generically one-to-one (nonzero rank-one maps determine the three lines). Thus \(\Sigma\) is irreducible of dimension \(3+2=5\), and the projective-bundle push-forward formula gives
\[
\deg\Sigma=\int_T s_3(E)=[t^3h_1h_2h_3]\prod_{\{i,j\}=\{1,2\},\{2,3\},\{3,1\}}(1-t(h_i+h_j))^{-1}=14.
\]
Indeed, the coefficient is \(12+2=14\), with \(h_i^2=0\). Each coordinate \(\mathbb P^3\) meets \(\Sigma\) exactly where its remaining matrix has rank at most one, namely on the Segre quadric \(\mathbb P^1\times\mathbb P^1\subset\mathbb P^3\). The three coordinate \(\mathbb P^3\)'s are pairwise disjoint. None is contained in \(\Sigma\), since each contains invertible matrices. These are all four irreducible components, with no unlisted components.

**4. Integral specialization.** The classical primitive sextic is the quadratic discriminant \(p_1^2-4p_0p_2\), equivalently the published \(6\times6\) determinant. Modulo \(2\) it is \(Q^2\); this statement concerns specialization of that *polynomial*, not a claim that the reduced discriminant cubic is nonreduced as a variety.

## Verification
The standalone file `verify.py` symbolically checks the middle-coefficient/trace identity and modulo-two specialization; computes the projective-bundle degree \(14\) exactly; and enumerates the \(4095\) nonzero coefficient vectors over \(\mathbb F_2\) to compare the Jacobian equations with the product-zero criterion. Running `python verify.py` with Python 3 and SymPy returns `VERIFY_OK`. The finite-field enumeration is only a consistency check: the global decomposition, irreducibility, dimension and degree are proved above for all algebraically closed fields of characteristic two.

## Relationship to prior work
Emiris and Vidunas, *Discriminants of multilinear systems* (2016), Section 5, already give the classical discriminant as a quadratic discriminant and as a \(6\times6\) determinant. Abo, Portakal and Sodomaco, *A vector bundle approach to Nash equilibria* (public 2025), Theorem 3.11 and Remark 3.12, prove the characteristic-zero degree-six discriminant and its determinant representation; their Section 3.2 studies singular strata in that setting. Neuhaus, Portakal, Sodomaco and Tung, *Nashtopes and their A-discriminants* (2026), Example 2.4 and the strictly balanced degree formula, recover the complex 3-player format. Thus the square modulo two is an immediate formal consequence of earlier formulas and **not** the originality claim. The contribution assessed here is the complete four-component reduced **characteristic-two** singular locus, including the degree \(14\) of its nonlinear component and the three quadric intersections. General theories of circular-complex representation varieties may imply the rank-stratum decomposition, but the exact degree and this discriminant identification were not found in the inspected sources.

## Limitations
The result is limited to three two-dimensional factor spaces in characteristic \(2\). It classifies the **reduced** singular locus, not its possibly nonreduced Jacobian scheme, and does not analyze larger game formats or other primes. The primitive sextic and its elementary characteristic-two square are known/implicit from 2016; claiming them alone would not establish originality. A broader older circular-complex theorem might contain an implicit route to the four components; the degree \(14\) and arrangement are independently computed here. Independent mathematical auditing has not occurred.

## References
1. I. Z. Emiris and R. Vidunas, *Discriminants of multilinear systems*, arXiv:1607.01496v1 (2016), §5, equations (10)–(11).
2. H. Abo, I. Portakal, and L. Sodomaco, *A vector bundle approach to Nash equilibria*, arXiv:2504.03456v1 (first public 2025-04-04), §3.2, Theorem 3.11 and Remark 3.12.
3. E. Neuhaus, I. Portakal, L. Sodomaco, and K. Tung, *Nashtopes and their A-discriminants*, arXiv:2610.29889v1 (2026-10-21), Example 2.4 and the balanced-format degree theorem.
4. *Moduli Spaces of Representations of Special Biserial Algebras*, International Mathematics Research Notices (2020), general circular-complex context; only its publicly accessible abstract/introduction was compared for this run.
