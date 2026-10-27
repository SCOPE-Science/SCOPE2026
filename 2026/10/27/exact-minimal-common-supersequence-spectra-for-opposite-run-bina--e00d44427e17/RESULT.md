# Exact minimal-common-supersequence spectra for opposite-run binary words

## Finding

For every integer \(m\geq 1\), consider the two binary strings
\[
A_m=0^m1^m,\qquad B_m=1^m0^m.
\]
A *minimal common supersequence* (MCS) is a binary word containing both strings as scattered subsequences such that deleting any one position destroys at least one of the two subsequence relations. Minimal does **not** mean shortest.

Every MCS has one of the two complementary forms
\[
U\,1^{m-j}\,V\quad\text{and}\quad \overline{U\,1^{m-j}\,V},
\qquad 0\leq j<m,
\]
where \(U\) has exactly \(m\) zeros and \(j\) ones and ends in zero, and \(V\) has exactly \(m\) zeros and \(j\) ones and begins in zero. Conversely, **each** word of either form is an MCS; all displayed words are distinct within their parameter classes. The bar means bitwise complementation.

Consequently, the entire attainable MCS length set is
\[
\{3m,3m+1,\ldots,4m-1\},
\]
and the number at length \(3m+j\) is exactly
\[
N_{m,j}=2\binom{m+j-1}{j}^{\!2},\qquad 0\leq j<m.
\]
There are exactly
\[
N_m=2\sum_{j=0}^{m-1}\binom{m+j-1}{j}^{\!2}
\sim\frac{16^m}{6\pi m}
\]
MCSs in total. The asymptotic proportion having maximum length \(4m-1\) is \(3/4\).

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), repeated exponent notation means concatenation, all occurrences are indexed by word position, and a subsequence may skip arbitrary positions but must preserve order. Embeddings are injections of the pattern positions into the host positions preserving their order and letters. A common supersequence is *deletion-minimal* if no single-symbol deletion leaves a common supersequence. Deletion-minimality agrees with the absence of **any** strictly shorter subsequence that is still a common supersequence, because any such shorter subsequence can be obtained by successive individual deletions, including a first deletion preserving the property.

The stated enumeration is for the **specific family** \((A_m,B_m)\), not arbitrary pairs or shortest-only supersequences. All claims quantify over every integer \(m\geq1\), and the finite verifier is supplementary, not the universal proof.

## Proof

**1. A necessary symbol count.** Choose one embedding of \(A_m\) and one of \(B_m\) in a common supersequence \(w\). If their selected zero positions intersect, let \(t\) be a shared zero. The \(m\) selected ones of \(B_m\) occur before \(t\), while the \(m\) selected ones of \(A_m\) occur after \(t\); therefore these are disjoint, and \(w\) contains at least \(2m\) ones. If the selected zero sets are disjoint, \(w\) contains at least \(2m\) zeros. So every common supersequence contains at least \(2m\) copies of **one** symbol.

For any chosen pair of embeddings in a *minimal* common supersequence, every position of \(w\) lies in their union: otherwise that unused position could be deleted while leaving both embeddings intact. Since the two embedded patterns each have \(m\) zeros and \(m\) ones, it follows that \(w\) contains no more than \(2m\) copies of either symbol. Combined with the preceding dichotomy, at least one symbol occurs **exactly** \(2m\) times, while both symbols occur at least \(m\) times.

**2. Simultaneous saturation cannot be minimal.** Suppose \(w\) has exactly \(2m\) zeros and exactly \(2m\) ones. Denote its ordered zero positions by \(z_1<\cdots<z_{2m}\) and its ordered one positions by \(o_1<\cdots<o_{2m}\). Since \(A_m\) is a subsequence, we can embed it using the first \(m\) zeros and the first \(m\) ones after \(z_m\). Since \(B_m\) is a subsequence, we can embed it using the first \(m\) ones and the first \(m\) zeros after \(o_m\). If \(z_m<o_m\), the position \(o_m\) is selected by **both** embeddings. If \(o_m<z_m\), the position \(z_m\) is selected by **both**. (The two middle positions cannot be equal because their letters differ.) Thus the union of these embeddings has fewer than \(4m\) positions, leaving an unused position of \(w\). This contradicts minimality. Hence a minimal word has exactly \(2m\) copies of one symbol and \(m+j\) of the other for a unique \(0\le j<m\).

**3. Factorization for the zero-rich orientation.** By binary complementation, it suffices to classify a minimal word with exactly \(2m\) zeros and \(m+j\) ones, where \(0\le j<m\). Mark its \(m\)th and \((m+1)\)st zeros. Write \(x\), \(y\), and \(z\) for the numbers of ones before the \(m\)th zero, strictly between the two marked zeros, and after the \((m+1)\)st zero, respectively. Thus \(x+y+z=m+j\).

The pattern \(A_m\) embeds if and only if at least \(m\) ones occur after the \(m\)th zero, i.e. \(y+z\ge m\). Likewise \(B_m\) embeds if and only if at least \(m\) ones occur before the \((m+1)\)st zero, i.e. \(x+y\ge m\). Together these are equivalent to \(x\le j\) and \(z\le j\).

If \(j=0\), these inequalities force \(x=z=0\) and \(y=m\), giving \(U1^mV\) with \(U=V=0^m\).

For \(j>0\), minimality forces \(x>0\) and \(z>0\). Indeed, if \(x=0\) and \(z>0\), deleting a one after the \((m+1)\)st zero leaves both inequalities true: \(y=x+y\ge m\) and \(y+z=m+j\ge m+1\). If \(x=z=0\), a central one can similarly be deleted, because \(y=m+j>m\). The case \(z=0\) is symmetric.

Now remove a one preceding the \(m\)th zero. This removal cannot disturb \(A_m\), so it must destroy \(B_m\). Therefore \(x+y=m\), implying \(z=j\). Symmetrically, removing a one following the \((m+1)\)st zero must destroy \(A_m\), so \(y+z=m\), implying \(x=j\). Therefore \(y=m-j\). The word necessarily factors as \(U1^{m-j}V\), where \(U\) contains its first \(m\) zeros and \(j\) initial ones and ends in zero, while \(V\) contains its last \(m\) zeros and \(j\) final ones and begins in zero.

Conversely, for every such factorization, the two displayed subsequence inequalities hold at equality. Deleting any zero leaves \(2m-1\) zeros and \(m+j<2m\) ones, violating the necessary symbol-count condition in step 1. Deleting any one in \(U\) destroys \(B_m\); deleting any one in \(V\) destroys \(A_m\); and deleting a one from the middle block destroys **both** because both inequalities held at equality. Thus every position is essential, proving minimality. Bit complementation gives the other orientation.

**4. Counts, endpoints, and asymptotics.** There are \(\binom{m+j-1}{j}\) possible prefixes \(U\): choose the positions of its \(j\) ones among the first \(m+j-1\) positions, reserving a trailing zero. Independently the same count applies to \(V\), with an initial zero reserved. The two orientations are disjoint because one has exactly \(2m\) zeros and the other exactly \(2m\) ones, while \(m+j<2m\). The indicated factorization is unique for each word, giving \(N_{m,j}\), and every \(0\le j<m\) is attained. In particular exactly two shortest MCSs of length \(3m\) exist, and exactly \(2\binom{2m-2}{m-1}^2\) longest MCSs of length \(4m-1\) exist.

For the asymptotics, let \(T_{m,j}=\binom{m+j-1}{j}^{2}\). For \(1\le j\le m-1\),
\[
\frac{T_{m,j-1}}{T_{m,j}}=\left(\frac{j}{m+j-1}\right)^2\le\frac14.
\]
For every fixed nonnegative integer \(k\), \(T_{m,m-1-k}/T_{m,m-1}\to4^{-k}\) as \(m\to\infty\). Dominated convergence using the uniform geometric bound therefore gives
\[
\frac{\sum_{j=0}^{m-1}T_{m,j}}{T_{m,m-1}}\longrightarrow\sum_{k=0}^{\infty}4^{-k}=\frac43.
\]
Since \(T_{m,m-1}=\binom{2m-2}{m-1}^2\sim16^{m-1}/(\pi m)\) by Stirling's formula, the total and longest-length proportion follow:
\[
N_m\sim 2\cdot\frac43\cdot\frac{16^{m-1}}{\pi m}
=\frac{16^m}{6\pi m},\qquad
\frac{N_{m,m-1}}{N_m}\longrightarrow\frac34.
\]

## Verification

The included standalone C++17 source `check_minimal.cxx` independently enumerates **all** binary words of candidate lengths \(3m\) through \(4m\) for each \(1\le m\le5\). For each word, it tests both subsequence embeddings and deletion of every position, separately tests the structural form claimed above, and compares the actual counts to the binomial formula. The independent direct-search totals are:

| \(m\) | MCS count by increasing length | Total |
|---:|---|---:|
| 1 | 2 | 2 |
| 2 | 2, 8 | 10 |
| 3 | 2, 18, 72 | 92 |
| 4 | 2, 32, 200, 800 | 1,034 |
| 5 | 2, 50, 450, 2,450, 9,800 | 12,752 |

Compile with `g++ -O3 -std=c++17 -Wall -Wextra -pedantic check_minimal.cxx -o check_minimal` and execute `./check_minimal`; successful completion prints `VERIFY_OK`. These finite checks do not prove the statement for arbitrary \(m\); the four-step proof above does.

## Relationship to prior work

Sopp, Liyanage, Gong, and Zhu (2026, arXiv:2603.22591v1) give algorithms for computing and enumerating the minimal common supersequences of **general** pairs of input strings. Their general enumeration machinery can be applied to this family, but it does not state the special factorization, exact **length-by-length** binomial-square spectrum, or its longest-length concentration as an explicit theorem. Earlier work by Irving and Fraser and the thesis of Fraser treat maximal common subsequences/minimal common supersequences and related algorithms; priority for equivalent unstated specializations remains an open bibliographic question.

The **total-count sequence** is **not novel as a naked integer sequence**: the identity \(N_m=2a(m-1)\), where OEIS A112029 lists \(a(n)=\sum_{k=0}^{n}\binom{n+k}{k}^{2}\), identifies the previously tabulated integers and their known asymptotic analysis. The contribution claimed here is specifically the complete classification of the MCS **words** for this natural pair and the refined per-length spectrum, not discovery of a new number sequence or first proof of the corresponding binomial-sum asymptotics.

## Limitations

The theorem addresses only opposite-order equal-length two-run binary inputs, not general words, unequal-run pairs, larger alphabets, or shortest-common-supersequence algorithms. The exact total numerical sequence is present in OEIS independently of this word interpretation. The 1994/1996 early paper was not fully available in this examination; although a substantively relevant thesis chapter and the 2026 preprint were inspected, an unlocated equivalent structural characterization in older work cannot be conclusively excluded. No independent scientific audit has been performed.

## References

- Braeden Sopp, Adiesha Liyanage, Mingyang Gong, and Binhai Zhu, *Computing and Enumerating Minimal Common Supersequences Between Two Strings*, arXiv:2603.22591v1, first submitted 23 March 2026. https://arxiv.org/abs/2603.22591
- R. W. Irving and C. B. Fraser, *Maximal Common Subsequences and Minimal Common Supersequences*, Combinatorial Pattern Matching (CPM), 1994.
- C. B. Fraser, *Subsequences and Supersequences of Strings*, PhD thesis, 1995, especially the chapter on minimal common supersequences.
- OEIS Foundation, *A112029: \(a(n)=\sum_{k=0}^{n}\binom{n+k}{k}^{2}\)*, originally recorded 2005. https://oeis.org/A112029
