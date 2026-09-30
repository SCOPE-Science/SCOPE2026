# Independent Audit — 2026/09/21/gamma-monotonicity-critical-tau-bracket--04bd6407a2a1

- Audit date: 2026-09-30 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `0e72fbbe2e6200e9fecef0259f0d618548f7e16d`
- Disposition: **PASSED**

## Correctness

**PASS** — The derivative criterion A_tau=psi D_tau-logGamma D_tau' is correct. The Binet/Stirling comparison gives logGamma<S and psi>S' on the required range, so A_tau exceeds P_tau=S'D-SD'. The supplied directed-interval verifier certifies P_212.435>0 on [2.23,15]; an independent dense numerical check located the minimum near x=8.89147 at about 2.38e-7, consistent with the positive certified margin. For x>=15 the displayed quartic numerator of D'' has negative value and derivative at 15 and strictly negative second derivative, hence D''<0; therefore P' >0. The 2017 source's small-x lemmas cover tau>1 through x3≈2.2324 and its old theorem covers tau<=25. Its ratio-monotonicity theorem correctly propagates the T=212.435 tail inequality to all smaller tau. At x=9 the exact digamma/Gamma values produce the stated scalar equation, and directed interval arithmetic brackets its unique root in (212.508612771,212.508612772), above which u_tau'(9)<0.

## Originality

**PASS** — Kupán-Márton-Szász proved only tau<=25 rigorously, exhibited failure at tau=1000, and reported numerical evidence for a transition in (212,213). The audited result converts that numerical location into a rigorous narrow bracket and extends the proven sufficient endpoint to 212.435. Targeted searches by the quotient, source paper, numerical transition, and exact new constants found no later theorem resolving this interval. The novelty is the certified extension/bracket, not the Binet formula or monotone-l'Hospital machinery.

## Scientific value

**PASS** — The result turns a decade-old numerical transition into a rigorous near-sharp phase bracket of width below 0.074 while increasing the known sufficient parameter range by more than a factor of eight. The remaining gap and the computer-assisted component are transparent and reproducible.

## Sources

- **A result regarding monotonicity of the Gamma function** — P. A. Kupán; Gy. Márton; R. Szász. https://doi.org/10.1515/ausm-2017-0022 — Primary source: proves tau<=25, gives a tau=1000 counterexample, reports numerical critical behavior in (212,213), and supplies the ratio-monotonicity/small-x lemmas reused here.
- **A refinement of a double inequality for the gamma function** — J.-L. Zhao; B.-N. Guo; F. Qi. https://arxiv.org/abs/1001.1495 — Earlier source of the all-tau monotonicity conjecture later refuted by Kupán-Márton-Szász.
- **DLMF §5.9 Integral Representations** — NIST Digital Library of Mathematical Functions. https://dlmf.nist.gov/5.9 — Standard Binet integral background used in the analytic certificate.

## Limitations

- The exact critical value tau_c remains undetermined.
- No claim is made that strict monotonicity fails at tau=tau_9 itself.
- The lower endpoint 212.435 relies on a reproducible interval-arithmetic certificate rather than a formal proof assistant.
- A later result under substantially different notation remains a residual originality risk.

## Independent checks

```json
{
  "derivative_reduction_reconstructed": true,
  "source_small_x_scope_checked": true,
  "ratio_monotonicity_direction_checked": true,
  "interval_verifier_inspected": true,
  "independent_dense_minimum_x": 8.8914705,
  "independent_dense_minimum_P": 2.3794097940463617e-07,
  "tau9_interval_logic_checked": true,
  "source_tree_unchanged": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned record tree was unchanged from the inventory snapshot through the checked commit. GitHub was used only as read-only evidence. Open-access and preprint sources were checked first, and no decisive comparison required institutional retrieval. No GitHub write or separate dispatcher report was performed.
