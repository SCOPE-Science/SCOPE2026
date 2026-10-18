# Independent mathematical audit

## correctness

PASS

Rebuilt the eight-compartment vector field from Ihsanjaya–Susyanto (2023), equation (2.1), at the exact stated rational parameter family. The disease-free point has R0=1067/1080<1, independent of theta. The A=0 stationary branch forces the unique DFE. For A=a>0, solving seven stationary coordinates gives S=Lambda/(2+a), Vs=Lambda/((2+a)(1+a)), E=4a, I=5a/4, H=5a/12, R=11a/[3(1+theta+5a)], VR=theta*R/(1+a). The last equation reduces bijectively to 3750a^2+(750theta-505)a+13(1+theta)=0; denominators are positive. Its discriminant is 25(22500theta^2-38100theta+2401), giving two positive roots precisely for 0<=theta<theta_c, a double positive root at theta_c=(127-4sqrt(858))/150 and none beyond. Independent SymPy reconstruction of the full 8x8 Jacobian and rational polynomial coefficients verifies the exact DFE factorization; exact rational Routh signs give unstable dimensions 0,1,0 at theta=0 for DFE, small, large equilibria respectively; direct numeric root approximation corroborates. No global basin/normal-form claim is proved.

## originality

PASS

PASS best of knowledge: an exact source-specific equilibrium fold and locally bistable subthreshold example are not implied by the prior general reinfection/backward-bifurcation phenomenon. The originating article asserts only the DFE as equilibrium (Theorem 2) and a later same-equation fractional-model full text studies fractional solution theory and numerical trajectories, not this positive-root threshold, stable endemic equilibrium, or full 8D local spectra. Literature aliases and Resultary comparisons found related models but not a theorem that implies the exact one-parameter finding.

## value

PASS

The actual 2023 source makes an incorrect uniqueness assertion, and a distinct intervention—recovered vaccination rather than susceptible vaccination—has a sharp actionable mathematical threshold invisible to R0. Exact two-endemic-equilibrium fold and simultaneous open local basins demonstrate a substantive boundary between invasion and established-endemic control. This is a motivated counterexample and complete exact intervention-family classification; parameter values are illustrative, not epidemiological estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
