# Sharp power-correlation range for stationary renewal age and residual life

## Statement

Let a stationary renewal process have strictly positive interarrival time \(X\), with
\(\mu=\mathbb E X\in(0,\infty)\). Let \(A\) and \(R\) be the backward and forward
recurrence times observed at stationarity. Fix \(r>0\) and assume
\(\mathbb E X^{2r+1}<\infty\). Put
\[
Q_r=\frac{(\mathbb E X^{r+1})^2}{\mu\,\mathbb E X^{2r+1}}.
\]
Then \(0<Q_r\le 1\), and
\[
\boxed{
\operatorname{Corr}(A^r,R^r)
=\frac{B(r+1,r+1)-Q_r/(r+1)^2}
       {1/(2r+1)-Q_r/(r+1)^2}}
\tag{1}
\]
where \(B\) is the beta function.

Consequently the exact universal range, over all such renewal laws, is
\[
\boxed{\ell_r\le \operatorname{Corr}(A^r,R^r)<u_r}
\tag{2}
\]
with
\[
u_r=(2r+1)B(r+1,r+1)
=\frac{\Gamma(r+1)^2}{\Gamma(2r+1)},
\tag{3}
\]
and
\[
\ell_r=
\frac{B(r+1,r+1)-(r+1)^{-2}}
     {(2r+1)^{-1}-(r+1)^{-2}}
=
\frac{2r+1}{r^2}\left((r+1)^2B(r+1,r+1)-1\right).
\tag{4}
\]
The lower endpoint is attained exactly when the interarrival time is deterministic.
The upper endpoint is not attained by a nondegenerate renewal law, but it is a sharp
supremum. Every value in \([\ell_r,u_r)\) is attained by a renewal process whose
interarrival distribution has two positive support points.

For integer \(k\ge1\), the bounds simplify to
\[
 u_k=\binom{2k}{k}^{-1},\qquad
 \ell_k=\frac{(k+1)^2/\binom{2k}{k}-(2k+1)}{k^2}.
\tag{5}
\]
Thus the first cases are
\[
[-1,1/2),\qquad[-7/8,1/6),\qquad[-31/45,1/20)
\]
for \(k=1,2,3\), respectively. Moreover
\[
 u_r\sim \frac{\sqrt{\pi r}}{4^r},\qquad \ell_r\sim-\frac2r
\quad(r\to\infty),
\tag{6}
\]
so the entire admissible power-correlation interval collapses to zero at high powers.

The sign is also identified exactly:
\[
\operatorname{Corr}(A^r,R^r)\gtrless0
\quad\Longleftrightarrow\quad
Q_r\lessgtr (r+1)^2 B(r+1,r+1).
\tag{7}
\]
For exponential interarrivals equality holds in (7), consistently with independence
of stationary age and residual life.

## Proof

At a stationary inspection epoch, the containing renewal interval \(L=A+R\) has the
size-biased interarrival distribution
\[
\mathbb E g(L)=\frac{\mathbb E[Xg(X)]}{\mu},
\]
and, conditional on \(L\), the inspection point is uniform in that interval. Equivalently,
\[
(A,R)=(UL,(1-U)L),
\tag{8}
\]
where \(U\sim\mathrm{Unif}(0,1)\) is independent of \(L\). This is also the standard
radial-uniform representation of a bivariate Schur-constant equilibrium law.

Writing \(m_s=\mathbb E X^s\), (8) gives
\[
\mathbb E A^r=\frac{m_{r+1}}{(r+1)\mu},\qquad
\mathbb E A^{2r}=\frac{m_{2r+1}}{(2r+1)\mu},
\]
and
\[
\mathbb E(A^rR^r)
=B(r+1,r+1)\frac{m_{2r+1}}{\mu}.
\]
Since \(A^r\) and \(R^r\) have equal variance, division by that variance gives (1).

Cauchy--Schwarz applied to \(X^{1/2}\) and \(X^{r+1/2}\) yields
\[
0<Q_r=\frac{m_{r+1}^2}{m_1m_{2r+1}}\le1,
\]
with equality if and only if \(X^r\) is almost surely constant, hence, for positive \(X\),
if and only if \(X\) is deterministic.

Let \(a=B(r+1,r+1)\), \(b=(r+1)^{-2}\), and \(c=(2r+1)^{-1}\).
Because \(U^r\) and \((1-U)^r\) are strictly oppositely monotone,
\(a<(\mathbb EU^r)^2=b<c\). Therefore
\[
q\longmapsto \frac{a-bq}{c-bq}
\]
is strictly decreasing on \((0,1]\). Substitution of \(q=1\) gives (4), while
\(q\downarrow0\) gives (3), proving the endpoint bounds.

It remains to show that no values between the endpoints are missing. For any \(M>1\),
let a candidate stationary interval length \(L\) take values \(1,M\), with probability
\(p\) at \(M\). Then
\[
q(p,M)=\frac{(\mathbb E L^r)^2}{\mathbb E L^{2r}}
\]
is continuous in \(p\), equals \(1\) at \(p=0\), and for \(p=M^{-r}\) tends to zero
as \(M\to\infty\). Hence every \(q\in(0,1]\) occurs for some finite two-point law
of \(L\). Such a law is the size-biased interval law of a positive two-point renewal
interarrival distribution: if \(H\) is the law of \(L\), define
\[
\mu=\left(\int x^{-1}\,dH(x)\right)^{-1},\qquad
 dF(x)=\mu x^{-1}\,dH(x).
\]
Then \(F\) is a probability law with mean \(\mu\) and size-biased law \(H\).
Thus all values in (2) are attained except the limiting upper endpoint, which would
require \(Q_r=0\).

Equation (5) follows from
\(B(k+1,k+1)=((2k+1)\binom{2k}{k})^{-1}\). Equation (6) follows from the gamma
ratio asymptotic. Finally, (7) follows by setting the numerator of (1) equal to zero.
For an exponential interarrival law,
\[
Q_r=\frac{\Gamma(r+2)^2}{\Gamma(2r+2)}
=(r+1)^2B(r+1,r+1),
\]
which proves the stated benchmark.

## Context and prior literature

The linear case \(r=1\) is classical. Gakis and Sivazlian (1994) derived steady-state
correlation formulas for backward and forward recurrence times, and later work studied
stationary covariance and finite-time joint moments. Nelsen (2005) developed the
Schur-constant representation and dependence theory; Nair and Sankaran (2014) applied
that framework directly to stationary renewal age and residual life. In particular, the
radial-uniform decomposition (8) is prior theory, not a new claim here. The range
\([-1,1/2)\) for ordinary Schur-constant correlation is also known in the literature.

The contribution claimed here is the exact all-\(r>0\) power-correlation formula and
its **sharp distribution-free attainable interval**, including endpoint/extremizer
classification, the two-point attainability construction, the exponential sign threshold,
and the high-power collapse. To the best of our knowledge, the literature search did not
locate this powered-correlation envelope or an equivalent theorem. Raw joint-moment
identities themselves are not claimed as new.

## Limitations

The result concerns equal powers \(A^r,R^r\) and Pearson correlation at stationarity.
It does not give the sharp range for unequal powers, finite-time recurrence pairs, rank
correlations, mutual information, or conditional dependence given observed covariates.
The upper endpoint is a supremum rather than a maximum. The originality assessment has
residual risk from older Schur-constant and \(\ell_1\)-symmetric literature in which the
same envelope might be implicit under different terminology.

## References

- K. G. Gakis and B. D. Sivazlian (1994), *The correlation of the backward and forward recurrence times in a renewal process*, Stochastic Analysis and Applications 12(5), 543--549. DOI: 10.1080/07362999408809372.
- R. B. Nelsen (2005), *Some properties of Schur-constant survival models and their copulas*, Brazilian Journal of Probability and Statistics 19, 179--190.
- N. U. Nair and P. G. Sankaran (2014), *Modelling lifetimes with bivariate Schur-constant equilibrium distributions from renewal theory*, METRON 72, 331--349. DOI: 10.1007/s40300-014-0045-0.
- N. U. Nair and P. G. Sankaran (2014), *Characterizations and time-dependent association measures for bivariate Schur-constant distributions*, Brazilian Journal of Probability and Statistics 28(3), 409--423. DOI: 10.1214/12-BJPS215.
- S. Losidis and K. Politis (2019), *The covariance of the backward and forward recurrence times in a renewal process: the stationary case and asymptotics for the ordinary case*, Stochastic Models 35, 51--62. DOI: 10.1080/15326349.2019.1575752.
- S. Losidis, K. Politis and G. Psarrakos (2021), *Exact Results and Bounds for the Joint Tail and Moments of the Recurrence Times in a Renewal Process*, Methodology and Computing in Applied Probability 23, 1489--1505. DOI: 10.1007/s11009-020-09787-w.
- C. Lefèvre and M. Simon (2021), *Schur-Constant and Related Dependence Models, with Application to Ruin Probabilities*, Methodology and Computing in Applied Probability 23, 317--339. DOI: 10.1007/s11009-019-09744-2.
