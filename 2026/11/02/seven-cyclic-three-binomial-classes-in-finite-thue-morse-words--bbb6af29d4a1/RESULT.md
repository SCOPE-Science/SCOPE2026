# Seven cyclic three-binomial classes in finite Thue–Morse words

## Finding
Let \(T_k=\mu^k(0)\), where \(\mu(0)=01\) and \(\mu(1)=10\). For a binary word \(w\), write \(\binom{w}{u}\) for the number of *scattered* occurrences of \(u\) as a subsequence. Two words are \(3\)-binomially equivalent when these counts agree for all nonempty binary \(u\) of length at most three. Let \(\rho_i(T_k)\) denote the cyclic rotation beginning at position \(i\), where \(0\leq i<2^k\).

**Theorem.** For every integer \(k\geq3\), the \(2^k\) rotations \(\rho_i(T_k)\) occupy exactly seven \(3\)-binomial equivalence classes. Exactly one class contains \(2^{k-2}\) rotation indices, and each of the other six contains \(2^{k-3}\). Two rotations are \(3\)-binomially equivalent if and only if their two counts \(\binom{w}{01}\) and \(\binom{w}{001}\) agree. For \(k=0,1,2\), the class counts are respectively \(1,2,4\).

The multiplicities count rotation **indices**, not merely distinct cyclic strings.

## Assumptions and scope
All rotations retain their full length \(2^k\). No sentinel is appended. The alphabet is exactly \(\{0,1\}\), and all binomial coefficients count order-preserving, not necessarily adjacent, subsequences. A circular rotation is linearized at its chosen start position before subsequences are counted.

Put \(m=2^{k-1}\) and write \(T_{k-1}=a_0a_1\cdots a_{m-1}\). Define
\[
H_j=\sum_{r=0}^{j-1}(1-2a_r),\qquad 0\leq j<m.
\]
Let \(A(w)=\binom{w}{01}\) and \(B(w)=\binom{w}{001}\).

## Proof
**1. The constant even-position pair deck.** For each \(j\), the rotation \(\rho_{2j}(T_k)\) is \(\mu(\rho_j(T_{k-1}))\). Every morphism block has one zero and one one. For \(k\geq3\), \(T_{k-1}\) has exactly \(m/2\) of each letter. In an image of \(m\) blocks, each ordered pair of distinct blocks contributes exactly one scattered \(01\), while a single block contributes an additional \(01\) precisely if it is \(01\). Consequently every even rotation satisfies
\[
A(\rho_{2j}(T_k))=\binom m2+\frac m2=\frac{m^2}{2}=:A_*.
\]
Each rotation has \(m\) zeros and \(m\) ones. Hence its full one- and two-letter binomial deck is determined by \(A\), and that deck is constant at all even positions.

**2. Triple counts have seven possible states.** For an arbitrary binary word \(x=au\), rotation to \(ua\) changes a scattered triple count by
\[
\binom{ua}{bcd}-\binom{au}{bcd}
=\mathbf1_{d=a}\binom{u}{bc}-\mathbf1_{b=a}\binom{u}{cd}.
\]
The two-letter deck of \(u\) is determined by that of \(au\), together with its initial letter and the one-letter deck. Thus, starting at any even rotation, the change of the entire eight-coordinate triple deck after moving its initial symbol is a fixed vector \(E_a\), depending only on \(a\). Moving both symbols in its first block changes the triple deck by a fixed vector \(D_a\) depending only on whether that block is \(01\) or \(10\).

The balanced word \(T_{k-1}\) contains equally many of these block types. Summing the changes around the entire circular orbit gives \(D_0+D_1=0\). Therefore, if \(C_i\) is the complete triple-count vector of \(\rho_i(T_k)\),
\[
C_{2j}=C_0+H_jD_0,\qquad
C_{2j+1}=C_0+H_jD_0+E_{a_j}.
\]
Because \(a_{2r}=a_r\) and \(a_{2r+1}=1-a_r\) (the smaller-rank Thue–Morse letters),
\[
H_{2r}=0,\qquad H_{2r+1}=1-2a_r.
\]
The possible pairs \((H_j,a_j)\) are exactly \((0,0),(0,1),(1,1),(-1,0)\), while the even-position values of \(H_j\) range over \(\{-1,0,1\}\). This proves **at most seven** equivalence classes, without checking individual triple patterns.

**3. The two-coordinate lower bound.** Rotating the initial zero of a balanced length-\(2m\) word to its end decreases \(A\) by \(m\); rotating its initial one increases \(A\) by \(m\). Thus
\[
A(\rho_{2j+1}(T_k))=
\begin{cases}A_*-m,&a_j=0,\\ A_*+m,&a_j=1.\end{cases}
\]
For \(B=\binom{w}{001}\), moving initial \(0\) to the end changes \(B\) by \(m-A(w)\); moving initial \(1\) changes it by \(\binom m2\). Starting at even position with \(A=A_*\) and then moving the complementary second symbol therefore shows
\[
B(\rho_{2j}(T_k))=B(T_k)+\frac m2 H_j,
\]
and
\[
B(\rho_{2j+1}(T_k))=B(T_k)+\frac m2H_j+
\begin{cases}m-A_*,&a_j=0,\\ \binom m2,&a_j=1.\end{cases}
\]
The three even classes have distinct \(B\)-values and identical \(A=A_*\). The four odd states split by the two distinct values \(A_*-m\) and \(A_*+m\), and within each pair their distinct \(H\)-values give distinct \(B\)-values. Even and odd states cannot coincide because their \(A\)-values differ. Hence there are **exactly seven** classes, and equality of these two binomial coefficients is also sufficient for full \(3\)-binomial equivalence in this rotation family.

**4. Exact class sizes.** There are \(m/2\) even indices \(j\) with \(H_j=0\), and \(m/4\) each with \(H_j=1\) and \(H_j=-1\). Among the odd rotations the four pairs \((H_j,a_j)\) each occur \(m/4\) times, since the smaller-rank word has balanced letters. Thus the seven class sizes are \(m/2\) and six copies of \(m/4\). Direct inspection handles ranks \(0,1,2\). \(\square\)

## Verification
The standalone `checker.py` constructs every \(T_k\) for \(0\leq k\leq9\), independently recomputes the complete scattered-subsequence deck through length three for **every** rotation using a dynamic program, and compares the exact class-size multiset. It also checks the two-coordinate sufficiency at each rank \(k\geq3\). Execute with `python3 checker.py`; the successful terminal marker is `ALL_CHECKS_PASSED`. These finite checks are supplemental; the proof establishes the result for every rank.

## Relationship to prior work
Rigo and Salimov (available by 27 May 2013; published at WORDS 2013) introduced binomial complexity and established bounded binomial complexity for Thue–Morse factors. Lejeune, Leroy and Rigo (first public 2018) proved a much stronger full-factor equivalence criterion and determined the number of \(3\)-binomial classes among **all** length-\(n\) factors of the infinite word (\(21\) at lengths \(n\equiv0\pmod8\), \(n\geq8\)). Our claim is not that general complexity count: it determines the exact **seven-class subset** consisting of the cyclic rotations of a finite complete iterate, including its index multiplicities and a two-statistic recognition rule. This requires analyzing which factor types are realized by those rotations. General full-factor equivalence machinery is relevant prior coverage and remains a historical-priority risk; it is not claimed to be independent of that machinery.

## Limitations
The result is specific to complete dyadic Thue–Morse iterates, scattered subsequences of length at most three, and their indexed circular rotations. It does not classify rotations of arbitrary prefixes or higher binomial orders. Neither independent validation nor exhaustive historical-priority certification has been performed.

## References
- M. Rigo and P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words*, WORDS 2013, LNCS 8079, pp. 217–228. Author preprint available since 2013-05-27: https://orbi.uliege.be/handle/2268/149313
- M. Rigo and P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words*, *Theoretical Computer Science* 601 (2015), 47–57. https://orbi.uliege.be/handle/2268/178703
- M. Lejeune, J. Leroy, M. Rigo, *Computing the k-binomial complexity of the Thue–Morse word*, first public 2018-12-18, https://arxiv.org/abs/1812.07330 ; *J. Combin. Theory Ser. A* 176 (2020), 105284.
