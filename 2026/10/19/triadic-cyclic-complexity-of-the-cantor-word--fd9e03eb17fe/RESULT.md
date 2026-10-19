# Triadic cyclic complexity of the Cantor word

## Finding

Let \(C=101000101000\cdots\) be the infinite binary Cantor word, the fixed point beginning in \(1\) of the substitution \(\mu(1)=101\), \(\mu(0)=000\). Let \(c_C(n)\) be the number of equivalence classes of distinct contiguous length-\(n\) factors of \(C\), where equivalence means cyclic rotation (conjugacy). For every integer \(k\ge0\), put \(N=3^k\). Among length-\(N\) factors, the number of cyclic classes represented by words containing exactly \(j\) ones is

\[
H_k(j)=\begin{cases}
1, & j=0,\\
1, & 1\le j\le 2^k\text{ and }j\text{ is a power of }2,\\
2, & 1\le j\le 2^k\text{ and }j\text{ is not a power of }2,\\
0, & j>2^k.
\end{cases}
\]

In particular, the exact cyclic complexity is

\[
\boxed{c_C(3^k)=2^{k+1}-k}\qquad(k\ge0).
\]

The class counts for \(k=0,1,2,3,4,5,6,7\) are \(2,3,6,13,28,59,122,249\).

## Assumptions and scope

A factor is a finite contiguous subword; distinct factors are considered as *words*, not as occurrences. Cyclic equivalence identifies words \(uv\) and \(vu\) for arbitrary (possibly empty) finite words \(u,v\). A cyclic class is counted if at least one representative occurs in \(C\); this definition does not require *all* rotations to occur. The assertion holds at lengths \(3^k\) for all integers \(k\ge0\), with no recurrence assumption on \(C\).

## Proof

**1. Reduction to two families of windows.** Set \(N=3^k\) and \(W_k=\mu^k(1)\), so \(|W_k|=N\). Each substitution image is a palindrome, and reversal commutes with the substitution, hence \(W_k\) is a palindrome. It begins and ends in \(1\) and contains exactly \(2^k\) ones. Since \(C\) contains no adjacent \(1\)'s, the identity \(C=\mu^k(C)\) represents \(C\) as length-\(N\) blocks, each either \(W_k\) or \(0^N\), with at least one zero block between consecutive \(W_k\) blocks. A length-\(N\) window cannot include a \(1\) from two distinct \(W_k\) blocks. Consequently, every length-\(N\) factor is either \(0^N\), a zero-padded nonempty prefix of \(W_k\), or a zero-padded nonempty suffix of \(W_k\). All these possibilities actually occur: \(010\) is a factor of \(C\), so \(\mu^k(010)=0^NW_k0^N\) is a factor of \(C\).

**2. Exactly two candidate classes at each positive weight.** Write the positions of the ones of \(W_k\) as \(0=p_1<p_2<\cdots<p_{2^k}=N-1\), using zero-based positions. For \(1\le j\le2^k\), define

\[
A_j=0^{N-p_j-1}\,W_k[0:p_j+1],
\]

where the bracket denotes the prefix of the stated length. The word \(A_j\) has exactly \(j\) ones. Any zero-padded prefix of \(W_k\) containing exactly \(j\) ones is conjugate to \(A_j\): a trailing run of zeros is merely moved around the circle to the leading zero run. Since \(W_k\) is palindromic, the zero-padded suffixes of weight \(j\) are conjugate to the reversal \(\widetilde A_j\). Distinct weights cannot be conjugate. Thus the total answer is obtained by deciding, independently for each \(j\), whether \(A_j\) and \(\widetilde A_j\) are conjugate.

**3. An odd marked circular gap.** The positions of ones in \(W_k\) are exactly the integers whose base-three representations, padded to \(k\) places, have only digits \(0\) and \(2\). Equivalently, if \(j-1=\sum_{r=0}^{k-1}\varepsilon_r2^r\) with \(\varepsilon_r\in\{0,1\}\), then

\[
p_j=2\sum_{r=0}^{k-1}\varepsilon_r3^r.
\]

For every \(1\le i<2^k\), binary carry in passing from \(i-1\) to \(i\) gives the consecutive-one distance

\[
g_i=p_{i+1}-p_i=3^{\nu_2(i)}+1.
\]

Each \(g_i\) is even. Reading \(A_j\) cyclically from its first \(1\), the successive distances between the \(j\) ones form the circular vector

\[
(g_1,g_2,\ldots,g_{j-1},h_j),\qquad h_j=N-p_j.
\]

Here \(h_j\) is positive and odd, because \(N\) is odd while \(p_j\) is even. It is therefore the *unique odd entry* of the vector. Reversal reverses the order of cyclic gaps. A cyclic rotation taking this vector to its reversal must align the unique odd entry with itself. It follows that \(A_j\) is conjugate to \(\widetilde A_j\) if and only if \((g_1,\ldots,g_{j-1})\) is a palindrome. The condition is vacuous for \(j=1\), as it should be.

**4. Exactly the powers of two are symmetric.** If \(j=2^a\) for some integer \(a\ge1\), then \(\nu_2(i)=\nu_2(2^a-i)\) for every \(1\le i<2^a\). Hence \((g_1,\ldots,g_{j-1})\) is palindromic. Conversely, suppose \(j\ge2\), and let \(a\) be the unique nonnegative integer such that \(2^a\le j-1<2^{a+1}\). Among indices \(1,\ldots,j-1\), the value \(\nu_2(i)\) is uniquely maximal at \(i=2^a\). A palindrome with a unique maximal entry must have it at its central position, so \(2^a=j/2\), implying \(j=2^{a+1}\). Together with \(j=1\), the symmetric weights are exactly \(j=1,2,4,\ldots,2^k\).

**5. Counting.** The all-zero factor gives one class. For each of the \(2^k\) positive weights there are two candidate classes; the \(k+1\) power-of-two weights merge their pair into one class. Therefore

\[
c_C(N)=1+2\cdot2^k-(k+1)=2^{k+1}-k.
\]

The same argument establishes the complete weight-by-weight profile stated above. \(\square\)

## Verification

Run \(\texttt{python3 verify_cantor.py}\) with Python 3 and no external dependencies. The verifier constructs a morphic prefix of length \(3^{k+2}\) and independently regenerates it from the ternary-digit definition. It enumerates all distinct length-\(3^k\) factors for \(0\le k\le7\), classifies each by an independent least-rotation algorithm, and compares the cyclic classes and their symmetry profile against the structural representatives. Each generated prefix contains \(\mu^k(010)=0^{3^k}W_k0^{3^k}\), so the proof above shows that it covers the *entire* infinite factor set at the tested length. The program returned \(\texttt{VERIFY_OK}\), including \(4373\) factors and \(249\) conjugacy classes at length \(2187\).

## Relationship to prior work

Cassaigne, Fici, Sciortino and Zamboni introduced cyclic complexity and studied general bounds, Sturmian words, selected Toeplitz words, paperfolding words and the Thue–Morse word. Their inspected arXiv text does not give this Cantor-word triadic family. Lü, Chen, Guo and Wen studied factor and permutation complexity of Cantor-like words and reported \(p_C(n)=2n-1\) for \(n\ge2\). That ordinary factor count does not determine how those factors merge into conjugacy classes. In particular, the present result uses the additional reversal symmetry and marked odd gap of the self-similar blocks. Related work on \(k\)-abelian complexity and Lie complexity uses different equivalence relations and does not directly entail this cyclic-class profile.

## Limitations

The result is limited to triadic factor lengths; no complete formula at arbitrary lengths is established. The class profile counts cyclic classes containing at least one factor, not the number of distinct rotations that occur inside a class. Computational checks are finite corroboration and do not substitute for the proof. Possible equivalent results in unindexed literature or inaccessible full text remain an originality risk. Independent audit has not been performed.

## References

1. J. Cassaigne, G. Fici, M. Sciortino and L. Q. Zamboni, *Cyclic Complexity of Words*, first publicly posted 24 February 2014, arXiv:1402.5843, https://arxiv.org/abs/1402.5843 .
2. X.-T. Lü, J. Chen, Y.-J. Guo and Z.-X. Wen, *On the permutation complexity of the Cantor-like sequences*, *Theoretical Computer Science* 616 (2016), 100–110, https://doi.org/10.1016/j.tcs.2015.12.022 .
3. J. Chen, X. Lü and W. Wu, *On the k-abelian complexity of the Cantor sequence*, arXiv:1703.04063, https://arxiv.org/abs/1703.04063 (distinct equivalence relation, consulted as context).
4. J. P. Bell and J. Shallit, *Lie complexity of words*, arXiv:2102.03821, https://arxiv.org/abs/2102.03821 (distinct full-orbit constraint, consulted as context).
