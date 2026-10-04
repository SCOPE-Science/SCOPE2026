# The eighth multilinear codimension of \(M_2\) in characteristic \(2\) is \(4487\)

## Finding
Let \(K\) be an infinite field of characteristic \(2\), let \(P_n\) be the \(K\)-space spanned by the \(n!\) multilinear words
\[
x_{\sigma(1)}x_{\sigma(2)}\cdots x_{\sigma(n)},\qquad \sigma\in S_n,
\]
and define the ordinary multilinear codimension
\[
c_n(M_2(K))=\dim_K\bigl(P_n/(P_n\cap \operatorname{Id}(M_2(K)))\bigr).
\]
Then
\[
c_8(M_2(K))=4487.
\]
Equivalently, the degree-eight multilinear identity space has dimension
\[
8!-4487=35833.
\]

## Assumptions and scope
The statement concerns ordinary associative polynomial identities, without grading or involution, over an infinite field \(K\) of characteristic \(2\). It is a degree-eight finite-cutoff statement and does not claim a finite basis for the full T-ideal of \(M_2(K)\).

The restriction to infinite \(K\) matches the setting of the recent source that determines the multilinear identities through degree \(7\). The rank computation below is performed over the prime field \(\mathbb F_2\); because its matrix has entries in \(\{0,1\}\), the same rank holds after extension of scalars to every characteristic-two field.

## Proof
Write \(E_{ij}\), \(i,j\in\{0,1\}\), for the four matrix units. Because a multilinear polynomial is linear in each variable, it vanishes on every tuple in \(M_2(K)^n\) if and only if it vanishes on every tuple of matrix units. Thus the kernel of the linear evaluation map
\[
\operatorname{ev}_n:P_n\longrightarrow \bigoplus_{(A_1,\ldots,A_n)\in\{E_{00},E_{01},E_{10},E_{11}\}^n}M_2(K)
\]
is exactly \(P_n\cap\operatorname{Id}(M_2(K))\), and hence \(c_n(M_2(K))=\operatorname{rank}(\operatorname{ev}_n)\).

For a fixed word \(x_{\sigma(1)}\cdots x_{\sigma(n)}\), a nonzero matrix-unit evaluation is equivalent to a binary path
\[
a_0,a_1,\ldots,a_n\in\{0,1\}
\]
with
\[
x_{\sigma(k)}=E_{a_{k-1},a_k}\quad(1\le k\le n),
\]
in which case the product is \(E_{a_0,a_n}\). Therefore one can construct the entire evaluation column of a word by enumerating the \(2^{n+1}\) binary paths, encoding the induced assignment of one of four matrix units to each variable together with the output matrix unit.

For \(n=8\), this yields a \(262144\)-row binary evaluation matrix with \(40320\) columns. Exact Gaussian elimination over \(\mathbb F_2\) gives
\[
\operatorname{rank}(\operatorname{ev}_8)=4487.
\]
The same rank is obtained by two independent elimination orders: one partitions the columns by the first variable of the word and eliminates using highest set-bit pivots; the other partitions by the last variable in reverse order and uses lowest set-bit pivots. Hence
\[
\dim(P_8\cap\operatorname{Id}(M_2(K)))=40320-4487=35833.
\]
Since the evaluation matrix is defined over \(\mathbb F_2\), its rank is unchanged on scalar extension from \(\mathbb F_2\) to \(K\), proving the claim.

## Verification
The package contains three standalone exact checkers. `artifacts/verify_low_degree.py` reconstructs the same matrix-unit evaluation map through degree \(7\) and returns the quotient dimensions
\[
1,2,6,23,90,340,1246.
\]
In particular, the degree-four kernel is one-dimensional, which is consistent with the standard polynomial identity of degree \(4\).

`artifacts/verify_rank8_forward.cpp` exhausts all \(40320\) degree-eight words, groups them by first variable, and performs exact binary elimination; it returns rank \(4487\) and kernel dimension \(35833\). `artifacts/verify_rank8_reverse.cpp` repeats the exhaustive calculation with a different column partition, opposite traversal, and opposite pivot convention, again returning rank \(4487\) and kernel dimension \(35833\).

These are exhaustive finite linear-algebra computations, not samples. The arbitrary-infinite-field conclusion follows from the symbolic matrix-unit reduction and scalar-extension argument above.

## Relationship to prior work
Iritan Ferreira dos Santos, arXiv:2609.25362v1, studies \(M_2(K)\) over infinite fields of characteristic \(2\). The paper's public abstract states that the standard degree-four identity and two degree-five multilinear identities generate all multilinear identities through degree \(7\), and it notes that the associative finite-basis problem remains open. The present claim concerns the immediately next multilinear degree and gives its exact codimension rather than a generating theorem.

Semantic searches of the published-finding corpus corpus for the exact degree-eight codimension, the value \(4487\), and equivalent formulations did not locate an entry asserting this result. Nearby records about matrix power sums, graded involutions, and superinvolution codimensions concern different identity theories and do not imply the ordinary characteristic-two multilinear codimension computed here.

## Limitations
The full text of arXiv:2609.25362v1 was not accessible in the inspected source channel; only its public abstract and indexing metadata were available. Consequently, although the abstract scopes the stated generation theorem to degree at most \(7\), an unadvertised degree-eight table or observation in the full manuscript could not be excluded directly. Older literature may also contain the same codimension under different terminology. The literature search therefore supports, but does not prove, originality.

The result gives one exact next-degree invariant. It neither proves nor disproves finite basability of \(\operatorname{Id}(M_2(K))\), and it does not identify a minimal generating set for the degree-eight identity space.

## References
1. Iritan Ferreira dos Santos, *On multilinear polynomial identities for \(2\times2\) matrices in characteristic \(2\)*, arXiv:2609.25362v1, first submitted 21 September 2026.
2. V. Drensky, *A minimal basis of identities for a second-order matrix algebra over a field of characteristic 0*, Algebra and Logic 20 (1981/1982). This is characteristic-zero background and does not cover the present characteristic-two claim.
