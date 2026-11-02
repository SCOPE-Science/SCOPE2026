# Sharp resolvent thresholds for stable polarization patterns on weighted opinion networks

## Finding

Consider the clipped-sign opinion dynamics of AlMahmoud and Mallmann-Trenn on any finite, connected, undirected, positively weighted graph. In the strong-central-slope regime specified below, **all** asymptotically stable equilibria are precisely those arising from sign vectors that satisfy an explicit linear-resolvent inequality. For fixed positive clipping radius, the transition to all \(2^n\) locally attracting polarization patterns is determined by the least diagonal entry of the graph resolvent. An isolated dissenter is stable exactly when its *individual* diagonal entry passes the same threshold. On star networks, an isolated dissenting leaf may be stable although an isolated dissenting hub is not.

Put
\[
H_b=b(L+bI)^{-1},\qquad \tau_\varepsilon=\frac{1+\varepsilon}{2},
\]
where \(L\) is the symmetric weighted graph Laplacian. Then the exact count of asymptotically stable equilibria is
\[
\mathcal N(G,b,\varepsilon)
=\sum_{s\in\{-1,1\}^{V}}
\prod_{i\in V}{\bf1}\{s_i(H_bs)_i>\varepsilon\}.
\]
For each vertex \(i\), the equilibrium associated with just that vertex having negative sign is attracting if and only if
\[
(H_b)_{ii}>\tau_\varepsilon.
\]
Moreover,
\[
\boxed{\mathcal N(G,b,\varepsilon)=2^{|V|}\quad\Longleftrightarrow\quad
\min_{i\in V}(H_b)_{ii}>\tau_\varepsilon.}
\]
The equivalence includes the necessity, not just a sufficient high-influence estimate.

## Assumptions and scope

Let \(G=(V,E,w)\) be connected with \(n=|V|\ge 2\), positive undirected weights \(w_{ij}=w_{ji}\), and weighted degrees \(d_i=\sum_jw_{ij}\). Fix \(b>0\) and a clipping radius satisfying
\[
0<\varepsilon<\frac{b}{b+d_{\max}},\qquad d_{\max}=\max_i d_i.
\]
Define \(f_\varepsilon(z)=-1\) when \(z<-\varepsilon\), \(f_\varepsilon(z)=z/\varepsilon\) when \(-\varepsilon\le z\le\varepsilon\), and \(f_\varepsilon(z)=1\) when \(z>\varepsilon\). On the invariant cube \([-1,1]^V\), consider
\[
\dot x_i=\sum_jw_{ij}(x_j-x_i)+b\bigl(f_\varepsilon(x_i)-x_i\bigr).
\]
An asymptotically stable equilibrium refers to the actual continuous-time dynamics, not merely formal consistency of a sign pattern. No assertion is made about all unstable equilibria or basins of attraction. Each weight is finite and strictly positive on an edge; no regularity, transitivity, or large-graph limit is assumed.

## Proof

**1. Resolvent positivity and conservation.** The matrix \(L+bI\) is symmetric positive definite, with nonpositive off-diagonal entries and strictly positive inverse entries for a connected graph. Its inverse is nonnegative, for example by writing
\[
(L+bI)^{-1}=\int_0^\infty e^{-bt}e^{-Lt}\,dt.
\]
Since \(L\mathbf 1=0\), the symmetric matrix \(H_b=b(L+bI)^{-1}\) is strictly positive and row stochastic: \(H_b\mathbf1=\mathbf1\). It is also invertible.

**2. Every attracting equilibrium lies strictly in a plateau.** Let \(F_\varepsilon\) be the antiderivative of \(f_\varepsilon\) with \(F_\varepsilon(0)=0\); explicitly it equals \(z^2/(2\varepsilon)\) for \(|z|\le\varepsilon\), and \(|z|-\varepsilon/2\) otherwise. Define the continuously differentiable energy
\[
\mathcal E(x)=\frac12x^\top Lx+\frac b2\sum_i x_i^2-b\sum_i F_\varepsilon(x_i).
\]
The flow is exactly \(\dot x=-\nabla\mathcal E(x)\), hence \(d\mathcal E/dt=-\|\dot x\|^2\le0\). An asymptotically stable equilibrium must be a local minimum of \(\mathcal E\): a nearby state with strictly smaller energy cannot converge to the equilibrium, by continuity and energy monotonicity. If an equilibrium had \(|x_i|<\varepsilon\), varying only coordinate \(i\) gives second derivative
\[
\frac{\partial^2\mathcal E}{\partial x_i^2}=d_i+b-\frac b\varepsilon<0.
\]
For \(|x_i|=\varepsilon\), the same strictly negative curvature holds for a one-sided displacement *into* the central interval; the equilibrium has zero first derivative, so its energy decreases under such a small displacement. Both contradict local minimality. Thus every attracting equilibrium has \(|x_i|>\varepsilon\) for all \(i\).

**3. Every consistent sign vector gives an exponential sink.** In a strict plateau, set \(s_i=\operatorname{sgn}(x_i)\). Stationarity is \((L+bI)x=bs\), hence \(x=H_bs\), and consistency is precisely \(s_i(H_bs)_i>\varepsilon\) for each \(i\). Conversely, any such \(s\) yields a genuine equilibrium. In its open plateau neighborhood the Jacobian is \(-L-bI\), which is strictly negative definite. Therefore the equilibrium is locally exponentially attracting. Invertibility of \(H_b\) makes the corresponding equilibria distinct. This proves the exact census.

**4. Sharp one-dissenter test and all-pattern criterion.** For \(s=\mathbf1-2e_i\),
\[
H_bs=\mathbf1-2H_be_i.
\]
At the dissenting vertex consistency means \(1-2(H_b)_{ii}<-\varepsilon\), or \((H_b)_{ii}>\tau_\varepsilon\). At every other vertex \(j\), symmetry and row stochasticity imply \((H_b)_{ji}\le1-(H_b)_{ii}\); thus the same strict inequality ensures \(1-2(H_b)_{ji}>\varepsilon\). Necessity is immediate at \(i\). For arbitrary \(s\), positivity and stochasticity give
\[
s_i(H_bs)_i=(H_b)_{ii}+\sum_{j\ne i}(H_b)_{ij}s_is_j
\ge2(H_b)_{ii}-1.
\]
Consequently, the diagonal test suffices for every sign vector; if it fails at any vertex, that vertex's lone-dissenter sign pattern fails, proving necessity.

**5. A unique spectral threshold.** With an orthonormal Laplacian eigenbasis \((u_k)\), where \(0=\lambda_1<\lambda_2\le\cdots\) and \(u_1=\mathbf1/\sqrt n\),
\[
(H_b)_{ii}=\frac1n+\sum_{k=2}^n\frac b{b+\lambda_k}u_k(i)^2.
\]
This quantity is continuous and strictly increasing in \(b>0\), with endpoint limits \(1/n\) and \(1\). For fixed \(\varepsilon\in(0,1)\), there is a unique \(b_i(\varepsilon)>0\) solving \((H_b)_{ii}=\tau_\varepsilon\). On the admissible parameter range of this theorem, all \(2^n\) patterns are stable if and only if \(b>\max_i b_i(\varepsilon)\). The clipping restriction must still be checked separately when varying \(b\).

**6. Complete bipartite specialization.** For \(K_{p,q}\) with every edge of weight \(w>0\), write \(n=p+q\). Every vertex on the size-\(p\) side has diagonal resolvent entry
\[
h_A=\frac{b^2+bwn+qw^2}{(b+qw)(b+nw)},
\]
while on the size-\(q\) side the entry is
\[
h_B=\frac{b^2+bwn+pw^2}{(b+pw)(b+nw)}.
\]
Indeed the nonsymmetric quotient equilibrium equations for side averages \(U,V\), with average signs \(S,T\), give
\[
U=\frac{(b+pw)S+qwT}{b+nw},\qquad
V=\frac{pwS+(b+qw)T}{b+nw}.
\]
Individual equilibrium opinions equal \((qwV+bs_i)/(b+qw)\) on the first side and \((pwU+bs_j)/(b+pw)\) on the second. Thus summing \(\binom pk\binom q\ell\) over integer pairs \((k,\ell)\) whose four present sign classes satisfy their strict consistency inequalities gives an exact binomial-sum census of all attracting equilibria. This computation uses no mean-field or dense-graph approximation.

For a star \(K_{1,5}\) with \(w=1\), \(b=2\) and \(\varepsilon=1/10\), the hub has \(h_A=3/8\), while each leaf has \(h_B=17/24\); the common cutoff is \(11/20\). A single negative hub therefore fails the criterion, while a single negative leaf yields the attracting equilibrium
\[
\left(\frac34,-\frac5{12},\frac{11}{12},\frac{11}{12},\frac{11}{12},\frac{11}{12}\right).
\]
The hub-only negative sign vector instead solves the plateau equations to \((1/4,3/4,\ldots,3/4)\), which is sign-inconsistent and hence not an equilibrium of the clipped dynamics.

## Verification

The standalone exact-arithmetic checker `verification/check.py` solves rational resolvent systems on paths, cycles, stars, complete graphs and complete bipartite graphs. It compares the sign-vector census to the sharp diagonal criterion, verifies the bipartite binomial-sum formula, and checks the explicit star asymmetry. Running `python verification/check.py` passed 117 exact graph/parameter instances. It verifies finite instances and arithmetic only; the proof of all finite sizes and weighted graphs is the analytical argument above.

## Relationship to prior work

AlMahmoud and Mallmann-Trenn (2024) introduced the clipped platform-influence model in this form and characterize equilibria principally for two agents and complete networks (notably their Theorem 7), with a separate asymptotic two-block stochastic model. The new statement is a finite-graph exact **attracting-state** census, a sharp all-sign threshold, and a location-sensitive isolated-dissenter classification on arbitrary connected symmetric weighted graphs. Its complete-graph cases are consistent with, and are not offered as replacements for, their known exact complete-graph results.

Candogan et al. (2022) previously introduced social learning under platform influence, including sign-like nonlinear feedback; their accessible abstract describes consensus and disagreement and block-model analysis. Its complete full text was not independently available for a definitive equivalence assessment. Duncan et al. (2021) supply broader qualitative theory for steep sigmoids on regulatory networks, but their edge-feedback switching framework does not itself state the diagonal resolvent criterion for this self-feedback opinion model. Fixed-exogenous-signal Friedkin–Johnsen resolvents are mathematically related but do not alone classify stability under endogenous sign feedback. Equivalent prior work may remain unindexed or uninspected.

## Limitations

This classification concerns asymptotically stable *equilibria*, not all equilibrium points, periodic trajectories, or global basins. The strict clipping condition is essential to the exclusion of central/kink equilibria from the attracting class. The graph must be finite, connected, undirected and symmetrically weighted; the social-response function is exactly the piecewise-linear clipped sign. Outside the specified clipping regime, new central-region local minima or other phenomena may require separate analysis. No conclusions are claimed for directed graphs, heterogenous feedback gains, stochastic opinion updates, or finite-time convergence of arbitrary initial states.

## References

- H. AlMahmoud and F. Mallmann-Trenn, *Harmonizing vs Polarizing Platform Influence Functions* (first public preprint 11 October 2024), arXiv:2410.09225v1, https://arxiv.org/abs/2410.09225.
- O. Candogan, N. Immorlica, B. Light and J. Anunrojwong, *Social Learning under Platform Influence: Consensus and Persistent Disagreement* (2022), arXiv:2202.12453, https://arxiv.org/abs/2202.12453.
- W. Duncan, T. Gedeon, H. Kokubu, K. Mischaikow and H. Oka, *Equilibria and their Stability in Networks with Steep Sigmoidal Nonlinearities* (2021), arXiv:2103.17184, https://arxiv.org/abs/2103.17184.
