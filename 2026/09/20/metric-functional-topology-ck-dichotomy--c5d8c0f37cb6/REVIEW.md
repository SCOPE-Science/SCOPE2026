# Same-model review

## Correctness

**Verdict: PASS.**

The topology comparison has two independent ingredients. First, every internal metric functional on a normed space is convex and 1-Lipschitz, and pointwise limits preserve those properties. Hence every metric functional is continuous convex and therefore weakly lower semicontinuous, which makes every basic metric-functional open set classically weak-open. Second, Walsh's Corollary 3.5 identifies extreme dual-ball functionals with metric/Busemann functionals; central symmetry supplies both signs, so each extreme functional is continuous for the metric-functional topology. This proves the sandwich
\[
\sigma(X,\operatorname{ext}B_{X^*})\subseteq\sigma(X,X^\diamond)\subseteq\sigma(X,X^*).
\]
The finite-dimensional and strictly-convex-dual equalities then follow from elementary spanning facts.

The finite-codimensional-neighborhood statement follows from a standard subgradient at the origin for each continuous convex metric functional. Intersecting the kernels of finitely many supporting functionals produces a subspace contained in the basic neighborhood. Translation is legitimate because the recent topology theorem proves that surjective isometries induce homeomorphisms.

For C(K), the only topological input is that every infinite compact Hausdorff space contains countably many pairwise disjoint nonempty open sets and, by normality, supports continuous bump functions inside them. For an internal metric functional h_w, a point where |w| attains its maximum lies in at most one bump support, so h_w can be negative on at most one bump. Pointwise closure transfers this property to every metric functional. The d-weak liminf criterion then gives convergence for arbitrary prescribed positive amplitudes. The finite case reduces to finite-dimensional topology equality. No computation is required.

## Originality

**Verdict: PASS, to the best of our knowledge.**

The full text of Gutiérrez--Nevanlinna, arXiv:2609.19368v1 (2026-09-16), was inspected. It proves that the new topology is coarser than the metric topology and gives one unbounded d-weakly null sequence in C[0,1]. Its current version does not state a comparison with the classical weak topology, a finite-dimensional topology identification, a finite-codimensional-neighborhood theorem, or a C(K) compact-Hausdorff dichotomy.

The earlier paper *Metric functionals and weak convergence* was checked for the relevant linear results. It proves bounded sequential equivalence with classical weak convergence and invokes Walsh's result on extreme dual functionals. It also originally asserted boundedness in C[0,1], an assertion explicitly corrected by the September 2026 preprint. Its strictly-convex-dual result is sequential; the present sandwich gives equality of the two topologies, hence equivalence for arbitrary nets.

Walsh's 2018 paper was checked at the relevant Corollary 3.5, which identifies singleton Busemann points of a normed space with extreme points of the dual ball. That ingredient is prior work and is not claimed as new.

Targeted searches for the combinations “metric-functional topology” with classical weak topology, finite-dimensional normed spaces, and C(K), and for d-weak unbounded sequences on general C(K), did not locate an equivalent theorem. No inaccessible paper was identified as especially likely to contain the full package. The main residual originality risk is conceptual proximity: the C(K) proof is a natural topological generalization of the disjoint-support argument used for C[0,1], and a future revision or unindexed note could state it explicitly.

## Value

**Verdict: PASS.**

The result places the newly introduced topology precisely relative to familiar Banach-space weak topologies, upgrades known sequential behavior to topology-level equalities for broad classes, and gives a complete finite-versus-infinite classification for C(K). The arbitrary norm-profile theorem shows that the C[0,1] counterexample is not an interval-specific pathology but a universal phenomenon for infinite compact Hausdorff function spaces. The finite-codimensional-neighborhood statement gives a simple geometric description of local largeness in every infinite-dimensional normed space.

## Limitations

The algebraic-span condition on extreme dual functionals is sufficient, not claimed necessary, so the equality problem for general infinite-dimensional normed spaces remains open. The C(K) theorem is qualitative and gives no quantitative modulus. Its proof is closely related to the recent C[0,1] construction, which increases the chance of parallel or subsequent rediscovery.

Same-model review: passed. Independent audit: not yet performed.
