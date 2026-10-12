# Exact finite-field fibers of the zero-product sandwich map

## Finding

For every prime power \(q\) and integer \(n\ge2\), let \(\mathcal T_n(q)\) be the set of ordered triples \((A,B,R)\) of matrices in \(M_n(\mathbb F_q)\) satisfying \(AB=0\), and define the zero-product sandwich map \(\Phi_n(A,B,R)=ARB\). For a fixed matrix \(X\) of rank \(r\), the size \(w_{n,r}(q)=|\Phi_n^{-1}(X)|\) depends only on \(r\) and equals

\[
\boxed{
 w_{n,r}(q)=
 \sum_{\substack{a,b\ge r\\a+b\le n}}
 {n-r\brack a-r}_q
 {n-r\brack b-r}_q
 {n\brack a}_q
 {n-a\brack b}_q
 G_a(q)G_b(q)q^{n^2-ab},
}
\]

where \({s\brack t}_q\) is the Gaussian binomial coefficient and \(G_d(q)=\prod_{j=0}^{d-1}(q^d-q^j)\), with \(G_0(q)=1\). The empty sum is zero; in particular \(w_{n,r}(q)=0\) for \(2r>n\). Every rank \(r\le\lfloor n/2\rfloor\) has strictly positive fiber size.

Thus the entire probability distribution of \(\Phi_n(A,B,R)\), with the triple chosen uniformly from \(\mathcal T_n(q)\), is explicit. The probability of output rank \(r\) is

\[
\frac{{n\brack r}_q^2 G_r(q) w_{n,r}(q)}{
\sum_{s=0}^{\lfloor n/2\rfloor}{n\brack s}_q^2 G_s(q)w_{n,s}(q)}.
\]

For \(n=4\), \(q=2\), the exact fiber sizes for ranks \(0,1,2,3,4\) are, respectively,
\[
(35{,}813{,}933{,}056,\ 689{,}848{,}320,\ 5{,}160{,}960,\ 0,\ 0).
\]
The previously established half-rank theorem determines the support of this distribution; the formula above determines the multiplicity of **every** output.

## Assumptions and scope

The field \(\mathbb F_q\) is arbitrary, of prime-power cardinality \(q\). There are no restrictions on the matrices beyond \(AB=0\); in particular, \(A\), \(B\), and \(R\) may be singular or zero. The triples are ordered and the matrices are counted with their actual entries, not up to similarity. The rank \(r\) lies in \(0\le r\le n\), and the theorem includes the zero output.

## Proof

Fix \(X\in M_n(\mathbb F_q)\) of rank \(r\). Write \(a=\operatorname{rank}A\), \(b=\operatorname{rank}B\). The condition \(AB=0\) is equivalent to \(\operatorname{im}B\subseteq\ker A\) and forces \(a+b\le n\). The equation \(ARB=X\) forces \(\operatorname{im}X\subseteq\operatorname{im}A\) and \(\ker B\subseteq\ker X\), hence \(r\le a,b\).

Conversely, these three inclusions suffice for the existence of \(R\): because \(B\) induces an isomorphism \(V/\ker B\to\operatorname{im}B\) and \(A\) surjects onto \(\operatorname{im}A\), the assignment \(R\mapsto ARB\) has image exactly the space of linear maps \(V/\ker B\to\operatorname{im}A\). This space has dimension \(ab\) over \(\mathbb F_q\). Every specified \(X\) satisfying the two compatibility inclusions therefore has exactly \(q^{n^2-ab}\) preimages \(R\).

Count the compatible ordered pairs \((A,B)\) at fixed ranks \((a,b)\). The image of \(A\) can be any \(a\)-space containing the fixed \(r\)-space \(\operatorname{im}X\), giving \({n-r\brack a-r}_q\) choices. The kernel of \(B\) can be any \((n-b)\)-space contained in the fixed \((n-r)\)-space \(\ker X\), giving \({n-r\brack b-r}_q\) choices. Independently choose the \((n-a)\)-dimensional kernel \(H\) of \(A\) in \({n\brack a}_q\) ways, then the \(b\)-dimensional image \(J\) of \(B\) inside \(H\) in \({n-a\brack b}_q\) ways. For fixed image and kernel, a rank-\(a\) operator \(A\) is the same as an isomorphism \(V/H\to\operatorname{im}A\), so there are \(G_a(q)\) choices. Similarly there are \(G_b(q)\) operators \(B\) with the chosen image and kernel. No further incidence conditions arise: images and kernels of an arbitrary linear map can be prescribed independently at the requisite dimensions.

Multiplying these six factors, then the \(q^{n^2-ab}\) possible intermediates \(R\), and summing over \(r\le a,b\) and \(a+b\le n\), gives the boxed formula. The nonzero terms with \(a=b=r\) show positivity whenever \(2r\le n\). Left-right invertible changes of the output are also consistent with the rank-only dependence: \((A,B,R)\mapsto(PA,BQ,R)\) preserves \(AB=0\) and sends \(ARB\) to \(P(ARB)Q\).

The standard rank-\(r\) matrix count is \({n\brack r}_q^2G_r(q)\). Multiplying this count by the uniform rank-\(r\) fiber size and normalizing yields the displayed output distribution. An independent total-mass identity is

\[
 \sum_{r=0}^{n}{n\brack r}_q^2G_r(q)w_{n,r}(q)
 = q^{n^2}\sum_{\substack{a,b\ge0\\a+b\le n}}
 {n\brack a}_q^2{n-a\brack b}_q{n\brack b}_qG_a(q)G_b(q),
\]

because the right side counts all \((A,B,R)\) with \(AB=0\) by first choosing \((A,B)\) and then choosing arbitrary \(R\). This identity is a consequence of the proof, not an independent assumption.

## Verification

Run `python3 verify.py` using Python 3 with no third-party dependencies. The script exhaustively enumerates all triples for \(n=2\) over \(\mathbb F_2\) and \(\mathbb F_3\), checking both the zero fiber and a fixed rank-one fiber. It also enumerates all ordered pairs \((A,B)\) of binary \(3\times3\) matrices, separately verifying the compatible-pair count for targets of ranks \(0,1,2\), and checks the independent total-mass identity for \(2\le n\le5\) and \(q\in\{2,3\}\). It outputs `VERIFY_OK` if every assertion succeeds. These finite computations check implementation and boundary cases; the universal theorem is established by the preceding argument.

## Relationship to prior work

Subba and Subedi introduced zero-insertive elements and ZINC rings in 2025, and their September 2026 paper studies path and Leavitt path algebras, proving that every singular \(2\times2\) matrix over a field is zero-insertive. A prior publicly available note, *Zero-insertive matrices are exactly the half-rank locus* (record identifier `8052759fe4ed`), proves \(Z_i(M_n(D))\) is precisely the rank-\(\le\lfloor n/2\rfloor\) determinantal locus over division rings and counts its finite-field points. That rank-locus classification and its point count are **not** new here.

The present result answers a different quantitative question: for each individual output, **how many ordered zero-product sandwiches produce it?** The cited rank-locus theorem determines merely whether a fiber is empty, not its cardinality. The full witness distribution is not recovered from the number of eligible outputs, since multiplicities need not be equal at different ranks. Standard Gaussian counting of fixed-rank matrices provides some ingredients, but does not by itself impose all three simultaneous compatibility conditions on \(A\), \(B\), and \(R\).

## Limitations

Only full matrix algebras over finite fields are treated; no claim is made for arbitrary rings or for higher product words. The result counts ordered representations, not inequivalent representations under group actions. It does not claim that the half-rank support theorem is new. Although direct overlap searches and the most relevant available texts revealed no previously stated exact witness-fiber formula, a synonymous matrix-enumeration theorem in older literature is possible. Independent mathematical auditing has not been performed.

## References

1. S. Subba and T. Subedi, *Zero Insertive Nil Clean Rings*, arXiv:2508.01333v1, first public 2025-08-02.
2. S. Subba and T. Subedi, *Semicommutativity via Zero-Insertive Elements: Insights from Path and Leavitt Path Algebras*, arXiv:2609.24439v1, first public 2026-09-21.
3. *Zero-insertive matrices are exactly the half-rank locus*, public mathematical record `8052759fe4ed` (2026); the record proves the support theorem and gives point counts.
4. D. Laksov and A. Thorup, *Counting Matrices with Coordinates in Finite Fields and of Fixed Rank*, Mathematica Scandinavica 74 (1994), 19–33; standard rank-enumeration background.
