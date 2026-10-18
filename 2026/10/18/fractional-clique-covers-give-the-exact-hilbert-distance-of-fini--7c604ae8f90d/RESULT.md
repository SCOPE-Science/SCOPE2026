# Fractional clique covers give the exact Hilbert distance of finite quadratic combinatorial spaces

## Finding
Let \(n\ge1\), and let \(\mathcal F\) be a finite hereditary family of subsets of \([n]\) containing every singleton. Define the real normed space \(X_{\mathcal F,2}\) on \(\mathbb R^n\) by
\[
N_{\mathcal F}(x)=\max_{F\in\mathcal F}\left(\sum_{i\in F}x_i^2\right)^{1/2}.
\]
Define its fractional cover number by the finite linear program
\[
\tau^*(\mathcal F)=\min\left\{\sum_{F\in\mathcal F}\lambda_F:\lambda_F\ge0,\ \sum_{F\ni i}\lambda_F\ge1\ \text{for every }i\in[n]\right\}.
\]
Then the unrestricted, real-linear Banach–Mazur distance to Hilbert space satisfies
\[
\boxed{d_{\mathrm{BM}}(X_{\mathcal F,2},\ell_2^n)^2=\tau^*(\mathcal F).}
\]
**The standard coordinate Euclidean norm is already an optimal Hilbertian comparison**, even when \(\mathcal F\) has no coordinate-permutation symmetry. In particular, the squared distance is rational and is explicitly computable by linear programming.

For any finite simple graph \(G\), let \(\mathcal C(G)\) be its clique family, including singletons. Then
\[
\boxed{d_{\mathrm{BM}}(X_{\mathcal C(G),2},\ell_2^{|V(G)|})^2=\chi_f(\overline G),}
\]
where \(\chi_f\) is the fractional chromatic number. Consequently, \(G\) is perfect **if and only if** this squared Hilbert distance is an integer for every nonempty vertex-induced coordinate subspace \(X_{\mathcal C(G[S]),2}\). The converse uses the published strong perfect graph theorem, not a new proof of that theorem.

## Assumptions and scope
All scalars are real. The Banach–Mazur distance is the infimum \(\inf_{T}\|T\|\|T^{-1}\|\) over **all** invertible real-linear maps \(T:X_{\mathcal F,2}\to\ell_2^n\), rather than only the coordinate identity. Every singleton lies in \(\mathcal F\), so \(N_{\mathcal F}(e_i)=1\), and every \(F\) is a subset of \([n]\), so \(N_{\mathcal F}(x)\le\|x\|_2\). The empty set, if present in the hereditary family, contributes a zero term and a redundant linear-program variable. For graphs, a clique is allowed to have one vertex; isolated vertices require no exception. A perfect graph is one for which every induced subgraph has chromatic number equal to its clique number.

## Proof
**1. No rotated or anisotropic ellipsoid can improve the Euclidean comparison.** Given \(K\ge1\), the inequality \(d_{\mathrm{BM}}(X_{\mathcal F,2},\ell_2^n)\le K\) is attained exactly when some positive-definite real symmetric matrix \(A\), after a positive rescaling, satisfies
\[
N_{\mathcal F}(x)^2\le x^{\mathsf T}Ax\le K^2N_{\mathcal F}(x)^2\qquad(x\in\mathbb R^n).
\]
(The minimum exists in finite dimension; alternatively, the argument below applies to every feasible \(K\) and then to the infimum.) For each sign vector \(\varepsilon\in\{-1,1\}^n\), put \(D_\varepsilon=\operatorname{diag}(\varepsilon)\). Because \(N_{\mathcal F}(D_\varepsilon x)=N_{\mathcal F}(x)\), conjugating the two quadratic inequalities by \(D_\varepsilon\) preserves them. Averaging over the \(2^n\) sign vectors gives a feasible diagonal matrix
\[
A_0=2^{-n}\sum_\varepsilon D_\varepsilon A D_\varepsilon=\operatorname{diag}(a_1,\ldots,a_n).
\]
Putting \(x=e_i\) in the lower inequality shows \(a_i\ge1\) for every \(i\). Hence, for **every** real vector \(x\),
\[
\|x\|_2^2\le x^{\mathsf T}A_0x\le K^2N_{\mathcal F}(x)^2.
\]
Thus every Hilbertian comparison satisfies \(K^2\ge R\), where
\[
R:=\max_{x\ne0}\frac{\|x\|_2^2}{N_{\mathcal F}(x)^2}.
\]
Conversely, the Euclidean matrix \(A=I\) satisfies \(N_{\mathcal F}(x)^2\le\|x\|_2^2\le R N_{\mathcal F}(x)^2\). Therefore \(d_{\mathrm{BM}}^2=R\), with no unproved optimal-ellipsoid assertion.

**2. Identification with a finite fractional-cover program.** Because the expression for \(R\) is homogeneous and the norm is the maximum of coordinate-square sums,
\[
R=\max\left\{\sum_{i=1}^n t_i:t_i\ge0,\ \sum_{i\in F}t_i\le1\ (F\in\mathcal F)\right\}.
\]
Indeed, any feasible \(t\) is realized by \(x_i=\sqrt{t_i}\); conversely, put \(t_i=x_i^2\) for every \(x\) of norm at most one. This primal program is feasible and bounded because all singletons belong to \(\mathcal F\). Its finite-dimensional LP dual is exactly the fractional-cover minimization defining \(\tau^*(\mathcal F)\). Both have finite optima, so strong LP duality proves the first boxed equality.

**3. Graph specialization.** The cliques of \(G\) are exactly the stable sets of \(\overline G\). By the **definition** of fractional chromatic number as minimum nonnegative total weight of stable sets covering each vertex, the cover program is \(\chi_f(\overline G)\). This proves the second boxed equality without requiring \(G\) to be perfect.

**4. Perfectness detected by induced distances.** If \(G\) is perfect, so is its complement by the perfect graph theorem. For every induced \(H\), the elementary coloring bounds \(\omega(\overline H)\le\chi_f(\overline H)\le\chi(\overline H)\), together with perfection, give \(\chi_f(\overline H)=\omega(\overline H)\in\mathbb N\). Conversely, if \(G\) is not perfect, the strong perfect graph theorem supplies an induced odd hole or odd antihole on \(m=2k+1\ge5\) vertices. For an odd hole, all maximal cliques are edges: assigning weight \(1/2\) to each vertex in the primal, and weight \(1/2\) to each cycle edge in the dual, gives the common optimum \(m/2\), which is not an integer. For an odd antihole, every clique is an independent set of the underlying odd cycle and has at most \(k\) vertices. Assigning weight \(1/k\) to each vertex therefore gives a feasible primal value \(m/k\). The \(m\) cyclically shifted maximum independent \(k\)-sets cover each vertex exactly \(k\) times, so assigning each such clique dual weight \(1/k\) gives the same value \(m/k=2+1/k\), not an integer. This contradicts the assumed integrality for all induced coordinate subspaces and completes the equivalence.

## Verification
The separate standard-library `checker.py` enumerates rational primal and dual LP vertices for **all 64 labeled simple graphs on four vertices**, and verifies exact matching primal and dual optima in every case. It also checks seven explicit feasible equal-objective primal/dual certificates. The squared Hilbert distances in those cases are \(5/2\) for the five-cycle, \(3\) for the six-cycle, \(7/2\) for the seven-cycle, \(7/3\) for the complement of the seven-cycle, \(1\) for the complete four-vertex graph, \(4\) for the edgeless four-vertex graph, and \(2\) for a four-vertex path. Run `python3 checker.py` from the directory containing that file. These finite calculations support the formulas but are not substituted for the sign-averaging proof and LP duality.

## Relationship to prior work
Fakhoury, *Isometries of \(p\)-convexified combinatorial Banach spaces* (arXiv:2305.13125v1, May 22, 2023), introduces precisely this norm family and studies linear isometries. Her Theorem 1.1 addresses signed-permutation rigidity (with a special issue at exponent \(2\)); the new assertion is instead an **unrestricted optimal Hilbertian distortion** for arbitrary finite hereditary families. Borodulin-Nadzieja, Farkas, Jachimek and Pelczar-Barwacz, *The Zoo of combinatorial Banach spaces* (arXiv:2404.01733v1), studies the related sum-norm construction and structural questions, not this quadratic Hilbert-distance problem.

The published result *Fractional clique-cover norms and the sharp two-threshold for graph-generated Banach spaces* (public mathematical record identifier ending `da23138814f6`) proves fractional-cover identities for **canonical coordinate maps from an \(\ell_1\)-type clique norm into \(\ell_1\)**. It explicitly distinguishes those identities from unrestricted Banach–Mazur distances; their LP duality is relevant background, but it does not establish the sign-symmetrized optimal Hilbert ellipsoid for the \(\ell_2\)-convexification. Borodulin-Nadzieja, Farkas and Pelczar-Barwacz, *Geometric duality, perfect graphs, and the Sierpiński space* (arXiv:2605.14072v1), derives perfect-graph criteria through extreme points and duality for combinatorial **sum** norms. The graph integrality statement here concerns a different metric invariant of a quadratic norm. The finite LP duality, complement coloring inequalities, perfect graph theorem, and strong perfect graph theorem are classical inputs and are not claimed as discoveries.

## Limitations
The result is finite-dimensional and for real quadratic \(2\)-convexified norms with every coordinate represented. It does not determine distances between two different combinatorial spaces, infinite-dimensional Banach–Mazur distances, or quantitative stability of optimal matrices. The perfectness corollary relies on the published strong perfect graph theorem. The proof determines the optimal **value** and at least one optimal Hilbert form, not the full set of optimal forms. Other unindexed or unpublished results might imply an equivalent formula; literature comparison cannot establish absolute uniqueness.

## References
1. M. Fakhoury, *Isometries of \(p\)-convexified combinatorial Banach spaces*, arXiv:2305.13125v1 (May 22, 2023), definition of \(X_{\mathcal F,p}\), Theorem 1.1.
2. P. Borodulin-Nadzieja, B. Farkas, S. Jachimek, A. Pelczar-Barwacz, *The Zoo of combinatorial Banach spaces*, arXiv:2404.01733v1 (April 2, 2024), Section 1.
3. *Fractional clique-cover norms and the sharp two-threshold for graph-generated Banach spaces*, public mathematical result `da23138814f6` (October 11, 2026), general fractional-cover identity for canonical sum-norm coordinate maps.
4. P. Borodulin-Nadzieja, B. Farkas, A. Pelczar-Barwacz, *Geometric duality, perfect graphs, and the Sierpiński space*, arXiv:2605.14072v1 (May 13, 2026), Theorems 4.4–4.6.
5. M. Chudnovsky, N. Robertson, P. Seymour, R. Thomas, *The strong perfect graph theorem*, Annals of Mathematics 164 (2006), 51–229.
