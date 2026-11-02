# Independent mathematical audit

## correctness

PASS

Support-function additivity yields W_n(U)=Σ_edges|U_i−U_j|, with exact coupling U=(X−Xbar 1)/R from iid standard normals and R²=Σ(X_i−Xbar)². For unnormalised S_n=Σ|X_i−X_j|, define A=S_n−μm, Q=Σ(X_i²−1), μ=2/√π. Disjoint edges are independent and incident edges have Gaussian correlation absolute 1/2. Exact bivariate absolute-normal covariance κ=1/3+(2√3−4)/π yields Var(A)=m v+2t κ (v=2−4/π); direct Gaussian decomposition of each edge gives Cov(A,Q)=μm and Var(Q)=2n. Every aA+bQ is a bounded-degree dependency-graph sum with O(n) summands, bounded moments and O(n) connected r-tuples, so cumulants of scaled order r≥3 vanish and joint Gaussian limit follows. Taylor expanding 1/R=(1/√n)(1−Q/(2n)+O_P(n^-1)) gives W−μm/√n=A/√n−μα Q/(2√n)+o_P(1), hence variance αv+2τκ−2α²/π. Degree-square Cauchy–Schwarz implies τ≥2α²−α, α≥1, and positive coefficients v−2κ and 4κ−2/π imply s²>0. Independent numeric evaluations checked path/cycle s²≈0.415643842, 3-regular≈0.634255672, 4-regular≈0.860060774; independent incidence support/Minkowski formula was separately inspected in code. No finite experiment substitutes for the joint CLT.

## originality

PASS

The published exact graphical-zonotope moment result already gives E[W] and Var(W) in terms of edge and wedge counts; those first and second moments are explicitly NOT original here. Standard dependency-graph CLTs already imply asymptotic normality for unnormalised edge-gradient Gaussian sums with bounded degrees, but the claimed centered SPHERICAL width also requires joint convergence with Gaussian radius and cross-covariance μm. The package makes that nontrivial connection and gives an explicit positive universal variance classification depending only on α,τ. Primary Padrol–Pilaud–Poullot and Pešović–Stojadinović study graphical zonotope deformation/normal-fan combinatorics rather than random-width CLT. This is a qualified best-knowledge PASS, with significant risk that general Gaussian-graph-TV delta-method literature already treats the result.

## value

PASS

An exact positive CLT variance for the geometrically canonical Haar-width statistic on every bounded-degree graph sequence with two convergent local densities gives a natural universality classification. This identifies that triangles/higher motifs do not enter the leading fluctuations, despite their appearance in higher finite moments. It is a stronger usable probabilistic asymptotic than known exact first/second moments and supplies normal-limit calibration for random zonotope widths. Though dependency-graph methods are standard, the spherical normalization and universal graph-parameter formula are mathematically motivated rather than arbitrary substitutions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
