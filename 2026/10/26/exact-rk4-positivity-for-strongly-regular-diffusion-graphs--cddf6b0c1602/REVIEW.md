# Self-review

## Correctness — PASS
The specified graph class has an adjacency algebra spanned by \(I,A,J\). The derived nonedge RK4 entry has a positive quadratic factor because its exact discriminant is \(-16[5k(k-\lambda+\mu)+3(k-\mu)+2(\lambda-\mu)^2]\). The diagonal is positive by the sum-of-squares scalar RK4 identity. At edges the spectral projector has positive \(\alpha\)-coefficient and negative \(\beta\)-coefficient; writing \(M_j\) as a difference of two geometric terms gives the strict \(M_3^2/(M_2M_4)<4/3\) inequality and a globally negative derivative for the cutoff cubic. The spectral-stability comparison uses the exact projectors at \(h=\rho/\beta\), not an unproved inference from norm stability. The triangular graph's nine-vertex crossover follows from a verified integer polynomial sign. Reproducible algebraic and exact-rational checks are embedded; they corroborate rather than replace infinite-graph proof.

## Originality — PASS with residual uncertainty
The full accessible mathematical context of Gottlieb–Shu–Tadmor (2001), the relevant exact SSP construction and linear-operator sections of Gottlieb–Gottlieb (2003), and chapter 9 of Brouwer–Haemers (2011 preprint) were compared by mathematical implication. The earlier methods and SRG spectral facts do not state the universal strict nonedge positivity, unique graph-specific RK4 cutoff, or primitive/imprimitive equivalence with spectral stability. The closest recovered graph-diffusion results treat complete multipartite graphs, maximum-degree-two paths/cycles, rectangular rook graphs, weighted stars or Gauss RK methods; the present non-imprimitive classification does not follow from those specialized claims. The search is not proof of global novelty, and specialized omitted literature remains a risk.

## Value — PASS
Numerical diffusion positivity and Euclidean spectral stability are distinct requirements. On the wide class of strongly regular graphs this result replaces a matrix-by-matrix positivity check with a scalar cubic and identifies, for every graph in the class, exactly which transitions fail, with no reentry. The sharp dichotomy characterizes the complete multipartite cases where spectral stability suffices and all primitive cases where it does not. The triangular-graph corollary gives a concrete size threshold at which RK4 permits more than twice the Euler-safe step, making the exact invariant interpretable for network diffusion safety.

## Limits
Only the completed classical RK4 step for unweighted undirected graphs is treated. Historical specialist coverage remains possible. Finite tests and this review do not constitute an independent audit.

Self-review: passed. Independent audit: not yet performed.
