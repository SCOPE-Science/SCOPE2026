# Independent Audit — 2026/09/20/metric-functional-topology-ck-dichotomy--c5d8c0f37cb6

- Audit date: 2026-09-30 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `51fed15b9e01afa85b00fbd9d9f59d857e38b2db`
- Disposition: **PASSED**

## Correctness

**PASS** — The topology comparison and C(K) dichotomy are correct under the source definition of the one-sided metric-functional topology. Every metric functional is a pointwise limit of convex 1-Lipschitz internal functions, hence is convex, norm-continuous and weakly lower semicontinuous; therefore its strict superlevel sets are weakly open and tau_diamond is coarser than the classical weak topology. Walsh's result places every extreme dual-ball functional in X^diamond; applying it to both e and -e makes each extreme functional tau_diamond-continuous, giving sigma(X,ext B_X*) subset tau_diamond. A supporting functional at 0 for each convex h yields the finite-codimensional subspace contained in every basic 0-neighborhood. For infinite compact Hausdorff K, a countable disjoint family of nonempty open sets exists; normality supplies disjointly supported continuous bumps with arbitrary positive heights. An internal h_w can be negative on at most one bump because a norm-attaining point of w lies outside all but one support. Pointwise limits preserve this at-most-one-negative property, so every metric functional has liminf at least 0 and the bumps converge to 0 in tau_diamond. The finite-dimensional converse and weak-boundedness separation are standard.

## Originality

**PASS** — Gutiérrez--Nevanlinna's September 2026 preprint introduces the topology and advertises one unbounded d-weakly null sequence in C[0,1]. Their earlier paper proves equivalence with ordinary weak convergence for bounded sequences and notes boundedness under strictly convex duals. The inspected sources do not state the topology sandwich via extreme points, the finite-codimensional-neighborhood property, or the all-compact-Hausdorff C(K) dichotomy with arbitrary norm profiles. Walsh supplies the extreme-point metric-functional ingredient, not these consequences. The C(K) extension is conceptually close to the new C[0,1] example, so near-simultaneous follow-up remains a residual risk.

## Scientific value

**PASS** — The result gives a sharp structural picture of the new topology on a major Banach-space class: equality with weak topology for finite K and strict inequality for every infinite compact Hausdorff K, with arbitrarily prescribed norm growth and even norm-unbounded compact convergent sequences. The finite-codimensional neighborhood theorem also explains why infinite-dimensional open sets are necessarily norm-unbounded.

## Sources

- **A Weak Topology on Metric Spaces** — Armando W. Gutiérrez; Olavi Nevanlinna. https://arxiv.org/abs/2609.19368 — Introduces the topology associated with d-weak convergence and constructs an unbounded d-weakly null sequence in C[0,1].
- **Metric functionals and weak convergence** — Armando W. Gutiérrez; Olavi Nevanlinna. https://doi.org/10.4171/ZAA/1828 — Shows bounded d-weak sequences in normed spaces agree with classical weak convergence; uses extreme dual points and treats the strictly convex-dual boundedness consequence.
- **Hilbert and Thompson geometries isometric to infinite-dimensional Banach spaces** — Cormac Walsh. https://doi.org/10.5802/aif.3198 — Provides the extreme-dual-point metric-functional fact used in the topology sandwich.

## Limitations

- The algebraic span of extreme dual functionals is only a sufficient condition for tau_diamond=tau_w, not a characterization.
- The C(K) result is qualitative/topological and gives no rates.
- Because the C(K) argument directly generalizes a September 2026 C[0,1] counterexample, concurrent follow-up work is a material priority risk.

## Independent checks

```json
{
  "proof_reconstructed": true,
  "weak_lsc_superlevel_argument_checked": true,
  "finite_codimension_subgradient_argument_checked": true,
  "CK_disjoint_support_argument_checked": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation or separate dispatcher report was performed. Open-access and preprint sources were checked first; no decisive comparison remained inaccessible, so Oxford Download was not required.
