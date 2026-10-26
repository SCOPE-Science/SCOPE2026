# A universal half-coupling transition for nearly complete competitive ecological networks

## Finding
For each integer \(n\ge4\), delete a nonempty matching of \(s\) edges from the complete interaction graph \(K_n\), leaving \(r=n-2s\ge0\) vertices not incident to the deleted matching. In homogeneous symmetric competitive Lotka–Volterra dynamics, the stable full-coexistence threshold is **exactly \(\alpha=1/2\)** for every such \(n,s\). By contrast, the complete graph has threshold \(\alpha=1\). Thus deleting **one** of \(\binom n2\) competitive interactions halves the threshold for every \(n\ge4\).

The transition has an explicit dynamical structure. For \(0\le\alpha<1/2\), every strictly positive initial population converges to a unique, strictly positive equilibrium, given below. At \(\alpha=1/2\), a simplex of stationary states has equal abundances within each noninteracting pair, zero abundance at the \(r\) unmatched sites, and pair abundances totaling one. If initially both members of each pair have the same strictly positive abundance \(q_i(0)\), then **irrespective of the strictly positive unmatched-site initial abundances**, the entire trajectory converges at criticality to the point with pair abundance \(q_i(0)/\sum_j q_j(0)\).

For \(1/2<\alpha<1\), the only linearly asymptotically stable equilibria are the \(s\) binary states retaining the two members of exactly one deleted edge, both at abundance one. Under strictly positive, pair-balanced initial populations with a uniquely largest initial pair abundance, the winning pair is **exactly that initially largest pair**; all other populations go extinct. For a single deleted edge \(s=1\), this final state attracts **every strictly positive initial condition**, without pair-balance assumptions.

## Assumptions and scope
Let \(V=\{1,\ldots,n\}\), \(n\ge4\). Fix \(1\le s\le\lfloor n/2\rfloor\) pairwise disjoint pairs \(P_i=\{u_i,v_i\}\). The graph \(G\) has an undirected edge between every two distinct vertices except the pairs \(P_i\). For each \(k\in V\), \(x_k(t)\ge0\) evolves as
\[
\dot x_k=x_k\left(1-x_k-\alpha\sum_{\ell:\{k,\ell\}\in E(G)}x_\ell\right),\qquad\alpha\ge0.
\]
Positive initial conditions mean \(x_k(0)>0\) for every vertex. A stable-coexistence threshold means the first \(\alpha\ge0\) at which there is no **strictly positive, linearly asymptotically stable** equilibrium. The strong post-transition classification is restricted to \(\alpha<1\). Pair-balanced means \(x_{u_i}(0)=x_{v_i}(0)=q_i(0)>0\) for each \(i\); unmatched-site initial abundances are arbitrary positive numbers. For \(s\ge2\), winner identification requires a unique largest \(q_i(0)\). At the critical point equal initial pair abundances are allowed.

## Proof
**1. Subcritical equilibrium and global attraction.** Write \(A\) for the adjacency matrix of \(G\), \(M\) for the adjacency matrix of the removed matching, and \(J\) for the all-ones matrix. Then
\[
H_\alpha=I+\alpha A=(1-\alpha)I-\alpha M+\alpha J.
\]
The first two terms constitute independent \(2\times2\) blocks with eigenvalues \(1\) and \(1-2\alpha\) on matched pairs, plus singleton eigenvalues \(1-\alpha\). Hence \(H_\alpha\) is positive definite for \(0\le\alpha<1/2\). Define
\[
 c_\alpha=\left[1+\alpha\left(\frac{2s}{1-2\alpha}+\frac{r}{1-\alpha}\right)\right]^{-1}.
\]
The unique equilibrium is \(x_{u_i}^*=x_{v_i}^*=c_\alpha/(1-2\alpha)\) and \(x_k^*=c_\alpha/(1-\alpha)\) for each unmatched \(k\). Each entry is positive, and substitution gives \(H_\alpha x^*=\mathbf1\). For every strictly positive solution, the weighted relative entropy
\[
\mathcal L(x)=\sum_k\left[x_k-x_k^*-x_k^*\log(x_k/x_k^*)\right]
\]
has derivative \(\dot{\mathcal L}=-(x-x^*)^{\mathsf T}H_\alpha(x-x^*)<0\) off equilibrium. Boundedness follows from \(\dot x_k\le x_k(1-x_k)\). This proves global convergence.

**2. Exact critical simplex.** At \(\alpha=1/2\), for arbitrary \(t_i\ge0\) with \(\sum_i t_i=1\), take \(x_{u_i}=x_{v_i}=t_i\) and each unmatched abundance zero. Each paired vertex has total competing abundance \(2(1-t_i)\), giving zero per-capita growth; unmatched vertices have zero own abundance. Thus all these states are stationary. When paired initial abundances agree, equality within each pair persists by uniqueness of the ODE. Write \(q_i=x_{u_i}=x_{v_i}\), \(Q=\sum_iq_i\), and \(Y\) for the sum of unmatched abundances. The reduced equations are
\[
\dot q_i=q_i\bigl[1-2\alpha Q-\alpha Y+(2\alpha-1)q_i\bigr],\qquad
\dot y_k=y_k\bigl[1-2\alpha Q-\alpha Y-(1-\alpha)y_k\bigr].
\]
At \(\alpha=1/2\), all ratios \(q_i/q_j\) are constant. The strictly increasing potential in Step 4 ensures that the nonempty omega-limit set consists of equilibria. Since the ratios remain positive and finite, any omega-limit either has all \(q_i>0\) or all \(q_i=0\). The second possibility cannot occur: a limit with all \(q_i=0\) is a clique equilibrium on some positive unmatched subset (or the origin), and there each paired type has strictly positive invasion growth \((1-\alpha)/[1+\alpha(\ell-1)]>0\) (or growth one at the origin). A strictly positive \(q_i\) cannot converge to such an equilibrium. Thus every limit has positive pairs, forcing \(Y=0\) and \(Q=1\) by the reduced equations. Constant ratios now give \(q_i(\infty)=q_i(0)/\sum_jq_j(0)\). This also proves convergence, not merely a subsequential limit.

**3. Stable states above the threshold.** Fix \(1/2<\alpha<1\). A stable equilibrium cannot contain exactly one member of a deleted-edge pair: the absent twin has per-capita invasion rate equal to the surviving member's positive abundance. If both members are present, their equilibrium abundances coincide. Therefore a stable equilibrium must use either both or neither of each pair. For a state with positive paired abundances, writing \(S=\sum_k x_k\), the paired equilibrium equations give \(1-\alpha S=(1-2\alpha)q_i<0\); the unmatched equilibrium equations, if any unmatched site is present, instead give \(1-\alpha S=(1-\alpha)y_k>0\). These are incompatible. Consequently a stable equilibrium with pairs present contains only paired vertices. If \(k\) pairs are present, all have the same abundance \(q=1/[1+2\alpha(k-1)]\). When \(k\ge2\), a perturbation splitting two pair abundances has positive eigenvalue \((2\alpha-1)q\), so this is unstable. When \(k=1\), the two surviving abundances equal one, their two internal eigenvalues are \(-1\), and each omitted vertex has invasion eigenvalue \(1-2\alpha<0\), proving asymptotic stability. An equilibrium without any pair cannot be stable because each missing pair invades a surviving clique of \(\ell\) unmatched vertices at rate \((1-\alpha)/[1+\alpha(\ell-1)]>0\), or at rate one if none survive. This proves the complete classification of linearly asymptotically stable equilibria.

**4. Global winner selection on the paired-balance manifold.** The potential
\[
\Phi(x)=\sum_kx_k-\frac12\sum_kx_k^2-\alpha\sum_{\{k,\ell\}\in E(G)}x_kx_\ell
\]
satisfies \(\dot\Phi=\sum_kx_k(\partial_k\Phi)^2\ge0\). Positive trajectories are bounded, so every omega-limit lies among the nonnegative equilibria. In the paired-balance manifold, the equations in Step 2 show that for \(\alpha\in(1/2,1)\) every equilibrium with paired types positive contains \(k\ge1\) pair types of **equal** abundance and no unmatched types, while every equilibrium with no paired type is a clique equilibrium on some unmatched subset or the origin. The equilibrium set is finite, hence connectedness of each omega-limit implies convergence to one equilibrium. The clique-only alternatives have strictly positive paired invasion rates and cannot attract a strictly positive paired solution. Moreover,
\[
\frac{d}{dt}\log\frac{q_i}{q_j}=(2\alpha-1)(q_i-q_j).
\]
If \(q_h(0)>q_j(0)\) for all \(j\ne h\), the ratios \(q_h/q_j\) stay strictly greater than one and increase, so convergence to a multi-pair equilibrium (which requires equal abundances) is impossible. The winning singleton must be pair \(h\). When \(s=1\), balance is unnecessary: an equilibrium containing exactly one twin is invaded by the absent twin, any clique-only equilibrium is invaded by both twins, and both twins cannot coexist at equilibrium with unmatched vertices (the opposite-sign argument above). Thus all equilibria other than the pair-only state repel some initially positive coordinate; the potential and finiteness argument force every strictly positive trajectory to the unique pair-only state.

**5. Sharp one-edge fragility.** For \(K_n\), \(H_\alpha=(1-\alpha)I+\alpha J\) has a strictly positive stable equilibrium up to but not including \(\alpha=1\). For \(K_n\) with any single edge removed, Steps 1–3 give threshold \(1/2\). The fraction of removed interactions is \(1/\binom n2\), tending to zero as \(n\to\infty\), while the threshold ratio stays \(1/2\).

## Verification
The standalone `verify.py` checks the exact subcritical equilibrium, positive definiteness on finite test graphs, the critical simplex identities, the stable pair-only state and absent-species invasion eigenvalues using rational arithmetic for 150 graph/parameter cases; it also verifies nine symbolic difference identities and illustrates unique-winner convergence in 12 numerical initial-value problems. Run `python verify.py` with Python, SymPy and SciPy. These finite tests corroborate; they do not prove the all-size theorem, which follows from Steps 1–5.

## Relationship to prior work
Mooij, Baudena, von der Heydt, Miele and Kryven (2026) establish graph-general upper and lower critical-coupling bounds, including the complete-graph upper extremizer, and investigate triangle density; their article does not state the missing-matching half-threshold, the critical neutral simplex, or exact initial-condition winner selection. Mooij and Kryven (2025) relate large-competition stable states to maximal independent sets, and give explicit critical values for complete bipartite graphs and paths. Those special graph results cover some small cases (e.g., four-cycle and three-vertex path), but do not supply the present arbitrary matching-deletion phase diagram or its one-edge large-density discontinuity. The graph-common formulas \((I+\alpha A)^{-1}\mathbf1\) and the general entropy/potential methods are established tools; the particular family-level conclusion is the claim here. No universal statement beyond this family or proof of absolute priority is asserted.

## Limitations
All interspecific competitive edges have the same strength; growth and carrying capacities are normalized. No positive-parameter heterogeneity, stochasticity, network rewiring, or finite population effects are analyzed. The explicit critical and postcritical initial-condition selection results require pair-balanced starts except in the single-deleted-edge case. Above \(\alpha=1\) there may be additional stable configurations and the classification is not claimed. External bibliographic searches are not a guarantee of absolute novelty; equivalence under another nomenclature remains possible.

## References
1. M. N. Mooij, M. Baudena, A. S. von der Heydt, L. Miele, I. Kryven, *A dynamic mechanism for prevalence of triangles in competitive networks*, arXiv:2603.17584 (first posted 18 March 2026), https://arxiv.org/abs/2603.17584.
2. M. N. Mooij and I. Kryven, *Finding large independent sets in networks using competitive dynamics*, Communications Physics **8**, 235 (2025), https://doi.org/10.1038/s42005-025-02153-7.
3. B. S. Goh, *Global stability in many-species systems*, The American Naturalist **111** (1977), 135–143.
