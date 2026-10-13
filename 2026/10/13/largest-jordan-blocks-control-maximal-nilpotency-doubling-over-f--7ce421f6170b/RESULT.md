# Largest Jordan blocks control maximal nilpotency doubling over finite dual numbers
## Finding
Let \(q\) be a prime power and let
\[
R_q=\mathbb F_q[\varepsilon]/(\varepsilon^2).
\]
Let \(A\in M_n(\mathbb F_q)\) be nilpotent of index \(r\), meaning that \(r\) is the least positive integer with \(A^r=0\). Put
\[
s=\operatorname{rank}(A^{r-1}),
\qquad
X_B=A+\varepsilon B\quad(B\in M_n(\mathbb F_q)).
\]
Then every \(X_B\) has nilpotency index at most \(2r\), and
\[
\operatorname{ind}(X_B)=2r
\quad\Longleftrightarrow\quad
A^{r-1}BA^{r-1}\ne0.
\]
Equivalently,
\[
\operatorname{ind}(X_B)=2r
\quad\Longleftrightarrow\quad
B(\operatorname{im}A^{r-1})\not\subseteq\ker A^{r-1}.
\]
The dual parts that fail maximal doubling form a linear subspace of \(M_n(\mathbb F_q)\) of codimension \(s^2\). Hence
\[
\#\{B:\operatorname{ind}(X_B)=2r\}
=q^{n^2}-q^{n^2-s^2},
\]
and a uniformly chosen dual part has maximal doubled index with probability
\[
1-q^{-s^2}.
\]
For nilpotent \(A\), the integer \(s\) is exactly the number of Jordan blocks of size \(r\). Thus the maximal-index density depends only on the multiplicity of the largest Jordan blocks, and the maximum possible index among all lifts of every nilpotent \(A\) is exactly \(2r\).

## Assumptions and scope
The theorem is stated over an arbitrary finite field \(\mathbb F_q\), with no characteristic restriction. The nilpotency-index convention also covers \(A=0\): then \(r=1\), \(s=n\), and \(\varepsilon B\) has index \(2\) exactly when \(B\ne0\), giving \(q^{n^2}-1\) maximal lifts.

The structural criterion
\[
A^{r-1}BA^{r-1}\ne0
\]
is field-independent. Finiteness of the base field is used only for the exact count and probability.

## Proof
Because \(\varepsilon\) is central and \(\varepsilon^2=0\), for every integer \(m\ge1\),
\[
X_B^m
=A^m+\varepsilon\sum_{i=0}^{m-1}A^iBA^{m-1-i}.
\]
For \(m=2r\), the real part vanishes and every summand in the \(\varepsilon\)-coefficient contains either a left or a right power of \(A\) with exponent at least \(r\). Therefore
\[
X_B^{2r}=0.
\]
For \(m=2r-1\), all terms vanish except the term with \(i=r-1\), so
\[
X_B^{2r-1}
=\varepsilon A^{r-1}BA^{r-1}.
\]
It follows immediately that \(X_B\) has index \(2r\) exactly when \(A^{r-1}BA^{r-1}\ne0\). Since \(A^{r-1}\ne0\), such \(B\) exist, so the upper bound \(2r\) is always attained.

Write \(P=A^{r-1}\). Since \(P: \mathbb F_q^n\to\operatorname{im}P\) is surjective,
\[
PBP=0
\quad\Longleftrightarrow\quad
PB|_{\operatorname{im}P}=0
\quad\Longleftrightarrow\quad
B(\operatorname{im}P)\subseteq\ker P.
\]
Thus the nonmaximal dual parts are the kernel of the linear map
\[
L_P:M_n(\mathbb F_q)\longrightarrow M_n(\mathbb F_q),
\qquad L_P(B)=PBP.
\]
Under vectorization, \(L_P\) is represented by \(P^T\otimes P\). Hence
\[
\operatorname{rank}L_P
=\operatorname{rank}(P^T)\operatorname{rank}(P)
=s^2.
\]
Therefore \(\ker L_P\) has dimension \(n^2-s^2\), so it contains exactly \(q^{n^2-s^2}\) matrices. Subtracting from the \(q^{n^2}\) possible dual parts proves the counting formula.

Finally, nilpotent Jordan form exists over every field. On each Jordan block of maximal size \(r\), the map \(A^{r-1}\) has rank one, while it vanishes on every smaller block. Consequently \(s\) is exactly the number of largest Jordan blocks.

## Verification
The symbolic proof above is the proof for all prime powers \(q\). The bundled verifier supplies independent finite sanity checks over \(\mathbb F_2\).

It exhausts all \(64\) nilpotent matrices \(A\in M_3(\mathbb F_2)\), and for each one it exhausts all \(512\) dual parts \(B\), computes powers directly in the dual matrix ring, and checks the equivalence between maximal index and \(A^{r-1}BA^{r-1}\ne0\). It also exhausts all \(65536\) dual parts for representatives of the five nilpotent Jordan types in dimension four; the exact count is checked for every \(B\), and direct dual-ring powers are replayed on \(4096\) deterministic dual parts per type.

For the dimension-four types \((4)\), \((3,1)\), \((2,2)\), \((2,1,1)\), and \((1,1,1,1)\), the verifier obtains maximal-lift counts \(32768\), \(32768\), \(61440\), \(32768\), and \(65535\), respectively, exactly as predicted. The run ends with `VERIFY_OK`.

## Relationship to prior work
The February 2026 abstract by Özbay states that a dual matrix is nilpotent according to its real part and that the dual part can increase the nilpotency index. Şentürk and Özbay subsequently prove for real dual matrices that if the real part has index \(r\), then the \(2r\)-th power vanishes. A published result based on those sources determines the complete index distribution when the real part is a single nilpotent Jordan block \(J_n\); in that case there is one largest block, so \(s=1\), and its maximal-index proportion \(1-q^{-1}\) is the special case of the formula here.

The present result addresses the multi-block gap left explicit in that published single-block result. For an arbitrary nilpotent real part, it identifies the entire maximal-index stratum as the complement of a codimension-\(s^2\) linear subspace and shows that only the number of largest Jordan blocks controls its density. It does not claim the complete distribution of the smaller lifted indices.

## Limitations
The theorem classifies only whether a lift reaches the maximal possible index \(2r\); it does not give the full distribution of indices below \(2r\) for a general multi-block nilpotent real part. The exact multiplicity formula requires a finite base field, although the criterion for maximal doubling holds over an arbitrary field. The result concerns the square-zero dual-number extension and does not address higher-order truncated extensions.

## References
1. Neslihan Ayşen Özbay, *On the Algebraic Properties of Matrices over Dual Numbers*, in *2nd International Congress on Natural Sciences and Applied Mathematics Abstracts Book*, p. 52, DOI 10.5281/zenodo.18640991, published 2026-02-14.
2. Berrin Şentürk and Neslihan Ayşen Özbay, *On the Regularity and Clean Properties of Matrices over Dual Numbers*, arXiv:2609.29468v1, submitted 2026-09-24.
3. *Exact nilpotency-index distribution for Jordan lifts over finite dual numbers*, published result record `2026/10/4/SCOPE-exact-nilpotency-index-distribution-for-jordan-lifts-over-finite--a669645ca0b7`.
