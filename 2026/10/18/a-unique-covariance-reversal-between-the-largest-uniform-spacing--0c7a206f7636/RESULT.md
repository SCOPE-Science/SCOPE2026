# A unique covariance reversal between the largest uniform spacing and the number of long spacings

## Finding

For an integer \(m\ge2\), divide \([0,1]\) at \(m-1\) independent uniform points, and denote the resulting \(m\) (unordered) lengths by \(X_1,\ldots,X_m\). Write \(M_m=\max_i X_i\), \(N_m(t)=\sum_i\mathbf1\{X_i>t\}\), \(0<t<1\), and \(H_m=\sum_{j=1}^m1/j\). There exists precisely one threshold \(t_m\in(0,1)\) such that

\[
\operatorname{Cov}(N_m(t),M_m)<0\quad(0<t<t_m),\qquad
\operatorname{Cov}(N_m(t),M_m)>0\quad(t_m<t<1).
\]

The covariance is zero exactly at \(t_m\) inside \((0,1)\). The exceptional two-spacing value is \(t_2=1/2\); for every \(m\ge3\), \(0<t_m<1/2\). The threshold has the sharp asymptotic expansion

\[
\boxed{m t_m=\log\log m+\log\log\log m+o(1)\qquad(m\to\infty).}
\]

Thus the reversal occurs much earlier than the familiar typical-largest-spacing scale \((\log m)/m\). A finite, rationally evaluable formula for the covariance is given below.

## Assumptions and scope

The uniform breakpoints are independent and continuous, so the lengths form a uniform Dirichlet simplex vector, \(X\sim\operatorname{Dirichlet}(1,\ldots,1)\). Strict and non-strict inequalities give identical probabilities for the thresholds considered. All claims are for integer \(m\ge2\) and real \(0<t<1\). No independence among the spacings is asserted. The same joint law holds for the cyclic gaps of \(m\) independent uniform points on a circle of circumference one (after a cyclic relabeling).

Set \((z)_+=\max\{z,0\}\), \(b=t/(1-t)\), and define

\[
B_m(b)=b-\frac1m\sum_{k=1}^{m-1}
\frac{(-1)^{k+1}\binom{m-1}{k}}{k(k+1)}
\bigl[1-(1-kb)_+^m\bigr].
\]

Then the exact finite-sample formula is

\[
\boxed{\operatorname{Cov}(N_m(t),M_m)
=m(1-t)^m\left[B_m\!\left(\frac{t}{1-t}\right)-
\frac{t}{1-t}\frac{H_m}{m}\right].}
\]

Its unique zero is equivalently specified by \(B_m(b_m)/b_m=H_m/m\), with \(t_m=b_m/(1+b_m)\). The formula is piecewise polynomial in the transformed threshold and involves no uncomputed probabilities.

## Proof

**1. The simplex memoryless shift.** For a uniform simplex vector, \(\Pr(X_1>t)=(1-t)^{m-1}\). Conditional on \(X_1>t\), the full vector has the same distribution as \(t e_1+(1-t)Y\), where \(Y\) is a fresh uniform simplex vector and \(e_1\) is the first coordinate vector. This follows directly by translating and dilating the simplex: the joint density is constant, and the conditional region is a simplex of side factor \(1-t\).

Let \(M=\max_iY_i\), \(\Delta=M-Y_1\ge0\), and \(c_m=\mathbb E M=H_m/m\). The harmonic expectation follows, for example, by integrating the standard inclusion-exclusion tail

\[
\Pr(M>x)=\sum_{k=1}^{m}(-1)^{k+1}\binom mk(1-kx)_+^{m-1},
\]

which gives \(\mathbb E M=\sum_{k=1}^m(-1)^{k+1}\binom mk/(km)=H_m/m\).

For \(b=t/(1-t)\), the shifted maximum obeys the pointwise identity

\[
\max\{t+(1-t)Y_1,(1-t)Y_2,\ldots,(1-t)Y_m\}
=(1-t)\bigl[M+(b-\Delta)_+\bigr].
\]

Consequently, with \(B_m(b)=\mathbb E(b-\Delta)_+\), exchangeability gives

\[
\begin{aligned}
\operatorname{Cov}(N_m(t),M_m)
&=m\Pr(X_1>t)\bigl(\mathbb E[M_m\mid X_1>t]-c_m\bigr)\\
&=m(1-t)^m\bigl[B_m(b)-bc_m\bigr].
\end{aligned}
\]

**2. Explicit stop-loss distribution.** For a specified set \(J\subseteq\{2,\ldots,m\}\) of size \(k\), the simplex integral gives

\[
\Pr\{X_j>X_1+b\text{ for every }j\in J\}
=\frac{(1-kb)_+^{m-1}}{k+1}.
\]

To verify this nonstandard identity, condition on \(X_1=x\). Its density is \((m-1)(1-x)^{m-2}\); the surviving \((m-1)\)-coordinate simplex after the \(k\) restrictions has relative volume \(((1-(k+1)x-kb)_+/(1-x))^{m-2}\). Integrating over \(0\le x\le(1-kb)_+/(k+1)\) yields the displayed expression. Inclusion-exclusion over the events \(X_j>X_1+b\) gives

\[
\Pr(\Delta>b)=\sum_{k=1}^{m-1}(-1)^{k+1}
\binom{m-1}{k}\frac{(1-kb)_+^{m-1}}{k+1}.
\]

The stop-loss identity \(B_m(b)=\int_0^b\Pr(\Delta\le u)\,du\) gives precisely the finite sum under “Assumptions and scope”.

**3. Exactly one covariance reversal.** Define \(R_m(b)=B_m(b)/b=\mathbb E(1-\Delta/b)_+\) for \(b>0\). This is strictly increasing in \(b\): \(\Delta\) has positive probability in every interval \((0,b)\), so the integrand strictly increases on an event of positive probability. Since the coordinates are continuous and exchangeable, \(\Pr(\Delta=0)=1/m\); hence

\[
\lim_{b\downarrow0}R_m(b)=1/m
< H_m/m <1=\lim_{b\to\infty}R_m(b).
\]

Continuity and strict increase imply a unique root \(R_m(b_m)=H_m/m\). The covariance formula proves both strict signs and excludes other interior zeros. For \(m=2\), direct substitution gives \(b_2=1\), so \(t_2=1/2\). For \(m\ge3\), at \(t=1/2\), the event \(X_1>t\) forces \(X_1\) to be the maximum, and \(\mathbb E[M_m\mid X_1>1/2]=(m+1)/(2m)>H_m/m\). Thus \(t_m<1/2\).

**4. Sharp double-logarithmic location.** Let \(E_1,\ldots,E_m\) be independent unit exponential variables, \(S=\sum_iE_i\), and \(Z=\max_{2\le j\le m}E_j\). The normalized vector \((E_1/S,\ldots,E_m/S)\) is uniform Dirichlet, and \(\Delta=(Z-E_1)_+/S\). For every \(v\ge0\), elementary integration gives the exact exponential-difference law

\[
J_m(v):=\Pr(Z-E_1\le v)
=\int_0^\infty e^{-x}(1-e^{-x-v})^{m-1}\,dx
=\frac{e^v}{m}\bigl[1-(1-e^{-v})^m\bigr].
\]

Fix any constant \(C>2\) and put \(\varepsilon_m=m^{-1/4}\). Gamma concentration gives \(\Pr(|S/m-1|>\varepsilon_m)\le 2e^{-c\sqrt m}\) for an absolute \(c>0\) and all sufficiently large \(m\). Therefore, uniformly for \(0\le u\le C\log\log m\), the probability \(\Pr(m\Delta\le u)\) lies between \(J_m(u(1-\varepsilon_m))-2e^{-c\sqrt m}\) and \(J_m(u(1+\varepsilon_m))+2e^{-c\sqrt m}\). In this range, \(m e^{-u}\ge m/(\log m)^C\to\infty\), while \(u\varepsilon_m\to0\). Consequently

\[
\Pr(m\Delta\le u)=\frac{e^u}{m}(1+o(1))
\]

uniformly on that entire range, and integration yields

\[
B_m(s/m)=\frac{e^s-1}{m^2}(1+o(1))
\quad\text{uniformly for }0<s\le C\log\log m.
\]

For \(s=(1-\eta)\log\log m\) and \(s=(1+\eta)\log\log m\), with fixed \(0<\eta<1\), comparison of this expression against \(sH_m/m^2\) makes the former respectively smaller and larger for large \(m\). Strict uniqueness therefore yields \(s_m:=mb_m\sim\log\log m\). At the root, the uniform expansion now gives

\[
e^{s_m}-1=(1+o(1))s_m H_m,
\qquad
s_m=\log H_m+\log s_m+o(1).
\]

Since \(H_m=\log m+O(1)\) and \(s_m\sim\log\log m\), this implies \(s_m=\log\log m+\log\log\log m+o(1)\). Finally, \(m t_m=mb_m/(1+b_m)=s_m+o(1)\), as claimed.

## Verification

The supplied standard-library program `verify.py` evaluates the explicit stop-loss formula using exact rational arithmetic and compares the resulting covariance with an independently integrated inclusion-exclusion formula for \(\mathbb E[M_m\mathbf1\{X_1>t\}]\). It also checks boundary values, monotonicity at many rational points, and precise sign brackets in several dimensions. The program's finite checks are consistency tests; the proof above establishes the result for all integers \(m\ge2\) and all admissible real thresholds.

## Relationship to prior work

The standard uniform-spacing and exponential-normalization representations originate in classical spacing theory. Bairamov, Berred, and Stepanov (online 10 April 2008) give marginal distributions and expectations for ordered uniform spacings, including their largest spacing, and limit results for those order statistics. Their Section 5 considers the number of *a second independent sample's observations inside a chosen spacing*, rather than the number of spacings longer than a deterministic threshold. The present result concerns a cross-statistic covariance, its unique sign transition, and the double-logarithmic transition location. Darling's 1953 random-division paper develops transform techniques for sums of spacing functionals; its accessible abstract does not establish the present mixed maximum/exceedance statement. Broad exact joint order-statistic laws can support rederivations, but no inspected source states or immediately implies this signed covariance classification without additional analysis.

## Limitations

The theorem is restricted to the uniform Dirichlet law. It makes no claim that arbitrary nonuniform sampling or general Dirichlet concentration vectors have the same sign pattern. The literature search cannot exclude an earlier implicit derivation in a general joint spacing result, and Darling's complete paper was not inspected. Independent historical-priority validation has not been performed.

## References

1. I. Bairamov, A. Berred, and A. Stepanov, “Limit results for ordered uniform spacings,” *Statistical Papers* 51 (2010), 227–240. DOI: 10.1007/s00362-008-0134-3. First published online 10 April 2008. Lawfully accessible author PDF: https://dm.ieu.edu.tr/Ism/BaiBerredStep_StatisticalPapers.pdf.
2. D. A. Darling, “On a Class of Problems Related to the Random Division of an Interval,” *Annals of Mathematical Statistics* 24 (1953), 239–253. DOI: 10.1214/aoms/1177729030. Abstract inspected; full text not inspected.
3. R. Pyke, “Spacings,” *Journal of the Royal Statistical Society: Series B* 27 (1965), 395–449. Historical reference from the first cited paper; full text not inspected.
