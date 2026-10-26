# Zero-spine optimal conductance design for clique books

## Finding

Let \(m,s\ge2\) be integers and let \(G_{m,s}=K_2\vee (mK_s)\) be the **two-hub clique book**: two hub vertices are adjacent, there are \(m\) disjoint copies of the complete graph on \(s\) vertices, and every outer vertex is adjacent to both hubs. Its order is \(N=ms+2\). Assign an arbitrary nonnegative conductance \(w_e\) to every allowed edge, with \(\sum_e w_e=B>0\), and let \(\mathcal K(w)=\sum_{i<j}R_{ij}(w)\) denote the unordered-pair Kirchhoff index. Interpret \(\mathcal K(w)=+\infty\) if the positive-conductance support is disconnected.

**Theorem.** The unique global minimizer, even among asymmetric allocations, puts **zero conductance on the existing hub-to-hub spine edge** and strictly positive conductance on every other edge. All \(2ms\) hub-to-outer edges have a common conductance \(a_*\), and all \(m\binom{s}{2}\) edges internal to the leaf cliques have a common conductance \(b_*\). Set

\[
A=\frac{N(m-1)}{2}+1+\frac{N}{ms},\qquad
U=\sqrt{m(s+1)A},\qquad
V=m(s-1)\sqrt{\frac N2},\qquad T=U+V.
\]

Then the unique minimizer and its exact value are

\[
a_*=\frac B T\sqrt{\frac{A}{m(s+1)}},\qquad
b_*=\frac B{sT}\left(\sqrt{2N}-2\sqrt{\frac{A}{m(s+1)}}\right),\qquad
w_{\mathrm{spine}}^*=0,
\]

\[
\boxed{\min_{\sum_e w_e=B}\mathcal K(w)=\frac{T^2}{B}.}
\]

The formula for \(b_*\) is strictly positive throughout the asserted parameter range. In particular, deleting the spine is not an imposed sparsity condition: it is a consequence of optimal resource allocation under a linear conductance budget.

## Assumptions and scope

Graphs are finite, undirected, simple, with integer \(m,s\ge2\). All available edges have identical cost per unit conductance; their nonnegative weights may be chosen independently. The graph is required to remain electrically connected. Resistances are defined using the ordinary undirected weighted graph Laplacian and its Moore–Penrose inverse. The optimization concerns the **sum of effective resistances between every unordered vertex pair**, not the algebraic connectivity, the largest resistance, or a fixed-leader coherence functional. The constraint is an exact budget \(B>0\); because increasing a positive conductance strictly reduces the objective, the inequality-budget and exact-budget formulations have the same minimizers.

## Proof

**1. Global uniqueness and symmetry.** Put \(J=\mathbf1\mathbf1^{\mathsf T}\). On the convex set of connected nonnegative conductances the matrix \(L(w)+J/N\) is positive definite, and

\[
\mathcal K(w)=N\bigl(\operatorname{tr}(L(w)+J/N)^{-1}-1\bigr).
\]

For positive-definite matrices, the function \(X\mapsto\operatorname{tr}(X^{-1})\) is strictly convex: its second directional derivative in a nonzero symmetric direction \(H\) is \(2\operatorname{tr}(X^{-1}HX^{-1}HX^{-1})>0\). Here the map from edge weights to \(L(w)\) is injective, because each distinct simple-graph edge is determined by its own off-diagonal Laplacian entry. Thus \(\mathcal K\) is strictly convex in the conductance vector on the connected domain. It blows up when the support approaches disconnection. Consequently its minimum on the budget simplex exists, is finite, and is unique. The graph automorphism group swaps hubs and permutes the \(m\) cliques and vertices inside them; uniqueness forces the minimizer to be constant on the three edge orbits. Let \(a\) be the weight on each hub-to-outer edge, \(b\) the weight on each within-clique edge, and \(c\) the weight on the spine.

**2. Exact spectrum.** The weighted Laplacian splits orthogonally into: constants; a hub-antisymmetric direction; a hub-versus-all-leaves direction; \(m-1\) leaf-block contrasts; and \(m(s-1)\) within-block contrasts. Their respective eigenvalues are

\[
0\ (1),\qquad ms a+2c\ (1),\qquad Na\ (1),\qquad 2a\ (m-1),\qquad 2a+sb\ (m(s-1)),
\]

where parenthesized numbers indicate multiplicities. Therefore

\[
\mathcal K(a,b,c)=\frac{N}{ms a+2c}+\frac1a+\frac{N(m-1)}{2a}+\frac{Nm(s-1)}{2a+sb},
\]

with resource constraint

\[
B=c+2ms a+\frac{ms(s-1)}2 b.
\]

The connected finite-objective region necessarily has \(a>0\) and satisfies the other nonnegativity constraints.

**3. Convex three-variable allocation problem.** Introduce

\[
x=ms a+2c,\qquad y=2a+sb,\qquad A_0=\frac{N(m-1)}2+1.
\]

The objective, budget and nonnegative-edge restrictions become

\[
\begin{aligned}
&\min_{x,y,a>0}\quad \frac N x+\frac{Nm(s-1)}y+\frac{A_0}a,\\
&\text{subject to}\quad
\frac x2+\frac{m(s-1)}2y+\frac{m(s+2)}2a=B,\\
&x\ge ms a,\qquad y\ge2a.
\end{aligned}
\]

This problem is strictly convex and admits strict feasible points. Suppose its first inequality is active and its second strict. Then \(x=ms a\), the budget becomes \(m(s+1)a+m(s-1)y/2=B\), and the objective becomes

\[
\frac{A}{a}+\frac{Nm(s-1)}y,
\qquad A=A_0+\frac{N}{ms}.
\]

The Cauchy–Schwarz inequality for these two positive resource allocations gives the sharp minimum \(T^2/B\), attained uniquely at

\[
a_*=\frac B T\sqrt{\frac A{m(s+1)}},\qquad
y_*=\frac B T\sqrt{2N}.
\]

**4. The omitted-constraint and spine-deletion certificate.** It remains to prove that this boundary solution is feasible and globally optimal in the original *three-variable* problem rather than only the restricted face. Its ratio is

\[
\rho=\frac{y_*}{a_*}=\sqrt{\frac{2Nm(s+1)}A}.
\]

For every \(m,s\ge2\),

\[
\boxed{2<\rho<ms.}
\]

For the first inequality, \(\rho^2>4\) is equivalent to

\[
N(ms+1)>2+\frac{2N}{ms},
\]

which holds because \(ms\ge4\) and \(N=ms+2\). For the second, multiplying the desired inequality \(2Nm(s+1)<m^2s^2 A\) by \(2\) and subtracting its left side from its right side gives

\[
Nm\bigl(ms^2(m-1)-2s-4\bigr)+2m^2s^2>0.
\]

Indeed \(ms^2(m-1)-2s-4\ge 2s^2-2s-4=2(s-2)(s+1)\ge0\), while the remaining term is strictly positive.

The first strict inequality gives \(y_*>2a_*\), hence \(b_*=(y_*-2a_*)/s>0\). The second gives the strict positivity of the Kuhn–Tucker multiplier \(\mu\) of the active constraint \(ms a-x\le0\): choosing

\[
\lambda=\frac{2N}{y_*^2},\qquad
\mu=\frac{N}{y_*^2}-\frac{N}{m^2s^2a_*^2}>0,
\]

and the other inequality multiplier equal to zero satisfies all three stationarity equations and complementary slackness. For example stationarity in \(x\) says \(-N/x^2+\lambda/2-\mu=0\), that in \(y\) says \(-Nm(s-1)/y^2+\lambda m(s-1)/2=0\), and that in \(a\) follows from the two-variable equality-constrained optimum. Convexity makes these conditions sufficient for global optimality; strict convexity makes the solution unique. Since \(\mu>0\), the resource constraint \(x\ge ms a\) is necessarily active at the unique optimum: \(c=(x-ms a)/2=0\). This establishes the theorem for the *unrestricted* graph weights through Step 1.

## Verification

The companion `verify.py` directly assembles the Laplacian from all edge classes; it does not assume the displayed spectral factorization when calculating numerical eigenvalues or inverse traces. It checks 30 integer graph families, 10 exact symbolic characteristic-polynomial identities, 3,000 random nonsymmetric competing edge budgets, and two exact rational inverse-trace identities. Its recorded standard output is `verification_output.txt`. These are supplementary finite checks; the proof above establishes the claim for **all** allowed integers and positive budgets. The positivity inequalities and multipliers in Step 4 are the crucial infinite-family certificate.

## Relationship to prior work

Ghosh, Boyd and Saberi formulate minimization of total network effective resistance under a linear conductance budget as a convex problem, give general optimality criteria, and solve examples including trees, wheels and two-clique bridge barbells. A bridge barbell necessarily keeps the bridge conductance positive and is not the present join-of-cliques graph. Their methods support the approach but their inspected explicit examples do not state this theorem. Johnson and Chertkov study optimizing power networks with line-size budgets and subsequently use nonconvex sparsity encouragement; in contrast, the present spine deletion occurs **without** a sparsity penalty. Ellens and collaborators study effective graph resistance and optimize unweighted topologies under fixed order/diameter or edge addition, rather than a joint budget over individual edge conductances. The distinctions concern the object, budget and optimality statement—not merely different terminology.

Related statements concerning conductance-optimized **single-hub** clique windmills and fastest-mixing **two-hub** books address different host graphs or a different objective. A single universal hub cannot have a hub-to-hub spine edge; a two-hub spectral-gap optimum does not imply a Kirchhoff-index optimum. The indexed-search comparison found no theorem implying the formula and unique zero-spine allocation stated here, but search absence is not proof of novelty.

## Limitations

The theorem assumes two hubs, identical leaf-clique sizes at least two, at least two leaf cliques, equal unit costs per conductance, and the sum-of-all-pair-resistances objective. It does not cover weighted costs, heterogeneous petals, nonlinear network costs, directed graphs, or fixed-edge-count rather than conductance-budget design. Direct inspection of selected primary literature and indexed mathematical records does not exclude a specialized unindexed or differently formulated prior proof. The finite verification checks are not infinite certification. Independent external mathematical validation has not been performed.

## References

1. J. K. Johnson and M. Chertkov, *A Majorization-Minimization Approach to Design of Power Transmission Networks*, first publicly submitted 2010-04-13, arXiv:1004.2285, https://arxiv.org/abs/1004.2285.
2. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66, DOI:10.1137/050645452; lawful full text https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf. An earlier shorter proceedings version appeared in July 2006.
3. W. Ellens, F. M. Spieksma, P. Van Mieghem, A. Jamakovic and R. E. Kooij, *Effective graph resistance*, Linear Algebra and its Applications 435 (2011), 2491–2506, DOI:10.1016/j.laa.2011.02.024; lawful full text https://www.nas.ewi.tudelft.nl/people/Piet/papers/LAA_2011_EffectiveResistance.pdf.
