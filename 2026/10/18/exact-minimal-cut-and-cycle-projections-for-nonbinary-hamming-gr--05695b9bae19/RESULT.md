# Exact minimal cut and cycle projections for nonbinary Hamming graphs

## Finding

For every integer \(d\ge2\) and alphabet size \(q\ge3\), let \(G=H(d,q)=K_q^{\square d}\) be the unweighted Hamming graph. Choose any orientations of its edges; write \(D:\mathbb R^E\to\mathbb R^V\) for the vertex-edge incidence matrix, \(B=\operatorname{ran}D^{\mathsf T}\) for the cut space and \(Z=\ker D\) for the cycle space. Define the relative projection constant \(\lambda_p(Y)=\inf\{\|R\|_{\ell_p^E\to\ell_p^E}:R^2=R,\ \operatorname{ran}R=Y\}\) for \(1\le p\le\infty\).

The Euclidean orthogonal projections \(Q=D^{\mathsf T}(DD^{\mathsf T})^\dagger D\) onto \(B\) and \(P=I-Q\) onto \(Z\) minimize the projection norm *simultaneously for every* \(1\le p\le\infty\). The exact minima at both endpoints \(p=1\) and \(p=\infty\) are

\[
\lambda_1(B)=\lambda_\infty(B)=\frac{(d+1)(q-1)}q,
\qquad
\lambda_1(Z)=\lambda_\infty(Z)=1+\frac{(d+1)(q-1)}q-\frac{4(1-q^{-d})}{d(q-1)}.
\]

The same formulas extend to \(q=2\), which is a **previously established binary case** and is not included in the new claim. At \(p=2\) both minima are \(1\); no closed-form norms for other \(p\) are claimed.

## Assumptions and scope

All vector spaces and operator norms are over the real field; the ambient edge spaces have counting-measure \(\ell_p\) norms and do **not** use probability-normalized edge measure. All edges have unit length, and \(G\) is a finite simple graph. Its \(q^d\) vertices are words in \(\{0,\dots,q-1\}^d\); two vertices share an edge when they differ in exactly one coordinate. The Moore–Penrose inverse is taken relative to the ordinary Euclidean vertex inner product. The graph-automorphism group acts on oriented edge coordinates by signed permutations, isometrically for every \(p\). The orientation choice does not affect any asserted constant.

## Proof

**Minimality.** The orthogonal projections preserve the two subspaces and commute with all graph automorphisms. Theorem 43 of Dilworth–Kutzarova–Ostrovskii proves that on **every Hamming graph** the orthogonal cycle projection is the unique graph-automorphism-invariant projection onto the cycle space. If \(R\) is any projection onto \(Z\), averaging \(gRg^{-1}\) over the finite graph-automorphism group yields a projection onto \(Z\), still restricting to the identity on \(Z\), with norm at most \(\|R\|\) for any \(\ell_p\). By uniqueness the average equals \(P\); hence \(P\) minimizes for every \(p\). A projection onto \(B\) is treated analogously: the complement of any invariant projection onto \(B\) is invariant onto \(Z\), hence must be \(P\); therefore the averaged projection onto \(B\) is \(Q\), and \(Q\) minimizes for every \(p\).

**An exact cut column.** The graph is edge-transitive, so every column of \(Q\) has the same absolute \(\ell_1\) sum. Set \(r=d-1\). Orient the test edge from \((1,0,\ldots,0)\) toward \((0,0,\ldots,0)\), and let \(b\) be its signed vertex incidence vector. Factor the graph as \(K_q\square H(r,q)\). On \(K_q\) put \(h(0)=1\), \(h(1)=-1\), and \(h(a)=0\) otherwise; its Laplacian satisfies \(L_{K_q}h=qh\). Therefore the mean-zero solution of the vertex Poisson equation \(L_G\phi=b\) has the factorization \(\phi(a,z)=h(a)f(z)\), where

\[
f=(qI+L_{H(r,q)})^{-1}\delta_{\boldsymbol 0},
\qquad
f_k=\frac{1}{q^{r+1}}\int_0^1 (1+(q-1)u)^{r-k}(1-u)^k\,du,
\quad 0\le k\le r.
\]

Here \(f_k=f(z)\) when \(z\) has exactly \(k\) nonzero coordinates. This integral follows from \((qI+L)^{-1}=\int_0^\infty e^{-qt}e^{-tL}\,dt\) and the product heat kernel of \(K_q\), followed by \(u=e^{-qt}\). It is strictly positive and strictly decreasing in \(k\) because

\[
f_k-f_{k+1}=\frac{1}{q^r}\int_0^1 u(1+(q-1)u)^{r-1-k}(1-u)^k\,du>0.
\]

Since \((qI+L)f=\delta_{\boldsymbol0}\) and each row sum of \(L\) is zero, \(\sum_z f(z)=1/q\). The first-coordinate edge differences of \(\phi\) have total absolute sum \(2(q-1)\sum_z f(z)=2(q-1)/q\). The edges in the other \(r\) coordinates have total absolute sum

\[
2r(q-1)\sum_{k=0}^{r-1}\binom{r-1}{k}(q-1)^k(f_k-f_{k+1})
=\frac{r(q-1)}q.
\]

To evaluate the sum, substitute the integral and use

\[
(1+(q-1)u)+(q-1)(1-u)=q,
\qquad
\sum_{k=0}^{r-1}\binom{r-1}{k}(q-1)^k(f_k-f_{k+1})=\frac1{2q}.
\]

Because \(Qe=D^{\mathsf T}\phi\), these two edge families exhaust the column of \(Q\). Consequently

\[
\|Q\|_{1\to1}=\|Qe\|_1=\frac{(r+2)(q-1)}q=\frac{(d+1)(q-1)}q.
\]

**Cycle column and endpoints.** Edge transitivity makes the diagonal of \(Q\) constant. Its rank is \(|V|-1=q^d-1\), and \(|E|=dq^d(q-1)/2\); therefore

\[
Q_{ee}=\frac{\operatorname{tr}Q}{|E|}=\frac{2(1-q^{-d})}{d(q-1)}.
\]

As \(0\le Q_{ee}\le1\), the column of \(P=I-Q\) has absolute sum

\[
\|Pe\|_1=(1-Q_{ee})+\sum_{f\ne e}|Q_{fe}|=1+\|Qe\|_1-2Q_{ee},
\]

which yields the asserted cycle formula. Finally \(P\) and \(Q\) are real symmetric, so their maximum absolute row and column sums agree: \(\|P\|_{\infty\to\infty}=\|P\|_{1\to1}\) and likewise for \(Q\). Minimality gives the same endpoint projection constants. Orthogonal projections have \(\ell_2\) operator norm one for these nonzero proper ranges.

## Verification

Run `python3 check_hamming.py` using Python 3 and only its standard library. The program independently constructs graph Laplacians, solves exact rational grounded Poisson systems for nine graphs, and compares the resulting edge-column norms and diagonal values to the stated formulas. It additionally verifies five radial-integral identities for all forty-nine pairs \(2\le d,q\le8\). A total of 281 exact-rational identities passed during preparation. The finite tests are not an exhaustive proof of the all-parameter result; the preceding analytic argument supplies that proof.

## Relationship to prior work

Dilworth–Kutzarova–Ostrovskii, arXiv:2305.12582v1 (2023), already establish the uniqueness of the invariant cycle projection for arbitrary Hamming alphabets (Theorem 43). Their Theorem 45 and Corollary 60 explicitly evaluate endpoint norms only for the binary cube \(q=2\). The present calculation adds the exact nonbinary endpoint formulas, and transfers the pre-existing invariant-projection result to simultaneous \(\ell_p\) minimality of both complementary projections. Thus neither the uniqueness theorem nor the binary specialization is claimed as new.

## Limitations

The result concerns real unweighted Hamming graph edge spaces with full alphabet-permutation symmetry. General weighted Cartesian products or non-isomorphic coordinate alphabets are not treated. The proof uses the known invariant-projection uniqueness theorem as an external premise; it does not reprove that theorem. The literature comparison may be incomplete outside the inspected primary paper and searchable mathematical records; no independent audit or priority determination is asserted. No sharp intermediate-\(p\) numerical values are claimed.

## References

1. S. J. Dilworth, D. Kutzarova, and M. I. Ostrovskii, “Cycle spaces: invariant projections and applications to transportation cost,” arXiv:2305.12582v1 (first public 21 May 2023), especially Sections 2.6–2.7, Theorems 43 and 45 and Corollary 60. https://arxiv.org/abs/2305.12582
