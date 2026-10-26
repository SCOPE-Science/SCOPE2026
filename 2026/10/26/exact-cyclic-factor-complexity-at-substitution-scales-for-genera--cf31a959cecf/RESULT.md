# Exact cyclic factor complexity at substitution scales for generalized Cantor words

## Finding

Let \(q\ge 3\) be an integer, and define the binary morphism
\[\mu_q(1)=1 0^{q-2}1,\qquad \mu_q(0)=0^q.\]
Let \(C_q=\mu_q^{\omega}(1)\) be its one-sided infinite fixed point. For a positive integer \(n\), let \(c_q(n)\) count the equivalence classes, under cyclic rotation **only**, of all distinct contiguous length-\(n\) factors of \(C_q\). The rotations of a factor need not themselves occur as factors.

**Theorem.** For every integer \(q\ge3\) and every integer \(k\ge0\),
\[\boxed{c_q(q^k)=2^{k+1}-k}.\]
More precisely, put \(r=2^k\). Among length-\(q^k\) factors having exactly \(m\) ones, exactly one cyclic class occurs if \(m\in\{0,r\}\) or \(m\) is a power of two; exactly two cyclic classes occur for every other integer \(1\le m<r\). (For \(k=0\) the only weights are zero and one.)

The sequence \(c_q(q^k)\), independent of the base \(q\ge3\), begins \(2,3,6,13,28,59,122,249\). As a consequence, if \(p_q(n)\) denotes ordinary contiguous-factor complexity, then for each fixed \(q\ge3\),
\[\lim_{k\to\infty}\frac{c_q(q^k)}{p_q(q^k)}=0.\]

## Assumptions and scope

All words have the fixed labeled binary alphabet \(\{0,1\}\). A factor is contiguous and occurs in the one-sided infinite word at a finite index. The cyclic equivalence relation permits rotations, not reversal, symbol complementation, or arbitrary permutations. The formula applies at lengths \(q^k\), not at every positive length.

Write \(N=q^k\), \(A=\mu_q^k(1)\), and \(Z=0^N\). The word \(A\) has exactly \(r=2^k\) ones, begins and ends in one, and is a palindrome: both substituted images are palindromes and palindromicity is preserved under substitution.

## Proof

**1. An exhaustive two-block description.** At level \(k\), the infinite word is \(\mu_q^k(C_q)\), a concatenation of length-\(N\) blocks each equal to \(A\) or \(Z\). The adjacent letters in \(C_q\) are precisely \(00\), \(01\), and \(10\). Indeed, \(11\) never occurs because each substituted one is separated from its next one by at least \(q-2\ge1\) zeros; the other three pairs occur in the second substitution iterate. Thus every factor of length \(N\) belongs to the union
\[\mathcal X=\{A[t:N]0^t:0\le t<N\},\qquad
\mathcal Y=\{0^{N-t}A[0:t]:0\le t<N\}.\]
Here indexing in the square brackets is zero based and the right endpoint is exclusive. Conversely, every word in these sets occurs, from some neighboring block pair \(10\) or \(01\); the all-zero word comes from \(00\). This proves exhaustive coverage with no appeal to a finite scan.

**2. At most two cyclic classes at each weight.** If \(A[t]=0\), increasing \(t\) by one in \(\mathcal X\) merely cyclically rotates the word; the same holds for \(\mathcal Y\). Only passing a one changes Hamming weight. Consequently \(\mathcal X\) contains exactly one cyclic class at each positive weight \(m=1,\ldots,r\); \(\mathcal Y\) contains exactly one class at weights \(m=0,\ldots,r-1\). Different weights cannot yield conjugate words. At each interior weight there are therefore at most two classes, which are reversals of each other because \(A\) is a palindrome.

**3. The exact collision criterion.** Write the indices of the ones in \(A\) as \(0=p_0<p_1<\cdots<p_{r-1}=N-1\). For each \(j\in\{0,\ldots,r-1\}\), express \(j=\sum_{h=0}^{k-1}\epsilon_h2^h\), with \(\epsilon_h\in\{0,1\}\). Then
\[p_j=(q-1)\sum_{h=0}^{k-1}\epsilon_hq^h.\]
For \(1\le j<r\), carrying across the trailing binary ones gives
\[d_j:=p_j-p_{j-1}=(q-2)q^{\nu_2(j)}+1,\]
where \(\nu_2(j)\) is the exponent of two in \(j\).

Choose a representative consisting of the first \(m\ge1\) ones of \(A\), including the zeros between them, with zeros appended to reach length \(N\). Its cyclic sequence of distances between successive ones is
\[(d_1,d_2,\ldots,d_{m-1},H_m),\qquad H_m=N-p_{m-1}.\]
All internal distances are congruent to zero modulo \(q-1\), while \(H_m\equiv1\pmod{q-1}\). Since \(q-1\ge2\), the external distance is the **unique** distance with this nonzero residue. The other weight-\(m\) class is represented by the reverse of this word. Their circular words agree under rotation exactly when the internal distance sequence is palindromic, that is,
\[\nu_2(j)=\nu_2(m-j)\quad\text{for all }1\le j<m.\]

This condition holds for every \(m=2^s\): each \(j\) in the stated range has the same two-adic valuation as \(2^s-j\). Conversely, if \(m>1\) is odd, \(j=1\) violates the condition. If \(m=2^s u\), where \(s\ge1\) and \(u\ge3\) is odd, then \(j=2^s\) violates it because \(\nu_2(m-j)\ge s+1\). The case \(m=1\) has an empty internal sequence and also qualifies as a power of two. Hence the two classes coincide exactly for powers of two.

**4. Counting.** The extreme weights \(m=0\) and \(m=r\) contribute one class each. Each of the \(r-1\) interior weights contributes two classes, except the \(k\) powers \(1,2,\ldots,2^{k-1}\), each of which contributes one. Therefore
\[c_q(q^k)=2+2(r-1)-k=2^{k+1}-k.\]
For \(k=0\), this calculation has no interior weights and still gives two classes.

Finally, the \(N\) words \(A[t:N]0^t\) are pairwise distinct because their terminal zero-run lengths are exactly \(t\) (\(A\) ends in one). Hence \(p_q(N)\ge N=q^k\), whereas \(c_q(N)=2^{k+1}-k\), and the displayed complexity ratio tends to zero for every fixed \(q\ge3\). \(\square\)

## Verification

The accompanying standalone `verify.py` constructs the \(q\)-ary generalized Cantor substitution words directly, and independently enumerates all length-\(q^k\) factors of an iterate two levels deeper. It checks exact equality of the resulting factor set with the two-block description, classifies every factor by cyclic rotation using a linear-time minimum-rotation algorithm, and cross-checks small instances against literal enumeration of all rotations. It also verifies the displayed arithmetic formula for every consecutive-one distance. The supplied `counts.csv` is generated by that script.

Checks cover every \(3\le q\le7\), \(0\le k\le4\), plus \((q,k)=(3,5),(3,6),(3,7),(4,5)\). These finite tests support the theorem but do not replace its infinite proof.

To reproduce with Python 3, place `verify.py` and `counts.csv` in one directory and run `python verify.py`; the program regenerates the table and raises an assertion if any comparison fails.

## Relationship to prior work

Cassaigne, Fici, Sciortino, and Zamboni introduced cyclic complexity and studied its general properties and selected families, including Sturmian, Toeplitz, paperfolding, and Thue–Morse words. Their single-discrepancy substitution theorem does not directly apply: the present morphism's images of zero and one disagree at **two** positions, not one. No Cantor-specific substitution-scale count is stated in the inspected text.

Chen, Lü, and Wu study the ordinary and higher \(k\)-Abelian complexity of the classical Cantor sequence. Their equivalence relation counts factors according to endpoint information and multiplicities of short factors, rather than cyclic rotations. Those results do not supply this cyclic-class formula. Results about generalized Cantor palindromic, absent-factor, or bounded-order Abelian complexity similarly do not imply the valuation-based rotation/reversal collision classification proved here.

## Limitations

The exact enumeration is established at geometric lengths \(q^k\); the complete function at arbitrary lengths is not determined. This is a mathematical result with a proof and reproducible finite checks, not an independently audited or externally certified priority determination. Earlier unindexed work on cyclic complexity of Cantor-type words may exist.

## References

1. J. Cassaigne, G. Fici, M. Sciortino, L. Q. Zamboni, *Cyclic Complexity of Words*, arXiv:1402.5843, first posted 2014-02-24. https://arxiv.org/abs/1402.5843
2. J. Chen, X. Lü, W. Wu, *On the k-Abelian Complexity of the Cantor Sequence*, arXiv:1703.04063, first posted 2017-03-12. https://arxiv.org/abs/1703.04063
