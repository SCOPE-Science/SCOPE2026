# Independent mathematical audit

## correctness

PASS

Conditionally on N=n homogeneous Poisson events in [0,t], boundary-inclusive normalized gap vector is Dirichlet(1,...,1) with n+1 coordinates. Exact second moment gives E[Q|N=n]=2/(n+2), while E[C²|N=n]=(n+1)E[Q|n]−1=n/(n+2)=1−E[Q|n]. For N~Pois(μ), shifting E[Nf(N)]=μE[f(N+1)] gives Cov(N,Q)=−2μ E[1/((N+2)(N+3))] and Cov(N,C²)=+2μ E[1/((N+2)(N+3))]. The beta integral ∫_0^1 x(1−x)e^{μ(x−1)}dx produces 2[μ−2+(μ+2)e^{−μ}]/μ²; positivity follows 1−(1+μ)e^{−μ}>0, and expansions give μ/3 near zero and 2/μ−4/μ² at high intensity. Includes N=0 and population CV convention. Independent direct n<=10 truncated conditional Poisson moment computation at μ=1 agreed within 1e−6, as expected from tail truncation; universal identity is algebraic.

## originality

PASS

Best-of-knowledge new random-count mixed covariance for a natural Poisson-window spacing statistic. Di–Perlman examines arrival-spacing linearity and Greenwood-type measures; Mirakhmedov analyzes fixed-n Greenwood sums and goodness-of-fit asymptotics. Their accessible bibliographic material does not state a mixed Cov(N,ΣD_i²) identity or the exact opposing sign for population CV normalization. The conditional Dirichlet moment itself is standard and not claimed original; novelty concerns Poisson mixing and an all-intensity covariance reversal. Full Di–Perlman journal body inaccessible, named residual risk; this alone does not reject originality.

## value

PASS

The number of observed events is random in a homogeneous Poisson-window experiment, while spacing dispersion is often normalized by the realized mean gap. The exact strict covariance sign flip for two standard dispersion normalizations, valid at every intensity and including boundary gaps, shows the choice of normalization changes a meaningful statistical dependence interpretation. A researcher comparing counts with gap irregularity would need this precise correction, and the result is not merely a table entry, though the argument is short and uses standard Dirichlet moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
