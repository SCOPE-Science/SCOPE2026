# Independent Audit — 2026/09/20/symmetric-gmres1-euclidean-error-barrier--89eb763dddfc

- Audit date: 2026-09-30 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `acf3c17204359c4bc5f87bf0fe38bdf055da5e6a`
- Disposition: **PASSED**

## Correctness

**PASS** — For symmetric A and normalized error e, the MRI/GMRES(1) step has alpha=m_3/m_4 and therefore sum_i w_i z_i^3(1-z_i)=0 for z_i=alpha lambda_i. Averaging the exact scalar identity 4/3-(1-z)^2-12 z^3(1-z)=(6z^2-3z-1)^2/3 yields the sharp squared error ratio at most 4/3. Equality forces the two roots (3+-sqrt(33))/12 and the submitted weight; direct substitution gives alpha_0=1, alpha_1=-2, e_2=(2/3)e_0, first-step error factor 2/sqrt(3), second-step factor 1/sqrt(3), and residual factor sqrt(2/3) at each alternating step. The definite-case moment inequality has the correct sign and proves strict Euclidean error decrease for nontrivial SPD/SND steps. The 2-by-2 diag(1,-t) calculation shows amplification for every absolute condition number t>1 arbitrarily close to one, while the nonsymmetric Jordan family has unbounded error amplification.

## Originality

**PASS** — Saad's 2000 paper was obtained through authorized institutional access and checked through its residual-bound, restarted-Min-Res, and GMRES sections; it analyzes residual reduction and explicitly notes the indefinite obstruction, but does not state the sharp Euclidean solution-error factor 2/sqrt(3), equality pair, or alternating equality cycle. Weiss and Meurant treat solution-error behavior/estimation more broadly, and searches for the exact constants and equality spectrum found no match. Fridman's 1963 minimum-error paper is the most important historical residual risk: open metadata and secondary historical descriptions identify a different error-minimizing iteration, but its publisher full text could not be inspected because authorized retrieval stopped at human verification. That inaccessible text is not claimed read. On the evidence available, the source-specific sharp one-step barrier and equality dynamics remain original.

## Scientific value

**PASS** — The theorem gives a dimension-free, spectrum-scale-free sharp limit on how badly a residual-minimizing step can transiently increase Euclidean solution error for symmetric indefinite systems. Its exact two-cycle shows the worst spike can recur while residuals decrease steadily, and the nonsymmetric comparison isolates symmetry as the structural reason a universal bound exists.

## Sources

- **Further Analysis of Minimum Residual Iterations** — Yousef Saad. https://doi.org/10.1002/(SICI)1099-1506(200003)7:2%3C67::AID-NLA186%3E3.0.CO;2-8 — Authorized full text checked after open-access attempts; focuses on residual bounds and restarted Min-Res/GMRES behavior, not the audited sharp solution-error barrier.
- **Error-Minimizing Krylov Subspace Methods** — Richard Weiss. https://doi.org/10.1137/0915034 — Prior qualitative separation between residual minimization and solution-error behavior.
- **Estimates of the Norm of the Error in Solving Linear Systems with FOM and GMRES** — Gerard Meurant. https://doi.org/10.1137/100795565 — Prior solution-error estimation literature; no matching one-step 2/sqrt(3) theorem was located.
- **The method of minimum iterations with minimum errors for a system of linear algebraic equations with a symmetrical matrix** — V. M. Fridman. https://doi.org/10.1016/0041-5553(63)90412-9 — Historical comparison. Full publisher text remained inaccessible because authorized retrieval required human verification; it is not claimed read.

## Limitations

- The result is exact-arithmetic and specifically for unpreconditioned one-direction restarted minimal residual iteration on real symmetric nonsingular matrices.
- It does not imply convergence for indefinite systems; alpha can vanish and GMRES(1) can stagnate.
- It does not apply to nonsymmetric matrices, flexible/variable preconditioning, or finite-precision recurrences.
- Fridman's 1963 full text remained inaccessible after lawful retrieval attempts; available evidence indicates a distinct error-minimizing method, but this leaves residual historical-priority risk.

## Independent checks

```json
{
  "moment_identity_reconstructed": true,
  "scalar_square_identity_checked": true,
  "equality_weights_and_two_cycle_checked": true,
  "definite_case_moment_inequality_checked": true,
  "condition_number_counterexample_checked": true,
  "nonsymmetric_unbounded_family_checked": true,
  "open_access_first": true,
  "oxford_used": true,
  "saad_2000_job_id": "f1e27759da9257f9344b9bb2d56f8968",
  "saad_2000_status": "complete",
  "saad_pages_checked": "1-24 of 27",
  "fridman_1963_job_id": "5e7ff7fed28cff7846e6a059bb4f5af4",
  "fridman_1963_status": "needs_human",
  "fridman_full_text_not_claimed_read": true
}
```

The assigned record tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation or separate dispatcher report was performed. Open-access/preprint sources were checked before institutional retrieval. Any inaccessible comparison is explicitly identified and is not claimed read.
