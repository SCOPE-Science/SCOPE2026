# A universal chord-price cutoff for resistance-optimal pineapple networks

## Finding

Let \(k\ge2\) and \(m\ge1\) be integers, \(N=k+m+1\), and \(B,t>0\). Form a pineapple graph by joining a clique on the hub \(h\) and \(k\) peripheral core vertices, then attaching \(m\) degree-one vertices to \(h\). Assign *independently adjustable*, nonnegative conductances to every available edge, with unit expenditure per unit conductance on the \(k+m\) edges incident to \(h\) and price \(t\) on each of the \(\binom{k}{2}\) remaining clique edges. Require a connected positive-conductance support and exact expenditure \(B\). Minimize the Kirchhoff index \(\mathcal K=\sum_{u<v}R_{uv}\), with \(R_{uv}\) effective resistance.

**Theorem.** The unrestricted optimizer is unique and has three edge-orbit conductances: \(a\) on hub-to-core edges, \(b\) on hub-to-leaf edges, and \(c\) on edges between peripheral core vertices. Put
\[
\tau_N=\frac{2N}{N-1}.
\]
If \(t\ge\tau_N\), the unique optimizer deletes **every** nonhub clique edge and assigns
\[
a_*=b_*=\frac{B}{N-1},\qquad c_*=0,\qquad \mathcal K_*=\frac{(N-1)^3}{B}.
\]
If \(0<t<\tau_N\), define
\[
\beta=\frac{t(k-1)}2,\quad \alpha=k-\beta,\quad
Z=m\sqrt{N-1}+\sqrt{(m+1)\alpha}+\sqrt{(k-1)N\beta}.
\]
Then \(\alpha>0\) and the **unique** globally optimal allocation is
\[
 b_*=\frac{B\sqrt{N-1}}{Z},\qquad
 a_*=\frac BZ\sqrt{\frac{m+1}{\alpha}},\qquad
 c_*=\frac{B}{kZ}\left(\sqrt{\frac{(k-1)N}{\beta}}-\sqrt{\frac{m+1}{\alpha}}\right)>0,
\]
with
\[
\mathcal K_*=\frac{Z^2}{B}.
\]
In particular, the chord-deletion price threshold depends on the **total number of vertices only**, not on how the \(N-1\) nonhub vertices are divided between the core and pendant classes. Below that threshold every eligible nonhub clique edge is used; at and above it every such edge is absent. No symmetry constraint is placed on competitors. As a quantitative consequence, for fixed \(m\ge1\) and fixed \(t>0\), if \(\mathcal K_{\rm star}=(N-1)^3/B\) denotes the optimum without nonhub clique edges, then
\[
\lim_{k\to\infty}\frac{\mathcal K_*}{\mathcal K_{\rm star}}=\min\left\{\frac t2,1\right\}.
\]
Thus for prices below two, the fully optimized optional clique network retains an asymptotically strict gain over the star architecture, even with a fixed number of leaves.

## Assumptions and scope

The integers satisfy \(k\ge2\), \(m\ge1\); prices \(B,t\) are strictly positive real numbers. An absent edge is represented by zero conductance, and the positive-conductance graph must remain connected. Every eligible original edge is individually adjustable; the equalities \(a,b,c\) characterize the solution rather than restrict feasible inputs. The budget is linear and fully exhausted. The Kirchhoff index is an *unordered-pair* sum, not the averaged resistance or \(\operatorname{tr}L^+\); for \(N\) vertices it equals \(N\operatorname{tr}L^+\). The threshold includes equality in the chord-free regime. Neither nonlinear material costs nor alternative attachment topologies are asserted.

## Proof

**1. Convexity, existence and symmetry.** For a connected conductance assignment, let \(L\) be its weighted Laplacian, \(J=\mathbf1\mathbf1^\mathsf T\), and \(X=L+J/N\). Then \(X\) is positive definite and
\[
\mathcal K=N\bigl(\operatorname{tr}X^{-1}-1\bigr).
\]
Along a nonzero symmetric perturbation \(H\) of \(X\), the second derivative is
\[
2N\operatorname{tr}\bigl(X^{-1}HX^{-1}HX^{-1}\bigr)>0.
\]
Strict positivity follows by writing the trace as \(\operatorname{tr}[(A^{1/2} H A)^\mathsf T (A^{1/2} H A)]\) with \(A=X^{-1}\), since \(H\) and \(A\) are symmetric. The mapping from individual edge conductances to \(L\) is injective on a simple graph, as each off-diagonal entry specifies the corresponding edge conductance. Hence \(\mathcal K\) is strictly convex on connected feasible assignments. A finite minimum exists because the budget feasible set is compact, the graph admits a connected positive weighting, and \(\mathcal K\to\infty\) upon losing connectivity. The strict convex minimizer is unique. Permuting the \(k\) equivalent core vertices and the \(m\) equivalent leaves preserves cost and objective; uniqueness forces the three orbit weights \(a,b,c\).

**2. Exact resistance objective.** On the core clique, the Laplacian has a hub-versus-core eigenvalue \((k+1)a\) and a \((k-1)\)-fold core-contrast eigenvalue \(a+kc\). Consequently, the resistance between \(h\) and any core vertex and that between two distinct nonhub core vertices are, respectively,
\[
R_{h,u}=\frac1{ka}+\frac{k-1}{k(a+kc)},\qquad R_{u,v}=\frac2{a+kc}.
\]
Each leaf edge is a bridge, so a resistance path passing from a leaf to the rest incurs an additional \(1/b\). Summing the \(\binom N2\) unordered resistances gives the exact identity
\[
\mathcal K(a,b,c)=\frac{m(N-1)}b+\frac{m+1}{a}+\frac{(k-1)N}{a+kc}.
\]
The expenditure is
\[
B=ka+mb+\frac{t k(k-1)}2c.
\]

**3. Prices below the threshold.** Put \(v=a+kc\ge a\), \(\beta=t(k-1)/2\), and \(\alpha=k-\beta\). Then
\[
B=mb+\alpha a+\beta v,
\qquad
\mathcal K=\frac{m(N-1)}b+\frac{m+1}a+\frac{(k-1)N}v.
\]
For \(0<t<2N/(N-1)\), \(\alpha>0\). Cauchy–Schwarz proves
\[
\mathcal K\, B\ge
\left(m\sqrt{N-1}+\sqrt{(m+1)\alpha}+\sqrt{(k-1)N\beta}\right)^2=Z^2.
\]
Equality forces \((b,a,v)=\frac BZ(\sqrt{N-1},\sqrt{(m+1)/\alpha},\sqrt{(k-1)N/\beta})\). The necessary feasibility check \(v>a\) is equivalent to
\[
(k-1)N\alpha>(m+1)\beta
\iff
\beta<\frac{(k-1)N}{N-1}
\iff t<\tau_N,
\]
using \((m+1)+(k-1)N=k(N-1)\). Thus Cauchy equality is feasible and gives exactly the stated positive \(c_*=(v_*-a_*)/k\), proving global optimality in this regime.

**4. Prices at and above the threshold.** The chord-free candidate has \(a=b=B/(N-1)=s\), \(c=0\). Its partial derivatives are
\[
\partial_a\mathcal K=-\frac{k(N-1)}{s^2},\quad
\partial_b\mathcal K=-\frac{m(N-1)}{s^2},\quad
\partial_c\mathcal K=-\frac{k(k-1)N}{s^2}.
\]
The Lagrange multiplier for budget is \(\lambda=(N-1)/s^2\). Therefore the nonnegativity KKT condition on \(c=0\) reads
\[
\partial_c\mathcal K+\lambda\frac{t k(k-1)}2
=\frac{k(k-1)}{s^2}\left(\frac{(N-1)t}2-N\right)\ge0,
\]
exactly when \(t\ge\tau_N\). Convexity makes this condition sufficient; strict convexity makes the optimum unique, including at equality. With the core chords deleted the graph is a star, and the objective is \((N-1)^3/B\). For the stated asymptotic corollary, fix \(m,t>0\) and let \(k\to\infty\). The threshold \(2N/(N-1)\) tends to \(2\). If \(t<2\), the third term \(\sqrt{(k-1)N\beta}\) in \(Z\) is asymptotic to \(\sqrt{t/2}\,k^{3/2}\) and the other two terms are \(O(k^{1/2})\); hence \(Z^2/(N-1)^3\to t/2\). If \(t>2\), the chords are eventually absent, and the ratio is one. At \(t=2\) the same inner-branch asymptotics gives one. This completes the proof.

## Verification

A self-contained Python checker evaluates small pineapple Laplacians using exact rational Gaussian elimination after grounding one vertex, confirms the resistance identity for numerous rational conductance triples, checks rational budget identities and chord-boundary KKT signs, and compares analytic optimum values with independently assembled finite Laplacian eigenvalues for a grid of parameters on both sides of the cutoff. Execute `python3 verification.py` from the extracted package. These finite tests are auxiliary; the global, all-size claim is proved analytically above.

## Relationship to prior work

Ghosh, Boyd and Saberi (2008) established the general convex formulation, uniqueness, symmetry reductions, and analytic solutions for trees, wheels and barbell networks. The present proof uses their general framework; their inspected analytical examples do **not** state the priced pineapple formulas or interior optimum. A previously known all-chord screening criterion for priced trees already implies that a uniform star ceases to be optimal when a sufficiently cheap chord is offered. The present contribution is **not** that general KKT criterion: it determines the complete nonzero-chord optimizer for every lower price, its exact Kirchhoff objective, and the simultaneous universal threshold for all \(\binom{k}{2}\) possible clique chords. Haritha and Chithra (2023) give *unit-conductance* resistance distances for pineapple graphs but no priced conductance optimization. Later general work on cost-convexity and support screening (Tovar et al., 2026) treats broader optimization principles but does not explicitly give this family-wide closed allocation. Generic convexity, symmetry, Cauchy–Schwarz, and the star optimum are known tools and are not asserted to be new.

## Limitations

The classification concerns this specific complete-core/pendant-leaf topology, two unit-cost edge orbits and one common positive relative price on the remaining clique edges. Only linear expenditure is treated; a different edge-price pattern or nonlinear cost can change the optimizer. The result is an explicit graph-family specialization of a classical convex program, not a new general SDP or resistance principle. It remains possible that an equivalent pineapple-specific formula appears in incompletely indexed older sources; full exhaustive novelty cannot be certified. Numerical checks cover only finite parameter samples and provide no independent validation.

## References

1. A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review **50** (2008), 37–66, DOI:10.1137/050645452, available at https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf (publicly published 2008-02-01).
2. Haritha T. and A. V. Chithra, *Resistance distance in k-coalescence of certain graphs*, arXiv:2309.02704v1 (2023), especially Proposition 3.2 for unit-weight pineapple networks.
3. H. Tovar et al., *Cost convexity controls the architecture of resistance-optimal networks*, arXiv:2610.03627v1 (2026), for general support-price and convexity context.
