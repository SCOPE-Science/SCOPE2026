# Four households are the sharp threshold for double Atkinson inequality-rank reversal

## Finding

Let \(X=(x_1,\ldots,x_n)\) and \(Y=(y_1,\ldots,y_n)\) have strictly positive incomes and equal arithmetic means. Write \(A_\varepsilon\) for the Atkinson inequality index with inequality-aversion parameter \(\varepsilon>0\). As \(\varepsilon\) increases, the strict sign of \(A_\varepsilon(X)-A_\varepsilon(Y)\) changes at most once when \(n\leq3\). This is sharp for the phenomenon of two changes: with four households,
\[
X=(4,9,9,22),\qquad Y=(5,5,16,18),\qquad \overline X=\overline Y=11,
\]
there are exactly two positive-aversion crossing values \(\varepsilon_1\) and \(\varepsilon_2\), with
\[
1.42112151258<\varepsilon_1<1.42112151259,
\quad 2.14055381942<\varepsilon_2<2.14055381944.
\]
The index ranks \(X\) strictly more unequal for \(0<\varepsilon<\varepsilon_1\) and for \(\varepsilon>\varepsilon_2\), but strictly less unequal for \(\varepsilon_1<\varepsilon<\varepsilon_2\). Equality occurs exactly at the two displayed crossing values. Thus four is the minimum population size permitting this return of the same strict Atkinson inequality ranking.

## Assumptions and scope

Incomes are finite, real, and strictly positive. Both profiles consist of the same number \(n\geq1\) of equally weighted households and have the same positive arithmetic mean \(\mu\). No claim is made for unequal means, unequal population weights, zeros, or negative incomes. For \(r=1-\varepsilon\), define the power mean
\[
M_r(X)=\left(\frac1n\sum_{i=1}^n x_i^r\right)^{1/r}\quad(r\ne0),\qquad
M_0(X)=\left(\prod_{i=1}^n x_i\right)^{1/n}.
\]
The index is \(A_\varepsilon(X)=1-M_{1-\varepsilon}(X)/\mu\) for all \(\varepsilon>0\), including its continuous definition at \(\varepsilon=1\). A *strict ranking change* means opposite strict signs on two adjacent open parameter intervals, not an isolated tangency or a boundary tie at \(\varepsilon=0\). Equality of income multisets yields identically equal indices and no strict changes.

## Proof

**1. Translating an index comparison into exponential zeros.** Set
\[
F(r)=\sum_{i=1}^n x_i^r-\sum_{i=1}^n y_i^r.
\]
For \(r\ne0\), power-mean monotonicity with respect to the positive sum in the parenthesis gives
\[
\operatorname{sgn}\big(A_{1-r}(X)-A_{1-r}(Y)\big)
=-\operatorname{sgn}\big(F(r)/r\big).
\]
At \(r=0\), the same formula holds by continuity with \(F(r)/r\) interpreted as \(F'(0)\): the sign of the geometric-mean difference is the sign of \(\sum_i\log x_i-\sum_i\log y_i\). The assumptions force \(F(0)=0\) (equal number of entries) and \(F(1)=0\) (equal totals). The parameter range \(\varepsilon>0\) corresponds to \(r<1\).

**2. Root-count lemma (classical generalized Descartes rule).** If \(0<t_1<\cdots<t_m\) and all real coefficients \(c_j\ne0\), the number of real zeros of \(H(r)=\sum_j c_jt_j^r\), counted with multiplicity, does not exceed the sign variations of \((c_1,\ldots,c_m)\). Here is a proof outline sufficient for this use. Write \(H(r)=e^{\lambda_1r}K(r)\), where \(\lambda_j=\log t_j\) and \(K(r)=c_1+\sum_{j>1}c_je^{(\lambda_j-\lambda_1)r}\). The derivative \(K'\) has the coefficient signs of \((c_2,\ldots,c_m)\). Induct on the number of terms using Rolle's theorem with zero multiplicities. If \(c_1c_2<0\), the deleted first coefficient removes one sign change, and Rolle bounds the zeros of \(K\) by those of \(K'\) plus one. If \(c_1c_2>0\), \(K\) and \(K'\) initially have the same sign as \(r\to-\infty\); \(K\) cannot vanish before the first zero of \(K'\). Rolle then bounds the number of zeros of \(K\) by those of \(K'\) without an extra one. The one-term case is immediate. This is the standard Laguerre extension of Descartes' rule; it is not asserted to be new.

**3. At most three households.** The cases \(n=1\) and \(n=2\) have a fixed order by majorization, since equal-total two-element multisets are totally ordered by their spread. For \(n=3\), cancel matching values and collect equal bases in \(F\). The resulting ordered signed coefficient sequence has at most four changes. Indeed, it contains at most three positive and at most three negative contributions. Five changes would require six distinct alternating income levels. Then either the three ordered \(x\)-values are respectively all smaller than the three ordered \(y\)-values or vice versa, contradicting the common sum.

If one triple has both the smaller minimum and the larger maximum, it majorizes the other. The same conclusion, possibly with the roles reversed, applies if either extreme ties. All strictly concave welfare functions—and in particular every positive-aversion Atkinson index—then give one fixed inequality ordering. In the remaining case, after potentially exchanging \(X\) and \(Y\), both the minimum and maximum incomes of \(X\) are smaller than the corresponding extrema of \(Y\). Hence \(F(r)>0\) for all sufficiently negative \(r\), because the smallest income dominates there, while \(F(r)<0\) for all sufficiently positive \(r\), because the largest income dominates there. An exponential polynomial with these opposite end signs has an odd total number of real zeros counted with multiplicity (all its zeros are isolated and finite by the lemma). It has at most four, so at most three, zeros counted with multiplicity. Of those, the mandatory zeros \(r=0\) and \(r=1\) consume at least two. Thus at most one extra zero or unit of multiplicity is available. After dividing out the mandatory zero at \(r=0\), the continuous comparison function \(F(r)/r\) can therefore have at most one zero on \(r<1\); the forced zero at \(r=1\) is outside the positive-aversion interval. At most one strict inequality-rank change follows.

**4. Four-household witness and exact completeness.** For the displayed profiles,
\[
F(r)=4^r-2\cdot5^r+2\cdot9^r-16^r-18^r+22^r.
\]
The signed coefficients in order of increasing income are \((+1,-2,+2,-1,-1,+1)\), with exactly four sign changes; therefore the root-count lemma permits at most four real zeros, with multiplicities. Two are the forced roots \(F(0)=F(1)=0\). Direct exact rational evaluation gives
\[
F(-2)=\frac{142063}{62726400}>0,\qquad
F(-1)=-\frac1{2640}<0.
\]
Also,
\[
F'(0)=\log\left(\frac{4\cdot9^2\cdot22}{5^2\cdot16\cdot18}\right)
=\log\left(\frac{99}{100}\right)<0,
\]
so \(F(r)>0\) for all sufficiently small negative \(r\). There is therefore at least one root in \((-2,-1)\) and at least one in \((-1,0)\). These two, along with \(0\) and \(1\), exhaust the four-root bound; all are simple. Denote the negative roots by \(r_a<r_b<0\). Their crossing parameters are \(\varepsilon_1=1-r_b\) and \(\varepsilon_2=1-r_a\). Exact signs of \(F\), continuity, and the absence of further roots show that \(F(r)/r\) is negative for \(r<r_a\), positive for \(r_a<r<r_b\), and negative for \(r_b<r<1\), with the continuous interpretation at \(r=0\). The sign formula in Step 1 proves the claimed strict pattern, equality cases, and sharp minimal population size.

## Verification

Run `python3 verify.py` from a directory containing the accompanying complete `verify.py` artifact. It uses only the Python 3 standard library and checks the common income total, the ordered signed coefficients and four sign changes, the two exact rational power-sum evaluations, the exact product ratio \(99/100\), and the exhaustive three-plus-three alternating sign patterns that underlie the elementary lower-bound argument. High-precision decimal bisection reproduces the displayed crossing approximations. The analytic root-count argument, not the finite computations or numeric bisection, proves uniqueness of both roots and the population-size lower bound.

## Relationship to prior work

Atkinson (1970) defined the inequality family and established the welfare interpretation of Lorenz dominance; it also exhibited dependence of empirical rankings on inequality aversion. The generalized Descartes theorem for signed power sums is classical and discussed by Fejzić, Freiling, and Rinne (2009) in the context of alternating data sets. Aaberge (2008) developed higher-order Lorenz dominance for intersecting Lorenz curves. Chiu (2021) examined aversion conditions for *linear rank-dependent* inequality indices, particularly the S-Gini family. Creedy (2019, 2023) directly studied the sensitivity of Atkinson comparisons to the aversion parameter. The specific sharp boundary between three and four equal-weight positive-income households for **two strict reentries by one and the same Atkinson measure family**, with an exact witness and all-parameter root count, was not found in the inspected material. This statement is a limited literature comparison, not a claim that search establishes absolute novelty.

## Limitations

The result concerns theoretical index comparisons for equally weighted finite populations of the same size and mean. The witness is a deterministic mathematical income profile, not empirical evidence about households, welfare preferences, or the effect of a tax reform. Full text of the particularly relevant Creedy (2019, 2023) studies could not be checked; stronger prior coverage remains possible. No claim is made about the maximum number of reentries for populations above four, the minimum aggregate income among integer witnesses, or statistically estimated indices.

## References

1. A. B. Atkinson (1970), *On the measurement of inequality*, Journal of Economic Theory 2, 244–263. DOI: 10.1016/0022-0531(70)90039-6. Full text: https://cpi.stanford.edu/_media/pdf/Classic_Media/Atkinson_1970_Measurement%20and%20Methodology.pdf
2. H. Fejzić, C. Freiling, and D. Rinne (2009), *Descartes' Rule of Signs, Alternations of Data Sets, and Balanced Differences*, American Mathematical Monthly 116, 316–327. DOI: 10.1080/00029890.2009.11920943.
3. R. Aaberge (2008), *Ranking Intersecting Lorenz Curves*, IZA Discussion Paper 3852. Full text: https://docs.iza.org/dp3852.pdf
4. W. H. Chiu (2021), *Intersecting Lorenz curves and aversion to inverse downside inequality*, Social Choice and Welfare. DOI: 10.1007/s00355-020-01288-6.
5. J. Creedy (2019), *The Atkinson Inequality Measure and Inequality Aversion*, Working Papers in Public Finance 01/2019. Bibliographic record: https://ideas.repec.org/p/vuw/vuwcpf/20918.html
6. J. Creedy (2023), *Comparing Income Distributions Using Atkinson's Measure of Inequality*, Australian Economic Review 56, 141–155. DOI: 10.1111/1467-8462.12499.
