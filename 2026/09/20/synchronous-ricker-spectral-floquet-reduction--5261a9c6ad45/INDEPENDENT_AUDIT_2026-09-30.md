# Independent Audit — 2026/09/20/synchronous-ricker-spectral-floquet-reduction--5261a9c6ad45

- Audit date: 2026-09-30 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `6dfda0f63b8ee0a689d8acbc38ccf042871ba6ec`
- Disposition: **PASSED**

## Correctness

**PASS** — At a synchronized point z_k 1, row regularity gives A(z_k 1)=c z_k 1 and the exact Jacobian J_k=e^(r-w_k)(I-z_k A)=(z_{k+1}/z_k)(I-(w_k/c)A). The matrix factors are polynomials in one fixed matrix A, so they commute, while the scalar factors telescope around the cycle. Hence the monodromy is exactly P_p(A)=product_k(I-(w_k/c)A), and polynomial spectral mapping gives the stated Floquet multipliers. For every nonzero eigenvalue with Re(lambda)<=0, |1-t lambda|>1 for t>0, so the period-independent instability obstruction is strict. The uniform all-to-all spectrum and the directed-cycle spectrum give the stated thresholds, and at a=1 identical rows make component ratios exactly invariant. The broader common-response formula follows by the same Jacobian differentiation without the Ricker telescoping simplification.

## Originality

**PASS** — Planar symmetric Ricker bifurcations, n-species persistence/exclusion theory, almost-periodic coupled Ricker stability, and generic master-stability eigenmode decompositions are prior art. The checked sources do not state the submitted arbitrary-dimensional row-regular autonomous formula in which every Jacobian is an affine polynomial in the competition matrix and the complete p-cycle monodromy collapses to one explicit polynomial P_p(A), nor the resulting closed-left-half-plane obstruction for every positive period. The closest overlap risk is the N-dimensional extension described in Ryals-Sacker's almost-periodic coupling paper; only its accessible statement/abstract was available in this audit, so the novelty conclusion is appropriately limited to the exact competition-matrix polynomial and its consequences rather than to synchronization-by-eigenmodes generally.

## Scientific value

**PASS** — Within the row-regular synchronous sector the result removes the dimension-dependent Floquet product entirely and turns local cycle stability into evaluation of a scalar polynomial on the interaction spectrum. The period-independent spectral obstruction and explicit uniform/cyclic examples give useful structural diagnostics, while the theorem correctly stops short of cycle existence or global dynamics.

## Sources

- **The discrete dynamics of symmetric competition in the plane** — H. Jiang; T. D. Rogers. https://doi.org/10.1007/BF00275495 — Classical planar symmetric Ricker low-period/bifurcation analysis.
- **Competitive exclusion and coexistence in an n-species Ricker model** — A. S. Ackleh; P. L. Salceanu. https://doi.org/10.1080/17513758.2015.1020576 — Prior n-species persistence/exclusion theory; no matching row-regular Floquet polynomial was located.
- **Bifurcation in the almost periodic 2D Ricker map** — B. Ryals; R. J. Sacker. https://doi.org/10.3934/dcdsb.2021089 — Closest synchronization/stability comparison; accessible statement reports Lyapunov criteria and an N-dimensional coupling extension, not the audited autonomous competition-matrix polynomial.
- **Open Problems and Conjectures in the Evolutionary Periodic Ricker Competition Model** — R. Luis. https://doi.org/10.3390/axioms13040246 — Recent survey context emphasizing the difficulty of higher-dimensional periodic Ricker dynamics.

## Limitations

- The row-sum condition and common intrinsic response are essential to the exact synchronous reduction.
- The theorem is local and does not prove existence of the scalar cycle, persistence, global attraction, or absence of nonsynchronous attractors.
- Unit-modulus multipliers generally require nonlinear analysis.
- The full theorem-level text of the closest Ryals-Sacker N-dimensional almost-periodic extension was not obtained in this audit, leaving a residual originality risk.

## Independent checks

```json
{
  "jacobian_formula_rederived": true,
  "telescoping_monodromy_checked": true,
  "spectral_mapping_checked": true,
  "left_half_plane_obstruction_checked": true,
  "uniform_competition_threshold_checked": true,
  "directed_cycle_threshold_checked": true,
  "open_access_first": true,
  "oxford_used": false,
  "decisive_inaccessible_comparison": false
}
```

The assigned record tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation or separate dispatcher report was performed. Open-access/preprint sources were checked before institutional retrieval. Any inaccessible comparison is explicitly identified and is not claimed read.
