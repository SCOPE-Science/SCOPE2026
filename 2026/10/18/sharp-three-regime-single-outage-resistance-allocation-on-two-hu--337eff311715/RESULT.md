# Sharp three-regime single-outage resistance allocation on two-hub networks

## Finding
For every integer \(m\ge3\), a total conductance budget \(B>0\), and an exceptional-route unit price \(t>0\), consider the complete bipartite graph \(K_{2,m}\). Each of its \(m\) degree-two vertices supplies a length-two path between the same two hubs. The two edges on one distinguished path cost \(t\) per unit conductance, and the remaining \(2(m-1)\) edges cost one. Independently allocate positive edge conductances under the exact budget constraint.

For each edge \(e=uv\), delete \(e\) without redesigning the remaining network and measure the effective resistance between \(u\) and \(v\). Minimize the maximum of these \(2m\) failure-specific resistances. A **globally optimal allocation over all independent edge choices** has a common conductance \(a_*\) on every ordinary edge and a common conductance \(b_*\) on the two exceptional edges.

Write \(r_*=b_*/a_*\), and define the prices
\[
t_-(m)=\frac{2(m-1)}{m^2-3},\qquad t_+(m)=\frac{(m-1)^2}{2}.
\]
Then the unique optimal ratio **within hub-symmetric, ordinary-path-exchangeable allocations** is
\[
r_* = \begin{cases}
-(m-2)+\sqrt{\dfrac{2(m-1)}{t}-2(m-2)},&0<t<t_-(m),\\[5pt]
1,&t_-(m)\le t\le t_+(m),\\[5pt]
\dfrac{m-1}{\sqrt{2t}},&t>t_+(m).
\end{cases}
\]
The globally optimal edge values and the unrestricted minimum objective are
\[
a_* = \frac{B}{2(m-1+t r_*)},\qquad b_*=r_*a_*,
\]
\[
D_* = \frac{2(m-1+t r_*)}{B}\max\left\{1+\frac{2}{m-2+r_*},\;\frac1{r_*}+\frac2{m-1}\right\}.
\]
In particular, unequal conductance prices throughout the entire interval \(t_-(m)\le t\le t_+(m)\) still result in **exactly equal optimal conductances** on every edge. The price thresholds satisfy \(t_-(m)\sim2/m\) and \(t_+(m)\sim m^2/2\), so this equal-allocation plateau spans an increasing multiplicative price range. All globally optimal values are given above; no uniqueness claim is made for potentially asymmetric optimizers.

## Assumptions and scope
The undirected simple graph has hubs \(u,v\) and intermediate vertices \(z_1,\ldots,z_m\), with edges \(uz_i,vz_i\). All conductances are positive and the expenditure is exactly \(B\), with both edges incident to \(z_m\) priced \(t\). No conductance is reallocated following failure of any single edge. For positive weights the remaining graph is connected when \(m\ge2\), so every specified resistance is finite. A zero-weight edge in any one path forces an infinite objective under the natural extended-value convention: deleting its mate isolates that path's intermediate vertex. Thus allowing nonnegative design variables instead gives the same finite optimum.

Effective resistance is the voltage difference resulting from unit current injection at one specified terminal and removal at the other. The performance measure is \(D(w)=\max_{e=xy}R_{xy}(G(w)-e)\). This is not intact-network edge resistance, the sum of all pairwise resistances, or an uncertainty-averaged loss.

## Proof
**1. Global symmetry reduction.** For a fixed failed edge and prescribed terminal current, Thomson's minimum-energy principle represents its resistance as
\[
R_{xy}(G(w)-e)=\min_{f:\,\partial f=\mathbf e_x-\mathbf e_y,\ f_e=0}\sum_{d\ne e}\frac{f_d^2}{w_d}.
\]
The perspective function \((f_d,w_d)\mapsto f_d^2/w_d\) is jointly convex for positive \(w_d\). Partial minimization over an affine flow constraint preserves convexity in \(w\). Consequently every failure-specific resistance, and their finite maximum \(D(w)\), is convex. It is invariant under permutations of the \(m-1\) ordinary paths and interchange of the hubs. Averaging any feasible allocation over this finite cost-preserving automorphism group cannot increase \(D\). Hence a global minimizer exists among the allocations with a common ordinary conductance \(a>0\) and common exceptional conductance \(b>0\), even though the original edge weights vary independently. Existence follows from compactness of the closed cost simplex and divergence of the objective at its boundary.

**2. Exact outage resistances.** After failure of an ordinary-path edge, the remaining half of that path has resistance \(1/a\). Between the hubs, the other \(m-2\) ordinary paths and the exceptional path are parallel length-two paths of conductances \(a/2\) and \(b/2\), respectively. Series/parallel reduction gives
\[
D_{\rm ordinary}=\frac1a+\frac{2}{(m-2)a+b}.
\]
Similarly failure of an exceptional-path edge gives
\[
D_{\rm exceptional}=\frac1b+\frac{2}{(m-1)a}.
\]
Set \(r=b/a>0\). Budget saturation gives \(a=B/[2(m-1+tr)]\). Dividing both outage expressions by \(1/a\), their difference is
\[
\left(1+\frac{2}{m-2+r}\right)-\left(\frac1r+\frac{2}{m-1}\right)
=(r-1)\left(\frac1r-\frac{2}{(m-1)(m-2+r)}\right).
\]
The parenthesis is strictly positive for \(m\ge3\), because \((m-1)(m-2+r)-2r=(m-1)(m-2)+(m-3)r>0\). Thus the ordinary-path failure dominates exactly for \(r\ge1\), and exceptional-path failure dominates exactly for \(r\le1\).

**3. Minimization on both sides.** Suppress the positive factor \(2/B\). For \(r\ge1\), minimize
\[
F_>(r)=(m-1+tr)\left(1+\frac2{m-2+r}\right).
\]
Its derivative has the sign of
\[
t\left[(m-2+r)^2+2(m-2)\right]-2(m-1),
\]
a strictly increasing function of \(r\). Its unique stationary point lies at \(r>1\) exactly when \(t<t_-(m)\), and that point is the first displayed branch of \(r_*\).

For \(0<r\le1\), minimize
\[
F_<(r)=(m-1+tr)\left(\frac1r+\frac2{m-1}\right).
\]
Its derivative is \(-(m-1)/r^2+2t/(m-1)\), strictly increasing in \(r\). Its stationary point lies below one exactly when \(t>t_+(m)\), yielding the third branch of \(r_*\). When neither strict condition holds, the derivatives point toward the joining point \(r=1\) on their respective domains, giving the middle branch. Each branch has a unique minimizer, and the global minimum is attained by the stated \(r_*\), including both price thresholds. Substitution into the budget and resistance expressions proves the formulas.

**4. Width of the plateau.** Direct expansion gives \(t_-(m)\sim2/m\) and \(t_+(m)\sim m^2/2\). Hence \(t_+(m)/t_-(m)\sim m^3/4\). For each fixed \(m\), both thresholds are positive and \(t_-<t_+\) (already \(2/3<2\) at \(m=3\), with separation increasing thereafter).

## Verification
The accompanying standalone `verify.py` checks the key rational derivative/difference identities symbolically and constructs weighted graph Laplacians afresh to recompute every post-deletion terminal resistance on selected \(K_{2,m}\) instances. Its deterministic asymmetric cost-feasible competitors test the unrestricted prediction without being used as the proof. An exact example with \(m=3\), \(B=1\) has \((t,a_*,b_*,D_*)=(2/9,3/16,9/16,8)\), \((1,1/6,1/6,12)\), and \((8,1/12,1/24,36)\) in the three respective regimes.

Run `python verify.py` with Python 3, NumPy, SciPy and SymPy installed. The mathematical proof is independent of the finite numerical tests.

## Relationship to prior work
Johnson and Chertkov (2010), Sections II, III and V, formulate priced conductance network design and worst-case line-failure power-loss objectives using convex optimization, but their reported results do not give this exact \(K_{2,m}\) failure-endpoint formula or price-phase diagram. Zelazo and Bürger (2014), Sections IV and V, connect single-edge robustness margins with effective resistance but analyze stability thresholds rather than solving the present conductance-allocation problem. Suliman and Weinstein (2023), Sections 1 and 3, study minimization of **intact-network** maximum edge effective resistance via infinite Lewis weights. Deleting the measured edge first is a materially different optimization: its conductance does not directly carry current in that failure scenario, and the expressions above differ accordingly.

## Limitations
The claim is for the two-hub length-two-path family with one distinguished equal-priced route, not arbitrary theta graphs, heterogeneous costs on all paths, arbitrary multi-edge failures, or simultaneous failures. The global minimum and a globally optimal symmetric allocation are proved; uniqueness among fully asymmetric allocations is not asserted. Published and indexed comparisons reduce but cannot eliminate the possibility of equivalent unindexed prior work. No independent scientific validation has been performed.

## References
1. J. K. Johnson and M. Chertkov, *A Majorization-Minimization Approach to Design of Power Transmission Networks*, arXiv:1004.2285 (first posted 13 April 2010), especially Sections II, III, V. https://arxiv.org/abs/1004.2285
2. D. Zelazo and M. Bürger, *On the Robustness of Uncertain Consensus Networks*, arXiv:1408.4471 (first posted 19 August 2014), especially Sections IV, V. https://arxiv.org/html/1408.4471v2
3. A. Suliman and O. Weinstein, *Infinite Lewis Weights in Spectral Graph Theory*, arXiv:2302.05966 (first posted 12 February 2023), especially Sections 1, 3.3. https://arxiv.org/abs/2302.05966
4. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66, https://doi.org/10.1137/050645452 (background on total rather than failed-edge resistance).
