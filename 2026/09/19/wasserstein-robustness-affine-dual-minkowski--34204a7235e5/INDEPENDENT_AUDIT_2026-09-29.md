# Independent Audit — 2026/09/19/wasserstein-robustness-affine-dual-minkowski--34204a7235e5

- Audit date: 2026-09-29 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `c983e301182513597565544a4d8c6e88830761f4`
- Disposition: **PASSED**

## Correctness

**PASS** — For a fixed closed set C in a compact metric space, every coupling to a measure supported on C costs at least int d(x,C)^p dmu, while a measurable nearest-point selector attains that cost. Applying this to each closed hemisphere and minimizing over its compact normal parameter gives exactly Delta_p=dist_Wp(mu,B), including the arcsin((-u.v)_+) formula and an explicit nearest bad datum. Zhang-Jin Theorem 1.5 was checked in the open PDF and states precisely that for n>=3 and 2<=m<=n-1 solvability is equivalent to not being concentrated on a closed hemisphere. B is closed, its complement is open, dense and convex, and Delta_p^p is the infimum of linear functionals; the submitted strong concavity inequality then follows from the power-mean inequality. The 1-Lipschitz statement is the general distance-to-a-set bound. The one-sided Lp moment-body comparison follows from x<=arcsin x<=(pi/2)x. At W_infinity, the fixed-set formula is an essential-supremum distance; for solvable compact support, minimizing the support function of its convex hull gives its origin-centered inradius, yielding arcsin r_0 exactly.

## Originality

**PASS** — Zhang-Jin's September 2026 paper supplies the qualitative general-measure hemisphere criterion, not the Wasserstein distance-to-degeneracy formula, sharp perturbation radius, concavity margin, moment-body comparison, or W_infinity support-hull formula. Cai-Leng-Wu-Xi's 2025 work introduced affine dual curvature measures and solved an even-data problem under a strict subspace concentration condition; Zhang-Jin explicitly distinguish that earlier theorem from their new general-measure criterion. The 2025 publisher full text could not be read because institutional retrieval stopped at human verification, so no claim is made to have inspected it. Its published theorem scope is not decisive for the new arbitrary-measure robustness result, but the possible overlap is retained as a limitation. The optimal-transport projection lemma itself is elementary and is not claimed new.

## Scientific value

**PASS** — The theorem turns a qualitative existence condition into an exact adversarial robustness radius with an attaining perturbation, a convex mixing law, and Euclidean surrogate certificates. This gives a practical quantitative geometry for how close admissible data are to loss of solvability while correctly avoiding claims about uniqueness or conditioning of the realizing convex body.

## Sources

- **Affine dual Minkowski problem for general measures** — Cheng Zhang; Hailin Jin. https://arxiv.org/abs/2609.20003 — Open PDF checked. Theorem 1.5 states the exact not-concentrated-on-a-closed-hemisphere criterion for n>=3, 2<=m<=n-1.
- **Affine dual Minkowski problems** — Xiaxing Cai; Gangsong Leng; Yuchi Wu; Dongmeng Xi. https://doi.org/10.1016/j.aim.2025.110184 — 2025 predecessor introducing the measure and solving the even problem. Open-access attempts failed and Oxford retrieval reached human verification; its full text was not claimed read.
- **Optimal Transport: Old and New** — Cédric Villani. https://doi.org/10.1007/978-3-540-71050-9 — Standard Wasserstein-space background; the fixed-closed-set projection identity used here is elementary.

## Limitations

- The result quantifies robustness of existence of a datum, not uniqueness, regularity, or conditioning of the realizing body.
- It works on a fixed-mass probability slice; positive mass rescaling is handled separately by homogeneity.
- The Cai-Leng-Wu-Xi 2025 publisher full text remained inaccessible after lawful attempts because human verification was required; its stated even-data scope makes it nondecisive but leaves residual overlap risk.
- The result is restricted to the Zhang-Jin range n>=3 and 2<=m<=n-1.

## Independent checks

```json
{
  "zhang_jin_open_pdf_checked": true,
  "zhang_jin_theorem_1_5_screenshot_checked": true,
  "fixed_closed_set_transport_proof_reconstructed": true,
  "concavity_and_w_infinity_derivations_checked": true,
  "open_access_first": true,
  "oxford_attempted": true,
  "oxford_source": "https://doi.org/10.1016/j.aim.2025.110184",
  "oxford_job_id": "b5120c689db6dd5c25ec5ff943f4debc",
  "oxford_status": "needs_human",
  "inaccessible_material_not_claimed_read": true
}
```

The assigned source tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Open-access/preprint sources were checked before institutional retrieval. Any inaccessible comparison is explicitly identified above rather than claimed read.
