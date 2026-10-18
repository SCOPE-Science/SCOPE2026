# Unique heterogeneous coexistence on every connected nonbipartite social network

## Finding
For the interacting Pólya-urn social-pressure response on an arbitrary finite connected, undirected, positively weighted, nonbipartite graph, heterogeneous fixed biases never permit two distinct interior equilibria. More precisely, unless every bias is neutral, an interior equilibrium exists **if and only if both boundary Perron multipliers exceed one**; when it exists it is unique, and every strictly interior deterministic trajectory converges to it. Combining this classification with the stochastic-approximation and boundary-repulsion theorems established for this model in [1] yields almost-sure convergence of every admissibly initialized stochastic declaration-frequency process to that single deterministic interior equilibrium. Connected bipartite graphs admit a sharp exceptional family with an entire curve of equilibria, showing the graph hypothesis matters.

## Assumptions and scope
Let \(n\geq1\), and let \(A=(a_{ij})\) be a symmetric nonnegative matrix whose positive-edge support is connected. Require every weighted degree \(d_i=\sum_j a_{ij}\) to be positive. Self-loops are allowed. Set \(W_{ij}=a_{ij}/d_i\). For the principal theorem the support must be nonbipartite (equivalently it contains an odd closed walk). Let \(\gamma_i>0\), and assume \(\gamma_i\ne1\) for at least one vertex. Put \(\Gamma=\operatorname{diag}(\gamma_i)\), and define
\[
f_\gamma(s)=\frac{\gamma s}{1+(\gamma-1)s},\qquad F_i(x)=f_{\gamma_i}\bigl((Wx)_i\bigr),\quad x\in[0,1]^n.
\]
Define \(\rho_0=\rho(\Gamma W)\), \(\rho_1=\rho(\Gamma^{-1}W)\), with \(\rho\) the spectral radius. The only boundary fixed points are \(\mathbf0\) and \(\mathbf1\): if any coordinate is zero, connectedness and strict positivity of \(f_\gamma(s)\) for \(s>0\) force all coordinates zero, and similarly for one.

**Theorem.** If \(\rho_0>1\) and \(\rho_1>1\), there exists exactly one \(x_*\in(0,1)^n\) with \(F(x_*)=x_*\). Every orbit of the synchronous map \(x_{k+1}=F(x_k)\), started at \(x_0\in(0,1)^n\), tends to \(x_*\). The same holds for the deterministic diminishing-step recursion
\[
x_{k+1}=x_k+a_k(F(x_k)-x_k),\qquad 0<a_k\le1,\quad \sum_k a_k=\infty.
\]
If either multiplier is at most one, there is no interior fixed point. For the stochastic interacting Pólya urn with positive initial counts and simultaneous Bernoulli declarations according to the response above, \(\beta(t)\to x_*\) almost surely in the two-multiplier-supercritical case, using Theorems 3 and 4 of [1]. If either multiplier is at most one, [1, Theorem 4] gives almost-sure convergence to the appropriate consensus endpoint.

**Sharp graph boundary.** On a connected loopless bipartite graph with sides \(U,V\), two different interior fixed points can exist only if all vertices in \(U\) share one bias \(\alpha>0\) and all vertices in \(V\) share its reciprocal \(\alpha^{-1}\). In that exceptional case every \(b\in(0,1)\) determines a fixed point having coordinates \(f_\alpha(b)\) on \(U\) and \(b\) on \(V\). If all biases are one on a connected nonbipartite graph, every constant vector in \([0,1]^n\) is fixed; this neutral case is excluded from the theorem.

## Proof
**1. An odds-comparison rigidity lemma.** Write \(O(s)=s/(1-s)\) and, for \(r>0\), \(H_r(s)=rs/[1+(r-1)s]\). Then \(O(H_r(s))=rO(s)\), \(f_\gamma=H_\gamma\), and \(H_r\circ H_s=H_{rs}\). For \(r>1\),
\[
H_r''(s)=-\frac{2r(r-1)}{[1+(r-1)s]^3}<0\quad(0<s<1).
\]
Suppose that \(x,y\in(0,1)^n\) are distinct fixed points. Interchange them if necessary to ensure \(R=\max_i O(x_i)/O(y_i)>1\). By definition \(x_j\le H_R(y_j)\) for every \(j\). Monotonicity and Jensen's inequality imply, for every \(i\),
\[
(Wx)_i\le\sum_j W_{ij}H_R(y_j)\le H_R((Wy)_i).
\]
Applying odds, using \(O(f_{\gamma_i}(z))=\gamma_i O(z)\), and cancelling the common factor \(\gamma_i\), gives
\[
\frac{O(x_i)}{O(y_i)}=\frac{O((Wx)_i)}{O((Wy)_i)}\le R.
\]
At any vertex attaining the maximum ratio \(R\), equality holds throughout both preceding inequalities. As each nonzero \(W_{ij}\) is positive, the first equality forces \(x_j=H_R(y_j)\) for every neighbor \(j\); hence those neighbors also attain the maximum ratio. By connectedness **every vertex** attains it. Strict concavity of \(H_R\) and Jensen equality now force \(y_j\) to be constant on the neighborhood of every vertex. Any two vertices in a connected nonbipartite undirected graph are joined by an even-length walk, so the neighborhood equalities force all coordinates of \(y\) to equal one \(c\in(0,1)\). But then \(c=f_{\gamma_i}(c)\) at every vertex, which forces every \(\gamma_i=1\). This contradicts the hypothesis and proves uniqueness.

For a bipartite connected support, the same equality argument shows \(y\) constant on each bipartition class, say \(a\) on \(U\) and \(b\) on \(V\). Fixed-point equations become \(a=f_{\gamma_i}(b)\) for \(i\in U\), and \(b=f_{\gamma_j}(a)\) for \(j\in V\). Strict monotonicity in the parameter \(\gamma\) gives biases \(\alpha\) on \(U\), \(\alpha^{-1}\) on \(V\); conversely these biases yield the displayed one-dimensional equilibrium family.

**2. Spectral necessity.** If \(x\in(0,1)^n\) is a fixed point, then \(x\) is nonconstant (otherwise every bias would equal one). Define \(z_i=(1-x_i)/x_i>0\). The fixed-point odds identity and strict convexity of \(s\mapsto1/s\) yield
\[
(\Gamma^{-1}Wz)_i\ge z_i,
\]
with a strict inequality for at least one vertex, because otherwise the same even-walk argument makes \(x\) constant. Let \(v>0\) be a left Perron vector of \(\Gamma^{-1}W\). Multiplying by \(v\) gives \(\rho_1 v^\top z>v^\top z\), hence \(\rho_1>1\). Applying the identical argument to the complementary fixed point \(\mathbf1-x\), whose biases are \(\gamma_i^{-1}\), gives \(\rho_0>1\). Thus both inequalities are necessary; no spectral-boundary case has an interior fixed point.

**3. Spectral sufficiency.** The derivative of \(F\) at \(\mathbf0\) is \(\Gamma W\). If \(\rho_0>1\), take its positive right Perron vector \(p\gg0\). For sufficiently small \(\varepsilon>0\), Taylor expansion yields \(F(\varepsilon p)>\varepsilon p\) coordinatewise. The complementary dynamics \(\mathbf1-F(\mathbf1-z)\) have derivative \(\Gamma^{-1}W\) at \(z=\mathbf0\). With its right Perron vector \(q\gg0\), small \(\varepsilon\) gives \(F(\mathbf1-\varepsilon q)<\mathbf1-\varepsilon q\). Choose \(\varepsilon\) so the lower and upper vectors are ordered. Since \(F\) is order-preserving, its iterates from the lower vector increase and stay below the upper vector; their limit is an interior fixed point. Uniqueness follows from step 1.

**4. Attraction from all interior initial states.** For a fixed interior \(x_*\), Jensen and the commutation \(f_{\gamma_i}\circ H_r=H_r\circ f_{\gamma_i}\) show
\[
F(H_r(x_*))\ge H_r(x_*)\quad(0<r<1),\qquad
F(H_r(x_*))\le H_r(x_*)\quad(r>1),
\]
where \(H_r\) acts coordinatewise. The first uses convexity of \(H_r\), the second concavity. For any \(x_0\in(0,1)^n\), choose \(0<r<1<R\) with \(H_r(x_*)\le x_0\le H_R(x_*)\). The lower and upper iterates are respectively increasing and decreasing, remain strictly inside the cube, and have fixed-point limits. The uniqueness lemma makes both limits \(x_*\); order comparison squeezes every synchronous trajectory. For variable step sizes, the same barriers generate monotone bounded sequences. If the lower (respectively upper) limit were not fixed, some nonzero limiting signed drift would be bounded away from zero, contradicting boundedness and \(\sum_k a_k=\infty\). Hence both limits again equal \(x_*\).

**5. Stochastic conclusion and its precise provenance.** The original stochastic model has diminishing increments of size at most \(1/(t+1)\). Theorem 3 of [1] establishes almost-sure approach to the set of fixed points. Here that set is exactly \(\{\mathbf0,x_*,\mathbf1\}\); vanishing jump size therefore forces convergence to a single one of these three isolated points. Theorem 4 of [1] proves that a boundary with Perron multiplier greater than one is reached with probability zero. Both boundaries satisfy that condition, so the remaining limit is \(x_*\) almost surely. These stochastic ingredients are established in [1], not independently reproved here.

## Verification
Take \(W=\mathbf1\mathbf1^\top/3\) and \(\gamma=(3,1/2,1/2)\). Then \(\rho_0=4/3\), \(\rho_1=13/9\), and direct rational substitution gives the unique interior equilibrium \(x_*=(3/5,1/5,1/5)\). For the two-node bipartite edge with \(\gamma=(2,1/2)\), every \(b\in(0,1)\) gives \(x=(2b/(1+b),b)\), demonstrating a continuum when nonbipartiteness is removed. The included standalone `verify.py` uses rational arithmetic for these identities, checks strict odds-transform Jensen inequalities and order barriers, and compares deterministic numerical trajectories with the exact equilibrium. These finite checks support, but do not replace, the arguments above. Execute using `python verify.py` with Python 3.

## Relationship to prior work
Tang, Adler, Ajorlou and Jadbabaie [1] introduce the arbitrary-network weighted model, characterize boundary Perron thresholds, show approach to an equilibrium **set**, and expressly leave uniqueness/isolation of interior equilibria as an open direction (their Section III-B and conclusion). Their Theorems 3 and 4 supply the stochastic claims used in step 5; boundary repulsion is not claimed here as new. Jadbabaie, Makur, Mossel and Salhab [2] establish the earlier complete-graph homogeneous framework; Tang and coauthors [3] address inference of fixed private beliefs and biases, not uniqueness of heterogeneous interior equilibria. The contribution assessed here is the **global heterogeneous, arbitrary-connected-nonbipartite uniqueness and attraction theorem**, with its exact bipartite failure mechanism. Earlier special complete-graph analyses and Perron criteria do not imply this general uniqueness by title or parameter matching alone; they require the odds-comparison argument supplied above.

## Limitations
The uniqueness and deterministic attraction theorem is restricted to finite connected undirected networks, strictly positive biases, the stated fractional-linear response and at least one nonneutral bias. It does not address asymmetric directed interactions, changing graph weights, higher-dimensional opinion alphabets, or arbitrary nonlinear response functions. The bipartite exceptional statement classifies *nonuniqueness*, not all cases of isolated existence on bipartite graphs. The stochastic almost-sure result invokes two established theorems of [1]; it is not an independent construction of their Lyapunov or boundary-repulsion proofs. Novelty is assessed against inspected accessible sources; broader equivalent general fixed-point theorems remain a publication-priority risk.

## References
[1] J. Tang, A. Adler, A. Ajorlou and A. Jadbabaie, *Stochastic Opinion Dynamics under Social Pressure in Arbitrary Networks*, arXiv:2308.09275 (first public submission 2023-08-18), especially Theorems 3 and 4, Section III-B and the conclusion. https://arxiv.org/abs/2308.09275

[2] A. Jadbabaie, A. Makur, E. Mossel and R. Salhab, *Inference in Opinion Dynamics under Social Pressure*, arXiv:2104.11172 (2021). https://arxiv.org/abs/2104.11172

[3] J. Tang, A. Adler, A. Ajorlou and A. Jadbabaie, *Estimating True Beliefs in Opinion Dynamics with Social Pressure*, arXiv:2310.17171 (2023). https://arxiv.org/abs/2310.17171
