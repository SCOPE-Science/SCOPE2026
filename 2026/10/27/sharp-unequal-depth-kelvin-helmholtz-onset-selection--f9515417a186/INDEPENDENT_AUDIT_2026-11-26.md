# Independent mathematical audit

## correctness

PASS

The rigid-lid Laplace modes are cosh profiles; the interface kinematic and pressure conditions lead to the temporal quadratic with coefficients alpha_i=rho_i coth(k h_i). Its weighted-square minimum in frequency is k^2 alpha_l alpha_u U^2/(alpha_l+alpha_u), so a nonreal pair occurs exactly above the stated scalar threshold. The Dirichlet–Neumann partial-fraction expansion of tanh(h sqrt(z))/sqrt(z) has residues 2/h at poles -pi^2(n+1/2)^2/h^2; the series and its derivatives converge on compact nonnegative z intervals. For S=sum c/(z+a), B=-S/S'-z is a mean under weights c/(z+a)^2, and differentiation gives -2 Cov(a,1/(z+a))>0, since there are distinct poles and the second function strictly decreases. B(0)=3M1/M3 and B(z)~z at infinity. The derivative of (b+z)S has the sign of B-b, proving strictness at b=b_c and unique positive minimization only above it. The tanh expansion gives B'(0)=12 M1 M5/(5 M3^2)-2>=2/5 (strict for unequal depths), and local inversion and integration of the derivative give k_*^2=epsilon/C+O(epsilon^2) and the gap (M3/6C)epsilon^2+O(epsilon^3). At exact onset the finite root is repeated real on the finite branch only; it is not an exponentially growing mode. For the separate phase-speed boundary, the denominator T(z)=sum rho_i sqrt(z)coth(h_i sqrt(z)) has the expansion T(0)+sum d_j z/(z+a_j), d_j,a_j>0, from the coth poles. Thus T''<0 and the derivative sign of (b+z)/T is the sign of T-(b+z)T', strictly increasing and eventually positive. This supplies a global check beyond the frozen small-k expansion: its boundary is T(0)/T'(0), equivalent to the stated gamma_phase. Exact signed tension comparisons at two unequal-depth contrasts and at the matching ratio passed (python3 /workspace/repro/frozen_checks.py). The analysis only establishes temporal linear onset, not above-onset fastest growth.

## originality

PASS

The physical dispersion and all-mode variational threshold are substantially prior and not credited as new. The distinct supported result is a global root-count theorem for the unequal-depth kernel, with the weighted-moment transition and explicit edge law, plus separation from the distinct zero-shear phase-speed criterion. Closest inspected sources do not give these conclusions; an inaccessible cited specialist treatment is a residual risk, not a negative comparison.

## value

PASS

Without wavenumber search the weighted-depth criterion distinguishes long-wave onset from the first isolated finite wavelength, and uniqueness eliminates competing first-onset modes. The explicit near-transition wavelength and critical-shear gap quantify how this change happens. Demonstrating that phase-speed selection can err in either direction when substituted for KH onset is a concrete consequence in the natural unequal-depth model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
