# Independent mathematical audit

## correctness

PASS

For a,b>0, g(x)=e^{-ax} for x>=0 and e^{bx} for x<0; translation 1 and modulation 1/2. Its Zak transform is the absolutely convergent rational sum Z=P/(1-u/t)+Qvt/(1-vt), u=e^-a,v=e^-b,P=e^-ax,Q=e^bx. Even/odd lattice-index splitting gives S=|Z(x,w)|²+|Z(x,w+1/2)|² as a rational function of cos(4πw) with nonnegative numerator coefficients and positive denominators, strictly increasing in that cosine. At cos=-1, S-=2[αe^-2ax+βe^2bx−2γe^(b-a)x] and its derivative has sign of -aα+bβ y²−(b−a)γy, y=e^(a+b)x; one positive root lies strictly between 1 and e^(a+b), giving unique x*. At cos=1, S+ is a positive sum of three exponentials with strictly positive second derivative and equal x=0,1 endpoints by Zak quasi-periodicity, so B is attained exactly there. Explicit positive A and exact extremizing frequency classes follow. Independent 361-term Zak sums compared against closed fibers for five distinct rate pairs and were within prescribed truncation error; an initial 101-term approximation was insufficient for the slowest rate, corrected with tail extension, not a mathematical counterexample.

## originality

PASS

Foundational Zak fiber diagonalization and totally-positive exponential Gabor frames are prior. Kloos–Stoeckler 2013 Section 5 concerns even two-sided exponentials and constructs admissible frame bounds but does not state this exact two-parameter asymmetric optimum; Kloos 2014 addresses Zak zeros. Published separate result on shifted discrete sampling of asymmetric exponentials uses different operator/measurements. The exact two-rate redundancy-2 lower/upper bounds and precise Zak-fiber extremizers are the narrow qualified new statements.

## value

PASS

Optimal lower frame bound governs stability of Gabor synthesis/analysis, upper bound dynamic range, and the condition number gives quantitative reconstruction quality. Explicit sharp formulas across two unequal decay rates and all extremizing fibers solve a natural asymmetric-generator stability problem beyond existence of frames or symmetric special cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
