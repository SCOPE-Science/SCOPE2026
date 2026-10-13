# Zero forcing polynomials completely recognize fully nonfield co-maximal ideal graphs

## Finding

Let \(R\cong\prod_{i=1}^{r}R_i\) be a finite commutative ring with \(r\ge2\) local factors, assume every \(R_i\) is not a field, and let \(\lambda_i\ge2\) be the number of proper ideals of \(R_i\). For every nonempty proper \(S\subset[r]\), put \(w_S=\prod_{i\in S}\lambda_i\), \(m=2^r-2\), and \(N=\sum_{\varnothing\ne S\subsetneq[r]}w_S\). Then \[\mathcal Z(\mathcal C(R);u)=u^{N-m}\prod_{\varnothing\ne S\subsetneq[r]}(u+w_S).\] Consequently \(Z(\mathcal C(R))=M(\mathcal C(R))=N-m\), its real symmetric minimum rank is \(m=2^r-2\), and its minimum zero forcing sets are exactly the complements of one vertex from each Boolean blow-up class; their number is \((\prod_i\lambda_i)^{2^{r-1}-1}\). Moreover the polynomial recovers the unordered multiset \(\{\lambda_1,\ldots,\lambda_r\}\), and therefore determines \(\mathcal C(R)\) up to graph isomorphism within this fully nonfield finite local-product class.

For products of finite chain rings, the recovered proper-ideal counts are the nilpotency lengths, so the polynomial recovers the full chain-length multiset.

## Assumptions and scope

Let \(R\cong R_1\times\cdots\times R_r\), where \(r\ge2\), every \(R_i\) is a finite local nonfield, and \(\lambda_i\) is its number of proper ideals. The co-maximal ideal graph \(\mathcal C(R)\) has the proper ideals not contained in the Jacobson radical as vertices; two vertices are adjacent when their sum is \(R\).

The published Boolean blow-up theorem gives an independent class \(T_S\) for each nonempty proper \(S\subset[r]\), with
\[
|T_S|=w_S=\prod_{i\in S}\lambda_i,
\]
and \(T_S\) is completely joined to \(T_T\) exactly when \(S\cap T=\varnothing\).

## Proof

Each \(T_S\) is a false-twin class, so a zero forcing set cannot leave two white vertices in one class. Conversely, assume at most one white vertex remains in each class. Since every \(\lambda_i\ge2\), every class still contains a blue vertex. If \(\mathcal W\) is the nonempty set of white types, choose an inclusion-minimal \(T\in\mathcal W\). The complementary type \(T^c=[r]\setminus T\) is nonempty and proper. A blue vertex in \(T_{T^c}\) is adjacent to a white type \(U\) exactly when \(U\subseteq T\). Minimality makes \(T\) its unique white neighbor, so it forces the white vertex of \(T_T\). Repeating peels every white type.

Thus a class of size \(w_S\) independently contributes
\[
u^{w_S}+w_Su^{w_S-1}=u^{w_S-1}(u+w_S),
\]
which proves
\[
\mathcal Z(\mathcal C(R);u)=u^{N-m}\prod_{\varnothing\ne S\subsetneq[r]}(u+w_S).
\]
The minimum sets omit one vertex from every class, so \(Z=N-m\). Their count is \(\prod_Sw_S\). Every \(\lambda_i\) occurs in exactly \(2^{r-1}-1\) proper nonempty subset products, yielding \((\prod_i\lambda_i)^{2^{r-1}-1}\).

For minimum rank, let \(A_r\) be the adjacency matrix of the Boolean disjointness graph on the \(m=2^r-2\) nonempty proper subsets. The full disjointness matrix on all subsets is
\[
D_r=\begin{pmatrix}1&1\\1&0\end{pmatrix}^{\otimes r}.
\]
For \(r\ge2\), \(\det D_r=1\). Ordering the subsets as \(\varnothing\), the nonempty proper subsets, and \([r]\), then expanding along the \([r]\)-row and the resulting last column gives \(\det D_r=-\det A_r\). Hence \(\det A_r=-1\).

If \(X\) is the vertex-to-class incidence matrix, the actual adjacency matrix is \(XA_rX^{\mathsf T}\). Since every class is nonempty and \(A_r\) is invertible, its rank is \(m\), so \(\operatorname{mr}\le m\). The standard inequality \(M(G)\le Z(G)\) gives \(\operatorname{mr}=N-M\ge N-Z=m\). Therefore \(\operatorname{mr}=m\) and \(M=Z=N-m\).

Finally, the nonzero root magnitudes are the multiset of all proper nonempty subset products of the \(\lambda_i\). Their number recovers \(r\). Their product is \((\prod_i\lambda_i)^{2^{r-1}-1}\), so the full product \(P=\prod_i\lambda_i\) is recovered exactly. Adding \(1\) and \(P\) gives the multiset of all subset products. Since every \(\lambda_i\ge2\), this multiset can be inverted greedily: the smallest unexplained product is the next smallest \(\lambda_i\); remove all products obtained by multiplying it by the subset products already generated and iterate. Multiplicities handle repeated \(\lambda_i\). Thus the unordered local-count multiset is recovered.

## Verification

The packaged `verify.py` was inspected at its actual package path before replay. It proves computationally, with exact arithmetic, that the Boolean quotient determinant is \(-1\) for \(2\le r\le5\); exhausts every at-most-one-white profile through \(r=4\), including all \(16384\) profiles there; exhaustively reproduces the complete graph-level polynomial for \(\lambda=(2,2),(2,3),(2,2,2)\); checks representative full adjacency ranks; and replays subset-product reconstruction through five local factors with repetitions.

```text
B_2: types=2, determinant=-1
B_3: types=6, determinant=-1
B_4: types=14, determinant=-1
B_5: types=30, determinant=-1
B_2: all 4 at-most-one-white profiles force
B_3: all 64 at-most-one-white profiles force
B_4: all 16384 at-most-one-white profiles force
lambda=(2, 2): N=4, Z=2, minimum_sets=4
lambda=(2, 3): N=5, Z=3, minimum_sets=6
lambda=(2, 2, 2): N=18, Z=12, minimum_sets=512
lambda=(2, 3): adjacency_rank=2
lambda=(2, 2, 2): adjacency_rank=6
lambda=(2, 2, 2, 2): adjacency_rank=14
recovery (2, 2) -> (2, 2)
recovery (2, 5) -> (2, 5)
recovery (2, 2, 2) -> (2, 2, 2)
recovery (2, 3, 4) -> (2, 3, 4)
recovery (2, 2, 3, 5) -> (2, 2, 3, 5)
recovery (2, 3, 3, 4, 7) -> (2, 3, 3, 4, 7)
VERIFY_OK
```

The finite computations corroborate rather than replace the arbitrary-\(r\) proof.

## Relationship to prior work

Ye and Wu introduced co-maximal ideal graphs. Their article has primary Mathematics Subject Classification \(13A15\) and was published on 9 November 2012. Ye, Wu, Liu, and Yu subsequently proved the Boolean blow-up theorem and the class-size product formula used here; their inspected full text contains no occurrence of “zero forcing.”

A 2026 modular-compression theorem gives a broader binary type-profile reduction for zero forcing polynomials, so the generic fact that a forcing complement uses at most one representative per false-twin type is prior coverage. Its inspected full text contains no occurrence of “co-maximal” or “Boolean.” The new content here is the arbitrary-r admissibility proof, the exact product factorization, the unimodular minimum-rank theorem, and exact inversion of the polynomial to all local proper-ideal counts.

A previously obtained three-local-factor theorem is a strict special-rank overlap. It does not imply the arbitrary-r inclusion-minimal peeling argument, the Kronecker determinant identity, or the general subset-product reconstruction theorem.

## Limitations

Every local factor is assumed to be a nonfield. If some \(\lambda_i=1\), singleton blow-up classes can lose their only blue vertex, so the all-profiles forcing argument no longer applies unchanged. The polynomial recovers proper-ideal counts, not local ring isomorphism types. Minimum rank is over real symmetric graph-pattern matrices. Generic modular compression is prior work and is not claimed as new.

## References

1. M. Ye and T. Wu, “Co-Maximal Ideal Graphs of Commutative Rings,” *Journal of Algebra and Its Applications* 11 (2012), 1250114. DOI: 10.1142/S0219498812501149. Published 9 November 2012.
2. M. Ye, T. Wu, Q. Liu, and H. Yu, “Implements of Graph Blow-Up in Co-Maximal Ideal Graphs,” *Communications in Algebra* 42 (2014), 2476–2483. DOI: 10.1080/00927872.2012.762924. Public author-uploaded full text dated 19 December 2013.
3. X. Wang, “Modular Compression of Leaky Forts and Leaky Forcing Polynomials,” preprint, 26 May 2026. DOI: 10.5281/zenodo.20388397.
4. K. Boyer et al., “The zero forcing polynomial of a graph,” *Discrete Applied Mathematics* 258 (2019), 35–48. arXiv:1801.08910.
5. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
