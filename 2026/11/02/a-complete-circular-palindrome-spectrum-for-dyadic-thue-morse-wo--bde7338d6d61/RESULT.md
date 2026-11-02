# A complete circular-palindrome spectrum for dyadic Thue–Morse words

## Finding
Let \(T_0=0\) and \(T_{k+1}=\mu(T_k)\), where \(\mu(0)=01\) and \(\mu(1)=10\). For a word of length \(N=2^k\), a circular factor is a factor of the periodic extension starting at any of the \(N\) cyclic positions, of length at most \(N\). Let \(P_k(\ell)\) and \(A_k(\ell)\) be the numbers of **distinct**, not positioned, circular factors of length \(\ell\) that are respectively palindromes and antipalindromes (their reversals equal their bitwise complements). Set both values to zero outside \(1\le\ell\le2^k\).

For every \(k\ge3\), the following recurrences determine the entire length-by-length spectrum for \(1\le t\le2^{k-1}\):
\[
P_k(2t)=A_{k-1}\bigl(t+(t\bmod2)\bigr),\qquad
A_k(2t)=P_{k-1}(t)+P_{k-1}(t+1)-2\mathbf1_{t=1}.
\]
The odd-length spectrum is \(P_k(1)=P_k(3)=2\), \(P_k(\ell)=0\) for odd \(\ell\ge5\), and \(A_k(\ell)=0\) for odd \(\ell\). The base rank \(k=2\) has \(P_2(1)=P_2(2)=P_2(4)=2\), \(A_2(2)=A_2(4)=2\), and all other values zero. Thus for every \(k\ge2\), the total number \(p_k=\sum_{\ell=1}^{2^k}P_k(\ell)\) of distinct nonempty circular palindromes is exactly
\[
p_k=\begin{cases}
(7\cdot2^k+8)/6,& k\text{ even},\\
(4\cdot2^k+4)/3,& k\text{ odd}.
\end{cases}
\]
In particular the normalized count has two distinct parity-subsequence limits, \(7/6\) and \(4/3\), rather than one asymptotic density.

## Assumptions and scope
All symbols are from the fixed alphabet \(\{0,1\}\); the Thue–Morse substitution is exactly as defined above, and \(k\) is an integer. Circular factors may wrap but cannot traverse more than one full copy. Antipalindrome means \(v=\overline{v^{\mathrm{rev}}}\), where a bar complements each bit. Counts concern different factor **strings**: different starting positions producing the same string count once. The base rank \(k=2\) fixes all subsequent recurrences; rank \(k=1\) is not used in the displayed closed total.

## Proof
**1. Short palindromes and absence of long odd ones.** Every length-three factor of a circular substituted word \(\mu(w)\) contains a complete aligned pair, either \(01\) or \(10\). Hence there is no run \(000\) or \(111\), even around the circular boundary. For a hypothetical palindrome of length five beginning at an even substituted position, the five symbols have form \(a\,\overline a\,b\,\overline b\,c\). Palindromicity forces \(a=b=c\), giving a forbidden three-letter constant run in the underlying cyclic word. At an odd substituted position, the five symbols are \(\overline a\,b\,\overline b\,c\,\overline c\), with the same consequence. The input \(T_{k-1}\) has no cyclic constant run of three for \(k-1\ge2\). Thus \(T_k\), \(k\ge3\), has no circular palindrome of length five. Every longer odd palindrome contains a central length-five palindrome, so all longer odd lengths are excluded. Both letters and both length-three palindromes \(010\), \(101\) occur in \(T_3=01101001\) and persist in every later iterate. An antipalindrome over a binary alphabet cannot have an odd length, because its center would equal its own complement.

**2. Two parities of starts.** A length-\(2t\) factor beginning at an even position is \(\mu(v)\) for a cyclic input factor \(v\) of length \(t\). One beginning at an odd position is
\[
G(u)=\overline{u_1}\,\mu(u_2\cdots u_t)\,u_{t+1},
\]
for a cyclic input factor \(u=u_1\cdots u_{t+1}\). For the exceptional full-length endpoint, the latter expression uses one additional input symbol from the periodic extension; any demand for it below will be a forbidden palindrome of odd length at least five. The two displayed maps are injective on fixed-length input factors: the first output exposes the input at its even-indexed bits, and the second exposes all input letters in its alternating positions and final bit.

The identity \(\mu(v)^{\mathrm{rev}}=\mu(\overline{v^{\mathrm{rev}}})\) proves that the even-start output is palindromic precisely when \(v\) is antipalindromic, and antipalindromic precisely when \(v\) is palindromic. Comparing corresponding symbols in \(G(u)\) likewise proves that the odd-start output is palindromic precisely when \(u\) is antipalindromic, and antipalindromic precisely when \(u\) is palindromic.

**3. Palindromes: only one contributing parity.** Since antipalindromes have even lengths, when \(t\) is even, only the even-start construction can give a palindrome of length \(2t\), bijecting with antipalindromes of length \(t\) in the preceding iterate. When \(t\) is odd, only the odd-start construction is possible, bijecting with antipalindromes of length \(t+1\). This proves the first recurrence, including its distinct-factor count because the relevant map is injective. When \(t=2^{k-1}\), it is even, so no input beyond one preceding circular traversal is required.

**4. Antipalindromes: one explicit overlap.** For antipalindromic outputs of length \(2t\), the even-start image arises from the \(P_{k-1}(t)\) input palindromes; the odd-start image arises from the \(P_{k-1}(t+1)\) input palindromes. Their overlap would have to consist of outputs whose pairs at even positions are complementary, as all outputs of \(\mu\) are. Applied to \(G(u)\), this forces \(u_1=u_2=\cdots=u_{t+1}\). For \(t\ge2\), such an input would contain a forbidden cyclic run of three, so the two image sets are disjoint. For \(t=1\), they overlap in exactly the two strings \(01\) and \(10\), since the preceding iterate contains both single symbols and the cyclic pairs \(00\), \(11\). At the full-length boundary, the possible extra input factor would be a palindrome of odd length \(2^{k-1}+1\ge5\), which cannot occur even in its cyclic periodic extension, by step 1. The second recurrence follows.

**5. Summation.** Write \(a_k=\sum_{\ell=1}^{2^k}A_k(\ell)\). As \(t\) runs from \(1\) to \(2^{k-1}\), every even input length in the first recurrence occurs exactly twice, while odd input lengths contribute zero. In the second recurrence the shifted sum \(\sum_tP_{k-1}(t+1)\) omits the two one-letter palindromes and has no additional endpoint term. Thus
\[
p_k=4+2a_{k-1},\qquad a_k=2p_{k-1}-4\qquad(k\ge3).
\]
Consequently \(p_{k+2}=4p_k-4\). Direct inspection of \(T_2=0110\) gives \(p_2=6\), and the recurrence gives \(p_3=12\). Solving the even- and odd-rank recurrences gives precisely the two formulas in the finding.

## Verification
Running the standalone accompanying `checker.py` enumerates each circular factor directly at all ranks \(1\) through \(9\), checks palindromicity and antipalindromicity independently, checks the complete recurrences at every permissible length for ranks \(3\) through \(9\), and verifies the total formulas for ranks \(2\) through \(9\). The palindrome totals are \(2,6,12,20,44,76,172,300,684\); antipalindrome totals are \(2,4,8,20,36,84,148,340,596\). These experiments corroborate but do not replace the all-rank proof above.

## Relationship to prior work
Allouche, Baake, Cassaigne and Damanik study palindromic complexity of infinite symbolic sequences, including the Thue–Morse sequence. Peltomäki and Blondin-Massé et al. also study (anti)palindrome structure in the infinite Thue–Morse word. Their infinite-word factor counts do not directly classify wrap-around factors of a *particular finite dyadic iterate*. Simpson's general circular-palindrome bound supplies a comparator, not this exact rank- and length-resolved spectrum. Historical-priority uncertainty remains, in particular because Simpson's complete text was not accessible in the present investigation.

## Limitations
The result does not classify arbitrary-length prefixes, arbitrary conjugate-factor multiplicities, longer periodic factors exceeding one full traversal, or other binary substitutions. Independent validation has not been performed. Search-based originality assessments are necessarily nonexhaustive.

## References
1. J.-P. Allouche, M. Baake, J. Cassaigne and D. Damanik, *Palindrome Complexity*, first arXiv posting 2001-06-14, https://arxiv.org/abs/math/0106121 .
2. J. Peltomäki, *Privileged Factors in the Thue–Morse Word*, first arXiv posting 2013-06-28, https://arxiv.org/abs/1306.6768 .
3. A. Blondin-Massé, S. Brlek, S. Garon and S. Labbé, *Combinatorial properties of f-palindromes in the Thue–Morse sequence* (2008).
4. J. Simpson, *Palindromes in circular words*, Theoretical Computer Science (2014), https://doi.org/10.1016/j.tcs.2014.07.012 .
