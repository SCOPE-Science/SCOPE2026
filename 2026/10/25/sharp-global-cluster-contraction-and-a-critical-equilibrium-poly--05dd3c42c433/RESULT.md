# Sharp global cluster contraction and a critical equilibrium polytope for hyperflower tent maps

## Finding
For the folded coupled hypergraph map on a hyperflower, **every** initial state synchronizes asymptotically within each central/leaf block at the sharp, coupling-independent rate \((\mu/2)^n\) when \(0<\mu<2\). In contrast, at \(\mu=2\) the full system admits, for every coupling, an explicit affine-dimensional family of stationary nonsynchronized states. The critical threshold is sharp for uniform-in-coupling global cluster attraction.

Precisely, write \(C\) for the center, \(P_1,\ldots,P_\ell\) for the leaves and
\[
D(x)=\max_{B\in\{C,P_1,\ldots,P_\ell\}}\;\max_{i,k\in B}|x_i-x_k|.
\]
For \(0<\mu<2\), \(D(x(n))\le(\mu/2)^nD(x(0))\) for every initial state, every real coupling and every iteration index. The contraction factor cannot be improved uniformly over those choices whenever some block contains at least two vertices.

At \(\mu=2\), with \(d=c+\ell t\), the polytope
\[
\mathcal P=\left\{x\in[0,\tfrac12]^d:\sum_{i\in C}x_i=\sum_{i\in P_j}x_i\text{ for }1\le j\le\ell\right\}
\]
is fixed pointwise for **all** real couplings. Its affine dimension is exactly \(d-\ell\). If at least one of \(c,t\) exceeds one, \(\mathcal P\) contains fixed states with positive within-block diameter. For nonzero coupling, every point in \(\mathcal P\) whose coordinates lie strictly between zero and one half has a neighborhood within the lower half cube in which the *entire* fixed-point set agrees with \(\mathcal P\). Above criticality, \(2<\mu\le4\), universal-in-coupling global attraction again fails.

## Assumptions and scope
Fix integers \(c,t,\ell\ge1\). The hyperflower has \(c\) central vertices \(C\) that are inputs in each of \(\ell\) hyperedges; each hyperedge additionally has its own \(t\) peripheral output vertices \(P_j\), with the leaves disjoint. Thus \(d=c+\ell t\). Set \(k=c+t-1\), which is positive. For any vector \(v\in\mathbb R^d\), put
\[
S_j(v)=\sum_{i\in C}v_i-\sum_{i\in P_j}v_i.
\]
The normalized chemical-hypergraph Laplacian used in the source model has the explicit form
\[
(\Delta_Hv)_i=\frac{\sum_{j=1}^\ell S_j(v)}{\ell k}\quad(i\in C),\qquad
(\Delta_Hv)_i=-\frac{S_j(v)}{k}\quad(i\in P_j).
\]
The first formula follows from normalized degree \(\ell k\) at a center vertex, and the second from degree \(k\) at a leaf vertex. No singleton block contributes to its own diameter.

Let \(\sigma:\mathbb R\to[0,1]\) be the periodic triangular folding map: for each integer \(m\), \(\sigma(z)=z-2m\) on \([2m,2m+1]\), and \(\sigma(z)=2m+2-z\) on \([2m+1,2m+2]\). This continuous map is globally \(1\)-Lipschitz and equals the identity on \([0,1]\). Let \(f_\mu(s)=\frac\mu2\min\{s,1-s\}\) on \([0,1]\), with \(0<\mu\le4\), so that \(f_\mu\) maps the unit interval into itself and is globally \(\mu/2\)-Lipschitz. Given any real \(\varepsilon\), define
\[
x_i(n+1)=\sigma\!\left(f_\mu(x_i(n))-\varepsilon\,(\Delta_H f_\mu(x(n)))_i\right),\qquad x(0)\in[0,1]^d.
\]
The full cube is forward invariant because \(\sigma\) takes values in \([0,1]\). Our cluster-attraction claim concerns within-center and within-individual-leaf differences; it does not assert equality between distinct leaves or asymptotic convergence of the quotient dynamics.

## Proof
**1. Common-input contraction.** For fixed \(x\), the Laplacian formula shows that \((\Delta_H f_\mu(x))_i\) has the **same value for all** \(i\) in \(C\), and similarly has the same value for all \(i\) in any given \(P_j\). Thus if \(i,k\) belong to one block, the two pre-folding arguments differ by precisely \(f_\mu(x_i)-f_\mu(x_k)\): the coupling contributions cancel *without a bound on* \(\varepsilon\). Since \(\sigma\) is \(1\)-Lipschitz and \(f_\mu\) is \(\mu/2\)-Lipschitz,
\[
|x_i(n+1)-x_k(n+1)|\le\frac\mu2|x_i(n)-x_k(n)|.
\]
Taking maxima gives \(D(x(n+1))\le(\mu/2)D(x(n))\); induction yields the announced global bound. When \(\mu<2\), its right side tends to zero, giving global asymptotic cluster synchrony for arbitrary initial conditions and coupling.

**2. Optimality below the threshold.** Assume some block contains at least two vertices. Set \(\varepsilon=0\). Choose an initial state with two different coordinates in that block, both in \([0,1/4]\), and set all other coordinates to zero. The scalar tent map acts as multiplication by \(\mu/2\) on \([0,1/2]\), and for \(\mu<2\) this interval is forward invariant under that linear branch. Consequently \(D(x(n))=(\mu/2)^nD(x(0))>0\) at every \(n\). No uniformly smaller factor is possible.

**3. Fixed-point polytope at the threshold.** At \(\mu=2\), the tent map equals the identity on \([0,1/2]\). On \(\mathcal P\) every balance \(S_j(x)\) vanishes, hence \(\Delta_Hx=0\), and the update becomes \(\sigma(x_i)=x_i\). Thus each point of \(\mathcal P\) is fixed for every \(\varepsilon\). The \(\ell\) equations \(S_j(x)=0\) are independent because each has a variable from its own leaf absent from all the other equations. To see the intersection with the lower half cube has the full expected affine dimension, use the strictly interior balanced vector with all center coordinates equal to \(a=t/[4(c+t)]\), and all leaf coordinates equal to \(b=c/[4(c+t)]\). Then \(ca=tb\), and \(0<a,b<1/2\). An affine neighborhood of this vector inside the kernel lies in the cube, so \(\dim_{\rm aff}\mathcal P=d-\ell\).

If \(c\ge2\), increase one center coordinate of that interior vector by a small positive amount and decrease another by the same amount; all balances stay zero. If \(t\ge2\), do the same in one leaf. Small enough variations remain strictly inside the cube, and the resulting fixed points have \(D>0\). This gives nonsynchronized equilibria at the critical value regardless of coupling.

**4. Exact local fixed-point dimension for nonzero coupling.** Fix \(\varepsilon\ne0\) and any point \(x_*\in\mathcal P\) with all coordinates in \((0,1/2)\). By continuity there is a neighborhood \(U\) of \(x_*\), entirely in the lower half cube, where all the pre-folding arguments \(x_i-\varepsilon(\Delta_Hx)_i\) lie in \((0,1)\). Thus for \(x\in U\), the folding and tent maps both act as the identity on the relevant arguments, and the fixed-point equation becomes \(\varepsilon\Delta_Hx=0\). Since \(\varepsilon\ne0\), this is exactly the set of balance equations \(S_j(x)=0\) for each leaf (by the leaf coordinate formulas). It follows that \(\operatorname{Fix}(F)\cap U=\mathcal P\cap U\). For \(\varepsilon=0\), instead the entire lower half cube is fixed; this exception is important.

**5. Optimal threshold for a uniform-over-coupling statement.** For \(2<\mu\le4\) at \(\varepsilon=0\), the scalar tent map has two distinct fixed points \(0\) and \(r=\mu/(\mu+2)\in(1/2,1)\): indeed \(f_\mu(r)=(\mu/2)(1-r)=r\). Assign both values to two vertices of the same nonsingleton block. Every coordinate is then fixed and \(D>0\). Together with Step 3 this proves the global universal-in-coupling statement holds exactly when \(0<\mu<2\) for nontrivial blocks.

## Verification
`CHECKER.py` uses only standard-library exact rational arithmetic. It implements the hyperflower Laplacian through both the displayed row formulas and an *independent signed incidence-matrix construction*. It checks forward interval invariance, cluster contraction and iterations for multiple integer hyperflower sizes and real rational couplings, optimality on the uncoupled branch, balanced critical fixed states and above-threshold counterexamples. Run `python CHECKER.py` to reproduce the recorded \(15159\) exact-rational assertions. These finite computations cross-check normalizations and examples; the proof for all hyperflower sizes, couplings and iterations is Steps 1–5 above.

## Relationship to prior work
Böhle, Kuehn, Mulas and Jost [1] define precisely this folded chemical-hypergraph model, give the hyperflower spectral eigenmodes, obtain the necessary linearized condition \(\log(\mu/2)<0\) for within-component stability, and state that numerical evidence **suggests** its sufficiency. The new result proves global, all-initial-condition sufficiency with a sharp rate *uniform in all real couplings*, and determines an explicit positive-dimensional nonsynchronized fixed set at the neutral boundary. These conclusions are not statements of [1]. Its source Laplacian and the fact that the zero eigenspace has dimension \(d-\ell\) are credited, not claimed as new.

Salova and D'Souza [2] develop general hypergraph cluster-admissibility and linear-stability reduction. Von der Gracht, Nijholt and Rink [3] classify robust synchrony patterns through structural higher-order interactions. Neither inspected work establishes the all-initial quantitative bound or the model-specific fixed-polytope and sharp threshold for the triangular-folded tent hyperflower map. Generic common-input contraction ideas are familiar; priority for an equivalent formulation in other coupled-map literature cannot be completely excluded.

## Limitations
The attraction theorem uses the exact common-input structure of each hyperflower block and the scalar tent map's global Lipschitz constant. It does not infer chaotic behavior, convergence of cluster means, or intercluster synchronization. If \(c=t=1\), every center/leaf block is a singleton and the diameter vanishes identically, so the claimed sharpness and counterexamples to within-block synchrony require at least one nonsingleton block. The local *exact* critical fixed-set description assumes \(\varepsilon\ne0\) and coordinates strictly inside \((0,1/2)\); it is not a global classification of every possible fixed point outside that region. The theorem makes no assertions of independent validation or publication priority beyond the explicit literature comparisons.

## References
[1] T. Böhle, C. Kuehn, R. Mulas and J. Jost, *Coupled Hypergraph Maps and Chaotic Cluster Synchronization*, arXiv:2102.02272v1, first public 2021-02-03; revised open text arXiv:2102.02272v2, 2021-05-18; DOI:10.1209/0295-5075/ac1a26.

[2] A. Salova and R. M. D'Souza, *Cluster synchronization on hypergraphs*, arXiv:2101.05464, first public 2021-01-14; revised open text arXiv:2101.05464v4.

[3] S. von der Gracht, E. Nijholt and B. Rink, *Hypernetworks: cluster synchronisation is a higher-order effect*, arXiv:2302.08974, first public 2023-02-17; revised open text arXiv:2302.08974v2.
