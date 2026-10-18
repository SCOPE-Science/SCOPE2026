# A sharp household-count bound on Theil inequality reversals under universal cash grants

## Finding
For every integer \(n\ge 2\), let \(X=(x_1,\ldots,x_n)\) and \(Y=(y_1,\ldots,y_n)\) have strictly positive real components and equal arithmetic mean \(\mu>0\). For a common nonnegative lump-sum grant \(t\), write \(T_X(t)\) and \(T_Y(t)\) for the Theil T indices of the shifted vectors. Unless the two income multisets agree, the equation \(T_X(t)=T_Y(t)\) has at most \(n-2\) distinct solutions with \(t>0\). In particular, the relative ranking changes sign at most \(n-2\) times on positive grants.

This bound is attained when \(n=3\) and \(n=4\). For four households, choose
\[
X=(1,7,25,35),\qquad Y=(2,5,29,32),\qquad\mu=17.
\]
The difference \(T_X(t)-T_Y(t)\) is strictly positive at \(t=0\), strictly negative at \(t=20\), and strictly positive at \(t=40\). It therefore crosses zero exactly twice, once in \((0,20)\) and once in \((20,40)\); exact integer comparisons tighten those brackets to \((5,6)\) and \((32,33)\). This is a reversion of the relative Theil ranking under successive universal cash grants, not merely a single crossing.

## Assumptions and scope
The vectors contain the same number of households, incomes are strictly positive, the two initial arithmetic means agree, and every household in both populations receives the same nonnegative absolute grant. No tax, behavioral, selection, or redistribution responses are modeled. The Theil index of an income vector \(Z\) is
\[
T(Z)=\frac1n\sum_{i=1}^n\frac{z_i}{\bar z}\log\!\left(\frac{z_i}{\bar z}\right),\qquad \bar z=\frac1n\sum_i z_i.
\]
Logarithms are natural. We count distinct zeros on the open half-line \(t>0\), not multiplicities; any strict ranking reversal requires a zero. If \(X\) and \(Y\) have the same income multiset, their Theil indices coincide identically and no strict reversal occurs.

## Proof
Define \(\varphi_t(u)=(t+u)\log(t+u)\) and the unnormalized difference
\[
F(t)=\sum_{i=1}^n\varphi_t(x_i)-\sum_{i=1}^n\varphi_t(y_i).
\]
Equal means imply \(\sum_i x_i=\sum_i y_i=n\mu\), hence normalization terms cancel exactly:
\[
T_X(t)-T_Y(t)=\frac{F(t)}{n(\mu+t)}.\tag{1}
\]
Differentiating the unnormalized difference, the additive constants from the derivatives cancel, giving
\[
F'(t)=\sum_i\log(t+x_i)-\sum_i\log(t+y_i)
=\log\frac{P_X(t)}{P_Y(t)},\quad
P_X(t)=\prod_i(t+x_i),\quad P_Y(t)=\prod_i(t+y_i).\tag{2}
\]
Because both products are monic polynomials of degree \(n\), and their next-to-leading coefficients are their equal sums of incomes, the difference \(Q(t)=P_X(t)-P_Y(t)\) has degree at most \(n-2\). Both products are strictly positive for \(t\ge0\), so \(F'(t)=0\) precisely when \(Q(t)=0\). If \(Q\equiv0\), the products agree as polynomials, which identifies the income multisets and forces \(F\equiv0\). Otherwise \(F'\) has at most \(n-2\) distinct positive zeros.

The expansion \((t+u)\log(t+u)=t\log t+u(1+\log t)+u^2/(2t)+O(t^{-2})\) for fixed \(u>0\), together with equal totals, yields
\[
F(t)=\frac{\sum_i x_i^2-\sum_i y_i^2}{2t}+O(t^{-2}),\qquad \lim_{t\to\infty}F(t)=0.\tag{3}
\]
If \(F\not\equiv0\) has \(m\ge1\) distinct positive zeros, Rolle's theorem gives at least \(m-1\) distinct zeros of \(F'\) between successive zeros. There is also a zero of \(F'\) strictly after the last zero of \(F\): otherwise the nonzero real-analytic function \(F\), starting at zero at the last root and tending to zero at infinity, would be strictly monotone eventually without ever turning, which is impossible. Equivalently, choose a later point at which \(F\ne0\), use a further later value closer to zero, and apply the extreme-value theorem to obtain an interior extremum. Therefore \(m\le n-2\). Equation (1) proves the bound for Theil crossings.

For the four-household witness, polynomial multiplication gives
\[
P_X(t)-P_Y(t)=-3t^2+314t-3155.\tag{4}
\]
Because grants \(t=0,20,40\) are integers, the sign of \(F(t)\) can be determined **exactly without numerical logarithms** by comparing the integer products \(\prod_i(t+x_i)^{t+x_i}\) and \(\prod_i(t+y_i)^{t+y_i}\). The signs are \(+,-,+\), and the same exact-product comparison gives \(F(5)>0>F(6)\), \(F(32)<0<F(33)\). Continuity gives at least two strictly positive zeros, while the general \(n=4\) bound gives at most two. For \(n=3\), \(X=(1,11,24)\) and \(Y=(2,9,25)\), each totaling \(36\), have exactly opposite signs at \(t=0\) and \(t=20\), similarly verified by integer powers, realizing the bound of one reversal. For \(n=2\), \(Q\) is constant and the upper bound is zero. The theorem does not claim attainability of \(n-2\) for all \(n>4\).

## Verification
Run the standalone standard-library program `python3 verify.py`. It reconstructs both quartic product polynomials, checks their difference in (4), performs exact arbitrary-precision integer-product comparisons at grants \(0,5,6,20,32,33,40\), and checks the three-household construction. The program returns `PASS` when its assertions succeed. Its finite arithmetic is an exact witness certificate; the general all-household-size bound is analytical and does not depend on enumeration.

## Relationship to prior work
Theil's entropy index is a standard relative-inequality statistic. Liao, *Income Inequality and Income Segregation* (first public online 11 February 2016), treats social income inequality and decomposition; its inspected accessible text does not state the present fixed-mean universal-grant root-count theorem. Cowell, *Theil, Inequality and the Structure of Income Distribution* (2003), explicitly treats theoretical properties of Theil indices and is a plausible broader source; its complete full text was not accessible in this review, so potential coverage by results about translation or inequality orderings remains a bibliographic risk. The precise claim here is the maximum number of rank changes under a common additive absolute shift, with an exact four-household double-reversal witness, not a generic statement about changing one income or a parameter of an alternative inequality index.

## Limitations
The result relies on equal initial arithmetic means, an identical additive grant in both samples, positive initial incomes, and Theil T rather than other inequality functionals. It neither predicts policy behavior nor implies that double reversals are typical. The first-occurrence four-household construction is explicit but does not classify all such constructions. An undiscovered equivalent theorem in the income-inequality literature, particularly on translative nonrobustness, cannot be ruled out from the accessible bibliography; independent scientific and bibliographic audit has not been performed.

## References
1. Tim Futing Liao, *Income Inequality and Income Segregation*, **Socius** (first published online 2016-02-11), DOI: 10.1177/2378023115627462; https://doi.org/10.1177/2378023115627462.
2. Frank A. Cowell, *Theil, Inequality and the Structure of Income Distribution* (2003); institutional repository listing https://researchonline.lse.ac.uk/id/eprint/2288/ (full text not available through the inspected access route).
