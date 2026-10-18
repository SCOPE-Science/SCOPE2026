# Independent mathematical audit

## correctness

PASS

PASS. Frozen RESULT.md blob 4c8ad2c3168df51d2d527ed39f3fbf299d690ef4 inspected. F_m(r)=p(1-r^m)/(1+r^m)-2r^N/(1-r) is strictly decreasing for 0<r<1, p in (0,2], N,m>=1; F_m(0+)=p and F_m(1-)=-infinity ensure unique sharp root. Increasing m increases F_m at each interior r, so R_{m+1}>R_m; evaluating F_m(A)=-2p A^m/(1+A^m)<0 at unique A solving p=2A^N/(1-A) bounds R_m<A<1. Monotone limit L satisfies L=A because R_m^m<=A^m->0. Mean value theorem between R_m and A and bound m*xi_m^(m-1)<=m*A^(m-1)->0 give the exact asymptotic deficit (A-R_m)/A^m -> 2A(1-A)/[N-(N-1)A]. Substitution N=1 recovers 4p/(p+2)^2. Independently bisection checked p=1,2 N=1 and p=1.2 N=3 at m=15,40; normalized ratios approach 1. Assumption that the root is the sharp radius is imported from cited prior theorem, not proven by this audit.

## originality

PASS

PASS with a narrowly bounded originality claim. Earlier sharp radii and their implicit equations are completely prior; 2025 Hamada-Honda-Kohr publisher article (all 19 pages obtained and materially read through authorized access) states high-m endpoint limit in Remarks 2.2 and 3.4 but no exact exponential correction/prefactor was identified. 2021 Kayumov-Khammatova-Ponnusamy p=1,2 cases already imply limiting radii. What remains is the precise first exponentially small defect for powered parameters p,N, not a new Bohr inequality. It follows from elementary mean-value/root perturbation and can be regarded as a simple quantitative corollary; residual risk of equivalent unstated derivative observations remains.

## value

PASS

PASS, qualified. m is the natural zero-order of the Schwarz map and R_{m,N} the sharp radius governing the analytic inequality. The deficit from its limiting powered Bohr constant answers a precise quantitative convergence question for this natural invariant; for N=1 the base p/(p+2) and exact prefactor 4p/(p+2)^2 are usable error estimates, not merely a renamed parameter or arbitrary small-instance check. The derivation is elementary and does not strengthen the original inequality; its narrowness limits scope, not by itself mathematical utility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
