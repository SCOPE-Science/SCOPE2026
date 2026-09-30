# Independent Audit — 2026/09/20/band-dominated-complemented-essential-witness--13f1862c93ef

- Audit date: 2026-09-29 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `fada255f84547a71eecddc8ce8b2f6ad0c51b139`
- Disposition: **PASSED**

## Correctness

**PASS** — The block-witness proof is sound. For finite F, BP_F has finite rank because each fiber is finite-dimensional, hence ||BQ_F||>=dist(B,K). A finite-propagation operator therefore has arbitrarily far-out finitely supported unit vectors with image norm near its essential norm; 2R separation makes their images disjoint, yielding an exact lower bound on the generated l_p/c_0 copy. The norm-one projection onto that disjoint block sequence is valid in both l_p and c_0. Norm approximation transfers the witness to band-dominated A. The same copy forces distance to strictly singular and finitely strictly singular ideals to equal the compact essential norm. Finally b_n>=rho follows from n-dimensional subspaces of the witness, while a_n->rho because finite-coordinate projections in the codomain approximate compact maps uniformly, so compact and approximable operators coincide for these target sums.

## Originality

**PASS** — The inspected band-dominated literature centers on Fredholmness, limit operators, essential norms and internal ideals. Rabinovich-Roch-Silbermann (2001/2004) and Roch (2022) do not advertise a strict-singularity/Bernstein-number identification; targeted searches for 'band-dominated' with strictly singular, finitely strictly singular, Bernstein numbers, and complemented copies produced no covering theorem. The result uses elementary block localization rather than the richer limit-operator hypotheses common in the literature. Residual risk remains because the 2004 monograph was not searched theorem-by-theorem, so the priority claim is appropriately narrow.

## Scientific value

**PASS** — The theorem gives an unusually concrete geometric realization of the essential norm by a 1-complemented classical sequence copy and converts that witness into exact distances to two larger operator ideals plus the asymptotic Bernstein profile. The finite-fiber/locally-finite hypotheses make the scope clear, and the result applies beyond homogeneous group settings.

## Sources

- **Band-dominated operators with operator-valued coefficients, their Fredholm properties and finite sections** — V. S. Rabinovich; S. Roch; B. Silbermann. https://doi.org/10.1007/BF01299850 — Foundational operator-valued band-dominated/Fredholm theory.
- **Limit Operators and Their Applications in Operator Theory** — Vladimir Rabinovich; Steffen Roch; Bernd Silbermann. https://doi.org/10.1007/978-3-0348-7911-8 — 2004 monograph devoted to band-dominated operators and limit-operator Fredholm theory.
- **Ideals of band-dominated operators** — Steffen Roch. https://doi.org/10.1080/17476933.2021.1913134 — 2022 paper on an increasing family of closed ideals in the band-dominated algebra on l2(Z^N); abstract/full page does not state the audited strict-singularity/Bernstein theorem.

## Limitations

- Finite-dimensional coordinate fibers and local finiteness are essential to the escaping finite-block argument.
- The domain and codomain use matching outer l_p exponents or both c_0; l_infinity and cross-exponent maps are not covered.
- The 2004 monograph was not exhaustively inspected theorem-by-theorem, leaving residual historical-priority risk.

## Independent checks

```json
{
  "proof_reconstructed": true,
  "projection_norm_one_checked": true,
  "operator_ideal_distance_argument_checked": true,
  "approximation_number_limit_checked_via_target_approximation_property": true,
  "open_access_first": true,
  "oxford_used": false
}
```

GitHub was used only as read-only evidence. The assigned source tree was unchanged between the inventory commit and source-tree-check commit. Open-access/preprint sources were checked before any institutional retrieval attempt. No inaccessible text is claimed as read.
