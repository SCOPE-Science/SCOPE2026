# Finite recognition and complete classification of binomid quartics with integer root shifts

## Finding
For any integers \(0\le a\le b\le c\le d\), let
\[
f_n=(n+a)(n+b)(n+c)(n+d)\qquad(n\ge1).
\]
For \(0\le k\le n\), define the generalized binomial coefficient
\[
\mathcal B_f(n,k)=\frac{\prod_{j=n-k+1}^{n}f_j}{\prod_{j=1}^{k}f_j},
\]
where an empty product is \(1\). The following are equivalent:

1. \(\mathcal B_f(n,k)\) is an integer for every \(n\ge1\) and \(0\le k\le n\) (the *binomid* property).
2. The three rational numbers \(f_2/f_1\), \(f_3/f_1\), and \(f_3f_4/(f_1f_2)\) are all integers.
3. The ordered quadruple \((a,b,c,d)\) is one of
\[
(0,0,0,0),\quad (0,0,0,1),\quad (0,0,1,1),\quad
(0,0,1,2),\quad (0,1,2,3).
\]
Thus an unbounded four-parameter family of quartic sequences has a complete classification and a finite three-coefficient recognition test.

## Assumptions and scope
All root shifts are **nonnegative integers**, in nondecreasing order. Every \(f_n\) is strictly positive. The theorem does not classify quartics with arbitrary complex, rational, or positive roots, nor arbitrary integer-valued quartic polynomials. Multiplying the entire sequence by any nonzero constant that keeps its terms integral does not change its generalized binomial coefficients; the statement uses the monic normalization.

## Proof
**Necessity of the three tests.** The generalized coefficients at \((n,k)=(2,1),(3,1),(4,2)\) are respectively \(f_2/f_1\), \(f_3/f_1\), and \(f_3f_4/(f_1f_2)\). Hence binomidness implies the three conditions.

**A finite, exhaustive root-shift sieve.** Put \(R_0=1\) and, for an ordered prefix \((a_1,\ldots,a_j)\) of length \(j\le4\), set
\[
R_j=\prod_{i=1}^{j}\frac{a_i+2}{a_i+1}.
\]
In particular, \(R_4=f_2/f_1\). For \(j<4\), every completion has \(R_4>R_j\), since all factors \((t+2)/(t+1)\) are strictly larger than \(1\). Therefore, if the completion makes \(R_4\) integral, it must satisfy
\[
R_4\ge T_j:=\lfloor R_j\rfloor+1.
\]
Suppose the next root shift is \(t\ge a_j\) (take \(t\ge0\) for the empty prefix). Since subsequent shifts are at least \(t\), each of the \(4-j\) remaining factors is at most \((t+2)/(t+1)\). Therefore the necessary bound is
\[
R_j\left(\frac{t+2}{t+1}\right)^{4-j}\ge T_j.\tag{1}
\]
Its left side strictly decreases towards \(R_j<T_j\) as \(t\to\infty\). Thus each prefix has only finitely many possible next shifts, and increasing \(t\) can stop permanently as soon as (1) fails.

The exact branching procedure is: start with \((j,R_j)=(0,1)\); for each ordered prefix, visit every integer \(t\) from its last shift (or \(0\)) through the last value satisfying (1); append \(t\) and replace \(R_j\) by \(R_j(t+2)/(t+1)\); at depth four retain exactly the prefixes for which \(R_4\) is an integer. All inequalities and divisions are rational. This is an **exhaustive finite enumeration**, not a cutoff experiment: (1) proves every discarded tail impossible and proves termination.

The stage counts, including nonintegral prefixes, at depths \(0,1,2,3,4\) are \(1,5,21,143,1867\), respectively. Exactly \(83\) depth-four prefixes have integral \(f_2/f_1\). Filtering these \(83\) by the exact divisibility \(f_1\mid f_3\) leaves precisely:
\[
\begin{gathered}
(0,0,0,0),\ (0,0,0,1),\ (0,0,1,1),\ (0,0,1,2),\\
(0,0,1,5),\ (0,1,1,2),\ (0,1,2,3),\ (1,2,3,4).
\end{gathered}
\]
Applying the third test removes exactly these three quadruples, whose \(\mathcal B_f(4,2)\) values are:
\[
\begin{array}{c|c}
(a,b,c,d)&\mathcal B_f(4,2)\\\hline
(0,0,1,5)&1440/7\\
(0,1,1,2)&500/3\\
(1,2,3,4)&98/3
\end{array}
\]
This yields exactly the five quadruples in condition 3. The accompanying `verify.py` uses arbitrary-precision integer fractions to reproduce every branch and divisibility test. As a separate exact enumeration, it also algebraically solves the last coordinate from \((m-R_3)(d+1)=R_3\), checking agreement with all \(83\) first-test quadruples.

**Sufficiency.** The first four product forms can be written as
\[
\begin{aligned}
 n^4&=n^4,\\
 n^3(n+1)&=n^2\,\bigl(n(n+1)\bigr),\\
 n^2(n+1)^2&=\bigl(n(n+1)\bigr)^2,\\
 n^2(n+1)(n+2)&=n\,\bigl(n(n+1)(n+2)\bigr),
\end{aligned}
\]
while the fifth is \(n(n+1)(n+2)(n+3)\). The sequence \((n)_{n\ge1}\) and each rising-factorial sequence \((n(n+1)\cdots(n+m-1))_{n\ge1}\) for \(m=2,3,4\) are binomid: after scaling by \(m!\), the latter is the \(m\)-th column of Pascal's triangle, which is binomid by Shapiro's column theorem. A termwise product of binomid sequences is binomid, because its generalized coefficients multiply. Hence all five forms satisfy condition 1.

Combining necessity, the exhaustive finite sieve and sufficiency proves all equivalences.

## Verification
Execute `python3 verify.py` using only the Python standard library. The checker supplies two mathematically exhaustive, exact-arithmetic enumeration procedures, verifies the intermediate \(83\)- and \(8\)-candidate lists and the final five candidates, prints the three excluded nonintegral coefficients, and additionally tests all generalized coefficients through row \(80\) for the five survivors. The exhaustive sieve is justified by inequality (1); testing finitely many coefficients by itself would not prove unrestricted integrality. The file `verification_output.txt` records a successful execution. The positive-family integrality proof uses the published Pascal-column theorem rather than the finite coefficient checks.

## Relationship to prior work
Shapiro's *Divisibility Properties for Integer Sequences* (2023), Section 4.3, establishes that Pascal columns are binomid and explicitly notes the difficulty of classifying binomid polynomials beyond degree two. The present theorem is a complete classification of the **monic degree-four subclass with nonnegative integer root shifts**, not a classification of all quartic binomid polynomials. Caalim and Tanaka (2024) characterize binomid sequences through prime-valuation indices and study lexicographically minimal extensions; their results do not supply this finite recognition criterion or five-quadruple classification. The sufficiency of the listed forms follows from known closure properties; the negative classification and exact three-test equivalence are the new content.

## Limitations
There is no claim for general integer-valued quartics, arbitrary integer roots that can produce zeros among positive indices, or degree five and above. The classification relies on a finite exact rational-arithmetic sieve whose completeness rests on (1); its code and independent last-coordinate method are supplied for reproducibility. The literature comparison cannot exclude unpublished or unindexed equivalent statements. No independent mathematical audit has been performed.

## References
1. D. B. Shapiro, *Divisibility Properties for Integer Sequences*, arXiv:2302.02243 (first posted 2023-02-04), especially Lemma 3, Theorem 15 and Section 4.3. https://arxiv.org/abs/2302.02243
2. J. Caalim and Y. Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, INTEGERS 24 (2024), article A53, published 2024-05-20. DOI: 10.5281/zenodo.11221709. https://math.colgate.edu/~integers/y53/y53.pdf
