# Independent mathematical audit

## correctness

PASS

For a labeled vertex fixed at 0, isolation forbids other iid uniform points in an arc of length 2r; remaining n-1 points stay iid uniform in the single complementary interval L=1-2r. Any circular shortcut outside this interval traverses the removed arc of length 2r>r. Two remaining points thus have edge probability ψ=1-(1-r/L)^2 for r<L, otherwise 1. With I=sum isolation indicators and E the edge count, exchangeability gives Cov(I,E)=nL^(n-1)(binom(n-1,2)ψ-n(n-1)r). Symbolic expansion agrees with the stated low-radius quadratic Q_n and high-radius linear factor. Q_5 has discriminant -15 and Q_n increases with n on (0,1/3); n<=5 negative. Q_6=-4(3r-1)(4r-1), upper root 1/3. For n>=7, Q_n(0)=-4 and Q_n(1/3)=(n-6)/9>0, and its concave quadratic has unique relevant lower root; high branch has unique upper root (n-2)/(2n)>1/3. All assertions hold for every integer n>=2, 0<r<1/2, including n=2 and matching r=1/3. An independent symbolic SymPy identity and 2,891 rational cases verify algebra/signs but are not substitutes for the all-parameter proof.

## originality

PASS

Best-of-knowledge originality for the exact finite-n hard-circle mixed covariance and its two-transition sign theorem. The primary sources inspected treat Poisson approximation of marginal isolation/edge/component counts, soft one-dimensional connection models, or rare edge-count events. In Penrose 2018, Theorems 2.1–2.4 are asymptotic distribution statements for individual graph statistics, not the finite-n isolation–edge covariance. No inspected primary theorem or Resultary record implies the complete two-root sign law; general Palm/Mecke or U-statistic moment formulas remain a plausible source of implicit coverage.

## value

PASS

A qualitatively motivated dependence phenomenon: isolation removes the incident edges but confines remaining vertices and can raise their mutual edge count. The exact all-n covariance and sharp n=6 threshold with two explicit radius transitions determine when this effect dominates. This is an infinite-family sign classification of two canonical random-graph statistics, not a mere parameter re-labeling or arbitrary tiny-instance check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
