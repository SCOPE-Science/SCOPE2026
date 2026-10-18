# Independent mathematical audit

## correctness

PASS

For k>=2 the source threshold tau_c(k)=min_{a>0}[2+(2a^k+1)/(a+...+a^(k-1))] has a unique minimizer by its one-sign-change derivative polynomial. Reciprocal comparison puts it below 1, and comparison with a=1 plus a^-1-1 lower bound yields 0< c_k=-k log a_k<=3k/(k-1)<=6. Rescaling gives F_k(c)=k(tau(c)-2)=F(c)+G(c)/k+O(k^-2) uniformly with a derivative on the compact domain. F(c)=c(e^c+2)/(e^c-1) has unique positive nondegenerate minimizer c* solving e^c+1-2e^-c=3c. Thus c_k=c*+O(k^-1) and tau_c(k)=2+C*/k+D*/k^2+O(k^-3), with C*=F(c*) and D*=c*^2(1+2e^-c*)(1+e^-c*)/[2(1-e^-c*)^2]. Expanding 2cosh beta recovers beta_c=sqrt(C*) k^-1/2+(D*-C*^2/12)/(2sqrt(C*)) k^-3/2+O(k^-5/2). Independent 55-digit root/minimum computations recovered c*=1.035658479401893..., C*=2.745643576732724..., D*=2.986777725427654..., and k=20,100,1000 values; finite checks only supplement rigorous uniform expansion.

## originality

PASS

Henning–Külske–Le Ny–Rozikov prove existence and uniqueness of the same scalar threshold and evaluate small tree order, and Potts sources prove equivalent phase parametrization and larger phase classification, all credited prior work. None of the relevant full-text sections materially inspected states the two-term large-k asymptotic, the c* equation or explicit constants; weakly indexed Bethe-lattice equivalents remain a residual risk.

## value

PASS

The onset of mirror-symmetric three-periodic gradient Gibbs boundary laws on a natural high-degree tree family has a nontrivial inverse-temperature scale k^-1/2. Sharp first two coupling coefficients and critical rescaled minimizer quantify the existence transition for arbitrary large k, a meaningful model invariant rather than arbitrary numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
