# Independent mathematical audit

## correctness

PASS

The assigned affine branches have lengths 1/2, 2^-17, 2^-17, 2^-5761, whose sum is <1, so disjoint branches exist and all slopes exceed 1. For full-shift pressure P(t)=-b t+log(1+2e^-ct+e^-360ct), b=log 2, c=16log 2, the normalized log slopes are d=(0,1,360) with beta=1/16. Reconstructed alpha=-P'(t)=c(beta+mu), P''(t)=c^2 V>0 and spectrum L(alpha(t))=t+P(t)/alpha(t). Independent differentiation in alpha gives L''=(2PP''-alpha^2)/(alpha^3P''), so its sign is the analytic G(w)=2(beta w+logZ)V-(beta+mu)^2. Executed the package's 75-digit mpmath interval checker, then an independent 100-digit high-precision implementation plus strict interval-endpoint sign comparisons. The sign sequence at five increasing rational w is (-,+,-,+,-), yielding >=4 distinct sign-changing roots via continuity and analyticity, with alpha strictly monotone. Ma 2020 Theorems 2.2,4.2 supply the lower bounds n>=4 and r_T>=3. At least four, not exactly four, is established.

## originality

PASS

Best-of-knowledge originality for the simultaneous optimal pair (four physical branches, three distinct slopes), not novelty of pressure formalism or separate minimum bounds. Full relevant Ma 2020 primary article and JPV 2021 primary article were compared by actual implication: Ma supplies n=4 with four distinct slopes and r_T>=3 separately; JPV supplies r_T=3 with seven branches. None inspected supplies their intersection (4,3), while this explicit multiplicity (1,2,1) pressure witness does. The Resultary/web searches did not find a prior matching or dominating statement, without proving global novelty.

## value

PASS

Two natural complexities of affine cookie-cutter Lyapunov spectra are physical branch count n and number of distinct expansion factors r_T. Prior results separately attain the sharp four-branch threshold and three-slope threshold, but do not show attainability together; a concrete 4/3 witness settles their joint feasibility, with only one duplicated middle slope. This is a motivated extremal structural construction that distinguishes physical multiplicity from essential slope count; not a routine renaming, computational curiosity, or parameter substitution of the earlier four-distinct-slope witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
