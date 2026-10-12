# Exact ambiguity one coefficient short of right-bounded-block reconstruction
## Finding
Fix a binary word of known length \(n\) with
\[
m=|w|_a,\qquad 1\le m\le n-m,
\]
and write its run decomposition as
\[
w=b^{s_0}ab^{s_1}a\cdots ab^{s_m},
\qquad s_j\in\mathbb N_0.
\]
Suppose the available right-bounded-block data are one coefficient short of the standard worst-case family:
\[
\binom{w}{a},\binom{w}{ab},\binom{w}{a^2b},\ldots,\binom{w}{a^{m-1}b}.
\]
Because \(n\) and \(m\) are known, \(\binom{w}{b}=n-m\) is known as well.

Define
\[
T_{\rm even}(s)=
\min_{\substack{0\le j\le m\\ j\ {\rm even}}}
\left\lfloor\frac{s_j}{\binom mj}\right\rfloor,
\qquad
T_{\rm odd}(s)=
\min_{\substack{0\le j\le m\\ j\ {\rm odd}}}
\left\lfloor\frac{s_j}{\binom mj}\right\rfloor.
\]
Then the number of length-\(n\) binary words with exactly \(m\) letters \(a\) and exactly the same truncated right-bounded-block data is
\[
1+T_{\rm even}(s)+T_{\rm odd}(s).
\]

More precisely, every compatible word has run vector
\[
s+t\,v,\qquad
v_j=(-1)^j\binom mj,
\]
for a unique integer
\[
-T_{\rm even}(s)\le t\le T_{\rm odd}(s).
\]

Consequently the truncated data reconstruct \(w\) uniquely if and only if
\[
T_{\rm even}(s)=T_{\rm odd}(s)=0.
\]
Equivalently, there is an even index \(j\) with
\[
s_j<\binom mj
\]
and an odd index \(j\) with the same strict inequality.

## Assumptions and scope
The binomial coefficient
\[
\binom{w}{u}
\]
denotes the number of occurrences of \(u\) as a scattered factor, or subsequence, of \(w\).

The primary reconstruction scheme assumes that \(n\) is known, takes \(m=|w|_a\le|w|_b\), and represents the word by the \(m+1\) nonnegative exponents in the displayed run decomposition. It proves reconstruction from the family ending at \(a^m b\). The claim here analyzes exactly the immediately preceding layer, where \(a^m b\) is omitted.

No claim is made here about arbitrary earlier truncations ending at \(a^\ell b\) with \(\ell<m-1\), nor about nonbinary alphabets.

## Proof
For \(0\le\ell\le m\), the right-bounded-block coefficient is
\[
y_\ell=\binom{w}{a^\ell b}
=
\sum_{j=\ell}^{m}\binom j\ell s_j.
\]
For \(\ell=0\), this is simply
\[
y_0=\sum_{j=0}^{m}s_j=n-m.
\]
Thus the one-short data determine the \(m\) linear equations
\[
y_\ell=
\sum_{j=\ell}^{m}\binom j\ell s_j,
\qquad 0\le\ell\le m-1.
\]

Let \(P\) be the \(m\times(m+1)\) matrix with entries
\[
P_{\ell j}=\binom j\ell.
\]
Its first \(m\) columns form a triangular matrix with diagonal entries \(1\), so
\[
\operatorname{rank}P=m.
\]
Hence its nullspace is one-dimensional.

Set
\[
v_j=(-1)^j\binom mj.
\]
For every \(0\le\ell<m\),
\[
\begin{aligned}
\sum_{j=\ell}^{m}\binom j\ell v_j
&=
\sum_{j=\ell}^{m}
(-1)^j\binom mj\binom j\ell\\
&=
\binom m\ell
\sum_{r=0}^{m-\ell}
(-1)^{r+\ell}\binom{m-\ell}{r}\\
&=0.
\end{aligned}
\]
So \(v\) spans the nullspace. Moreover
\[
v_m=(-1)^m,
\]
therefore \(v\) is primitive in the integer lattice. It follows that two integer run vectors give the same truncated data if and only if their difference is
\[
t\,v
\]
for an integer \(t\).

It remains only to impose nonnegativity. If \(t\ge0\), the even coordinates increase and the odd coordinates decrease, so feasibility is exactly
\[
t\le
\min_{\substack{j\ {\rm odd}}}
\left\lfloor\frac{s_j}{\binom mj}\right\rfloor
=
T_{\rm odd}(s).
\]
If \(t=-u\le0\), the odd coordinates increase and the even coordinates decrease, so feasibility is exactly
\[
u\le T_{\rm even}(s).
\]
Therefore the complete feasible set of integer parameters is
\[
-T_{\rm even}(s),\ldots,T_{\rm odd}(s),
\]
which has cardinality
\[
1+T_{\rm even}(s)+T_{\rm odd}(s).
\]
The uniqueness criterion follows immediately.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The first verification engine works purely with run vectors. For every
\[
1\le m\le8,\qquad 0\le |w|_b\le9,
\]
it enumerates every nonnegative run vector with the prescribed total number of \(b\)'s, groups vectors by all truncated Pascal moments, and checks that each fibre is exactly the predicted integer interval
\[
s+t\,v.
\]

A second engine enumerates binary words directly through length \(12\). It computes every coefficient
\[
\binom{w}{a^\ell b}
\]
using generic subsequence dynamic programming, not the run-vector formula, groups words by the truncated data, and verifies the exact ambiguity count and the predicted compatible run vectors.

The verifier separately checks the binomial annihilation identity for all \(1\le m\le20\). These finite checks supplement the symbolic proof; they are not used to infer the infinite statement.

## Relationship to prior work
Fleischmann, Lejeune, Manea, Nowotka, and Rigo derive the run-vector formula
\[
\binom{w}{a^\ell b}
=
\sum_j\binom j\ell s_j
\]
and show that at most
\[
\min(|w|_a,|w|_b)+1
\]
right-bounded-block coefficients reconstruct a binary word. Their treatment explicitly says that a full characterization of unique values is unavailable for arbitrary parameters, and their conclusion identifies better uniqueness criteria as useful for understanding when fewer than the worst-case number of coefficients suffices.

The present result gives an exact answer for the first layer below that worst case: after dropping only the terminal coefficient, the entire collision class is a one-dimensional integer interval in the alternating binomial direction. It gives not only a uniqueness test but the exact number of compatible words.

Later work on binary Simon congruence studies equality of sets of scattered factors rather than these multiplicity measurements. Recent \(k\)-deck work studies complete fixed-length subsequence-count vectors and their affine dimensions; it does not state this restricted right-bounded-block fibre formula.

Targeted searches for right-bounded-block uniqueness, alternating-binomial kernels, the one-coefficient-short truncation, and exact collision counts did not locate a covering published statement.

## Limitations
The theorem treats only the top truncated layer
\[
a,ab,\ldots,a^{m-1}b.
\]
For deeper truncations there are more null directions and the nonnegative integer fibres can have substantially richer geometry.

The result assumes the word length and \(m=|w|_a\) are known, as in the source reconstruction setup. It does not claim a smallest possible measurement set over all possible scattered factors.

An unindexed note or unpublished calculation could contain the same Pascal-kernel observation.

## References
1. P. Fleischmann, M. Lejeune, F. Manea, D. Nowotka, and M. Rigo, “Reconstructing Words from Right-Bounded-Block Words,” arXiv:2001.11218v1, first public version 2020-01-30; DLT 2020, DOI 10.1007/978-3-030-48516-0_8; long version in International Journal of Foundations of Computer Science 32(6), DOI 10.1142/S0129054121420016.
2. P. Fleischmann, J. Höfer, A. Huch, and D. Nowotka, “\(\alpha\)-\(\beta\)-Factorization and the Binary Case of Simon's Congruence,” arXiv:2306.14192v1, 2023.
