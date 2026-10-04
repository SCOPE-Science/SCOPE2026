# All dyadic multiples \(60\cdot 2^n\) are strongly pseudoperfect

## Finding
A positive integer \(N\) is strongly pseudoperfect if there is a subset \(S\) of its positive divisors such that
\[
d\in S\quad\Longleftrightarrow\quad \frac{N}{d}\in S
\]
and
\[
\sum_{d\in S}d=2N.
\]

For every integer
\[
n\ge0,
\]
the number
\[
60\cdot2^n
\]
is strongly pseudoperfect.

Thus the question posed by McCormack and Zelinsky asking whether every member of the family
\[
60,120,240,480,\ldots
\]
is strongly pseudoperfect has an affirmative answer.

## Assumptions and scope
Put
\[
a=n+2,\qquad N_a=15\cdot2^a.
\]
Then \(a\ge2\). Every divisor of \(N_a\) belongs to exactly one of the complementary divisor pairs
\[
P_i=\left\{2^i,15\cdot2^{a-i}\right\},
\qquad
Q_i=\left\{3\cdot2^i,5\cdot2^{a-i}\right\},
\qquad 0\le i\le a.
\]
Their pair-sums are
\[
p_i=2^i+15\cdot2^{a-i},
\qquad
q_i=3\cdot2^i+5\cdot2^{a-i}.
\]

It is therefore enough to specify, for each \(a\ge2\), a collection of the \(P_i\) and \(Q_i\) whose pair-sums total
\[
30\cdot2^a.
\]
The selected divisors are then automatically closed under \(d\mapsto N_a/d\).

## Proof
The following five constructions cover all sufficiently large \(a\), residue class by residue class modulo \(5\). Empty indexed unions are interpreted as empty.

For
\[
a=5r+4,\qquad r\ge0,
\]
select
\[
P_0,\ P_1,\ Q_0,\ Q_{a-1},
\]
and
\[
P_{4+5j}\qquad(0\le j\le r-1).
\]
Writing
\[
x=32^r,
\]
the fixed pair-sums contribute
\[
464x+16,
\]
while the indexed family contributes
\[
16(x-1).
\]
The total is
\[
480x=30\cdot2^{5r+4}.
\]

For
\[
a=5r+2,\qquad r\ge1,
\]
select
\[
P_0,\ P_1,\ P_{a-1},\ Q_0,\ Q_3,\ Q_{a-2},
\]
and, for \(1\le j\le r-1\),
\[
P_{5j+1},\ P_{5j+2},\ Q_{5j+3}.
\]
With \(x=32^r\), the fixed contribution is
\[
\frac{235x+160}{2},
\]
and the indexed contribution is
\[
\frac{5x-160}{2}.
\]
Hence the total is
\[
120x=30\cdot2^{5r+2}.
\]

For
\[
a=5r,\qquad r\ge2,
\]
select
\[
P_0,\ P_1,\ P_2,\ P_4,\ P_a,\ Q_{a-4},\ Q_{a-1},
\]
and
\[
P_{7+5j}\qquad(0\le j\le r-3).
\]
With \(x=32^r\), the fixed contribution is
\[
\frac{239x+1024}{8},
\]
and the indexed contribution is
\[
\frac{x-1024}{8}.
\]
Their sum is
\[
30x=30\cdot2^{5r}.
\]

For
\[
a=5r+1,\qquad r\ge2,
\]
select
\[
P_0,\ P_1,\ P_3,\ Q_2,\ Q_4,\ Q_{a-2},\ Q_a,
\]
together with
\[
P_{5j+1}\qquad(1\le j\le r-1)
\]
and
\[
P_{5j+4}\qquad(1\le j\le r-2).
\]
With \(x=32^r\), the fixed contribution is
\[
\frac{475x+768}{8},
\]
while the two indexed families together contribute
\[
\frac{5x-768}{8}.
\]
Thus the total is
\[
60x=30\cdot2^{5r+1}.
\]

For
\[
a=5r+3,\qquad r\ge2,
\]
select
\[
P_0,\ P_1,\ P_3,\ Q_2,\ Q_4,\ Q_5,\ Q_{a-2},\ Q_a,
\]
together with
\[
P_{5j+2}\qquad(1\le j\le r-1)
\]
and
\[
P_{5j}\qquad(2\le j\le r-1).
\]
With \(x=32^r\), the fixed contribution is
\[
\frac{955x+768}{4},
\]
and the indexed contribution is
\[
\frac{5x-768}{4}.
\]
The total is therefore
\[
240x=30\cdot2^{5r+3}.
\]

Each displayed indexed contribution follows from the finite geometric identity
\[
1+32+\cdots+32^{m-1}=\frac{32^m-1}{31}.
\]
For example, in the first residue class,
\[
\sum_{j=0}^{r-1}p_{4+5j}
=
16\sum_{j=0}^{r-1}32^j
+
480\sum_{j=0}^{r-1}32^j
=
16(x-1).
\]
The other four reductions are obtained in the same way by separating the \(2^i\) and \(2^{a-i}\) terms.

It remains only to cover the small values excluded by the ranges above. The following complementary-pair selections have the required total:
\[
\begin{array}{c|l}
a&\text{selected pairs}\\ \hline
2&P_0,P_2,Q_0,Q_2\\
3&P_0,P_1,P_2,P_3\\
5&P_0,P_1,P_4,P_5,Q_1,Q_4\\
6&P_0,P_1,P_5,Q_0,Q_2\\
8&P_0,P_1,P_7,Q_1,Q_4,Q_6,Q_8.
\end{array}
\]
The values \(a=4,7,9\) already fall under the residue-class formulas above.

Consequently every \(a\ge2\), hence every \(n\ge0\), has an explicit complement-closed divisor set summing to \(2N_a\). Therefore every \(60\cdot2^n\) is strongly pseudoperfect.

## Verification
The accompanying `verify.py` reconstructs every selected complementary pair from the formulas above. It verifies all five exceptional cases, checks the residue-class constructions for hundreds of values of \(r\), confirms that every selected object is a genuine divisor pair of \(15\cdot2^a\), checks complement closure at the divisor level, and verifies the exact sum
\[
\sum_{d\in S}d=30\cdot2^a.
\]

The verifier also checks the five algebraic fixed-plus-geometric reductions used in the proof:
\[
\begin{aligned}
(464x+16)+16(x-1)&=480x,\\
\frac{235x+160}{2}+\frac{5x-160}{2}&=120x,\\
\frac{239x+1024}{8}+\frac{x-1024}{8}&=30x,\\
\frac{475x+768}{8}+\frac{5x-768}{8}&=60x,\\
\frac{955x+768}{4}+\frac{5x-768}{4}&=240x.
\end{aligned}
\]
A successful replay prints `VERIFY_OK`.

The finite replay is a regression check. The all-\(n\) quantifier is proved by the five symbolic residue-class identities and the finite list of exceptional \(a\).

## Relationship to prior work
McCormack and Zelinsky introduced the term strongly pseudoperfect and, in the first public version of their paper, explicitly observed that
\[
60,120,240,480,960,1920,3840,7680,15360
\]
are strongly pseudoperfect. They then asked whether
\[
60\cdot2^n
\]
is strongly pseudoperfect for every \(n\ge0\).

Their paper was first public on 18 December 2023 and lists MSC classes \(11A05\), \(11A25\), and \(26D15\).

Wang and Zelinsky's September 2026 follow-up develops new infinite constructions and proves that there are infinitely many odd strongly pseudoperfect numbers. Its full text was inspected because it is the most relevant later source. It cites the McCormack--Zelinsky paper, discusses new constructions for numbers involving powers of \(2\), and tabulates \(60,120,240\), but it does not state the dyadic-\(60\) theorem proved here. Its Theorem 9 concerns a different family
\[
pq2^a
\]
with parameters tied by \(q=2^{b+1}-1\) and \(p=2^{a+1}-(2^b+1)\), and does not imply the present result.

Targeted exact searches for the family \(60\cdot2^n\), for arithmetic progressions of the exponent, and for McCormack--Zelinsky Question 39 did not locate a prior general solution. The current OEIS entry for strongly pseudoperfect numbers cites both papers but does not state this family theorem.

## Limitations
The theorem concerns one explicit family of strongly pseudoperfect numbers. It does not classify all strongly pseudoperfect numbers, determine their density, or imply that every strongly pseudoperfect number is extremely strongly pseudoperfect.

The proof supplies one representation in each exponent class and does not classify all representations of \(60\cdot2^n\).

Literature search non-detection is not a proof of novelty. An unindexed or unpublished proof of the same family could exist.

## References
1. Tim McCormack and Joshua Zelinsky, “Weighted Versions of the Arithmetic-Mean-Geometric Mean Inequality and Zaremba's Function,” arXiv:2312.11661v1, first posted 18 December 2023; MSC \(11A05\), \(11A25\), \(26D15\).
2. Audrey Wang and Joshua Zelinsky, “Strongly Pseudoperfect Numbers,” arXiv:2609.36068v1, first posted 28 September 2026.
3. OEIS A334405, strongly pseudoperfect numbers.
