# Cycle \(p\)-heat: individual Lipschitz contraction and sharp two-input instability

## Finding

Let \(S_t\) be the unweighted graph \(p\)-heat semigroup on \(C_n\), with \(n\ge3\) and \(1<p<\infty\). If \(L(f)=\max_i|f_{i+1}-f_i|\) denotes the graph-Lipschitz seminorm, then every single trajectory satisfies
\[
L(S_tu)\le L(u)\qquad(t\ge0).
\]
Nevertheless, the nonlinear semigroup is nonexpansive **between two trajectories** in the same seminorm,
\[
L(S_tu-S_tv)\le L(u-v)\quad\text{for every }u,v\text{ and }t\ge0,
\]
if and only if \(p=2\) or \(n=3\). For every \(n\ge4\) and \(p\ne2\), the initial normalized amplification rate is not merely positive: its supremum over pairs of distinct initial states is \(+\infty\):
\[
\sup_{u\ne v}\liminf_{t\downarrow0}
\frac{L(S_tu-S_tv)/L(u-v)-1}{t}=+\infty.
\]
All assertions concern real-valued vertex signals and continuous time.

## Assumptions and scope

Fix an integer \(n\ge3\) and a real \(p\in(1,\infty)\). The vertices of \(C_n\) are indexed by \(0,\ldots,n-1\), with indices modulo \(n\). Each edge has length and conductance one, and each vertex has mass one. The metric is the undirected shortest-path metric. Define \(\phi_p(s)=|s|^{p-2}s\) for \(s\ne0\), and \(\phi_p(0)=0\). The flow solves
\[
\dot u_i=\phi_p(u_{i+1}-u_i)+\phi_p(u_{i-1}-u_i).
\]
There is a unique global solution from each real initial vector: this is the negative gradient flow of the convex, continuously differentiable energy \(\sum_i|u_{i+1}-u_i|^p/p\). The gradient is monotone, which proves uniqueness, and the vertex maximum principle bounds all coordinates on finite intervals, proving global existence. The Lipschitz seminorm associated with the stated graph metric is exactly \(L(u)=\max_i|u_{i+1}-u_i|\), by telescoping along shortest paths.

## Proof

**1. Exact edge equation.** Orient edge \(i\) from vertex \(i\) to \(i+1\), and set \(a_i=u_{i+1}-u_i\). Then \(\sum_i a_i=0\), and direct subtraction of adjacent vertex equations gives
\[
\dot a_i=\phi_p(a_{i+1})+\phi_p(a_{i-1})-2\phi_p(a_i). \tag{1}
\]
This identity, including its signs, is independent of orientation choices once the cyclic convention has been fixed.

**2. One-input maximum principle.** The function \(\phi_p\) is strictly increasing. At any index where \(a_i\) is maximal, both neighboring \(\phi_p(a)\) values are at most \(\phi_p(a_i)\), so \(\dot a_i\le0\). Likewise every minimizing coordinate has \(\dot a_i\ge0\). Applying the finite-coordinate Dini-derivative maximum principle to (1), \(\max_i a_i(t)\) is nonincreasing and \(\min_i a_i(t)\) is nondecreasing. Therefore \(\|a(t)\|_\infty=L(u(t))\) is nonincreasing for all \(t\ge0\).

**3. Linear and triangular cases of two-input contraction.** If \(p=2\), (1) reduces to the linear heat equation \(\dot a_i=a_{i+1}+a_{i-1}-2a_i\). The difference of any two edge vectors satisfies the same heat equation, so the maximum principle gives \(L(S_tu-S_tv)\le L(u-v)\). If \(n=3\), the graph is the complete graph on three vertices and \(L(h)=\max_i h_i-\min_i h_i\). For two solutions set \(h=u-v\). At a maximum of \(h\), each summand of
\[
\dot h_i=\sum_{j\sim i}\left[\phi_p(v_j-v_i+h_j-h_i)-\phi_p(v_j-v_i)\right]
\]
is nonpositive by monotonicity, while at a minimum each summand is nonnegative. Thus the oscillation of \(h\) decreases, proving two-input contraction for the triangle at every \(p>1\).

**4. Explicit nonlinear obstruction on every longer cycle.** Assume \(n\ge4\) and \(p\ne2\), and choose any \(R>0\). Define the following cyclic edge vectors (the displayed expression has \(n\) coordinates):
\[
 a=(1,R,-(R+n-2),\underbrace{1,\ldots,1}_{n-3}),
 \qquad
 b=(1,1,-1,\underbrace{0,\ldots,0}_{n-4},-1).
\]
Both sum to zero, so they are the oriented gradients of vertex vectors \(U,V\). All coordinates of \(a\) are nonzero. For \(\varepsilon>0\), set \(U^\pm=U\pm\varepsilon V/2\) and \(u^\pm(t)=S_tU^\pm\). Then
\[
L(U^+-U^-)=\varepsilon L(V)=\varepsilon,
\]
and for the normalized first edge difference
\[
 z_0(t)=\frac{(u^+_1-u^+_0)-(u^-_1-u^-_0)}{\varepsilon}
\]
one has \(z_0(0)=1\). Differentiating (1) at time zero for each of the two solutions, then letting \(\varepsilon\downarrow0\), yields
\[
 \lim_{\varepsilon\downarrow0}\dot z_0(0)
 =\phi'_p(R)-\phi'_p(1)-2\phi'_p(1)
 =(p-1)(R^{p-2}-3). \tag{2}
\]
The derivative exists since \(a\) has no zero coordinates and \(\phi'_p(s)=(p-1)|s|^{p-2}\) there. When \(p>2\), the right-hand side of (2) tends to \(+\infty\) as \(R\to\infty\); when \(1<p<2\), it does so as \(R\downarrow0\). Given any \(M>0\), first choose \(R\) so that (2) exceeds \(M+1\), then choose a sufficiently small positive \(\varepsilon\) so that \(\dot z_0(0)>M\). Because \(z_0(0)=1\), the seminorm of the normalized solution difference is at least \(z_0(t)\). Hence
\[
\liminf_{t\downarrow0}\frac{L(S_tU^+-S_tU^-)/\varepsilon-1}{t}
\ge \dot z_0(0)>M.
\]
This proves unbounded instantaneous normalized growth, and in particular strict two-input Lipschitz expansion for some arbitrarily small positive times. It also proves that four vertices are the smallest cyclic obstruction: at three vertices contraction always holds.

**5. Exact small witness.** On \(C_4\) at \(p=3\), take \(R=4\). Then \(a=(1,4,-6,1)\) and \(b=(1,1,-1,-1)\). The right-hand side of (2) is exactly \(2\), so sufficiently small symmetric perturbations already violate the two-input inequality.

## Verification

The accompanying standard-library Python program `verify_cycle_p_heat.py` verifies the edge-flow orientation identity with exact rational arithmetic for sizes \(3\le n\le12\) at \(p=3\), checks thirty nonlinear first-edge differential witnesses for sizes \(4,5,6,8,12\), and integrates four representative pairs with fourth-order Runge–Kutta steps to corroborate strict short-time growth. Run with `python verify_cycle_p_heat.py` from a directory containing the file. The analytic steps above prove the infinitely many sizes and all real exponents; finite numerical runs do not substitute for that proof.

## Relationship to prior work

Mugnolo's foundational treatment of discrete \(p\)-heat establishes nonlinear well-posedness, vertex-order comparison and contraction in vertex norms; its Theorem 3.4 and Proposition 3.9 do not explicitly classify two-input **edge-Lipschitz** stability on cycles. Münch and Wojciechowski's heat-gradient characterization concerns a *linear* Markov semigroup, not the nonlinear \(p\ne2\) edge-gradient flow. The present theorem separates these notions by proving one-input contraction for every nonlinear exponent while constructing arbitrarily strong instantaneous two-input edge-gradient amplification on each \(C_n\) with \(n\ge4\). Earlier tree-only nonlinear two-input rigidity does not imply this result because the cyclic graph flow is not the restriction of the tree flow to an induced path.

## Limitations

The result assumes unit vertex masses, unit edge conductances, unit graph edge lengths, simple cycles, real signals and continuous time with \(1<p<\infty\). It does not classify weighted cycles, non-cycle graphs, the sharp two-input operator Lipschitz factor at a fixed positive time, or discrete-time numerical steps. In particular, the unbounded *initial derivative* does not assert unbounded amplification at a fixed time. The literature comparison establishes absence of a matching result in the sources inspected, not a proof of global publication priority.

## References

1. D. Mugnolo, *Parabolic theory of the discrete p-Laplace operator*, arXiv:1207.1996 (initially public July 9, 2012), especially Theorem 3.4, Proposition 3.9 and Corollary 3.11. https://arxiv.org/abs/1207.1996
2. F. Münch and R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875 (December 4, 2017), especially Theorem 3.8. https://arxiv.org/abs/1712.00875
