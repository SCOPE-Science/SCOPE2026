# Sharp tricritical active-period threshold in temporal plant–pollinator percolation

## Finding
For the shifted-Poisson active-period, equal-Poisson-degree cavity model defined below, the change from continuous to discontinuous establishment of a viable plant–pollinator community occurs at **one exactly characterized mean active period** \(\tau_{\mathrm c}=1+\lambda_{\mathrm c}\), where \(\lambda_{\mathrm c}\) is the unique positive solution of
\[
(4\lambda-1)\sqrt{(1+\lambda)e^\lambda}=1.
\]
Numerically, \(\lambda_{\mathrm c}=0.420049608669704\ldots\), \(\tau_{\mathrm c}=1.420049608669704\ldots\), and \(z_{\mathrm c}=\sqrt{(1+\lambda_{\mathrm c})e^{\lambda_{\mathrm c}}}=1.470159219746206\ldots\).

Put \(\lambda=\tau-1\ge0\) and \(z_0(\lambda)=\sqrt{(1+\lambda)e^\lambda}\). For every \(z>0\), the nonnegative fixed points have the following complete classification (besides the ever-present zero state):

1. If \(0\le\lambda\le\lambda_{\mathrm c}\), there are no positive fixed points when \(z\le z_0(\lambda)\), and exactly one when \(z>z_0(\lambda)\).
2. If \(\lambda>\lambda_{\mathrm c}\), there is a unique fold connectivity \(z_{\mathrm s}(\lambda)\) strictly between \(1\) and \(z_0(\lambda)\). For \(z<z_{\mathrm s}\) there is no positive fixed point; at equality there is precisely one positive double fixed point; for \(z_{\mathrm s}<z<z_0\) there are exactly two distinct positive fixed points; and for \(z\ge z_0\) there is exactly one positive fixed point. In the two-positive-point regime the smaller one is repelling and the larger attracting for scalar fixed-point iteration, while the zero point is attracting. The fold is characterized without an extraneous branch by \(F(q)=q\), \(\partial_qF(q)=1\), \(q>0\).
3. On the continuous side, for fixed \(\lambda<\lambda_{\mathrm c}\) and \(z\downarrow z_0\) from above, the unique positive plant fraction satisfies
\[
q\sim\frac{4(z-z_0)}{z_0[1+z_0(1-4\lambda)]}.
\]
At exactly \(\lambda=\lambda_{\mathrm c}\), the onset has a different, square-root law:
\[
q\sim\sqrt{\frac{192}{z_{\mathrm c}(23z_{\mathrm c}^{2}+30z_{\mathrm c}+23)}}\,\sqrt{z-z_{\mathrm c}}.
\]
The viable pollinator fraction \(a\) satisfies \(a/q\longrightarrow z_0e^{-\lambda}\) at both continuous onsets (with \(z_0=z_{\mathrm c}\) at the tricritical point).

These assertions classify solutions of the **mean-field cavity equations**, not the extinction outcomes of every finite random network realization.

## Assumptions and scope
The plant and pollinator within-step degrees are independent Poisson distributions with common positive mean \(z\), so their ordinary and excess-degree generating functions are \(P=A=Q=B=\exp(z(t-1))\). The pollinator active period has shifted-Poisson generating function \(L(t)=t\exp[\lambda(t-1)]\), with \(\lambda\ge0\) and mean \(\tau=1+\lambda\). We use the normalized remaining-period generating function \(K(t)=L'(t)/L'(1)\), as required by size-biased sampling. Let \(q\) denote plant-neighbour viability, \(b\) pollinator-neighbour viability, \(p\) viable-plant fraction, and \(a\) viable-pollinator fraction.

The source's cavity equations give
\[
q=1-e^{-zb},\quad s=1-e^{-zq},\quad b=sK(s),\quad p=1-e^{-zb}=q,\quad a=L(s).
\]
Thus \(q\in[0,1]\) is a fixed point of
\[
F_{z,\lambda}(q)=1-\exp\![-zH_\lambda(1-e^{-zq})],\qquad
H_\lambda(s)=\frac{s(1+\lambda s)e^{\lambda(s-1)}}{1+\lambda}.
\]
Here \(q=0\) is always a fixed point, \(F_{z,\lambda}(1)<1\), and positive fixed points represent self-consistent positive cavity states. Attracting/repelling refers only to the scalar iteration \(q_{n+1}=F_{z,\lambda}(q_n)\), not a separately specified population-dynamical flow. At the fold, the single positive root has multiplicity two in \(F(q)-q\) and multiplier one.

## Proof
**Reduction and shape.** Substituting the specified generating functions into the degree-biased cavity equations gives the scalar map above. For \(s=1-e^{-zq}\), direct differentiation gives
\[
H_\lambda'(s)=\frac{e^{\lambda(s-1)}}{1+\lambda}
(1+3\lambda s+\lambda^2s^2),\qquad
H_\lambda''(s)=\frac{e^{\lambda(s-1)}}{1+\lambda}
(4\lambda+5\lambda^2s+\lambda^3s^2).
\]
Both are nonnegative, with \(H'\) strictly positive, and
\[
F'_{z,\lambda}(q)=z^2(1-s)H_\lambda'(s)e^{-zH_\lambda(s)}>0.
\]
Set \(\Phi(s)=\partial_s\log F'_{z,\lambda}(q(s))\). Then
\[
\Phi(s)=\frac{H''_\lambda(s)}{H'_\lambda(s)}-\frac1{1-s}-zH'_\lambda(s)
\]
and
\[
\Phi'(s)=-\frac{\lambda^2(7+6\lambda s+2\lambda^2s^2)}{(1+3\lambda s+\lambda^2s^2)^2}-\frac1{(1-s)^2}-zH''_\lambda(s)<0
\]
for \(0\le s<1\). Therefore \(F'\) first increases then decreases, or decreases throughout. The function \(G(q)=F(q)-q\) has at most two zeros in \((0,1)\): three distinct positive zeros, together with \(G(0)=0\), would force at least three roots of \(F'=1\) by Rolle's theorem, contradicting the single-peaked shape of \(F'\).

**Critical threshold.** At the origin,
\[
F'(0)=\frac{z^2e^{-\lambda}}{1+\lambda}=\left(\frac{z}{z_0(\lambda)}\right)^2,
\]
and at \(z=z_0\),
\[
\frac12F''(0)=\frac{z_0(4\lambda-1)-1}{2}.
\]
The function \((4\lambda-1)z_0(\lambda)\) is strictly increasing for \(\lambda\ge1/4\), starts at zero and eventually exceeds one; for \(\lambda<1/4\) it is negative. Hence it crosses one precisely once at \(\lambda_{\mathrm c}\). When \(\lambda\le\lambda_{\mathrm c}\) and \(z=z_0\), \(\Phi(0)\le0\), so \(F'(q)<F'(0)=1\) for all \(q>0\), and \(F(q)<q\). For every fixed \(q>0\), \(F_{z,\lambda}(q)\) increases strictly with \(z\), so \(z<z_0\) also has no positive fixed point. At \(z>z_0\), \(F'(0)>1\) and \(G(1)<0\); the shape bound proves exactly one positive root.

**Fold and all root counts.** For \(\lambda>\lambda_{\mathrm c}\) at \(z=z_0\), \(F'(0)=1\) but \(F''(0)>0\), so \(G(q)>0\) at small \(q>0\), giving exactly one positive root. Slightly below \(z_0\), \(G'(0)<0\) while \(G\) remains positive at some interior point, hence there are exactly two positive roots. For \(z\le1\) we have \(H_\lambda(s)\le s\le zq\), and \(F(q)\le zH_\lambda(s)\le z^2q\), with strict inequality for \(q>0\), hence there are no positive roots. In fact \(z_{\mathrm s}>1\) strictly: since \(\lambda>0\) and \(s\le1-e^{-z}\), the stronger uniform bound \(F(q)\le z^2K(1-e^{-z})q\) holds, with \(K(1-e^{-1})<1\) at \(z=1\); by continuity the bound is strictly below \(q\) for all \(z\) in some interval above 1. Monotonicity in \(z\) makes the set of parameter values for which \(G(q)>0\) somewhere an upper interval. Its lower endpoint is the unique \(z_{\mathrm s}\in(1,z_0)\). Compactness, \(G'(0)<0\) at this endpoint, and \(G(1)<0\) imply an interior tangency \(G(q_{\mathrm s})=G'(q_{\mathrm s})=0\). Strict single-peakedness of \(F'\) makes this positive root unique and quadratic; a larger \(z\) produces strictly positive \(G\) there and exactly two roots until \(z_0\). At \(z_0\) the near-zero negative root coalesces with zero; above \(z_0\) precisely one positive root survives. For two distinct simple roots, \(G\) crosses upward at the lower and downward at the upper; since \(F'>0\), their multipliers respectively exceed one and lie between zero and one. Zero's multiplier is \((z/z_0)^2<1\) inside the bistable wedge.

**Critical exponents.** Taylor expansion around \(q=0\) at \(z=z_0\) gives
\[
F_{z_0,\lambda}(q)-q=\frac{z_0(4\lambda-1)-1}{2}q^2+C_3q^3+O(q^4).
\]
For fixed \(\lambda<\lambda_{\mathrm c}\), the linear perturbation in \(z-z_0\) is \(2(z-z_0)q/z_0\), giving the stated linear onset by division by the positive root. At the unique tricritical parameters the quadratic term vanishes, while direct differentiation and substitution of \(4\lambda_{\mathrm c}-1=1/z_{\mathrm c}\) and \(z_{\mathrm c}^2=(1+\lambda_{\mathrm c})e^{\lambda_{\mathrm c}}\) yield
\[
C_3=-\frac{23z_{\mathrm c}^2+30z_{\mathrm c}+23}{96}<0.
\]
Balancing \(2(z-z_{\mathrm c})q/z_{\mathrm c}\) against \(C_3q^3\) proves the square-root law. Finally, \(s=1-e^{-zq}\sim z_0q\) and \(a=L(s)=se^{\lambda(s-1)}\sim z_0e^{-\lambda}q\) as the positive root tends to zero.

## Verification
Run `python check.py` with Python 3, SymPy and SciPy. The program independently differentiates the complete map to third order, compares coefficients after imposing the critical constraints, solves the defining scalar threshold and fold equations, stress-tests positive root counts and branch multipliers across several parameter regimes, and compares near-threshold roots to the two asymptotic formulae. In this package the script was executed from its actual path and all assertions passed. The tests support the algebra but do not substitute for the global shape proof. For \(\lambda=1\), numerical fold solution: \(z_{\mathrm s}\approx1.941437091795518\), \(q_{\mathrm s}\approx0.366150894283529\), compared with \(z_0=\sqrt{2e}\approx2.331643981597124\).

## Relationship to prior work
Clegg and Gross (2026), *Temporal Structure Mediates the Robustness and Collapse of Plant–Pollinator Networks*, introduce the temporal bipartite ecological model, derive its generating-function cavity equations, and numerically exhibit gradual transitions, catastrophic transitions and bistability. Those ingredients, including the phase-change phenomenon, are prior work. The present mathematical result concerns their particular equal-Poisson-degree, shifted-Poisson-period specialization: it proves the exact unique transition parameter, a global enumeration and multiplier classification of all nonzero scalar solutions, and the linear-versus-tricritical onset amplitudes. Clegg and Gross (2024/2025), *Cross-feeding creates tipping points in microbiome diversity*, analyze a related but different two-parameter microbiome dependency model with its own cusp. A cusp in that different model does not determine the constant or branch structure established here. Generic saddle-node or bifurcation normal forms likewise do not by themselves supply this model's global no-extra-root conclusion or threshold value.

## Limitations
The statement assumes equal Poisson degree distributions, independent seasonal configurations and the normalized size-biased remaining-period law; it does not cover arbitrary heterogeneous degree or season-length distributions. It characterizes fixed points of a cavity approximation, not rigorous almost-sure giant-core thresholds for arbitrary finite networks. Local attraction concerns fixed-point iteration, not an externally imposed ecological dynamical flow. No claim is made that these bifurcations are absent from all earlier literature; exact historical priority beyond the inspected references remains unverified. Fold connectivity has an implicit, uniquely determined definition, not an elementary closed form. The critical constant is specified exactly as a unique transcendental root, with decimals provided only for orientation.

## References
1. T. Clegg and T. Gross, *Temporal Structure Mediates the Robustness and Collapse of Plant–Pollinator Networks*, arXiv:2604.07347v1, first posted 2026-04-08, https://arxiv.org/html/2604.07347v1, in particular the cavity equations (12)–(16) and the Poisson/shifted-Poisson specialization.
2. T. Clegg and T. Gross, *Cross-feeding Creates Tipping Points in Microbiome Diversity*, arXiv:2412.05212v1, first posted 2024-12-06; *Proceedings of the National Academy of Sciences* 122 (2025), e2425603122, https://pmc.ncbi.nlm.nih.gov/articles/PMC12088387/.
3. M. E. J. Newman, S. H. Strogatz, and D. J. Watts, *Random graphs with arbitrary degree distributions and their applications*, *Physical Review E* 64 (2001), 026118, https://doi.org/10.1103/PhysRevE.64.026118 (generating-function background).
