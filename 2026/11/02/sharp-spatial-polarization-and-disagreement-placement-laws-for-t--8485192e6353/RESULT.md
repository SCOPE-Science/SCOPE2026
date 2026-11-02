# Sharp spatial-polarization and disagreement placement laws for two finite-strength opinion anchors on a cycle

## Finding

Consider the unweighted cycle with \(N\ge4\) vertices and two equal-strength, opposite opinion anchors. Let their graph separation be \(d\in\{1,\ldots,\lfloor N/2\rfloor\}\), let their common strength be \(k>0\), and write
\[
G_d=\frac1d+\frac1{N-d}=\frac{N}{d(N-d)}.
\]
For the unique steady-state opinion vector \(x^{(d)}\), define the **local disagreement energy** and **population polarization** by
\[
E_d=\sum_{i=0}^{N-1}(x_i-x_{i+1\bmod N})^2,
\qquad
V_d=\sum_{i=0}^{N-1}(x_i-\bar x)^2,
\quad \bar x=N^{-1}\sum_i x_i.
\]
Then the exact all-parameter identities are
\[
\boxed{E_d=\frac{k^2G_d}{(k+2G_d)^2}},\qquad
\boxed{V_d=\frac{k^2(N+2G_d)}{12(k+2G_d)^2}},\qquad \bar x=\frac12.
\]
These two indices have **different sharp placement phase diagrams**. For every \(1\le d<\lfloor N/2\rfloor\),
\[
\begin{aligned}
 E_d\gtreqless E_{d+1}&\iff
 k\gtreqless K^E_d:=2\sqrt{G_dG_{d+1}},\\
 V_d\gtreqless V_{d+1}&\iff
 k\gtreqless K^V_d:=N+\sqrt{(N+2G_d)(N+2G_{d+1})}.
\end{aligned}
\]
Both threshold sequences decrease strictly as \(d\) increases. Consequently, as anchor strength increases from zero to infinity, the maximizing separation for **each** index visits *every* integer separation, starting at the largest possible separation and ending at adjacent anchors. Each switch involves two neighboring separations only; at a threshold exactly those two tie for the maximum, and away from thresholds the maximum is unique. The minimum is always attained at one of the two extreme separations. For \(J\in\{E,V\}\), it switches from adjacent anchors at small \(k\) to maximally separated anchors at large \(k\), with endpoint tie exactly at
\[
K^E_{\min}=2\sqrt{G_1G_m},\qquad
K^V_{\min}=N+\sqrt{(N+2G_1)(N+2G_m)},\quad m=\lfloor N/2\rfloor.
\]
In particular, throughout the nonempty interval
\[
2G_1<k<2(N+G_m),
\]
**adjacent anchors uniquely maximize local disagreement**, while **maximally separated anchors uniquely maximize population polarization**. Thus two natural notions of opinion divergence prescribe opposite placements on the very same homogeneous social network.

For example, with \(N=12\) and \(k=4\), the adjacent case has \((E_1,V_1)=(132/289,143/289)\), while the diametral case has \((E_6,V_6)=(12/49,38/49)\). The former uniquely maximizes \(E\) and the latter uniquely maximizes \(V\).

## Assumptions and scope

For every integer \(N\ge4\), label vertices by \(0,1,\ldots,N-1\) modulo \(N\). Every cycle edge has unit weight. Two *external signals* of immutable preferred values \(1\) and \(0\) act with the same finite strength \(k>0\) on vertices \(0\) and \(d\), respectively; all vertices, including those two, average with their cycle neighbors. Opinions evolve continuously according to
\[
\dot x_i=x_{i-1}+x_{i+1}-2x_i
+k\boldsymbol 1_{i=0}(1-x_0)-k\boldsymbol 1_{i=d}x_d.
\]
The external signals, not the two recipient vertices, are stubborn. The model has no additional innate opinion, nonlinear response, random gossip, heterogeneous weights, or endogenous graph changes. The claim concerns the deterministic equilibrium values and their across-vertex spread, not the stationary sample-path variance of a stochastic binary voter model.

## Proof

Let \(L\) be the cycle Laplacian and let \(e_i\) denote the coordinate vectors. The equilibrium equation is
\[
(L+ke_0e_0^{\mathsf T}+ke_de_d^{\mathsf T})x=ke_0.
\]
Its quadratic form is
\[
\sum_i(z_i-z_{i+1})^2+kz_0^2+kz_d^2>0
\]
for nonzero \(z\); hence the coefficient matrix is positive definite and the equilibrium exists uniquely. The same property gives exponential convergence of every trajectory.

At every vertex except \(0,d\), discrete harmonicity makes the opinion profile affine along each of the two connecting arcs. Put \(U=x_0\), \(W=x_d\), and \(\Delta=U-W\). The two unit-resistance arcs of lengths \(d\) and \(N-d\) have combined conductance \(G_d\). Their net flux at the anchored vertices gives
\[
k(1-U)=G_d\Delta=kW.
\]
Thus \(U+W=1\), \(\Delta=k/(k+2G_d)\), and the arc values interpolate linearly between \((1+\Delta)/2\) and \((1-\Delta)/2\). Averaging these two affine arc profiles gives \(\bar x=1/2\), including for even or odd arc lengths.

Each of the \(d\) edges of the first arc carries difference magnitude \(\Delta/d\), and each of the \(N-d\) edges on the other arc carries difference magnitude \(\Delta/(N-d)\). Therefore
\[
E_d=\Delta^2G_d.
\]
The exact finite-sum identity
\[
\sum_{j=0}^{\ell-1}\left(\frac j\ell-\frac12\right)^2
=\frac\ell{12}+\frac1{6\ell}
\quad(\ell\ge1)
\]
applied to each arc counts all \(N\) vertex squares correctly: one endpoint is counted twice and the other omitted, but both have equal squared deviation \(\Delta^2/4\). It gives
\[
V_d=\Delta^2\left(\frac N{12}+\frac{G_d}6\right).
\]
Substituting \(\Delta\) proves both formulas.

Now fix \(g>h>0\). Directly compare the positive square roots of the formulas for \(E(g)\), \(E(h)\): cancellation of \(\sqrt g-\sqrt h>0\) shows
\[
E(g)\gtreqless E(h)\iff k\gtreqless2\sqrt{gh}.
\]
For \(V\), set \(a=\sqrt{N+2g}\), \(b=\sqrt{N+2h}\). The identity \(2(gb-ha)=(a-b)(ab+N)\) yields
\[
V(g)\gtreqless V(h)\iff k\gtreqless N+\sqrt{(N+2g)(N+2h)}.
\]
Finally \(G_1>G_2>\cdots>G_m\). Both adjacent-threshold sequences are therefore strictly decreasing. The sign comparisons show that the values, indexed by increasing \(d\), first increase and then decrease, with at most one adjacent equality at their maximum. Each spacing is a strict maximum for an open strength interval between consecutive thresholds. Such a unimodal sequence has its minimum at an endpoint; comparing its two endpoint values gives the two displayed minimum-switch thresholds and their tie cases. For completeness, the continuous derivatives of the two formulas as functions of \(g\) have the signs of \(k-2g\) and \(k-2(N+g)\), respectively; hence for \(2G_1<k<2(N+G_m)\), \(E\) increases while \(V\) decreases across the allowed \(G_d\). This proves the simultaneous opposite placements and all asserted strictness.

## Verification

`CHECKER.py` (standard-library Python) solves the anchored cycle equilibrium from scratch by exact rational Gaussian elimination for every \(4\le N\le19\), every distinct separation, and six positive rational anchor strengths. It checks the equilibrium mean, both exact energy identities, positivity, full adjacent comparisons, the endpoint-minimum assertion, and threshold equalities numerically at their algebraic values. It also checks the \(N=12,k=4\) witness with exact fractions. An executed run returned `PASS 4391 exact-rational and threshold checks`. These finite checks verify implementation and examples; the all-integer and all-positive-real result rests on the displayed proof, not on enumeration.

## Relationship to prior work

Acemoglu, Como, Fagnani and Ozdaglar [1] study persistent opinion disagreement and derive harmonic stationary expected opinions for networks with stubborn agents; their Section 5 includes special geometries including cycles, but does not give these finite-strength, all-separation optimality thresholds. Hunter and Zaman [2] optimize influencer placements for opinion variance and demonstrate nonmonotonicity, but do not give this two-anchor cycle classification. Yi and Patterson [3] define neighbor disagreement versus global polarization and derive general Laplacian expressions, including a related Friedkin–Johnsen formulation. Their general formulas cover pointwise computation on a fixed graph but do not themselves state or prove the ordered, exact placement-switch thresholds for every cycle size and strength. Musco, Musco and Tsourakakis [4] develop broader graph-design optimization objectives rather than this exact fixed-cycle separation law. The difference between the two performance indices, not the underlying Laplacian formula, is the essential contribution here.

## Limitations

This is a deterministic linear social-dynamics model with equal cycle weights, exactly two equal-strength opposing external anchors, and a fixed graph. It is not a claim about observed social outcomes, election behavior, stochastic voter model variance, costs of changing the graph, or empirical effects of real interventions. An arbitrary-graph inverse-matrix representation of the same equilibrium is already known; historical priority for the particular all-strength phase diagram has not been independently established. External papers and search results cannot certify uniqueness of publication priority.

## References

[1] D. Acemoglu, G. Como, F. Fagnani and A. Ozdaglar, *Opinion fluctuations and disagreement in social networks*, arXiv:1009.2653, first submitted 2010-09-14, https://arxiv.org/abs/1009.2653.

[2] D. Scott Hunter and T. Zaman, *Optimizing Opinions with Stubborn Agents*, arXiv:1806.11253, first submitted 2018-06-29, https://arxiv.org/abs/1806.11253.

[3] Y. Yi and S. Patterson, *Disagreement and Polarization in Two-Party Social Networks*, arXiv:1911.11338, first submitted 2019-11-26, https://arxiv.org/abs/1911.11338.

[4] C. Musco, C. Musco and C. E. Tsourakakis, *Minimizing Polarization and Disagreement in Social Networks*, arXiv:1712.09948, first submitted 2017-12-28, https://arxiv.org/abs/1712.09948.
