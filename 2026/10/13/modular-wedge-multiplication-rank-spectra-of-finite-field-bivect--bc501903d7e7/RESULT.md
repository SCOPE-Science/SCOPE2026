# Modular wedge-multiplication rank spectra of finite-field bivectors

## Finding
For a finite field \(k=\mathbb F_q\) of characteristic \(p\), a vector space \(V\) of dimension \(n\ge1\), and \(\omega\in\bigwedge^2V\), consider the linear map \(L_\omega:\bigwedge V\to\bigwedge V\), \(\eta\mapsto\omega\wedge\eta\). This theorem determines the complete multiplicity distribution of \(\operatorname{rank}_k L_\omega\) as \(\omega\) runs through the \(q^{\binom n2}\) bivectors.

Define \(\binom ci=0\) for \(i<0\) or \(i>c\). For \(c\ge1\) and \(0\le j<c\), put \(a=\min\{j,c-j-1\}\) and
\[
 b_p(c,j)=\sum_{i=0}^{a}\left(\binom ci-\binom c{i-1}\right)\mathbf1_{p\nmid(a+1-i)},\qquad
 f_p(c)=\sum_{j=0}^{c-1}b_p(c,j),\qquad f_p(0)=0.
\]
For \(0\le r\le\lfloor n/2\rfloor\) define
\[
 R_p(n,r)=2^{n-2r}\sum_{s=0}^{r}\binom rs2^s f_p(r-s),\qquad
 A_q(n,r)={n\brack 2r}_q\,q^{r(r-1)}\prod_{i=1}^r(q^{2i-1}-1).
\]
The Gaussian coefficient \({n\brack h}_q\) denotes the number of \(h\)-dimensional subspaces of \(k^n\); empty sums are zero and empty products are one.

**Theorem.** Let \(2r\) be the rank of the alternating matrix representing \(\omega\). Then \(\operatorname{rank}L_\omega=R_p(n,r)\). For fixed \(n,p\), these operator ranks are strictly increasing as \(r\) increases. Exactly \(A_q(n,r)\) bivectors have this rank, hence their full rank enumerator is
\[
 \boxed{\mathcal H_{n,q}(T)=\sum_{r=0}^{\lfloor n/2\rfloor}A_q(n,r)T^{R_p(n,r)}.}
\]
In characteristic two this simplifies to \(R_2(n,r)=2^{n-r-1}(2^r-1)\), so the rank of the multiplication operator alone recovers the alternating-form rank even though high wedge powers of \(\omega\) can vanish for characteristic reasons.

For instance, \(\mathcal H_{4,2}(T)=1+35T^4+28T^6\). In dimension six, the full-alternating-rank operator has rank \(28\) in characteristic two, but rank \(29\) in characteristic three, illustrating the modular change.

## Assumptions and scope
The exterior algebra is the ordinary alternating quotient of the tensor algebra, **also in characteristic two**, so \(v\wedge v=0\) for every vector \(v\). There is no fixed nondegenerate pairing on \(V\). The alternating matrix of \(\omega\) is its coordinate coefficient matrix; its rank is independent of basis and is even in all characteristics. The theorem counts bivectors, not arbitrary degree-even exterior-algebra elements and not exterior multiplication by arbitrary inhomogeneous elements. The field size \(q\) may be any prime power and its characteristic is the prime \(p\).

## Proof
**1. Alternating normal form.** Elementary simultaneous row-column operations on an alternating matrix put every \(\omega\) in the form
\[
 \omega=z_1+\cdots+z_r,\qquad z_i=a_i\wedge b_i,
\]
where \(a_1,b_1,\dots,a_r,b_r\) are linearly independent and the remaining \(d=n-2r\) basis vectors span a complementary subspace \(W\). This classification is valid in characteristic two because the defining condition is alternating, not merely skew-symmetric. The factor \(\bigwedge W\) multiplies every operator rank by \(2^d\).

**2. Exact exterior-to-Boolean decomposition.** In the exterior algebra on the \(r\) two-dimensional pairs, each pair contributes exactly one of \(1,a_i,b_i,z_i\) to a basis monomial. Fix a set \(S\) of \(s\) pairs from which a single variable is selected, and fix one of its \(2^s\) choices of \(a_i\) or \(b_i\). Multiplication by \(z_1+\cdots+z_r\) preserves this summand: the selected pairs are annihilated, and on each of the other \(c=r-s\) pairs it changes \(1\) into \(z_i\) and annihilates \(z_i\). Thus the summand is canonically a Boolean-subset module, with degree-\(j\) operator
\[
 U_{c,j}:k^{\binom cj}\longrightarrow k^{\binom c{j+1}},\qquad e_J\longmapsto\sum_{i\notin J}e_{J\cup\{i\}}.
\]
Because each \(z_i\) is of even degree, no signs arise when it crosses exterior factors. Summing all summands gives
\[
 \operatorname{rank}L_\omega
 =2^{n-2r}\sum_{s=0}^r\binom rs2^s
      \sum_{j=0}^{r-s-1}\operatorname{rank}_k U_{r-s,j}.
\]

**3. The modular inclusion-matrix rank.** The matrix of \(U_{c,j}\) is the transpose of the inclusion matrix from \(j\)-subsets to \((j+1)\)-subsets of a \(c\)-set. For \(j\le c-j-1\), Wilson's unimodular diagonal form gives diagonal entries \(j+1-i\) with multiplicities \(\binom ci-\binom c{i-1}\), indexed by \(0\le i\le j\). Reduction modulo \(p\) keeps precisely entries nonzero modulo \(p\). When \(j>c-j-1\), complementing subsets identifies \(U_{c,j}\) with the transpose of \(U_{c,c-j-1}\), preserving rank. Therefore \(\operatorname{rank}_k U_{c,j}=b_p(c,j)\), and Step 2 yields \(R_p(n,r)\) exactly. The required integer diagonal form is stated and proved as Corollary 3 of Ghorbani--Khosrovshahi--Maysoori--Mohammad-Noori (2007), following Wilson (1990); its hypotheses \(j\le j+1\le c-j\) hold in the lower-half case.

**4. Exact multiplicities.** A bivector of coefficient rank \(2r\) has a radical of dimension \(n-2r\). Choose that radical in \({n\brack 2r}_q\) ways and then choose a nondegenerate alternating form on its \(2r\)-dimensional quotient. The latter space is the homogeneous space \(\mathrm{GL}_{2r}(q)/\mathrm{Sp}_{2r}(q)\), of cardinality \(q^{r(r-1)}\prod_{i=1}^r(q^{2i-1}-1)\). Every form occurs exactly once, giving \(A_q(n,r)\), including \(r=0\).

**5. Operator rank strictly detects the alternating rank.** Let \(T_r\) denote multiplication by \(z_1+\cdots+z_r\) on the \(4^r\)-dimensional exterior algebra of the \(2r\) paired variables, and put \(g_r=\operatorname{rank}T_r\). Adding one paired factor splits the new space into two single-occupancy copies carrying \(T_r\), and one even-occupancy pair with matrix \(\left(\begin{smallmatrix}T_r&0\\I&T_r\end{smallmatrix}\right)\). Hence
\[
 g_{r+1}=2g_r+4^r+\operatorname{rank}(T_r^2).
\]
Since \(T_r\) is nilpotent, \(4^r+\operatorname{rank}(T_r^2)-2g_r\) equals the number of its size-one Jordan blocks. At least \(2^r\) such blocks exist: take monomials with exactly one of \(a_i,b_i\) for each pair. They lie in the kernel, while every image monomial contains an entire pair \(z_i\), so their span is disjoint from the image. It follows that \(g_{r+1}>4g_r\). For fixed \(n\), multiplication by \(2^{n-2r}\) therefore gives \(R_p(n,r+1)>R_p(n,r)\), as required.

**6. Characteristic-two simplification.** Since the even elements \(z_i\) commute, each has square zero, and \(p=2\), we have \(T_r^2=0\). The recurrence becomes \(g_{r+1}=2g_r+4^r\), with \(g_0=0\), giving \(g_r=(4^r-2^r)/2\) by induction. Multiplication by the unpaired factor yields \(R_2(n,r)=2^{n-r-1}(2^r-1)\). This also holds at \(r=0\) for \(n\ge1\).

## Verification
The self-contained script `verify.py` reconstructs the exterior-multiplication matrices from wedge signs and checks their ranks by independent modular Gaussian elimination. It also independently constructs each bivector's alternating coefficient matrix and verifies the exact rank and the Gaussian-multiplicity formula. Exhaustive tests cover every bivector in dimensions \(3,4,5\) over \(\mathbb F_2\) and dimension \(4\) over \(\mathbb F_3\); canonical-form tests cover characteristics \(2,3,5,7\) and dimensions up to seven. This is finite validation, not an exhaustive proof in arbitrary dimension.

## Relationship to prior work
Kustin and Vraciu, *The Weak Lefschetz Property for monomial complete intersections* (arXiv:1110.2822v1, first public October 13, 2011), study maximal rank of multiplication by linear forms in monomial complete intersections. The Boolean summands above are such square-zero complete intersections, but their Lefschetz-property criteria do not enumerate all exterior multiplication ranks or alternating-form fibers. Ghorbani, Khosrovshahi, Maysoori and Mohammad-Noori, *Inclusion Matrices and Chains* (arXiv:0709.3144v1, first public September 20, 2007), give Wilson's classical integral diagonal form for subset-inclusion matrices; that key ingredient is explicitly credited in Step 3. The standard count of alternating-form orbits, including characteristic two, appears for instance in Friedrich Knop's June 7, 2016 mathematical discussion cited below. The present theorem combines these inputs with the exterior-to-Boolean decomposition, proves strict operator-rank recovery, and determines the complete finite-field rank enumerator. A historically equivalent combined statement has not been ruled out.

## Limitations
No complete Jordan-block distribution is claimed, only the operator rank distribution. The result is specific to homogeneous exterior degree two, not general even-degree elements. The result does not classify similarity classes of exterior-algebra multiplication operators beyond rank, and the count concerns all bivectors rather than random elements of the whole exterior algebra. Bibliographic coverage of historical modular symplectic Lefschetz representations is incomplete.

## References
1. E. Ghorbani, G. B. Khosrovshahi, Ch. Maysoori, M. Mohammad-Noori, *Inclusion Matrices and Chains*, arXiv:0709.3144v1 (September 20, 2007), Corollary 3, https://arxiv.org/pdf/0709.3144.
2. R. M. Wilson, *A Diagonal Form for the Incidence Matrices of t-Subsets vs. k-Subsets*, European Journal of Combinatorics 11 (1990), 609–615, DOI 10.1016/S0195-6698(13)80046-7.
3. A. R. Kustin, A. Vraciu, *The Weak Lefschetz Property for monomial complete intersections in positive characteristic*, arXiv:1110.2822v1 (October 13, 2011), https://arxiv.org/abs/1110.2822.
4. F. Knop, mathematical explanation of finite-field alternating-form rank multiplicities, MathOverflow question 238834, answer June 7, 2016, https://mathoverflow.net/questions/238834/number-of-skew-symmetric-matrices-of-fixed-rank.
