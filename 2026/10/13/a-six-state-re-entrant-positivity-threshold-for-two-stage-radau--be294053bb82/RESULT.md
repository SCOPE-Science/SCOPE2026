# A six-state re-entrant positivity threshold for two-stage Radau IIA on pure-birth chains
## Finding
Consider the homogeneous unit-rate absorbing pure-birth chain on \(N\ge2\) states,
\[
Q_N=\begin{pmatrix}
-1&1&&&\\
&-1&1&&\\
&&\ddots&\ddots&\\
&&&-1&1\\
&&&&0
\end{pmatrix}.
\]
Apply the two-stage, third-order Radau IIA method. Its stability function is
\[
R(z)=\frac{1+z/3}{1-2z/3+z^2/6}.
\]
Then every row of the endpoint matrix \(R(hQ_N)\) sums to one for every \(h\ge0\), and its exact entrywise-nonnegativity sets are:

* for \(2\le N\le5\), exactly \(0\le h\le3\);
* for \(N=6\), exactly
\[
h=0\quad\text{or}\quad \eta\le h\le3,
\]
where \(\eta\) is the unique positive root of
\[
p(h)=h^5+30h^4+180h^3+360h^2+180h-72,
\]
namely
\[
\eta=0.253946561637298\ldots.
\]
Thus six states are the first in this homogeneous pure-birth hierarchy for which every sufficiently small positive step is non-Markov, but positivity re-enters at an intermediate step size.

## Assumptions and scope
A Markov generator is used in row-vector convention, so \(Q_N\mathbf 1=0\). Endpoint positivity means entrywise nonnegativity of the one-step matrix; intermediate Runge--Kutta stage values are not classified. The birth rate has been normalized to one; for rate \(\lambda>0\), replace \(h\) by \(\lambda h\).

The claim concerns the homogeneous pure-birth hierarchy, not arbitrary continuous-time Markov generators. The minimality statement is therefore only within this hierarchy.

## Proof
Write the transient \((N-1)\times(N-1)\) block as
\[
Q_T=-I+S,
\]
where \(S\) is the nilpotent superdiagonal shift. Analytic functional calculus gives
\[
R(hQ_T)=\sum_{k=0}^{N-2} c_k(h)S^k,
\qquad
c_k(h)=\frac{h^k}{k!}R^{(k)}(-h).
\]
With \(D=h^2+4h+6>0\), the coefficients needed through six states are
\[
 c_0=\frac{2(3-h)}D,
\]
\[
 c_1=\frac{-2h(h^2-6h-18)}{D^2},
\qquad
 c_2=\frac{-2h^2(h+3)(h^2-12h-18)}{D^3},
\]
\[
 c_3=\frac{-2h^3(h^4-12h^3-108h^2-216h-108)}{D^4},
\]
\[
 c_4=\frac{-2h^4(h^5-15h^4-180h^3-540h^2-540h-108)}{D^5}.
\]
For \(0\le h\le3\), every displayed coefficient is nonnegative. For the last three polynomials this follows immediately from \(h^2\le3h\), \(h^4\le3h^3\), and \(h^5\le3h^4\), respectively.

Because each row sum is one, the absorbing-column entry from a state at distance \(m\) from absorption is
\[
t_m(h)=1-\sum_{k=0}^{m-1}c_k(h).
\]
Direct simplification gives
\[
t_1=\frac{h(h+6)}D,
\qquad
t_2=\frac{h^2(h^2+12h+18)}{D^2},
\]
\[
t_3=\frac{h^3(h^3+18h^2+54h+36)}{D^3},
\]
\[
t_4=\frac{h^4(h^4+24h^3+108h^2+144h+36)}{D^4},
\]
and
\[
t_5=\frac{h^5p(h)}{D^5}.
\]
Thus \(t_1,\ldots,t_4\ge0\) for every \(h\ge0\). The polynomial \(p\) has exactly one sign change in its coefficient list, so Descartes' rule of signs gives at most one positive root. Since \(p(0)=-72\) and \(p(3)>0\), it has exactly one positive root \(\eta\). Hence \(t_5<0\) on \(0<h<\eta\) and \(t_5\ge0\) on \(h\ge\eta\).

For \(N\le5\), every matrix entry on \(0\le h\le3\) is one of \(c_0,\ldots,c_3\) or \(t_1,\ldots,t_4\), hence is nonnegative. For \(N=6\), the only additional needed terms are \(c_4\) and \(t_5\), giving the re-entrant interval. Finally, for every \(N\ge2\) and every \(h>3\), each transient diagonal equals \(c_0<0\), so positivity fails. This proves all stated if-and-only-if classifications.

## Verification
The accompanying `verify.py` independently reconstructs the rational coefficient formulas with exact integer polynomial arithmetic, checks the closed forms for \(c_0,\ldots,c_4\) and \(t_1,\ldots,t_5\), verifies the rational sign bracket
\[
p(2539/10000)<0<p(127/500),
\]
and checks the exact witnesses
\[
t_5(1/4)=-\frac{1607}{18424351793}<0,
\qquad
t_5(1/2)=\frac{4237}{39135393}>0.
\]
The checker validates algebra used in the proof; uniqueness of the positive root and the full intervals follow analytically from Descartes' rule and the sign arguments above.

## Relationship to prior work
Hairer and Wanner describe Radau IIA as a canonical family for stiff differential equations, give the Runge--Kutta stability-function formula, and list the two-stage order-three Radau IIA stability function used here. Their treatment establishes A-stability, stiff accuracy, and damping properties, not the finite-state Markov positivity classification above.

Horváth studies positivity step-size thresholds for Runge--Kutta methods on broad classes of positive initial-value problems. His full paper establishes general positivity step-size thresholds and special positively invariant subsets. Those thresholds require positivity uniformly across all smaller step sizes and do not give the exact nonmonotone six-state Radau window derived here. The present statement is more specific: it gives an exact state-count boundary and re-entrant positivity window for one homogeneous Markov hierarchy.

The closest published semantic-database result found is the eight-state positivity barrier for the distinct fourth-order diagonal \([2/2]\) Padé / two-stage Gauss--Legendre map. That result has a different rational stability function and an eight-state onset, so it does not imply the six-state Radau IIA classification.

## Limitations
No claim is made for arbitrary CTMC generators, nonuniform birth rates, internal-stage positivity, or higher-stage Radau IIA methods. Horváth's broad positivity theory is relevant prior work, but its inspected results do not give this exact six-state Radau classification. An unindexed equivalent specialization remains a possible priority risk. The exact result is therefore limited to the displayed homogeneous pure-birth family.

## References
1. E. Hairer and G. Wanner, *Stiff differential equations solved by Radau methods*, Journal of Computational and Applied Mathematics 111 (1999), 93--111, DOI: 10.1016/S0377-0427(99)00134-X.
2. Z. Horváth, *On the positivity step size threshold of Runge--Kutta methods*, Applied Numerical Mathematics 53 (2005), 341--356, DOI: 10.1016/j.apnum.2004.08.026.
