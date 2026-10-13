# Risk ratio and odds ratio first reverse trial rankings at five patients per arm
## Finding
Consider balanced binary-outcome trials with exactly
\[
n
\]
participants in the treatment arm and exactly
\[
n
\]
in the control arm.

Write
\[
a
\]
for the number of treatment-arm events and
\[
b
\]
for the number of control-arm events. Require all four cells to be positive and orient the table so that the treatment is protective:
\[
1\le a<b\le n-1.
\]

The risk ratio is
\[
RR(a,b;n)=\frac{a}{b},
\]
while the odds ratio is
\[
OR(a,b;n)
=
\frac{a/(n-a)}{b/(n-b)}
=
\frac{a(n-b)}{b(n-a)}.
\]

Across two such trials, these two effect measures need not rank the treatment effects in the same order.

No strict ranking reversal is possible for
\[
n\le4.
\]

At
\[
n=4,
\]
the first weak-order difference appears:
\[
(1,2)
\quad\text{and}\quad
(2,3)
\]
have
\[
RR=\frac12
\quad\text{and}\quad
RR=\frac23,
\]
but both have
\[
OR=\frac13.
\]
Thus the odds ratio already collapses a distinction made by the risk ratio.

At
\[
n=5,
\]
a strict reversal appears for the first time, and it is unique among protective tables:
\[
A=(2,3),
\qquad
B=(3,4).
\]

For trial \(A\),
\[
RR(A)=\frac23,
\qquad
OR(A)=\frac49.
\]

For trial \(B\),
\[
RR(B)=\frac34,
\qquad
OR(B)=\frac38.
\]

Because smaller values represent stronger protection,
\[
RR(A)<RR(B)
\]
says trial \(A\) has the stronger treatment effect, while
\[
OR(A)>OR(B)
\]
says trial \(B\) has the stronger effect.

The mechanism persists for every larger balanced arm size. For every integer
\[
n\ge5,
\]
define
\[
A_n=(n-3,n-2)
\]
and
\[
B_n=(n-2,n-1).
\]
Then
\[
RR(A_n)<RR(B_n)
\]
but
\[
OR(A_n)>OR(B_n).
\]

Thus the first strict ranking conflict occurs at five participants per arm, but the disagreement is structural rather than a one-off finite example.

## Assumptions and scope
Each compared study is a balanced two-arm trial or cohort table with exactly \(n\) subjects in each arm.

All four cells are positive. This excludes zero-cell corrections and infinite odds ratios.

Both comparisons are oriented so that treatment has fewer events than control. If both effects are harmful instead, swapping treatment and control reciprocates both \(RR\) and \(OR\) and preserves strict rank reversal. A comparison with one protective and one harmful effect cannot reverse because both measures lie on the same respective sides of \(1\).

The theorem compares the point estimates computed directly from the two-by-two tables. It does not address sampling uncertainty, confidence intervals, covariate adjustment, or meta-analytic weighting.

## Proof
For a protective balanced table \((a,b)\),
\[
RR=\frac ab
\]
and
\[
OR=\frac{a(n-b)}{b(n-a)}.
\]

For two tables
\[
T=(a,b),
\qquad
U=(c,d),
\]
all relevant denominators are positive. Therefore
\[
RR(T)-RR(U)
\]
has the sign of
\[
ad-bc,
\]
while
\[
OR(T)-OR(U)
\]
has the sign of
\[
ad(n-b)(n-c)-bc(n-a)(n-d).
\]

Hence a strict ranking reversal occurs exactly when
\[
(ad-bc)
\left(
ad(n-b)(n-c)-bc(n-a)(n-d)
\right)
<0.
\]

For
\[
n=2,
\]
there is no protective table with all four cells positive.

For
\[
n=3,
\]
the only protective table is
\[
(1,2),
\]
so there is nothing to compare.

For
\[
n=4,
\]
the protective tables are
\[
(1,2),\ (1,3),\ (2,3).
\]
Their \((RR,OR)\) pairs are
\[
\left(\frac12,\frac13\right),
\quad
\left(\frac13,\frac19\right),
\quad
\left(\frac23,\frac13\right).
\]
There is no strict reversal, although \((1,2)\) and \((2,3)\) tie under \(OR\).

For
\[
n=5,
\]
the six protective tables are
\[
(1,2),\ (1,3),\ (1,4),\ (2,3),\ (2,4),\ (3,4).
\]
Their exact \((RR,OR)\) values are
\[
\left(\frac12,\frac38\right),
\quad
\left(\frac13,\frac16\right),
\quad
\left(\frac14,\frac1{16}\right),
\quad
\left(\frac23,\frac49\right),
\quad
\left(\frac12,\frac16\right),
\quad
\left(\frac34,\frac38\right).
\]
Direct comparison of these six pairs shows exactly one strict reversal:
\[
(2,3)
\quad\text{versus}\quad
(3,4).
\]

For the infinite family,
\[
RR(A_n)
=
\frac{n-3}{n-2}
<
\frac{n-2}{n-1}
=
RR(B_n),
\]
because
\[
(n-2)^2-(n-3)(n-1)=1.
\]

The odds ratios are
\[
OR(A_n)
=
\frac{2(n-3)}{3(n-2)}
\]
and
\[
OR(B_n)
=
\frac{n-2}{2(n-1)}.
\]
The inequality
\[
OR(A_n)>OR(B_n)
\]
is equivalent to
\[
4(n-3)(n-1)>3(n-2)^2,
\]
whose left side minus right side is
\[
n(n-4)>0.
\]
Thus the reversal holds for every
\[
n\ge5.
\]

## Verification
The embedded `verify_rr_or_minimal_reversal.py` uses only the Python standard library and exact rational arithmetic.

It enumerates every protective balanced table with positive cells and checks every unordered pair.

Two independent comparison paths are used:
- direct `Fraction` evaluation of \(RR\) and \(OR\);
- integer cross-multiplication using the exact two sign numerators from the proof.

The verifier confirms:
- no protective table at \(n=2\);
- one table at \(n=3\);
- three tables at \(n=4\), with no strict reversal and exactly the displayed odds-ratio tie;
- six tables at \(n=5\), with exactly one strict reversal;
- the exact witness values \(2/3,3/4,4/9,3/8\);
- the infinite family for every \(5\le n\le500\) as a finite consistency check.

The all-\(n\) family itself is proved symbolically above; finite replay is not a substitute for that proof.

Run:

`python3 verify_rr_or_minimal_reversal.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Davies, Crombie and Tavakoli analyze when odds ratios mislead if read as risk ratios. They emphasize that the discrepancy depends on the initial or baseline risk and becomes larger for common outcomes and larger effects.

Zhang and Yu give the exact conversion
\[
RR
=
\frac{OR}{1-p_0+p_0 OR},
\]
where \(p_0\) is the baseline risk. This formula makes explicit that a fixed odds ratio does not determine a fixed risk ratio without the baseline risk.

Cummings reviews risk ratios and odds ratios for trials and cohort studies in full two-by-two-table notation. The review again shows that when outcomes are common, the odds ratio moves farther from \(1\) than the risk ratio and that the relationship depends on the underlying risk level.

Those sources establish the distinction between the measures and the role of baseline risk. The present finding asks a different finite ordering question: when can two balanced positive-cell trials be ranked in opposite strict orders by the two measures? Targeted searches using rank-reversal language, equal-arm tables, exact event counts, and baseline-risk terminology did not locate the five-per-arm minimum, the unique first pair, or the displayed all-\(n\) family.

## Limitations
The finite minimum assumes equal arm sizes within and across the two compared studies.

All cells are positive; zero-event and all-event tables are excluded.

The claim concerns direct unadjusted effect measures. Adjusted odds ratios, marginal risk ratios, time-to-event measures, and confidence intervals are outside scope.

The result does not claim that one effect measure is universally preferable. It isolates an exact mechanism by which baseline-risk dependence can change cross-study ordering.

An unindexed teaching example, software regression test, or textbook exercise could contain the same small tables even if the sharp minimum theorem is absent.

## References
1. H. T. O. Davies, I. K. Crombie and M. Tavakoli, “When can odds ratios mislead?”, *BMJ* 316, 989–991, published 28 March 1998. DOI: 10.1136/bmj.316.7136.989.
2. J. Zhang and K. F. Yu, “What's the Relative Risk? A Method of Correcting the Odds Ratio in Cohort Studies of Common Outcomes,” *JAMA* 280(19), 1690–1691, published online 18 November 1998. DOI: 10.1001/jama.280.19.1690.
3. P. Cummings, “The Relative Merits of Risk Ratios and Odds Ratios,” *Archives of Pediatrics & Adolescent Medicine* 163(5), 438–445, published online 4 May 2009. DOI: 10.1001/archpediatrics.2009.31.
