# Exact lift counts for shortest self-orthogonal embeddings over \(\mathbb Z_4\)
## Finding

Consider the favorable shortest-embedding regime of An, Kim, and Ling. Let
\[
C\subseteq\mathbb Z_4^n
\]
be a free code of rank \(k\), and fix a shortest doubly even self-orthogonal embedding of its binary residue code with generator
\[
[\overline G\mid B],
\qquad
B\in\mathbb F_2^{k\times r}.
\]
Assume one shortest quaternary lift has generator
\[
[G\mid B'+2X],
\]
where \(B'\) is the \(\{0,1\}\)-lift of \(B\).

The source proves that all shortest quaternary lifts with this fixed binary residue embedding are obtained by replacing \(X\) with
\[
X+Y,
\qquad
Y\in\ker f_B,
\]
where
\[
f_B:\mathbb F_2^{k\times r}\longrightarrow\mathbb F_2^{k\times k},
\qquad
f_B(U)=BU^T+UB^T.
\]

Put
\[
t=\operatorname{rank}_{\mathbb F_2}B.
\]
Then
\[
\boxed{
\dim_{\mathbb F_2}\ker f_B
=
k(r-t)+\frac{t(t+1)}2
}
\]
and hence
\[
\boxed{
\operatorname{rank}f_B
=
\frac{t(2k-t-1)}2
}.
\]

Therefore the exact number of coordinate-labeled generator-matrix lifts extending the fixed original generator \(G\) and the fixed residue embedding \([\overline G\mid B]\) is
\[
\boxed{
N(B)=2^{k(r-t)+t(t+1)/2}
}.
\]

In particular, the lift count depends on the appended binary block only through its rank. For fixed \(k\) and \(r\), if the rank increases from \(t\) to \(t+1\), then
\[
\frac{N_{t+1}}{N_t}=2^{t+1-k}.
\]
Thus the search space is nonincreasing with rank, and it shrinks strictly until the final possible step \(t=k-1\) to \(t=k\), where the exponent is unchanged.

## Assumptions and scope

The statement uses the source's Proposition 5.3. Its hypotheses include that the original \(\mathbb Z_4\)-code is free and that its shortest self-orthogonal embedding length agrees with the shortest doubly even self-orthogonal embedding length of its binary residue code. In this regime the paper constructs all shortest lifts over a fixed shortest binary residue embedding by an affine translate of \(\ker f_B\).

The count here is a count of **coordinate-labeled generator-matrix lifts** with the original generator \(G\) and the residue block \(B\) fixed. It is not a count of monomial-equivalence classes of the resulting codes. Distinct kernel elements give distinct appended \(\mathbb Z_4\)-matrices because the map
\[
Y\longmapsto2Y
\]
from binary matrices into \(\{0,2\}\)-matrices over \(\mathbb Z_4\) is injective.

No claim is made outside the source's Proposition 5.3 regime.

## Proof

Let
\[
B\in\mathbb F_2^{k\times r}
\]
have rank \(t\). The kernel dimension of
\[
f_B(U)=BU^T+UB^T
\]
is unchanged by invertible row and column operations on \(B\).

Indeed, take
\[
P\in\operatorname{GL}(k,2),
\qquad
Q\in\operatorname{GL}(r,2),
\]
and set
\[
B_1=PBQ.
\]
The change of variables
\[
U_1=PUQ^{-T}
\]
is a vector-space bijection, and direct multiplication gives
\[
f_{B_1}(U_1)
=
P f_B(U)P^T.
\]
Hence
\[
U\in\ker f_B
\quad\Longleftrightarrow\quad
U_1\in\ker f_{B_1}.
\]

We may therefore reduce \(B\) to the rank-normal form
\[
B_0=
\begin{pmatrix}
I_t&0\\
0&0
\end{pmatrix},
\]
with \(k\) rows and \(r\) columns.

Write a general matrix \(U\in\mathbb F_2^{k\times r}\) as
\[
U=(U^{(1)}\mid U^{(2)}),
\]
where \(U^{(1)}\) consists of the first \(t\) columns and \(U^{(2)}\) the remaining \(r-t\) columns. The equation
\[
B_0U^T+UB_0^T=0
\]
has three immediate consequences.

First, the block \(U^{(2)}\) is completely unrestricted, contributing
\[
k(r-t)
\]
free binary coordinates.

Second, the bottom \((k-t)\times t\) block of \(U^{(1)}\) must vanish.

Third, the top \(t\times t\) block of \(U^{(1)}\) must satisfy
\[
A+A^T=0.
\]
Over \(\mathbb F_2\), this means exactly that \(A\) is symmetric. The vector space of symmetric \(t\times t\) binary matrices has dimension
\[
\frac{t(t+1)}2.
\]

Adding the free dimensions yields
\[
\dim\ker f_B
=
k(r-t)+\frac{t(t+1)}2.
\]
Since the domain has dimension \(kr\), rank-nullity gives
\[
\operatorname{rank}f_B
=
kr-k(r-t)-\frac{t(t+1)}2
=
\frac{t(2k-t-1)}2.
\]

The source's Proposition 5.3 says that, once one lift \(X\) is fixed, every shortest lift with the same binary residue embedding is uniquely of the form
\[
X+Y,
\qquad
Y\in\ker f_B.
\]
Therefore the number of lifts is
\[
|\ker f_B|
=
2^{k(r-t)+t(t+1)/2}.
\]

Finally, if
\[
e(t)=k(r-t)+\frac{t(t+1)}2,
\]
then
\[
e(t+1)-e(t)=t+1-k,
\]
which proves the rank-monotonicity statement.

## Verification

`artifacts/verify.py` uses only the Python standard library.

For every binary matrix \(B\) with
\[
1\le k\le3,
\qquad
1\le r\le3,
\]
the script computes \(t=\operatorname{rank}B\), exhausts every matrix
\[
U\in\mathbb F_2^{k\times r},
\]
and directly counts the solutions of
\[
BU^T+UB^T=0.
\]
For every one of these matrices it checks that the count is exactly
\[
2^{k(r-t)+t(t+1)/2}.
\]

Independently, it constructs the matrix of the linear map \(f_B\) and verifies the rank formula
\[
\operatorname{rank}f_B
=
\frac{t(2k-t-1)}2.
\]
It also checks the canonical rank-normal forms through \(k,r\le6\) and verifies the adjacent-rank exponent identity.

The finite computation is a stress test; the arbitrary-size statement is proved symbolically in the Proof section.

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

An, Kim, and Ling solve the relevant structural embedding problem over \(\mathbb Z_4\). In the favorable equality regime, their Proposition 5.3 parametrizes all shortest lifts over a fixed binary residue embedding by the kernel of
\[
U\longmapsto BU^T+UB^T,
\]
and their algorithm enumerates these choices when searching for good Lee distance.

The paper does not state the dimension of that kernel, the number of lifts, or a rank-only formula for the search-space size. Its computational section reports successful searches and twelve database-improving codes, but not the cardinality of the affine lift spaces searched.

The new result closes that quantitative gap: the entire number of lifts is determined by the single invariant
\[
t=\operatorname{rank}B.
\]
This is stronger than merely observing that the kernel can be found by Gaussian elimination, because it gives a closed formula valid for every \(k,r\) and every binary block of rank \(t\).

Focused searches using the source title and identifier, the map \(BU^T+UB^T\), kernel-dimension language, lift-count terminology, and the closed exponent formula did not locate a prior statement of this count.

## Limitations

The formula counts lifts over one fixed binary residue embedding, with coordinate labels and the original generator fixed. Different kernel elements can still yield codes that become equivalent after a monomial transformation, and no orbit count is claimed.

The theorem relies on the source's favorable equality regime. It does not count embeddings when the shortest quaternary length is strictly larger than the shortest doubly even residue-embedding length.

The count measures the size of the lift search space, not the number of lifts attaining any specified Lee distance.

## References

1. Junmin An, Jon-Lark Kim, and San Ling, *Embedding linear codes over \(\mathbb Z_4\) into self-orthogonal codes*, arXiv:2606.08964v1, first public 8 June 2026; Designs, Codes and Cryptography 94 (2026), DOI 10.1007/s10623-026-01948-1.
2. Junmin An, Nathan Kaplan, Jon-Lark Kim, Jinquan Luo, and Guodong Wang, *Shortest self-orthogonal embeddings of binary linear codes*, arXiv:2511.05440, 2025.
