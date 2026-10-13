# Two-prime-support classification of proper-divisor-sum practical numbers

## Finding

Let \(s(m)=\sigma(m)-m\), where \(\sigma\) is the ordinary divisor-sum function. Call a positive integer \(N\) **\(s\)-practical** if every integer between \(0\) and \(S_s(N)=\sum_{d\mid N}s(d)\) is a subset sum of the multiset \(\{s(d):d\mid N\}\), taking at most one summand for each positive divisor \(d\).

**Theorem.** For every odd prime \(p\) and integers \(a,b\ge1\), the number \(N=2^a p^b\) is \(s\)-practical if and only if exactly one of the following alternatives holds:

\[
\begin{aligned}
&p=3\quad\text{and}\quad
[(a\ge4,\ b\ge1)\ \text{or}\ (a\ge3,\ b\ge2)\ \text{or}\ (a\ge2,\ b\ge3)];\\
&p=5\quad\text{and}\quad
[(a\ge4,\ b\ge2)\ \text{or}\ (a\ge3,\ b\ge3)].
\end{aligned}
\]

In particular, the only allowable odd prime factors in this two-prime-support family are \(3\) and \(5\), and the minimal exponent pairs are \((2,3),(3,2),(4,1)\) for \(p=3\) and \((3,3),(4,2)\) for \(p=5\).

## Assumptions and scope

The theorem quantifies over **all** positive exponents \(a,b\) and **all** odd primes \(p\). It does not classify \(s\)-practical numbers with only one prime factor, with two odd prime factors, or with at least three distinct prime factors. Repeated values of \(s(d)\) are counted separately because the corresponding divisors are distinct. The zero weight \(s(1)=0\) does not affect subset sums.

## Proof

**1. Exact divisor weights and a subset-sum criterion.** For \(i,j\ge0\), put

\[
F_p(i,j)=s(2^ip^j)
=\frac{((p+1)2^i-p)p^j-(2^{i+1}-1)}{p-1}.
\]

The formula follows directly from \(\sigma(2^ip^j)=(2^{i+1}-1)(p^{j+1}-1)/(p-1)\). Define \(S_p(a,b)=\sum_{i=0}^{a}\sum_{j=0}^{b}F_p(i,j)\). Given nonnegative integer weights \(w_1\le\cdots\le w_t\), their subset sums fill the entire interval from \(0\) to \(\sum_jw_j\) if and only if \(w_1\le1\) and \(w_k\le1+\sum_{j<k}w_j\) for all \(k\ge2\). Indeed, each new weight extends the previously filled interval exactly when it meets this inequality; if it fails, the first missing integer cannot be attained by any larger weight.

**2. Necessary small-weight obstructions.** For \(a=1\) and any odd \(p\), the only positive weights below \(3\) are \(s(2)=s(p)=1\); therefore \(3\) is missing. Suppose \(a\ge2\). Then the weights \(1,1,3\) arise from divisors \(2,p,4\). If \(p\ge7\), every other weight is at least \(7\), so \(6\) is missing. Thus only \(p=3,5\) remain.

For \(p=3\), direct application of the finite greedy criterion gives the following first missing integers: \(12\) for \((a,b)=(2,1)\), \(53\) for \((2,2)\), and \(35\) for \((3,1)\). These, together with \(a=1\), exhaust the exponent pairs outside the three claimed upper quadrants.

For \(p=5\), the pair \((a,b)=(3,2)\) has first missing integer \(259\). For every \(a\ge2\) and \(b=1\), the weights \(1,1,3\) are followed by weights at least \(7\), so \(6\) is missing. For every \(a=2\) and \(b\ge2\), the only positive weights below \(20\) are \(1,1,3,6,8\), whose total is \(19\); hence \(20\) is missing. Together with \(a=1\), these cases exclude precisely the complement of the two claimed upper quadrants.

**3. Five complete base certificates.** Sorting the weights \(F_p(i,j)\), the greedy criterion verifies the following five pairs. Each row records \((p,a,b)\), the complete value \(S_p(a,b)\), and the sorted weights (including \(0\)):

- \((3,2,3)\): \(358\); \(0,1,1,3,4,6,13,16,21,55,66,172\).
- \((3,3,2)\): \(273\); \(0,1,1,3,4,6,7,16,21,36,55,123\).
- \((3,4,1)\): \(161\); \(0,1,1,3,6,7,15,16,36,76\).
- \((5,3,3)\): \(2704\); \(0,1,1,3,6,7,8,22,31,43,50,117,218,265,592,1340\).
- \((5,4,2)\): \(1205\); \(0,1,1,3,6,7,8,15,22,43,50,106,117,265,561\).

Each listed sequence satisfies the stated greedy inequalities, so all five numbers are \(s\)-practical. The remaining task is to propagate completeness to **all** greater exponents without relying on finite sampling.

**4. Adding whole divisor rows and columns.** Set

\[
H_j=\frac{(p+1)p^j-2}{p-1},\qquad
K_j=\frac{p^{j+1}-1}{p-1},\qquad
U_a=2^{a+1}-1.
\]

Then \(F_p(i,j)=2^iH_j-K_j\) and \(S_p(a,b)=U_a\sum_{j=0}^{b}H_j-(a+1)\sum_{j=0}^{b}K_j\).

Assume the old rectangle \(0\le i\le a,0\le j\le b\) is complete. To add the row \(i=a+1\), insert its weights in order \(j=0,1,\ldots,b\). The quantities \(F_p(a+1,j)-\sum_{t<j}F_p(a+1,t)\) increase with \(j\), since their successive difference is

\[
F_p(a+1,j+1)-2F_p(a+1,j)
=\frac{((p+1)2^{a+1}-p)(p-2)p^j+(2^{a+2}-1)}{p-1}>0.
\]

Thus the single condition \(M_R(a,b)\ge0\), where

\[
M_R(a,b)=S_p(a,b)+1-
\left(F_p(a+1,b)-\sum_{j<b}F_p(a+1,j)\right),
\]

suffices to make the enlarged rectangle complete. Similarly, inserting the new column \(j=b+1\) in order \(i=0,1,\ldots,a\) is valid if

\[
M_C(a,b)=S_p(a,b)+1-
\left(F_p(a,b+1)-\sum_{i<a}F_p(i,b+1)\right)\ge0.
\]

Indeed, consecutive column gaps differ by \(F_p(i+1,b+1)-2F_p(i,b+1)=K_{b+1}>0\).

**5. Monotonic margins.** For \(p=3\) on \(a\ge2,b\ge1\), and for \(p=5\) on \(a\ge3,b\ge1\), **both** \(M_R\) and \(M_C\) increase strictly under either unit increment of \(a\) or \(b\). Here are algebraic checks for the unbounded ranges.

The increments in \(a\) are

\[
\begin{aligned}
M_R(a+1,b)-M_R(a,b)&=2^{a+2}\sum_{j<b}H_j-\sum_{j\le b}K_j,\\
M_C(a+1,b)-M_C(a,b)&=\sum_{j\le b}F_p(a+1,j)-K_{b+1}.
\end{aligned}
\]

For \(j\ge0\), \(K_j\le H_j\), while \(K_b\le(p+1)H_{b-1}\) when \(b\ge1\). Therefore \(\sum_{j\le b}K_j\le(p+2)\sum_{j<b}H_j\), and the first displayed increment is positive because \(2^{a+2}\ge16>p+2\). Each \(F_p(a+1,j)\) includes the proper divisors \(p^j,2p^j,\ldots,2^ap^j\), so it is at least \((2^{a+1}-1)p^j\). As \(K_b=\sum_{j=0}^bp^j\) and \(K_{b+1}=pK_b+1\), the second increment is positive as well.

The increments in \(b\), obtained by substituting the explicit formulas for \(F_p\) and \(S_p\), are

\[
\begin{aligned}
M_R(a,b+1)-M_R(a,b)
&=\frac{p^b[2(p+1)U_a-(a+1)p^2-(p-2)]-(4U_a-a)}{p-1},\\
M_C(a,b+1)-M_C(a,b)
&=\frac{p^{b+1}[(p+1)U_a-ap^2-2p+1]-(2U_a-a-1)}{p-1}.
\end{aligned}
\]

Both numerators increase with \(a\) and \(b\) on the stated domains: their coefficients of \(p^b\) and \(p^{b+1}\) are positive and increasing in \(a\). Their increments in \(a\) are, respectively,

\[
\begin{aligned}
&p^b[2(p+1)2^{a+1}-p^2]-(4\cdot2^{a+1}-1),\\
&p^{b+1}[(p+1)2^{a+1}-p^2]-(2\cdot2^{a+1}-1),
\end{aligned}
\]

which are positive and increasing from the lower corners \((p,a,b)=(3,2,1)\) and \((5,3,1)\). At these corners the two \(b\)-increments \((\Delta_bM_R,\Delta_bM_C)\) are \((29,17)\) and \((82,31)\), respectively, proving strict positivity everywhere in the relevant domains.

Finally, the five complete base rectangles from step 3 have respective margin pairs

\[
(141,77),\quad(106,141),\quad(37,106),\quad(551,206),\quad(302,551).
\]

All margins are positive; their monotonicity guarantees that every subsequent addition of a row or column preserves completeness. The union of the five resulting upper quadrants is exactly the set asserted in the theorem. Combining this with step 2 proves both directions for all allowable parameters. \(\square\)

## Verification

Run `python3 verify_s_practical.py`. The script (Python standard library only) independently evaluates proper-divisor sums by enumerating divisors in small cases, checks all five complete base lists and their margins, verifies explicit excluded parameter pairs, compares the theorem with greedy classifications for hundreds of rectangles, and tests the algebraic margin-difference identities. Its replay output is in `verify-output.txt`. The finite checks are not presented as a proof of the infinite classification: steps 4–5 prove closure for every exponent.

## Relationship to prior work

Schwab and Thompson introduced \(f\)-practical numbers and proved that the \(s\)-practical set has natural density zero; their Section 6 establishes infinitude using prime numbers, not a two-prime-support classification. Aidun and Thompson's 2026 work on \(S_s(n)\) proves distributional and moment results, not this discrete completeness criterion. OEIS A393492 explicitly tabulates \(s\)-practical numbers, including initial composite examples, but a finite table does not prove the theorem for all exponents. Other classifications for ordinary practical, \(\lambda^*\)-practical and \(\varphi\)-practical integers use different weights and do not imply the displayed classification.

## Limitations

The statement is restricted to exact prime support \(\{2,p\}\). No asymptotic for the full set of \(s\)-practical numbers, or classification at larger prime support, follows. The 2026 thesis by Anniek Reuijl, *Representing integers with sums of proper divisors*, is directly relevant; its bibliographic information and OEIS-linked claims were checked, but its full text could not be accessed. Possible unpublished or unindexed prior coverage remains an originality risk. The reported review is not an independent audit.

## References

1. N. Schwab and L. Thompson, *A generalization of the practical numbers*, arXiv:1701.08504, Section 6 (2017 preprint; journal 2018).
2. I. Aidun and L. Thompson, *A statistical investigation of a divisor-sum function*, arXiv:2604.05284, first submitted 2026-04-07 (2026).
3. OEIS A393492, *S-practical numbers*, initially authored by A. Eldar 2026-02-16; online tabulation and references.
4. A. Reuijl, *Representing integers with sums of proper divisors*, Utrecht University Master's thesis (2026), bibliographic record and OEIS reference; full text not inspected.
