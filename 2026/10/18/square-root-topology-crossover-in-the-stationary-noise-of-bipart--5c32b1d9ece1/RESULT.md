# Square-root topology crossover in the stationary noise of bipartite spin copying

## Finding
Let \(K_{m,n}\) have side sizes \(m,n\ge1\). Each site carries \(\sigma_v\in\{-1,+1\}\) and flips its spin spontaneously at rate \(\eta>0\). Compare two independent-copying rules: **vertex clock** (every vertex, at rate one, copies a uniformly selected neighbor) and **directed-edge clock** (every directed edge, at rate one, makes its receiving vertex copy its sending vertex). All clocks are independent. Let \(M=(m+n)^{-1}\sum_v\sigma_v\) and let \(V_{\rm V},V_{\rm E}\) be the unique stationary variances of \(M\) under the two rules.

For fixed \(\eta>0\) and every integer sequence \(n\to\infty\), \(m=m(n)\ge1\) with \(m/\sqrt n\to c\in(0,\infty)\),
\[
\boxed{\sqrt n\,V_{\rm V}\to\frac{1}{8\eta(1+\eta)c},\qquad
\sqrt n\,V_{\rm E}\to\frac{c}{\eta},\qquad
\frac{V_{\rm E}}{V_{\rm V}}\to8(1+\eta)c^2.}
\]
Consequently the leading stationary-fluctuation ordering changes at the sharp aspect-ratio scale \(m\sim c_*\sqrt n\) with \(c_*=[8(1+\eta)]^{-1/2}\): for every fixed \(0<c<c_*\), edge clocks eventually give smaller variance, whereas for \(c>c_*\), vertex clocks eventually give smaller variance. **Nothing here asserts exact finite-size equality or a higher-order ordering at \(c=c_*\).**

Both variances also have exact all-size rational formulas. Put \(N=m+n\),
\[
U=\frac{m^{-1}+n^{-1}}{m^{-1}+n^{-1}+8\eta(1+\eta)},\qquad
Z=\frac{(m+2\eta)(n+2\eta)}{8\eta^3+6\eta^2N+\eta N^2+\eta N+mn}.
\]
Then
\[
\boxed{V_{\rm V}=\frac{N+[N(N-1)+4\eta mn]U}{N^2},}
\]
\[
\boxed{V_{\rm E}=\frac{N+\left[\frac{m(m-1)n}{n+2\eta}+\frac{n(n-1)m}{m+2\eta}+2mn\right]Z}{N^2}.}
\]
As complementary boundaries, for fixed \(m\) as \(n\to\infty\), \(V_{\rm V}\to[1+8m\eta(1+\eta)]^{-1}\) whereas \(V_{\rm E}\to0\); if \(m/n\to\rho\in(0,\infty)\), then \(V_{\rm V}\to0\) whereas \(V_{\rm E}\to[1+\eta(2+\rho+\rho^{-1})]^{-1}\).

## Assumptions and scope
Every node is an independent two-state spin. A noise event **flips** the current spin at rate \(\eta\) (not an event resampling a fair independent spin at rate \(\eta\)). Under vertex clocks, each vertex initiates copying at total rate one; under directed-edge clocks, each **ordered adjacent pair** initiates copying at rate one, so a vertex's total copying rate equals its degree. In particular the total copying rates differ between protocols on irregular graphs. This is an intended comparison between per-vertex and per-interaction kinetics, not a comparison at fixed global attempt rate. Copying an equal spin leaves the configuration unchanged. There is no noise scaling with system size. The source graph is the complete bipartite simple graph and \(m,n\) are positive integers. Both dynamics are finite irreducible continuous-time chains because \(\eta>0\), and spin-reversal symmetry forces stationary mean magnetization zero.

## Proof
Let \(A\) denote the size-\(m\) side and \(B\) the size-\(n\) side. Write \(\lambda_A,\lambda_B\) for the total copying rates of a vertex in each side: \((1,1)\) for vertex clocks and \((n,m)\) for directed-edge clocks. Define the correlations between two distinct \(A\)-sites, two distinct \(B\)-sites, and an \(A\)-\(B\) pair as \(x,y,z\), respectively. For a singleton side, its within-side correlation is only a formal auxiliary and never enters the variance because its combinatorial coefficient vanishes.

Apply the generator to \(\sigma_i\sigma_j\). A noise flip at either endpoint negates that product, contributing \(-4\eta\) times its expectation. When a copying event is initiated at either endpoint, replace that spin with the sampled neighbor's spin. On two sites of the same side the sampled neighbor lies across the bipartition. Stationarity therefore gives
\[
0=-4\eta x+2\lambda_A(z-x),\qquad
0=-4\eta y+2\lambda_B(z-y),
\]
whence \(x=\lambda_A z/(\lambda_A+2\eta)\) and \(y=\lambda_B z/(\lambda_B+2\eta)\). For an across-side pair, the sampled neighbor coincides with the other endpoint with probabilities \(1/n\) and \(1/m\), and the product then equals one. Thus
\[
0=-4\eta z+\lambda_A\left(\frac1n+\frac{n-1}{n}y-z\right)
+\lambda_B\left(\frac1m+\frac{m-1}{m}x-z\right).
\]
Substituting the first two identities yields the exact unique solution
\[
z=\frac{\lambda_A/n+\lambda_B/m}{\lambda_A+\lambda_B+4\eta-
\frac{\lambda_A(n-1)\lambda_B}{n(\lambda_B+2\eta)}-
\frac{\lambda_B(m-1)\lambda_A}{m(\lambda_A+2\eta)}}.
\]
The denominator is strictly positive: by the bounds \(\lambda_j/(\lambda_j+2\eta)<1\), the two subtracted terms are individually strictly smaller than \(\lambda_A\) and \(\lambda_B\). With \(\mathbb E M=0\), expand \(M^2\), obtaining
\[
V=\frac{N+m(m-1)x+n(n-1)y+2mnz}{N^2}.
\]
For vertex clocks, the two within-side correlations coincide at \(U\), and \(z=(1+2\eta)U\), yielding the displayed \(V_{\rm V}\). For directed-edge clocks, substitution gives \(z=Z\), \(x=nZ/(n+2\eta)\), \(y=mZ/(m+2\eta)\), hence \(V_{\rm E}\). No probabilistic independence of different spins is assumed.

For \(m/\sqrt n\to c\in(0,\infty)\), \(m\to\infty\) and \(m/n\to0\). In the vertex expression, \(U\sim[8\eta(1+\eta)m]^{-1}\), and the coefficient of \(U\) in \(V_{\rm V}\) tends to one, while the diagonal \(1/N\) term is negligible at scale \(n^{-1/2}\). Thus \(\sqrt n V_{\rm V}\to[8\eta(1+\eta)c]^{-1}\). In the edge expression, the numerator of \(Z\) is asymptotic to \(mn\), its denominator to \(\eta n^2\), so \(Z\sim m/(\eta n)\). Both within-side factors \(n/(n+2\eta)\) and \(m/(m+2\eta)\) tend to one; the diagonal term is again negligible. Thus \(\sqrt n V_{\rm E}\to c/\eta\). Their positive ratio converges to \(8(1+\eta)c^2\), whose unique crossing of one is \(c_*\). The fixed-\(m\) and balanced-partition limits follow by direct leading-term comparison in the exact formulas.

## Verification
Execute `python verify_bipartite.py` with Python 3 and no third-party dependencies. The program independently builds the exact lumped Markov generator on the count states \((i,j)\) of positive spins in each part, solves its full rational stationary linear system, and compares its magnetization variance and available pair correlations against the formulas. It checks 54 combinations of graph sizes, noise levels and clocks by exact rational arithmetic. Sample large-graph computations test asymptotic convergence but are not used as an infinite-size proof. The analytic generator identities and limits above establish the theorem for arbitrary admissible \(m,n,\eta\).

## Relationship to prior work
The original heterogeneous-network voter-process literature distinguishes node, link and invasion update rules and discusses the complete bipartite graph, principally without independent spin-flip noise [1]. The noisy voter model and its ergodicity on graphs are established in [2]. The general exact moment equations for the node-update noisy voter model were developed in [4]; the authors use an annealed network approximation to obtain a tractable degree-dependent variance and do not give this bipartite two-clock comparison. Exact spectral solutions [3] and bipartite quasi-stationary results [6] concern the unperturbed voter model with absorbing consensus rather than the strictly positive-noise equilibrium. Pair-approximation techniques [5] and general noisy-voter stationary-limit results [7] are broader context, without these evaluated cross-protocol formulae and the sharp \(\sqrt n\) aspect-ratio threshold in the inspected texts. This claim is a specific new calculation and classification using well-established moment methods; it does not claim those methods as new. A logically equivalent prior formulation could exist in another source.

## Limitations
The result compares processes with genuinely different total copying activity per vertex: an edge-clock vertex has degree-proportional activity while a vertex-clock vertex has unit activity. The crossover is a stationary second-moment result, not a claim about full stationary distributions, dynamic mixing, consensus without noise, finite-size exact crossing, or a thermodynamic phase transition. The only universal ordering statement is away from the asymptotic threshold at fixed positive noise. The originality comparison is limited to the specifically inspected literature, not an exhaustive theorem search.

## References
[1] V. Sood, T. Antal, S. Redner, *Voter Models on Heterogeneous Networks*, arXiv:0712.4288 (first arXiv version 2007-12-27), https://arxiv.org/abs/0712.4288.

[2] A. Ramadas, *Mixing of the Noisy Voter Model*, arXiv:1403.1991 (2014), https://arxiv.org/abs/1403.1991.

[3] W. Pickering, C. Lim, *Solution of the Voter Model by Spectral Analysis*, arXiv:1408.2130 (2014), https://arxiv.org/abs/1408.2130.

[4] A. Carro, R. Toral, M. San Miguel, *The noisy voter model on complex networks*, arXiv:1602.06935 (2016), https://arxiv.org/abs/1602.06935.

[5] A. F. Peralta et al., *Stochastic pair approximation treatment of the noisy voter model*, arXiv:1807.04615 (2018), https://arxiv.org/abs/1807.04615.

[6] I. Ben-Ari, H. Panzo, P. Speegle, R. O. VandenBerg, *Quasi-Stationary Distributions for the Voter Model on Complete Bipartite Graphs*, arXiv:2004.10187 (2020), https://arxiv.org/abs/2004.10187.

[7] R. Pymar, N. Rivera, *Asymptotic behaviour of the noisy voter model density process*, arXiv:2112.01478 (2021), https://arxiv.org/abs/2112.01478.
