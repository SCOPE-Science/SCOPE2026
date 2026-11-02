# Exact binary valuations of shifted Narayana numbers and a sharp counting law

## Finding
Let the Narayana sequence be defined by \(a_0=0\), \(a_1=a_2=1\), and \(a_{n+3}=a_{n+2}+a_n\) for every \(n\geq0\). For every integer \(n\geq0\), its shifted term has the exact binary valuation
\[
\nu_2(a_n+1)=
\begin{cases}
0,&n\bmod 7\in\{0,4,6\},\\
1,&n\bmod 7\in\{1,2\},\\
2,&n\equiv5\pmod {14},\\
1,&n\equiv12\pmod {14},\\
1+\nu_2((n+4)/7),&n\equiv3\pmod7.
\end{cases}
\]
The argument \((n+4)/7\) in the last case is a positive integer. In particular all nonnegative valuations occur.

Define \(C_t(N)=\#\{0\le n<N:\nu_2(a_n+1)=t\}\), for integers \(N,t\geq0\). With
\[
p_t=\begin{cases}
3/7,&t=0\text{ or }t=1,\\
3/28,&t=2,\\
1/(7\cdot2^t),&t\geq3,
\end{cases}
\]
all natural densities exist and, **uniformly in both \(N\) and \(t\)**,
\[
\boxed{|C_t(N)-p_tN|\leq9/7.}
\]
This discrepancy constant is optimal: at \(t=1\) and \(N=4\) the difference is \(9/7\).

## Assumptions and scope
The sequence starts at index zero with the normalization above, not the alternative convention beginning with three ones. The valuation \(\nu_2(m)\) is the exponent of two in a nonzero positive integer \(m\). The formula covers all \(n\geq0\), with no asymptotic qualification. The counting variable \(N\) is a nonnegative integer, and the limiting density \(p_t\) is for each fixed \(t\). The displayed error is nevertheless uniform in \(t\).

## Proof
Set \(w_n=(a_n,a_{n+1},a_{n+2})^{\mathsf T}\) and
\[
M=\begin{pmatrix}0&1&0\\0&0&1\\1&0&1\end{pmatrix},\qquad w_{n+1}=Mw_n.
\]
Since \(\det M=1\), this recurrence extends integrally to negative indices. Direct back substitution gives \(w_{-4}=(-1,0,1)^{\mathsf T}\). Exact integer multiplication yields
\[
M^7=\begin{pmatrix}3&2&4\\4&3&6\\6&4&9\end{pmatrix}=I+2C,
\quad C=\begin{pmatrix}1&1&2\\2&1&3\\3&2&4\end{pmatrix},
\]
and
\[
M^{14}=I+4B,
\quad B=\begin{pmatrix}10&7&15\\15&10&22\\22&15&32\end{pmatrix}.
\]
The first coordinates of \(Cw_{-4}\) and \(Bw_{-4}\) are respectively \(1\) and \(5\).

First consider \(n\equiv3\pmod7\), and write \(n=7s-4\) for a uniquely determined positive integer \(s\). The zeroth coordinate of \(M^{7s}w_{-4}\) equals \(a_n\). If \(s\) is odd, the binomial expansion of \((I+2C)^s\) modulo four gives
\[
a_n+1\equiv2s\pmod4,
\]
so \(\nu_2(a_n+1)=1\). If \(s\) is even, put \(m=s/2\). For every positive integer \(m\) and integral matrix \(B\), the binomial expansion implies
\[
(I+4B)^m\equiv I+4mB\pmod{2^{\nu_2(m)+3}}.
\]
Indeed, for \(j\geq2\), \(\nu_2(4^j\binom mj)\geq 2j+\nu_2(m)-\nu_2(j)\geq\nu_2(m)+3\). Consequently
\[
a_n+1\equiv20m\pmod{2^{\nu_2(m)+3}},
\]
which has exact valuation \(\nu_2(m)+2=\nu_2(s)+1\), since the leading coefficient \(5\) is odd. This proves the nonperiodic branch.

For the remaining residues, \(M^{14}\equiv I\pmod4\) gives the following values of \(a_n+1\) modulo four, indexed by \(n\bmod14\) from zero to thirteen:
\[
(1,2,2,2,3,0,1,3,2,2,0,1,2,1).
\]
Only the residue \(n\equiv5\pmod {14}\) requires distinguishing valuation two from higher valuations, because the other zero entry corresponds to the branch just proved. Here \(w_5=(3,4,6)^{\mathsf T}\), the first coordinate of \(Bw_5\) is \(148\), and \(a_5+1=4\). Since \((I+4B)^m\equiv I+4mB\pmod8\), every index \(n=14m+5\) satisfies \(a_n+1\equiv4\pmod8\). The valuation classification follows.

For counting, valuation zero is exactly the six residue classes \(\{0,4,6,7,11,13\}\pmod{14}\); valuation one consists of \(\{1,2,3,8,9,12\}\pmod{14}\). Valuation two consists of \(\{5,10,19\}\pmod {28}\). For every \(t\geq3\), valuation \(t\) consists of the **single** residue class
\[
n\equiv 7\cdot2^{t-1}-4\pmod{7\cdot2^t}.
\]
These are disjoint exact classifications, so their densities are \(p_t\) as claimed. For a single residue class modulo any positive modulus the error in counting positions below \(N\) is strictly less than one. For the finite sets of residues above, direct enumeration of only \(0\leq N<14\) or \(0\leq N<28\) yields, respectively, the exact discrepancy ranges
\[
[-5/7,4/7],\qquad[-3/7,9/7],\qquad[-15/28,6/7].
\]
Translation by a full period does not change the discrepancy. Combining these finite bounds with the less-than-one bound for \(t\geq3\) proves the asserted uniform constant. Finally \(\nu_2(a_n+1)=1\) at \(n=1,2,3\), while it is zero at \(n=0\). Thus \(C_1(4)=3\), giving the sharp discrepancy \(3-4(3/7)=9/7\).

## Verification
Running `python3 verify.py` checks both displayed integer matrix identities and the two critical matrix-vector coefficients. It independently computes the sequence modulo \(2^{24}\) through index \(100000\), compares all \(100001\) resulting valuations with the classification, checks selected indices with modular binary matrix exponentiation, computes the exact periodic discrepancy extrema using rational arithmetic, and checks the high-valuation progressions for nineteen levels. The verifier prints `VERIFY_OK` on success. Finite checks independently support the exact identities but the infinite conclusions follow from the preceding proof.

## Relationship to prior work
Ismail, Rihane and Anwar (2022) study the same shifted numbers \(a_n\pm1\), but characterize **3-adic** rather than binary valuations; their Theorem 3.6 does not entail the binary result. Ji, Yang and Cai (2022, Section 2.1) establish lower bounds for binary valuations of **unshifted** Narayana numbers, used in a different Diophantine application; those bounds do not determine \(\nu_2(a_n+1)\). Lin (2021) develops negative-index recurrence identities without the exact binary valuation law or uniform counting theorem. These distinctions concern implications of actual statements, not merely different titles. No claim of absolute bibliographic priority or independent external validation is made.

## Limitations
The result is restricted to the shifted sequence \(a_n+1\) at the prime two. It neither classifies the binary valuations of \(a_n-1\) (which vanishes at several small indices), nor those of unshifted Narayana numbers, nor valuations at other primes. A prior equivalent statement in unindexed sources cannot be categorically excluded. The verification program checks finite cases; the full theorem relies on the exact matrix proof.

## References
1. M. Ismail, S. Rihane and M. Anwar, *Narayana Sequence and The Brocard–Ramanujan Equation*, arXiv:2206.09174, first publicly posted 18 June 2022. https://arxiv.org/abs/2206.09174
2. Y. Ji, P. Yang and T. Cai, *On Diophantine Equations Related to Narayana's Cows Sequence and Double Factorials or Repdigits*, *Symmetry* **14** (2022), 2004, https://doi.org/10.3390/sym14102004.
3. X. Lin, *On the Recurrence Properties of Narayana’s Cows Sequence*, *Symmetry* **13** (2021), 149, https://doi.org/10.3390/sym13010149.
4. OEIS A000930, *Narayana's cows sequence*, https://oeis.org/A000930 (sequence normalization differs by an index shift).
