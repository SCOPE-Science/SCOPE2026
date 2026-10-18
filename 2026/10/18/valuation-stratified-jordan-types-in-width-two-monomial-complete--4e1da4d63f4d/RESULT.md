# Valuation-stratified Jordan types in width-two monomial complete intersections

## Finding

For every field \(k\) and integer \(m\ge2\), set
\[
A_m=k[x,y]/(x^2,y^m),\qquad R_m=k[y]/(y^m).
\]
The radical \(\mathfrak m=(x,y)\) has dimension \(2m-1\). Write every \(a\in\mathfrak m\) uniquely as \(a=f(y)+xg(y)\) with \(f\in yR_m\) and \(g\in R_m\). Define the truncated valuation \(v_y(0)=m\) and \(v_y(h)=\min\{i:[y^i]h\ne0\}\) for nonzero \(h\in R_m\). Put \(\alpha=v_y(f)\in\{1,\ldots,m\}\) and \(\beta=v_y(g)\in\{0,\ldots,m\}\).

Let \(L_a:A_m\to A_m\) denote multiplication by \(a\), let \(r_t=\operatorname{rank}_k(L_a^t)\), and write \([u]_+=\max(u,0)\). The **complete power-rank profile**, for every integer \(t\ge1\), is
\[
\boxed{r_t=\begin{cases}
2[m-t\alpha]_+,&t\cdot 1_k=0\ \text{or}\ \beta\ge\alpha,\\[2pt]
[m-(t-1)\alpha-\beta]_++[m-(t+1)\alpha+\beta]_+,&t\cdot1_k\ne0\ \text{and}\ \beta<\alpha.
\end{cases}}
\tag{1}
\]
For the trivial power, \(r_0=2m\); for all \(t\ge m+1\), \(r_t=0\). Thus every possible Jordan type of \(L_a\) is explicitly determined by \((\alpha,\beta)\) and the characteristic. More precisely, the number of blocks of length exactly \(j\), for \(1\le j\le m+1\), is
\[
\boxed{b_j=r_{j-1}-2r_j+r_{j+1}.}\tag{2}
\]

For every finite field \(k=\mathbb F_q\) of characteristic \(p\), define
\[
w_m(v;q)=\begin{cases}(q-1)q^{m-v-1},&0\le v<m,\\1,&v=m.\end{cases}
\]
For **every** partition \(\lambda\vdash2m\), the exact number \(N_{m,q}(\lambda)\) of radical elements giving this Jordan type is
\[
\boxed{N_{m,q}(\lambda)=\sum_{\alpha=1}^m\sum_{\beta=0}^m w_m(\alpha;q)w_m(\beta;q)\,\mathbf1\bigl[(b_j(\alpha,\beta))_{j=1}^{m+1}=(b_j(\lambda))_{j=1}^{m+1}\bigr].}\tag{3}
\]
In particular, the formula is an explicit \(m(m+1)\)-term finite sum with no unresolved system of equations or matrix search. Repeated Jordan types arising from different valuation pairs are added rather than counted separately. The resulting counts sum to \(q^{2m-1}\), the cardinality of the radical.

The **sharp maximal nilpotency index** of multiplication by a radical element is
\[
\boxed{\max_{a\in\mathfrak m}\operatorname{nilind}(L_a)=\begin{cases}m+1,&m\cdot1_k\ne0,\\m,&m\cdot1_k=0.\end{cases}}\tag{4}
\]
Thus even the top possible Jordan-block size changes at the primes dividing \(m\).

## Assumptions and scope

There is no algebraic-closure or infinitude assumption on \(k\). Equation (1) and the block reconstruction (2) work in characteristic zero and in every positive characteristic. Equation (3) requires the finite-field cardinality \(q\), and works for all prime powers. All elements are **labeled elements** of the radical, not isomorphism or automorphism orbits. Partitions list all Jordan block sizes, including size-one blocks. An element with nonzero scalar term is excluded, because its multiplication operator is invertible rather than nilpotent.

## Proof

**1. A free rank-two module.** Identify \(A_m=R_m\oplus xR_m\), using the ordered \(R_m\)-basis \((1,x)\). Because \(x^2=0\) and the algebra is commutative, for each integer \(t\ge1\) the binomial identity gives
\[
a^t=f^t+t xf^{t-1}g,
\qquad
L_{a^t}\ \widehat{=}\
\begin{pmatrix}f^t&0\\tf^{t-1}g&f^t\end{pmatrix}\quad\text{over }R_m.\tag{5}
\]
This identity remains valid when \(f\) or \(g\) vanishes, and when the characteristic annihilates \(t\).

**2. Smith exponents before reduction.** Work over the discrete valuation ring \(k[[y]]\) and choose arbitrary power-series lifts \(f=y^\alpha u\), \(g=y^\beta v\), where \(u,v\) are units if the corresponding element is nonzero. For a zero element one may choose its lift to be \(y^m\). This does not change matrix (5) modulo \(y^m\). When \(t\cdot1_k=0\), the matrix is diagonal with both Smith exponents \(t\alpha\). When \(t\cdot1_k\ne0\), the valuation of the greatest common divisor of its entries is
\[
d_1=\min(t\alpha,(t-1)\alpha+\beta),
\]
and its determinant has valuation \(2t\alpha\); hence the second Smith exponent is \(d_2=2t\alpha-d_1\). Equivalently,
\[
(d_1,d_2)=\begin{cases}(t\alpha,t\alpha),&\beta\ge\alpha,\\((t-1)\alpha+\beta,(t+1)\alpha-\beta),&\beta<\alpha.\end{cases}\tag{6}
\]
For lifts representing zero elements, (6) remains correct as a statement **after reduction modulo \(y^m\)**, because different lifts differ by multiples of \(y^m\) and yield the same matrix. We only use the truncated Smith exponents \(\min(d_i,m)\). The vanishing of \(t\) in the field is the sole extra characteristic dependence.

**3. Ranks and Jordan blocks.** Multiplication by \(y^d\) on \(R_m\) has \(k\)-rank \([m-d]_+\), for each nonnegative integer \(d\). Applying this to the two Smith factors gives (1), including all zero-lift boundary cases. If a nilpotent operator has Jordan blocks of lengths \(\lambda_i\), then \(r_t=\sum_i\max(\lambda_i-t,0)\). Its second finite difference gives (2). Since \(a^{m+1}=0\), formulas for \(j\le m+1\) are exhaustive.

**4. Exact finite-field fibers.** An element of \(R_m\) has valuation \(v<m\) in exactly \((q-1)q^{m-v-1}\) ways, and valuation \(m\) exactly once. The coefficients of \(f\) and \(g\) are independent, apart from the required missing constant coefficient in \(f\). Each ordered valuation pair therefore has \(w_m(\alpha;q)w_m(\beta;q)\) elements. Each such element has the partition given by (1)--(2). Summing precisely those whose partition equals \(\lambda\) proves (3). The total is \((\sum_{\alpha=1}^{m}w_m(\alpha;q))(\sum_{\beta=0}^{m}w_m(\beta;q))=q^{m-1}q^m\).

**5. Sharp index.** Because \(f\in yR_m\), \(f^m=0\), so \(a^m=m xf^{m-1}g\). When \(m\cdot1_k=0\) this vanishes for every \(a\). When \(m\cdot1_k\ne0\), \(a=x+y\) satisfies \(a^m=mxy^{m-1}\ne0\). Also \(a^{m+1}=0\) for every radical element. Finally \(y^{m-1}\ne0\), so \(a=y\) has nilpotency index \(m\) even in the exceptional characteristics. This proves (4).

## Verification

The standalone `verify_jordan.py` independently constructs multiplication matrices in the monomial basis, computes their powers directly, and applies finite-field Gaussian elimination. Its algorithm does not use the Smith formula to compute observed ranks; it compares them with (1), reconstructs partitions, and checks every coefficient of (3). Exhaustive prime-field checks cover \(q=2\) and \(2\le m\le7\); \(q=3\) and \(2\le m\le5\); \(q=5\) and \(2\le m\le3\); and \(q=7,m=2\). The number of checked radical elements in each configuration is \(q^{2m-1}\). Output ends with `VERIFY_OK_ALL_JORDAN_VALUATIONS`. The proof does not rely on these finite experiments, and the verification program does not test nonprime extension fields separately.

As a quick example at \(m=3\), the partition \((4,2)\) has multiplicity \((q-1)^2q^3\) when \(\operatorname{char}k\ne3\) and is absent in characteristic \(3\). The partition \((3,2,1)\) has multiplicity \((q-1)^2q^2\) when \(\operatorname{char}k\ne2\) and is absent in characteristic \(2\). These are distinct modular transitions.

## Relationship to prior work

The monomial complete-intersection Lefschetz theory of Cook II (2011, Sections 2, 4 and 7) classifies the existence of Lefschetz linear forms in relevant characteristics and includes the width-two strong-Lefschetz boundary. The monomial-complete-intersection results of Lundqvist--Nicklasson (2016, Sections 3 and 4, especially Remark 4.6) treat Lefschetz properties, including finite coefficient fields, but not the cardinality of every nonhomogeneous radical Jordan-type stratum. Iarrobino--Macias Marques--McDaniel (2018, Example 3.37) treats exactly the exponent pair (2,3) but explicitly displays only the three Jordan partitions from the linear-form directions \(x\), \(y\), and \(x+by\) for nonzero \(b\). It supplies neither the additional nonlinear radical types (for example \(xy\), of type \((2,2,1,1)\)) nor the full finite-field counts or the family of arbitrary \(m\). Its surrounding poset notation may be read more broadly, so this scope distinction is a residual interpretive risk. The height-two classification of Altafi--Iarrobino--Khatami (2018, Example 1.2 and Section 2) likewise explicitly concerns linear forms, and already records the three characteristic-zero linear-form types for the (2,3) member. The later Jordan-type survey by Altafi--Iarrobino--Khatami (2023) describes Jordan partitions, special Jordan types, and rank mechanisms more broadly. The present statement does not assert novelty of Smith normal form, monomial-CI strong Lefschetz theory, or the Jordan partition of \(x+y\); the studied assertion is the uniform two-valuation power-rank formula **and** its complete finite-field fiber enumeration for all radical elements and all \(m\).

Existing related element-multiplication censuses for \(k[x,y]/(x^3,y^3)\) and rank distributions of homogeneous quadratic elements in \(k[x,y]/(x^m,y^m)\) have different parameter domains. Neither gives the present mixed-length \((2,m)\) all-element distribution. The deduction uses standard Smith machinery, so a previously published equivalent specialization remains a genuine priority risk.

## Limitations

The enumeration is for the regular module of the specified monomial complete intersection, not arbitrary modules, other exponent pairs, or orbit classification. It does not describe scheme-theoretic closures or singularities of Jordan strata. The formula for each partition is a bounded valuation sum rather than a separately simplified polynomial for every partition. Independent mathematical audit has not been performed, and uniqueness in the entire literature is not established.

## References

1. D. Cook II, *The Lefschetz properties of monomial complete intersections in positive characteristic*, arXiv:1111.4979v1 (first posted 21 November 2011), especially Sections 2, 4 and 7.
2. S. Lundqvist and L. Nicklasson, *On the structure of monomial complete intersections in positive characteristic*, arXiv:1604.06820v1 (first posted 22 April 2016), especially Sections 3 and 4.
3. A. Iarrobino, P. Macias Marques and C. McDaniel, *Artinian algebras and Jordan type*, arXiv:1802.07383v1 (2018), especially Section 3.5, Example 3.37.
4. N. Altafi, A. Iarrobino and L. Khatami, *Complete intersection Jordan types in height two*, arXiv:1810.00716v1 (first posted 1 October 2018), especially Example 1.2 and Sections 1--2.
5. N. Altafi, A. Iarrobino and L. Khatami, *Jordan type of an Artinian algebra, a survey*, arXiv:2307.00957 (2023), including the introduction and Jordan-type examples.
