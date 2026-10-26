# Graded homology and Jordan frequency spectra of quadratic multiplication in characteristic two

## Finding
Let \(n\ge2\), let \(q=2^e\) be any even prime power, and put \(A=\mathbb F_q[x_1,\ldots,x_n]/(x_1^2,\ldots,x_n^2)\), with its total-degree grading. Every homogeneous quadratic \(Q=\sum_{i<j}a_{ij}x_ix_j\) has square zero. Accordingly, \(d_Q(a)=Qa\) defines a cochain complex with differential of degree two. The alternating coefficient matrix \(B_Q=(b_{ij})\), where \(b_{ii}=0\) and \(b_{ij}=b_{ji}=a_{ij}\) for \(i<j\), has even rank \(2r\), \(0\le r\le\lfloor n/2\rfloor\).

**Graded homology and graded Jordan spectrum.** Define \(H_i(Q)=\ker(d_Q:A_i\to A_{i+2})/\operatorname{im}(d_Q:A_{i-2}\to A_i)\), with out-of-range components zero. Their Hilbert polynomial is
\[
H_Q(t)=\sum_{i=0}^n\dim H_i(Q)t^i=(2t)^r(1+t)^{n-2r}.
\]
The number of length-one Jordan strings in degree \(i\) is \(\dim H_i(Q)\). The number of length-two strings beginning in degree \(i\) is the coefficient of \(t^i\) in
\[
P_{2,Q}(t)=\frac{(1+t)^n-(2t)^r(1+t)^{n-2r}}{1+t^2}.
\]
This quotient is a polynomial with nonnegative integral coefficients. In particular, the number of length-two blocks is \(2^{n-1}-2^{n-r-1}\) for \(r\ge1\), and zero for \(r=0\); the number of length-one blocks is \(2^{n-r}\). The resulting ungraded Jordan form is entirely determined by \(r\). The Hilbert polynomial also determines \(r\) as its smallest nonzero degree.

**Multiplicative strengthening.** When \(Q\ne0\), the quotient \(\operatorname{Ann}_A(Q)/(Q)\), whose underlying vector space is the homology, is a square-zero (generally nonunital) algebra: every product of two classes vanishes. When \(Q=0\), its algebra structure is \(A\) itself.

**Exact finite-field frequency.** Among the \(q^{\binom n2}\) labeled quadratics, the number with alternating rank \(2r\), equivalently with the specified graded homology and Jordan spectra, is
\[
N_{n,r}(q)=\binom{n}{2r}_q q^{r(r-1)}\prod_{j=1}^{r}(q^{2j-1}-1),\qquad 0\le r\le\lfloor n/2\rfloor.
\]
The Gaussian coefficient counts radical subspaces, the product counts nonsingular alternating forms on their quotients, and the empty product equals one. Every stratum is nonempty and their counts sum to \(q^{\binom n2}\). For \(n=4\), the frequencies for \(r=0,1,2\) are \((1,35,28)\) over \(\mathbb F_2\) and \((1,1071,3024)\) over \(\mathbb F_4\).

## Assumptions and scope
The coefficient field must have characteristic two, but need not be a prime field. The parameter \(n\) is any integer at least two. The set being counted is the entire vector space of homogeneous degree-two elements of the specified truncated polynomial algebra, not the full augmentation ideal. The alternating matrix is formed in the displayed coordinate basis; its rank is invariant under invertible linear changes of variables. The quotient \(\operatorname{Ann}_A(Q)/(Q)\) is an algebra because \(Q^2=0\), so \((Q)\subseteq\operatorname{Ann}_A(Q)\) and \((Q)\) is an ideal inside that annihilator.

## Proof
**1. Square-zero property and alternating normal form.** In characteristic two, \(Q^2=\sum_{i<j}a_{ij}^2x_i^2x_j^2=0\). Any invertible linear substitution of the degree-one variables extends to an automorphism of \(A\), because every linear form also squares to zero. The usual elementary alternating-form reduction, valid over characteristic-two fields, converts any rank-\(2r\) quadratic to
\[
Q=p_1+\cdots+p_r,\qquad p_j=u_jv_j,
\]
where \(u_j,v_j\) are paired independent variables, with \(n-2r\) unused variables \(z_k\). Thus it suffices to compute for this normal form.

**2. Two-variable complex.** The exterior-style squarefree algebra on \(u,v\) has graded basis \(1,u,v,uv\). Multiplication by \(uv\) maps \(1\) isomorphically to \(uv\) and kills \(u,v,uv\). This complex splits into an acyclic two-term subcomplex \(\langle1\rangle\to\langle uv\rangle\) and two one-term complexes represented by \(u\) and \(v\), both in degree one. The cohomology has Hilbert polynomial \(2t\). Each unused variable contributes a zero-differential two-dimensional factor with Hilbert polynomial \(1+t\).

**3. Tensor decomposition.** As a graded vector space, \(A\) is the tensor product of its \(r\) paired factors and \(n-2r\) unused factors. Multiplication by \(Q\) is the sum of the pairwise multiplication differentials. In characteristic two their cross terms cancel and the tensor differential squares to zero. An acyclic two-term factor tensored with another finite-dimensional complex remains contractible: contracting \(\langle1\rangle\to\langle uv\rangle\) gives an explicit contracting homotopy, and characteristic two cancels the cross terms. Removing these summands leaves exactly one choice \(u_j\) or \(v_j\) from each pair, multiplied by arbitrary unused-variable monomials. These are linearly independent homology representatives, giving \(H_Q(t)=(2t)^r(1+t)^{n-2r}\).

**4. Graded Jordan chains and annihilator products.** Since \(d_Q^2=0\), choose a graded basis of two-step chains and homology classes. A length-two chain contributes degrees \(i\) and \(i+2\); homology classes contribute length-one chains. Thus \((1+t)^n=(1+t^2)P_{2,Q}(t)+H_Q(t)\), proving the complete graded Jordan formulas. Evaluating at \(t=1\) gives \(\sum_i\operatorname{rank}(d_Q|_{A_i})=(2^n-2^{n-r})/2\), and hence the ungraded Jordan form.

For \(r\ge1\), choose the homology representatives described in step 3. A product of two such monomials vanishes if they chose the same variable in any pair. Otherwise, their product contains \(p_1p_2\cdots p_r\) multiplied by a monomial in unused variables. But \(Qp_2\cdots p_r=p_1p_2\cdots p_r\), because every \(p_j^2=0\); hence the product is in the boundary ideal \((Q)\). Bilinearity proves that all products of homology classes vanish.

**5. Counting the strata.** The radical of an alternating matrix of rank \(2r\) has dimension \(n-2r\). Choosing that radical gives \(\binom{n}{2r}_q\) choices. Once it is fixed, alternating forms with exactly that radical correspond bijectively to nondegenerate alternating forms on the \(2r\)-dimensional quotient. Their number is \(|\operatorname{GL}_{2r}(q)|/|\operatorname{Sp}_{2r}(q)|=q^{r(r-1)}\prod_{j=1}^r(q^{2j-1}-1)\). Multiplying proves the frequency formula. Rank is unique for each quadratic, so these disjoint strata exhaust all \(q^{\binom n2}\) quadratics. Because the smallest nonzero homology degree is \(r\), none of the stated graded types merge.

## Verification
A standalone exact finite-field checker constructs the alternating matrices and all graded multiplication maps from independent squarefree-monomial bases. It exhausts all homogeneous quadratics for \((q,n)=(2,2),(2,3),(2,4),(2,5),(4,2),(4,3),(4,4)\) and checks their graded homology, total Jordan ranks, and every rank-stratum multiplicity. It additionally checks 48 deterministic coefficient tuples in each of the four larger configurations \((2,6),(4,5),(4,6),(2,7)\), for 5,454 checked inputs in total. It performs elimination over \(\mathbb F_4\) using the irreducible polynomial \(t^2+t+1\), not integer reduction modulo four. A finite checker does not prove the all-dimensional statement; the algebraic argument above does.

## Relationship to prior work
Classical alternating-form normal forms and finite-field symplectic group orders provide the matrix strata, not a new rank-enumeration technique. Fulman and Goldstein, *Stein's method and the rank distribution of random matrices over finite fields* (arXiv:1211.0504, 2012), explicitly study the alternating-matrix rank distribution. David Cook II, *The Lefschetz properties of monomial complete intersections in positive characteristic* (arXiv:1111.4979, 2011), treats the characteristic-two monomial complete-intersection setting, principally through Lefschetz properties. The present assertion concerns the full graded homology and exact Jordan starting-degree frequencies for multiplication by every quadratic, plus the multiplication law on its annihilator quotient, across all numbers of variables. A general homological or symplectic reduction might make these formulas implicit in older theory; they are not claimed as discoveries of the standard normal-form or form-counting ingredients.

## Limitations
The theorem is restricted to homogeneous degree-two multiplication over fields of characteristic two. It does not classify arbitrary augmentation-ideal elements or odd-characteristic squarefree exterior multiplication. The independent literature comparison is not exhaustive, and the graded tensor argument is based on classical underlying tools; priority for the assembled statement is not settled by absence of a matching search result. No independent mathematical audit has been performed.

## References
1. David Cook II, *The Lefschetz properties of monomial complete intersections in positive characteristic*, arXiv:1111.4979v1, publicly submitted 21 November 2011, https://arxiv.org/abs/1111.4979 .
2. Jason Fulman and Larry Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, arXiv:1211.0504v1, publicly submitted 2 November 2012, https://arxiv.org/abs/1211.0504 .
