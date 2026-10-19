# Exact privileged-factor complexity of periodic Zimin words

## Finding
For each integer \(n\ge 1\), define \(Z_1=1\) and \(Z_{n+1}=Z_n(n+1)Z_n\). Let \(W_n=Z_n^\omega\) be the right-infinite periodic word over the labeled alphabet \(\{1,\ldots,n\}\). For every integer \(\ell\ge1\), the numbers \(P_n(\ell)\) and \(A_n(\ell)\) of **distinct** palindromic and privileged length-\(\ell\) factors of \(W_n\) coincide, and are exactly
\[
P_n(\ell)=A_n(\ell)=
\begin{cases}
1,&\ell\text{ even},\\
\max\{1,n-\lfloor\log_2\ell\rfloor\},&\ell\text{ odd}.
\end{cases}
\]
Moreover, \(W_n\) is rich: every one of its finite factors has the maximal possible number of distinct palindromic subfactors (its length plus one, including the empty word). The cyclic word represented by \(Z_n\), with factors limited to one circumference \(N=2^n-1\), has exactly
\[
\frac{3N-1}{2}=3\cdot 2^{n-1}-2
\]
distinct nonempty privileged factors, and exactly the same number of distinct nonempty palindromic factors.

## Assumptions and scope
A *factor* is contiguous. Distinct factors are compared as words, not as occurrences. A nonempty *palindrome* reads the same in both directions. A word of length zero or one is *privileged*; a longer word is privileged precisely if it is a complete first return to a shorter privileged word, i.e., it begins and ends with that shorter word and has exactly those two occurrences (overlap is allowed). *Rich* means that a word of length \(t\) contains exactly \(t+1\) distinct palindromes including the empty word. The formula concerns all \(n\ge1\) and all positive factor lengths \(\ell\), even those exceeding the period. The circular count restricts length to \(1\le\ell\le N\). Symbols remain distinct labels: no binary projection is taken.

## Proof
**1. Positions and reflection.** Induction on the recursion shows that \(|Z_n|=N=2^n-1\), that \(Z_n\) is a palindrome, and that its one-based symbol at position \(i\in\{1,\ldots,N\}\) is \(1+\nu_2(i)\), where \(\nu_2\) denotes the exponent of two dividing a positive integer. Thus the positions labeled \(k<n\) are
\[
i=(2a+1)2^{k-1},\quad 0\le a<2^{n-k},
\]
and the single position labeled \(n\) is \(2^{n-1}\). The periodic sequence \(W_n\) is globally invariant under reflection about the symbol \(n\) and about the seam between consecutive periods, since \(Z_n\) is a palindrome of odd length.

**2. Classification of odd palindromes.** An odd-length palindrome has a central letter \(k\). For \(k<n\), every occurrence of letter \(k\) has a palindrome centered there of every radius \(r\) with \(0\le r<2^{k-1}\). Indeed, at distance \(1\le j<2^{k-1}\), the two neighboring symbols are both \(1+\nu_2(j)\). The palindrome fails at radius \(2^{k-1}\): the two sites at that distance correspond to the consecutive multiples \(a2^k\) and \((a+1)2^k\), whose symbols differ. At a period boundary, the zero or \(2^n\) index instead wraps to a site labeled \(1\), and still differs from the other neighbor. Thus a center of rank \(k<n\) supports **exactly** the odd palindromic lengths \(1,3,\ldots,2^k-1\). All centers of the same rank give the same palindrome at a fixed permissible length; different ranks give different central letters. The unique rank-\(n\) center is globally a reflection center, hence supports every odd length. At odd \(\ell\ge1\), a rank \(k<n\) contributes exactly when \(\ell\le2^k-1\); adding the rank-\(n\) center yields \(\max\{1,n-\lfloor\log_2\ell\rfloor\}\) different palindromes.

**3. Classification of even palindromes.** Every adjacent pair of letters inside \(Z_n\) has one odd-positioned letter \(1\) and one even-positioned letter at least \(2\). The only equal adjacent letters in the periodic word are therefore the two \(1\)'s on either side of the period seam. Every even palindrome must be centered at such a seam. Global reflection about the seam gives one even palindrome of each positive even length; periodicity makes the word independent of the choice of seam. There are no others. This proves the formula for \(P_n\).

**4. Complete returns and richness.** We prove that every complete first return to a palindromic factor of \(W_n\) is itself palindromic. First consider an odd palindrome whose central letter is \(k<n\), of radius \(r\le2^{k-1}-1\). Its occurrences have precisely the centers labeled \(k\). Consecutive such centers are separated by \(2^k\), except for one gap of \(2^k-1\) across the period seam. For a regular gap, the midpoint has symbol rank at least \(k+1\). The complete-return factor is centered at this midpoint and extends \(2^{k-1}+r\le2^k-1\) to either side; the same valuation symmetry as in step 2 makes it a palindrome. For the exceptional gap, its midpoint is the period seam, a global reflection center, so this complete return is also palindromic. The unique rank-\(n\) central letter gives one occurrence of each of its odd palindromes per period; the complete return between consecutive occurrences is centered at a seam and is palindromic. Finally, any even palindrome occurs once per period, centered at a seam, and its complete return between two successive seams is centered at a rank-\(n\) letter and is palindromic. These exhaust the palindromes and their complete first returns.

By the complete-return characterization of rich words (Glen, Justin, Widmer, and Zamboni, Theorem 2.14), every finite factor of \(W_n\) is rich. By the characterization that a word is rich exactly when its privileged factors are its palindromic factors (Peltomäki, Proposition 3.6), the privileged and palindromic factor sets agree. Therefore \(A_n(\ell)=P_n(\ell)\) for every positive \(\ell\).

**5. One-circumference count.** For each rank \(k\in\{1,\ldots,n\}\), there is one distinct odd circular palindrome at each of the \(2^{k-1}\) lengths \(1,3,\ldots,2^k-1\). Thus there are \(\sum_{k=1}^n2^{k-1}=N\) distinct odd palindromes of length at most \(N\). Since \(N\) is odd, there are exactly \((N-1)/2\) positive even lengths not exceeding \(N\), each contributing one palindrome. The total is \((3N-1)/2\). All these words occur circularly in \(Z_n\), and richness makes exactly the same count valid for privileged words.

## Verification
The standalone `verify.py` independently computes palindromic factor sets by direct substring testing and by outward center expansion for all orders \(1\le n\le8\) and all \(1\le\ell\le3(2^n-1)\). It compares the sets, not just their sizes, and then compares both counts with the closed formula. For \(1\le n\le7\), it also independently evaluates the recursive complete-first-return definition of privileged words for every distinct circular factor of length at most \(2^n-1\), testing equality of the privileged and palindromic sets and the total-count formula. Run `python verify.py` in a directory containing this file. These are finite checks of a separately supplied proof; they do not certify its unrestricted quantifiers by themselves.

## Relationship to prior work
Glen, Justin, Widmer, and Zamboni (2008) established the complete-return characterization of rich words and general structural criteria for periodic richness. Peltomäki (2012) introduced the relevant privileged-complexity framework and proved that richness is equivalent to coincidence of privileged and palindromic factors; the article also covers strict episturmian words, whose constant odd-length complexity differs from the present dyadic staircase. Schaeffer and Shallit (2015) gave general logical and automata-based methods for detecting special factors in automatic sequences, including privileged factors. Those broad results provide context and tools, but the inspected texts do not state the all-length Zimin-periodic complexity formula, the classification of its centers, or the derived exact one-circumference total. The complete-return and privileged/rich equivalences used above are credited, not claimed as new.

## Limitations
The theorem is for the distinctly labeled finite Zimin word repeated periodically, not for the nonperiodic infinite ruler word, not for morphic images with letter identifications, and not for arbitrary palindromic periods. The historical-originality comparison is based on accessible literature and mathematical-record searches; an unindexed prior equivalent formula remains possible. The proof relies on established published characterizations of rich and privileged words, whose statements are cited explicitly. No independent scientific audit has been performed.

## References
1. A. Glen, J. Justin, S. Widmer, and L. Q. Zamboni, *Palindromic Richness*, arXiv:0801.1656, first publicly posted 2008-01-10, Theorems 2.14 and 3.1. https://arxiv.org/abs/0801.1656
2. J. Peltomäki, *Introducing Privileged Words: Privileged Complexity of Sturmian Words*, arXiv:1210.3146, first publicly posted 2012-10-11, Proposition 3.6 and Section 5. https://arxiv.org/abs/1210.3146
3. L. Schaeffer and J. Shallit, *Closed, Palindromic, Rich, Privileged, Trapezoidal, and Balanced Words in Automatic Sequences*, arXiv:1508.02074, first publicly posted 2015-08-09. https://arxiv.org/abs/1508.02074
4. S. Fischler, *Palindromic Prefixes and Episturmian Words*, arXiv:math/0501420, first publicly posted 2005-01-24. https://arxiv.org/abs/math/0501420
