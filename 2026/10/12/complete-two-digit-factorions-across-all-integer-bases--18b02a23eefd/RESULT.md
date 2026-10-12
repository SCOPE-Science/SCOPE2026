# Complete two-digit factorions across all integer bases
## Finding
For an integer base \(b\ge2\), write an exactly two-digit number as
\[
(a,c)_b=ab+c,
\qquad 1\le a<b,
\qquad 0\le c<b.
\]
Call it a factorion when
\[
ab+c=a!+c!.
\]
Then all two-digit factorions, in all integer bases, fall into exactly four disjoint classes:

1. \((a,c,b)=(1,0,2)\).
2. \(c\in\{1,2\}\), \(a\ge4\), and \(b=(a-1)!\).
3. \(c\ge3\), \(1\le a\le c\), \(a\mid c\), \((a,c)\ne(3,3)\), and
\[
b=(a-1)!+\frac{c!-c}{a}.
\]
4. \(c\ge3\), \(a>c\), \(a\mid(c!-c)\), and the same base formula holds.

Thus every positive leading digit occurs in infinitely many such factorions as the base varies. Also, for each fixed trailing digit \(c\ge4\), the exact number of two-digit factorion representations across all bases is
\[
\tau(c)+\#\{a:a\mid(c!-c),\ a>c\}.
\]

## Assumptions and scope
For a base-\(b\) expansion with digits \(d_i\), the digit-factorial map is
\[
F_b(n)=\sum_i d_i!.
\]
A factorion is a fixed point of this map. The theorem classifies exactly the two-digit stratum while allowing the base to vary over all integers at least \(2\). It does not classify factorions with three or more digits.

The convention \(0!=1\) is used.

## Proof
The factorion equation is
\[
ab+c=a!+c!.
\]
Solving for the base gives the forced value
\[
b=(a-1)!+\frac{c!-c}{a}.
\tag{1}
\]
Therefore integrality is equivalent to
\[
a\mid(c!-c).
\tag{2}
\]
No other base can work for the chosen digit pair. It remains only to classify when (1) is an integer satisfying the digit inequalities
\[
b>a,
\qquad b>c.
\tag{3}
\]

If \(c=0\), then \(c!-c=1\), so (2) forces \(a=1\); (1) gives \(b=2\). This is class 1.

If \(c=1\) or \(c=2\), then \(c!-c=0\), so (1) gives
\[
b=(a-1)!.
\]
Condition (3) fails for \(a=1,2,3\) and holds for every \(a\ge4\). This is class 2.

Now suppose \(c\ge3\) and \(a\le c\). Since \(a\) is a factor of \(c!\), condition (2) is equivalent to
\[
a\mid c.
\tag{4}
\]
If \((a,c)=(3,3)\), formula (1) gives \(b=3\), which is not a valid base for leading digit \(3\). In every other case satisfying (4), the digit inequalities hold. For \(a=1\), one has \(b=c!-c+1>c\). For \(a=2\) the first possible value is \(c=4\), and for \(a=3\) after excluding \(c=3\) the first is \(c=6\); direct substitution gives the inequalities. For \(a\ge4\), write \(c=ka\). Then
\[
b=(a-1)!+k(c-1)!-k.
\]
If \(k=1\), this is \(2(a-1)!-1>a=c\) for every \(a\ge4\). If \(k\ge2\), then \(c\ge8\), so \(k(c-1)!-k>kc=c\), while also \((a-1)!>a\). Thus both digit bounds hold. This is class 3.

Finally suppose \(c\ge3\) and \(a>c\). Then \(a\ge4\). Whenever (2) holds, formula (1) satisfies
\[
b\ge(a-1)!>a>c,
\]
because \(c!-c>0\). Hence (2) is both necessary and sufficient, proving class 4.

The four classes are disjoint and exhaust all digit pairs, so the classification is complete.

For the leading-digit infinitude, choose \(c\) to be a sufficiently large multiple of \(a\). Class 3 then applies for every fixed \(a\), with the explicit small choices \(c\ge3\) for \(a=1\), even \(c\ge4\) for \(a=2\), and multiples \(c\ge6\) for \(a=3\).

For fixed \(c\ge4\), class 3 contributes exactly one representation for each positive divisor \(a\mid c\), hence \(\tau(c)\) representations. Class 4 contributes exactly the divisors \(a>c\) of \(c!-c\). The two sets are disjoint, proving the stated count.

## Verification
The attached checker exhausts all digit pairs
\[
1\le a\le60,
\qquad 0\le c\le60,
\]
computes the unique candidate base from the defining equation, and compares direct validity with the four-case theorem. It also enumerates every two-digit number for bases \(2\le b\le100\) and confirms that the observed factorions equal those predicted by the classification.

The program separately verifies the fixed-trailing-digit count formula for \(4\le c\le6\). These finite calculations corroborate the algebraic proof but do not establish its unrestricted quantifiers.

## Relationship to prior work
Kiss studied the decimal digit-factorial map and its fixed points and cycles. That archival paper works in decimal representation; it does not classify factorions across arbitrary bases.

Gupta's later note also concerns sums of factorials of digits. Its bibliographic record was accessible, but complete text was not available through the inspected lawful routes, so possible overlap in that note remains a literature risk.

OEIS A193163 is an exact table of factorions by base, beginning at base \(2\). It records concrete rows rather than an all-base two-digit converse. A260651 counts factorions in each base and likewise does not supply the digit-pair classification.

Public summaries of factorions in arbitrary bases highlight two infinite constructions: digits \((m,1)\) and \((m,2)\) in base \((m-1)!\), and digits \((1,m)\) in base \(m!-m+1\). These are precisely class 2 and the \(a=1\) subfamily of class 3. The theorem above shows how those familiar constructions sit inside the complete two-digit spectrum and identifies all additional solutions.

## Limitations
The theorem addresses two digits only. Higher digit lengths introduce several independent factorial terms and are not reduced by the one-base equation (1).

The strongest residual originality risk is Gupta's inaccessible complete note and unindexed recreational literature. The accessible multi-base database and current public summaries were inspected at statement level, and no full converse matching the four classes was located.

Older decimal papers predate the exact dated multi-base database, but their accessible metadata supplies only journal year or month rather than an exact public calendar day. The structured source date therefore uses the earliest exact public day verified for the arbitrary-base object, 6 August 2011, without inventing an older day.

## References
1. P. Kiss, “A Generalization of a Problem in Number Theory,” *Mathematics Seminar Notes* 5(3) (1977), 313–317.
2. S. S. Gupta, “Sum of the factorials of the digits of integers,” *The Mathematical Gazette* 88(512) (2004), 258–261, doi:10.1017/S0025557200174996.
3. OEIS Foundation, A193163, “Irregular table read by rows, in which row \(n\) lists the factorions in base \(n\).”
4. OEIS Foundation, A260651, “Number of factorions in base \(n\).”
