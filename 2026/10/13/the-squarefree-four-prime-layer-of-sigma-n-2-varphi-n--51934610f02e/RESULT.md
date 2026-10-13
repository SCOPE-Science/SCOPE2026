# The squarefree four-prime layer of \(\sigma(n)=2\varphi(n)\)
## Finding
Let \(\sigma(n)\) denote the sum of the positive divisors of \(n\), and let \(\varphi(n)\) denote Euler's totient function.

The squarefree integers with exactly four distinct prime factors satisfying
\[
\sigma(n)=2\varphi(n)
\]
are exactly
\[
24871,\ 29029,\ 50065,\ 58435,\ 64285,\ 87685,\ 137885,\ 140335.
\]
Their prime factorizations are
\[
24871=7\cdot11\cdot17\cdot19,
\]
\[
29029=7\cdot11\cdot13\cdot29,
\]
\[
50065=5\cdot17\cdot19\cdot31,
\]
\[
58435=5\cdot13\cdot29\cdot31,
\]
\[
64285=5\cdot13\cdot23\cdot43,
\]
\[
87685=5\cdot13\cdot19\cdot71,
\]
\[
137885=5\cdot11\cdot23\cdot109,
\]
and
\[
140335=5\cdot13\cdot17\cdot127.
\]

## Assumptions and scope
Only squarefree integers with exactly four distinct prime factors are classified. Write
\[
n=pqrs,
\qquad
p<q<r<s
\]
with distinct primes.

For squarefree \(n\), multiplicativity gives
\[
\sigma(n)=(p+1)(q+1)(r+1)(s+1)
\]
and
\[
\varphi(n)=(p-1)(q-1)(r-1)(s-1).
\]
Thus the equation is equivalent to
\[
H(p)H(q)H(r)H(s)=2,
\qquad
H(t)=\frac{t+1}{t-1}.
\tag{1}
\]
The function \(H(t)\) is strictly decreasing for \(t>1\).

The theorem does not classify nonsquarefree solutions with four distinct prime factors, nor squarefree solutions with five or more prime factors.

## Proof
An even integer cannot satisfy \(\sigma(n)=2\varphi(n)\): if \(2\mid n\), then
\[
2\varphi(n)\le n<\sigma(n).
\]
Hence all four primes in the present squarefree case are odd.

If \(p=3\), then \(H(p)=2\), while each of the other three factors in (1) is greater than \(1\), which is impossible. Thus \(p\ge5\).

If \(p\ge13\), then
\[
H(p)H(q)H(r)H(s)
< H(13)^4
=\left(\frac76\right)^4
<2.
\]
Therefore
\[
p\in\{5,7,11\}.
\tag{2}
\]

Because \(q<r<s\) and \(H\) is decreasing, equation (1) implies the strict bound
\[
2<H(p)H(q)^3.
\tag{3}
\]
For \(p=5\), inequality (3) fails when \(q\ge23\), since
\[
H(5)H(23)^3=\frac32\left(\frac{12}{11}\right)^3<2.
\]
Thus \(q\in\{7,11,13,17,19\}\). The case \(q=7\) is impossible because
\[
H(5)H(7)=2
\]
already. The case \(q=19\) is impossible because \(r\ge23\) and
\[
H(5)H(19)H(23)^2=\frac{240}{121}<2.
\]
Hence for \(p=5\), only
\[
q\in\{11,13,17\}
\tag{4}
\]
remains.

For \(p=7\), inequality (3) fails when \(q\ge17\), so \(q\in\{11,13\}\). The value \(q=13\) is impossible because \(r\ge17\) and
\[
H(7)H(13)H(17)^2=\frac{63}{32}<2.
\]
Thus the only possibility with \(p=7\) is
\[
q=11.
\tag{5}
\]

For \(p=11\), already \(q\ge13\), and
\[
H(11)H(13)^3<2,
\]
contradicting (3). So no solution has \(p=11\).

It remains to bound \(r\) in the four pairs from (4) and (5). Again, since \(s>r\), equation (1) gives
\[
2<H(p)H(q)H(r)^2.
\tag{6}
\]
The first prime beyond each resulting cutoff makes the right side less than \(2\):
\[
H(5)H(11)H(41)^2=\frac{3969}{2000}<2,
\]
\[
H(5)H(13)H(31)^2=\frac{448}{225}<2,
\]
\[
H(5)H(17)H(29)^2=\frac{6075}{3136}<2,
\]
and
\[
H(7)H(11)H(19)^2=\frac{160}{81}<2.
\]
Therefore the only candidate triples \((p,q,r)\) are
\[
(5,11,r),\quad r\in\{13,17,19,23,29,31,37\},
\]
\[
(5,13,r),\quad r\in\{17,19,23,29\},
\]
\[
(5,17,r),\quad r\in\{19,23\},
\]
and
\[
(7,11,r),\quad r\in\{13,17\}.
\]

For a fixed triple, put
\[
A=H(p)H(q)H(r).
\]
If \(A\ge2\), no fourth factor can occur. If \(A<2\), equation (1) determines the fourth prime uniquely:
\[
s=\frac{2+A}{2-A}.
\tag{7}
\]
The complete exact evaluation is

| \((p,q,r)\) | \(A\) | value forced by (7) |
| --- | --- | --- |
| \((5,11,13)\) | \(21/10\) | none, since \(A>2\) |
| \((5,11,17)\) | \(81/40\) | none, since \(A>2\) |
| \((5,11,19)\) | \(2\) | none |
| \((5,11,23)\) | \(108/55\) | \(109\) |
| \((5,11,29)\) | \(27/14\) | \(55\), composite |
| \((5,11,31)\) | \(48/25\) | \(49\), composite |
| \((5,11,37)\) | \(19/10\) | \(39\), composite |
| \((5,13,17)\) | \(63/32\) | \(127\) |
| \((5,13,19)\) | \(35/18\) | \(71\) |
| \((5,13,23)\) | \(21/11\) | \(43\) |
| \((5,13,29)\) | \(15/8\) | \(31\) |
| \((5,17,19)\) | \(15/8\) | \(31\) |
| \((5,17,23)\) | \(81/44\) | \(169/7\), not an integer |
| \((7,11,13)\) | \(28/15\) | \(29\) |
| \((7,11,17)\) | \(9/5\) | \(19\) |

The eight prime outputs in the table are all larger than \(r\), and they yield exactly the eight factorizations stated in the finding. This exhausts every ordered prime quadruple.

## Verification
The attached `verify.py` recomputes the proof with exact rational arithmetic. It derives the finite branch set from the monotonic inequalities rather than from an external numerical cutoff, evaluates the unique fourth factor from (7), tests primality by deterministic trial division, and verifies
\[
\sigma(n)=2\varphi(n)
\]
for every surviving integer.

The replay returns exactly eight solutions and the exact ordered prime quadruples listed above. The script is corroborative; the finite exhaustion is already justified by the inequalities in the proof.

## Relationship to prior work
OEIS A062699 is the exact sequence of integers satisfying
\[
\sigma(n)=2\varphi(n).
\]
Its initial terms include all eight integers in the present theorem, but the database listing itself does not prove that these are every squarefree term with exactly four prime factors.

Broughan and Delbourgo prove that the only solutions with at most three distinct prime factors are
\[
3,\ 35,\ 1045,
\]
and they separately prove finiteness for squarefree solutions with any fixed number of prime factors. Their theorem stops before the four-prime layer.

Broughan and Zhou later give a heuristic construction of squarefree solutions and display one example for each support size through ten; for support size four their displayed example is
\[
24871=7\cdot11\cdot17\cdot19.
\]
That table is explicitly an example table, not an exhaustive classification of support size four.

For squarefree \(n\), Dedekind's function \(\psi(n)\) equals \(\sigma(n)\), so the present theorem also identifies the four-prime squarefree support patterns inside the equation
\[
\psi(n)=2\varphi(n).
\]
OEIS A292390 records that broader support-set equation but likewise does not provide this exact four-support classification.

## Limitations
The theorem concerns only squarefree integers with exactly four distinct prime factors. It does not address nonsquarefree members of A062699 with four distinct prime factors, nor any support size at least five.

The proof establishes exhaustiveness by an elementary monotonicity-and-rational-enumeration argument. A logically equivalent short argument could exist in an unindexed note or problem discussion; targeted searches and inspection of the closest primary papers did not reveal one.

## References
1. OEIS Foundation, A062699, numbers \(n\) such that \(\sigma(n)=2\varphi(n)\); entry authored 11 July 2001.
2. K. A. Broughan and D. Delbourgo, “On the Ratio of the Sum of Divisors and Euler's Totient Function I,” *Journal of Integer Sequences* 16 (2013), Article 13.8.8, published 13 October 2013.
3. K. A. Broughan and Q. Zhou, “On the Ratio of the Sum of Divisors and Euler's Totient Function II,” *Journal of Integer Sequences* 17 (2014), Article 14.9.2, published 12 August 2014.
4. OEIS Foundation, A292390, numbers \(n\) such that \(\psi(n)=2\varphi(n)\).
