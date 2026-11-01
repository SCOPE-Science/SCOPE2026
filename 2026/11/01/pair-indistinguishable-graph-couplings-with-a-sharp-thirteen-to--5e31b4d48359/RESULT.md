# Pair-indistinguishable graph couplings with a sharp thirteen-to-one equilibrium split

## Finding
For every simple undirected graph \(G\), with vertex degrees \(d_i\), consider two families of autonomous ordinary differential equations with a common parameter \(\kappa>0\):
\[
 \dot x_i=-x_i-x_i^3+\kappa\sum_{j\sim i}(x_i-x_j)\qquad (U),
\]
\[
 \dot x_i=-x_i-x_i^3+\frac{\kappa}{d_i}\sum_{j\sim i}(x_i-x_j)\qquad (N).
\]
The coupling term of \((N)\) is defined to be zero at an isolated vertex. The two vector fields agree identically, for every initial state and every \(\kappa\), on every graph of maximum degree at most one. Thus no complete observations from isolated nodes and edges can distinguish the two aggregation conventions.

The connected three-vertex complete graph \(K_3\) is a minimal-size witness to a decisive difference. For any \(1/3<\kappa<2/3\), \((N)\) has precisely the zero equilibrium and all its trajectories converge to zero exponentially, whereas \((U)\) has precisely thirteen distinct hyperbolic equilibria: zero with two unstable directions, six saddles with one unstable direction each, and six attracting equilibria. Every trajectory of \((U)\) converges to an equilibrium; Lebesgue-almost every initial condition converges to one of the six attracting equilibria.

The complete parameter classification of \((U)\) on \(K_3\) is: for \(0<\kappa\le1/3\), zero is the unique equilibrium and is globally attracting (exponentially when \(\kappa<1/3\)); for every \(\kappa>1/3\), exactly the same thirteen-equilibrium census and stability partition hold. The normalized family has the identical classification upon replacing \(\kappa\) by \(\kappa/2\).

## Assumptions and scope
The node state space is all of \(\mathbb R\), and coupled state space is \(\mathbb R^{|V(G)|}\). The graph is simple and undirected. The same real coupling parameter and identical scalar nodal law are used in \((U)\) and \((N)\); only degree normalization differs. Isolated vertices carry zero coupling. For the complete equilibrium classification, the graph is exactly the unweighted triangle \(K_3\). Equilibria and attraction are in the full state space, not only on a synchronization subspace. Hyperbolicity is asserted only for the strict regime \(\kappa>1/3\).

For \(\kappa>1/3\), define \(b=3\kappa-1\) and let \(s=s(\kappa)\) be the unique real root of
\[
 \kappa s^3+s^2+s+2\kappa=0.
\]
This root satisfies \(-2<s<-\sqrt[3]{2}\). Set \(u=\sqrt{\kappa(1-s)-1}>0\). The thirteen equilibria are zero, all six permutations of \((\sqrt b,-\sqrt b,0)\), and all three permutations of each of \((u,u,su)\) and \((-u,-u,-su)\). These sets are pairwise disjoint for every \(\kappa>1/3\).

## Proof
**Pair indistinguishability and minimal graph size.** Each nonisolated vertex of any graph with maximum degree at most one has degree one; hence division by its degree changes nothing. No simple graph with at most two vertices has a vertex of degree exceeding one. On \(K_3\), every vertex has degree two, so \((N)\) is exactly \((U)\) with effective strength \(\kappa/2\).

**Gradient structure and the sharp threshold.** Let \(L=3I-\mathbf1\mathbf1^{\mathsf T}\) be the triangle Laplacian, whose eigenvalues are \(0,3,3\). The unnormalized flow is negative gradient flow of the proper quartic potential
\[
 V_\kappa(x)=\tfrac12\|x\|^2+\tfrac14\sum_{i=1}^3x_i^4-\tfrac\kappa2x^{\mathsf T}Lx.
\]
For \(0<\kappa\le1/3\),
\[
 x^{\mathsf T}\nabla V_\kappa(x)
 =x^{\mathsf T}(I-\kappa L)x+\sum_i x_i^4>0
 \quad(x\ne0).
\]
Thus zero is the only critical point and is globally attracting by the strict energy identity \(\dot V_\kappa=-\|\nabla V_\kappa\|^2\), compact sublevel sets, and the invariance principle. When \(\kappa<1/3\), the direct squared-norm inequality gives exponential convergence at rate at least \(1-3\kappa\).

**Exhaustion of all equilibria above threshold.** Write \(S=x_1+x_2+x_3\). Each equilibrium coordinate solves the same depressed cubic
\[
 x_i^3-(3\kappa-1)x_i+\kappa S=0.
\]
If all three coordinates are distinct, they are the three roots of this cubic. Their sum is zero, forcing \(S=0\), and the coordinates are exactly \(0,\sqrt b,-\sqrt b\). If all coincide, the coupling vanishes and all must be zero. In the remaining case two coordinates agree: write \((x_1,x_2,x_3)=(u,u,su)\) with \(u\ne0\) and \(s\ne1\). Eliminating \(u\) gives
\[
 u^2=\kappa(1-s)-1,
 \qquad \kappa s^3+s^2+s+2\kappa=0.
\]
The cubic in \(s\) has strictly positive derivative for every real \(s\) when \(\kappa>1/3\), since \(3\kappa s^2+2s+1=(s+1)^2+(3\kappa-1)s^2>0\). Its values at \(-2\) and \(-\sqrt[3]{2}\) have opposite signs. Hence there is precisely one real root, in the interval stated. From its defining equation,
\[
 u^2=-\frac{s+2}{s^3+2}>0.
\]
This yields precisely six additional equilibria (two signs and three positions).

**Hyperbolic stability of all thirteen points.** The Hessian is \(H(x)=\operatorname{diag}(1+3x_i^2)-\kappa L\); the Jacobian is \(-H\). At zero the Hessian eigenvalues are \(1,1-3\kappa,1-3\kappa\), so its unstable dimension is two for \(\kappa>1/3\). At any permutation of \((\sqrt b,-\sqrt b,0)\), the antisymmetric Hessian eigenvalue is \(2b>0\); on the complementary symmetric two-plane the Hessian determinant is \(-2b^2<0\). Consequently these six points each have one unstable direction.

At \((u,u,su)\), the antisymmetric Hessian eigenvalue is
\[
 \lambda_a=\kappa\frac{(w+1)(2-w)^2}{w(w-1)}>0,
 \qquad w=-s\in(\sqrt[3]{2},2).
\]
The remaining symmetric two-plane block has diagonal entry and determinant
\[
 \frac{B_{11}}\kappa=\frac{w^3-w^2-2w+4}{w(w-1)}>0,
\]
\[
 \frac{\det B}{\kappa^2}=
 \frac{2(w+1)(2-w)(w^4-2w^3+4w-2)}{w^2(w-1)^2}>0.
\]
For the second inequality, \(w^4-2w^3+4w-2\) is positive for \(w>1\): it equals one at \(w=1\), has positive derivative there, and has second derivative \(12w(w-1)>0\) for \(w>1\). The first numerator equals \(w^2(w-1)+2(2-w)>0\). Sylvester's criterion proves positive definiteness of \(H\). Central sign reversal and coordinate permutations preserve Hessian eigenvalues, so all six two-equal equilibria are hyperbolic sinks.

**Global limiting dynamics.** The potential is proper and decreases along every trajectory. Hence all forward trajectories exist globally, remain bounded, and their omega-limit sets are contained in the equilibrium set. The omega-limit set of a bounded trajectory is connected; because the equilibrium set is finite, the limit is a single equilibrium. The stable manifolds of the seven hyperbolic nonsinks have codimension at least one and Lebesgue measure zero. Almost every initial condition therefore tends to one of the six sinks. For the normalized triangle, substitute \(\kappa/2\) everywhere, giving the claimed strict discrepancy for \(1/3<\kappa<2/3\).

## Verification
The standalone Python file `verify.py` reconstructs the two-equal cubic root, all thirteen candidate equilibria, their residuals, and their Hessian signs for seven coupling strengths above threshold. It checks the isolated/pair equality on sample states and the normalized triangle threshold. The program prints `VERIFY_OK` upon success. Its numerical residual tests are finite checks, not an exhaustive computer proof; the preceding algebra and gradient argument establish the universal statements.

At \(\kappa=1/2\), the unnormalized triangle has thirteen equilibria and six sinks, including a permutation of approximately \((0.5213870984,0.5213870984,-0.8048595351)\), while the normalized triangle has only the globally attracting zero equilibrium.

## Relationship to prior work
Fan, Du, Bi, Wang, and Wang (2026) study learning reusable nodal and pair-coupling modules for networked dynamics. Their formulation expressly *prescribes the full coupling matrix*. The result here addresses the different, weaker information regime in which only the unweighted topology, the nominal coupling parameter, and isolated/pair dynamical observations are available, without declaring the degree-weight convention. It is not a counterexample to the source's stated assumption of a known weighted coupling matrix.

Caputo, Cruz-Pacheco, and Panayotaros (2014/2015) study ordinary **positive** graph diffusion of an intrinsically bistable cubic reaction law, including front pinning. Kouvaris, Kori, and Mikhailov (2012) treat bistable reaction–diffusion on networks; McCullen and Wagenknecht (2016) study localized and Turing-type patterns in multi-species network systems. Their inspected models and conclusions do not imply the exact thirteen-point census and normalization-dependent observational indistinguishability for the present monostable, anti-diffusively coupled scalar law.

## Limitations
The conclusion is conditional on not knowing the edge-weight convention for larger networks. If the *weighted* coupling matrix is provided, the two families are distinguishable as specifications; the source motivating modular network modeling assumes such a matrix is prescribed. This is an exact identifiability and phase-portrait statement for a particular scalar cubic family and an unweighted triangle, not a claim about generic chaotic oscillators, learning algorithms, arbitrary graph sizes, noisy sampled data, or an independent historical-priority certification. All analytical statements are mathematical consequences of the printed equations; the finite code checks are corroborative only.

## References
1. H. Fan, Y. Du, M.-X. Bi, Y. Wang, and X. Wang, *Digital Twins of Networked Dynamical Systems: Machine Learning Prediction of Synchronization Transitions in Coupled Chaotic Oscillators*, arXiv:2610.30632v1, first posted 2026-10-22. https://arxiv.org/abs/2610.30632
2. J.-G. Caputo, G. Cruz-Pacheco, and P. Panayotaros, *Bistable reaction-diffusion on a network*, arXiv:1406.7742v1 (2014), *Journal of Physics A* (2015). https://arxiv.org/html/1406.7742v1
3. N. E. Kouvaris, H. Kori, and A. S. Mikhailov, *Traveling and Pinned Fronts in Bistable Reaction-Diffusion Systems on Networks*, *PLoS ONE* 7:e45029 (2012), doi:10.1371/journal.pone.0045029. https://pmc.ncbi.nlm.nih.gov/articles/PMC3461022/
4. N. McCullen and T. Wagenknecht, *Pattern Formation on Networks: from Localised Activity to Turing Patterns*, *Scientific Reports* 6:27397 (2016), doi:10.1038/srep27397. https://www.nature.com/articles/srep27397
