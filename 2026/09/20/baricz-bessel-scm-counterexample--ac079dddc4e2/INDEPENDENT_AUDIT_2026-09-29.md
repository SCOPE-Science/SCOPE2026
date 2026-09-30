# Independent Audit — 2026/09/20/baricz-bessel-scm-counterexample--ac079dddc4e2

- Audit date: 2026-09-29 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `6d630ccc8817a4b238f83669b2804beb4b23d927`
- Disposition: **PASSED**

## Correctness

**PASS** — The counterexample is exact. From the standard recurrence one obtains F''/F=2-2r-2a/x+ar/x+a(a-1)/x^2 with a=2nu+1 and r=I_{nu+1}/I_nu. At nu=-15/16, x=2 this is 841/256-(39/16)r(2). Independently recomputing the rational tail bound gives r(2)>58189629168/42817909615=1.3590021..., which exceeds 841/624=1.3477564..., and hence F''(2)/F(2)<-23112816509/843183450880<0. Since I_nu(2)>0 for nu>-1, complete monotonicity fails. Continuity in order gives the stated open failure neighborhood.

## Originality

**PASS** — Baricz's 2010 paper explicitly presents open problems in the interval nu in (-1,-1/2], and the accessible full-text extract identifies x^{nu+1}e^{-x}I_nu(x) as the unresolved function. Salazar's July 2026 Riccati paper resolves several other Baricz/BPV questions but its stated results do not include this Section-2(b) SCM problem. Exact searches for nu=-15/16, F''(2), and the target function found no prior counterexample. The rational-tail method is not itself claimed new; the novelty is the concrete disproof of this open universal statement.

## Scientific value

**PASS** — A single rigorous rational-order witness decisively closes a long-standing yes/no problem and, by continuity, proves failure on a nontrivial open interval of orders. Although it does not classify the entire interval, it materially changes the status of the 2010 conjectural question.

## Sources

- **Bounds for modified Bessel functions of the first and second kinds** — Árpád Baricz. https://doi.org/10.1017/S0013091508001016 — 2010 source containing the open complete-monotonicity problem; accessible full-text extract checked.
- **Riccati Reductions for Modified Bessel Ratios: Bernstein Positivity, Exact Certificates, and Transfer Obstructions** — Domingos S. P. Salazar. https://arxiv.org/abs/2607.05538 — Recent exact-certificate work resolving other Bessel open problems; abstract does not include the audited SCM question.
- **Amos-type bounds for modified Bessel function ratios** — Kurt Hornik; Bettina Grün. https://doi.org/10.1016/j.jmaa.2013.05.070 — Prior ratio-bound background, not a solution of the audited complete-monotonicity problem.

## Limitations

- The result refutes the universal SCM statement but does not classify all nu in (-1,-1/2].
- The endpoints of the open neighborhood of failure are not optimized.
- Parts (a) and (c) of Baricz’s open-problem list are not addressed.

## Independent checks

```json
{
  "derivative_identity_checked": true,
  "rational_tail_certificate_recomputed": true,
  "lower_bound_r": 1.3590021019525664,
  "threshold_r": 1.3477564102564104,
  "certified_upper_Fpp_over_F": -0.027411373509380423,
  "open_access_first": true,
  "oxford_used": false
}
```

GitHub was used only as read-only evidence. The assigned source tree was unchanged between the inventory commit and source-tree-check commit. Open-access/preprint sources were checked before any institutional retrieval attempt. No inaccessible text is claimed as read.
