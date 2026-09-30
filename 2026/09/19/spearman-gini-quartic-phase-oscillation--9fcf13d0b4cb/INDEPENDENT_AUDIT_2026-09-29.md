# Independent Audit — 2026/09/19/spearman-gini-quartic-phase-oscillation--9fcf13d0b4cb

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `e0caa80a7f2f54863b5db0b81e35e6a6c7b38a9e`
- Disposition: **PASSED**

## Correctness

**PASS** — Starting from the two source branches, exact symbolic series reversion independently reproduces the record. Both branches have cubic coefficient -(5+3sqrt(3))/2. Their quartic coefficients are K0+16x^3-24x^4 and K0+16(1-x)^3-24(1-x)^4 with K0=39/2+45sqrt(3)/4. The derivative 48u^2(1-2u) is nonnegative on [0,1/2], so the phase range is exactly [K0,K0+1/2]. The exact switch x_N=N/(2N+1) tends to 1/2 and both branch limits coincide there. Thus the universal cubic Peano expansion, quartic phase law, full cluster interval and failure of a fourth-order Peano coefficient are correct.

## Originality

**PASS** — Ansari-Rockel-Steinmaßl's September 2026 paper is the first exact rho-gamma region source located and supplies the countably piecewise algebraic boundary; the auxiliary rho-footrule optimizer was solved only in August 2026. Their public descriptions do not state the audited cubic coefficient, quartic phase function or fourth-order cluster interval. Targeted searches using the exact constants and endpoint/Taylor/Peano terminology did not locate prior coverage. Repository chronology also shows this record predates the later duplicate audited in the same assignment. The originality claim is deliberately restricted to the higher-order endpoint asymptotics, not the exact boundary or transport optimizer.

## Scientific value

**PASS** — The result identifies the first asymptotic order at which the infinitely many algebraic pieces accumulating at comonotonicity remain visible. Cancellation through cubic order followed by a phase-dependent quartic coefficient gives a concise regularity invariant of the newly solved attainable boundary and an exact cluster interval, a meaningful refinement of the global region theorem.

## Sources

- **The exact region determined by Spearman's rho and Gini's gamma** — Jonathan Ansari; Marcus Rockel; Stefanie Steinmaßl. https://arxiv.org/abs/2609.19890 — Primary exact-region source; gives an explicit rho-maximal boundary with countably many algebraic pieces accumulating at comonotonicity.
- **The exact Spearman rho-footrule region via optimal transport with applications to finite rankings, mixability, and Chatterjee's rank correlation** — Jonathan Ansari; Marcus Rockel. https://arxiv.org/abs/2608.20176 — Auxiliary 2026 optimal-transport boundary result used by the rho-gamma source.
- **Initial SCOPE quartic-phase commit** — SCOPE-Science repository. https://github.com/SCOPE-Science/SCOPE2026/commit/b29c045dccbcb26650404642b0010b836fae4f55 — Repository priority evidence: this record was introduced at 2026-09-19T01:07:57Z, before the later duplicate in the assignment.

## Limitations

- The theorem is local to the rho-maximal boundary near comonotonicity and does not re-prove the global attainable-region theorem.
- The phase is naturally expressed in the source parameter theta rather than solely as an elementary function of gamma.
- Equivalent unrecorded higher-order consequences of the very recent rho-footrule optimizer remain a residual originality risk.
- No statement is made about empirical sampling distributions of rho or gamma.

## Independent checks

```json
{
  "series_reversion_symbolically_checked": true,
  "cubic_coefficient_both_branches": "-(5+3*sqrt(3))/2",
  "quartic_phase_checked": "K0+16*u^3-24*u^4",
  "cluster_width_checked": 0.5,
  "branch_switch_checked": true,
  "first_public_commit": "b29c045dccbcb26650404642b0010b836fae4f55",
  "first_public_commit_time_utc": "2026-09-19T01:07:57Z",
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence; no repository mutation or separate dispatcher report was performed. Preprints and lawful open-access sources were checked first. No decisive originality comparison remained inaccessible, so Oxford Download was not required.
