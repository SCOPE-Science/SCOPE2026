# A sharp endemic fold and a balancing principle for pure higher-order contagion on multipartite hypergraphs

## Finding

Let \(m\geq3\), let \(V_1,\ldots,V_m\) be nonempty disjoint groups of respective integer sizes \(n_1,\ldots,n_m\), and let \(H\) be the complete \(m\)-partite \(m\)-uniform hypergraph: every hyperedge contains precisely one vertex from every group. Each vertex recovers at rate one. At infection parameter \(\lambda>0\), an uninfected vertex becomes infected through a hyperedge only when all the other \(m-1\) members are infected. In the node-independent deterministic SIS closure, with infected probabilities \(z_v\in[0,1]\), the equations are
\[
 \dot z_v=-z_v+\lambda(1-z_v)\prod_{j\ne i}\left(\sum_{w\in V_j}z_w\right),\qquad v\in V_i.\tag{1}
\]

Define, for \(h>0\),
\[
 u_i(h)=\frac{2}{1+\sqrt{1+4n_i/h}},\quad
 \Lambda_{\boldsymbol n}(h)=\frac{h}{\prod_{i=1}^m n_i u_i(h)},\quad
 \Phi_{\boldsymbol n}(h)=\sum_{i=1}^m\frac{1-u_i(h)}{2-u_i(h)}.
\]
There is exactly one \(h_*>0\) satisfying \(\Phi_{\boldsymbol n}(h_*)=1\). Put \(\lambda_*(\boldsymbol n)=\Lambda_{\boldsymbol n}(h_*)\). The **complete equilibrium and local-stability classification**, valid in the full \(\sum_i n_i\)-dimensional node system, is:

1. The disease-free state is locally exponentially attracting for every \(\lambda>0\), and it is the only equilibrium when \(0<\lambda<\lambda_*(\boldsymbol n)\).
2. At \(\lambda=\lambda_*(\boldsymbol n)\) there is one additional strictly positive equilibrium, with \(z_v=u_i(h_*)\) for \(v\in V_i\). It is a nondegenerate saddle-node equilibrium (one simple zero eigenvalue; all other eigenvalues strictly negative).
3. For \(\lambda>\lambda_*(\boldsymbol n)\) there are exactly two strictly positive equilibria, \(h_-<h_*<h_+\) determined by \(\Lambda_{\boldsymbol n}(h_\pm)=\lambda\). The lower branch has precisely one unstable real eigenvalue and is a hyperbolic saddle; the upper branch is locally exponentially attracting. No other equilibria, including partially infected boundary equilibria, occur.
4. Among all positive integer group-size vectors with prescribed total population \(N=\sum_i n_i\ge m\), the threshold \(\lambda_*(\boldsymbol n)\) is uniquely minimized up to permutation by group sizes differing by at most one. More generally, replacing unequal sizes \(a,b\) with \(a+1,b-1\) for integers \(b\ge a+2\) strictly decreases the threshold. For arbitrary positive real sizes, the sharp lower bound is
\[
 \lambda_*(\boldsymbol n)\geq
 \frac{(m-1)^{m-1}}{(m-2)^{m-2}(N/m)^{m-1}},\tag{2}
\]
with equality precisely when all \(n_i=N/m\). When \(N\) is divisible by \(m\), the balanced finite hypergraph attains (2).

In particular, for three groups of size three, \(\lambda_*=4/9\); replacing \((3,3,3)\) by \((2,3,4)\) raises it to approximately \(0.48510449188147\), and \((1,4,4)\) raises it to approximately \(0.66171687727106\). These decimals are only illustrations; the variational characterization and inequalities above are exact.

## Assumptions and scope

The graph is an \(m\)-uniform hypergraph with **transversal** edges only: one vertex from each of the \(m\) groups, and all possible such edges. Each individual has identical unit recovery rate and identical per-hyperedge infection coefficient \(\lambda\), with no pairwise transmission, imported infection, external reservoir, self-infection, or behavioral feedback. Equation (1) is a deterministic independence-closure for node infection probabilities; it is not claimed to be an exact finite-population Markov marginal equation. No scaling of \(\lambda\) with population size is implicit. The group sizes are integers in the graph result; the real-size extension is a statement about the analytical threshold formula.

There are no nonzero boundary equilibria. Indeed, at an equilibrium a zero coordinate forces at least one other group to have zero total infection. Every coordinate outside a zero-total group then satisfies \(\dot z_v=-z_v\), hence must vanish at equilibrium; the remaining zero-total group vanishes by definition. Thus every nonzero equilibrium is strictly interior.

## Proof

**Step 1: every positive equilibrium is group-symmetric.** For fixed totals \(S_j=\sum_{w\in V_j}z_w\), all vertices in group \(V_i\) have the same infection pressure \(E_i=\lambda\prod_{j\ne i}S_j\). The equilibrium equation \(z_v/(1-z_v)=E_i\) uniquely determines \(z_v=E_i/(1+E_i)\). Thus a positive equilibrium has a common value \(x_i\in(0,1)\) within each group. It satisfies
\[
 x_i=\lambda(1-x_i)\prod_{j\ne i}(n_jx_j),\qquad 1\le i\le m.\tag{3}
\]
Multiplying (3) by \(n_ix_i/(1-x_i)\) gives the common value
\[
 \frac{n_ix_i^2}{1-x_i}=\lambda\prod_j n_jx_j=:h>0.\tag{4}
\]
The unique solution of (4) in \((0,1)\) is \(x_i=u_i(h)\). Conversely, a choice \(h>0\) yields a positive equilibrium if and only if \(\lambda=\Lambda_{\boldsymbol n}(h)\). This is an exact one-parameter description of every positive equilibrium.

**Step 2: the unique fold.** Differentiation of \(n_i u_i^2/(1-u_i)=h\) gives
\[
 \frac{d\log u_i}{d\log h}=\frac{1-u_i}{2-u_i},\qquad
 \frac{d\log\Lambda_{\boldsymbol n}}{d\log h}=1-\Phi_{\boldsymbol n}(h).\tag{5}
\]
Every \(u_i(h)\) strictly increases from zero to one, and \((1-u)/(2-u)\) strictly decreases from \(1/2\) to zero as \(u\) increases. Hence \(\Phi\) strictly decreases from \(m/2>1\) to zero. The unique critical point \(h_*\) of \(\Lambda\) is a strict nondegenerate minimum, since
\[
 \left.\frac{d^2\log\Lambda}{dh^2}\right|_{h=h_*}
 =-\frac{\Phi'(h_*)}{h_*}>0.\tag{6}
\]
As \(h\downarrow0\), \(u_i(h)\sim\sqrt{h/n_i}\), so \(\Lambda(h)\sim h^{1-m/2}/\sqrt{\prod n_i}\to\infty\). As \(h\to\infty\), \(u_i(h)\to1\) and \(\Lambda(h)\sim h/\prod n_i\to\infty\). Therefore a horizontal line at \(\lambda\) intersects the graph in exactly zero, one, or two positive points according as \(\lambda\) is below, at, or above \(\lambda_*\).

**Step 3: full-system Jacobian and inertia.** The class-constant perturbations form an invariant \(m\)-dimensional subspace at any group-symmetric equilibrium. From (3), the corresponding Jacobian \(J\) has entries
\[
 J_{ii}=-\frac1{1-x_i},\qquad J_{ij}=\frac{x_i}{x_j}\quad(i\ne j).
\]
Similarity by \(D=\operatorname{diag}(x_i)\) transforms it into the real symmetric matrix
\[
 D^{-1}JD={\boldsymbol1}{\boldsymbol1}^{\mathsf T}-C,\qquad
 C=\operatorname{diag}\left(\frac{2-x_i}{1-x_i}\right).
\]
Congruence with \(C^{-1/2}\) shows that this matrix has \(m-1\) negative eigenvalues and one remaining eigenvalue whose sign is the sign of
\[
 \sum_i\frac{1-x_i}{2-x_i}-1=\Phi_{\boldsymbol n}(h)-1.\tag{7}
\]
All within-group zero-sum perturbations have eigenvalues \(-1/(1-x_i)<0\), of multiplicity \(n_i-1\). Indeed, infection pressure on a vertex depends on other groups only through group sums, so these within-group modes neither feed into other groups nor receive within-group coupling. Therefore the full node Jacobian has precisely one positive eigenvalue on the lower branch, none on the upper, and a simple zero at the fold. Equation (6), this simple kernel, and the positive nonzero derivative of the vector field with respect to \(\lambda\) against the positive left zero eigenvector establish a nondegenerate saddle-node. At the zero state the entire Jacobian equals \(-I\), because all infection terms have degree at least two. This proves the local claims.

**Step 4: balance minimizes the threshold.** For fixed \(h>0\), define the infected *count* factor
\[
 g_h(n)=nu(h;n)=\frac h2\left(\sqrt{1+4n/h}-1\right).
\]
It is strictly positive, increasing, and strictly concave in \(n>0\), because \(g_h'(n)=(1+4n/h)^{-1/2}>0\) and \(g_h''(n)=-(2/h)(1+4n/h)^{-3/2}<0\). Thus \(\log g_h(n)\) is also strictly concave. At fixed \(N=\sum_i n_i\), Jensen's inequality gives
\[
 \prod_i g_h(n_i)\le g_h(N/m)^m,
\]
strictly unless all sizes are equal. Hence \(\Lambda_{\boldsymbol n}(h)\ge\Lambda_{(N/m,\ldots,N/m)}(h)\) for every \(h\). Evaluating at the minimizing \(h\) for the left-hand side gives the corresponding (strict, when unbalanced) inequality of minimum thresholds. The integer smoothing rule follows from strict concavity: when \(b\ge a+2\), replacing \((a,b)\) by \((a+1,b-1)\) strictly raises \(g_h(a)g_h(b)\) for every \(h\), thereby strictly lowering the minimum threshold. Repetition terminates precisely at the near-equal integer partition.

For equal positive real sizes \(s=N/m\), symmetry forces \(u_i(h)=x\), and (3) becomes \(1=\lambda s^{m-1}x^{m-2}(1-x)\). The unique maximum of \(x^{m-2}(1-x)\) occurs at \(x=(m-2)/(m-1)\), giving (2) and its equality criterion. This completes the proof.

## Verification

The standalone program `verify_tripartite.py` runs with Python 3, NumPy and SymPy using `python verify_tripartite.py` after installing `requirements.txt`. It verifies exact stationary and Jacobian identities for the balanced three-group fold, the two opposite-stability branches at \(\lambda=9/8\), and a heterogeneous rational endemic equilibrium with group sizes \((72,27,16)\), class probabilities \((1/2,2/3,3/4)\), and \(\lambda=1/216\). It also compares numerical thresholds for every integer three-group partition with total size at most 18. The finite tests are not a proof of the general assertions; the proof above supplies the arbitrary-order and arbitrary-size arguments.

## Relationship to prior work

Cui–Liu–Jardón-Kojakhmetov–Cao (arXiv:2306.00619, initial public version June 1, 2023) formulate node-based hypergraph SIS infection, including joint infection mechanisms, and provide general stability results; the paper does not give the exact transversal complete-multipartite equilibrium curve, complete branch inertia, or fixed-total-population balancing theorem. Kiss–Iacopini–Simon–Georgiou (arXiv:2309.12752, initial version September 22, 2023) derive homogeneous complete-simplicial mean-field equations and scalar bifurcation diagrams, including higher-order interactions; the balanced specialization here has the same familiar scalar fold mechanism, which is not claimed as new. The contribution is the exact and complete *heterogeneous* multipartite classification and the strict optimum over group-size allocations.

Cisneros-Velarde–Bullo (arXiv:2005.11404) establish general multi-group higher-order SIS existence and stability criteria, but their conditions do not resolve the present exact allocation-dependent fold. Landry–Restrepo (arXiv:2302.13967) study a different two-community planted-partition hypergraph and emphasize sensitivity to unequal community sizes; their formulation is not the complete transversal \(m\)-partite model and does not imply the balancing theorem above. These comparisons are statement-level; no claim of exhaustive bibliographic priority or independent vetting is made.

## Limitations

The theorem classifies equilibria and their **local** stability, not global basins, stochastic extinction times, persistence of the finite-state epidemic, or rates under an alternative population-size normalization. The exact finite stochastic SIS chain has an absorbing healthy state, unlike the deterministic endemic equilibria of (1). Equal recovery rates, pure all-others-infected group transmission, and the complete transversal multipartite structure are essential assumptions. The balancing conclusion is for fixed *total number of vertices* and fixed per-hyperedge infection coefficient. The strict onset formula concerns the deterministic closure and need not be a stochastic outbreak threshold. An equivalent theorem in another source or normalization may exist; independent bibliographic and mathematical validation remain outstanding.

## References

1. S. Cui, F. Liu, H. Jardón-Kojakhmetov, M. Cao, *General SIS diffusion process with indirect spreading on a hypergraph*, arXiv:2306.00619 (first submitted June 1, 2023), https://arxiv.org/abs/2306.00619 . Relevant model and results: Sections 3–4 and 6.
2. I. Z. Kiss, I. Iacopini, P. L. Simon, N. Georgiou, *Insights from exact social contagion dynamics on networks with higher-order structures*, arXiv:2309.12752 (first submitted September 22, 2023), https://arxiv.org/abs/2309.12752 . Relevant material: Sections II–III and Appendix A.
3. P. Cisneros-Velarde, F. Bullo, *Multi-group SIS Epidemics with Simplicial and Higher-Order Interactions*, arXiv:2005.11404, https://arxiv.org/abs/2005.11404 . Relevant material: Sections 4–6.
4. N. W. Landry, J. G. Restrepo, *Opinion disparity in hypergraphs with community structure*, arXiv:2302.13967, https://arxiv.org/abs/2302.13967 . Relevant material: Sections II–III.
