# Balanced positive-cell Simpson reversal first occurs at eleven per arm
## Finding
Consider a binary adverse outcome in two groups, treatment and control, each with the same total size
\[
m.
\]
Each group is split into two labeled strata.

Write the first-stratum treatment total as \(a\), its adverse-event count as \(x\), the first-stratum control total as \(b\), and its adverse-event count as \(y\). In the second stratum, the corresponding adverse-event counts are \(u\) and \(v\). Thus the second-stratum totals are \(m-a\) and \(m-b\).

Require every one of the eight cells to be positive:
\[
1\le x<a,
\qquad
1\le y<b,
\qquad
1\le u<m-a,
\qquad
1\le v<m-b.
\]

A strict Simpson reversal for adverse-event risk is
\[
\frac{x}{a}<\frac{y}{b},
\qquad
\frac{u}{m-a}<\frac{v}{m-b},
\]
but, after pooling the strata,
\[
\frac{x+u}{m}>\frac{y+v}{m}.
\]

No such positive-cell balanced table exists for
\[
m\le 10.
\]

At
\[
m=11,
\]
strict reversal occurs. There are exactly four labeled first-layer tables, which form exactly two orbits under exchange of the two strata.

One orbit representative is
\[
\begin{array}{c|cc|cc}
&\multicolumn{2}{c|}{\text{Stratum 1}}&\multicolumn{2}{c}{\text{Stratum 2}}\\
&\text{Adverse}&\text{Non-adverse}&\text{Adverse}&\text{Non-adverse}\\\hline
\text{Treatment}&1&2&5&3\\
\text{Control}&3&5&2&1
\end{array}
\]
with
\[
\frac13<\frac38,
\qquad
\frac58<\frac23,
\]
but
\[
\frac6{11}>\frac5{11}.
\]

The second orbit representative is
\[
\begin{array}{c|cc|cc}
&\multicolumn{2}{c|}{\text{Stratum 1}}&\multicolumn{2}{c}{\text{Stratum 2}}\\
&\text{Adverse}&\text{Non-adverse}&\text{Adverse}&\text{Non-adverse}\\\hline
\text{Treatment}&1&3&5&2\\
\text{Control}&2&5&3&1
\end{array}
\]
with
\[
\frac14<\frac27,
\qquad
\frac57<\frac34,
\]
but again
\[
\frac6{11}>\frac5{11}.
\]

Therefore total sample size
\[
22
\]
is necessary and sufficient under equal overall arm sizes and strictly positive cells.

Because every risk is strictly between zero and one, the direction of a treatment-versus-control comparison is the same whether it is expressed by risk difference, risk ratio, or odds ratio. The displayed reversal is therefore an association-sign reversal, not an artifact of one particular binary effect scale.

## Assumptions and scope
There are exactly two strata and two overall groups. Treatment and control have equal total size \(m\), but their stratum allocations need not be equal.

All eight cells are positive. This excludes zero-event and zero-non-event strata, so every risk, risk ratio, and odds ratio is finite and nondegenerate.

The theorem concerns strict reversal of adverse-event risk. Reversing the outcome label gives the equivalent success-rate formulation.

Equal overall arm size is the balancing constraint. Equal allocation within each stratum would make reversal impossible, because the pooled risks would then be weighted by the same stratum proportions.

The result is a finite combinatorial boundary. It does not by itself identify a causal treatment effect; Simpson reversal is precisely a warning that pooled association can be confounded by differing stratum composition.

## Proof
For one arm of total size \(m\), the four positive cells
\[
(\text{stratum 1 adverse},\text{stratum 1 non-adverse},\text{stratum 2 adverse},\text{stratum 2 non-adverse})
\]
form a positive composition of \(m\) into four parts. Hence there are exactly
\[
\binom{m-1}{3}
\]
possible cell quadruples for one arm and
\[
\binom{m-1}{3}^2
\]
possible balanced two-arm tables.

For a table encoded by \((a,b,x,y,u,v)\), the three strict reversal conditions can be tested with exact integer arithmetic:
\[
xb<ya,
\]
\[
u(m-b)<v(m-a),
\]
and
\[
x+u>y+v.
\]
These are exactly the two within-stratum treatment-benefit inequalities and the pooled reversal inequality.

The exhaustive counts of admissible positive-cell balanced tables for
\[
m=4,5,6,7,8,9,10,11
\]
are
\[
1,
16,
100,
400,
1225,
3136,
7056,
14400.
\]
They equal
\[
\binom{m-1}{3}^2
\]
as required.

Exact enumeration finds strict-reversal counts
\[
0,
0,
0,
0,
0,
0,
0,
4.
\]
Thus the lower boundary is exhaustive, not sampled.

At \(m=11\), the four labeled solutions in the encoding above are
\[
(3,8,1,3,5,2),
\]
\[
(4,7,1,2,5,3),
\]
\[
(7,4,5,3,1,2),
\]
and
\[
(8,3,5,2,1,3).
\]
Exchanging the two strata pairs the first with the fourth and the second with the third. Hence there are exactly two first-layer orbits under stratum exchange.

For a binary \(2\times2\) comparison, treatment adverse risk is lower than control adverse risk exactly when the corresponding cross-product difference is negative. The verifier checks that both strata have negative cross-product difference while the pooled table has positive cross-product difference in all four first-layer solutions. Therefore the reversal also changes the direction of the odds ratio and risk ratio.

## Verification
The embedded `verify_balanced_positive_simpson_minimum.py` uses only the Python standard library and exact rational/integer arithmetic.

It independently generates every positive-cell table with equal treatment and control totals for each
\[
4\le m\le11,
\]
checks the exact composition counts, tests the two stratum inequalities and pooled inequality by cross multiplication, and recovers the complete first layer.

It verifies that the first four labeled solutions form exactly two stratum-exchange orbits and checks the association sign by the \(2\times2\) cross-product criterion.

Run:

`python3 verify_balanced_positive_simpson_minimum.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Simpson's 1951 paper is the classical source for the phenomenon. It explicitly warns that amalgamating \(2\times2\) tables can create paradoxical conclusions and gives a treatment example in which treatment is beneficial within both sex strata while the pooled table loses that association.

Later work gives general characterizations and geometric explanations of Simpson reversal. Samuels derives necessary and sufficient conditions for association reversal phenomena, and Linusson and Stamps review the standard two-dimensional reversal before developing a higher-dimensional generalization.

A particularly close public example is the Stanford Encyclopedia of Philosophy's balanced illustration with 13 observations in each comparison group: one rate is \(1/5<2/8\), the other is \(6/8<4/5\), yet the pooled rates are \(7/13>6/13\). All eight cells there are positive. That establishes a balanced positive-cell example at 26 observations, but not minimality.

An archived Brilliant educational page goes further and explicitly asks for the smallest strict Simpson example over unrestricted nonnegative integer counts. Its stated optimization domain allows zero cells and does not impose equal pooled group totals. It therefore does not cover the balanced positive-cell problem solved here.

Targeted searches for equal-arm, positive-cell, minimum-sample, exact-count, and 11-per-arm formulations did not locate the 22-observation boundary or the two-orbit first layer.

## Limitations
The sharp value 22 depends on all eight cells being positive and on equal total treatment and control sizes.

If zero cells are allowed, or if the pooled arm totals are unequal, smaller strict Simpson examples can exist. The theorem makes no claim about those domains.

The two strata are labeled for enumeration; the first-layer classification then factors by the natural stratum-exchange symmetry.

The public smallest-example challenge noted above is a genuine bibliographic proximity risk because it studies an adjacent optimization problem. Its constraints differ materially, but an unindexed solution or teaching note could also have investigated the balanced positive-cell specialization.

## References
1. E. H. Simpson, “The Interpretation of Interaction in Contingency Tables,” *Journal of the Royal Statistical Society, Series B* 13(2), 238–241, July 1951. DOI: 10.1111/j.2517-6161.1951.tb00088.x.
2. M. L. Samuels, “Simpson's Paradox and Related Phenomena,” *Journal of the American Statistical Association* 88(421), 81–88, 1993. DOI: 10.1080/01621459.1993.10594297.
3. S. Linusson and M. T. Stamps, “Association and Simpson conversion in \(2\times2\times2\) contingency tables,” *Algebraic Statistics* 12, 57–74, 2021; arXiv:1809.04633.
4. S. G. Baker and B. S. Kramer, “Good for Women, Good for Men, Bad for People: Simpson's Paradox and the Importance of Sex-Specific Analysis in Observational Studies,” *Journal of Women's Health & Gender-Based Medicine* 10(9), 867–872, 2001. DOI: 10.1089/152460901753285769.
5. “Simpson's Paradox,” *Stanford Encyclopedia of Philosophy*, archived Fall 2023 edition.
6. “Simpson's Paradox,” archived Brilliant Math & Science Wiki, section “Challenging Examples.”
