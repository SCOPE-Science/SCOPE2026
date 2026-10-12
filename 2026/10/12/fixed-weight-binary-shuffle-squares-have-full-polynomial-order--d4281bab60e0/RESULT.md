# Fixed-weight binary shuffle squares have full polynomial order
## Finding
Let \(\mathtt{B}(2n,2k)\) be the set of binary shuffle squares of length \(2n\) containing exactly \(2k\) occurrences of \(\mathtt{1}\). For every pair of integers \(n\ge k\ge1\),
\[
\binom{n+k}{2k}
\le
|\mathtt{B}(2n,2k)|
\le
\binom{2n}{2k}.
\]
Consequently, for every fixed integer \(k\ge1\),
\[
|\mathtt{B}(2n,2k)|=\Theta_k(n^{2k})
\qquad(n\to\infty).
\]

This gives the asymptotic order requested in Section 2.5 of Grytczuk, Pawlik, and Pleszczyński for every fixed number \(2k\) of occurrences of \(\mathtt{1}\).

## Assumptions and scope
A binary word \(W\) of length \(2n\) is a shuffle square if its positions can be partitioned into two increasing subsequences that spell the same word of length \(n\).

The parameter \(k\) is fixed when the asymptotic statement is taken. The two-sided binomial bounds themselves hold simultaneously for all integers \(n\ge k\ge1\).

The result determines the polynomial order \(n^{2k}\). It does not determine the leading asymptotic constant for \(k\ge2\).

## Proof
The upper bound is immediate: every word counted by \(\mathtt{B}(2n,2k)\) is a binary word of length \(2n\) whose \(2k\) positions occupied by \(\mathtt{1}\) can be chosen in
\[
\binom{2n}{2k}
\]
ways.

For the lower bound, choose nonnegative integers
\[
p_0,p_1,\ldots,p_k
\]
satisfying
\[
p_0+p_1+\cdots+p_k=n-k,
\]
and form the length-\(n\) root
\[
X=0^{p_0}1\,0^{p_1}1\cdots1\,0^{p_k}.
\]
For every \(0\le i<k\), choose an integer \(c_i\) with
\[
0\le c_i\le p_i.
\]

Take two labeled copies \(A\) and \(B\) of \(X\). Produce a self-shuffle whose ones occur in the order
\[
A_1,B_1,A_2,B_2,\ldots,A_k,B_k.
\]
Before \(A_{i+1}\), place all \(p_i\) zeros from the current zero block of \(A\), followed by \(c_i\) zeros from the current zero block of \(B\). Between \(A_{i+1}\) and \(B_{i+1}\), place the remaining \(p_i-c_i\) zeros from that block of \(B\). After \(B_k\), place both trailing blocks of \(p_k\) zeros.

The resulting binary word is a shuffle square by construction. Its zero-run lengths before, between, and after the \(2k\) ones are
\[
(p_0+c_0,\ p_0-c_0,\ p_1+c_1,\ p_1-c_1,\ldots,
p_{k-1}+c_{k-1},\ p_{k-1}-c_{k-1},\ 2p_k).
\]
Therefore the output word uniquely recovers every parameter:
\[
p_i=\frac{g_{2i}+g_{2i+1}}2,
\qquad
c_i=\frac{g_{2i}-g_{2i+1}}2
\quad(0\le i<k),
\]
and
\[
p_k=\frac{g_{2k}}2.
\]
Thus distinct parameter tuples give distinct shuffle squares.

For fixed \(p_0,\ldots,p_k\), there are
\[
\prod_{i=0}^{k-1}(p_i+1)
\]
choices of \(c_0,\ldots,c_{k-1}\). Summing over all weak compositions of \(n-k\) gives
\[
\sum_{p_0+\cdots+p_k=n-k}
\prod_{i=0}^{k-1}(p_i+1).
\]
Its generating function in \(n-k\) is
\[
\left(\sum_{p\ge0}(p+1)z^p\right)^k
\left(\sum_{p\ge0}z^p\right)
=
(1-z)^{-(2k+1)}.
\]
Hence the number of constructed words is exactly
\[
[z^{n-k}](1-z)^{-(2k+1)}
=
\binom{n+k}{2k},
\]
which proves the lower bound.

For fixed \(k\),
\[
\binom{n+k}{2k}
\sim
\frac{n^{2k}}{(2k)!},
\qquad
\binom{2n}{2k}
\sim
\frac{2^{2k}n^{2k}}{(2k)!}.
\]
The two bounds therefore give
\[
|\mathtt{B}(2n,2k)|=\Theta_k(n^{2k}).
\]

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier constructs every member of the lower-bound family for \(1\le k\le4\) and \(k\le n\le10\). For each constructed word it records an explicit two-color shuffle certificate, verifies that both colored subsequences equal the claimed root, reconstructs the parameters from the zero-run vector, and checks that the number of distinct outputs is exactly
\[
\binom{n+k}{2k}.
\]

As an independent small-instance check, it exhaustively tests every binary word of even length through \(10\), computes whether it is a shuffle square by trying every half-size position subset, and reproduces the fixed-weight rows
\[
(1,1),
\]
\[
(1,4,1),
\]
\[
(1,10,10,1),
\]
\[
(1,19,42,19,1),
\]
and
\[
(1,31,128,128,31,1),
\]
which agree with the published table.

The finite computation checks the construction and bookkeeping. The all-\(n\), all-\(k\) bounds and the fixed-\(k\) asymptotic order follow from the proof above.

## Relationship to prior work
Grytczuk, Pawlik, and Pleszczyński define \(\mathtt{B}(2n,2k)\) and determine the exact case \(k=1\). They then explicitly ask for at least the asymptotic order of the other sequences \(|\mathtt{B}(2n,2k)|\) for fixed \(k\). The theorem above answers that request for every fixed \(k\).

He, Huang, Nam, and Thaper study the total number of binary shuffle squares of length \(2n\), proving a lower bound of order \(\binom{2n}{n}\), and obtain alphabet-size asymptotics for fixed word length. Those results aggregate all Hamming weights and do not imply a polynomial lower bound for any particular fixed weight.

Datko and Pawlik later study how many shuffle squares a fixed binary root generates and how many roots a shuffle square can have. Their one-\(\mathtt{1}\) root analysis is compatible with the construction above but does not state the fixed-weight counting order for the union over all roots.

The present lower bound is injective at the output-word level, so it avoids overcounting words that admit several shuffle decompositions or several roots.

## Limitations
For \(k\ge2\), the proof gives the correct exponent but leaves a factor of at most \(2^{2k}\) between the leading constants supplied by the two binomial bounds.

The result is specific to binary shuffle squares with fixed Hamming weight. It does not determine the asymptotic distribution of weights among all shuffle squares.

No claim is made about an exact formula for \(|\mathtt{B}(2n,2k)|\) when \(k\ge2\).

## References
1. J. Grytczuk, B. Pawlik, and M. Pleszczyński, “Variations on shuffle squares,” arXiv:2308.13882v1, first public 2023-08-26.
2. X. He, E. Huang, I. Nam, and R. Thaper, “Shuffle Squares and Reverse Shuffle Squares,” arXiv:2109.12455; European Journal of Combinatorics 116 (2024), 103883.
3. D. Datko and B. Pawlik, “Roots of Binary Shuffle Squares,” Symmetry 17 (2025), 305, DOI 10.3390/sym17020305.
