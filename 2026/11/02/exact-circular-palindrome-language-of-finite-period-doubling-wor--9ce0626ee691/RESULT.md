# Exact circular-palindrome language of finite period-doubling words

## Finding
Let \(\mu(0)=01\) and \(\mu(1)=00\), and write \(P_k=\mu^k(0)\). For \(k\ge2\), let \(H_k\) denote the distinct nonempty palindromic circular factors of \(P_k\), where every factor has length at most \(|P_k|=2^k\). A circular factor may cross the join between the last and first positions once; starts are indexed modulo \(2^k\).

Set \(H_2=\{0,1,00,000,010\}\). For any odd-length binary palindrome \(v=v_1\cdots v_{2t+1}\), put
\[\Phi(v)=\overline v_1 0\overline v_2 0\cdots0\overline v_{2t+1},\qquad \Psi(v)=0\Phi(v)0,\]
where the bar complements a bit. For every \(k\ge3\), the following is a **disjoint equality of sets**:
\[\boxed{H_k=\{00,101,01010\}\ \sqcup\ \{\Phi(v),\Psi(v):v\in H_{k-1},\ |v|\text{ odd}\}.}\]
Consequently,
\[\boxed{|H_k|=3\cdot2^{k-1}-1\quad(k\ge2).}\]
The word \(00\) is the unique even-length member of \(H_k\), for each \(k\ge2\).

The result also determines the **exact length spectrum**. Write \(p_k(\ell)=|\{v\in H_k:|v|=\ell\}|\), and extend it by zero at nonexistent lengths. For \(k\ge3\) and every integer \(t\ge0\),
\[p_k(4t+1)=p_{k-1}(2t+1)+\mathbf 1_{\{t=1\}},\]
\[p_k(4t+3)=p_{k-1}(2t+1)+\mathbf 1_{\{t=0\}},\]
while \(p_k(2)=1\) and \(p_k(2j)=0\) for \(j\ne1\). Initially \(p_2(1)=2\), \(p_2(2)=1\), \(p_2(3)=2\), and all other entries vanish. The recurrence applies only to lengths at most \(2^k\), and produces zero above that range.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\), the morphism and its initial letter are fixed, and the objects are **complete dyadic iterates** \(P_k\), not arbitrary prefixes or all factors of the one-sided infinite fixed point. A palindrome equals its reversal. Factors of length exceeding one traversal are excluded. Counts identify equal words even when they start at different cyclic positions.

## Proof
**1. Parity and the absence of short cyclic palindromes.** Inductively, \(P_k\) alternates an even-position zero with the complement of a letter from \(P_{k-1}\) at the next odd position. Concretely, in zero-based indices, \(P_k[2j]=0\), \(P_k[2j+1]=1-P_{k-1}[j]\), with indices interpreted cyclically. Thus every \(1\) appears at an odd position and the cyclic digram \(11\) is impossible. In addition, \(0000\) is impossible in \(P_k\): four consecutive zeros would include two consecutive odd positions, forcing the corresponding adjacent letters of \(P_{k-1}\) to be \(11\). For \(k\ge2\), cyclic \(00\) exists because \(P_{k-1}\) contains a \(1\). Each cyclic four-letter palindrome must be one of \(0000\), \(0110\), \(1001\), or \(1111\). The first is excluded above; the second and fourth contain \(11\); in \(1001\), the two \(1\)'s have opposite position parity, impossible. Hence \(P_k\) has **no circular even-length palindrome of length at least four**, since the four central letters of such a palindrome would themselves form a forbidden four-letter palindrome. The only even-length circular palindrome is \(00\).

**2. Odd palindrome centered at an odd position.** A word centered at a position \(2j+1\) (an odd position of \(P_k\)) alternates letters from the complemented lower-level circle with mandatory zeros between them. Palindromicity at offsets \(2,4,\ldots\) is equivalent to palindromicity of the corresponding lower-level circular segment. Odd lengths ending at odd positions are exactly \(\Phi(v)\), and the one-zero extension at each end is exactly \(\Psi(v)\), for an odd circular palindrome \(v\) of \(P_{k-1}\). Conversely, every such \(v\) has both lifts in the upper-level cyclic word: since \(|v|\) is odd and \(|P_{k-1}|\) is even, \(|v|\le2^{k-1}-1\), so the longer lift has length \(2|v|+1\le2^k-1\). Therefore there is no truncation at a full traversal. The maps \(\Phi\) and \(\Psi\) are injective, and their output lengths are respectively \(1\pmod4\) and \(3\pmod4\), so their images are disjoint.

**3. Odd palindrome centered at an even position.** Such a center is a zero. If its adjacent odd-position letters differ, its only palindrome is the length-one word \(0\), which is already present as \(\Phi(1)\). If they agree, their corresponding adjacent letters in \(P_{k-1}\) agree; because the lower circle has no \(11\), those adjacent letters must both be \(0\), and the resulting three-letter palindrome is \(101\). Its two additional outside positions are even and hence both zero, yielding the five-letter palindrome \(01010\). A length-seven continuation would require equality of the next outer odd-position letters, giving a cyclic four-letter palindrome in \(P_{k-1}\) whose two middle symbols are \(00\); none exists by step 1. Longer palindromes are therefore impossible. Both exceptional words occur because the lower circle contains \(00\) for \(k-1\ge2\).

The only palindrome centered at an even position that is also a lift is \(0\). The words \(101\) and \(01010\) are not lifts: a lift of length three has the form \(0b0\), and a lift of length five has the form \(b0c0b\); this latter form differs from \(01010\) in its fixed interleaved positions. Together with the unique even palindrome \(00\), this proves the stated disjoint set recursion.

**4. Counts and lengths.** There is one even-length member in every \(H_k\). Thus if \(h_k=|H_k|\), the disjoint recursion gives \(h_k=3+2(h_{k-1}-1)=2h_{k-1}+1\). Since \(h_2=5\), solving gives \(h_k=3\cdot2^{k-1}-1\). The lengths of the two lifts are \(2|v|-1\) and \(2|v|+1\); the exceptional odd factors have lengths three and five, yielding the specified length recurrences.

## Verification
The accompanying `checker.py` regenerates \(P_k\), exhaustively enumerates each circular factor of every permitted length, filters palindromes, and compares the resulting distinct-word set against the claimed recursion for each \(2\le k\le9\). It also checks the exact total, the unique even factor, and all lengthwise multiplicities. Verified totals at ranks \(2,3,4,5,6,7,8,9\) are respectively \(5,11,23,47,95,191,383,767\). These finite computations corroborate but do not replace the unrestricted induction above.

## Relationship to prior work
Allouche, Baake, Cassaigne and Damanik study palindromic factor counts for **infinite** automatic and substitution sequences, including the period-doubling sequence. Schaeffer and Shallit develop logical and automatic methods for palindromic factors and richness of automatic sequences. Cassaigne and collaborators study **cyclic conjugacy complexity** (equivalence of factors under rotation), a different invariant from palindromes found when an actual finite word is joined into a circle. Simpson gives a universal upper bound of \(5N/3\) distinct circular palindromes for a circle of length \(N\), but the abstract does not state the present period-doubling classification. Here the exact total equals \((3/2)N-1\) for dyadic \(N\ge4\), close to but below that universal bound. In particular, results about palindromes anywhere in the *infinite* sequence do not by themselves specify which palindrome words occur in the *finite cyclic closure* of a given dyadic iterate.

## Limitations
This proves no analogous formula for arbitrary-length prefixes, arbitrary conjugates of distinct morphic words, or circular factors longer than a single traversal. The complete 2014 Simpson article and 2000 Damanik article were not accessible in this investigation; hence exhaustive historical priority verification is outstanding. There has been no independent mathematical audit.

## References
- J.-P. Allouche, M. Baake, J. Cassaigne and D. Damanik, *Palindrome complexity*, arXiv:math/0106121 (first public preprint 2001-06-14), Section 4.2. https://arxiv.org/abs/math/0106121
- L. Schaeffer and J. Shallit, *Closed, Palindromic, Rich, Privileged, Trapezoidal, and Balanced Words in Automatic Sequences*, arXiv:1508.02074 (2015). https://arxiv.org/abs/1508.02074
- J. Cassaigne, G. Fici, M. Sciortino and L. Q. Zamboni, *Cyclic Complexity of Words*, arXiv:1402.5843 (2014). https://arxiv.org/abs/1402.5843
- J. Simpson, *Palindromes in circular words*, Theoretical Computer Science 550 (2014), 66–78, DOI:10.1016/j.tcs.2014.07.012.
