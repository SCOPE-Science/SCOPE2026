# Exact maximum–Gini dependence for uniform spacings

## Finding
Let \(m\ge2\) be an integer and let \((X_1,\ldots,X_m)\) be uniformly distributed on the simplex \(\{x_i\ge0,\ \sum_i x_i=1\}\), equivalently \(\operatorname{Dirichlet}(1,\ldots,1)\). Define the largest spacing and the (ordinary, uncorrected) sample Gini coefficient by
\[
M=\max_{1\le i\le m} X_i,\qquad
G=\frac1m\sum_{1\le i<j\le m}|X_i-X_j|.
\]
Writing \(H_m=\sum_{r=1}^m r^{-1}\) and \(H_m^{(2)}=\sum_{r=1}^m r^{-2}\), the exact covariance is
\[
\boxed{\operatorname{Cov}(M,G)=\frac{(m+1)H_m-2m}{2m^2(m+1)}>0.}
\]
The corresponding Pearson correlation is
\[
\boxed{\operatorname{Corr}(M,G)=\frac{\sqrt3((m+1)H_m-2m)}{\sqrt{(m^2-1)(mH_m^{(2)}-H_m^2)}}\sim\frac{3\sqrt2}{\pi}\frac{\log m}{\sqrt m}.}
\]
The correlation equals one for \(m=2\) and is strictly between zero and one for every \(m\ge3\). In particular the two classical measures of spacing irregularity are positively correlated at every finite size but asymptotically uncorrelated.

## Assumptions and scope
The coordinates comprise all \(m\) interval spacings formed by \(m-1\) independent uniform points on \([0,1]\), including boundary spacings. They are nonnegative and sum to one almost surely. The stated Gini is the finite-population (not bias-corrected) Gini coefficient; it satisfies \(0\le G\le(m-1)/m\). Expectations, variances, and covariance are under this exact null law. No assertion concerns nonuniform data or general Dirichlet shape parameters.

## Proof
Introduce independent unit-rate exponentials \(Y_1,\ldots,Y_m\), their total \(T=\sum_iY_i\), and \(X_i=Y_i/T\). The vector of proportions is independent of \(T\sim\operatorname{Gamma}(m,1)\), whence \(\mathbb ET=m\) and \(\mathbb ET^2=m(m+1)\).

Arrange the \(Y_i\) in decreasing order \(Y_{[1]}>\cdots>Y_{[m]}>Y_{[m+1]}=0\). The exponential order-spacing theorem says that the gaps \(Y_{[r]}-Y_{[r+1]}\), for \(1\le r\le m\), are independent exponentials of rates \(r\). Thus there exist independent \(E_r\sim\operatorname{Exp}(1)\) such that these gaps equal \(E_r/r\). Set \(A=TM=Y_{[1]}\) and \(B=TG=m^{-1}\sum_{i<j}|Y_i-Y_j|\). Exactly \(r(m-r)\) pairs straddle the gap at rank \(r\); hence
\[
A=\sum_{r=1}^{m}\frac{E_r}{r},\qquad
B=\sum_{r=1}^{m-1}\left(1-\frac rm\right)E_r.
\]
Independence and unit variances give
\[
\mathbb EA=H_m,\quad \mathbb EB=\frac{m-1}{2},\quad
\operatorname{Cov}(A,B)=\sum_{r=1}^{m-1}\left(\frac1r-\frac1m\right)=H_m-1.
\]
Since \((M,G)\) is independent of \(T\), we have \(\mathbb EM=H_m/m\), \(\mathbb EG=(m-1)/(2m)\), and
\[
\mathbb E[MG]=\frac{\mathbb E[AB]}{m(m+1)}
=\frac{H_m(m-1)/2+H_m-1}{m(m+1)}.
\]
Subtracting the product of marginal means gives the boxed covariance.

Similarly, independence of the \(E_r\) yields \(\operatorname{Var}(A)=H_m^{(2)}\) and
\(\operatorname{Var}(B)=\sum_{r=1}^{m-1}(1-r/m)^2=(m-1)(2m-1)/(6m)\). Dividing second moments by \(\mathbb ET^2=m(m+1)\) and subtracting squared means gives
\[
\operatorname{Var}(M)=\frac{mH_m^{(2)}-H_m^2}{m^2(m+1)},\qquad
\operatorname{Var}(G)=\frac{m-1}{12m^2}.
\]
Their ratio with the covariance is the stated Pearson formula.

To prove positivity, let \(b_m=(m+1)H_m-2m\). Then \(b_2=1/2\) and \(b_{m+1}-b_m=H_m-1+1/(m+1)>0\) for \(m\ge2\). When \(m=2\), \(M=1/2+G\) almost surely. For \(m\ge3\), configurations with the same maximum but differing pairwise disparities occur on positive-density neighborhoods, so \(G\) is not an affine function of \(M\); strict Cauchy–Schwarz gives correlation less than one. Finally, \(H_m=\log m+\gamma+o(1)\), \(H_m^{(2)}\to\pi^2/6\), and \((\log m)^2=o(m)\) give the claimed positive asymptotic equivalent.

## Verification
The companion `verify.py` uses exact rational arithmetic to compare all five moment formulas against independently assembled exponential-gap second moments for each \(m=2,\ldots,500\). The boundary checks give \(\operatorname{Cov}(M,G)=1/48\) for \(m=2\) and \(1/54\) for \(m=3\). Independently generated normalized exponentials provide seeded Monte Carlo diagnostics for four dimensions; the complete output appears in `verification_results.txt`. The computational checks corroborate, but do not replace, the all-\(m\) proof above.

## Relationship to prior work
Jammalamadaka and Goria (2004) introduce Gini's index of uniform spacings as a goodness-of-fit statistic and obtain its marginal null distribution, explicitly identifying range-based spacing measures as a related direction. Their unnormalized double-pair statistic equals \(2mG\) in the notation here. Rao and Sobel (1980) give joint densities of ordered uniform spacings and their largest-spacing distribution. These sources provide the foundational objects and allow moments to be formulated, but the inspected formulas do not themselves state the exact maximum–Gini covariance, the finite-size strict-positivity classification, or its correlation asymptotic. The exponential-gap proof evaluates this particular joint moment in a closed harmonic form.

## Limitations
This result is for exchangeable uniform simplex spacings only. It does not establish independence, monotone conditional regression, or behavior under alternatives to uniformity. The full ordered-spacing joint laws in older literature in principle permit integration of this joint moment, so possible earlier equivalent evaluations remain a historical-priority risk. No independent external mathematical audit has been performed.

## References
1. S. Rao Jammalamadaka and M. N. Goria, *A test of goodness-of-fit based on Gini's index of spacings*, Statistics & Probability Letters **68** (2004), 177–187. DOI: `10.1016/j.spl.2004.02.009`. Open full text: `https://jammalam.faculty.pstat.ucsb.edu/html/Some%20Publications/2004_GiniGOF_SPL.pdf`.
2. J. S. Rao and M. Sobel, *Incomplete Dirichlet integrals with applications to ordered uniform spacings*, Journal of Multivariate Analysis **10** (1980), 603–610. DOI: `10.1016/0047-259X(80)90073-1`. Open full text: `https://jammalam.faculty.pstat.ucsb.edu/html/Some%20Publications/1980_SpacingsDirichlet_JMVA.pdf`.
