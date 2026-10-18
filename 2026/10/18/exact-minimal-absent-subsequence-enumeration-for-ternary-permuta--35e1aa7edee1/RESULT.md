# Exact minimal-absent-subsequence enumeration for ternary permutation powers

## Finding
Let \(P\) be any permutation of three distinct symbols, and write \(W_m=P^m\) for \(m\ge1\). A word is a **minimal absent subsequence** (MAS) of \(W_m\) if it is not a scattered subsequence, but every word obtained by deleting one letter from it is a scattered subsequence. Denote the number of such words by \(a_m\). Then
\[
\boxed{\sum_{m\ge1}a_m x^m=\frac{6x-2x^2+10x^3-3x^4+8x^5-3x^6}{1-3x+2x^2-4x^3+2x^4-3x^5+x^6}.}
\]
Thus the first twelve counts are \(6,16,46,127,349,960,2640,7264,19989,54999,151326,416368\). The result additionally characterizes **each** MAS by adjacent comparisons and gives a finite transfer-matrix expression refining the count by MAS length, for every alphabet size at least two.

## Assumptions and scope
Use the order given by the permutation: replace the symbols of \(P\), from left to right, by \(0,1,\ldots,q-1\). Since this is a bijection of alphabets, MAS membership and cardinalities are unchanged. Below \(q\ge2\), \(m\ge1\), and \(W_m=(01\cdots(q-1))^m\). For a word \(u=u_1\cdots u_L\) define its number of weak descents by
\[
d(u)=\sum_{i=1}^{L-1}\mathbf 1_{\{u_i\ge u_{i+1}\}}.
\]
All comparisons refer to the chosen order; subsequences need not be contiguous. The statement counts distinct absent words, not embeddings, and uses no symbols outside the alphabet of \(W_m\).

**Local characterization.** A word \(u\) is an MAS of \(W_m\) if and only if \(L\ge2\) and all of the following hold:
\[
d(u)=m,\qquad u_1\ge u_2,\qquad u_{L-1}\ge u_L,
\]
\[
\mathbf1_{\{a\ge b\}}+\mathbf1_{\{b\ge c\}}-\mathbf1_{\{a\ge c\}}\ge1
\quad\text{for every consecutive triple }(a,b,c)\text{ of }u.
\]
In particular, for fixed \(q\), the length-refined counts admit the exact finite matrix formula below; the displayed rational closed form specializes to \(q=3\).

## Proof
**Greedy embedding.** Reading a nonempty word \(u\) as a subsequence of \(W_m\) greedily, the first symbol is read from the first copy of \(P\). The next symbol is read in the same copy precisely if it is larger than the preceding symbol. Otherwise it must be read in the next copy. Greedy positions cannot be improved by postponing a letter. Consequently \(u\) occurs as a subsequence of \(W_m\) if and only if \(1+d(u)\le m\). The empty word always occurs.

**Minimality.** For a nonempty \(u\) absent from \(W_m\), deleting any letter must reduce \(d(u)\) to at most \(m-1\). All one-letter deletions suffice: any proper subsequence is a subsequence of one of them. No one-letter word is absent. Removing the first or last symbol deletes just one comparison, of value zero or one. Since \(u\) is absent, these two conditions force \(d(u)=m\) and both endpoint comparisons to be weak descents. Removing an interior symbol \(b\) between \(a,c\) changes \(d\) by
\[
\Delta(a,b,c)=\mathbf1_{\{a\ge b\}}+\mathbf1_{\{b\ge c\}}-\mathbf1_{\{a\ge c\}}.
\]
Thus all deletions lower the descent count if and only if each interior triple has \(\Delta\ge1\). This proves both directions of the local characterization, including \(L=2\).

**Exact transfer enumeration.** Index ordered pairs \((a,b)\) lexicographically in \(\{0,\ldots,q-1\}^2\). Define \(E_{ab}=\mathbf1_{\{a\ge b\}}\), \(V_{ab}(x,t)=xt^2E_{ab}\), and the \(q^2\)-square transition matrix \(T_q(x,t)\) whose only possibly nonzero entries are
\[
(T_q)_{(a,b),(b,c)}=t\,x^{\mathbf1_{\{b\ge c\}}}\mathbf1_{\{\Delta(a,b,c)\ge1\}}.
\]
Every admissible word is counted once by its first pair, successive triples, and final pair. Its monomial is \(x^{d(u)}t^{|u|}\). Hence the bivariate generating function of the MAS of all permutation powers is
\[
F_q(x,t)=V(x,t)(I-T_q(x,t))^{-1}E.
\]
The inverse is well-defined as a formal series: any transition carrying zero powers of \(x\) is a strict ascent, and two consecutive such transitions cannot both meet the triple condition, so the zero-\(x\) part of \(T_q\) is nilpotent. This matrix identity establishes the complete length-refined distribution for each fixed \(q\).

**Closed ternary rational form.** Set \(q=3\), \(t=1\), and \(M=T_3(x,1)\). In lexicographic pair order \((00,01,02,10,11,12,20,21,22)\), define
\[
D=1-3x+2x^2-4x^3+2x^4-3x^5+x^6,
\]
\[
\begin{aligned}
Q_{00}&=1+x+2x^2+x^3+2x^4-x^5, &Q_{01}&=x+2x^3-x^4,\\
Q_{02}&=2x-x^2+x^3, &Q_{10}&=1+2x^2-x^3+3x^4-x^5,\\
Q_{11}&=1+2x^2-x^3, &Q_{12}&=x-x^3,\\
Q_{20}&=1-2x+3x^2-2x^3+3x^4-x^5, &Q_{21}&=1-x+2x^2,\\
Q_{22}&=1-x^2.&&
\end{aligned}
\]
Direct polynomial multiplication gives the two **exact identities**
\[
(I-M)Q=DE,\qquad x\sum_{a\ge b}Q_{ab}=6x-2x^2+10x^3-3x^4+8x^5-3x^6.
\]
Since \(D(0)=1\), these prove the displayed rational generating function for all \(m\ge1\), not just its first coefficients. The accompanying independent standard-library checker verifies every coefficient of all nine polynomial identities.

## Verification
Run `python3 check.py` in this directory. The checker verifies the nine polynomial equalities and numerator identity by exact integer polynomial arithmetic; generates the first eighteen coefficients via two different methods; directly checks the defining subsequence predicate by exhaustive enumeration at \(m=1,2,3\); and checks all six permutations at \(m=1,2\). Its recorded output is `check_output.txt`. The definition-level length spectra for the first three powers are \((2:6)\), \((3:10,4:6)\), and \((4:15,5:30,6:1)\). The infinite formula follows from the proof and symbolic polynomial identities, not from finite enumeration.

## Relationship to prior work
Kosche, Koß, Manea and Siemer introduce minimal absent subsequences, prove general characterizations, and explicitly investigate the same repeated ordered-permutation family (their \(B_k\)); their Proposition 3.6 contrasts polynomially many shortest absent subsequences with an exponentially large subset of minimal absent subsequences for sufficiently large even alphabet. They also identify all *shortest* absent subsequences of the family. The present result does **not** claim those facts as new; it gives the complete local MAS test and an exact rational enumeration of **all** minimal absent subsequences for the smallest nonbinary alphabet, together with a length-refined transfer formula. Li, Wang and Fu analyze deletion balls of periodic \(q\)-ary strings, including the repeated-permutation maximizers. Their deletion-ball cardinalities by length do not determine minimality under deletion of an additional symbol and do not provide the MAS enumerator established here. An exact binary alternating-power MAS enumeration is also known; the two-letter specialization is not claimed here as new. Its binary formula does not imply the three-letter rational series by relabeling or parameter substitution. These are statement-level differences rather than merely different terminology.

## Limitations
The explicit one-variable rational coefficients are given for alphabet size three; for arbitrary finite alphabets the result gives an exact finite-matrix expression, not a similarly simplified scalar formula. The work does not prove any code-theoretic optimality or a new general bound on MAS size. Earlier general characterizations can algorithmically enumerate MAS for each individual input word. No independent expert audit has been conducted, and unindexed or differently formulated prior exact enumerations remain a possible originality risk.

## References
1. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968 (first posted 2021-08-31), *Fundamenta Informaticae* 189 (2023), 199–240; especially Section 3 and Proposition 3.6. https://arxiv.org/pdf/2108.13968
2. H. Li, X. Wang, F.-W. Fu, *On the Number of Subsequences in the Nonbinary Deletion Channel*, arXiv:2601.06493 (first posted 2026-01-10), especially Sections I, IV and V. https://arxiv.org/pdf/2601.06493
3. D. Adamson, P. Fleischmann, A. Huch, *(Sets of) Complement Scattered Factors*, arXiv:2603.20790 (first posted 2026-03-21); a related but distinct complement-after-deletion operation. https://arxiv.org/pdf/2603.20790
