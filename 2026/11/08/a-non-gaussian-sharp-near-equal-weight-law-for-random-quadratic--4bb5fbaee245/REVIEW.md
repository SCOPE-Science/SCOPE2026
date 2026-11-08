# Self-review

## Correctness — PASS
The moment-constrained minimax LP is exactly dual to an empirical \(L_1\) median norm. Uniform convergence to the explicitly integrated population norm, a joint Gaussian moment CLT, and the calculated dual support prove the weak limit. The folded-normal CDF and positive-band threshold are algebraic consequences. The packaged deterministic verifier checks the finite-dimensional formulas and feasible LP corrections. It does not replace the infinite-sample proof.

## Originality — PASS, with residual risk
The most directly relevant source is Neumayer–Schäfer–Ullrich, arXiv:2610.32699: finite-dimensional duality and random-node near-equal weights were already known. Bělík–Narayan–Turnage, arXiv:2609.09506, analyze a specific least-squares weighting method. Hayakawa–Lyons–Oberhauser, arXiv:2101.04250, address random convex-hull inclusion, not optimal uniform-relative weight bands. Accessible related mathematical claims concern only unconstrained quadratic moment positivity or spherical-affine chi limits. The proposed new statement is the explicit nonelliptical quadratic optimal-band law; a mathematically equivalent uncatalogued general calibration-weight specialization remains a priority risk.

## Value — PASS
Randomized quadrature requires positive exact weights without undue noise amplification or influence concentration. The full limiting law quantifies the required correction threshold at its sharp \(m^{-1/2}\) scale and supplies confidence quantiles, beyond existing qualitative positivity or sufficient finite-sample bounds. It is naturally motivated by quadratic integration and the common requirement of nearly equal sample weights.

## Scope and reproducibility
Independent uniform interval nodes, degree-two exactness and optimal maximum relative correction only. The theorem is asymptotic, does not assert rates or growing degree, and finite checks do not establish the limit. Run `python verify.py` after installing `REQUIREMENTS.txt`; the source lists and public proof appear in `RESULT.md`.

Self-review: passed. Independent audit: not yet performed.
