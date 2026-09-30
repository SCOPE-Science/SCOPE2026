# Independent Audit — 2026/09/21/odd-cycle-identification-symmetric-measurement-errors--1c8863f1cbd5

- Audit date: 2026-09-30 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `123906220f270666512c53fc8fe1769d5d4b80df`
- Disposition: **PASSED**

## Correctness

**PASS** — Central symmetry makes each characteristic function real and even; continuity, phi_i(0)=1, and nowhere-vanishing force phi_i>0. Hence each observed difference law gives the exact additive log equation a_i+a_j=b_ij. The nullspace of this unsigned incidence system on a connected component is one-dimensional exactly when the component is bipartite and zero exactly when it contains an odd cycle, which proves the identification criterion and constructive odd-cycle recursion. The Gaussian variance perturbation +c on one bipartition and -c on the other preserves every edge-difference law and, after a compensating latent-variance adjustment, can preserve one absolute marginal. The m-edge minimum follows because every connected non-bipartite k-vertex component needs at least k edges, while a triangle with tree attachments achieves equality. Independent exhaustive graph checks through five vertices found no discrepancy between full unsigned-incidence rank and non-bipartiteness.

## Originality

**PASS** — Three-cornered-hat literature classically solves variance equations, while Kotlarski-type repeated-measurement results use the richer joint distribution of repeated measurements. Nonparametric triple-collocation work addresses a different observation model and underdetermination problem. Targeted searches did not locate full error-distribution identification from only selected pairwise-difference marginals with the exact odd-cycle graph criterion, Gaussian bipartite alias, and m-edge minimal design. The unsigned-incidence rank fact and characteristic-function algebra themselves are classical.

## Scientific value

**PASS** — The theorem upgrades variance-only comparison designs to exact distributional identification under transparent assumptions and turns the design question into a sharp graph property. The matching Gaussian nonidentification construction demonstrates necessity inside a smooth familiar model, and the m-edge design gives an immediately usable sparse measurement layout.

## Sources

- **A Method for Estimating the Frequency Stability of an Individual Oscillator** — J. E. Gray; D. W. Allan. https://tf.nist.gov/general/pdf/57.pdf — Classical three-cornered-hat variance reconstruction.
- **Nonparametric triple collocation** — G. S. Nearing et al.. https://doi.org/10.1002/2017WR020359 — Different nonparametric triple-collocation framework based on information quantities.
- **Nonparametric simulation extrapolation for measurement-error models** — I. Spicker. https://doi.org/10.1002/cjs.11777 — Recent symmetric replicate-error methodology without the heterogeneous-error odd-cycle reconstruction.
- **On characterizing the gamma and the normal distribution** — I. I. Kotlarski. https://projecteuclid.org/journals/pacific-journal-of-mathematics/volume-20/issue-1/On-characterizing-the-gamma-and-the-normal-distribution/pjm/1102992112.full — Classical repeated-measurement identification uses joint distributions rather than sparse marginal pairwise-difference laws.

## Limitations

- Identification is population-level and can be numerically ill-conditioned where characteristic functions are small.
- Mutual independence, central symmetry about known zero, and nowhere-zero error characteristic functions are essential assumptions.
- Without symmetry, phases remain unidentified by the present log-linear argument; characteristic-function zeros also require separate analysis.
- The graph-linear-algebra core is elementary, leaving a residual folklore-priority risk.

## Independent checks

```json
{
  "positive_characteristic_function_argument_checked": true,
  "unsigned_incidence_nullspace_proof_checked": true,
  "odd_cycle_reconstruction_checked": true,
  "gaussian_bipartite_alias_checked": true,
  "minimal_edge_count_checked": true,
  "connected_graph_rank_exhaustive_through_vertices": 5,
  "source_tree_unchanged": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned record tree was unchanged between the inventory snapshot and the checked commit. GitHub was used only as read-only evidence; no repository mutation or separate dispatcher report was performed. Open-access and preprint sources were checked first, with authorized institutional retrieval used only where a directly relevant full text remained unavailable.
