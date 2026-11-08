# Independent mathematical audit

## correctness

PASS

Condition on k labeled cyclic roots and their permutation. The directed matrix-tree determinant det(nI_m-J_m)=k n^(m-1) counts rooted directed forests, m=n-k. For r marked nonroot terminals, removing them and attaching each to one of n-r remaining vertices gives probability (1-r/n)^(m-1), hence exact factorial moments and binomial-inversion PMF equal to m specified boxes avoided by m-1 uniform draws. The k=n boundary has Z=0. Conditional mean g_m=m(1-1/n)^(m-1) is strictly increasing m; since all k occur with positive mass, any strictly increasing h(C) has strictly negative covariance with Z. Conditioning on a fixed vertex being absent from the image gives C distributed as the cyclic count of a uniform mapping on n-1 other vertices, yielding Cov(C,Z)=n q_n^n(c_(n-1)-c_n). Standard Gaussian Riemann sums and Rayleigh scaling give the covariance and correlation constants. Independent brute force enumerated every function for n=2,3,4,5 (4+27+256+3125) and checked exact joint PMF and cyclic marginals; finite checks are not the unbounded proof.

## originality

PASS

Best-of-knowledge original contribution after comparing actual claims and implications with primary literature: Classical marginals do not imply any joint distribution. Existing asymptotic conditioning on origins does not imply the explicit finite factorial moments conditional on cyclic count. Residual risk remains that an uninspected EGF coefficient identity is an equivalent formula.

## value

PASS

The cyclic core controls long-term iteration, while terminal vertices measure one-step image depletion. Their exact finite joint null distribution and strict negative regression for every increasing transform link two natural but previously separately studied random-map statistics, supporting structural calibration and dependence analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
