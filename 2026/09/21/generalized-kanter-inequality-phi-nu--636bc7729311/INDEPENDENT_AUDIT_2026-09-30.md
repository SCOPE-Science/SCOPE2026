# Independent Audit — 2026/09/21/generalized-kanter-inequality-phi-nu--636bc7729311

- Audit date: 2026-09-30 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `d2d873ac7f23b48ecd77c29f23c30413c9c7c57a`
- Disposition: **PASSED**

## Correctness

**PASS** — The Baricz-Pogány integral representation reduces the inequality to positivity of D_a(r)=∫(1-x^2)^(a-1)b_r(x)dx. For r>0 the normalized kernel H_r has derivative sign x tanh(2rx)-2r(1-x^2), a strictly increasing expression, so b_r has one interior sign change from positive to negative. The boundary-weight integral simplifies to F(r)=psi(r+1/2)-log r+Ei(-4r). Its derivative is the Laplace transform of a kernel negative on (0,4) and positive on (4,infinity), which permits at most one positive-to-negative sign change; with F(0+)=0, F'(0+)=pi^2/2-4>0, and F(infinity)=0, this forces F(r)>0. Reweighting a one-sign-change function by the decreasing factor (1-x^2)^a preserves positivity, proving strictness for r>0, nu>-1/2. The half-order and r=0 equality cases and large-r sharpness are correct. Independent high-precision sampling over nu in {-0.49,-0.25,0,0.5,1,2,5} and r from 0.001 to 50 found strictly positive gaps; the smallest sampled gap was about 8.99e-13 at nu=5,r=50, consistent with asymptotic sharpness.

## Originality

**PASS** — Baricz-Pogány explicitly end their paper with an open problem asking for a generalization of Kanter's inequality for Phi_nu. A 2026 open-access paper revisits these Bessel sums and rewrites existing Kanter-type expressions in confluent-hypergeometric form, but the checked text does not state the audited gamma-ratio lower bound. Searches by the exact Phi_nu family, gamma ratio, Bessel form and Kummer form found no equivalent prior theorem. The claim therefore directly answers the recorded open problem, with a residual risk from differently notated special-function inequalities.

## Scientific value

**PASS** — The theorem supplies a natural two-parameter extension that exactly recovers Kanter at nu=0, is sharp on both natural boundaries, and is asymptotically sharp. It resolves an explicit open problem and packages a reusable one-sign-change reweighting argument.

## Sources

- **On a sum of modified Bessel functions** — Á. Baricz; T. K. Pogány. https://arxiv.org/abs/1301.5429 — Primary source introducing Phi_nu and explicitly posing an open problem about a generalized Kanter inequality.
- **On Finite and Infinite Sums of the Modified Bessel Function of the First Kind** — D. Veestraeten. https://doi.org/10.1007/s00009-026-03050-1 — Current-status comparison; rewrites existing Kanter-related formulas via confluent hypergeometric functions rather than giving the audited gamma-ratio lower bound.
- **A shorter proof of Kanter's Bessel function concentration bound** — L. Mattner; B. Roos. https://arxiv.org/abs/math/0603522 — Classical Kanter-bound background for the nu=0 specialization.

## Limitations

- The result concerns the particular Phi_nu family rather than all lower bounds for Bessel sums.
- Equivalent prior coverage under substantially different beta-integral or Kummer-function notation remains possible.
- The numerical checks supplement rather than replace the analytic proof.

## Independent checks

```json
{
  "integral_reduction_reconstructed": true,
  "single_sign_change_argument_checked": true,
  "boundary_integral_sign_argument_checked": true,
  "decreasing_weight_transfer_checked": true,
  "sampled_minimum_gap": 8.985598284498155e-13,
  "sampled_minimum_gap_at": {
    "nu": 5,
    "r": 50
  },
  "source_open_problem_checked": true,
  "source_tree_unchanged": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned record tree was unchanged from the inventory snapshot through the checked commit. GitHub was used only as read-only evidence. Open-access and preprint sources were checked first, and no decisive comparison required institutional retrieval. No GitHub write or separate dispatcher report was performed.
