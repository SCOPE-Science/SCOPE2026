# Independent Audit — 2026/09/18/almost-bcd-banach-mazur-euclidean-stability--8119d118c382

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `32b1e47ec547eebf7cc2d0c7aaf2beab48ce649c`
- Disposition: **PASSED**

## Correctness

**PASS** — The quantitative conversion is valid. Han-Liu Theorem B(iii) gives p_par(T_x^*X)≤8√δ almost everywhere under the local doubling and weak (1,1)-Poincaré hypotheses, and their Corollary 4.8 gives the same bound for dual Minkowski norms. For the parallelogram ratio R, the normalizing maximum in p_par is at most 2||u||^2+2||v||^2, so |R-1|≤p_par; the standard change of variables exchanges R with 1/R. Thus the von Neumann-Jordan constant is at most 1+8√δ. Passer's quantitative Jordan-von Neumann theorem then gives d_BM≤1+(18m^2-17m+14)·8√δ+O_m(δ), and its two-dimensional explicit formula yields the record's displayed nonasymptotic expression after ε=8√δ. Banach-Mazur distance is invariant under finite-dimensional duality, so the cotangent statement transfers to the original Minkowski norm. For sharpness, Han-Liu prove Δ_BCD(F_τ)≈τ^2 for nonquadratic smooth perturbations and a linear parallelogram defect; the inequalities C_NJ≤d_BM^2 and C_NJ-1≥p_par/2 then force d_BM-1≳|τ|, while the identity map gives the matching O(|τ|) upper bound.

## Originality

**PASS** — Han-Liu provide the entropy-error-to-parallelogram estimate and sharp Finsler perturbation scale, while Passer provides the independent finite-dimensional parallelogram-to-Banach-Mazur stability theorem. The located Han-Liu text does not state a Banach-Mazur consequence, and targeted searches found no prior combination yielding this almost-everywhere Euclidean cotangent-ball estimate with the sharp square-root error exponent. The record is therefore a legitimate new quantitative corollary rather than a rebranding of either source theorem.

## Scientific value

**PASS** — Banach-Mazur distance is an affine-invariant geometric conclusion substantially stronger and more directly interpretable than a raw parallelogram-defect bound. The result converts the new almost-BCD condition into quantitative Euclidean stability of cotangent fibers and proves the √δ exponent cannot be improved in fixed dimension. This gives a useful bridge between synthetic curvature-dimension theory and finite-dimensional Banach-space geometry.

## Sources

- On the Geometry of Wasserstein Barycenter II: Riemannian Rigidity, Essential Non-Branching, and Finsler Models (Bang-Xian Han; Deng-Yu Liu): https://arxiv.org/abs/2609.19564 — Theorem B(iii) gives the a.e. p_par≤8√δ estimate; Corollary 4.8 and Theorem C/4.11 give the normed-space and quadratic-perturbation bounds.
- An Approximate Version of the Jordan von Neumann Theorem for Finite Dimensional Real Normed Spaces (Benjamin Passer): https://arxiv.org/abs/1305.3546 — Quantitative conversion from small von Neumann-Jordan constant to Banach-Mazur closeness, including the dimension-dependent asymptotic and the explicit two-dimensional estimate.

## Limitations

- The general coefficient inherits nonoptimal constants from Han-Liu and Passer and is not claimed dimension-sharp.
- Except in dimension two the upper estimate is asymptotic as δ→0.
- Fiberwise Banach-Mazur closeness does not by itself give global bi-Lipschitz or Gromov-Hausdorff stability of the ambient metric-measure space.

## Independent checks

```json
{
  "method": "source-theorem verification plus algebraic conversion",
  "han_liu_theorem_B_iii_checked_in_full_arxiv_pdf": true,
  "han_liu_corollary_4_8_checked_in_full_arxiv_pdf": true,
  "han_liu_quadratic_perturbation_checked_in_full_arxiv_pdf": true,
  "passer_dimension_coefficient": "18m^2-17m+14",
  "duality_and_sharpness_chain_checked": true,
  "all_ok": true
}
```

The assigned source tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was read only as evidence and no repository mutation was performed. Open-access/preprint sources were checked first; Oxford Download was not needed in this record.
