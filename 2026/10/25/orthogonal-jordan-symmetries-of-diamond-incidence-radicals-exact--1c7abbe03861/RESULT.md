# Orthogonal Jordan symmetries of diamond incidence radicals: exact groups and derivation defects

## Finding
Let \(k\) be any field and \(r\ge2\). Let \(P_r\) be the finite poset with one bottom element \(u\), one top element \(w\), and \(r\) pairwise incomparable elements \(v_1,\ldots,v_r\) strictly between them. Write \(A_r=\operatorname{rad} I(P_r,k)\) for the nonunital Jacobson radical of its incidence algebra. A *square-preserving automorphism* means a bijective \(k\)-linear map \(T:A_r\to A_r\) satisfying \(T(a^2)=T(a)^2\) for every \(a\). A *Jordan derivation* here means a \(k\)-linear map \(D\) with \(D(a^2)=D(a)a+aD(a)\) for every \(a\); these quadratic definitions apply even in characteristic two.

**Classification.** With \(V=k^r\oplus k^r\) and \(q(x,y)=x^{\mathsf T}y\), every square-preserving automorphism has a unique form
\[
T(v+t z)=Mv+(f(v)+ct)z,
\qquad M\in\operatorname{GO}(V,q),\quad q(Mv)=c q(v),\quad f\in V^*,\quad c\in k^\times.
\]
Here \(c\) is determined by \(M\). It is an ordinary associative algebra automorphism exactly when \(M=\operatorname{diag}(P,cP^{-\mathsf T})\) for some \(P\in\operatorname{GL}_r(k)\). Both groups have the same central-shear factor \(V^*\).

The Jordan derivations have the unique normal form, relative to \(A_r= k^r_x\oplus k^r_y\oplus kz\),
\[
D=\begin{pmatrix}
P&Q&0\\ R&\lambda I_r-P^{\mathsf T}&0\\ f_x&f_y&\lambda
\end{pmatrix},
\qquad Q^{\mathsf T}=-Q,\quad R^{\mathsf T}=-R,\quad Q_{ii}=R_{ii}=0.
\]
The zero-diagonal clauses are essential in characteristic two. Ordinary associative derivations are exactly those with \(Q=R=0\). Consequently
\[
\dim_k\operatorname{Der}(A_r)=(r+1)^2,\qquad
\dim_k\operatorname{JDer}(A_r)=2r^2+r+1,
\]
and the natural derivation-space defect equals \(r(r-1)\). The defect directions are two copies of the alternating-matrix space, each of dimension \(\binom r2\); the quotient by ordinary derivations is an ordinary-derivation module with these two alternating-matrix directions; the central shears act trivially on that quotient.

For every prime power \(q\), the finite-field counts are
\[
|\operatorname{Aut}(A_r(\mathbb F_q))|=q^{2r}(q-1)|\operatorname{GL}_r(q)|,
\]
\[
|\operatorname{JAut}(A_r(\mathbb F_q))|
=q^{2r}(q-1)\,2q^{r(r-1)}(q^r-1)
\prod_{i=1}^{r-1}(q^{2i}-1),
\]
so the index of associative automorphisms among square-preserving automorphisms is precisely
\[
\boxed{2q^{r(r-1)/2}\prod_{i=1}^{r-1}(q^i+1)}.
\]
The formulas hold for all finite fields, including characteristic two. The boundary \(r=1\), not part of the principal range, has equal derivation spaces but a group index of two.

## Assumptions and scope
For any finite poset \(P\), the incidence algebra has standard basis \(e_{ab}\) indexed by comparable pairs \(a\le b\), with product \(e_{ab}e_{cd}=\delta_{bc}e_{ad}\). Its radical is spanned by basis intervals with \(a<b\). For the stated height-three diamond poset, put \(x_i=e_{u,v_i}\), \(y_i=e_{v_i,w}\) and \(z=e_{u,w}\). The only nonzero basis products are \(x_i y_i=z\); in particular, the radical is associative, \(A_r^2=kz\ne0\) and \(A_r^3=0\). All maps are \(k\)-linear and no unitality is assumed for this nonunital algebra. The result does not cover general incidence algebras, arbitrary height-three posets or all niltriangular matrix algebras.

## Proof
**1. Multiplication form and automorphisms.** Let \(v=(x,y)\) and \(v'=(x',y')\) denote the vector parts. Then \(vv'=x^{\mathsf T}y' z\), so \(v^2=q(v)z\). The vector \(x_1+y_1\) has square \(z\); therefore the linear span of all squares equals \(kz\). Any square-preserving bijection \(T\) must take \(z\) to \(cz\) with \(c\ne0\). Its induced quotient map on \(A_r/kz\) is some \(M\in\operatorname{GL}(V)\), and it has a unique shear \(f\in V^*\). The square equation is exactly \(q(Mv)=cq(v)\), and conversely that equation makes the map square-preserving. Hence its linear part is the general orthogonal similitude group \(\operatorname{GO}(V,q)\), and the shear is unrestricted.

For an ordinary algebra automorphism the bilinear product must also be preserved, i.e. \(B(Mv,Mw)=cB(v,w)\) for \(B((x,y),(x',y'))=x^{\mathsf T}y'\). In block notation \(M=\begin{psmallmatrix}P&Q\\R&S\end{psmallmatrix}\), this is \(M^{\mathsf T}\begin{psmallmatrix}0&I\\0&0\end{psmallmatrix}M=c\begin{psmallmatrix}0&I\\0&0\end{psmallmatrix}\). The left and right kernels of \(B\) are the two distinguished summands and must be preserved, forcing \(Q=R=0\); then \(P^{\mathsf T}S=cI\), so \(S=cP^{-\mathsf T}\). This proves both group descriptions without characteristic restrictions.

**2. Derivation normal forms.** A Jordan derivation \(D\) maps \(z=(x_1+y_1)^2\) into \(kz\), so write \(D(z)=\lambda z\). Modulo \(kz\), write \(D(v)=Mv+f(v)z\), where \(M=\begin{psmallmatrix}P&Q\\R&S\end{psmallmatrix}\). The Jordan square identity is equivalent to
\[
B(Mv,v)+B(v,Mv)=\lambda q(v)
\]
where \(B\) denotes the bilinear form \(B((x,y),(x',y'))=x^{\mathsf T}y'\). Expanding with \(v=(x,y)\) gives
\[
x^{\mathsf T}Rx+y^{\mathsf T}Q^{\mathsf T}y+x^{\mathsf T}(S+P^{\mathsf T}-\lambda I)y=0
\]
for every \(x,y\). Testing standard basis vectors and their pairwise sums (valid even over \(\mathbb F_2\)) yields \(S=\lambda I-P^{\mathsf T}\) and makes \(Q,R\) alternating, meaning skew-symmetric *and zero-diagonal*. Conversely these conditions annihilate the quadratic identity. A usual derivation must preserve every ordered product; this is equivalent to \(M^{\mathsf T}B+BM=\lambda B\), which forces \(Q=R=0\) and the same formula for \(S\). The shears \(f_x,f_y\) are unconstrained because \(z\) annihilates \(A_r\). Counting parameters gives the stated dimensions. For the adjoint statement, commuting an ordinary block-diagonal derivation with a \(Q\)- or \(R\)-direction remains of that same alternating type; central-shear directions belong to the ordinary subalgebra, so the class modulo ordinary derivations carries the asserted alternating modules.

**3. Exact order of the orthogonal group.** Over \(\mathbb F_q\), write \(O_r\) for the isometry group of \(q(x,y)=x^{\mathsf T}y\) on the \(2r\)-dimensional split quadratic space. Its elements act freely and transitively on ordered hyperbolic bases. The number of nonzero isotropic first vectors is
\[
S_r=(q^{r-1}+1)(q^r-1).
\]
Indeed the total number of zeroes of \(q\) is \(q^r+(q^r-1)q^{r-1}\), because \(x=0\) allows all \(y\) and each nonzero \(x\) imposes one independent linear equation on \(y\). Removing zero yields \(S_r\). Fix an isotropic vector \(u\ne0\) and one hyperbolic mate \(v_0\); all isotropic mates \(v\) satisfying the polar pairing \(b(u,v)=1\) are uniquely specified by a vector in the hyperbolic \(2r-2\)-space perpendicular to \(u,v_0\), with one remaining coefficient fixed by \(q(v)=0\). There are exactly \(q^{2r-2}\) choices. Their perpendicular complements support the remaining hyperbolic basis. Thus \(|O_0|=1\) and
\[
|O_r|=(q^{r-1}+1)(q^r-1)q^{2r-2}|O_{r-1}|,
\]
which solves to \(|O_r|=2q^{r(r-1)}(q^r-1)\prod_{i=1}^{r-1}(q^{2i}-1)\). This count is valid for odd and even \(q\), without assuming that the characteristic differs from two.

The multiplier map on \(\operatorname{GO}(V,q)\) is onto \(\mathbb F_q^\times\), since \((x,y)\mapsto(cx,y)\) has multiplier \(c\). Every multiplier fiber is a coset of \(O_r\). Multiplying by the unrestricted \(q^{2r}\) shears gives the Jordan-automorphism count; the block-diagonal ordinary automorphisms give \(q^{2r}(q-1)|\operatorname{GL}_r(q)|\). Since \(|\operatorname{GL}_r(q)|=q^{r(r-1)/2}\prod_{i=1}^{r}(q^i-1)\), their ratio reduces to the boxed expression.

## Verification
The standalone finite-field linear-equation checker `diamond_jordan_checker.py` constructs all multiplication constraints on the basis of \(A_r\). It computes dimensions of the ordinary and quadratic Jordan derivation spaces for \(r=1,2,3,4\) and primes \(p=2,3,5,7\). All sixteen cases agree with the formulas. It also checks the explicit Jordan/ordinary normal forms over characteristics two, three and five, and brute-force enumerates the general orthogonal similitude group for \((r,q)=(1,2),(1,3),(2,2)\). The exact orthogonal orders are checked independently against the hyperbolic-basis recurrence; the higher-dimensional assertions rest on the written proof, not on finite enumeration. Reproduce with `python3 diamond_jordan_checker.py`.

## Relationship to prior work
The 2007 work of Cheng and Jing and 2006 work of Zhang and Yu establish derivation rigidity for certain unital triangular algebras under 2-torsion-free hypotheses. The nonunital branching incidence radical considered here is outside those stated conclusions. Kuzucuoğlu and Levchuk (2010) treat Jordan isomorphisms of *full niltriangular rings indexed by chains*, and Kuzucuoğlu (2011) treats Jordan derivations on strictly triangular matrix rings. Neither indexed class is the branching diamond radical for \(r\ge2\), and their available statements do not imply the claimed orthogonal-group order or the defect formula without additional reductions. The full 2010/2011 articles were not available for complete comparison; consequently the possibility of an indirect general theorem remains a publication-priority risk. Classical split-orthogonal group arithmetic is used and reproved here; the orthogonal order itself is not claimed new. The new proposed contribution is the simultaneous recognition and enumeration of the square-preserving and associative symmetries of this specific natural incidence-radical family, including the quadratic infinitesimal defect.

## Limitations
Absolute publication priority is not established. The results hold for \(r\ge2\) over arbitrary fields, and cardinality formulas require a finite field. Square-preserving is the explicitly stated quadratic definition in characteristic two, which should not be confused with definitions involving a factor of one-half. No analogous classification is claimed for larger posets, the complete incidence algebras or infinite-dimensional radicals. The primary remaining originality risk is an unpublished or insufficiently inspected general theorem for Jordan maps on nonunital rank-one-product algebras or branching incidence radicals.

## References
1. X. Cheng and W. Jing, *On Jordan Derivations of Triangular Algebras*, arXiv:0706.1942v1, first publicly available 13 June 2007. https://arxiv.org/abs/0706.1942
2. F. Kuzucuoğlu and V. M. Levchuk, *Jordan Isomorphisms of Radical Finitary Matrix Rings*, Journal of Algebra and Its Applications 9 (2010), 659–667, doi:10.1142/S0219498810004282.
3. F. Kuzucuoğlu, *Jordan Derivations on Strictly Triangular Matrix Rings*, Algebra Colloquium 18 (2011), 519–522, doi:10.1142/S1005386711000393.
4. X. T. Wang and Y. M. Li, *Decomposition of Jordan Automorphisms of Triangular Matrix Algebra over Commutative Rings*, Glasgow Mathematical Journal 52 (2010), 529–536, doi:10.1017/S0017089510000406.
