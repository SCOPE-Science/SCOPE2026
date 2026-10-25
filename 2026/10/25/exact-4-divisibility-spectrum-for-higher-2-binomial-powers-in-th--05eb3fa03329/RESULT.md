# Exact \(4\)-divisibility spectrum for higher \(2\)-binomial powers in the Thue–Morse word

## Finding

Let \(t=t_0t_1\cdots\) be the one-sided binary Thue–Morse word, the fixed point beginning in \(0\) of \(\mu(0)=01\) and \(\mu(1)=10\). For two binary words \(u,v\), write \(u\equiv_2 v\) if every binary scattered subsequence of length at most \(2\) occurs equally often in each.

**Theorem.** For every pair of integers \(m\ge1\) and \(\ell\ge3\), there exists a starting position \(i\ge0\) for which the \(\ell\) consecutive blocks
\[
 t[i+jm\, ..\, i+(j+1)m-1],\qquad 0\le j<\ell,
\]
are pairwise \(2\)-binomially equivalent **if and only if** \(4\mid m\). In fact, if \(4\mid m\), every \(i\equiv0\pmod4\) is such a starting position for every \(\ell\ge3\).

The qualification \(\ell\ge3\) is essential: for two blocks, other root lengths can occur. The present theorem concerns exact order-\(2\) binomial equivalence, not literal or abelian equality.

## Assumptions and scope

Positions are indexed from \(0\); all factors are contiguous and have positive finite length. A scattered occurrence of a word \(v\) in \(u\) is a strictly increasing selection of positions spelling \(v\). We allow all integers \(\ell\ge3\), with no upper bound. The sequence is the specified *one-sided* fixed point, not an arbitrary sequence in its subshift. The standard congruence property of fixed-order binomial equivalence is also proved below for the only instance used.

## Proof

**1. A binary two-statistic criterion.** For a binary word \(w=w_0\cdots w_{L-1}\), put
\[
 S(w)=\sum_{j=0}^{L-1}w_j,\qquad J(w)=\sum_{j=0}^{L-1}j w_j.
\]
For equal-length words, \(u\equiv_2v\) holds precisely when \(S(u)=S(v)\) and \(J(u)=J(v)\). Indeed, the number of scattered \(01\) subsequences is
\[
 \binom{w}{01}=J(w)-\binom{S(w)}2.
\]
The counts of \(00\) and \(11\) are respectively \(\binom{L-S(w)}2\) and \(\binom{S(w)}2\), while the count of \(10\) is \(S(w)(L-S(w))-\binom{w}{01}\). These identities account for every binary subsequence of length at most \(2\).

**2. No odd-length abelian cube.** The recurrence \(t_{2j}=t_j\), \(t_{2j+1}=1-t_j\) shows that each aligned two-letter pair contains one \(1\). Suppose \(m=2h+1\) and three consecutive length-\(m\) blocks have identical numbers of ones. Within any three successive blocks, an adjacent pair begins at an even position: if the first begins at an even position choose blocks \(0,1\), and otherwise choose blocks \(1,2\). For that pair, beginning at \(2a\), write \(b=t_{a+h}\). The first block contains \(h+b\) ones; the next begins at \(2(a+h)+1\) and contains \(h+1-b\). These integers differ by \(1\), a contradiction. Thus no abelian cube of odd root length occurs anywhere in \(t\).

**3. No even root congruent to \(2\) modulo \(4\).** Suppose \(m=2h\) with \(h\) odd and three consecutive length-\(m\) blocks are pairwise \(2\)-binomially equivalent.

If their initial position is even, \(i=2a\), they are exactly \(\mu(x_0),\mu(x_1),\mu(x_2)\) for consecutive length-\(h\) factors \(x_0,x_1,x_2\) of \(t\). Each image has \(h\) ones, and direct summation yields
\[
 J(\mu(x_s))=h^2-S(x_s).
\]
Equality of the image moments therefore forces \(S(x_0)=S(x_1)=S(x_2)\), an odd-root abelian cube ruled out by step 2.

If \(i=2a+1\), denote the four relevant source boundary bits by \(b_s=t_{a+sh}\), where \(0\le s\le3\). The \(s\)-th length-\(2h\) block has \(h+b_{s+1}-b_s\) ones. As these one-counts are equal for \(s=0,1,2\), their consecutive increments \(b_{s+1}-b_s\) are a common integer \(d\). Hence \(b_3-b_0=3d\). Since all bits are \(0\) or \(1\), \(d=0\) and \(b_0=b_1=b_2=b_3=:b\). Put \(x_s=t[a+sh\, ..\, a+(s+1)h-1]\). Now each odd-start block is the cyclic left rotation by one symbol of \(\mu(x_s)\), because the symbol appended at its right boundary equals the first symbol \(b\) removed at its left boundary. For a length-\(2h\) word \(y\), left rotation changes its moment by \(-S(y)+2h y_0\). Consequently the moment of this odd-start block is
\[
 h^2-S(x_s)-h+2hb.
\]
Equality of moments again forces \(S(x_0)=S(x_1)=S(x_2)\), the same forbidden abelian cube. Therefore no candidate with \(m\equiv2\pmod4\) exists.

**4. Every root divisible by four works, at every aligned position.** The second substitution iterate is
\[
 \mu^2(0)=0110,\qquad \mu^2(1)=1001.
\]
These words both have two ones and moment \(3\), so by step 1 they are \(2\)-binomially equivalent. Such equivalence respects concatenation: for words \(a,b\) and each scattered word \(v\) of length at most \(2\), the count in \(ab\) is the sum of its count in \(a\), its count in \(b\), and the cross-term product of the appropriate single-symbol counts. Hence replacing either concatenated factor by a \(2\)-binomially equivalent factor preserves every such count. It follows that all \(\mu^2(x)\) for binary words \(x\) of the same length are mutually \(2\)-binomially equivalent.

For \(m=4k\), \(k\ge1\), and \(i=4a\), the equality \(t=\mu^2(t)\) identifies every successive length-\(m\) block at \(i+jm\) with the second-iterate image of a length-\(k\) source factor. These images are \(2\)-binomially equivalent for any number of consecutive blocks. This proves existence for every \(\ell\ge3\) and every position divisible by \(4\). Combining with steps 2 and 3 proves the biconditional. \(\square\)

## Verification

The standalone `verify.py` uses no third-party packages. It independently enumerates actual scattered subsequence counts for all binary words through length \(10\), checks the second-iterate substitution property for all source words through length \(8\), and compares the theorem against every possible start within a length-\(32768\) arithmetic Thue–Morse prefix for all root lengths through \(256\). It separately checks higher exponents via direct scattered subsequence counting and searches for odd-length abelian cubes. These finite computations test the implementation and boundary cases; the unrestricted statements follow from the proof above, not the sample range. Reproduce with `python3 verify.py`.

## Relationship to prior work

Rigo and Salimov introduced binomial equivalence and treated the complexity of the Thue–Morse word [1]. Rao, Rigo, and Salimov constructed other morphic words avoiding \(2\)-binomial squares or cubes [2]; existence of an avoiding word does not determine the possible root lengths of higher binomial powers inside Thue–Morse. Lejeune, Leroy, and Rigo classified the \(k\)-binomial complexity of the Thue–Morse word [3], counting factor-equivalence classes rather than adjacent repetitions of three or more blocks. The result here is the exact all-length occurrence spectrum for \(2\)-binomial exponents at least \(3\), including its uniform aligned-position existence statement.

## Limitations

The theorem neither determines the starting positions at nonmultiples of four when the root is permissible nor counts occurrences of higher binomial powers. It applies to the binary Thue–Morse fixed point, equivalence order \(2\), and exponents at least \(3\), not arbitrary automatic words, orders or exponents. A prior unindexed or unstated derivation could affect historical priority; this note does not claim exhaustive bibliographic uniqueness or independent certification.

## References

[1] M. Rigo and P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words*, WORDS 2013; publicly accessible since 27 May 2013. https://orbi.uliege.be/handle/2268/149313

[2] M. Rao, M. Rigo, and P. Salimov, *Avoiding 2-binomial squares and cubes*, arXiv:1310.4743 (17 October 2013). https://arxiv.org/abs/1310.4743

[3] M. Lejeune, J. Leroy, and M. Rigo, *Computing the k-binomial complexity of the Thue–Morse word*, arXiv:1812.07330 (18 December 2018). https://arxiv.org/abs/1812.07330
