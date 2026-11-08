# Independent mathematical audit

## correctness

PASS

The synchronous count transition on K_{a,b} is exactly a pair of independent conditional binomial kernels, with strict opposite-side majority giving all 0/all 1 and tie giving a binomial draw. At even times, each side depends on its own initial fixed state and disjoint alternating sets of tie coins; their eventual monochrome colors are independent. A tied U side restarts after two rounds with probability BD and has blue limit u*=(C+DA)/(1−BD); similarly v*=(A+BC)/(1−BD), where A,B use Bin(a,p_U) and C,D Bin(b,p_V). Since B,D<=1/2, BD<=1/4, extinction of both tie substates is a.s.; eventual class probabilities are uv,(1−u)(1−v),u(1−v)+(1−u)v. Union-geometric bound yields E[T]<=22/3; binomial CLT at p=1/2+lambda/sqrt(N) proves the claimed critical normal profile, provided both side sizes are even, initially tied, and a/N has interior limit. Independently solved an 11-transient-state small exact absorbing chain; no extrapolation from its finite size.

## originality

PASS

PASS with qualification. Zehmakan already studies random majority with fair tie coins, even cycles and blinking 2-cycles, including special product probabilities under random initial coloring. That special model is credited; it does not state the deterministic-initial unequal-community-bias biclique hitting law or its finite uniform time and critical window. Distinct asynchronous globally biased majority process also fails to dominate this transition law.

## value

PASS

Exact classification of recurrent polarization versus consensus and a size-independent absorption-time bound for synchronous social dynamics on biclique communities, plus an asymptotic critical-bias window, is a natural and nontrivial dynamical question rather than a routine single-step Markov matrix calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
