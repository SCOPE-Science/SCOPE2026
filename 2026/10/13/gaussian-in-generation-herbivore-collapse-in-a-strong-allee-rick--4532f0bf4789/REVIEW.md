# Scientific review: Gaussian-in-generation herbivore collapse

## Correctness

**PASS.** For every positive orbit tending to extinction, continuity and \(f(0)=q<1\) force eventual geometric bounds on both populations. Local differentiability makes \(\sum(j+1)|\delta_j|\) finite, and the partition identity \(y_{n+1}=x_{n+1}(e^{a y_n}-1)\) makes the second logarithmic correction summable. Consequently the two strictly positive asymptotic constants in RESULT.md exist and the exact quadratic herbivore logarithmic profile follows. On the explicit strong-Allee basin \(0<x_0<b\), the necessary extinction is proved directly. The integer hitting-time corollaries follow from the positive asymptotic ratios and eventual monotonicity. The standalone verifier was run with three positive parameter sets and returned `VERIFY_OK`; finite arithmetic is corroboration, not the infinite-time proof.

## Originality

**PASS, with stated limitations.** The model of Bešo, Kalabušić and Pilav [1], inspected through the full publicly accessible article text, proves qualitative extinction and local stability in Section 3.1 but does not derive a full two-population profile, convergent positive prefactors, or the different detection-clock scales. The 2014 Chow–Jang article [2] was examined through the complete 23-page primary text, including its extinction propositions and conclusions: it studies an allied map in which the parasitoid biomass update differs, and does not provide the present quantitative joint law. A 2008 non-Allee model [3] has the incompatible low-density factor \(f(0)>1\). Published similarity searches found no result logically implying the claimed constants; model names alone were not used to infer novelty. The separate literature comparisons and residual risks are in AUDIT.json.

## Value

**PASS.** Extinction basins alone do not determine how soon the two species fall below a measurement cutoff. Here the strong-Allee collapse has unequal and *sharply quantified* clocks: the plant's geometric relaxation requires logarithmic time, while the herbivore, whose replenishment depends on vanishing plant biomass, has a Gaussian-in-generation profile with a square-root logarithmic clock. The coefficient \(rb/2\) and complete orbit-dependent normalization follow across the entire positive extinction basin, not from a chosen finite parameter slice. The general growth-factor formulation identifies the transferable structural mechanism and distinguishes the scientific phenomenon from a routine numeric threshold calculation.

## Closest literature and limits

[1] E. Bešo, S. Kalabušić, E. Pilav, *Dynamics of a plant-herbivore system with Ricker plant growth and the strong Allee effects on plant population* (2023 early access), DOI 10.3934/dcdsb.2023108, normalized equation (5) and §3.1. [2] Y. Chow and S. R.-J. Jang, *Allee effects in a Ricker-type predator–prey system* (2014), DOI 10.1080/10236198.2014.918966, §§2–4. [3] Y. Kang, D. Armbruster and Y. Kuang, *Dynamics of a plant-herbivore model* (2008), DOI 10.1080/17513750801956313. These comparisons support a circumscribed originality conclusion, not an assertion of exhaustive global priority. Relevant unindexed general asymptotic theorems remain a residual risk. The finding excludes boundary-axis initial conditions, does not classify all extinction basins, and makes no stochastic ecological prediction.

Self-review: passed. Independent audit: not yet performed.
