# Sharp four-habitat nonmonotonicity of Moran autocorrelation under dispersal

## Finding

Let \(G\) be any finite connected simple undirected graph with \(2\le n\le4\) vertices, simple binary adjacency matrix \(A\), degree matrix \(D\), and combinatorial Laplacian \(L=D-A\). Let \(s\in\{0,1\}^{n}\) be nonconstant. For a dispersal-to-local-loss ratio \(t\ge0\), define the spatial equilibrium \(u(t)=(I+tL)^{-1}s\) of homogeneous-turnover linear source–sink dynamics. Define the classical *globally normalized, unstandardized-adjacency* Moran autocorrelation of a nonconstant field \(u\) by
\[
M_G(u)=\frac{n}{2m}\frac{(u-\bar u\mathbf1)^\mathsf{T}A(u-\bar u\mathbf1)}{\|u-\bar u\mathbf1\|_2^2},\qquad m=|E(G)|.
\]
Then \(t\mapsto M_G(u(t))\) is nondecreasing for all \(t\ge0\), **except** when \(G\) is the four-vertex path and, in path order, \(s=(0,0,1,1)\) or \(s=(1,1,0,0)\). In either exceptional case,
\[
M_G(u(t))=\frac{(2t+1)(6t+1)}{3(10t^2+6t+1)},
\]
which increases strictly up to the unique maximizer
\[
t_* = \frac{1+\sqrt5}{4},\qquad M_G(u(t_*))=\frac{\sqrt5-1}{3},
\]
and decreases strictly for all \(t>t_*\). Its initial value is \(1/3\), and its limit as \(t\to\infty\) is \(2/5\). Among all connected habitat networks and nonconstant binary source fields, **four sites are the minimum size** for such a decline of Moran autocorrelation under increasing dispersal.

For the same exceptional configuration, classical Geary autocorrelation is strictly decreasing at every dispersal level:
\[
C_G(u(t))=\frac{6t^2+4t+1}{2(10t^2+6t+1)},\qquad
\frac{dC_G}{dt}=-\frac{2t^2+4t+1}{(10t^2+6t+1)^2}<0.
\]
The Geary identity is a supporting metric comparison, not a separate novelty claim.

## Assumptions and scope

The local source strengths are binary but actual equilibrium abundances are real. A site loses density at the same positive rate \(\mu\) at every location and receives nonnegative source input \(s\); individuals disperse at equal rate \(d\) along each undirected contact edge. The equilibrium of \(\dot v=s-\mu v-dLv\) is a positive multiple of \(u(d/\mu)\). Because Moran and Geary indices are invariant under positive rescaling, \(t=d/\mu\) is the only governing ratio. Nodes are weighted uniformly, adjacency weights are symmetric binary and *not row standardized*, and the graph is connected. The theorem covers all finite ratios \(t\ge0\), not only a sampled parameter grid. The limit \(t\to\infty\) of the normalized index exists in the exceptional example although at formally infinite mixing the equilibrium becomes spatially constant and the index itself is undefined.

## Proof

**1. Equilibrium and derivative reduction.** The Laplacian is positive semidefinite, so \(Q(t)=I+tL\) is positive definite for every \(t\ge0\). Since \(L\mathbf1=0\), the average of \(u(t)\) equals that of \(s\). Writing \(k=\sum_i s_i\) and \(c=ns-k\mathbf1\), define the polynomial vector \(z(t)=\operatorname{adj}(Q(t))c\). Its nonzero scalar multiple is the centered equilibrium, because \(Q(t)^{-1}=\operatorname{adj}(Q(t))/\det Q(t)\) and \(Q(t)\mathbf1=\mathbf1\). Put \(N(t)=z(t)^\mathsf{T}Az(t)\), \(B(t)=z(t)^\mathsf{T}z(t)\). Since the source is nonconstant and \(Q(t)\) invertible, \(B(t)>0\) for \(t\ge0\). Consequently
\[
M_G(u(t))=\frac{n}{2m}\frac{N(t)}{B(t)},\qquad
\frac{dM_G}{dt}=\frac{n}{2m}\frac{N'(t)B(t)-N(t)B'(t)}{B(t)^2}.
\]
All coefficients in the derivative numerator \(W(t)=N'B-NB'\) are exact integers.

**2. Complete small-network certificate.** Every labeled simple graph with \(n\le4\) is one of the \(2^{\binom n2}\) edge masks. An explicit connectivity test retains every connected mask. For each, every nonconstant binary source is one of the \(2^n-2\) nontrivial source masks. The accompanying dependency-free script `verify_moran.py` computes the polynomial adjugate by permutation determinants with unbounded integer arithmetic, constructs \(N\), \(B\), and \(W\), and tests every coefficient. It enumerates exactly \(1,4,38\) connected labeled graphs on \(2,3,4\) vertices, yielding \(2,24,532\) graph–source pairs, respectively (\(558\) in total). In every case except \(24\) configurations, **every coefficient of \(W\) is nonnegative**, so \(W(t)\ge0\) for all \(t\ge0\), proving the required global monotonicity without numerical sampling or extrapolation. The exceptional \(24\) cases are precisely the \(12\) labeled copies of the four-path, each with the two end-block source patterns described above. Their derivative numerators change sign from positive to negative. Exhaustiveness follows from the explicit graph and source bit-mask loops, rather than an assumed catalog of isomorphism types. The script checks all of these assertions and the independent closed-form identities below.

**3. Exact exceptional trajectory.** In path order take \(s=(0,0,1,1)\). Solving \(Q(t)u=s\) and subtracting \(\bar u=1/2\) gives
\[
u(t)-\tfrac12\mathbf1=\frac{(-4t-1,-2t-1,2t+1,4t+1)}{2(2t^2+4t+1)}.
\]
Substitution into the displayed adjacency quotient yields
\[
M_G(u(t))=\frac{(2t+1)(6t+1)}{3(10t^2+6t+1)},\qquad
\frac{dM_G}{dt}=-\frac{2(4t^2-2t-1)}{3(10t^2+6t+1)^2}.
\]
The sole nonnegative root of the quadratic in the derivative is \((1+\sqrt5)/4\), giving the single strict maximum and the exact peak and endpoint limits. Replacing the source by its binary complement replaces the centered equilibrium by its negative; Moran autocorrelation is unchanged. For every connected graph, dispersal strictly reduces the centered equilibrium variance: diagonalizing \(L\) on the mean-zero subspace yields \(\|u(t)-\bar u\mathbf1\|^2=\sum_{j=2}^n |\langle s,\phi_j\rangle|^2/(1+t\lambda_j)^2\), with \(\lambda_j>0\), so its derivative is strictly negative when the source is nonconstant. Consequently, the decrease in Moran autocorrelation after \(t_*\) occurs despite genuine spatial smoothing, not because the population field becomes rougher. The displayed Geary formula follows by using \(C_G(u)=\frac{n-1}{2m}\frac{(u-\bar u\mathbf1)^\mathsf{T}L(u-\bar u\mathbf1)}{\|u-\bar u\mathbf1\|^2}\) on the same centered vector. Its derivative has a strictly negative numerator for all \(t\ge0\). This concludes the classification.

## Verification

Run `python3 verify_moran.py` with Python 3 and no third-party packages. Its output is

`VERIFY_OK graphs=1,4,38 profiles=2,24,532 exceptions=24 exactly_P4_end_blocks=1 Moran_exact_identity=1 Geary_exact_identity=1`

The program uses exhaustive labeled graph and source enumeration, integer polynomial addition/multiplication/differentiation, permutation determinants, exact identity comparisons, and coefficient-sign certificates. The 558-case check covers *all* graphs and binary sources in the claimed finite domain; it is not offered as evidence for graphs of order five or more. The exact displayed rational formulas separately prove the entire continuous parameter range in the exceptional configuration. No stochastic simulations or numerical root finding are needed.

## Relationship to prior work

Classical Moran autocorrelation goes back to Moran (1950). The biological motivation is the dispersal–autocorrelation connection in Bahn, Krohn and O'Connor (2008), which studies dispersal using a density-regulated simulation model. The fully accessible ecological spatial-autocorrelation analysis of Chen (2013) studies richness rankings and spatial autoregression with different environmental and spatial scales. These establish important conceptual context but their accessible statements do not supply this exact linear source–sink, minimum-four-site, fixed-graph binary-source classification. Bahn (2008) also reported no consistent empirical association between indirect dispersal indices and spatial autocorrelation in bird data, a different inferential target. The present result concerns a fixed graph and an explicit turnover–diffusion equilibrium, **not** a statement that dispersal universally reduces ecological clustering. A potentially closer full-text comparison with the 2008 simulation paper remains incomplete; its abstract alone cannot establish whole-paper noncoverage.

## Limitations

The mechanism is model- and normalization-specific: it assumes linear immigration–loss dynamics, identical loss rates, undirected equal-weight edges, two-valued source habitats and raw-adjacency global Moran/Geary indices. The exceptional reduction in Moran autocorrelation is modest and is an exact mathematical boundary, not an assertion of ecological effect size. The index is undefined at a perfectly uniform field (the infinite-dispersal limit), even though its limit from finite dispersal is well-defined. The theorem does not cover row-standardized weights, nonlinear density dependence, varying dispersal kernels, stochastic community formation, or graphs of more than four vertices. Previously published equivalent specialized calculations have not been ruled out completely, especially in one inaccessible source.

## References

1. Moran, P. A. P. (1950). Notes on Continuous Stochastic Phenomena. *Biometrika* 37(1–2), 17–23. DOI: 10.1093/biomet/37.1-2.17.
2. Bahn, V., Krohn, W. B., and O'Connor, R. J. (2008). Dispersal leads to spatial autocorrelation in species distributions: A simulation model. *Ecological Modelling* 213, 285–292. DOI: 10.1016/j.ecolmodel.2007.12.005.
3. Bahn, V. (2008). Failure to find the relationship between dispersal and spatial autocorrelation in species abundance. *Journal of Negative Results: Ecology & Evolutionary Biology* 5, 1–13. Author full text available from Wright State University faculty repository.
4. Chen, Y. (2013). An autoregressive model for global vertebrate richness rankings: long-distance dispersers may have stronger spatial structures. *Zoological Studies* 52, 57. DOI: 10.1186/1810-522X-52-57.
