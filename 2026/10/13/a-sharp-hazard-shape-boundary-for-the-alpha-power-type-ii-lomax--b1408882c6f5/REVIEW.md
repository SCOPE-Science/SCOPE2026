# Scientific review: exact APIILx hazard-shape phase boundary

## Correctness — PASS

The probability law and hazard are reconstructed from the source CDF (equations (2.4)–(2.7)). The change of variable \(t=-\log(1-v/2)\) gives the exact, numerically stable hazard and logarithmic derivative in RESULT.md. The sign lemma is proved for all positive parameters: the function \(a/(1-e^{-at})\) is strictly increasing in \(a\), and \(\sinh(z)/z\) is strictly increasing in positive \(z\). These establish strict monotonicity of the transformed derivative sign, its exact endpoint \(B(\alpha)\), and the unique peak or global decrease across every boundary case. Scale invariance and the absence of globally increasing or multiphasic hazards follow. The reproducibility script checks 360 distinct parameter/time combinations and exact radical peak conditions. The proof, not finite testing, establishes the universal quantifiers. No external mathematical lemma beyond the elementary inequalities is assumed.

## Originality — PASS, subject to recorded priority risk

The complete, accessible 2026 primary PDF describes both decreasing and unimodal hazard *shapes* and displays examples, but does not give the sharp if-and-only-if boundary \(\theta B(\alpha)=1\), monotone root characterization or proof that those are the only possible shapes for every positive parameter. The accessible 2025 alpha-power type-II-G generator article derives its general transformation and works through exponential and Weibull baselines, not the Lomax-baseline phase boundary. The accessible 2023 alpha-power power-Lomax article uses a distinct exponential-in-CDF generator and a four-parameter model. A prior indexed APIILx tail-exponent analysis addresses asymptotic moments and tail behavior and does not determine the global derivative-sign classification. Exact-paper, alias, derivative, alternate-generator and broader-family literature searches did not reveal covering statements. Lack of a retrieved result is not a proof of priority; potentially unindexed equivalent analyses remain a risk.

## Value — PASS

The hazard-shape division is an inherent and practically interpretable feature of a proposed lifetime model. A complete parameter criterion is useful before fitting a decreasing-failure-rate or unimodal-failure-rate phenomenon: it determines precisely whether an initial rise is possible, shows it can have only one peak, provides the unique peak location, and demonstrates that no positive parameter choice can yield globally increasing failure rate. It upgrades published plots and qualitative observations to a nontrivial exhaustive classification, not a minor numerical improvement or a parameter renaming. The result is restricted to the stated model and does not make claims about estimation consistency or empirical fits.

## Closest literature and limitations

1. Kalt et al. (2026), DOI `10.3934/math.2026334`, full publisher PDF, sections 1–3 and 6–7, equations (2.4)–(2.7), Figure 1. Provides the source hazard and qualitative shapes, not the sharp criterion.
2. Mohsin and Kalt (2025), DOI `10.18280/mmep.120330`, full open HTML text, sections 2–4. Provides the general generator, with exponential/Weibull examples, but not the studied Lomax hazard partition.
3. Qura et al. (2023), DOI `10.1155/2023/6661792`, accessible full-page HTML narrative and sections 1–2, 7. An analogous name refers to a different family and does not imply this theorem; math images in that HTML view were not independently extracted.
4. The classical Lomax model is the \(\alpha=1\) special case and has decreasing hazard; no claim to originality is made for that fact.

Scientific limits: exact full-support model only; a short observed range may appear increasing even when the hazard ultimately falls. Residual priority risk from unindexed or otherwise overlooked equivalent statements remains. Independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
