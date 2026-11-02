# Sharp \(\ell_1\) stability of reciprocal access on every network

## Finding

Let \(G=(V,E)\) be any finite simple undirected graph, including disconnected graphs, and let every edge \(\{i,j\}\) have a fixed symmetric weight \(w_{ij}=w_{ji}\geq0\). Define the reciprocal-access map \(\Phi_G:\mathbb R_{\geq0}^{V}\to\mathbb R_{\geq0}^{V}\) by
\[
(\Phi_G(x))_i=x_i+\sum_{j:\{i,j\}\in E}w_{ij}\min\{x_i,x_j\}.
\]
Then \(\Phi_G\) is a bijection, and its inverse has the sharp global bound
\[
\boxed{\|\Phi_G^{-1}(a)-\Phi_G^{-1}(b)\|_1\leq\|a-b\|_1\qquad(a,b\in\mathbb R_{\geq0}^{V}).}
\]
The constant \(1\) is optimal even when \(G\) is fixed and connected and the targets are strictly positive.

A strategic consequence concerns agents with nonnegative collection choices, positive individual saturation targets \(a_i\), and utilities
\[
U_i(x)=r_i\min\{(\Phi_G(x))_i,a_i\}-c_i x_i,\qquad r_i>c_i>0.
\]
Every such reciprocal capped-linear exchange game has **exactly one pure Nash equilibrium** \(x^*(a)=\Phi_G^{-1}(a)\). For any two strictly positive target vectors, \(\|x^*(a)-x^*(b)\|_1\leq\|a-b\|_1\), independently of graph size, maximum degree, edge weights, and heterogeneous slopes and costs satisfying the stated inequalities.

## Assumptions and scope

The graph and weights are fixed when targets change. Edge contributions are received symmetrically by both endpoints and are proportional to the minimum of the endpoints' collection levels. Coordinates and weights are real; the game has continuous, not integer-constrained, collection choices. No connectedness, degree, uniform-weight, or uniform-target assumption is imposed. Agents can have distinct saturation targets, slopes, and costs. The equilibrium assertion concerns only capped-linear benefits, not arbitrary concave benefits.

## Proof

**1. Constructive surjectivity.** Fix any \(a\in\mathbb R_{\geq0}^{V}\). Initially let \(R=V\), residual targets \(h_i=a_i\), and no assigned levels. For each unassigned vertex \(i\in R\), form
\[
d_i=1+\sum_{j\in R:\{i,j\}\in E}w_{ij},\qquad \rho_i=h_i/d_i.
\]
Choose an index \(p\in R\) attaining the smallest ratio, assign \(x_p=\rho_p\), remove \(p\) from \(R\), and subtract \(w_{jp}x_p\) from \(h_j\) for every remaining neighbor \(j\). Repeat until all vertices have been assigned. Ties can be broken arbitrarily.

Every chosen level is nonnegative and the assignment order is nondecreasing. Indeed, suppose \(p\) is next with \(z=\rho_p\). By minimality, \(h_j\geq d_jz\) for each other remaining \(j\). After removing \(p\), its neighbor's new numerator and denominator satisfy \(h_j'=h_j-w_{jp}z\geq(d_j-w_{jp})z=d_j'z\), and the same inequality holds unchanged for nonneighbors. Hence every future ratio is at least \(z\). The initial ratios are nonnegative, proving the assertion inductively.

When vertex \(i\) was selected, all previously assigned neighbors had collection no larger than \(x_i\), and all later assigned neighbors have collection no smaller than \(x_i\). The residual equation \(h_i=d_ix_i\) therefore says precisely
\[
a_i=x_i+\sum_{j:\{i,j\}\in E}w_{ij}\min\{x_i,x_j\}.
\]
Thus \(\Phi_G(x)=a\) for every nonnegative target \(a\). The procedure takes \(O(|V|^2+|E|)\) arithmetic operations with straightforward residual and degree updates (and at most quadratic work for a simple graph).

**2. Sharp lower expansion.** Let \(x,y\in\mathbb R_{\geq0}^{V}\) and \(\delta_i=x_i-y_i\). On each edge \(\{i,j\}\), the function
\[
s\longmapsto\min\{y_i+s\delta_i,y_j+s\delta_j\},\quad0\leq s\leq1,
\]
is continuous and piecewise affine. Its derivative, except at finitely many tie points, is either \(\delta_i\) or \(\delta_j\). Integrating gives coefficients \(\theta_{ij}^{i},\theta_{ij}^{j}\geq0\) with \(\theta_{ij}^{i}+\theta_{ij}^{j}=1\) and
\[
\min\{x_i,x_j\}-\min\{y_i,y_j\}=\theta_{ij}^{i}\delta_i+\theta_{ij}^{j}\delta_j.
\]
Therefore the coordinate difference is
\[
(\Phi_G(x)-\Phi_G(y))_i=\left(1+\sum_{j\sim i}w_{ij}\theta_{ij}^{i}\right)\delta_i+\sum_{j\sim i}w_{ij}\theta_{ij}^{j}\delta_j.
\]
Apply the reverse triangle inequality to each coordinate and sum. The off-diagonal loss associated with each edge and endpoint exactly cancels that endpoint's additional diagonal gain, because the same weight is received at both ends. Consequently
\[
\|\Phi_G(x)-\Phi_G(y)\|_1
\geq\sum_i\left(1+\sum_{j\sim i}w_{ij}\theta_{ij}^{i}\right)|\delta_i|-\sum_i\sum_{j\sim i}w_{ij}\theta_{ij}^{j}|\delta_j|
=\sum_i|\delta_i|=\|x-y\|_1.
\]
This gives injectivity; combined with Step 1 it establishes bijectivity and the asserted inverse bound.

To see sharpness on every fixed graph, select any vertex \(p\), choose all collection coordinates strictly positive and \(x_p\) strictly larger than its neighbors' levels, and increase only \(x_p\) by \(\varepsilon>0\). All incident edge minima remain unchanged. Both the collection and access \(\ell_1\) changes are exactly \(\varepsilon\). Thus no inverse constant below \(1\) is possible, even away from the boundary of the positive cone.

**3. Equilibrium equivalence.** For fixed neighbors, agent \(i\)'s accessible amount as a function of its own contribution \(s\geq0\) is \(g_i(s)=s+\sum_{j\sim i}w_{ij}\min\{s,x_j\}\). This is continuous, strictly increasing, starts at zero, tends to infinity, and increases by at least as much as \(s\). Because \(r_i>c_i>0\), the payoff \(r_i\min\{g_i(s),a_i\}-c_is\) is strictly increasing while \(g_i(s)<a_i\) and strictly decreasing once \(g_i(s)>a_i\). Hence its unique maximizer solves \(g_i(s)=a_i\). The Nash conditions are exactly \(\Phi_G(x)=a\). Steps 1–2 give the unique equilibrium and the sharp target-to-equilibrium \(\ell_1\) bound.

## Verification

The standalone exact-rational `verify.py` checks arbitrary symmetric nonnegative weighted graphs and targets with fixed random seed. Executing `python3 verify.py` evaluates \(2240\) independent graph/target trials with three checks per trial: the \(\ell_1\) expansion, exact inversion of two observed access profiles, and exact surjectivity on an independently generated strictly positive target. It also checks sharpness on a positive two-vertex instance, symmetric stars of degrees \(3\) through \(12\), and a one-way nonreciprocal contrast. Fractions are exact, not floating approximations. These tests support but do not replace the universal proof.

To clarify why the norm is important, take a unit-weight star with \(d\geq3\) leaves. Starting from center collection \(d+3\) and leaf collections \(1\), increase each leaf's target access by \(1\) and keep the center's target unchanged. The new collections have center \(d/2+3\) and leaves \(3/2\). The inverse \(\ell_\infty\) amplification is \(d/2\), unbounded as \(d\) grows, while the \(\ell_1\) estimate is attained with equality. Thus the theorem is specifically a sharp total-adjustment guarantee, not a uniform coordinatewise nonexpansivity result.

## Relationship to prior work

Hakim, Papadimitriou, and Yannakakis (2026) introduce the reciprocal minimum-exchange contract, prove an inverse transform for complete interaction in Appendix A.1, and give an equilibrium-construction algorithm for arbitrary undirected graphs in Section 6 and Appendix C. Their graph results establish existence and Pareto optimality for general concave benefits and document failure of supermodularity and equilibrium comparability. The present result concerns a different guarantee: surjectivity and exact inverse \(\ell_1\) stability on **arbitrary symmetrically weighted networks**, plus unique and quantitatively stable equilibrium for heterogeneously saturated marginal values. Neither the graph-construction theorem nor the complete-graph inverse formula asserts this network-wide inverse norm bound. Graph equilibrium existence by itself is not claimed as new.

Earlier data-exchange market formulations of Bhaskara et al. (2024) and Akrami et al. (2024) use different fairness, utility-balancing, or coalition-stability models. Their available abstracts do not establish coverage of the specific reciprocal-min access map's sharp inverse inequality. The priority comparison is not an assertion that the complete texts of those distinct models were exhaustively excluded.

## Limitations

The proof relies on symmetric contributions \(w_{ij}\min\{x_i,x_j\}\) appearing in **both** endpoint access totals. It does not establish the same \(\ell_1\) guarantee for directed or asymmetrically weighted transfers. The star calculation shows that no graph-independent \(\ell_\infty\) inverse Lipschitz factor follows. Existence and uniqueness of equilibria for arbitrary nonlinear concave benefits, discrete collection quantities, and strategic manipulation are outside the claim. The result is mathematically proven and computationally spot-checked but has not received independent external review; earlier unindexed or differently named formulations remain a possible priority risk.

## References

1. R. Hakim, C. Papadimitriou, M. Yannakakis, *Fair Data-Exchange Mechanisms*, arXiv:2602.11417 (first public February 11, 2026), https://arxiv.org/abs/2602.11417. Material considered: Sections 2, 6, Appendix A.1, and Appendix C.
2. A. Bhaskara et al., *Data Exchange Markets via Utility Balancing*, arXiv:2401.13053 (2024), https://arxiv.org/abs/2401.13053 (contextual abstract).
3. H. Akrami, B. R. Chaudhury, J. Garg, A. Murhekar, *On the Theoretical Foundations of Data Exchange Economies*, arXiv:2412.01968 (2024), https://arxiv.org/abs/2412.01968 (contextual abstract).
