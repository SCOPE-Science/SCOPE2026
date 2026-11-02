# First short-period gap in a ternary quadratic recurrence

## Finding
For every integer \(k\ge2\), consider periodic sequences over \(\mathbb F_3\) satisfying
\[
x_n=x_{n-1}+x_{n-k}^2\pmod 3.
\]
The complete list of least periods at most nine is \(1,4,9\). Period one consists only of zero. A nonzero period-four cycle exists precisely when \(k\equiv2,3\pmod4\), and a period-nine cycle exists precisely when \(k\equiv4,6\pmod9\). For each admissible congruence there is exactly one cycle of the indicated length, up to cyclic rotation. No period two, three, five, six, seven, or eight is possible, for any lag. In particular, the first possible nonconstant cycle after period four has period nine; \(k=4\) realizes it.

Explicit cycles, displayed as one period beginning at a zero, are

- \((0,1,1,2)\) for \(k\equiv2\pmod4\), and \((0,1,2,2)\) for \(k\equiv3\pmod4\).
- \((0,0,1,2,2,2,0,1,2)\) for \(k\equiv4\pmod9\), and \((0,0,1,2,0,1,1,1,2)\) for \(k\equiv6\pmod9\).

The statement concerns **all periodic solutions**, not whether the special initial word in Finch's paper eventually reaches any particular cycle.

## Assumptions and scope
Arithmetic takes place in \(\mathbb F_3\); \(k\) is any fixed integer at least two. A cyclic word \(x=(x_0,\ldots,x_{m-1})\) extends to a two-sided period-\(m\) sequence, and has least period \(m\) when no proper divisor of \(m\) is a period. Throughout, indices of a period-\(m\) word are reduced modulo \(m\); consequently the rule depends on the arbitrary lag \(k\) only through \(r=k\bmod m\). A cycle is an equivalence class of such words under rotation, not an orbit count among nonperiodic initial data.

## Proof
First, in \(\mathbb F_3\), the square of a value is the indicator of its being nonzero. Put \(d_i=x_i-x_{i-1}\in\{0,1\}\) and \(b_i=[x_i\ne0]\). The recurrence is exactly
\[
d_i=b_{i-r},\qquad r=k\bmod m.
\]
Summing the equality around a period gives \(Z:=\#\{i:x_i\ne0\}=\#\{i:d_i=1\}\equiv0\pmod3\). When \(Z=0\), the word is identically zero. Otherwise all positive steps traverse the sequence \(0\to1\to2\to0\), and there are \(Z/3\) full circuits. Each circuit visits a zero at least once, so \(m-Z\ge Z/3\). For \(m\le9\), this leaves \(Z=3\) when \(m\ge4\), or \(Z=6\) only when \(m=8,9\). In particular, \(Z=9\) at \(m=9\) is impossible.

When \(Z=3\), up to rotation the word is \(0^a1^b2^c\), where \(a,b,c\ge1\). The number of nonzero entries gives \(b+c=3\), while \(a=m-3\). The support of the three nonzero increments is at the three starts of these constant blocks, with circular gaps \(a,b,c\). Since \(d\) must be a translate of \(b\), this support must itself comprise three consecutive indices. The gaps are therefore \(1,1,m-2\), in some order. Given \(b+c=3\), this forces \(a=1\) and \(m=4\). Checking the two choices \((b,c)=(1,2),(2,1)\) gives the displayed period-four words and exactly \(r=2,3\) respectively. This also excludes all nonconstant words of periods two, three, five, six, and seven.

For \(Z=6\), there are exactly two circuits, so up to rotation beginning at a zero the word has the form
\[
0^{a_1}1^{b_1}2^{c_1}0^{a_2}1^{b_2}2^{c_2},
\]
where each of the six run lengths is positive. Their sum is \(m\); the zero count is \(a_1+a_2=m-6\). Thus only \(m=8,9\) require consideration. There are exactly \(\binom{m-1}{5}\) positive six-run compositions: \(21\) at \(m=8\) and \(56\) at \(m=9\). For each composition, test the possible residues \(0\le r<m\) by all \(m\) elementary residue equalities \(d_i=b_{i-r}\) for \(0\le i<m\). This finite test yields the complete list below, writing the six lengths as \((a_1,b_1,c_1,a_2,b_2,c_2)\):

| \(m\) | six-run lengths | \(r\) | least period |
| --- | --- | --- | --- |
| 8 | \((1,1,2,1,1,2)\) | 3 or 7 | 4 |
| 8 | \((1,2,1,1,2,1)\) | 2 or 6 | 4 |
| 9 | \((1,1,1,2,1,3)\) | 4 | 9 |
| 9 | \((2,1,3,1,1,1)\) | 4 | 9 |
| 9 | \((1,3,1,2,1,1)\) | 6 | 9 |
| 9 | \((2,1,1,1,3,1)\) | 6 | 9 |

The six-run test is completely specified, and the standalone verifier enumerates all \(77\) compositions and all lag residues without heuristics. In the two length-nine cases, the two displayed compositions for a given residue are rotations of a single nine-word; all nine cyclic rotations are solutions, yielding one primitive orbit. The length-eight words shown have least period four. For an independent complete check, the verifier also enumerates every ternary word of length at most nine and rejects all candidates not satisfying the cyclic recurrence. This second enumeration gives precisely the same primitive-period table. Hence the classification holds for every integer \(k\ge2\), because \(k\) only enters through its residue modulo the candidate period. The period-nine representative with \(k\equiv4\pmod9\) proves sharpness at \(k=4\). \(\square\)

## Verification
Run `python3 verify.py` using Python 3 standard library. One exhaustive engine tests every ternary cyclic word of lengths one through nine against every possible lag residue and computes its least period. A separate engine enumerates all positive six-run compositions at lengths eight and nine, independently matching the listed rows. Successful output ends with `independent_enumerators=yes`. This is an exact exhaustive finite certificate for the only finite cases remaining after the structural reduction; it is not an inference from a sample of lag parameters.

## Relationship to prior work
Finch's 2026 paper establishes a universal lower bound four for the distinguished initial-value sequence and describes four-periodic words and a capture criterion (Propositions 11–13). Its small-lag table includes a period-nine example but does not classify *all* short periodic cycles or rule out periods five through eight for arbitrary lags. The present claim is the complete short-orbit spectrum, including exact period-nine lag congruences and uniqueness of the nine-cycles. Its period-four component agrees with the cited paper and is not claimed as new. Related results on the paper's different recurrence (B) have a different update rule and do not imply this classification.

## Limitations
The argument stops at least period nine, does not assert a classification of longer cycles, and makes no claim that the prescribed sparse initial state enters any particular cycle for every lag. The originality search cannot rule out unindexed prior elementary cycle classifications; independent review is not yet performed.

## References
Steven Finch, *Three Quadratic Recurrences Modulo 3: What We Can Prove and What We Can Guess*, arXiv:2610.34300v1, first submitted 2026-10-25, Sections 1 and 4, especially Propositions 11–13. https://arxiv.org/html/2610.34300v1
