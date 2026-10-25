# Exact Gini–Greenwood dependence and calibration of a ranked-spacings test

## Finding

For every integer \(m\ge2\), let \((X_1,\ldots,X_m)\sim\operatorname{Dirichlet}(1,\ldots,1)\) and define the normalized spacing Gini statistic and Greenwood statistic
\[
G_m=\frac1m\sum_{1\le i<j\le m}|X_i-X_j|,\qquad Q_m=\sum_{i=1}^m X_i^2.
\]
Their exact dependence is
\[
\operatorname{Cov}(G_m,Q_m)=\frac{m-1}{2m(m+1)(m+2)}>0,\qquad
\operatorname{Corr}(G_m,Q_m)=\frac12\sqrt{\frac{3(m+3)}{m+2}}.
\]
The correlation decreases strictly with \(m\) but tends to \(\sqrt3/2\), not zero.

Let \(X_{(1)}\le\cdots\le X_{(m)}\) and consider the ranked-spacing discrepancy originally proposed by Jammalamadaka and Goria (2004), with their parameter \(n=m-1\):
\[
T_m=\sum_{i=1}^m\left(X_{(i)}-\frac{i}{m^2}\right)^2.
\]
Its exact mean and variance are
\[
\mathbb ET_m=\frac{(m-1)(5m^2-2m-1)}{6m^3(m+1)},
\]
\[
\boxed{\operatorname{Var}(T_m)=
\frac{(m-1)^2(37m^3-4m^2-23m-6)}{12m^4(m+1)^2(m+2)(m+3)}.}
\]
Furthermore,
\[
m^{3/2}\left(T_m-\frac5{6m}\right)\xrightarrow{d}N\left(0,\frac{37}{12}\right).
\]
The exact finite-sample covariance and variance, not the already-proposed statistic or general asymptotic methodology, constitute the principal claim.

## Assumptions and scope

An iid sample of \(m-1\) points drawn from a specified continuous distribution is mapped to \((0,1)\) by its distribution function. Its \(m\) successive boundary-inclusive spacings have the stated uniform Dirichlet law. The claims concern the fully specified continuous null, \(m\ge2\), and not alternatives, estimated parameters, or the full exact density of \(T_m\). Our \(G_m\) divides the sum over unordered spacing pairs by \(m\), unlike some earlier Gini normalizations.

## Proof

**First and second moments of the two marginal statistics.** Standard Dirichlet moments give
\[
\mathbb EQ_m=\frac2{m+1},\qquad
\operatorname{Var}(Q_m)=\frac{4(m-1)}{(m+1)^2(m+2)(m+3)}.
\]
For completeness, \(\mathbb EX_1^4=24/(m)_4\) and \(\mathbb EX_1^2X_2^2=4/(m)_4\), where \((m)_k=m(m+1)\cdots(m+k-1)\) is a rising factorial.

For the ordered simplex let \(Y_j=X_{(j)}\), \(Y_0=0\), and set \(Z_j=(m-j+1)(Y_j-Y_{j-1})\). Conditional on any coordinate ordering, the vector \(Z\) has the uniform \(\operatorname{Dirichlet}(1,\ldots,1)\) law: the transformation has constant Jacobian on the ordered simplex. The ordered-pair identity
\[
\sum_{i<j}|X_i-X_j|=\sum_{j=1}^m(2j-m-1)Y_j
\]
therefore gives
\[
G_m=\sum_{j=1}^m\frac{j-1}{m}Z_j.
\]
Using \(\mathbb EZ_j=1/m\), \(\operatorname{Var}(Z_j)=(m-1)/(m^2(m+1))\), and \(\operatorname{Cov}(Z_i,Z_j)=-1/(m^2(m+1))\) for distinct indices yields
\[
\mathbb EG_m=\frac{m-1}{2m},\qquad \operatorname{Var}(G_m)=\frac{m-1}{12m^2}.
\]

**Mixed moment.** By symmetry it suffices to compute \(\mathbb E[|X_1-X_2|Q_m]\). Set \(R=X_1+X_2\), \(U=X_1/R\). The splitting property of the Dirichlet law makes \(U\) uniform on \((0,1)\) and independent of \(R\) and the other normalized coordinates. In particular,
\[
\mathbb E|2U-1|=\frac12,\qquad
\mathbb E\big[|2U-1|(U^2+(1-U)^2)\big]=\frac38.
\]
Using \(\mathbb ER^3=24/(m)_3\) and \(\mathbb E[R X_j^2]=4/(m)_3\) for every \(j\ge3\), one gets
\[
\mathbb E\big[|X_1-X_2|(X_1^2+X_2^2)\big]=\frac9{(m)_3},
\quad
\mathbb E[|X_1-X_2|X_j^2]=\frac2{(m)_3}\quad(j\ge3).
\]
The same formulas apply when \(m=2\) by interpreting \(R=1\) and omitting the nonexistent remaining coordinates. Consequently
\[
\mathbb E[|X_1-X_2|Q_m]=\frac{2m+5}{m(m+1)(m+2)}.
\]
There are \(\binom m2\) identical pair contributions in \(G_m\); subtracting \(\mathbb EG_m\mathbb EQ_m\) yields
\[
\operatorname{Cov}(G_m,Q_m)=\frac{m-1}{2m(m+1)(m+2)}.
\]
Substitution of the two marginal variances proves the stated correlation, strictly decreasing in \(m\).

**Ranked-spacings statistic.** Writing \(L=\sum_{j=1}^m jY_j\) gives \(2L-(m+1)=mG_m\). Expansion of the square and \(\sum_{j=1}^m j^2=m(m+1)(2m+1)/6\) establishes the deterministic identity
\[
T_m=Q_m-\frac{G_m}{m}-\frac{(m+1)(4m-1)}{6m^3}.
\]
The displayed exact mean follows by substituting expectations. Likewise,
\[
\operatorname{Var}(T_m)=\operatorname{Var}(Q_m)+\frac{\operatorname{Var}(G_m)}{m^2}-\frac{2\operatorname{Cov}(G_m,Q_m)}m,
\]
which reduces to the claimed rational function. Its numerator is strictly positive for \(m\ge2\).

**Joint limit.** Write \(X_i=E_i/S\) with iid \(\operatorname{Exp}(1)\) variables and \(S=\sum E_i\). The standard Hoeffding decomposition for the pairwise absolute-difference U-statistic, together with the ordinary multivariate central limit theorem and delta method for normalization by \(S\), gives
\[
\sqrt m\binom{G_m-1/2}{mQ_m-2}
\xrightarrow{d}N_2\left(0,
\begin{pmatrix}1/12&1/2\\1/2&4\end{pmatrix}\right).
\]
The component influence functions, for \(E\sim\operatorname{Exp}(1)\), are
\[
a(E)=\frac{E-3}{2}+2e^{-E},\qquad b(E)=E^2-4E+2.
\]
Direct exponential integration gives \(\mathbb Ea=\mathbb Eb=0\), \(\mathbb Ea^2=1/12\), \(\mathbb Eab=1/2\), and \(\mathbb Eb^2=4\). The remainder terms vanish under the finite-moment Hoeffding theory. Because \(m^{3/2}(T_m-\mathbb ET_m)\) has first-order influence \(b-a\), its limit variance is \(4+1/12-1=37/12\). Finally \(\mathbb ET_m-5/(6m)=O(m^{-2})\), giving the displayed centering.

## Verification

The included standard-library `verify.py` implements an independent exact-rational moment calculation using the ordered-simplex Dirichlet transformation rather than the conditional two-coordinate split in the mixed-moment proof. It checks all moment formulas, the correlation identity, the ranked-discrepancy mean and variance, and its deterministic normalization for every \(m=2,\ldots,24\) (230 checks). These computations supplement the proof; they do not substitute for its arbitrary-\(m\) argument or asymptotic limit.

## Relationship to prior work

Jammalamadaka and Goria (2004), Section 3, equations (10)–(11), previously introduced this exact ranked-spacing discrepancy and expressed it as a Gini/Greenwood linear combination; neither the statistic nor that algebraic decomposition is claimed as new. On page 183 they identify the statistical dependence of Gini and Greenwood as an unresolved element in studying the discrepancy distribution. Tung and Jammalamadaka (2012), Section 2, Theorem 4, develop general asymptotic U-statistics theory for uniform spacings. Thus the applicability of asymptotic normal methods is covered in prior work, and the present limiting variance is an explicit evaluation within that general framework. The specific exact finite-\(m\) Gini–Greenwood mixed moment and consequent exact ranked-discrepancy variance were not located in those papers or targeted searches. Historical priority is not certified.

## Limitations

This establishes moments and the first-order null normal limit, not a finite-sample distribution function, exact quantiles, local power, or distributional independence. The joint limit is asymptotic rather than a uniform error bound. Other equivalent earlier calculations may exist in specialized or unindexed literature. No independent mathematical audit has been performed.

## References

1. S. Rao Jammalamadaka and M. N. Goria (2004), “A test of goodness-of-fit based on Gini's index of spacings,” *Statistics & Probability Letters* 68(2), 177–187. DOI: 10.1016/j.spl.2004.02.009. Public copy: https://jammalam.faculty.pstat.ucsb.edu/html/Some%20Publications/2004_GiniGOF_SPL.pdf
2. David D. Tung and S. Rao Jammalamadaka (2012), “U-Statistics based on spacings,” *Journal of Statistical Planning and Inference* 142, 673–684. DOI: 10.1016/j.jspi.2011.09.007. Public copy: https://jammalam.faculty.pstat.ucsb.edu/html/Some%20Publications/2012_U-StatisticsBasedOnSpacings_JSPI.pdf
