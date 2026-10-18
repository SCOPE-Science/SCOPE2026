# Quasiconvex minimax attention and a sharp layer-count law in strategic multiplex consensus

## Finding

**Theorem (opinion-blind attention design).** In the strategic multiplex reporting game specified below, suppose all network layers share a strictly positive stationary distribution. For bounded but unknown private opinions, the *worst possible* equilibrium displacement of the aggregated consensus admits an exact quasiconvex reformulation and second-order-cone feasibility test. Complete elimination of displacement for every opinion profile is equivalent to a convex-hull condition on layer-specific manipulation vectors; whenever feasible, it needs at most as many active layers as agents. That bound cannot be improved in general: a family of distinct primitive layers and positive reporting costs requires **every** one of its \(n\) layers for universal neutrality, and has the exact optimal worst-case displacement

\[
\inf_{\substack{\alpha\in\Delta_n\\ |\operatorname{supp}\alpha|\le m}}
\sup_{\theta\in[0,1]^n}\left|y^*(\alpha,\theta)-\bar\theta\right|
=\frac{\delta(1-m/n)}{n+\delta+m},\qquad 1\le m\le n.
\]

Here \(\delta>0\) is an explicit reporting-cost contrast. The infimum is attained by assigning equal attention to any \(m\) active layers. No nontrivial finite experiment is used to prove this identity.

## Assumptions and scope

Let \(n\ge2\) be the number of agents, \(L\ge1\) the number of layers, and let \(W^{(\ell)}\in\mathbb R^{n\times n}\) be primitive row-stochastic matrices for \(1\le\ell\le L\). Assume they share a common normalized stationary vector \(\pi\), so that \(\pi_i>0\), \(\sum_i\pi_i=1\), and \(\pi^\top W^{(\ell)}=\pi^\top\) for every layer. Agent \(i\) has private opinion \(\theta_i\in[0,1]\) and a strictly positive quadratic reporting-cost coefficient \(c_{i\ell}>0\) on layer \(\ell\).

An attention vector \(\alpha\) belongs to the closed probability simplex \(\Delta_L=\{\alpha\ge0:\sum_{\ell}\alpha_\ell=1\}\). The original strictly positive-attention game extends continuously to this simplex because every layer is primitive. If an attention coordinate vanishes, that layer is inactive; its reports have zero influence, but still incur positive costs. Results about *strictly positive* attention are identified explicitly below.

The merged DeGroot matrix is \(C(\alpha)=\sum_\ell\alpha_\ell W^{(\ell)}\). Because every layer has stationary distribution \(\pi\), a layer-\(\ell\) report by agent \(i\) has consensus leverage \(\omega_{i\ell}=\alpha_\ell\pi_i\). Each agent chooses reports \(x_{i\ell}\in\mathbb R\) to minimize

\[
U_i(x)=\frac12\big(y(x)-\theta_i\big)^2+
\frac12\sum_{\ell=1}^L c_{i\ell}(x_{i\ell}-\theta_i)^2,
\quad y(x)=\sum_{i,\ell}\alpha_\ell\pi_i x_{i\ell}.
\]

Write \(y^*(\alpha,\theta)\) for the unique Nash-equilibrium aggregated consensus and \(\bar\theta=\sum_i\pi_i\theta_i\) for truthful consensus. The **opinion-blind risk** is

\[
\mathcal R(\alpha)=\sup_{\theta\in[0,1]^n}
\big|y^*(\alpha,\theta)-\bar\theta\big|.
\]

Define entirely from the known stationary centralities and costs

\[
h_{i\ell}=\frac{\pi_i^2}{c_{i\ell}},\qquad
s_\ell=\sum_{i=1}^n h_{i\ell},\qquad
a_{i\ell}=h_{i\ell}-\pi_i s_\ell,
\]

and let \(A=(a_{i\ell})\in\mathbb R^{n\times L}\), with columns \(a_\ell\). Each column satisfies \(\sum_i a_{i\ell}=0\).

**Exact risk and quasiconvexity.** For every \(\alpha\in\Delta_L\),

\[
\boxed{\mathcal R(\alpha)=
\frac{\|A(\alpha_1^2,\ldots,\alpha_L^2)^\top\|_1}
{2\big(1+\sum_\ell s_\ell\alpha_\ell^2\big)}.}
\]

There is a bijective change of simplex coordinates

\[
z_\ell=\frac{\alpha_\ell^2}{\sum_j\alpha_j^2},\qquad
\alpha_\ell=\frac{\sqrt{z_\ell}}{\sum_j\sqrt{z_j}}.
\]

In the new coordinates,

\[
\boxed{\mathcal R(z)=\frac{\|Az\|_1}{2G(z)},\qquad
G(z)=\left(\sum_\ell\sqrt{z_\ell}\right)^2+\sum_\ell s_\ell z_\ell.}
\]

The function \(G\) is strictly positive and concave on \(\Delta_L\), while \(\|Az\|_1\) is convex. Consequently every risk sublevel set is convex in \(z\). The global infimum is attained and can be calculated to an arbitrary prescribed numerical tolerance by bisection over second-order-cone feasibility problems, without local minimization of the original nonconvex attention expression.

**Exact conic feasibility.** Fix a nonnegative candidate bound \(\tau\). There exists an attention vector with \(\mathcal R\le\tau\) if and only if there exist real variables \(z_\ell,r_i,u_{\ell m}\) satisfying

\[
\begin{aligned}
&z\ge0,\quad\sum_\ell z_\ell=1,\quad r_i\ge (Az)_i,\quad r_i\ge -(Az)_i,\\
&u_{\ell m}\ge0,\quad
\left\|\big(2u_{\ell m},z_\ell-z_m\big)\right\|_2\le z_\ell+z_m\quad(\ell<m),\\
&\sum_i r_i\le2\tau\left(\sum_\ell(1+s_\ell)z_\ell+2\sum_{\ell<m}u_{\ell m}\right).
\end{aligned}
\]

Every constraint is affine or second-order-conic for a fixed \(\tau\). The formula remains valid at \(\tau=0\) and at boundary attention vectors.

**Universal neutrality and support.** There exists \(\alpha\in\Delta_L\) with \(\mathcal R(\alpha)=0\) precisely when

\[
\boxed{0\in\operatorname{conv}\{a_1,\ldots,a_L\}.}
\]

If this holds, one can choose \(\alpha\) supported on at most \(n\) layers. Strictly positive attention on *all* \(L\) layers gives zero risk if and only if \(0\) belongs to the relative interior of that convex hull. These are exact, opinion-independent design tests involving only observed centralities and reporting costs.

**Sharpness with genuinely distinct layers.** Fix \(n=L\ge2\) and \(\delta>0\). Let \(P_\ell\), for \(1\le\ell\le n\), be the distinct cyclic-shift permutation matrices on \(n\) agents, \(J\) the all-ones matrix, and

\[
W^{(\ell)}=\frac12P_\ell+\frac{1}{2n}J,
\qquad
\pi_i=\frac1n,
\qquad
c_{i\ell}=\frac{1}{n^2(1+\delta\mathbf1_{\{i=\ell\}})}.
\]

Each \(W^{(\ell)}\) is strictly positive, primitive, and doubly stochastic, and the layers are distinct. In this family, a layer is particularly cheap for one corresponding agent, with a different agent advantaged in each layer. For every integer \(1\le m\le n\), the sharp support-constrained formula displayed in the first paragraph holds, and all minimizing \(m\)-layer attentions are uniform on their support. In particular, universal neutrality requires exactly \(n\) active layers, attained uniquely at \(\alpha_\ell=1/n\) for every \(\ell\).

For illustration, when \(n=3\) and \(\delta=1\), the best worst-case risks using respectively one, two, or three layers are exactly \(2/15\), \(1/18\), and \(0\).

## Proof

**1. Derive the equilibrium independently.** For any active or inactive layer, differentiating \(U_i\) with respect to the report \(x_{i\ell}\) yields the first-order condition

\[
c_{i\ell}(x_{i\ell}-\theta_i)+\alpha_\ell\pi_i(y-\theta_i)=0.
\]

The Hessian in each agent's reports is the positive-definite diagonal matrix \(\operatorname{diag}(c_{i1},\ldots,c_{iL})\) plus the positive-semidefinite rank-one matrix with entries \(\omega_{i\ell}\omega_{im}\). Therefore the first-order conditions characterize each agent's unique best response. They give

\[
x_{i\ell}=\theta_i+\frac{\alpha_\ell\pi_i}{c_{i\ell}}(\theta_i-y).
\]

Substitution into the leverage-weighted aggregate produces

\[
(1+K)y=\bar\theta+\sum_iK_i\theta_i,
\quad K_i=\sum_\ell h_{i\ell}\alpha_\ell^2,
\quad K=\sum_iK_i=\sum_\ell s_\ell\alpha_\ell^2.
\]

Because \(1+K>0\), this has a unique solution. Defining the reports from that solution satisfies every first-order condition and the consensus equation, proving Nash existence and uniqueness also on the closed simplex. This calculation reproduces the motivating article's tilted-consensus identity, but does not assert novelty for that identity.

**2. Compute the exact bounded-opinion maximum.** Subtract \(\bar\theta\) from the equilibrium consensus:

\[
y^*-\bar\theta
=\frac{\sum_i(K_i-\pi_iK)\theta_i}{1+K}
=\frac{\sum_i\big(\sum_\ell a_{i\ell}\alpha_\ell^2\big)\theta_i}{1+K}.
\]

Let \(v_i=\sum_\ell a_{i\ell}\alpha_\ell^2\). Then \(\sum_i v_i=0\). A linear function on \([0,1]^n\) reaches its extreme at a vertex; its largest positive value is \(\sum_{v_i>0}v_i\), and the absolute minimum is its negative counterpart. Since the positive and negative parts have equal total mass,

\[
\sup_{\theta\in[0,1]^n}\big|\sum_i v_i\theta_i\big|
=\frac12\sum_i|v_i|.
\]

This proves the exact formula for \(\mathcal R(\alpha)\). Note that the maximum is attained by extreme opinions, not merely approximated by them.

**3. Transform to convex risk sublevels.** Since \(\sum_\ell\alpha_\ell=1\), the transformation between \(\alpha\) and \(z\) displayed above is bijective, including boundaries. Moreover

\[
\alpha_\ell^2=\frac{z_\ell}{(\sum_j\sqrt{z_j})^2}.
\]

Multiplying numerator and denominator of the exact risk by \((\sum_j\sqrt{z_j})^2\) gives the expression involving \(G\). Expand

\[
G(z)=\sum_\ell(1+s_\ell)z_\ell+
2\sum_{\ell<m}\sqrt{z_\ell z_m}.
\]

The geometric mean \(\sqrt{uv}\) is concave on the nonnegative quadrant, hence \(G\) is concave. Since \(\sum z_\ell=1\), \(G(z)\ge1\). For every \(\tau\ge0\),

\[
\{z:\mathcal R(z)\le\tau\}
=\{z:\|Az\|_1-2\tau G(z)\le0\},
\]

an intersection of the simplex with a sublevel set of a convex function. Thus the transformed problem is quasiconvex. Continuity on the compact simplex proves existence of a global minimizer.

**4. Establish exact second-order-conic feasibility.** For each \(\ell<m\),

\[
\big\|(2u_{\ell m},z_\ell-z_m)\big\|_2\le z_\ell+z_m
\quad\Longleftrightarrow\quad
u_{\ell m}^2\le z_\ell z_m
\]

for nonnegative \(z_\ell,z_m,u_{\ell m}\), where the symbol on the right is the same auxiliary variable \(u_{\ell m}\). Thus a conic feasible point necessarily has \(u_{\ell m}\le\sqrt{z_\ell z_m}\), and \(r_i\ge|(Az)_i|\). The last constraint then implies \(\|Az\|_1\le2\tau G(z)\). Conversely, if this inequality holds, choose \(r_i=|(Az)_i|\) and \(u_{\ell m}=\sqrt{z_\ell z_m}\). All cone and linear constraints hold. This proves both implications and shows that feasibility, not a heuristic local optimization, characterizes the global threshold.

**5. Characterize full cancellation and sparse designs.** Because \(G>0\), zero risk is equivalent to \(Az=0\). Together with \(z\in\Delta_L\), this is exactly the statement that zero lies in the convex hull of the columns of \(A\). Every column lies in the \((n-1)\)-dimensional hyperplane of zero-sum vectors, so Carathéodory's theorem reduces any convex representation of zero to at most \(n\) columns. The inverse coordinate transform preserves support. Strictly positive attention corresponds to strictly positive barycentric coefficients on *every* listed column. Such coefficients exist exactly when zero belongs to the relative interior of the convex hull: a positive combination lies in that relative interior, and conversely, a relative-interior point can be written as a small uniform positive combination of all columns plus a residual convex combination.

**6. Prove sharpness and the complete channel-budget frontier.** In the cyclic-shift family, direct substitution gives

\[
h_{i\ell}=1+\delta\mathbf1_{\{i=\ell\}},\quad
s_\ell=n+\delta,\quad
a_{i\ell}=\delta\left(\mathbf1_{\{i=\ell\}}-\frac1n\right).
\]

Consequently, for \(z\in\Delta_n\),

\[
\mathcal R(z)=\frac{\delta\sum_{i=1}^n|z_i-1/n|}
{2\left[(\sum_i\sqrt{z_i})^2+n+\delta\right]}.
\]

If at most \(m\) coordinates are nonzero, the total variation distance from uniform satisfies

\[
\sum_{i=1}^n|z_i-1/n|\ge2(1-m/n).
\]

Also Cauchy--Schwarz yields \((\sum_i\sqrt{z_i})^2\le m\sum_i z_i=m\). Thus

\[
\mathcal R(z)\ge\frac{\delta(1-m/n)}{n+\delta+m}.
\]

Take any \(m\) coordinates equal to \(1/m\) and the rest zero. Both inequalities are equalities, so the bound is sharp and gives uniform attention on the same \(m\) layers. Equality in Cauchy--Schwarz requires equal positive \(z_i\) on the support; for \(m=n\), vanishing numerator likewise forces uniform \(z\). Thus no smaller number of layers can yield zero risk, while the \(n\)-layer uniform attention does. All cases \(n\ge2\), \(\delta>0\), and \(1\le m\le n\) are covered.

## Verification

The standalone standard-library program `verify.py` implements exact rational arithmetic. It independently checks the equilibrium first-order equations and aggregation identity against all binary opinion vertices in small heterogeneous examples; compares the original worst-case formula with the transformed one; produces equality witnesses for the rotated second-order-cone constraints; and checks the layer-budget expression for \(n=2,\ldots,7\), three reporting-cost contrasts, and every admissible support budget. It also compares \(534\) rational attention perturbations with the theoretical lower bound. Run `python verify.py` from the directory containing this result. Every check completed successfully in the recorded run.

These finite calculations confirm identities on tested instances only. Universal quasiconvexity, the conic equivalence, the convex-hull classification, and the sharp layer-count frontier follow from the arguments above, not from enumeration.

## Relationship to prior work

The model, consensus-leverage decomposition, unique Nash equilibrium, and fixed-opinion distortion identity are established in Ebrahimi and Franceschetti (2026), especially Lemma 3.1 and Theorems 4.1--4.2. Their Theorem 7.1 solves attention optimization for a **specified** opinion vector when layers share a stationary distribution; their Theorems 7.2--7.3 treat general layers with opinion-specific gradients and polynomial root methods. Those results are assumed, acknowledged, and independently reconstructed at the points used here. The question answered here is different: minimize the **worst possible** distortion simultaneously over every bounded unknown opinion vector, for any number of agents and layers. The convex-sublevel characterization, explicit second-order-cone feasibility test, complete opinion-independent neutrality condition, and sharp layer-count frontier are not stated in the inspected motivating work.

Jalan and Papachristou (2025/2026) study strategic participants within a Friedkin--Johnsen network, including equilibrium and manipulation-detection questions. Their payoff, aggregation mechanism, and optimization target differ; a fixed common-centrality multiplex attention minimax theorem is not among the inspected claims. Shiu and Naghizadeh (2026) study ordinary truthful multiplex coordination and consensus stability, without agents strategically misreporting their initial values. General quasiconvex fractional optimization and second-order-conic formulations are standard tools, as in Boyd and Vandenberghe; no novelty is claimed for these mathematical tools outside this particular strategic-aggregation design problem.

## Limitations

All layers must have the same strictly positive stationary vector. The exact conic minimax reduction need not hold for re-centralizing attention changes when the layer stationary vectors differ. The risk is a worst-case displacement over private opinions in \([0,1]^n\), not over a variance-constrained set, and it measures consensus displacement rather than welfare, polarization, or identification of manipulators. Channel-budget optima allowing absent layers are stated on the closed simplex; if every layer is required to carry strictly positive attention, the global infimum equals the closed-simplex optimum, but a boundary optimum may not be attained. The sharp cost-contrast family is an explicit structural witness, not a claim that every multiplex network requires \(n\) layers. Specialized literature might contain broader implication-equivalent results.

## References

1. Raman Ebrahimi and Massimo Franceschetti, *Strategic Opinion Manipulation in Multiplex Networks*, arXiv:2609.22524, first submitted September 18, 2026. https://arxiv.org/abs/2609.22524 ; full-text HTML https://arxiv.org/html/2609.22524 .
2. Akhil Jalan and Marios Papachristou, *Opinion Dynamics with Multiple Adversaries*, arXiv:2502.15931, first submitted February 21, 2025; version 2 January 21, 2026. https://arxiv.org/html/2502.15931v2 .
3. Ruey-An Shiu and Parinaz Naghizadeh, *Coordination Games on Multiplex Networks: Consensus, Convergence, and Stability of Opinion Dynamics*, arXiv:2603.07633, first submitted March 8, 2026. https://arxiv.org/html/2603.07633v3 .
4. Stephen Boyd and Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press, 2004, for general convex and quasiconvex optimization methods. https://stanford.edu/~boyd/cvxbook/ .
