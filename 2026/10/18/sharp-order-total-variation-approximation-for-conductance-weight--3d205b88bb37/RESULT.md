# Sharp-order total-variation approximation for conductance-weighted one-out trees

## Finding

Let \(G=(V,E)\) be any finite connected loopless simple graph, \(n=|V|\ge2\), with strictly positive symmetric edge conductances \(c_e\). Independently, every vertex \(v\) selects an incident edge \(e\) with probability \(c_e/d_v\), where \(d_v=\sum_{e\ni v}c_e\). Forget the directions and repeated selections to form an undirected edge set \(H\). Write \(\mathcal T\) for the set of spanning trees, \(w(T)=\prod_{e\in T}c_e\), \(\tau=\sum_{T\in\mathcal T}w(T)\), \(\mathsf P(T)=w(T)/\tau\) for the conductance-weighted spanning-tree law, and \(C(T)=\sum_{e\in T}c_e\). Set \(\mu=\mathbb E_{\mathsf P}C\) and \(\mathsf Q=\mathcal L(H\mid H\in\mathcal T)\).

**Theorem.** All of the following hold without any regularity or minimum-degree hypothesis beyond connectedness:

\[
\Pr(H=T)=\frac{w(T)C(T)}{\prod_{v\in V}d_v},\qquad
\Pr(H\in\mathcal T)=\frac{\tau\mu}{\prod_{v\in V}d_v},\qquad
\mathsf Q(T)=\mathsf P(T)\frac{C(T)}{\mu}.
\]

In particular, letting \(c_{\min}=\min_e c_e\) and \(c_{\max}=\max_e c_e\),

\[
\|\mathsf Q-\mathsf P\|_{\mathrm{TV}}
=\frac{\mathbb E_{\mathsf P}|C-\mu|}{2\mu}
\le\frac12\sqrt{\frac{c_{\max}}{(n-1)c_{\min}}}.
\]

Equality of the two tree laws holds **exactly when every simple cycle has constant edge conductance** (with arbitrary weights permitted on bridges and different cycle blocks). Equivalently, \(C(T)\) is constant over all spanning trees.

The order \(n^{-1/2}\) cannot be improved uniformly among graphs whose edge-conductance ratios are bounded: a connected chain of \(m\) vertex-disjoint triangles with edge conductances \(1,2,3\), joined by bridges of weight \(1\), has \(n=3m\) and

\[
\lim_{m\to\infty}\sqrt{m}\,\|\mathsf Q_m-\mathsf P_m\|_{\mathrm{TV}}
=\frac{6}{59\sqrt\pi}>0.
\]

These statements concern the *conditioned* one-out edge set, not the unconditioned one-out law or its usual edge-edit Wasserstein distance.

## Assumptions and scope

The graph is finite, simple, connected, and has \(n\ge2\) vertices. Every edge has one strictly positive, finite, symmetric conductance. All random neighbor choices are independent. There are no loops, multiple edges, zero-probability choices, or degree-zero vertices. A spanning tree has exactly \(n-1\) distinct undirected edges. Total variation uses \(\|P-Q\|_{\mathrm{TV}}=\frac12\sum_T|P(T)-Q(T)|\). The chain-of-triangles family has exactly \(m\) disjoint triangles joined in series by \(m-1\) bridges; its vertex count is \(3m\).

## Proof

**1. Exact law.** Fix a spanning tree \(T\). Every vertex selects exactly one neighbor, so there are \(n\) directed selections. Their undirected image equals \(T\) only if precisely one edge is selected in both directions. Choose that mutual edge \(e\in T\). All remaining edges of \(T\) are then forced to point toward the two endpoints of \(e\): each vertex not on \(e\) has a unique next edge leading toward \(e\). Conversely these choices always produce \(T\). The probability of this particular directed assignment is \(c_e^2\prod_{f\in T\setminus\{e\}}c_f/\prod_v d_v=w(T)c_e/\prod_v d_v\). The assignments for distinct mutual edges are disjoint. Summing over \(e\) proves the first formula; summing over \(T\) gives the second and dividing gives the third. All denominators are positive.

**2. Total variation and rigidity.** From the Radon--Nikodym derivative \(\mathrm d\mathsf Q/\mathrm d\mathsf P=C/\mu\), the claimed exact total-variation identity follows. Thus \(\mathsf Q=\mathsf P\) precisely when \(C(T)\) is constant on all spanning trees. Suppose this constancy holds. For any simple cycle \(Z\) and any \(e\in Z\), extend \(Z\setminus\{e\}\) to a spanning tree \(T\). For any \(f\in Z\setminus\{e\}\), \(T-f+e\) is another spanning tree, so \(c_f=c_e\). Hence every cycle is monochromatic. Conversely, any two spanning trees are connected by single-edge basis exchanges. Every exchange \(T-f+e\) uses a fundamental simple cycle containing both \(f\) and \(e\), whose weights are equal if every cycle is monochromatic. So \(C\) is unchanged by every exchange and is constant.

**3. Universal bound.** Write \(I_e=\mathbf1_{\{e\in T\}}\) under \(\mathsf P\); then \(C=\sum_e c_e I_e\). The matrix-tree formula gives \(\tau=\det L_*\), where \(L_*\) is any reduced weighted graph Laplacian. For an arbitrarily oriented edge \(e\), let \(b_e\) denote its reduced incidence vector. Since \(L_*=\sum_e c_e b_e b_e^{\mathsf T}\), for distinct edges \(e\ne f\), differentiation of \(\log\tau\) gives
\[
\operatorname{Cov}(I_e,I_f)
=c_e c_f\frac{\partial^2\log\tau}{\partial c_e\partial c_f}
=-c_e c_f\bigl(b_e^{\mathsf T}L_*^{-1}b_f\bigr)^2\le0.
\]
The differentiations are justified by the finite tree polynomial and positive definiteness of \(L_*\). Therefore
\[
\operatorname{Var}_{\mathsf P}(C)
\le\sum_e c_e^2\operatorname{Var}(I_e)
\le\sum_e c_e^2\mathbb E I_e
\le c_{\max}\,\mathbb E C=c_{\max}\mu.
\]
Cauchy--Schwarz bounds \(\mathbb E|C-\mu|\le\sqrt{\operatorname{Var}(C)}\). Every tree has \(n-1\) edges, so \(\mu\ge(n-1)c_{\min}\). Combining these inequalities proves the displayed universal total-variation bound.

**4. Sharpness of the order.** In the chain of \(m\) triangles, every bridge belongs to every spanning tree. Each triangle contributes an independent selection of two of its three edges. With edge weights \(1,2,3\), the triangle's total selected conductance \(X\) equals \(3,4,5\) with respective probabilities \(2/11,3/11,6/11\). Thus
\[
C=(m-1)+\sum_{j=1}^m X_j,
\quad \mathbb EX=48/11,
\quad \operatorname{Var}(X)=72/121,
\quad \mu=59m/11-1.
\]
By the ordinary i.i.d. central limit theorem and uniform integrability (the normalized sums have uniformly bounded second moments),
\[
\frac{\mathbb E|C-\mu|}{\sqrt m}
\longrightarrow \sqrt{\frac{72}{121}}\sqrt{\frac2\pi}
=\frac{12}{11\sqrt\pi}.
\]
Dividing by \(2\mu\) gives the asserted limit \(6/(59\sqrt\pi)\). Since \(n=3m\) and all weights lie in \([1,3]\), this proves sharpness of the order for a uniformly bounded conductance ratio.

## Verification

The accompanying standard-library Python program `verification/check_weighted_oneout.py` exhaustively enumerates every independent vertex choice and every spanning tree on six small weighted and unweighted graphs (orders two through six). It verifies, using exact rational fractions, all finite exact probability identities, the total-variation expression, the mean-size-bias identity, and the universal bound. It independently checks example triangle weights \(1,2,3\), for which the tree-event probability is \(4/5\) and the conditional-versus-weighted-tree total variation is \(7/88\). The infinite-order convergence and optimality are proved by the determinant differentiation and central-limit arguments above; finite enumeration is not used as a substitute.

## Relationship to prior work

Mészáros and Peled (2026, arXiv:2610.11554v1) study the **unconditioned**, unweighted one-out graph and prove its normalized edge-edit Wasserstein proximity to a uniform spanning tree when minimum degree increases. Their Section 3.1 uses a one-out map in which *one designated root does not choose an outgoing neighbor*, conditional on the map giving a tree; this is a different sampling law from allowing **every** vertex to choose and then conditioning the resulting undirected graph to be a tree. The root-free map's exact weighted tree distribution, its conductance-size bias, sharp \(n^{-1/2}\) total-variation comparison, cycle-weight rigidity and sharp example are not statements of that paper. The matrix-tree determinant and its edge-indicator negative correlation, and the classical central limit theorem, are used as established tools, not claimed as new.

The result is consistent with the general theory of weighted spanning trees and random mappings; it does not assert a new tree-ensemble construction outside this precisely specified conditioning regime.

## Limitations

The total-variation bound may exceed one for small \(n\) or large conductance ratios, in which case it is still mathematically correct but uninformative. No universal convergence is asserted without a bound on \(c_{\max}/c_{\min}\). Sharpness means the *order* \(n^{-1/2}\), not optimality of the stated numerical prefactor. The result does not address directed nonreversible choice kernels or graphs with self-loops and parallel edges. Priority against every possible earlier random-mapping formulation has not been independently audited.

## References

1. A. Mészáros and Y. Peled, *Product approximations for uniform spanning trees and determinantal processes*, arXiv:2610.11554v1, first posted 2026-10-08, https://arxiv.org/abs/2610.11554.
2. L. Fredes and J. Marckert, *Models of random subtrees of a graph*, Probability Surveys 20 (2023), https://doi.org/10.1214/23-PS22. Background reference only; no claim of full-text priority exclusion is made.
3. Classical weighted matrix-tree identity and transfer-current/negative-correlation formulas for finite weighted uniform spanning trees; the specific covariance formula is rederived above.
