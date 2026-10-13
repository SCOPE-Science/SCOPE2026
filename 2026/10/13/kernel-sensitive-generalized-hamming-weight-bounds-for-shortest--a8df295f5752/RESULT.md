# Kernel-sensitive generalized Hamming-weight bounds for shortest LCD embeddings
## Finding

Let
\[
F\in\{\mathbb F_2,\mathbb F_3,\mathbb F_4\}
\]
with the Euclidean/Hermitian convention used by An, Hong, Kim, and Lim. Let \(C\subseteq F^n\) be an \([n,k]\) linear code with
\[
\ell=\dim\operatorname{Hull}(C),
\]
and let
\[
\widetilde C\subseteq F^{n+\ell}
\]
be any shortest LCD embedding of \(C\).

Puncturing the \(\ell\) added coordinates gives a linear isomorphism
\[
P:\widetilde C\longrightarrow C.
\]
Let
\[
Q:\widetilde C\longrightarrow F^\ell
\]
be projection onto the added coordinates. The shortest-embedding normal form implies that \(Q\) is surjective. Define
\[
K=P(\ker Q)\le C.
\]
Then
\[
\dim K=k-\ell.
\]

With the convention
\[
d_0(K)=0,
\]
every generalized Hamming weight satisfies
\[
d_r(\widetilde C)\ge
\min_{\substack{\max(0,r-k+\ell)\le t\le\min(r,\ell)\\t\in\mathbb Z}}
\left[
t+\max\{d_r(C),d_{r-t}(K)\}
\right],
\qquad 1\le r\le k.
\]

Consequently,
\[
d_r(C)+\max(0,r-k+\ell)
\le d_r(\widetilde C)
\le d_r(C)+\ell.
\]
At full dimension,
\[
d_k(\widetilde C)=d_k(C)+\ell.
\]

If \(C\) is self-orthogonal, then \(\ell=k\), so \(K=0\) and
\[
d_r(\widetilde C)\ge d_r(C)+r,
\qquad 1\le r\le k.
\]

Thus hull dimension controls not only the number of coordinates required by a shortest LCD embedding, but also forces growth in the upper generalized Hamming-weight hierarchy. The kernel subcode \(K\) supplies a sharper embedding-specific correction.

## Assumptions and scope

For a linear code \(D\), define
\[
d_r(D)=
\min_{\substack{U\le D\\\dim U=r}}
|\operatorname{Supp}(U)|.
\]

The source proves that a shortest LCD embedding of an \([n,k]\) code with hull dimension \(\ell\) has length \(n+\ell\), and characterizes every such embedding by an appended block of rank \(\ell\). Equivalently, after row operations, the added columns contain an invertible \(\ell\times\ell\) block.

No generalized Hamming-weight statement is assumed from the source.

The theorem concerns support weights of shortest embeddings. It does not claim that a shortest embedding maximizes any \(d_r\) among all LCD embeddings or all LCD codes of the same dimension and length.

## Proof

The puncturing map
\[
P:\widetilde C\to C
\]
is surjective by the definition of embedding. Since both codes have dimension \(k\), \(P\) is an isomorphism.

The source's shortest-embedding characterization gives
\[
\operatorname{rank}Q=\ell.
\]
Hence
\[
\dim\ker Q=k-\ell,
\qquad
\dim K=k-\ell.
\]

Fix an \(r\)-dimensional subcode
\[
U\le\widetilde C
\]
and set
\[
t=\dim Q(U).
\]
Rank-nullity gives
\[
\dim(U\cap\ker Q)=r-t.
\]
Since \(\dim\ker Q=k-\ell\),
\[
t\ge\max(0,r-k+\ell),
\]
while trivially
\[
t\le\min(r,\ell).
\]

Old and new coordinates are disjoint, so
\[
|\operatorname{Supp}(U)|
=
|\operatorname{Supp}(P(U))|
+
|\operatorname{Supp}(Q(U))|.
\]
Because \(P\) is injective,
\[
\dim P(U)=r,
\]
and therefore
\[
|\operatorname{Supp}(P(U))|\ge d_r(C).
\]

Also,
\[
P(U\cap\ker Q)
\]
is an \((r-t)\)-dimensional subcode of \(K\). Hence, with \(d_0(K)=0\),
\[
|\operatorname{Supp}(P(U))|
\ge
\max\{d_r(C),d_{r-t}(K)\}.
\]

The \(t\)-dimensional code \(Q(U)\le F^\ell\) has support size at least \(t\), since a rank-\(t\) generator needs at least \(t\) nonzero coordinate columns. Thus
\[
|\operatorname{Supp}(U)|
\ge
t+\max\{d_r(C),d_{r-t}(K)\}.
\]
Minimizing over the admissible values of \(t\) and then over \(U\) proves the kernel-sensitive lower bound.

Dropping the kernel term and using the smallest admissible \(t\) gives
\[
d_r(\widetilde C)
\ge
d_r(C)+\max(0,r-k+\ell).
\]

For the upper bound, choose an \(r\)-dimensional \(V\le C\) attaining \(d_r(C)\). Its unique lift \(P^{-1}(V)\) uses at most all \(\ell\) added coordinates, so
\[
d_r(\widetilde C)\le d_r(C)+\ell.
\]

For \(r=k\), the old-coordinate support of \(\widetilde C\) is the support of \(C\), while \(Q(\widetilde C)=F^\ell\) uses every added coordinate. Therefore
\[
d_k(\widetilde C)=d_k(C)+\ell.
\]

If \(C\) is self-orthogonal, then \(\ell=k\). The only admissible projection rank is \(t=r\), yielding
\[
d_r(\widetilde C)\ge d_r(C)+r.
\]

## Verification

`artifacts/verify.py` uses only the Python standard library.

It exhaustively generates small systematic binary and ternary codes. For each source generator it computes the Euclidean hull, changes to a basis beginning with a hull basis, and constructs the source normal-form shortest LCD embedding by appending an identity block to the hull rows.

For every tested code the script checks the source hull dimension, full rank of the embedded Gram matrix, rank \(\ell\) of the added-coordinate projection, dimension \(k-\ell\) of \(K\), and every generalized Hamming weight of \(C\), \(K\), and \(\widetilde C\) by exhaustive reduced-row-echelon enumeration of all message subspaces.

It then verifies the kernel-sensitive lower bound in every subcode dimension, the universal two-sided bound, the terminal equality, and the self-orthogonal specialization whenever applicable.

The finite computation is a stress test. The arbitrary-length theorem is established by the rank-nullity and support argument above.

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

An, Hong, Kim, and Lim prove that the minimum number of added coordinates in an LCD embedding equals the hull dimension and characterize all shortest embeddings. They use this structure to improve ordinary minimum distance and construct new optimal LCD codes. Their paper does not discuss generalized Hamming weights.

Generalized Hamming weights are classical higher-support invariants. Recent algorithmic work gives general methods for computing generalized and relative generalized Hamming weights, but does not state a shortest-LCD-embedding law connecting the hierarchy with hull dimension and the kernel of the added-coordinate projection.

The coarse estimate
\[
d_r(\widetilde C)\le d_r(C)+\ell
\]
is included only as context. The substantive statement is the rank-sensitive lower bound and its kernel refinement. Its forced term
\[
\max(0,r-k+\ell)
\]
uses the full-rank added-coordinate projection specific to a shortest LCD embedding.

Focused searches under shortest-LCD-embedding, generalized-Hamming-weight, puncturing, kernel-subcode, hull-dimension, projection-rank, and weight-hierarchy formulations did not locate this bound.

## Limitations

The theorem gives bounds, not a universal closed formula for every generalized weight.

The sharper term depends on
\[
K=P(\ker Q),
\]
which can vary with the chosen shortest embedding.

The result is stated in the source's binary, ternary, and quaternary Euclidean/Hermitian setting. The support proof itself applies whenever puncturing is an isomorphism and the added-coordinate projection has known rank.

A general matroid or relative-generalized-weight theorem under different terminology could subsume part of the argument; no such covering result was located.

## References

1. Junmin An, Ji-Hoon Hong, Jon-Lark Kim, and Haeun Lim, *Shortest LCD embeddings of binary, ternary and quaternary linear codes*, arXiv:2601.20600v1, first public version 28 January 2026; Advances in Mathematics of Communications 25 (2026), 192--202, DOI 10.3934/amc.2026048.
2. V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory 37 (1991), 1412--1418.
3. Rodrigo San-José, *An Algorithm for Computing Generalized Hamming Weights and the Sage Package GHWs*, ACM Transactions on Mathematical Software 51 (2025), Article 26, DOI 10.1145/3773284.
