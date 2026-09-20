# Review

## Correctness

**PASS.**

The proof separates into a metric-transport lemma and an application of Zhang--Jin's existence theorem.

For a fixed closed hemisphere \(H_v\), every coupling from \(\mu\) to a measure supported in \(H_v\) pays pointwise at least \(d_S(u,H_v)^p\). A Borel nearest-point selector attains that lower bound, so the distance to \(\mathcal P(H_v)\) is exactly the \(L^p(\mu)\)-norm of the point-to-hemisphere distance. Minimization over the compact parameter sphere gives the distance to the union of all hemisphere-supported measures. The spherical formula \(d_S(u,H_v)=\arcsin((-u\cdot v)_+)\) has the correct endpoint values, including \(\pi/2\) at \(u=-v\).

The positivity criterion is exact because a measure outside every closed hemisphere gives a strictly positive continuous objective for every \(v\), and compactness turns pointwise positivity into a positive minimum. Conversely, concentration on one hemisphere makes the minimum zero.

The closedness, openness, density, and convexity statements were checked separately. Concavity follows because \(\Delta_p^p\) is the infimum of linear functionals; the stronger displayed concavity of \(\Delta_p\) then follows from the weighted power-mean inequality. The \(1\)-Lipschitz property is the standard distance-to-a-set estimate.

The one-sided \(L^p\) moment body formula was checked from its support function: positive homogeneity and subadditivity follow from the positive-part inequality and Minkowski's inequality. Its centered inradius is the minimum \(L^p\) positive-projection norm, and the factor-\(\pi/2\) comparison follows pointwise from \(x\le\arcsin x\le(\pi/2)x\). At \(p=\infty\), the fixed-support transport formula reduces to a maximum over \(\operatorname{supp}\mu\); the separating-hyperplane criterion identifies admissibility with \(0\in\operatorname{int}\operatorname{conv}(\operatorname{supp}\mu)\), giving the exact \(\arcsin\) of the centered inradius.

Zhang--Jin Theorem 1.5 supplies exactly the needed equivalence between affine-dual Minkowski solvability and the closed-hemisphere condition for \(n\ge3\), \(2\le m\le n-1\). Their Section 2.4 states \(mn\)-homogeneity, validating normalization to probability data.

No hidden uniqueness or stability of the realizing convex body is inferred.

## Originality

**PASS, to the best of our knowledge.**

The current Zhang--Jin v1 was inspected at its theorem statement, preliminaries, and continuity section. It gives the qualitative necessary-and-sufficient hemisphere criterion and records weak continuity of affine dual curvature measures, but no Wasserstein robustness radius, transport distance to the nonsolvable locus, nearest nonsolvable perturbation, concavity statement, \(L^p\)-moment-body inradius comparison, or \(W_\infty\) convex-hull formula was located. Searches using combinations of “affine dual Minkowski”, “closed hemisphere”, “Wasserstein”, “robustness”, “stability”, and “distance to degeneracy” did not locate a matching result, and the current SCOPE archive had no matching affine-dual/Wasserstein record.

The closest conceptual ingredients are standard: distance from a probability measure to measures supported on one fixed closed set is obtained by nearest-point transport, and many Minkowski-type existence theorems use a “not concentrated on a closed hemisphere” hypothesis. Those ingredients are not claimed as new. The claimed finding is the exact sharp stability geometry produced when they are combined with the newly completed Zhang--Jin characterization.

The 2025 Cai--Leng--Wu--Xi paper *Affine dual Minkowski problems* is the most relevant source not inspected in full. Available bibliographic descriptions indicate that it introduces the affine dual measures and solves the even problem. Because a full-text search for a Wasserstein stability statement was not available here, it remains the main residual literature risk. The very recent date of Zhang--Jin's preprint also leaves a real possibility of later-version or not-yet-indexed parallel observations.

## Value

**PASS.**

The qualitative solvability boundary becomes quantitatively exact: \(\Delta_p\) gives the maximal Wasserstein perturbation radius preserving existence and constructs a nearest adversarial datum attaining failure. The additional convexity, openness/density, concavity, and \(1\)-Lipschitz properties give a usable geometry of the admissible data set rather than only a reformulation of the existence theorem. The one-sided \(L^p\) moment body comparison supplies a Euclidean convex-geometric surrogate within a universal factor, while the \(W_\infty\) endpoint is exactly the arcsine of the centered inradius of the support convex hull. This is especially useful for approximation or noisy-data versions of the affine dual Minkowski problem, where weak convergence alone does not provide a numerical margin to degeneracy.

The result deliberately stops short of claiming stability of solution bodies, which would require substantially more analysis.

## Limitations

The statement is confined to the Zhang--Jin range \(n\ge3\), \(2\le m\le n-1\), and to normalized fixed-mass data for the Wasserstein metric. It gives no quantitative control of a realizing body, no uniqueness result, and no uniform positive lower bound on \(\Delta_p\) over all admissible data. The motivating theorem is extremely recent, and the inaccessible full text of Cai--Leng--Wu--Xi (2025) leaves a residual originality risk.

Same-model review: passed. Independent audit: not yet performed.
