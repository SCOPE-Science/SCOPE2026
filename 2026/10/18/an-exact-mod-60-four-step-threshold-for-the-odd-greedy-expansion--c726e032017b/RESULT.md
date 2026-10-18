# An exact mod-60 four-step threshold for the odd greedy expansion of \(2/q\)

## Finding

Let \(q\ge3\) be odd. The odd greedy algorithm for \(2/q\) repeatedly subtracts the greatest reciprocal \(1/d\) not exceeding the current positive remainder, with \(d\) an odd positive integer. Write \(L(q)\) for its eventual number of terms, or \(\infty\) if it never terminates. Then

\[
L(q)=\begin{cases}
2,&q\equiv1\pmod4\text{ or }q\equiv3\pmod{12},\\
4,&q\bmod60\in\{7,35,47,55\},\\
\ge6,&q\bmod60\in\{11,19,23,31,43,59\}.
\end{cases}
\]

The final inequality permits nontermination. The indicator of the exactly-four-term class has **least positive even period 60** on the odd integers. Its natural density among odd positive denominators is \(2/15\). The densities for two terms and at least six terms are \(2/3\) and \(1/5\), respectively. In particular, exactly \(4/5\) of odd denominators \(q\) finish within four greedy steps.

## Assumptions and scope

The initial rational number is exactly \(2/q\) for each odd \(q\ge3\). At a positive remainder \(u/v\), expressed in lowest terms, choose the smallest positive **odd** integer \(d\) for which \(1/d\le u/v\); subtract \(1/d\) and repeat. Equal consecutive denominators are allowed, including the expansion \(2/3=1/3+1/3\). This is the standard odd greedy algorithm, not the unrestricted Egyptian-fraction greedy algorithm. No claim is made for general fixed numerators or for the duration of expansions outside the first four steps.

For any subset of odd positive integers, its natural density *among odds* means the limit of its count through \(X\) divided by the count of all positive odd integers through \(X\), if the limit exists.

## Proof

**Parity lemma.** A sum of \(m\) unit fractions with odd denominators has a common odd denominator and a numerator congruent to \(m\pmod2\). The fraction \(2/q\) has even numerator over an odd denominator. Therefore any finite odd greedy expansion of \(2/q\) has even length. In particular there cannot be exactly one, three, or five terms.

**First remainder.** If \(q\equiv1\pmod4\), the first denominator is \(x=(q+1)/2\), an odd integer, and

\[
\frac2q-\frac1x=\frac1{qx}.
\]

Thus \(L(q)=2\). If \(q\equiv3\pmod4\), the first denominator instead is \(x=(q+3)/2\), also odd, and

\[
\frac2q-\frac1x=\frac3A,\qquad A=qx.
\]

The second term finishes the expansion exactly when \(3\mid A\). As \(q\equiv3\pmod4\), inspection modulo \(12\) gives \(3\mid A\) exactly for \(q\equiv3\pmod{12}\). This proves the two-term criterion, consistent with the fixed-numerator theorem of Louwsma and Martino [1].

**The next two remainders.** It remains to consider \(q\equiv7\) or \(11\pmod{12}\), when \(A\equiv5\pmod6\). The smallest odd denominator allowed for \(3/A\) is

\[
y=\frac{A+4}{3};\qquad
\frac3A-\frac1y=\frac4D,\qquad D=Ay=\frac{A(A+4)}3.
\]

For every odd \(A\), \(A(A+4)\equiv5\pmod8\), so \(D\equiv7\pmod8\). The smallest permitted odd denominator for \(4/D\) is consequently

\[
z=\frac{D+5}{4};\qquad
\frac4D-\frac1z=\frac5{Dz}.
\]

The remaining fraction is an odd-denominator unit fraction exactly when \(5\mid Dz\). From \(4z=D+5\), one has \(5\mid Dz\) exactly when \(5\mid D\): if \(5\nmid D\), then \(z\equiv4^{-1}D\not\equiv0\pmod5\). Since \(3D=A(A+4)\), the criterion is \(A\equiv0\) or \(1\pmod5\).

With \(A=q(q+3)/2\), the case \(A\equiv1\pmod5\) is equivalent to \(q^2+3q-2\equiv0\pmod5\). Its discriminant is \(17\equiv2\pmod5\), a nonsquare, so this case never occurs. Hence \(L(q)=4\) exactly when \(q\equiv0\) or \(2\pmod5\) while \(q\equiv7\) or \(11\pmod{12}\). The Chinese remainder theorem gives the four classes \(7,35,47,55\pmod{60}\). The odd classes not covered so far are exactly \(11,19,23,31,43,59\pmod{60}\). In them the algorithm has not terminated after four terms; by the parity lemma, its finite length is at least six.

**Minimal period and density.** The four classes show periodicity modulo \(60\). Any even eventual period and \(60\) have a greatest common divisor that is likewise an eventual period. Every proper divisor of \(60\) divides at least one of \(12,20,30\). However \(q\equiv7\pmod{60}\) is in the exactly-four-term class, whereas \(q+12\equiv19\), \(q+20\equiv27\), and \(q+30\equiv37\pmod{60}\) are not. Hence none of these is a period and the least even period is \(60\). There are \(30\) odd residues modulo \(60\), of which \(20\) give two terms, \(4\) give four terms, and \(6\) remain unsettled at step four. Their respective densities are \(20/30=2/3\), \(4/30=2/15\), and \(6/30=1/5\). This completes the proof.

## Verification

The companion `verify.py` uses exact rational arithmetic with `fractions.Fraction`, independently executing up to four greedy subtractions for every odd denominator \(3\le q\le20001\). It checks the modular prediction for all \(10000\) tested denominators, independently checks all odd residues modulo \(60\), and reconstructs each starting fraction exactly. Run `python verify.py` with Python 3. These finite tests check implementation and arithmetic but are not the proof for unbounded \(q\); the congruence argument above establishes that scope.

For instance, the fraction \(2/7\) uses odd denominators \(5,13,115,10465\) and terminates in four terms. The fraction \(2/11\) does not terminate during its first four terms.

## Relationship to prior work

Louwsma and Martino [1] establish the complete fixed-numerator **two-term** classification (Theorem 2.3, with a numerator-two example) and, separately, a general parameterization of expansions of fixed length conditional on the first \(m-1\) denominators (Theorem 3.2). Their latter theorem gives a general implicit description encompassing any individual four-term expansion. It does **not** give the uniform modulus-60 recognition criterion as the starting denominator varies, its minimal period, or the exact density split for the fixed numerator \(2\). The present calculation isolates those arithmetic consequences and their sharp period. Pihko [2] constructs and studies specific families with prescribed remainder numerators, including long numerator-two expansions, rather than classifying every starting denominator through a fixed four-step horizon. Brown [3] constructs arbitrarily long odd greedy expansions; those examples do not determine the present residue-class proportions.

## Limitations

The six remaining odd residue classes are known here only not to finish within four steps. No claim is made that every corresponding expansion eventually terminates. The classification and density concern one fixed numerator and this specific algorithm; they do not imply statements about minimal-length Egyptian fraction representations or other numerators. A general fixed-prefix parameterization in [1] implicitly describes each individual four-term expansion, so the originality of the **global residue/density simplification** is narrower than an unrestricted classification of four-term rational expansions. Undiscovered equivalent residue analyses remain possible.

## References

[1] J. Louwsma and J. Martino, *Rational numbers with odd greedy expansion of fixed length*, arXiv:2309.07280v1 (first posted 13 September 2023), https://arxiv.org/html/2309.07280v1 . See Theorems 2.3 and 3.2 and Sections 4–5.

[2] J. Pihko, *Remarks on the “Greedy Odd” Egyptian Fraction Algorithm II*, Fibonacci Quarterly 48 (2010), 202–208, https://www.fq.math.ca/Papers1/48-3/Pihko.pdf . See Theorem 2.3 and Section 3.

[3] K. Brown, *Odd-Greedy Unit Fraction Expansions*, https://www.mathpages.com/home/kmath478.htm (undated online mathematical exposition).
