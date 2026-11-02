# Closed-set limits and the sharp cluster criterion for Brownian second-difference conditioning

## Finding

Let \(W\) be standard Brownian motion on \([0,1]\). For each integer \(n\ge2\), choose an arbitrary deterministic set \(E_n\subseteq\{1,\ldots,n-1\}\) and let \(Q_n\) be the centered Gaussian conditional law of \(W\), given simultaneously
\[
W_{(i+1)/n}-2W_{i/n}+W_{(i-1)/n}=0,\qquad i\in E_n.
\]
Link increment indices \(i\) and \(i+1\) when \(i\in E_n\). Its connected components are consecutive blocks, with endpoints \(0=a_0<a_1<\cdots<a_m=n\) in increment coordinates. Define
\[
F_n=\{a_0/n,\ldots,a_m/n\},\qquad \delta_n=\max_{1\le j\le m}(a_j-a_{j-1})/n.
\]
For closed \(F\subset[0,1]\) containing the endpoints, \(I_Ff\) equals \(f\) on \(F\) and is affine on each connected component of \([0,1]\setminus F\).

**Theorem.** The conditional law has the exact pathwise representation
\[
Q_n=\mathcal L(I_{F_n}B+R_n),\quad
\Pr\{\|R_n\|_\infty>u\}\le 2n e^{-2nu^2}\quad(u>0),
\]
where \(B\) is standard Brownian motion and \(R_n\), independent of \(B\), consists of independent standard Brownian bridges on the \(n\) fine grid cells, each zero at its cell endpoints. Every Hausdorff limit \(F_{n_j}\to F\) yields
\[
Q_{n_j}\Rightarrow \mathcal L(I_FB)\quad\text{in }C[0,1].
\]
Every closed \(F\) containing \(0,1\) occurs for an appropriate choice of the constraints. In particular, the sharp criterion for an unchanged Wiener limit is
\[
Q_n\Rightarrow\mathcal L(B)
\quad\Longleftrightarrow\quad\delta_n\longrightarrow0.
\]
Whenever \(E_n\ne\varnothing\), \(Q_n\) and Wiener measure are mutually singular at that finite \(n\), even if the former converges weakly to the latter.

For any closed \(F\), the limit has explicit covariance
\[
K_F(s,t)=\min(s,t)-\sum_{(a,b)\in\mathcal G(F)}
\mathbf1_{\{s,t\in(a,b)\}}
\left(\min(s,t)-a-\frac{(s-a)(t-a)}{b-a}\right),
\]
where \(\mathcal G(F)\) denotes the disjoint open gaps of \(F\). At most one term is nonzero. It is the Brownian covariance with the Brownian-bridge covariance removed independently inside each gap. Extending the indicators to include endpoints gives the same result because the corresponding bridge covariance then vanishes.

## Assumptions and scope

There is no density, regularity, stationarity or nestedness hypothesis on \(E_n\). Conditioning refers to the regular Gaussian conditional law at the zero vector of the nondegenerate finite observation vector; it is not conditioning on a positive-probability event. The topology for convergence is the uniform topology on continuous functions, not total variation. The grid has equal step length \(1/n\); closed limit sets must contain \(0,1\). All random variables are real valued and the initial value is \(W_0=0\).

## Proof

**1. Projection of Gaussian increments.** Write \(D_i=W_{i/n}-W_{(i-1)/n}\), so the \(D_i\) are independent \(N(0,1/n)\) variables. Each second-difference constraint is exactly \(D_{i+1}=D_i\). The constraint subspace for the vector of increments is the orthogonal direct sum of the one-dimensional constant-vector subspaces on the connected blocks. For an isotropic Gaussian vector, its Gaussian conditional distribution given that all orthogonal contrasts vanish equals the orthogonal projection onto their common kernel. Consequently, within a block of length \(\ell\), all conditioned increments equal one shared \(N(0,1/(n\ell))\) variable; different blocks are independent. Summing a block gives an increment of variance \(\ell/n\), exactly that of an unconditioned Brownian increment over the corresponding time interval. Thus the conditioned path values at \(F_n\) have the same joint distribution as \(B\) sampled there, and all the intervening grid-node values are their affine interpolants.

**2. Fine-cell fluctuations.** Brownian motion between any two consecutive grid nodes decomposes into its straight-line interpolant plus a Brownian bridge of time length \(1/n\). The bridges on disjoint fine cells are independent of each other and of the entire grid-node vector. The constraints depend only on this vector, so the bridge residuals retain their laws and independence after conditioning. This proves \(Q_n=\mathcal L(I_{F_n}B+R_n)\). The reflection principle for a Brownian bridge of length \(h\) gives \(\Pr(\sup\mathrm{bridge}>u)=e^{-2u^2/h}\); applying it also to the negative and taking a union bound across \(n\) cells proves the displayed tail inequality. Therefore \(\|R_n\|_\infty\to0\) in probability. For the same coupling, \(\|I_{F_n}B-B\|_\infty\le\omega_B(\delta_n)\), where \(\omega_B\) is the path modulus of continuity.

**3. Deterministic closed-set continuity.** Suppose closed \(F_j\) contain the endpoints and converge to closed \(F\) in the Hausdorff metric. For every \(f\in C[0,1]\), \(\|I_{F_j}f-I_Ff\|_\infty\to0\). To prove this, suppose not and take times \(t_j\to t\) witnessing a fixed defect. If \(t_j\in F_j\) along a subsequence, then \(t\in F\) and the interpolated values tend to \(f(t)\). Otherwise let \(a_j<t_j<b_j\) be the adjacent points of \(F_j\), and extract limits \(a_j\to a\) and \(b_j\to b\), with \(a\le t\le b\), in \(F\). If \(a=b\), the affine value is a convex combination of \(f(a_j)\) and \(f(b_j)\), hence tends to \(f(t)\). If \(a<b\), no point of \(F\) can lie strictly between \(a\) and \(b\): otherwise Hausdorff convergence would force a point of \(F_j\) strictly between \(a_j\) and \(b_j\). Therefore \((a,b)\) is one gap of \(F\), and the affine interpolation converges to \(I_Ff(t)\). In all cases the defect tends to zero, contradiction. Applying this to almost every Brownian path and adding the vanishing residual \(R_n\) proves the Hausdorff-limit assertion.

**4. Completeness of the limits.** For any closed \(F\subset[0,1]\) containing \(0,1\), take \(F_n\) to be the grid points in \(\{0,1/n,\ldots,1\}\) nearest to points of \(F\), including \(0,1\). Then \(d_H(F_n,F)\le1/n\). Make \(i\in E_n\) precisely when \(i/n\notin F_n\) for \(1\le i<n\); the component endpoints are then exactly \(F_n\), proving realizability.

**5. The sharp dichotomy.** The longest complementary gap of \(F_n\) is \(\delta_n\), and \(d_H(F_n,[0,1])=\delta_n/2\). Hence \(\delta_n\to0\) implies \(F_n\to[0,1]\) and the coupling above implies convergence to Wiener measure. Conversely, if \(\delta_n\not\to0\), select a subsequence with \(\delta_n\ge\varepsilon>0\). By compactness of closed subsets of \([0,1]\) under Hausdorff distance, pass to a further subsequence converging to \(F\), and to endpoints of a longest gap converging to \(a<b\), with \(b-a\ge\varepsilon\). The interior of \((a,b)\) is disjoint from \(F\). Every sample path of \(I_FB\) is affine on this deterministic interval, whereas Brownian motion almost surely is not: its centered second difference over three equally spaced interior times is a nondegenerate Gaussian. The subsequential limit is therefore not Wiener measure, completing the necessity proof.

**6. Singular finite laws and covariance.** For each nonempty \(E_n\), at least one stipulated second difference vanishes \(Q_n\)-almost surely while it has strictly positive variance under Wiener measure; this produces mutual singularity. The covariance formula follows from the Brownian Markov-bridge decomposition: conditioned on the Brownian values on \(F\), the residual independent bridges in the gaps have covariance \(\min(s,t)-a-(s-a)(t-a)/(b-a)\) inside a common gap, and zero elsewhere. Removing these residuals gives the law of \(I_FB\).

## Verification

Run `python verify.py` using Python and SymPy. It independently computes Gaussian Schur-complement conditional covariances for every subset of second-difference constraints on small grids, compares them with the endpoint-interpolation formula at grid nodes and at cell midpoints, and checks complete-conditioning and empty-conditioning controls. The recorded output in `verify_output.txt` is `PASS: 6422 exact assertions; node Schur complements and off-grid Brownian bridge decomposition.` These are finite identity checks, not a substitute for the Hausdorff-limit proof or a complete literature search.

## Relationship to prior work

Raket (2026), Section 7, Corollary 7.4, proves that a *single* fixed-order shrinking Brownian finite-difference observation has a vanishing covariance effect. The present theorem is instead about arbitrarily many simultaneous, overlapping second differences: it isolates the longest connected constraint run as a sharp necessary-and-sufficient limit criterion and classifies every closed-set subsequential law. Raket (2021), Section 4.3, examples 4.2–4.4, supplies Gaussian conditional-covariance calculations for single endpoint increments. Wilson et al. (2021) describe general pathwise Gaussian conditioning; their framework is a relevant antecedent, but a general conditioning identity alone does not state the particular sharp run-length criterion and closed-set limit classification here. Classical Brownian bridge interpolation underlies the proof. Historical originality beyond the inspected texts is not independently certified.

## Limitations

The theorem assumes exactly zero, noiseless *second-difference* observations on a uniform deterministic grid. It does not assert analogous results for noisy constraints, higher-order differences, random grid placement or non-Brownian Gaussian processes. It classifies weak subsequential limits; it does not establish total-variation convergence (which is impossible for nonempty constraint sets) or statistical rates for estimating a limiting closed set. Gaussian projections and Brownian bridges are classical tools; historical prior work could contain a more general result implying this statement.

## References

1. Lars Lau Raket, *A Bestiary of Brownian Processes: A Field Guide to Boundary Conditions and Conditioning*, arXiv:2610.33747v1, first posted 24 October 2026, Sections 6–7. https://arxiv.org/html/2610.33747v1
2. Lars Lau Raket, *Differential equations, splines and Gaussian processes*, arXiv:2102.03306v1, first posted 24 January 2021, Section 4.3. https://arxiv.org/pdf/2102.03306
3. James T. Wilson, Viacheslav Borovitskiy, Alexander Terenin, Peter Mostowsky and Marc Peter Deisenroth, *Pathwise Conditioning of Gaussian Processes*, Journal of Machine Learning Research 22(105):1–47, 2021. https://www.jmlr.org/papers/v22/20-1260.html
