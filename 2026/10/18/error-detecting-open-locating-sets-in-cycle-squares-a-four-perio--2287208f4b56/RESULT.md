# Error-detecting open locating sets in cycle squares: a four-periodic law and complete enumerator

## Finding

Let \(G_n=C_n^2\) be the second power of the cycle, on \(\mathbb Z/n\mathbb Z\): vertices are adjacent when their cyclic separation is one or two. Let \(F_n(z)\) enumerate all error-detecting open-locating-dominating (DET:OLD) vertex sets \(S\), with weight \(z^{|S|}\).

**Structure and full polynomial.** For every \(n\ge12\), the complement \(X=V(G_n)\setminus S\) is an independent set in the circulant \(H_n=C_n(1,2,5,6,7)\) if and only if \(S\) is DET:OLD. Consequently
\[
F_n(z)=z^n I(H_n;z^{-1})=z^n\operatorname{tr}(T(z^{-1})^n),\qquad n\ge12,
\]
where \(I\) is the independence polynomial and the explicit \(128\)-state transfer matrix \(T\) is described below. The formula determines **every coefficient**, not only the minimum.

**Minimum and its multiplicity.** If \(\delta_n\) is the minimum DET:OLD cardinality, then no DET:OLD set exists for \(3\le n\le7\), and
\[
\delta_8=7,\quad\delta_9=8,\quad\delta_{10}=9,\quad\delta_{11}=9;
\qquad
\delta_n=\begin{cases}3n/4,&4\mid n,\\n-\lfloor n/4\rfloor+1,&4\nmid n,\end{cases}\quad n\ge12.
\]
Writing \(m_n\) for the number of distinct labeled minimum sets, we have \(m_n=n\) for \(8\le n\le11\); for \(n\ge12\),
\[
m_n=\begin{cases}
4,&4\mid n,\\
2n,&n\in\{13,14,15\},\\
3n/2,&n=22,\\
3n,&n=23,\\
2n,&n\equiv3\pmod4,\\
n,&\text{otherwise}.
\end{cases}
\]
The cases are disjoint in the displayed order. Small-order polynomials are \(F_n=0\) for \(3\le n\le7\), and
\[
F_8=z^8+8z^7,\quad F_9=z^9+9z^8,\quad
F_{10}=z^{10}+10z^9,\quad F_{11}=z^{11}+11z^{10}+11z^9.
\]

## Assumptions and scope

All graphs are finite, simple and undirected. Cycle powers use distinct neighbors, including at the small orders. For each vertex \(v\), write \(N_S(v)=N(v)\cap S\). A set \(S\) is DET:OLD if \(|N_S(v)|\ge2\) for all \(v\), and for each pair \(u\ne v\), at least one of \(|N_S(u)\setminus N_S(v)|\) and \(|N_S(v)\setminus N_S(u)|\) is at least two. This is the established one-false-negative criterion of Seo--Slater, as stated in Jean--Seo (Theorem 1.1(iii)). An undefined minimum means no feasible set exists, not that its value is zero.

For \(n\ge12\), the graph \(H_n\) joins vertices whose difference lies in \(\{\pm1,\pm2,\pm5,\pm6,\pm7\}\pmod n\). Let \(D=\{1,2,5,6,7\}\). A cyclic gap between consecutive omitted vertices is their clockwise modular difference.

## Proof

**1. Exact complement characterization.** For \(n\ge12\), write indices modulo \(n\), with \(N(i)=\{i-2,i-1,i+1,i+2\}\). First suppose \(S\) is DET:OLD and put \(X=V\setminus S\). For the pair \(i,i+1\), the two exclusive neighborhoods are \(\{i-2,i+1\}\) and \(\{i,i+3\}\). Both have size two. If \(X\) contains one element from each, the pair cannot be distinguished twice in either direction. The four cross-differences, up to sign, are \(1,2,5\). Varying \(i\) forbids all omission pairs at those differences. For the pair \(i,i+3\), the exclusive neighborhoods are \(\{i-2,i-1\}\) and \(\{i+4,i+5\}\), whose four cross-differences are \(5,6,7\). Thus \(X\) is independent in \(H_n\).

Conversely, assume \(X\) is independent in \(H_n\). Any three members of the four-element set \(N(i)\) contain two separated by one or two; therefore \(|N(i)\cap X|\le2\), and \(S\) two-dominates every vertex. It remains to distinguish distinct vertices. By cyclic symmetry, their separation can be taken between one and \(\lfloor n/2\rfloor\). At separation one or three, the two exclusive neighborhoods above each have two elements. If both directions failed, there would be an omitted element on both sides, contrary to independence at a forbidden cross-difference. At separation two, the exclusive neighborhoods are
\[
A=\{i-2,i-1,i+2\},\qquad B=\{i,i+3,i+4\}.
\]
Failure of both directions would omit at least two elements from each. Since \(i-2,i-1\) are forbidden to be omitted together, the omission in \(A\) must include \(i+2\); since \(i+3,i+4\) are forbidden together, the omission in \(B\) must include \(i\). Those two are separated by two, contradiction. At separation four, the exclusive neighborhoods are
\[
A=\{i-2,i-1,i+1\},\qquad B=\{i+3,i+5,i+6\}.
\]
Double failure similarly forces omissions at \(i+1\) and \(i+3\), again forbidden. At separation at least five, the two open neighborhoods are disjoint (for \(n\ge12\)), so two-domination alone ensures both difference counts are at least two. This proves the equivalence.

**2. Complete polynomial by finite-memory transfer.** Index the matrix \(T(w)\) by all seven-bit states \(a\in\{0,1,\ldots,127\}\), where bit position zero records the most recent omission indicator, bit one the preceding indicator, and so on. From state \(a\), a zero indicator always permits a transition to \((2a)\bmod128\) with weight one. A one indicator permits a transition to \((2a+1)\bmod128\) with weight \(w\) exactly if all bit positions \(d-1\) for \(d\in D\) are zero in \(a\). Thus \(T_{a,b}(w)\) is the sum of these transition weights when their destination is \(b\), and zero otherwise.

For \(n\ge12\), closed walks of length \(n\) in this de Bruijn-type transition graph correspond bijectively to indexed cyclic binary omission words obeying all forbidden circular differences. The trace records each admissible word once, and the exponent of \(w\) is its number of omissions. Hence \(I(H_n;w)=\operatorname{tr}(T(w)^n)\) and the stated complete cardinality polynomial follows. This identity holds as a Laurent expression after substituting \(w=z^{-1}\), but \(F_n\) is an ordinary polynomial.

**3. Sharp minimum and optimal-set multiplicity.** Consider an independent omitted set \(X\) of \(t\ge3\) vertices. Its \(t\) positive clockwise successive gaps each lie in \(\{3,4\}\cup\{8,9,\ldots\}\). Two adjacent gaps from \(\{3,4\}\) cannot include a three, because their sum would be six or seven, a forbidden difference. In fact these conditions suffice for independence: the only sum of at least two allowed positive gaps that could lie in \(D\) is a sum of two small gaps, namely six or seven; all longer positive sums are at least eight, while complementary circular separations are also sums of consecutive gaps.

Let \(b\) count gaps at least eight and \(c\) count gaps equal to three. Then \(c\le b\) whenever \(b\ge1\), and
\[
n\ge 4t+4b-c.
\]
If \(b=0\), no gap of three is possible and all gaps are four, forcing \(n=4t\). If \(b=1\) and \(t\ge3\), no gap of three can have long gaps on both sides, so \(c=0\) and \(n\ge4t+4\). If \(b\ge2\), \(n\ge4t+3b\ge4t+6\). Therefore \(n=4t\) or \(n\ge4t+4\). Conversely, gaps all four realize \(n=4t\), and gaps \((8+r,4,\ldots,4)\), with \(r\ge0\), realize \(n=4t+4+r\). A set of two omissions is governed directly by its single pair separation. These facts yield maximum omission size \(n/4\) if \(4\mid n\), and \(\lfloor n/4\rfloor-1\) otherwise for all \(n\ge12\); direct checks of the small finite boundaries are described below.

For multiples of four, all optimal gaps are four, yielding four distinct translates. At orders thirteen through fifteen, exactly two omissions are possible, with cyclic separation three or four, giving \(2n\) distinct sets. At remaining nonmultiples \(n\ge16\), put \(t=\lfloor n/4\rfloor-1\), and write \(n=4t+4+r\) with \(r\in\{1,2,3\}\). There must be a long gap. If there is exactly one, it has size \(8+r\) and all other gaps are four, giving \(n\) labeled sets. If there are two long gaps, the inequality forces \(r=3\) and at least one gap of three. With exactly one three, the only cyclic pattern is \((8,3,8,4,\ldots,4)\), contributing another \(n\) sets. With two threes, both must neighbor both long gaps, which requires \(t=4\), with patterns \((8,3,8,3)\) at \(n=22\), or \((9,3,8,3)\) at \(n=23\). These contribute respectively \(n/2\) and \(n\) additional sets. Three long gaps are impossible because the required excess is at least nine. This gives the multiplicity formula, including the exceptional orders.

**4. Small orders.** For \(3\le n\le7\), even the full vertex set fails double distinction. One witness vertex pair is \((0,1)\) at orders three, four and five, and \((0,3)\) at orders six and seven. For \(n=8,9,10\), only the full set and the \(n\) single omissions satisfy the criterion. At order eleven, there are additionally exactly eleven two-omission sets: their omitted vertices have cyclic separation three. These finite classifications, also exhaustively checked by the attached program, give the four small-order polynomials.

## Verification

The standalone `verify.py` (Python standard library only) independently evaluates the defining neighborhood-difference predicates for **every** subset of \(G_n\) with \(3\le n\le16\). For \(12\le n\le16\), it separately evaluates circulant independence for every omission subset and compares the two Boolean predicates. It independently constructs and evaluates the \(128\)-state transfer for every \(12\le n\le40\), comparing exact optimum sizes, multiplicities, and where feasible complete coefficient distributions with direct enumeration. The resulting `verification_output.txt` ends in `VERIFY_OK`; rerun with `python verify.py`. Full finite enumeration is exhaustive only in the explicitly specified ranges. The infinite statements follow from the structural proof and trace bijection, not from extrapolated computations.

## Relationship to prior work

Seo and Slater introduced error-detecting open-locating sets as a sensor-error model; their 2015 treatment includes cycles \(C_n\), which do not have feasible DET:OLD sets, but not the cycle-square result proved here. Jean and Seo's 2023 paper gives the useful two-domination/two-asymmetric-distinction characterization, proves computational hardness, and studies extremal graphs, infinite grids and cubic graphs. Their results do not imply the circulant complement characterization, all-cardinality transfer polynomial or the finite-cycle-square extremal classification. Later work on error-correcting OLD sets uses a different fault model; ordinary identifying or locating codes on circulants likewise require different distinction conditions. Possible earlier equivalent formulations outside the inspected material are not excluded.

## Limitations

The result is restricted to the second power of a simple cycle, not all cycle powers or all circulants. The explicit \(128\)-state matrix is a finite algorithmic closed expression, not a closed product of linear factors. No independent external review or certification has been performed. The 2015 antecedent was accessed through available primary excerpts rather than a complete locally obtained PDF; unindexed historical duplication remains a research-literature risk. Small-order conclusions are independently checked by exhaustive computer enumeration, while every infinite assertion has a separate mathematical proof.

## References

- D. C. Jean and S. J. Seo, *On Error-detecting Open-locating-dominating Sets*, arXiv:2306.12583v1 (first public 21 June 2023), https://arxiv.org/abs/2306.12583 ; see Theorem 1.1 and Sections 2--5.
- S. J. Seo and P. J. Slater, *Fault Tolerant Detectors for Distinguishing Sets in Graphs*, Discussiones Mathematicae Graph Theory 35 (2015), 797--818, DOI:10.7151/DMGT.1838, particularly the cycle discussion (Theorem 3).
- D. C. Jean and S. J. Seo, *Open-locating-dominating sets with error correction*, arXiv:2307.16312v1 (2023), https://arxiv.org/abs/2307.16312 ; a different error-correction condition.
