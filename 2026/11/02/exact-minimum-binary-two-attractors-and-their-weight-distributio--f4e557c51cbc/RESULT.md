# Exact minimum binary two-attractors and their weight distribution

## Finding

For every nonempty finite binary word \(w\), let \(\gamma_2(w)\) be the minimum number of marked positions needed so that every distinct contiguous factor of length at most two has an occurrence meeting a marked position. The marked positions belong to the **linear** word, with no wraparound factors.

**Theorem.** Every such word satisfies \(\gamma_2(w)\in\{1,2,3\}\). More precisely,

\[
\gamma_2(w)=\begin{cases}
1,&w\text{ is constant},\\
3,&w\in\mathcal E,\\
2,&\text{otherwise},
\end{cases}
\]

where the two disjoint exceptional families are

\[
\mathcal E=\bigl\{0^a(10)^b1^c,\ 1^a(01)^b0^c:\ a,c\ge2,\ b\ge1\bigr\}.
\]

For integers \(n\ge1\) and \(0\le t\le n\), the exact number of exceptional indexed length-\(n\) words with \(t\) ones is

\[
N_3(n,t)=2\max\{0,\min(t-2,n-t-2)\}.
\]

Their bivariate ordinary generating function and length-only count are

\[
\sum_{n\ge1}\sum_{t=0}^n N_3(n,t)z^nu^t
=\frac{2z^6u^3}{(1-z)(1-zu)(1-z^2u)},
\]

\[
N_3(n)=\begin{cases}0,&1\le n\le5,\\
2\left\lfloor\dfrac{(n-4)^2}{4}\right\rfloor,&n\ge6.
\end{cases}
\]

There are exactly two constant binary words at each length, so the complete numbers of words with optimal two-attractor sizes one, two and three are \(2\), \(2^n-2-N_3(n)\) and \(N_3(n)\), respectively. In particular, for a uniform binary word of length \(n\), the probability of requiring three positions is \(\Theta(n^2 2^{-n})\).

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), the input word is indexed and linear, and \(n\ge1\). Both length-one and length-two factors must be covered. An occurrence \(w_i\cdots w_j\) is covered if the inclusive interval \([i,j]\) meets the marked set. Positions and factor occurrences are counted with multiplicity for coverage purposes, but the requirements distinguish factor **types** only. This is the usual non-sharp \(2\)-attractor, not the sharp two-factor variant or the unrestricted full-length string attractor.

## Proof

**1. Coverage by digram pairs.** Let \(D(w)\subseteq\{00,01,10,11\}\) be the set of distinct length-two factors. A marked interior position meets at most the two adjacent digrams, corresponding to a contiguous length-three factor. Thus a position can simultaneously cover two distinct digram types exactly when that length-three factor is among

\[
001,\ 100,\ 010,\ 101,\ 011,\ 110.
\]

The associated unordered pairs of digram types are, respectively,

\[
\{00,01\},\quad\{00,10\},\quad\{01,10\},\quad
\{01,10\},\quad\{01,11\},\quad\{10,11\}.
\]

The pair \(\{00,11\}\) is never covered by one position.

**2. When a digram is absent, two marks suffice.** If the word is nonconstant and \(00\notin D(w)\), either \(11\) is absent as well, giving an alternating word, or a run of at least two ones meets an adjacent zero. In the latter case there is an occurrence of \(011\) or \(110\); mark its central one and a zero adjacent to an occurrence of the other transition type, if that transition occurs. These two marks cover every present digram and both letters. If the other transition does not occur, any zero and the central one suffice. The case \(11\notin D(w)\) is symmetric. If both constant digrams occur but one transition type is absent, the word consists of a single zero run followed by a single one run, or vice versa; marking the two positions across their boundary covers every present factor of length at most two. This proves \(\gamma_2(w)\le2\) whenever \(D(w)\ne\{00,01,10,11\}\).

For the remaining case suppose all four digram types appear. Two selected positions can cover all four only if each covers two distinct types and these pairs are disjoint. The only disjoint pairings from step 1 are

\[
\{00,01\}\mid\{10,11\},\qquad
\{00,10\}\mid\{01,11\}.
\]

Consequently a two-position attractor exists **if and only if** the word contains both \(001\) and \(110\), or contains both \(100\) and \(011\). The two central letters of the witnessing three-letter factors are different, so the selected marks also cover both length-one factors. This proves both necessity and sufficiency.

**3. Classification of the exceptions.** A word with all four digrams but no two-position attractor must avoid at least one factor in each of \(\{001,110\}\) and \(\{100,011\}\). Avoiding both \(001\) and \(100\) is impossible: the word contains \(00\) and a one, and a maximal zero run of length at least two must meet a one at some boundary, producing one of these two factors. Likewise, avoiding both \(110\) and \(011\) is impossible. Thus the only possibilities are:

- Both \(100\) and \(110\) are absent. Every double-zero run is before every one, while every double-one run is after every zero. Since all four digrams occur, the word has an initial zero run of length at least two, an alternating interior containing at least one \(10\), and a final one run of length at least two. It is exactly \(0^a(10)^b1^c\), with \(a,c\ge2\) and \(b\ge1\).
- Both \(001\) and \(011\) are absent. Interchanging the letters gives exactly \(1^a(01)^b0^c\) under the same parameter restrictions.

Conversely these two families contain all four digrams but have neither of the requisite paired witnesses, so no two marks suffice. Every word in the first family contains an \(010\) factor, and each in the second contains a \(101\) factor. Marking the central position of that alternating triple covers both transition digrams; one mark in a \(00\) occurrence and one in an \(11\) occurrence cover the remaining digrams and both letters. Hence three marks suffice. For a nonconstant word one mark cannot cover both singleton letter types, establishing the asserted trichotomy; a constant nonempty word needs exactly one mark.

**4. Composition refinement.** In the first exceptional family, a word with length \(n\) and exactly \(t\) ones has \(t=b+c\) and \(n-t=a+b\). Thus for each integer \(b\) in the range

\[
1\le b\le\min(t-2,n-t-2)
\]

there is exactly one choice of \(a=n-t-b\) and \(c=t-b\). The second family gives the same count, and the families are disjoint because their initial letters differ. This proves \(N_3(n,t)\). Summing the independent choices of \(a,c\ge2\) and \(b\ge1\) proves the displayed rational generating function. At \(u=1\), its coefficient is \(2\sum_{b=1}^{\lfloor(n-4)/2\rfloor}(n-2b-3)\), which evaluates to the stated length-only formula. All enumerative consequences follow.

## Verification

The included standalone `verification/verify.py` independently generates all nonempty binary words of lengths one through fifteen, calculates the exact minimum two-attractor size directly from the factor-occurrence/position-incidence matrix, and compares it to the exceptional-language classification. It also checks the complete length and weight distributions and independently checks the coefficient formula through length 299. The verifier reports `VERIFY_OK exhaustive_words=65534 coefficients_through_n=299`. This finite computation corroborates but does not replace the all-length argument above.

Run from the extracted package root with `python3 verification/verify.py`. The program uses only the Python standard library.

## Relationship to prior work

Kempa, Policriti, Prezza and Rotenberg (2018, arXiv:1803.01695) define ordinary and sharp \(k\)-attractors and develop algorithms based on truncated suffix trees; their sharp length-two case reduces to edge cover. Fuchs and Whittington (2023, arXiv:2304.06523; STACS 2024) prove that ordinary \(2\)-attractor optimization is NP-complete over unrestricted, instance-dependent alphabets. Their construction uses many distinct symbols and does not yield a binary-language classification. Mantaci, Restivo, Romana, Rosone and Sciortino (2021) analyze full-length string attractors and selected infinite word families rather than the complete length-two binary spectrum.

The present theorem isolates a nontrivial exact fixed-alphabet boundary of the general optimization problem. Its structural two-family classification, exact composition distribution and rational generating function are not consequences of the general hardness statement, the truncated-suffix-tree algorithm or a result about unrestricted attractors.

## Limitations

The result concerns linear, indexed binary words and coverage of factors of length **at most two**; it does not classify circular attractors, larger alphabets, larger factor-length cutoffs or full-length string attractors. Computational verification is finite, not an all-length certificate. Priority relative to unpublished or unindexed equivalent classifications remains open; no independent scientific audit is claimed.

## References

1. D. Kempa, A. Policriti, N. Prezza and E. Rotenberg, *String Attractors: Verification and Optimization*, arXiv:1803.01695 (first public version March 5, 2018). https://arxiv.org/abs/1803.01695
2. J. Fuchs and P. Whittington, *The 2-Attractor Problem Is NP-Complete*, arXiv:2304.06523 (first public version April 13, 2023), STACS 2024. https://arxiv.org/abs/2304.06523
3. S. Mantaci, A. Restivo, G. Romana, G. Rosone and M. Sciortino, *A Combinatorial View on String Attractors*, Theoretical Computer Science 850 (2021), 236–248. https://pages.di.unipi.it/rosone/Papers/MRRRS_TCS2021.pdf
