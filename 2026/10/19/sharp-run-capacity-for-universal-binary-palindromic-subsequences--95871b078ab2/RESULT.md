# Sharp run capacity for universal binary palindromic subsequences

## Finding
Fix the binary alphabet \(\{0,1\}\). For a nonempty finite word \(w\), write \(R(w)\) for its number of maximal nonempty constant-letter runs. Let \(\mathcal P_k\) be the set of all binary palindromes of length \(k\), and say that \(w\) is *palindrome-subsequence universal of order* \(k\) when every member of \(\mathcal P_k\) occurs in \(w\) as an order-preserving, not necessarily contiguous, subsequence.

**Theorem.** For every integer \(k\ge1\), the minimum run count of any palindrome-subsequence-universal word of order \(k\) is precisely
\[
\boxed{2\left\lceil\frac{k}{2}\right\rceil}.
\]
The smallest possible length of such a word is precisely \(2k\); a word achieves **both** minima simultaneously. Explicit witnesses are
\[
W_{2m}=(0011)^m\quad(m\ge1),\qquad
W_{2m+1}=(0011)^m01\quad(m\ge0).
\]
In particular, if \(\pi(w)\) is the greatest order of palindrome-subsequence universality of \(w\) (zero when it does not contain both letters), then for every \(r\ge1\),
\[
\boxed{\max_{R(w)=r}\pi(w)=2\left\lfloor\frac r2\right\rfloor}.
\]
All maxima range over finite binary words of arbitrary length with **exactly** the stated number of runs. The run-minimum is sharper by one run than ordinary full-alphabet subsequence universality at even orders, while at odd orders they agree.

## Assumptions and scope
The alphabet consists of two fixed, distinct letters \(0\) and \(1\). A subsequence may skip positions but may not reorder them. Runs are maximal contiguous constant blocks, so \(R(001100)=3\). Palindromes include the two constant words \(0^k\) and \(1^k\). Only nonempty host words are considered; order zero is admitted by convention.

The notion of a greatest order is well-defined: every palindrome of length \(k-1\) embeds into some palindrome of length \(k\) (insert a center symbol if its length is even, or duplicate its center if its length is odd). Thus universality at order \(k\) implies universality at lower orders. It is finite because \(0^k\) and \(1^k\) require at least \(k\) occurrences of each letter.

## Proof
**1. A run obstruction.** Whenever \(u\) is a subsequence of \(w\), each change of letter in \(u\) forces a change between distinct runs of \(w\). Hence \(R(u)\le R(w)\). If \(R(u)=R(w)\), the first letter of \(u\) must equal the first letter of \(w\): the injection from the ordered runs of \(u\) into those of \(w\) is then a bijection.

For odd \(k=2m+1\), the two complementary alternating strings of length \(k\), starting with \(0\) and \(1\), are both palindromes. Each has exactly \(k\) runs. Any host containing both must have at least \(k+1=2m+2\) runs: fewer than \(k\) would exclude each string, whereas exactly \(k\) would force the host's first letter to equal two distinct values.

For even \(k=2m\), let \(a\) be the alternating binary word of length \(m\) starting with \(0\). The words \(aa^{\mathrm R}\) and its bitwise complement are palindromes of length \(2m\). Each has exactly \(2m-1\) runs, since the equal central letters merge two runs. They start with opposite letters. By the same run argument, any host containing both must have at least \(2m\) runs. This also covers \(m=1\).

Together the preceding cases prove \(R(w)\ge2\lceil k/2\rceil\).

**2. A binary-arch embedding lemma.** Suppose a binary word \(v\) can be partitioned into \(h\) consecutive nonempty blocks, each containing both letters, followed by an arbitrary residual suffix. Then every binary word of length \(h\) is a subsequence of \(v\): embed its \(i\)-th desired symbol inside the \(i\)-th block. We call a block of type \(01\), \(10\), or \(001\) a *complete arch*; each contains both letters. No converse to the lemma is needed.

**3. Simultaneously sharp witnesses.** For \(m\ge1\), consider \(W_{2m}=(0011)^m\), whose length is \(4m\) and run count is \(2m\). Removing its initial \(0\) gives the explicit decomposition
\[
01\,(10\,01)^{m-1}\,1,
\]
with \(2m-1\) complete arches and one residual \(1\). Removing its final \(1\) gives
\[
001\,(10\,01)^{m-1},
\]
with \(2m-1\) complete arches.

For \(m\ge1\), put \(W_{2m+1}=(0011)^m01\), of length \(4m+2\) with \(2m+2\) runs. Its suffix after the first \(0\) is
\[
01\,(10\,01)^{m-1}\,10\,1,
\]
with \(2m\) complete arches. Its prefix before the last \(1\) is
\[
001\,(10\,01)^{m-1}\,10,
\]
also with \(2m\) complete arches. The remaining case \(m=0\) is \(W_1=01\), for which both truncated words are nonempty and no arches are required.

Thus, for every \(k\ge1\), the suffix of \(W_k\) after its first \(0\), and the prefix before its final \(1\), each contain every binary length-\((k-1)\) word as a subsequence. Any palindrome of length \(k\) either begins with \(0\) or ends with \(1\), since its first and last symbols agree. In the first case embed its leading \(0\) at the first position of \(W_k\), and the remaining \(k-1\) symbols in the suffix. In the second case embed its first \(k-1\) symbols in the prefix, and its trailing \(1\) at the final position. Consequently \(W_k\) contains every member of \(\mathcal P_k\). The run counts of the witnesses meet the lower bound from Step 1.

**4. Minimum length.** Any universal host contains the constant palindromes \(0^k\) and \(1^k\), requiring at least \(k\) zeroes and \(k\) ones. Hence its length is at least \(2k\). Our witnesses have exactly this length and so are also shortest.

**5. Fixed-run capacity.** The lower bound from Step 1 says \(\pi(w)\ge k\) requires \(R(w)\ge2\lceil k/2\rceil\), whence \(\pi(w)\le2\lfloor R(w)/2\rfloor\). For even \(r=2m\ge2\), the witness \(W_{2m}\) has exactly \(r\) runs and universality order \(2m\). For odd \(r=2m+1\ge3\), append a single \(0\) to \(W_{2m}\). This adds exactly one run and preserves all previously embedded palindromes. For \(r=1\), any constant word has universality order zero. These witnesses attain the bound for every \(r\).

**6. Comparison with unrestricted subsequence universality.** If all binary length-\(k\) words (rather than just palindromes) must be present, the two alternating length-\(k\) words both have \(k\) runs and start with opposite letters. Step 1 forces at least \(k+1\) host runs. Conversely, taking \(k\) consecutive complete binary arches uses at most \(2k\) runs, and appropriately long alternating constant runs achieve exactly \(k+1\) runs and contain every length-\(k\) word (e.g. \(0^k1^k0^k1^k\cdots\), with \(k+1\) runs). Thus the comparison is exact.

## Verification
The standalone file `verify.py` implements subsequence embedding independently of the arch argument, generates every binary palindrome of fixed length from its free half, and checks the witnesses for each \(1\le k\le28\). It also exhaustively examines every binary host of lengths \(1\) through \(12\), checking the lower bounds whenever universal; and checks the fixed-run constructions for each \(1\le r\le36\). Invoke `python3 verify.py` from the directory containing this manuscript and the checker. All checks completed successfully.

The universal quantifiers in the theorem follow from the proofs above. Finite verification is corroborative and is not used as a proof of the infinite claims.

## Relationship to prior work
Barker, Fleischmann, Harwardt, Manea, and Nowotka [1] establish ordinary scattered-factor universality, including its arch factorization and connections to palindromic **host** words. Our theorem restricts the **test patterns** to palindromes while allowing arbitrary hosts; it determines the sharp host-run resource under this restricted spectrum. The distinction between which patterns are tested and which hosts are allowed is essential. Adamson and colleagues [2] study ordinary universality over regular languages, not the palindromic-pattern run threshold. The proofs here use elementary versions of the binary arch idea; neither the arch fact itself nor ordinary universality is claimed as new.

## Limitations
The statement covers the binary alphabet, finite hosts, all palindromic test patterns of one exact length, and runs measured in the host itself. It does not claim the corresponding optimum for larger alphabets, cyclic hosts, contiguous factors, or the enumeration of all extremizing hosts. The sharpness examples are constructions and not a uniqueness classification. A separately published but unindexed equivalent run threshold cannot be categorically excluded by literature search.

## References
[1] L. Barker, P. Fleischmann, K. Harwardt, F. Manea, D. Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629v1, publicly submitted 2020-03-10. https://arxiv.org/html/2003.04629v1

[2] D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea, D. Nowotka, *\(k\)-Universality of Regular Languages*, arXiv:2311.10658v1, publicly submitted 2023-11-17. https://arxiv.org/html/2311.10658v1
