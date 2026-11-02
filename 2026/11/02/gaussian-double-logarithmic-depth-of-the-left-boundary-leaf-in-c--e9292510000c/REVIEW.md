# Review of the boundary-leaf height limit

## Correctness (C): PASS

The claimed object is the number of ordered interval splits traversed by leaf 1, not a randomly relabeled or uniformly chosen leaf. The exact recursion has transition \(q(m,i)\), and the independent harmonic variable/fair-bit construction recovers that transition exactly. The proof supplies the critical ingredient absent from standard random-leaf analyses: the first four moments of the decrement \(\ell_m-\ell_{I_m}\) tend to \(r!/2\), with a uniform quantitative bound. Its mean tends to \(1/2\), its variance to \(3/4\), and its fourth moment remains bounded. Stopping the descending chain at potential \((\log H_{n-1})^{1/3}\) gives a martingale central limit theorem with asymptotic duration \(2\log H_{n-1}\), hence fluctuation variance \(6\log H_{n-1}\). The remainder is negligible on the square-root scale. The standalone finite checker passed 383 assertions; finite tests do not prove the CLT. Remaining mathematical risk is the usual possibility of a gap in the written asymptotic martingale argument, pending independent review.

## Originality (O): PASS, with qualification

Aldous and Janson (arXiv:2303.02529, §3.9, Open Problem 2) explicitly pose the distributional question for the original ordered labels and anticipate only the \(2\log\log n\) scale for label 1. That scale is prior art and is not claimed as novel. Their discussions of harmonic descent and the results of Aldous–Pittel (arXiv:2302.05066) and Aldous–Janson (arXiv:2412.12319) concern uniformly chosen leaves; the latter explicitly says its results do not use original ordered labels. A uniform-leaf height has a different order and kernel and cannot imply the boundary-leaf Gaussian theorem. The 2025 Iksanov–Nikitin–Yakymiv and 2026 Chorbadzhiyska–Minchev–Savov works address tagged/uniformly sampled leaves and related fragmentations, while Ma's 2026 paper treats the maximum over leaves. Title/abstract inspection of those later articles is weaker evidence than a comprehensive full-text priority audit, and relevant unexamined results remain a residual risk. Searches of the mathematical-record database and the accessible previous-record claim summaries did not identify a dominating theorem, but that absence is not itself a novelty proof.

## Value (V): PASS

This answers a natural subcase of an explicitly stated open distributional problem for nonexchangeable ordered labels. Deterministic boundary labels have a markedly smaller height scale than uniformly chosen leaves. The newly quantified \(\sqrt{6\log\log n}\) fluctuations and Gaussian limit explain that difference at the second order. This is a structural asymptotic theorem rather than a routine finite calculation or a claim of solving the whole open problem.

## Scope, sources and limitations

Primary motivating text: https://arxiv.org/html/2303.02529v3, §3.9. Primary uniform-leaf comparator: https://arxiv.org/html/2412.12319v1, §1.2. Other relevant sources: https://arxiv.org/abs/2302.05066, https://arxiv.org/abs/2510.17343, https://arxiv.org/abs/2608.18320, https://arxiv.org/abs/2609.14329. The theorem is for a single fixed boundary label in the discrete ordered critical model; it has no quantitative convergence rate and is not an independent mathematical validation.

Self-review: passed. Independent audit: not yet performed.
