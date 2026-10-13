# Absolute and relative risk reduction first reverse at six patients per arm
## Finding
Consider a balanced binary-outcome trial with
\[
m
\]
patients in the treatment arm and
\[
m
\]
patients in the control arm.

Let
\[
t
\]
be the number of adverse events in the treatment arm and
\[
c
\]
the number of adverse events in the control arm. Assume every cell of the \(2\times2\) table is positive and treatment is beneficial:
\[
1\le t<c\le m-1.
\]

The absolute risk reduction is
\[
\mathrm{ARR}
=
\frac{c-t}{m}.
\]

The number needed to treat is
\[
\mathrm{NNT}
=
\frac{1}{\mathrm{ARR}}
=
\frac{m}{c-t}.
\]

The relative risk reduction is
\[
\mathrm{RRR}
=
1-\frac{t}{c}
=
\frac{c-t}{c}.
\]

For
\[
m\le5,
\]
there is no pair of admissible trials that ARR/NNT and RRR rank in opposite strict orders.

At
\[
m=6,
\]
strict reversal occurs for the first time. There are
\[
10
\]
admissible positive-cell treatment-benefit tables, and exactly
\[
2
\]
unordered pairs reverse.

A simple witness is
\[
X=(t,c)=(1,2)
\]
and
\[
Y=(3,5).
\]

For \(X\),
\[
\mathrm{ARR}(X)=\frac16,
\qquad
\mathrm{NNT}(X)=6,
\qquad
\mathrm{RRR}(X)=\frac12.
\]

For \(Y\),
\[
\mathrm{ARR}(Y)=\frac13,
\qquad
\mathrm{NNT}(Y)=3,
\qquad
\mathrm{RRR}(Y)=\frac25.
\]

Thus the absolute measure says that \(Y\) has the larger treatment effect,
\[
\mathrm{ARR}(Y)>\mathrm{ARR}(X),
\]
equivalently the smaller number needed to treat,
\[
\mathrm{NNT}(Y)<\mathrm{NNT}(X),
\]
while the relative measure gives the opposite strict ranking,
\[
\mathrm{RRR}(X)>\mathrm{RRR}(Y).
\]

The disagreement persists for every larger equal arm size. For every integer
\[
m\ge6,
\]
compare
\[
X_m=(t,c)=(1,2)
\]
with
\[
Y_m=(m-3,m-1).
\]
Then
\[
\mathrm{ARR}(X_m)=\frac1m
<
\frac2m
=
\mathrm{ARR}(Y_m),
\]
but
\[
\mathrm{RRR}(X_m)=\frac12
>
\frac{2}{m-1}
=
\mathrm{RRR}(Y_m).
\]

## Assumptions and scope
The outcome is binary and adverse.

The treatment and control arms have the same size. Equal arm sizes make ARR ranking depend only on the integer number of adverse events prevented.

Every confusion-table cell is required to be positive:
\[
1\le t<c\le m-1.
\]
This excludes zero-event edge cases and infinite or degenerate relative summaries.

The theorem compares point estimates only. It does not address sampling uncertainty, confidence intervals, statistical significance, duration of treatment, adverse effects of treatment itself, or transport to populations with different baseline risk.

NNT is used only as the reciprocal of positive ARR, so lower NNT and higher ARR are exactly equivalent rankings.

## Proof
Put
\[
d=c-t,
\]
the number of adverse events prevented in the equal-size trial.

Then
\[
\mathrm{ARR}=\frac dm,
\]
so at fixed \(m\), ARR ranking is exactly ranking by \(d\).

By contrast,
\[
\mathrm{RRR}=\frac dc.
\]

Therefore two trials \((d_1,c_1)\) and \((d_2,c_2)\) reverse exactly when
\[
(d_1-d_2)
\left(
\frac{d_1}{c_1}
-
\frac{d_2}{c_2}
\right)
<0.
\]

This is the complete algebraic criterion: the absolute measure rewards the larger number of events prevented, while the relative measure rewards the larger prevented fraction of the control-group event count.

For the finite boundary, every admissible balanced table is one integer pair
\[
(t,c)
\]
with
\[
1\le t<c\le m-1.
\]
Hence the number of admissible tables is
\[
\binom{m-1}{2}.
\]

For
\[
m=2,3,4,5,6,
\]
these counts are
\[
0,\ 1,\ 3,\ 6,\ 10.
\]

Exact comparison of every unordered pair gives strict-reversal counts
\[
0,\ 0,\ 0,\ 0,\ 2.
\]

At \(m=6\), the two reversing pairs are
\[
(1,2)\ \text{versus}\ (3,5)
\]
and
\[
(1,3)\ \text{versus}\ (2,5).
\]
Thus six patients per arm are necessary and sufficient under the stated positive-cell assumptions.

For the persistent family,
\[
X_m=(1,2)
\]
has
\[
d_X=1
\]
and
\[
\mathrm{RRR}(X_m)=\frac12.
\]
Meanwhile
\[
Y_m=(m-3,m-1)
\]
has
\[
d_Y=2
\]
and
\[
\mathrm{RRR}(Y_m)=\frac2{m-1}.
\]
For every
\[
m\ge6,
\]
one has
\[
\frac2{m-1}<\frac12.
\]
Hence ARR prefers \(Y_m\) and RRR prefers \(X_m\) for every \(m\ge6\).

## Verification
The embedded `verify_arr_rrr_minimal_reversal.py` uses only the Python standard library and exact rational arithmetic.

For every
\[
2\le m\le6,
\]
it generates every positive-cell beneficial table
\[
1\le t<c\le m-1,
\]
computes ARR, NNT, and RRR from their definitions, and compares every unordered pair.

It verifies admissible-table counts
\[
0,\ 1,\ 3,\ 6,\ 10
\]
and strict-reversal counts
\[
0,\ 0,\ 0,\ 0,\ 2.
\]

It verifies the exact first-layer pair list and the displayed witness.

It also checks the algebraic reversal criterion throughout a larger finite range and replays the persistent family for every
\[
6\le m\le500.
\]

Run:

`python3 verify_arr_rrr_minimal_reversal.py`

The first output line must be `VERIFY_OK`.

The all-\(m\) persistence statement is proved symbolically above; the finite replay establishes the exhaustive lower boundary.

## Relationship to prior work
Laupacis, Sackett, and Roberts introduced the number-needed-to-treat formulation for comparing clinical consequences of treatment.

Cook and Sackett give the directly relevant full treatment-effect formulas. They define ARR as the control event probability minus the treatment event probability, define RRR as ARR divided by the control event probability, and define NNT as the reciprocal of ARR. Their hypertension example is especially close in spirit: the same \(40\%\) RRR corresponds to markedly different absolute reductions and NNT values when baseline risks differ.

Schechtman later compares ARR, NNT, RR, RRR, and odds ratio in one framework and explicitly shows that different measures can give different impressions. Her examples include equal RRR with different ARR/NNT and equal ARR/NNT with different RRR, which demonstrates tie splitting between the absolute and relative summaries.

Those prior results establish the clinical importance of the distinction and the baseline-risk mechanism. They do not state the discrete sharp boundary proved here: under equal arm sizes, beneficial positive-cell tables cannot strictly reverse before six patients per arm, exactly two pairs reverse at the first layer, and an explicit family persists for every larger arm size.

Targeted searches using ARR, RRR, NNT, ranking reversal, equal arm size, six patients per arm, and the exact witness fractions did not locate this minimum-size theorem.

## Limitations
The sharp cutoff depends on equal treatment and control arm sizes and the requirement that every \(2\times2\) cell be positive.

Allowing zero cells lowers the smallest possible arm size.

Unequal arm sizes create a different lattice problem because ARR no longer depends only on an integer event-count difference.

The theorem concerns ordinal disagreement between point estimates. It does not imply that either metric is clinically preferable in all settings.

Existing literature already establishes that relative and absolute measures can create different impressions. The new claim is only the exact finite positive-cell boundary, its first-layer census, and the persistent integer family.

An unindexed teaching example or software test could contain the same six-per-arm witness even though the sharp minimality result was not located.

## References
1. A. Laupacis, D. L. Sackett, and R. S. Roberts, “An Assessment of Clinically Useful Measures of the Consequences of Treatment,” *New England Journal of Medicine* 318, 1728–1733, published 30 June 1988. DOI: 10.1056/NEJM198806303182605.
2. R. J. Cook and D. L. Sackett, “The number needed to treat: a clinically useful measure of treatment effect,” *BMJ* 310, 452–454, published 18 February 1995. DOI: 10.1136/bmj.310.6977.452.
3. E. Schechtman, “Odds Ratio, Relative Risk, Absolute Risk Reduction, and the Number Needed to Treat—Which of These Should We Use?,” *Value in Health* 5, 431–436, first published 16 September 2002. DOI: 10.1046/j.1524-4733.2002.55150.x.
