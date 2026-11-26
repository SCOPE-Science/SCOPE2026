# Sharp spectral cost of iid one-coordinate sketching for a summable power law

## Finding

Fix \(\rho>1\). Let \(A_\rho e_j=j^{-\rho/2}e_j\) on real \(\ell^2(\mathbb N)\). Let \(Q_L\) be the orthogonal projector onto the span of the images under \(A_\rho\) of \(L\) independent, identically distributed one-coordinate isotropic sketch vectors with a common full-support law. Write \(\mathcal E_L^{\mathrm{iid}}\) for the infimum of the expected squared Hilbert–Schmidt residual over these laws. Then

\[
\mathcal E_L^{\mathrm{iid}}\sim \frac{\rho^\rho}{\rho-1}L^{1-\rho},\qquad
\lim_{L\to\infty}\frac{\mathcal E_L^{\mathrm{iid}}}
{\inf_{\operatorname{rank} B\le L}\|A_\rho-B\|_{\mathrm{HS}}^2}=\rho^\rho.
\]

Thus optimizing the law for each budget still leaves a sharp multiplicative error penalty relative to unrestricted rank \(L\). The infimum is approachable by full-support laws but is not attained for any finite \(L\ge2\). The finite-budget optimizer used in the proof is a power-law specialization of known weighted cache placement, not a new allocation rule.

## Assumptions and scope

For a probability law \(\pi_j>0\), a sketch vector is \(\omega=\xi\pi_J^{-1/2}e_J\), where \(J\) has law \(\pi\) and \(\xi\) is an independent symmetric sign. It is isotropic in the sense that \(\mathbb E[\langle u,\omega\rangle\langle\omega,v\rangle]=\langle u,v\rangle\) for every \(u,v\in\ell^2\). The scalar product in this expectation is absolutely integrable by Cauchy–Schwarz. The sketch is finite in norm almost surely; its squared norm need not be integrable (in fact its expectation is infinite). Neither general sketches nor dependent coordinate selections are included. The budget counts draws, not distinct coordinates, and \(\rho\) is fixed as the budget increases.

## Proof

**Reduction and known allocation rule.** A sketch image is a nonzero multiple of its sampled basis vector. Thus \(Q_L\) retains exactly the sampled coordinates. By nonnegativity and independence the error is
\[
\mathcal E_L(\pi)=\mathbb E\|A_\rho-Q_L A_\rho\|_{\mathrm{HS}}^2
=\sum_{j\ge1}j^{-\rho}(1-\pi_j)^L.
\]
Up to normalizing request weights, this is the weighted miss probability for one cache slot at each of \(L\) sites with independent, identical placements. Błaszczyszyn and Giovanidis give the finite-catalogue optimization for a general coverage count; take the count to be \(L\) with probability one and the per-site budget to be one. Ji, Caire and Molisch give the corresponding truncated rule for the fixed number of independent selections in their cluster. Here the objective extends to the closed probability simplex on \(\mathbb N\); we give the argument there to also justify nonattainment in the full-support class.

Let \(L\ge2\), \(\delta=\rho/(L-1)\), and let \(t>1\) solve
\[
F(t):=\sum_{1\le j<t}[1-(j/t)^\delta]=1.
\]
The sum is continuous and strictly increasing for \(t>1\), starts at zero, and tends to infinity since each of the first \(\lfloor t/2\rfloor\) terms is at least \(1-2^{-\delta}\). Set \(m=\lceil t\rceil-1\) and \(\pi_j^*=[1-(j/t)^\delta]_+\). The summands \(f_j(p)=j^{-\rho}(1-p)^L\) are strictly convex on \([0,1]\). At positive \(\pi_j^*\), \(f_j'(\pi_j^*)=-Lt^{-\rho}\); for a zero coordinate \(f_j'(0)=-Lj^{-\rho}\ge-Lt^{-\rho}\). Hence summing the convex supporting-line inequalities gives \(\mathcal E_L(\pi)\ge\mathcal E_L(\pi^*)\) for every probability law. The derivative sums converge absolutely by \(|f'_j|\le L\) and \(\sum_j|\pi_j-\pi_j^*|\le2\). At any differing coordinate the supporting-line inequality is strict, so no full-support law attains this minimum. The full-support probabilities \((1-\eta)\pi^*+\eta(2^{-j})_{j\ge1}\) give its value in the limit \(\eta\downarrow0\) by dominated convergence. Using \(\sum_{j\le m}(j/t)^\delta=m-1\), substitution yields
\[
\mathcal E_L^{\mathrm{iid}}=(m-1)t^{-\rho}+\sum_{j>m}j^{-\rho}.
\]

**Summable power-law asymptotic.** As \(L\to\infty\), the root \(t\to\infty\) since \(F(t)\to0\) on every bounded interval for \(\delta\downarrow0\). For \(0<\delta\le1\) the concavity bound \(1-(x/t)^\delta\ge\delta(1-x/t)\) on \([0,t]\) gives \(t=O(1/\delta)\) by summing up to \(t/2\). The decreasing function \(\phi_t(x)=[1-(x/t)^\delta]_+\) satisfies
\[
0\le \int_0^t\phi_t(x)\,dx-F(t)\le\int_0^1\phi_t(x)\,dx\le\delta(1+\log t)=o(1).
\]
The final bound follows from \(1-e^{-u}\le u\) applied with \(u=\delta\log(t/x)\). The integral is \(t\delta/(1+\delta)\), so \(t\delta\to1\) and \(m\sim t\sim L/\rho\). The contribution of the retained support to the optimum miss cost is asymptotic to \(t^{1-\rho}\); that of the unretained tail is asymptotic to \(t^{1-\rho}/(\rho-1)\). Thus the leading coefficient in physical budget \(L\) is \(\rho^\rho/(\rho-1)\). The deterministic rank-\(L\) optimum is the squared-singular-value tail \(\sum_{j>L}j^{-\rho}\), by the Hilbert–Schmidt best rank approximation theorem. Dividing by its asymptotic \(L^{1-\rho}/(\rho-1)\) proves the claim.

## Verification and limits

`coupon_checker.py` in the original package supplies bounded auxiliary diagnostics for the allocation rule and the large-budget behavior. The proof above, not the diagnostics, gives the infinite-simplex and limiting results. The comparison is to unrestricted rank \(L\), not to every randomized approximation algorithm; forcing distinct selected coordinates would give a different problem.

## Relationship to prior work

- Lynch-Davies and Webb, *Sketching Outside the Hilbert Space for the Infinite-Dimensional Randomised SVD*, [arXiv:2610.31333v1](https://arxiv.org/abs/2610.31333v1), Example 2.13, give the infinite-dimensional one-coordinate isotropic framework. Saibaba and Międlar, [arXiv:2308.05814](https://arxiv.org/abs/2308.05814), Section 3.4, discuss coordinate sampling and coupon-collector obstructions in randomized low-rank approximation.
- Błaszczyszyn and Giovanidis, *Optimal Geographic Caching in Cellular Networks*, [arXiv:1409.7626](https://arxiv.org/abs/1409.7626), equations (3), (7), and (12)–(14), supply the equivalent weighted placement problem and finite-catalogue allocation with a general distribution for the number of caches. Ji, Caire and Molisch, [arXiv:1302.2168](https://arxiv.org/abs/1302.2168), Theorem 1, and [arXiv:1312.2637](https://arxiv.org/abs/1312.2637), Theorem 4, give the truncated law in independent cluster caching. Related constants of the form \(\gamma^\gamma\) appear for hit/outage scaling with a growing finite catalogue and nonsummable \(0<\gamma<1\), rather than the ratio here for fixed \(\rho>1\).
- Lee, Ji and Molisch, [arXiv:2005.05149v2](https://arxiv.org/abs/2005.05149v2), Lemma 1 and Section V, study exponential miss costs and Zipf or shifted-Zipf network throughput–outage scaling, including \(\gamma>1\). The stated order estimates there are not the sharp Hilbert–Schmidt ratio for a fixed summable infinite spectrum. The contribution claimed here is the sharp summable-spectrum comparison, not historical priority for weighted coverage, its KKT solution, or its orderwise scaling.
