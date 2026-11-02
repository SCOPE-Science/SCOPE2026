# Exact sandwich-subsequence profiles within binary Parikh-matrix classes

## Finding

Let \(A\ge2\), \(B\ge0\), and \(0\le C\le AB\) be integers. Let \(\mathcal P_{A,B,C}\) consist of the binary words containing \(A\) letters \(a\), \(B\) letters \(b\), and exactly \(C\) scattered occurrences of \(ab\). For \(w\in\mathcal P_{A,B,C}\), let \(I(w)\) be the number of letters \(b\) strictly between its first and last letters \(a\).

The complete bivariate distribution, before fixing \(C\), is
\[
\boxed{\sum_{|w|_a=A,\ |w|_b=B}u^{I(w)}z^{\binom{w}{ab}}
=\sum_{s=0}^{B}u^s z^s
\begin{bmatrix}s+A-2\\A-2\end{bmatrix}_{\!z}
\sum_{j=0}^{B-s}z^{Aj}.}
\tag{1}
\]
Here \(\binom{w}{ab}\) counts scattered occurrences of \(ab\), and the square brackets denote the ordinary Gaussian binomial polynomial. In particular, the number of words in \(\mathcal P_{A,B,C}\) having \(I(w)=s\) is the coefficient of \(z^C\) in the summand of (1) indexed by \(s\).

Write \(M=\min\{B,C,AB-C\}\). The *entire support* of this conditional distribution is
\[
\boxed{\{I(w):w\in\mathcal P_{A,B,C}\}=
\begin{cases}
\{s:0\le s\le M,\ s\equiv C\pmod2\},&A=2,\\
\{0\}\cup\{2,3,\ldots,M\},&A\ge3,\ A\mid C,\\
\{1\}\cup\{2,3,\ldots,M\},&A\ge3,\ A\nmid C.
\end{cases}}
\tag{2}
\]
An interval \(\{2,\ldots,M\}\) with \(M<2\) is understood to be empty. Every class is nonempty.

For every integer \(t\ge1\), a word contains the scattered pattern \(ab^t a\) exactly when \(I(w)\ge t\). Consequently a class contains **some** word having this pattern precisely when \(t\le M\), and its exact fraction of such words is
\[
\frac{\displaystyle\sum_{s=t}^{B}[z^C]\left(z^s
\begin{bmatrix}s+A-2\\A-2\end{bmatrix}_{\!z}
\sum_{j=0}^{B-s}z^{Aj}\right)}
{\displaystyle[z^C]\begin{bmatrix}A+B\\A\end{bmatrix}_{\!z}}.
\tag{3}
\]
A class has the pattern \(aba\) in **every** word exactly when \(A\nmid C\); for every \(t\ge2\), every nonempty class has a word avoiding \(ab^t a\).

## Assumptions and scope

Words are finite and linear, over the ordered alphabet \(\{a,b\}\). All subsequences are scattered, not contiguous. Exactly one letter is chosen for each position in a subsequence occurrence. The three nonnegative data \((A,B,C)\) are the complete binary Parikh-matrix parameters; \(A\ge2\) ensures a first and a last \(a\). The range \(0\le C\le AB\) is exactly the feasible range. The coefficient \([z^j]\) means extraction of the coefficient of \(z^j\) in an integer polynomial; no probabilistic or asymptotic limit is assumed.

The Gaussian polynomial is characterized, for \(0\le k\le n\), by \(\begin{bmatrix}n\\k\end{bmatrix}_{z}=\prod_{i=1}^{k}(1-z^{n-k+i})/(1-z^i)\), interpreted as a polynomial; the boundary cases are one. Formula (1) also provides a division-free computation via the usual Gaussian recurrence.

## Proof

**Gap encoding.** Every word with \(A\) letters \(a\) is uniquely
\[
w=b^{g_0}a b^{g_1}a\cdots a b^{g_{A-1}}a b^{g_A},
\qquad \sum_{j=0}^{A}g_j=B,
\]
where all gaps are nonnegative integers. Counting an \(ab\) pair by its \(b\)-endpoint and inspecting the first and last \(a\) gives
\[
\binom{w}{ab}=\sum_{j=1}^{A}j g_j,
\qquad I(w)=\sum_{j=1}^{A-1}g_j.
\tag{4}
\]
The reverse direction of this encoding is immediate: every nonnegative gap vector with total \(B\) defines exactly one word.

**The complete distribution.** Fix \(I(w)=s\). Set \(j=g_A\), which can take any integer value from zero through \(B-s\); then \(g_0=B-s-j\). The remaining gaps form a weak composition of \(s\) into \(A-1\) parts. Their weighted generating function is
\[
\sum_{g_1+\cdots+g_{A-1}=s}z^{\sum_{i=1}^{A-1}i g_i}
=z^s\begin{bmatrix}s+A-2\\A-2\end{bmatrix}_{z}.
\tag{5}
\]
Indeed, the left side is the complete homogeneous polynomial in the variables \(z,z^2,\ldots,z^{A-1}\), and the Gaussian identity follows either from the bounded-partition interpretation or the elementary recurrence for that polynomial. The final gap contributes \(z^{Aj}\). Multiplying and summing over \(s\) proves (1). Summing at \(u=1\) also gives the familiar complete \(ab\)-pair polynomial \(\begin{bmatrix}A+B\\A\end{bmatrix}_{z}\), proving the denominator of (3). Feasibility of each \(0\le C\le AB\) follows by moving an \(a\) one place past a \(b\), changing the pair count by one on a chain between the two sorted words.

**Sharp support.** Fix \(s\). If \(A=2\), the sole interior gap has size \(s\), hence (4) reduces to \(C=s+2j\), with \(0\le j\le B-s\). This is equivalent to \(s\le\min\{B,C,2B-C\}\) and \(s\equiv C\pmod2\), giving the first line of (2).

Suppose \(A\ge3\). At \(s=0\), (4) yields exactly \(C=Aj\), \(0\le j\le B\). At \(s=1\), its single interior \(b\) has a position strictly between the first and last \(a\), so exactly the values \(C=Aj+i\) with \(0\le j\le B-1\) and \(1\le i\le A-1\) are possible. These are precisely the nonmultiples of \(A\) within \([0,AB]\).

For \(s\ge2\), the weighted sum of \(s\) choices from \(1,\ldots,A-1\) realizes every integer from \(s\) to \((A-1)s\): start with \(s\) ones and distribute at most \(A-2\) increments to each one. At each fixed \(j\), the possible \(C\)'s therefore fill the integer interval \([Aj+s,Aj+(A-1)s]\). The intervals for successive \(j\)'s touch or overlap because \((A-2)s\ge A-1\). Their union for \(0\le j\le B-s\) is exactly \([s,AB-s]\), provided \(s\le B\). Equivalently, \(2\le s\le M\). This proves the remaining two cases of (2).

**Sandwich-pattern consequence.** A scattered \(ab^t a\) occurs if and only if at least \(t\) copies of \(b\) lie between the first and last \(a\), since the extreme two \(a\)'s may always be selected. Equations (1)–(2) then give both the existence threshold and (3). Finally (2) always allows \(I=0\) or \(I=1\), according to whether \(A\) divides \(C\); this proves the stated universal-quantifier conclusions.

## Verification

The standalone Python program `check.py` independently enumerates binary words by position choices, computes scattered \(ab\)-counts directly, and compares the full joint histogram with (1) evaluated through a separate Gaussian-binomial recurrence. It tests \(2\le A\le7\), \(0\le B\le7\): 48 parameter pairs, 12,825 individual words, 2,995 nonzero bivariate coefficients, and 804 conditional support spectra. It also makes 4,640 independent subsequence-embedding tests of the \(ab^t a\) equivalence. All tests passed; the exact output is in `check_output.txt`. These finite tests are corroboration; the gap-vector argument proves the arbitrary-parameter claim.

For example, \((A,B,C)=(3,4,6)\) has conditional histogram \(\{0:1,2:1,3:2,4:1\}\): interior count one is impossible, but all counts two through four occur. For \((A,B,C)=(2,3,3)\), only odd interior counts one and three occur.

## Relationship to prior work

Fazekas, Huang and Mercaş (2026) investigate binary Parikh-matrix languages and arithmetic criteria for subsequence universality; they also describe an additive approximation scheme for probabilities of fixed scattered patterns. The present exact coefficient distribution applies to a natural infinite family of sandwich patterns and classifies the entire support of a different internal-span statistic. Approximate fixed-pattern probabilities do not state formula (1), and all-pattern universality is distinct from occurrence of one designated sandwich pattern. The available abstract of that paper was inspected; its full text could not be inspected, so a special-case result in the body remains a priority risk.

Gaussian binomial coefficients and partition encodings for binary words are classical. Richomme (2026) gives geometric and partition-theoretic interpretations for binary two-binomial coefficients; Renard, Rigo and Whiteland (2025) study q-Parikh matrices. Neither an ordinary Gaussian-binomial marginal nor a q-deformation in itself specifies the added internal-gap statistic. The complete joint identity and exact support are the claims assessed here, not the known Gaussian recurrence or the known definition of Parikh matrices.

## Limitations

The theorem concerns one designated interior letter between the first and last instances of the other symbol, in binary words. It does not give an explicit closed-form distribution for arbitrary scattered patterns, nor an extension to ternary Parikh matrices. A self-contained proof and exhaustive small-parameter calculations support correctness; no independent mathematical audit was performed. The literature comparison includes some abstract-level sources, so an earlier equivalent formula or an unindexed specialization is not ruled out.

## References

1. Sz. Zs. Fazekas, X. Huang and R. Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, arXiv:2610.06717 (first public version October 5, 2026), https://arxiv.org/abs/2610.06717 ; DOI 10.4204/EPTCS.451.10.
2. G. Richomme, *On some 2-binomial coefficients of binary words: geometrical interpretation, partitions of integers, and fair words*, Theoretical Computer Science 1066 (2026) 115732, DOI 10.1016/j.tcs.2025.115732.
3. A. Renard, M. Rigo and M. A. Whiteland, *q-Parikh matrices and q-deformed binomial coefficients of words*, Discrete Mathematics 348 (2025) 114381, https://doi.org/10.1016/j.disc.2024.114381.
