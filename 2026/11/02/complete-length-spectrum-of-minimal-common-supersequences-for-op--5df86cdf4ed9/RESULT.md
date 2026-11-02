# Complete length spectrum of minimal common supersequences for opposite binary blocks

## Finding

Let \(m\ge1\), and consider the two binary words \(u_m=0^m1^m\) and \(v_m=1^m0^m\). A *minimal common supersequence* is a word containing both as scattered subsequences, but losing this property after deletion of any one position. If \(N_m(\ell)\) is the number of **distinct** minimal common supersequences of length \(\ell\), then

\[
N_m(\ell)=\begin{cases}
2\binom{m+j-1}{j}^{2},&\ell=3m+j,\quad 0\le j\le m-1,\\
0,&\text{otherwise}.
\end{cases}
\]

Thus the possible lengths form exactly the interval from \(3m\) to \(4m-1\), and the complete length-generating polynomial is

\[
F_m(z)=2\sum_{j=0}^{m-1}\binom{m+j-1}{j}^{2}z^{3m+j}.
\]

For a uniformly selected minimal common supersequence, the deficit from the maximum possible length converges in distribution to a geometric random variable:

\[
\lim_{m\to\infty}\Pr(4m-1-|W_m|=h)=\frac34\,4^{-h}\quad(h=0,1,2,\ldots).
\]

The total number is \(2\,\mathrm{A112029}(m-1)\), where A112029 is the previously tabulated binomial sum, and in particular

\[
F_m(1)\sim\frac{16^m}{6\pi m}.
\]

The binomial sum and its ordinary arithmetic asymptotic are known as OEIS A112029. The contribution here is their interpretation as a complete, explicitly classified minimal-supersequence length spectrum, including the limiting length-deficit law.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), and \(m\) ranges over all positive integers. A scattered subsequence retains symbol order but need not consist of contiguous positions. Minimality is with respect to deletion of an arbitrary single symbol (equivalently, no proper subsequence remains a common supersequence), *not* minimum length. Words with the same symbols in the same order are counted once, regardless of how many embeddings they admit.

## Proof

**1. Canonical embeddings and a dichotomy.** In any common supersequence \(w\), an embedding of \(u_m\) uses the first \(m\) zeros and the last \(m\) ones; an embedding of \(v_m\) uses the first \(m\) ones and the last \(m\) zeros. These are genuine embeddings: the existence of any embedding forces the first \(m\) zeros to precede the last \(m\) ones, and symmetrically for the other word. If \(w\) is minimal, every symbol position must belong to the union of these two fixed embeddings, or it could be deleted without destroying either. Consequently \(w\) contains at most \(2m\) occurrences of either symbol.

If it contained fewer than \(2m\) zeros and fewer than \(2m\) ones, the two embeddings would share a zero (because the first and last \(m\) zeros overlap) and also share a one. The shared zero must precede the shared one in the \(u_m\) embedding, but the shared one must precede the shared zero in the \(v_m\) embedding. This is impossible. Therefore every minimal common supersequence has **exactly \(2m\) occurrences of at least one symbol**.

**2. Classification in the \(2m\)-zero branch.** Suppose \(w\) has exactly \(2m\) zeros. Split it uniquely as \(w=L1^cR\), where \(L\) ends at the \(m\)-th zero and \(R\) begins at the \((m+1)\)-st zero; \(c\ge0\) is the number of ones strictly between those two zeros. Let \(a\) count the ones in \(L\) and \(b\) those in \(R\). Each of \(L,R\) has exactly \(m\) zeros. The two subsequence requirements are equivalent to

\[
a+c\ge m,\qquad c+b\ge m.
\]

Minimality forces \(a,b\le m-1\): if \(b\ge m\), deleting any zero in \(L\) would leave \(m\) zeros before \(m\) trailing ones and would not affect the other input's embedding. The case \(a\ge m\) is symmetric, deleting a zero in \(R\).

In fact both displayed inequalities must be equalities. If \(a+c>m\) and \(a>0\), delete a one in \(L\): it cannot be used by \(u_m\), and enough ones remain before \(R\) to embed \(v_m\). If \(a=0\), then \(c>m\), and deleting a central one preserves both inputs. Hence \(a+c=m\); symmetrically \(c+b=m\). Consequently

\[
a=b=j,\qquad c=m-j,\qquad 0\le j\le m-1.
\]

Conversely, any word with \(m\) zeros and \(j\) ones in \(L\), ending in zero, then \(m-j\) central ones, then \(m\) zeros and \(j\) ones in \(R\), beginning in zero, is minimal. Deleting a one in \(L\) or in the central block removes the necessary \(m\) ones before \(R\); deleting a one in the central block or in \(R\) removes the necessary \(m\) ones after \(L\). Deleting a zero from \(L\) requires using the first zero of \(R\) to finish the leading \(m\) zeros of \(u_m\), after which only \(j<m\) ones remain. Deleting a zero from \(R\) analogously leaves fewer than \(m\) ones before the first usable block of \(m\) trailing zeros of \(v_m\). Every deletion therefore destroys at least one input.

The positions of the \(j\) ones in \(L\) can be selected in \(\binom{m+j-1}{j}\) ways, because the final position is zero. The same number of choices holds for \(R\), whose first position is zero. This branch therefore contains exactly \(\binom{m+j-1}{j}^2\) words of length \(3m+j\).

**3. Complementation.** Interchanging zeros and ones gives an equally large branch with exactly \(2m\) ones. The branches are disjoint: words in the first have only \(m+j\le2m-1\) ones. Every minimal common supersequence belongs to one of the branches by Step 1. Doubling the count proves the formula and the entire length spectrum.

**4. Length-deficit limit.** Let \(a_{m,j}=\binom{m+j-1}{j}^2\). For \(1\le j\le m-1\),

\[
\frac{a_{m,j-1}}{a_{m,j}}=\left(\frac{j}{m+j-1}\right)^2\le\frac14.
\]

For each fixed \(h\ge0\), \(a_{m,m-1-h}/a_{m,m-1}\to4^{-h}\). The ratio bound yields a summable domination, so \(\sum_{j=0}^{m-1}a_{m,j}/a_{m,m-1}\to4/3\). Consequently the top-deficit probability converges to \((3/4)4^{-h}\). Stirling's formula gives \(a_{m,m-1}\sim16^{m-1}/(\pi(m-1))\), and therefore \(F_m(1)\sim16^m/(6\pi m)\).

## Verification

Run `python verify.py` with Python 3 and no external dependencies. The program constructs every word described by the formula, independently tests the subsequence and single-deletion conditions, and compares against unrestricted exhaustive binary-word enumeration for \(m=1,2,3,4\). For \(m=5\), it exhausts every word meeting the analytically proven necessary multiplicity condition. The observed totals are \(2,10,92,1034,12752\) with the full length histograms recorded in `verification_output.txt`. Those finite checks corroborate the proof; they do not establish the infinite-parameter statement by themselves.

## Relationship to prior work

Sopp, Liyanage, Gong and Zhu (2026) characterize minimal common supersequences and enumerate them by a general graph construction with polynomial preprocessing and delay; their Sections 3–5 do not give the present explicit opposite-block length spectrum. Lin (2026) proves general upper bounds on counts of minimal common supersequences of a fixed length, which do not force these equalities. Alon and coauthors (2022) provide bounds on shortest common supersequence multiplicities. Fraser's 1995 thesis develops dynamic programming for the lengths of minimal common supersequences, not this exact family distribution. OEIS A112029 already contains the corresponding binomial sum and its arithmetic asymptotic; neither is claimed as a newly discovered integer identity. The explicit interpretation, classification and geometric length law are the proposed new contribution.

## Limitations

The theorem is specialized to the equal-length opposite two-block pair; it does not count minimal common supersequences of arbitrary input strings or establish maximum multiplicity over all pairs. The mathematical analysis is self-contained, but novelty is subject to the possibility of earlier unindexed special-family enumerations. No independent mathematical audit has been performed.

## References

- B. Sopp, A. Liyanage, M. Gong and B. Zhu, *Computing and Enumerating Minimal Common Supersequences Between Two Strings*, arXiv:2603.22591v1, first public 2026-03-23. https://arxiv.org/abs/2603.22591
- A. D. Lin, *Lower Bounds for all List-Decodable Deletion Codes*, arXiv:2609.26650v1, first public 2026-09-22. https://arxiv.org/abs/2609.26650
- N. Alon, G. Bourla, B. Graham, X. He and N. Kravitz, *Logarithmically larger deletion codes of all distances*, arXiv:2209.11882v1, first public 2022-09-23. https://arxiv.org/abs/2209.11882
- C. B. Fraser, *Subsequences and Supersequences of Strings*, PhD thesis, University of Glasgow, 1995, Chapter 6. https://theses.gla.ac.uk/74575/1/10992195.pdf
- OEIS Foundation, A112029, *Sum of squares of binomial coefficients*. https://oeis.org/A112029
