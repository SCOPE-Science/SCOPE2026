# Semisimple Alexander-quandle retractions: a transformation–affine factorization and exact image ranks

## Finding
For a finite Alexander quandle with a semisimple invertible linear operator over a prime field, the **full endomorphism monoid** splits into a full transformation monoid on the component labels and an affine centralizer monoid on the connected factor. This gives an exact classification of all retraction images, their individual multiplicities, and every image cardinality.

Let \(p\) be prime, let \(V\) be a finite-dimensional \(\mathbb F_p\)-vector space, and let \(T\in\operatorname{GL}_{\mathbb F_p}(V)\) be semisimple. Put
\[
U=\ker(1-T),\qquad W=\operatorname{im}(1-T),\qquad Q=|U|.
\]
Then \(V=U\oplus W\) and \(1-T\) is invertible on \(W\). Equip \(V\) with the quandle operation \(x*y=Tx+(1-T)y\). Every quandle endomorphism is uniquely of the form
\[
F(u,w)=(\phi(u),Aw+b),
\]
where \(\phi:U\to U\) is *any set map*, \(A\) is an \(\mathbb F_p\)-linear endomorphism of \(W\) commuting with \(T\), and \(b\in W\). Composition is componentwise; on affine factors \((A,b)\circ(B,c)=(AB,Ac+b)\). Thus
\[
\operatorname{End}(V,*)\cong\mathcal T_Q\times\operatorname{AffEnd}_T(W).
\]
In particular, \(F\) is a retraction (\(F^2=F\)) exactly when \(\phi^2=\phi\), \(A^2=A\), and \(Ab=0\).

Write the characteristic-module decomposition of \(W\) as
\[
W\cong\bigoplus_{i=1}^t\mathbb F_{q_i}^{d_i},\qquad q_i=p^{e_i},
\]
where the summands correspond to the pairwise distinct irreducible factors of the minimal polynomial of \(T|_W\), with \(e_i\) their degrees and \(d_i\ge1\) their multiplicities. On each summand, the centralizer algebra is \(M_{d_i}(\mathbb F_{q_i})\). In this description the exact image-cardinality polynomial is
\[
\boxed{R_{V,T}(z)=\sum_{k=1}^{Q}\binom Qk k^{Q-k}
\sum_{0\le r_1\le d_1,\ldots,0\le r_t\le d_t}
\left(\prod_{i=1}^t {d_i\brack r_i}_{q_i}
q_i^{(r_i+1)(d_i-r_i)}\right)
z^{k p^{\sum_i e_i r_i}}.}
\]
Here \({d\brack r}_q=\prod_{j=0}^{r-1}(q^{d-j}-1)/(q^{r-j}-1)\) is the Gaussian binomial coefficient; all empty products are one.

Every image is exactly a set
\[
Y=K\times(c+S),\qquad\varnothing\ne K\subseteq U,
\]
where \(S\le W\) is \(T\)-stable and \(c+S\) is an affine coset. Conversely every such set is a retraction image. For a **specified** image with \(k=|K|\) and \(r_i=\dim_{\mathbb F_{q_i}}S_i\), the number of retractions onto it is
\[
\boxed{k^{Q-k}\prod_{i=1}^t q_i^{r_i(d_i-r_i)}.}
\]
The complete number of distinct images is
\[
\boxed{(2^Q-1)\prod_{i=1}^t\left(\sum_{r=0}^{d_i}{d_i\brack r}_{q_i}q_i^{d_i-r}\right).}
\]
The attainable cardinalities are exactly \(k p^{\sum_i e_i r_i}\), with \(1\le k\le Q\) and \(0\le r_i\le d_i\). There are \(Q|W|\) constant retractions, and the identity is the sole full-cardinality retraction. If \(\dim U\ge1\), the **largest proper** image has cardinality \((Q-1)|W|\); exactly \(Q(Q-1)\) retractions have this cardinality.

## Assumptions and scope
An Alexander quandle is a set with the operation \(x*y=Tx+(1-T)y\) for a group automorphism \(T\). Here the underlying group is the additive group of a finite \(\mathbb F_p\)-space. The hypothesis *semisimple* means that the minimal polynomial of \(T\) is squarefree over \(\mathbb F_p\), not that the operator must split into scalar eigenvalues over that prime field. Irreducible extension-field factors are explicitly included. All homomorphisms are set maps preserving the quandle operation, **not** assumed additive or linear; rank means the number of elements in the set image, not its vector-space dimension. Retractions are composition-idempotent quandle endomorphisms. Zero-dimensional summands and the one-element quandle are included.

## Proof
**1. Canonical component splitting.** Because \(T\) is semisimple, its \(1\)-eigenspace \(U\) has an invariant complementary sum \(W\) of the remaining primary components, and \(W=\operatorname{im}(1-T)\). For \(x=(u,w)\), \(y=(v,w')\),
\[
x*y=(u,Tw+(1-T)w').
\]
In particular, each fiber \(\{u\}\times W\) is an orbit under right translations: for given \(w,w_2\in W\), the equation \(Tw+(1-T)w'=w_2\) has a solution because \(1-T\) is invertible on \(W\).

**2. Homomorphism rigidity within fibers.** If \(F=(F_U,F_W)\) preserves the operation, the first component satisfies \(F_U(x*y)=F_U(x)\); the orbit property forces \(F_U(u,w)=\phi(u)\) with \(\phi\) depending only on \(u\). For fixed \(u\), let \(f_u(w)=F_W(u,w)\) and \(b_u=f_u(0)\). Put \(g_u=f_u-b_u\); it preserves the connected Alexander operation on \(W\) and satisfies \(g_u(0)=0\). With the second input equal to zero and then the first input equal to zero, respectively,
\[
g_u(Tx)=Tg_u(x),\qquad g_u((1-T)y)=(1-T)g_u(y).
\]
Given any \(a,b\in W\), take \(x=T^{-1}a\) and \(y=(1-T)^{-1}b\). The homomorphism law then gives \(g_u(a+b)=g_u(a)+g_u(b)\). Thus \(g_u=A_u\) is \(\mathbb F_p\)-linear and commutes with \(T\). Applying the homomorphism law to inputs in *different* fibers gives
\[
A_u(Tw+(1-T)w')+b_u
=T(A_uw+b_u)+(1-T)(A_vw'+b_v).
\]
Since every \(A_u\) commutes with \(T\), comparison of the variable \(w'\) gives \(A_u=A_v\); comparison of constants then gives \((1-T)(b_u-b_v)=0\), hence \(b_u=b_v\). This proves the unique normal form. Direct substitution proves sufficiency and the stated composition law.

**3. Retraction criterion.** Direct composition gives
\[
F^2(u,w)=(\phi^2(u),A^2w+Ab+b).
\]
It equals \(F(u,w)\) for every \((u,w)\) if and only if \(\phi^2=\phi\), \(A^2=A\), and \(Ab=0\). The first condition means \(\phi\) fixes every point of its nonempty image \(K\subseteq U\); with \(k=|K|\), the number of such \(\phi\) for a fixed \(K\) is \(k^{Q-k}\).

**4. Semisimple module classification and count.** Distinct irreducible \(\mathbb F_p[t]\)-summands of \(W\) admit no intertwining linear maps, and one block of degree \(e_i\) and multiplicity \(d_i\) has centralizer \(M_{d_i}(\mathbb F_{q_i})\). An idempotent \(A_i\) of rank \(r_i\) is uniquely a choice of image \(S_i\) and complement \(N_i\). There are \({d_i\brack r_i}_{q_i}\) choices of image and \(q_i^{r_i(d_i-r_i)}\) complements per fixed image. For each complement, \(b_i\in N_i=\ker A_i\) has \(q_i^{d_i-r_i}\) possibilities. This gives \({d_i\brack r_i}_{q_i}q_i^{(r_i+1)(d_i-r_i)}\) affine idempotents at the chosen rank, independently across blocks. Multiplication by the \(\binom Qk k^{Q-k}\) label idempotents proves the generating polynomial.

**5. Individual image multiplicities.** Since \(A\) is a module projection, \(S=\operatorname{im}A\) is a direct sum of invariant submodules. The affine part has image \(b+S\). Every affine coset \(c+S\) occurs: given a complementary invariant submodule \(N\), choose its unique representative \(b\) of \(c+S\). For a *fixed* coset and fixed \(S\), each module complement determines exactly one pair \((A,b)\), giving \(\prod_i q_i^{r_i(d_i-r_i)}\) choices. The unrelated label map contributes \(k^{Q-k}\). To count images, independently choose a nonempty \(K\), a stable submodule \(S\), and one of \(\prod_iq_i^{d_i-r_i}\) cosets. This yields the image-count formula and proves that all listed sizes occur.

**6. Boundary.** A constant map is a quandle endomorphism and a retraction; these are exactly the \(Q|W|\) rank-one maps. A full-cardinality idempotent is bijective, hence the identity. For \(Q\ge2\), any nonidentity map with \(k<Q\) has image at most \((Q-1)|W|\), equality only if \(k=Q-1\) and \(A=1_W\). If \(k=Q\) but \(A\ne1_W\), some irreducible factor has lost at least one dimension: its image has size at most \(Q|W|/q_i\). Because \(q_i\ge2\), this is strictly below \((Q-1)|W|\) for \(Q\ge3\); for \(Q=2\) the prime is \(2\) and there are no nonunit scalar irreducible factors over \(\mathbb F_2\), so \(q_i\ge4\), again strict. Therefore the maximum proper rank is \((Q-1)|W|\), achieved by choosing the omitted label and its image in the \(Q-1\) retained labels; there are \(Q(Q-1)\) such retractions. The argument also works when \(W=0\), with empty products interpreted as one.

## Verification
Run `python3 verify.py`. The checker **does not construct the normal form as its search space**: it forms the quandle multiplication table, assigns images of underlying points, propagates operation-preservation equalities, and branches exhaustively over all still-unassigned choices. It tests composition-idempotence directly for each resulting endomorphism. Seven full enumerations give:

- For the one-point quandle and for the trivial four-point quandle, the rank counts are respectively \(1\) and \(4z+24z^2+12z^3+z^4\).
- For \(p=3\), \(U=0\), and \(T=2\) on a one-space: \(3\) rank-one retractions and \(1\) rank-three retraction.
- For \(p=5\), \(U=0\), and \(T=2\) on a one-space: \(5\) rank-one retractions and \(1\) rank-five retraction.
- For \(p=3\), \(\dim U=1\), and \(T=2\) on a one-space: the polynomial is \(9z+18z^2+6z^3+6z^6+z^9\), with \(40\) retractions.
- For \(p=3\), \(U=0\), and \(T=2I\) on a two-space: the polynomial is \(9z+36z^3+z^9\); there are \(12\) affine-line images, each admitting exactly three retractions.
- For \(p=2\), \(\dim U=1\), and \(T\) with irreducible polynomial \(t^2+t+1\) on a two-space: the polynomial is \(8z+4z^2+2z^4+z^8\).

The same checker independently compares the **multiplicity distribution of specified images** against the formula. All checks return `ALL_EXACT_CHECKS_PASSED`. These finite enumerations are ancillary; the six proof steps establish the theorem in arbitrary finite dimension.

## Relationship to prior work
Iijima and Murao (2017) establish connected-component decompositions of Alexander quandles, giving the orbit-theoretic starting point. Higashitani and Kurihara (2022) characterize generalized Alexander quandles and their *isomorphism* classes using the underlying groups. Higashitani, Kamada, Kosaka, and Kurihara (2024) extend this isomorphism classification. Singh (2023) studies residual finiteness of quandle endomorphism monoids. None of these statements, as inspected, computes the **noninvertible** endomorphism monoid together with all retraction images and individual multiplicities for semisimple prime-field Alexander quandles. The Gaussian submodule counts and idempotent full-transformation-map counts are classical ingredients and are not themselves claimed as discoveries. The new assertion is the uniform factorization across arbitrarily many connected components and all extension-field simple blocks, followed by the full image-refined census.

## Limitations
The theorem requires a semisimple invertible operator over the **prime field** \(\mathbb F_p\), treating the underlying space as an additive elementary-abelian group. If an operator over an extension field is considered, its quandle homomorphisms are generally only prime-field linear on connected components, and the irreducible factors must accordingly be computed over the prime subfield. Nonsplit Jordan blocks are excluded. The cited prior work does not prove that this statement has never appeared under alternate terminology; finite enumeration alone cannot certify the arbitrary-dimension theorem.

## References
1. A. Higashitani and H. Kurihara, *Generalized Alexander quandles of finite groups and their characterizations*, arXiv:2210.16763v1 (2022-10-30), https://arxiv.org/abs/2210.16763.
2. Y. Iijima and T. Murao, *On connected component decompositions of quandles*, arXiv:1704.07689v1 (2017-04-25), https://arxiv.org/html/1704.07689v1.
3. A. Higashitani, S. Kamada, J. Kosaka, and H. Kurihara, *Classification of generalized Alexander quandles*, arXiv:2406.01074v1 (2024-06-03), https://arxiv.org/html/2406.01074v1.
4. M. Singh, *Endomorphism monoid and automorphism group of residually finite and profinite quandles*, arXiv:2311.03708v1 (2023-11-07), https://arxiv.org/abs/2311.03708.
5. S. Nelson, *Classification of finite Alexander quandles*, arXiv:math/0202281v1 (2002-02-26), https://arxiv.org/abs/math/0202281.
