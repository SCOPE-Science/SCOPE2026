# Modular graded Jordan spectra of bivector multiplication in exterior algebras

## Finding

Let \(q\) be any odd prime power of characteristic \(p\), let \(n\geq 1\), and let \(V\) be an \(n\)-dimensional vector space over \(\mathbb F_q\). For \(\omega\in\bigwedge^2 V\), write \(L_\omega\) for multiplication by \(\omega\) on the \(2^n\)-dimensional exterior algebra \(E=\bigwedge V\), and let \(2r\) be the alternating rank of its coefficient matrix, \(0\leq r\leq\lfloor n/2\rfloor\).

The following finite binomial expressions determine, for **every** \(n,p,r\), all Jordan-string lengths **and their starting exterior degrees**. Put \(\binom ab=0\) when \(b<0\) or \(b>a\). For \(0\leq k<p\), \(0\leq j\leq m-k\), set

\[
 t=\min\{j,m-j-k\},\qquad
 \rho_p(m,j,k)=\sum_{i=0}^{t}
 \left(\binom mi-\binom m{i-1}\right)
 \mathbf 1_{\,p\nmid\binom{t+k-i}{t-i}}.
\]

For \(k\geq p\), or \(m<k\), the relevant rank is zero. Define the graded rank polynomials for \(0\leq k<p\) by

\[
 \mathcal R_k(T)=(1+T)^{n-2r}
 \sum_{m=0}^{r}\binom rm(2T)^{r-m}
 \sum_{j=0}^{m-k}\rho_p(m,j,k)T^{2j},
\]

where an inner sum with upper bound below zero is empty; put \(\mathcal R_p(T)=\mathcal R_{p+1}(T)=0\). Then \([T^d]\mathcal R_k(T)\) is exactly the rank of

\[
 L_\omega^k:\bigwedge^d V\longrightarrow\bigwedge^{d+2k}V.
\]

For each \(1\leq\ell\leq p\), the **Jordan-string polynomial**

\[
 \boxed{\mathcal B_{\ell}(T)=\mathcal R_{\ell-1}(T)
 -(1+T^2)\mathcal R_{\ell}(T)+T^2\mathcal R_{\ell+1}(T)}
\]

has nonnegative integer coefficients: \([T^d]\mathcal B_\ell(T)\) is the number of Jordan blocks of length \(\ell\) starting in exterior degree \(d\). In particular, \(\mathcal B_\ell(1)\) is the ordinary Jordan-block multiplicity. Every \(\omega\) of alternating rank \(2r\) has this identical graded spectrum. Its nilpotency index is exactly \(\min\{p,r+1\}\) when \(r\geq1\), and one for \(r=0\).

The spectrum frequencies are also exact. Define the Gaussian coefficient

\[
 {n\brack s}_q=\prod_{a=0}^{s-1}\frac{q^{n-a}-1}{q^{s-a}-1}.
\]

For every \(r\) in the permitted range, precisely

\[
 \boxed{\mathcal N_{n,r}(q)={n\brack 2r}_q\,q^{r(r-1)}
 \prod_{a=1}^{r}(q^{2a-1}-1)}
\]

bivectors produce the corresponding graded Jordan spectrum. These numbers partition all \(q^{\binom n2}\) bivectors. The displayed expressions count **forms of a given rank**, not necessarily distinct spectra if two ranks happen to share one; where necessary, identical spectra are combined by adding their frequencies.

A visible modular boundary occurs already in dimension eight. A nondegenerate bivector has ordinary Jordan partition \((3^{45},2^{40},1^{41})\) in characteristic three, but \((5,4^8,3^{27},2^{48},1^{42})\) in characteristic five or any characteristic at least five. In characteristic three, the length-three blocks begin in degrees \(0,1,2,3,4\) with respective multiplicities \(1,8,27,8,1\); the length-two blocks all begin in degree three, and the length-one blocks in degree four.

## Assumptions and scope

All fields have odd positive characteristic; the extension degree in \(q=p^e\) is arbitrary. The operator is **left exterior multiplication by a homogeneous bivector**, not the induced action of a linear endomorphism on an exterior power. Exterior generators anticommute, and each squares to zero. The grading is exterior degree; multiplication by \(\omega\) increases degree by two. A string starting in degree \(d\) and of length \(\ell\) has degrees \(d,d+2,\ldots,d+2(\ell-1)\). No genericity of \(\omega\) is assumed.

## Proof

**1. Alternating normal form.** Elementary congruence reduction of an alternating matrix over an odd-characteristic field gives a basis \(a_1,b_1,\ldots,a_r,b_r,c_1,\ldots,c_{n-2r}\) in which

\[
 \omega=a_1\wedge b_1+\cdots+a_r\wedge b_r.
\]

Exterior multiplication is equivariant for invertible linear changes of basis, so its graded Jordan spectrum depends only on \(r\), not on coefficients or on the particular finite field of characteristic \(p\).

**2. Direct-sum decomposition.** For each two-dimensional factor with basis \(a_i,b_i\), its exterior algebra, under multiplication by \(a_i\wedge b_i\), is the direct sum of a length-two string \(1\mapsto a_i\wedge b_i\) and two length-one strings \(a_i\) and \(b_i\). In the graded tensor product, these even-degree multipliers commute (there are no sign changes between them). Choose \(m\) of the \(r\) factors to use their length-two summands; each of the other \(r-m\) factors contributes either of two degree-one fixed vectors. Thus the resulting summands, with multiplicity \(\binom rm2^{r-m}\), are the squarefree complete intersections

\[
 C_m=\mathbb F_q[z_1,\ldots,z_m]/(z_1^2,\ldots,z_m^2),
 \quad \deg z_i=2,
\]

shifted up by exterior degree \(r-m\), on which \(L_\omega\) becomes multiplication by \(z_1+\cdots+z_m\). The remaining \(n-2r\) exterior generators contribute the graded dimension factor \((1+T)^{n-2r}\). This decomposition is valid over every odd-characteristic field.

**3. Exact modular ranks.** Fix \(k<p\) and restrict multiplication by \((z_1+\cdots+z_m)^k\) from degree \(2j\) to \(2(j+k)\) in \(C_m\). In the squarefree monomial bases its matrix is \(k!\) times the transpose of the \(j\)-subset versus \((j+k)\)-subset inclusion matrix on an \(m\)-element set. The scalar \(k!\) is invertible for \(k<p\). When \(j\leq m-j-k\), the integral diagonal-form theorem for inclusion matrices [1, Corollary 3] applies directly, with \(t=j\) and larger set size \(j+k\). When \(j>m-j-k\), complement all subsets and transpose; the corresponding inclusion matrix has lower set size \(t=m-j-k\), larger set size \(t+k\), and satisfies the same theorem's range condition \(t+k\leq m-t\). In both cases the diagonal entries are \(\binom{t+k-i}{t-i}\) with multiplicities \(\binom mi-\binom m{i-1}\). Reduction modulo \(p\) proves exactly the formula for \(\rho_p(m,j,k)\).

For \(k\geq p\), the operator vanishes: the summands \(z_i\) commute and have square zero, so \((\sum_i z_i)^p=\sum_i z_i^p=0\) in characteristic \(p\). Summing the degree shifts and multiplicities from step 2 gives the claimed \(\mathcal R_k(T)\), including \(\mathcal R_0(T)=(1+T)^n\).

**4. Recovering individual strings.** Graded nilpotent endomorphisms of homogeneous degree two admit a homogeneous Jordan-string basis, by lifting homogeneous generators through the successive images and kernels (or equivalently by elementary graded module decomposition over \(\mathbb F_q[t]\), \(\deg t=2\)). A length-\(L\) string starting in degree \(d\) contributes

\[
 T^d(1+T^2+\cdots+T^{2(L-k-1)})
\]

to \(\mathcal R_k(T)\) for \(0\leq k<L\), and zero otherwise. Substituting this contribution into the displayed combination for \(\mathcal B_\ell\) makes it cancel for every \(\ell\ne L\), and leaves precisely \(T^d\) for \(\ell=L\). Thus every coefficient of \(\mathcal B_\ell\) counts the asserted graded strings and is nonnegative.

The nilpotency index is at most \(p\) by step 3. In the normal form, the power \(\omega^k\) applied to \(1\) is \(k!\) times the sum of distinct products of \(k\) chosen pair-bivectors, so it is nonzero for \(0\leq k<\min\{p,r+1\}\). This proves the sharp index.

**5. Frequencies.** An alternating matrix of rank \(2r\) has radical of codimension \(2r\), chosen in \({n\brack 2r}_q\) ways. On the resulting \(2r\)-dimensional quotient, nondegenerate alternating forms form one \(\mathrm{GL}_{2r}(\mathbb F_q)\)-orbit with symplectic stabilizer. The orbit size is

\[
 \frac{|\mathrm{GL}_{2r}(\mathbb F_q)|}{|\mathrm{Sp}_{2r}(\mathbb F_q)|}
 =q^{r(r-1)}\prod_{a=1}^{r}(q^{2a-1}-1).
\]

Multiplying proves \(\mathcal N_{n,r}(q)\). The disjoint alternating-rank strata exhaust \(\bigwedge^2 V\), whose size is \(q^{\binom n2}\), proving the total. This completes the theorem.

## Verification

Run `python3 verify_exterior_jordan.py` (standard library only). The program independently constructs matrices of exterior multiplication by a canonical bivector on every exterior monomial, computes ranks of all powers over \(\mathbb F_3,\mathbb F_5,\mathbb F_7\), and compares full degree-by-degree ranks and inferred strings with the formulas for all \(2\leq n\leq8\) and \(0\leq r\leq\lfloor n/2\rfloor\): 69 cases. It separately enumerates all \(3^6=729\) and \(5^6=15625\) alternating four-by-four matrices and checks the complete rank distribution. Its terminal marker is `VERIFY_OK_EXTERIOR_QUADRATIC_JORDAN 69 matrix-power cases`.

These finite checks are not a proof for arbitrary \(n\) or extension degree; the all-parameter proof is in the preceding section and invokes the published integral inclusion-matrix theorem explicitly. The verifier uses only prime fields and does not enumerate all bivectors in higher dimension.

## Relationship to prior work

Ghorbani, Khosrovshahi, Maysoori and Mohammad-Noori [1] prove the integral diagonal form of Boolean inclusion matrices (recovering Wilson's earlier theorem). That critical ingredient is **existing work**; neither its diagonal entries nor its proof are claimed new. The present result transfers this ingredient to modular bivector multiplication by a graded exterior-tensor decomposition and recovers the **complete degree-resolved Jordan distributions with exact finite-field stratum frequencies**. The inclusion-matrix theorem alone does not identify the exterior modules or their degree-by-degree Jordan strings. The classical alternating-matrix rank counts themselves are known and recorded in Lewis and collaborators [4, Proposition 3.8]; their contribution must not be mistaken for a new enumeration of alternating forms.

Cook [2] treats weak and strong Lefschetz properties of **commutative polynomial-ring** monomial complete intersections, primarily under linear multiplication. Those properties do not specify the complete graded Jordan spectrum of exterior multiplication by an arbitrary rank bivector. Altafi, Iarrobino and Macias Marques [3] review graded Jordan type and degree type for commutative Artinian algebras, but do not supply the displayed modular exterior-bivector frequency law.

The characteristic-zero symplectic Lefschetz decomposition supplies the large-characteristic benchmark, but its generic maximal-rank information does not yield the characteristic-three collapse in dimension eight. The present formulas expose that modular behavior and refine it by starting degree. Neither the alternating-form orbit count nor the inclusion-matrix rank theorem is claimed original; the proposed new contribution is the explicit characteristic-dependent graded Jordan spectrum, paired with the already-known form counts to yield a full frequency law.

## Limitations

The result requires odd characteristic; characteristic two is not included. It concerns degree-two exterior elements only and does not classify arbitrary even-degree elements or operators induced on \(\bigwedge^d V\) by an endomorphism of \(V\). The claimed novelty is the explicit assembled graded Jordan/frequency formula and its modular boundary, not the classical ingredients. Older modular symplectic representation literature may contain an equivalent transfer under different terminology; exhaustive priority verification and independent mathematical validation have not been performed.

## References

[1] E. Ghorbani, G. B. Khosrovshahi, Ch. Maysoori, M. Mohammad-Noori, *Inclusion Matrices and Chains*, arXiv:0709.3144v1 (first public 2007-09-20), Corollary 3 and its proof, https://arxiv.org/abs/0709.3144.

[2] David Cook II, *The Lefschetz properties of monomial complete intersections in positive characteristic*, arXiv:1111.4979v1 (2011-11-21), https://arxiv.org/abs/1111.4979.

[3] Nasrin Altafi, Anthony Iarrobino, Pedro Macias Marques, *Jordan type of an Artinian algebra, a survey*, arXiv:2307.00957v1 (2023-07-03), https://arxiv.org/abs/2307.00957.

[4] Joel Brewster Lewis and collaborators, *Matrices with restricted entries and q-analogues of permutations*, arXiv:1011.4539v1 (2010), Proposition 3.8 on skew-symmetric rank enumeration, https://arxiv.org/abs/1011.4539.
