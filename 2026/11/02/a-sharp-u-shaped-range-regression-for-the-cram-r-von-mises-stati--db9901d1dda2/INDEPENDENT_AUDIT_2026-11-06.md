# Independent mathematical audit

## correctness

PASS

For iid uniform[0,1] sample of n>=2, W=n∫(F_n-t)^2 dt = n/3+Σ U_i^2-(1/n)Σ_{i,j}max(U_i,U_j), with normalized classical one-sample CvM. Conditional on extrema (A=a,B=a+r), n-2 unordered interiors are iid uniform(a,a+r); direct pair-category counting gives E[W|A=a,R=r]=n[a²+a(r-1)+(1-r)²/3]+r²/3-r/6. A|R=r is uniform(0,1-r), giving E[W|R=r]=[n(1-r)²+2r²-r]/6. Second derivative (n+2)/3>0 and derivative zero at (2n+1)/[2(n+2)], interior crossing r=(n-1)/(n+2). R~Beta(n-1,2), and independent Sympy moment algebra reconfirmed EW=1/6 and Cov(R,W)=-(n-1)/[(n+1)(n+2)(n+3)]. The variance decomposition from centered empirical bridges yields Var W=(4n-3)/(180n), Var R=2(n-1)/[(n+1)^2(n+2)], hence exact Pearson correlation and -sqrt(45/2)/n rate. The source exact Dirichlet moment checker n=2..7 is corroborative.

## originality

PASS

The normalized classical CvM statistic, marginal distribution, order-statistic representation, and uniform range beta law are prior art. The conditional mean as an explicitly U-shaped quadratic jointly with its exact negative mixed covariance and Pearson correlation was not shown in the inspected marginal-distribution and fitted-parameter testing papers. Historical order-statistics literature may already contain an equivalent conditional moment.

## value

PASS

Range and CvM measure complementary extremes of spread and goodness-of-fit. A strictly U-shaped conditional expectation coexisting with negative covariance is an interpretable finite-sample dependence phenomenon; its exact turning point, sign crossing and vanishing correlation have statistical relevance without requiring a new test or general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
