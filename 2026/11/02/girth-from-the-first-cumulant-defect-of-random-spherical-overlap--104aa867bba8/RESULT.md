# Girth from the first cumulant defect of random spherical overlap sums

## Finding

For every finite simple undirected graph \(G=(V,E)\), every integer \(p\geq2\), and every deterministic assignment of nonzero real weights \((w_e)_{e\in E}\), take independent uniform unit vectors \((R_v)_{v\in V}\) on \(S^{p-1}\) and define
\[
H_G=\sum_{e=\{u,v\}\in E}w_e\langle R_u,R_v\rangle.
\]
Let \(Z_p\) have the law of the inner product of two independent uniform vectors on \(S^{p-1}\), and put
\[
\mathcal D_G(t)=\log\mathbb E e^{tH_G}-\sum_{e\in E}\log\mathbb E e^{tw_eZ_p}.
\]
For a forest, \(\mathcal D_G(t)\equiv0\) for all real \(t\). If \(G\) has finite girth \(g\), and \(\mathcal C_g(G)\) denotes its set of unoriented simple cycles of length \(g\), then
\[
\boxed{\mathcal D_G(t)=\frac{t^g}{p^{g-1}}\sum_{C\in\mathcal C_g(G)}\prod_{e\in C}w_e+O(t^{g+1})\qquad(t\to0).}
\]
Thus for **positive** weights, the first nonzero cumulant defect has order exactly the girth, and its coefficient recovers the weighted count of shortest cycles. This holds at every graph size and every dimension \(p\ge2\). For signed weights the coefficient identity still holds, but cancellations may hide the girth.

In particular, for an unweighted graph and independent Haar-random pure qubit states \((\psi_v)\), write
\[
W_G=\sum_{\{u,v\}\in E}\bigl(2|\langle\psi_u,\psi_v\rangle|^2-1\bigr).
\]
The Bloch-vector identity identifies \(W_G\) with \(H_G\) for \(p=3\); here \(Z_3\) is uniform on \([-1,1]\). The **single scalar distribution** of \(W_G\) therefore determines \(m=|E|=3\operatorname{Var}(W_G)\), whether the graph is a forest, and otherwise its girth and number \(c_g\) of shortest cycles, since
\[
\log\mathbb E e^{tW_G}-m\log\frac{\sinh t}{t}=\frac{c_g}{3^{g-1}}t^g+O(t^{g+1}).
\]
The logarithmic expression is defined continuously at \(t=0\).

As a finite-order consequence valid **without any girth assumption**, if \(c_j\) is the number of simple unoriented \(j\)-cycles, then
\[
\begin{aligned}
\kappa_2(W_G)&=m/3,\\
\kappa_3(W_G)&=2c_3/3,\\
\kappa_4(W_G)&=-2m/15+8c_4/9,\\
\kappa_5(W_G)&=-8c_3/3+40c_5/27.
\end{aligned}
\]
Consequently the second through fifth cumulants recover \(m,c_3,c_4,c_5\) exactly. Here \(\kappa_j\) denotes the ordinary \(j\)-th cumulant.

## Assumptions and scope

All graphs are finite, loop-free, and have no repeated edges; isolated vertices are permitted. The random vectors at distinct vertices are independent, and the sphere law is the normalized rotation-invariant surface measure. A cycle is a simple undirected cycle, counted once up to rotations and reversal. The girth of a forest is \(\infty\). Edge weights are fixed real numbers; positivity is necessary only for the assertion that the first nonzero coefficient always identifies the girth. The qubit specialization uses independent rank-one Haar pure states, not mixed states, and uniform unweighted edges. All assertions are exact identities about population laws, not finite-sample estimation guarantees.

## Proof

**1. Edge variables on a forest are independent.** Fix a forest \(F\) and a leaf \(v\) with neighbor \(u\). Conditional on all vectors except \(R_v\), the variable \(\langle R_u,R_v\rangle\) has the fixed law \(Z_p\), independent of the conditioned vectors, by rotational invariance. It is therefore independent of all other edge variables. Delete that edge and repeat. The family of inner products indexed by \(E(F)\) is mutually independent, each with law \(Z_p\). This proves the forest identity for arbitrary real weights, not just a formal power series identity.

**2. A simple cycle has an exact mixed moment.** Rotational invariance gives
\[
\mathbb E[R_vR_v^{\mathsf T}]=I_p/p,
\qquad
\mathbb E[\langle a,R_v\rangle\langle R_v,b\rangle]=\langle a,b\rangle/p.
\]
Successively integrating out the internal vertices of any simple \(j\)-cycle and finally the remaining two vectors yields
\[
\mathbb E\prod_{e=\{u,v\}\in C}\langle R_u,R_v\rangle=p^{1-j}.
\]
Every proper nonempty subset of that cycle is a forest; its constituent centered edge variables are independent. In the moment-partition formula for the joint cumulant of the \(j\) distinct edge variables on \(C\), all partition contributions except the single-block contribution vanish. Therefore the joint cumulant is exactly \(p^{1-j}\).

**3. The first mixed cumulant is controlled by girth.** Denote the edge variable by \(X_e=\langle R_u,R_v\rangle\). Cumulants are multilinear and vanish when their arguments can be split into two independent nonempty collections. Whenever the distinct edges appearing among \(r\) arguments form a forest and at least two different edges occur, the joint cumulant is zero by Step 1. For \(r<g\), any set of at most \(r\) distinct edges is a forest. Hence
\[
\kappa_r(H_G)=\kappa_r(Z_p)\sum_{e\in E}w_e^r \quad(1\le r<g).
\]
At \(r=g\), a nonzero mixed cumulant involving distinct edges can only use exactly \(g\) different edges forming a simple \(g\)-cycle. By Step 2 it equals \(p^{1-g}\) for each ordering. Each shortest cycle contributes \(g!p^{1-g}\prod_{e\in C}w_e\), while the diagonal terms are \(\kappa_g(Z_p)\sum_e w_e^g\). Thus
\[
\kappa_g(H_G)-\kappa_g(Z_p)\sum_e w_e^g
=g!p^{1-g}\sum_{C\in\mathcal C_g(G)}\prod_{e\in C}w_e.
\]
The variables are bounded, so all moment-generating functions are analytic near zero and the cumulant expansions converge there. Dividing the order-\(g\) cumulant identity by \(g!\) proves the claimed expansion and its remainder. Positive cycle products preclude cancellation.

**4. The qubit and low-order formulas.** A Haar pure qubit has a uniform Bloch vector \(R\in S^2\), and \(2|\langle\psi,\phi\rangle|^2-1=R_\psi\cdot R_\phi\). A dot product of two uniform Bloch vectors has the uniform law on \([-1,1]\), hence variance \(1/3\), fourth moment \(1/5\), and fourth cumulant \(-2/15\). In arbitrary dimension \(p\), the corresponding fourth moment is \(3/[p(p+2)]\), and the fourth cumulant is \(-6/[p^2(p+2)]\). For orders three and four, the only non-diagonal contributing distinct-edge patterns are a triangle and a four-cycle, respectively. Their contributions to the cumulants are \(3!c_3/p^2\) and \(4!c_4/p^3\).

At order five, besides a five-cycle, the only contributing repeated-edge pattern involves a triangle with one edge listed three times and its other two edges once. If these edges have variables \(X,Y,Z\), its joint cumulant is
\[
\operatorname{cum}(X,X,X,Y,Z)
=\frac{3}{p^2(p+2)}-\frac{3}{p^3}
=-\frac{6}{p^3(p+2)}.
\]
There are three choices of tripled triangle edge and \(5!/3!=20\) orderings per choice; thus the total triangle contribution is \(-360c_3/[p^3(p+2)]\), while five-cycles contribute \(5!c_5/p^4\). Every remaining pattern either contains an edge-variable support that is a forest, has an odd-degree vertex and vanishing product expectation, or splits into independent cumulant blocks. Taking \(p=3\) gives the four displayed cumulant identities.

## Verification

The accompanying `verify.py` uses only Python standard-library exact rational arithmetic and the spherical coordinate moment tensor
\[
\mathbb E[R_{i_1}\cdots R_{i_{2k}}]
=\frac{\sum_{\pi\,\mathrm{pairing}}\prod_{\{a,b\}\in\pi}\delta_{i_a i_b}}{p(p+2)\cdots(p+2k-2)}.
\]
It independently expands raw edge-product moments and converts them to cumulants, without using the forest/cycle proof as an algorithm. The included execution output reports **213 exact-rational assertions passed**, covering sphere dimensions \(2,3,4\), eight distinct graph families, cycle products of lengths three through seven, weighted triangle identities, and a signed-weight cancellation example. Run `python3 verify.py` beside the files. Numerical or finite symbolic tests do not establish the theorem for every graph or every cumulant order; that is supplied by Steps 1–3.

## Relationship to prior work

Zhang, *Exact probability laws of random inner products: Dirichlet splines, overlaps, uncertainty, and Bargmann invariants* (2026), develops random-state overlaps and cyclic Bargmann-invariant moments (especially Section 6.5 and Proposition 6.8), but the inspected results concern cyclic complex invariants, not the cumulant law of a graph-wide **sum of pair overlaps** or its inverse identification of girth. Peled and Spinka, *Lectures on the Spin and Loop \(O(n)\) Models*, Section 2.4 (2017 preprint, later revisions), present a general high-temperature subgraph expansion of exactly the classical spherical-spin partition function on arbitrary graphs. That general identity is important antecedent methodology; the statement here evaluates its first graph-dependent cumulant, proves exact forest independence, and identifies girth and shortest-cycle weight from a scalar distribution. Classical Heisenberg series work (Stanley, 1967) also provides diagrammatic background. No claim of novelty is made for rotational invariance, general high-temperature expansion, or the bare expectation of a cycle product.

## Limitations

The claim is about finite simple graphs and independent uniform vector states. Weighted girth identification requires positive weights: negative weights can cancel shortest-cycle products. The scalar law determines the edge count, girth and number of shortest cycles, and has additional low-order information, but is **not** claimed to determine the complete graph up to isomorphism or all graph invariants. Finite-sample cumulant estimation, robustness to imperfect Haar randomness, and infinite graph limits are not addressed. Historical-priority risk remains from general classical-spin linked-cluster expansions and potentially unindexed results; the derivation and overlap review do not constitute independent external validation.

## References

1. Lin Zhang, *Exact probability laws of random inner products: Dirichlet splines, overlaps, uncertainty, and Bargmann invariants*, arXiv:2610.25196v1, publicly posted 18 October 2026, https://arxiv.org/html/2610.25196v1; especially Sections 4 and 6.5.
2. Ron Peled and Yinon Spinka, *Lectures on the Spin and Loop \(O(n)\) Models*, arXiv:1708.00058, https://arxiv.org/abs/1708.00058; especially Section 2.4, equation (15).
3. H. Eugene Stanley, *High-Temperature Expansions for the Classical Heisenberg Model. I. Spin Correlation Function*, Physical Review **158** (1967), 537–545, https://doi.org/10.1103/PhysRev.158.537.
