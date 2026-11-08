# Independent mathematical audit

## correctness

PASS

In Yule–Harding–Kingman leaf-splitting distribution with n>=2 leaves, cherry count C and total cophenetic index Phi satisfy C=C_k+C_(n-k) for n>=3 and Phi=Phi_k+Phi_(n-k)+binom(k,2)+binom(n-k,2) under uniform root size k=1,...,n−1 and conditionally independent daughters. Means c_1=0,c_2=1,c_n=n/3 (n>=3), and p_n=n(n−1)−2n(H_n−1). Law of total covariance yields K_n=(2/(n−1))sum_{k<n}K_k+Cov_k(c_k+c_(n-k), p_k+p_(n-k)+binom(k,2)+binom(n−k,2)). Only k=1,2,n−2,n−1 cause the nonconstant cherry correction, so forcing is 2[2H_(n−2)−3n+7]/[3(n−1)], and the harmonic terms cancel in the induction, giving K_n=−(n−3)(5n−8)/(9(n−1)), K_2=0. With established VarC~2n/45, VarPhi~n⁴/12, n^(3/2)Corr→−5sqrt(30)/3. Independently recalculated the split mixed-moment recurrence exactly through n=100; finite check supplements induction.

## originality

PASS

Cardona–Mir–Rosselló 2012 calculates cophenetic moments and Sackin–cophenetic covariance; Wu–Choi 2015 examines cherry–pitchfork joint counts. Neither produces the cherry–cophenetic cross-moment directly. The cherry count and nonlocal pair-LCA index are not determined by one another or by Sackin. The exact covariance and n^(-3/2) decorrelation are assessed as new relative to inspected literature.

## value

PASS

A natural cross-statistic of tree balance and pair ancestry is exactly evaluated for every n, including sign and unusually rapid correlation decay. It gives a reusable joint-moment benchmark rather than merely another marginal variance or arbitrary small-n numerical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
