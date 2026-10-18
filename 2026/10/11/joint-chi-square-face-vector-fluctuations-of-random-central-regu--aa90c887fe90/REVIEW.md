# Independent mathematical audit

## correctness

PASS

Exact noncentral-free geometry: for generic centered hyperplane a with sum a_i=0, each j-face (0<=j<=N-3) corresponds uniquely to a crossed ambient simplex (j+1)-face supported on j+2 coordinates, hence f_j=binom(N,j+2)-binom(K,j+2)-binom(N-K,j+2). Discrete convexity makes balanced sign splits maximize f_j. Haar normals equal centered iid Gaussian directions, with K=#(X_i>bar X). Threshold empirical-process expansion gives T_N=(K-N/2)/sqrt(N)=>Normal(0,s²), s²=1/4-1/(2pi); the stated grid/Bernstein control handles the random threshold. For fixed j, quadratic Taylor coefficient of binomial deficit at k=N/2 is N^j/(2^j j!)+lower order; higher terms vanish after dividing by N^(j+1), yielding jointly (s²/(2^j j!)) Z². DKW and Gaussian bar-X tails bound all moments, yielding covariance constant 2s^4/(2^(j+k)j!k!) and correlation 1 for fixed j,k. Pair Gaussian sign probability supplies exact arcsine vertex mean and the deviation bound. Independently checked polynomial quadratic coefficients j=0..4 symbolically and combinatorial Euler identities for all split sizes N=4..10, plus seeded Gaussian mean/variance for N=32,128,512; none substitutes for CLT. No growth-rank claim.

## originality

PASS

PASS best-of-knowledge: The separately published exact vertex mean/one-dimensional chi-square result (Resultary d3f9..., published at 13:10:15Z) gives only j=0 and appeared after this joint record (13:07:08Z). The present exact ALL-rank face-vector law and rank-one joint chi-square moment/covariance classification are a genuine extension even if a vertex law is known. Kabluchko–Thäle 2017 full paper, specifically Theorem1.1 and Sections 3–4, treats EXPECTED face counts of random PROJECTIONS, a different model, not random central SECTIONS or their full fluctuations. Dirksen concerns central simplex section volumes; Affentranger–Schneider concerns projections, not this high-rank sectional joint limit. No earlier stronger exact section law found; full-text access to some projection-era sources limited.

## value

PASS

PASS: The entire random central simplex section face vector lies on an exact one-integer curve, and all fixed ranks share a single non-Gaussian chi-square fluctuation factor with sharp covariance constants. This is a nontrivial, motivated probabilistic-convex-geometric classification of a canonical random polytope, useful beyond the isolated vertex mean or volume expectation. The joint result does not reduce to a table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
