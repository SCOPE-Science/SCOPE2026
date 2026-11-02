# An exact ternary-language criterion for nine dividing central trinomial numbers

## Finding
Let \(T_n=[x^0](x^{-1}+1+x)^n\) for every integer \(n\ge0\). Write \(s_3(n)\) for the usual base-three digit string, most significant digit first (and \(s_3(0)=0\)). Then
\[
9\mid T_n\quad\Longleftrightarrow\quad
\begin{cases}
\text{there are at least two digits }2\text{ in }s_3(n),\\
\text{or there is exactly one digit }2,\text{ immediately preceded by }1,\text{ and followed by at least one digit.}
\end{cases}
\]
The second alternative is equivalently the occurrence of \(120\) or \(121\) with no other digit \(2\) in the expansion. For every integer \(k\ge2\), the exact number of \(0\le n<3^k\) satisfying \(9\mid T_n\) is
\[
\boxed{3^k-(k+6)2^{k-2}}.
\]
For \(k=1\) the count is zero. In particular, the set \(\{n\ge0:9\mid T_n\}\) has natural density one, and the number of exceptions below each power of three is exactly \((k+6)2^{k-2}\).

## Assumptions and scope
All integers \(n\) and \(k\) are quantified above. The coefficient extraction takes the constant Laurent coefficient. A leading zero may be added to the ternary expansion without changing the criterion. The assertion concerns divisibility by precisely the modulus \(9\), not exact \(3\)-adic valuations above one.

## Proof
Put \(A(x)=x^{-1}+1+x\). A direct identity in \(\mathbb Z[x,x^{-1}]\) is
\[
A(x)^3=A(x^3)+3Q(x),\qquad
Q(x)=x^{-2}+2x^{-1}+2+2x+x^2.
\]
For \(m\ge1\) and \(r\in\{0,1,2\}\), expand
\[
A(x)^{3m+r}=\big(A(x^3)+3Q(x)\big)^m A(x)^r
\]
modulo \(9\). Terms containing two copies of \(3Q\) vanish. For an integer \(j\ge0\) let \(c_j=[x^j]A(x)^{m-1}\); symmetry gives \(c_{-j}=c_j\). The constant coefficient of \(A(x^3)^{m-1}Q(x)A(x)^r\), for \(r=0,1,2\), is respectively
\[
2T_{m-1},\qquad 6T_{m-1}+2c_1,
\qquad16T_{m-1}+8c_1.
\]
Indeed only degrees divisible by three contribute. Since \(2c_1=T_m-T_{m-1}\), these are \(2T_{m-1}\), \(T_m+5T_{m-1}\), and \(4T_m+12T_{m-1}\). The zero-correction baseline is respectively \(T_m,T_m,3T_m\). Therefore
\[
\begin{aligned}
T_{3m}&\equiv T_m+6mT_{m-1}&&\pmod9,\\
T_{3m+1}&\equiv T_m+3m(T_m+5T_{m-1})&&\pmod9,\\
T_{3m+2}&\equiv 3(m+1)T_m&&\pmod9.
\end{aligned}
\tag{1}
\]
The initial values are \(T_0=T_1=1\) and \(T_2=3\). Reduction of (1) modulo \(3\) gives \(T_{3m}\equiv T_{3m+1}\equiv T_m\pmod3\) and \(T_{3m+2}\equiv0\pmod3\), also valid in the base cases. Thus
\[
T_u\equiv1\pmod3\text{ if }s_3(u)\text{ has no digit }2,
\quad T_u\equiv0\pmod3\text{ otherwise}.
\tag{2}
\]

We now read the digits from left to right. When a prefix \(m\) contains no digit \(2\), its extension ending in the first digit \(2\) has \(T_{3m+2}\equiv3(m+1)\pmod9\) by (1) and (2); this also holds for \(m=0\) using \(T_2=3\). Since \(m\bmod3\) is \(0\) or \(1\), this value is not divisible by \(9\). If a digit \(0\) or \(1\) is then appended, the prefix \(u=3m+2\) has \(u\equiv2\pmod3\), \(T_u\equiv0\pmod3\), and \(T_{u-1}\equiv1\pmod3\). In either of the first two recurrences, its difference from \(T_u\) is therefore \(3\pmod9\), so the new value becomes \(3(m+2)\pmod9\). All further appends of \(0\) or \(1\) leave this residue unchanged: for any current prefix \(u\) with a digit \(2\) somewhere above its units position, the correction in the first two recurrences vanishes modulo \(9\). If \(u\equiv0\pmod3\), the factor \(3u\) supplies \(9\); if \(u\equiv1\pmod3\), then \(u-1\) still has a digit \(2\), so \(T_{u-1}\equiv0\pmod3\), and \(T_u\equiv0\pmod3\) as well. The first condition is precisely \(m\equiv1\pmod3\), i.e. the digit just before the unique \(2\) is \(1\); a lower digit must exist for the extra \(3\) to arise.

Finally, after any second digit \(2\) is appended, the last recurrence in (1) multiplies an already \(3\)-divisible central trinomial value by \(3\), giving \(0\pmod9\). Further digits \(2\) preserve this. An append of \(0\) or \(1\) also preserves zero modulo \(9\): the correction vanishes if the old prefix \(u\equiv0\pmod3\), and otherwise \(u-1\) retains a digit \(2\) (the earlier one if the final digit of \(u\) is \(2\)), so both \(T_u\) and \(T_{u-1}\) are divisible by \(3\). This proves both alternatives and their converse, for all digit-string lengths.

For the count, among the \(3^k\) padded length-\(k\) ternary strings, those with at least two digits \(2\) number
\[
3^k-2^k-k2^{k-1}.
\]
Those with exactly one digit \(2\) and with immediately preceding digit \(1\) and at least one following digit have \(k-2\) possible positions for that \(2\), with all other \(k-2\) digits independently \(0\) or \(1\), giving \((k-2)2^{k-2}\) strings. Adding yields \(3^k-(k+6)2^{k-2}\). Since \((k+6)2^{k-2}=o(3^k)\), this implies natural density one: for arbitrary cutoffs between successive powers of three, the exceptional fraction is bounded by a constant multiple of \(k(2/3)^k\). \(\square\)

## Verification
A standalone standard-library Python program, `verify_trinomial_mod9.py`, calculates the first \(6561\) central trinomial numbers by the exact integer recurrence
\[
(n+1)T_{n+1}=(2n+1)T_n+3nT_{n-1}\quad(n\ge1).
\]
It compares every one of those terms modulo \(9\) with the digit criterion; checks (1) at \(2185\) admissible indices; and checks the count formula for every \(2\le k\le8\). It returns `VERIFY_OK terms=6561 zeros=5665 recurrences=2185 closed_counts=2..8`. The proof above, rather than these bounded computations, establishes the infinite statement.

## Relationship to prior work
Deutsch and Sagan's mod-\(3\) digit criterion is cited as Theorem 7 in Rampersad and Shallit (2022), Section 3; it detects the presence of a digit \(2\) but does not distinguish multiplicity-one from multiplicity-two cases modulo \(9\). Rowland and Yassawi (2014), Section 4.2, compute a central-trinomial automaton modulo \(4\) and develop general prime-power automaton methods, but do not give this ternary mod-\(9\) language or its exact counting polynomial. Hou and Li (2023), Theorems 1.2–1.3, treat congruences of sums of products of central trinomial numbers, a distinct statistic. Mikić (2023) studies divisibility of generalized trinomial coefficients by their parameter and valuations of central Delannoy numbers; the ordinary specialization has parameter \(1\), so it does not yield this mod-\(9\) characterization.

## Limitations
The criterion addresses divisibility by \(9\), not \(27\) or the full \(3\)-adic valuation. Earlier general automaton algorithms may compute the same residue set implicitly; a complete bibliographic priority claim is not made. No independent mathematical review is claimed.

## References
1. Q.-H. Hou and N. Li, *Reduction on the congruences of partial sums of P-recursive sequences*, arXiv:2312.13613 (first publicly posted 2023-12-21), Theorems 1.2–1.3.
2. N. Rampersad and J. Shallit, *Congruence Properties of Combinatorial Sequences via Walnut and the Rowland–Yassawi–Zeilberger Automaton*, Electronic Journal of Combinatorics 29(3), #P3.36 (2022), Section 3, Theorem 7; arXiv:2110.06244.
3. E. Rowland and R. Yassawi, *Automatic congruences for diagonals of rational functions*, Journal de Théorie des Nombres de Bordeaux 27 (2015), 245–288, Section 4.2; arXiv:1310.8635, first version 2013.
4. J. Mikić, *On new divisibility properties of generalized central trinomial coefficients and Legendre polynomials*, arXiv:2311.14623 (2023), Theorems 5 and 8.
