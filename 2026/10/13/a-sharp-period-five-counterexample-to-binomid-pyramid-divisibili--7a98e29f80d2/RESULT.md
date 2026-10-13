# A sharp period-five counterexample to binomid-pyramid divisibility

## Finding

For any integer \(q\geq2\), define the positive integer sequence \(f\) by repeating the block
\[
(f_1,f_2,f_3,f_4,f_5)=(1,q,q,1,q^2),\qquad f_{n+5}=f_n\quad(n\geq1).
\]
Every column of the binomid triangle of \(f\) is itself binomid: equivalently, **the entire binomid pyramid has integer entries**. Nevertheless \(f\) is not a divisibility sequence, because \(2\mid4\) but \(f_2=q\nmid f_4=1\).

The period is sharp: **every positive-integer periodic sequence of period at most four that is binomid at every level is a divisibility sequence**. Therefore five is the least possible period of a positive-integer, nondivisible sequence whose binomid pyramid is integral. The statement concerns *pure* periodicity, not eventual periodicity.

## Assumptions and scope

All sequences are indexed by positive integers and have strictly positive integer values. For such a sequence \(h\) define the generalized coefficient
\[
\left[\!\begin{matrix}n\\k\end{matrix}\!\right]_h
=\frac{\prod_{i=n-k+1}^{n}h_i}{\prod_{i=1}^{k}h_i},\qquad 0\leq k\leq n,
\]
with empty products equal to one. Sequence \(h\) is *binomid* when all these numbers are integers. For every positive integer \(c\), column \(c\) is the sequence
\[
C_c(n)=\left[\!\begin{matrix}n+c-1\\c\end{matrix}\!\right]_h
=\frac{\prod_{i=n}^{n+c-1}h_i}{\prod_{i=1}^{c}h_i}\quad(n\geq1).
\]
The sequence is *binomid at every level* when every \(C_c\) is binomid. This is the binomid-pyramid property in Shapiro's terminology. A divisibility sequence satisfies \(h_d\mid h_n\) whenever \(d\mid n\). A period \(T\) means \(h_{n+T}=h_n\) for every positive \(n\), without requiring it to be the least period.

## Proof

**1. A finite cyclic criterion.** For any positive integer \(q>1\), an exponent word \(u=(u_1,\dots,u_T)\) of nonnegative integers, extended periodically, defines \(h_n=q^{u_n}\). It is binomid precisely when
\[
\sum_{i=0}^{k-1}u_{s+i}\ \geq\ \sum_{i=1}^{k}u_i
\quad\text{for every }k\geq1,\ s\geq1,
\]
where the left indices are periodic and \(s+i\) begins at \(s\). Indeed the difference of the two sums is exactly the exponent of \(q\) in \(\bigl[{s+k-1\atop k}\bigr]_h\). Write \(k=tT+r\) with \(0\leq r<T\). Every length-\(T\) block has the same sum. Thus the condition reduces *exactly* to the finitely many inequalities for \(1\leq r<T\), requiring the first length-\(r\) cyclic block to have minimum sum.

**2. All columns of the period-five family.** Write \(a=(0,1,1,0,2)\), so \(f_n=q^{a_n}\), with subscripts on \(a\) interpreted cyclically modulo five. The exponent of \(q\) in \(C_c(n)\) is
\[
b_{c,n}=\sum_{i=0}^{c-1}a_{n+i}-\sum_{i=1}^{c}a_i.
\]
A length-five block of \(a\) always sums to four, so \(b_{c+5,n}=b_{c,n}\); and \(b_{c,n+5}=b_{c,n}\). For \(c\equiv0\pmod5\), every exponent is zero. For the other four column residues, the complete exponent blocks \((b_{c,1},\ldots,b_{c,5})\) are
\[
\begin{array}{c|c|c}
c\pmod5&\text{column exponent block}&\text{initial block sums for lengths }1,2,3,4\\\hline
1&(0,1,1,0,2)&(0,1,2,2)\\
2&(0,1,0,1,1)&(0,1,1,2)\\
3&(0,0,1,0,1)&(0,0,1,1)\\
4&(0,2,1,1,2)&(0,2,3,4)
\end{array}
\]
All five cyclic block sums at each indicated length are at least the displayed initial sum; this is checked directly from the four displayed five-tuples. The criterion from step 1 therefore proves that **every column is binomid for every positive index and every column number**. Nonnegative exponents in the table also show that the columns' individual terms are integers. The nondivisibility \(f_2=q\nmid f_4=1\) is immediate. The block has least period five since its unique exponent two cannot repeat at a shorter period.

**3. The lower-period obstruction.** Let \(g\) be any positive-integer sequence with period \(T\leq4\) whose every binomid column is binomid. Fix an arbitrary prime \(p\) and let \(v_i=\nu_p(g_i)\). All generalized-coefficient integrality inequalities hold primewise. Column one begins \(g_n/g_1\), so its length-one binomid condition gives \(v_1\leq v_i\) for all \(i\). Write \(A=v_1\), \(B=v_2\), \(C=v_3\), and \(D=v_4\) when those positions exist.

For \(T=1\) the assertion is immediate. For \(T=2\), \(A\leq B\) implies \(g_1\mid g_2\); each odd index has value \(g_1\), and each even index has value \(g_2\), so \(g\) is divisible.

For \(T=3\), the prime-valuation exponent block of column two is
\[
(0,C-A,C-B).
\]
Its initial length-two sum \(C-A\) cannot exceed the cyclic length-two sum starting at its third position, \(C-B\). Hence \(B\leq A\), while column one gives \(A\leq B\). Thus \(A=B\) at **every prime**, implying \(g_1=g_2\mid g_3\). Every index outside the zero residue class modulo three has value \(g_1\), while the zero class has value \(g_3\). Consequently \(d\mid n\Rightarrow g_d\mid g_n\).

For \(T=4\), column one's length-three inequality comparing cyclic blocks \((1,2,3)\) and \((3,4,1)\) gives
\[
A+B+C\leq C+D+A\quad\Longrightarrow\quad B\leq D.
\]
Column three has prime-valuation exponent block
\[
(0,D-A,D-B,D-C).
\]
Its length-two initial block cannot exceed the cyclic length-two block starting at the fourth position. Thus \(D-A\leq D-C\), giving \(C\leq A\). Column one also gives \(A\leq C\), so \(C=A\). Since this holds for every prime, \(g_1=g_3\), \(g_1\mid g_2\mid g_4\). Odd-index values are \(g_1\); indices congruent to two modulo four have value \(g_2\); and multiples of four have value \(g_4\). Under multiplication of indices, a multiple of an odd index is unrestricted, of a two-mod-four index is either two or zero modulo four, and of a four-multiple is always zero modulo four. These statements imply divisibility in each case.

All possibilities \(T\leq4\) are exhausted. Combined with step 2, this proves both assertions. \(\square\)

## Verification

Run `python3 verify.py` from the extracted artifact directory. The script reconstructs each column exponent word from the original five-word (not from the theorem statement alone), checks each reduced cyclic inequality, rechecks the infinite periodic reduction's finite residue classes for 100 columns, enumerates bounded small-period valuation words as an auxiliary test, and checks direct column-binomial exponents for 258300 finite combinations. Its output is recorded in `verification_output.txt`. The infinite validity follows from the symbolic five-period reduction and lower-period primewise implications in the proof; the finite computations alone do not certify the infinite claims.

## Relationship to prior work

Shapiro, *Divisibility Properties for Integer Sequences* (arXiv:2302.02243v1; INTEGERS 23 (2023), A57), defines binomid sequences, the binomid pyramid, and the every-level property. Its Theorem 15 proves a sufficient condition from divisor-products to binomid-at-every-level, and its §4.4, Open Questions 27(2), asks about extending divisibility questions to higher-order linearly recurrent sequences. The example here has a recurrence \(f_{n+5}=f_n\), making the full-pyramid property insufficient to imply divisibility in that higher-order setting; the order-two question is not settled.

Caalim and Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index* (INTEGERS 24 (2024), A53), prove periodicity properties and describe binomid indices. Their statements concern first-level binomid integrality, not integrality of every column of the binomid pyramid or its shortest nondivisible period. Their follow-up, *On the monoid of lexicographically minimal extensions* (arXiv:2505.20018v1), refines first-level extension and monoid structure, also without this every-column classification. Those works explain why periodic binomid indices are natural comparison objects, but their statements do not subsume the two assertions proved here.

## Limitations

This result concerns **purely periodic sequences of positive integers** and the binomid-at-every-level property. It does not classify all period-five examples, all eventual-periodic examples, or order-two recurrences. No claim of external independent validation is made. As with any literature comparison, an equivalent result in unindexed sources may exist.

## References

1. D. B. Shapiro, *Divisibility Properties for Integer Sequences*, arXiv:2302.02243v1 (first public version 2023-02-04); *INTEGERS* 23 (2023), A57. https://arxiv.org/abs/2302.02243 ; https://math.colgate.edu/~integers/x57/x57.pdf
2. J. Caalim and Y.-i. Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, *INTEGERS* 24 (2024), A53. https://math.colgate.edu/~integers/y53/y53.pdf
3. J. Caalim and Y.-i. Tanaka, *On the monoid of lexicographically minimal extensions*, arXiv:2505.20018v1 (2025). https://arxiv.org/abs/2505.20018
