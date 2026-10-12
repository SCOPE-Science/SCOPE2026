# Scientific review: Gaussian–Konno critical window

## Correctness — PASS

For the stated homogeneous infinite-line channel, global spatial translations commute with the coherent walk. Counting coherent letters gives exactly a binomial coherent-step count and an independent symmetric classical displacement. The coherent Fourier eigenphases give the known Konno velocity density; the three regimes follow from binomial concentration, the classical central limit theorem and a characteristic-function argument. The calculated fourth cumulant is \(-\lambda^4(1-\sin\theta)^2(4-\sin\theta)/2\), strictly negative for positive \(\lambda\) and interior \(\theta\). The included verifier returned `VERIFY_OK 297`, covering matrix-channel/convolution identities, normalization, symmetry and finite moment tests. These finite computations corroborate but do not establish the infinite-time limits.

## Originality — PASS, with priority qualification

The primary 2025/2026 paper of Štefaňák and collaborators defines the same Kraus channel and analyzes monitored first-return probabilities, not this unmonitored critical-window position law. Konno's coherent weak limit is prior work. Ahlbrecht and collaborators' commuting-Kraus weighted-velocity theorem already encompasses the fixed-parameter ballistic conclusion in appropriate hypotheses; **that component alone is not new**. Chisaki and collaborators study position measurements/restarts, Konno–Matsue–Segawa study a stripe-controlled walk, and Ellinas–Bracken–Smyrnakis obtain an analogous noise-squared-times-time crossover for a distinct coin-randomization channel. Full-text comparisons did not identify the particular inverse-square-root singular limit or the Gaussian–Konno convolution. The derivation uses elementary commutation and known limit ingredients, so an earlier implicit statement remains a material originality risk; searching cannot certify priority.

## Value — PASS

The exact scaling window determines when a nearly classical quantum walk retains detectable non-Gaussian coherent spreading. Its parameter-dependent convolution density, negative fourth cumulant and sharp separation of three regimes give a motivated transport benchmark, and its finite-time binomial formula avoids mixed-density-matrix simulation for final-position statistics. This is more precise than qualitative interpolation between ballistic and diffusive limits, while making no claim about quantum advantage or measured recurrence.

## Scope and limitations

Assumptions: \(0<\theta<\pi/2\); localized initial \((|R\rangle+i|L\rangle)/\sqrt2\) coin; coin-independent symmetric shifts; an infinite homogeneous line; channel parameter constant within each length-\(t\) run; no intermediate observation. Proven: weak asymptotic laws and exact finite-time distribution identity; fourth cumulant of the limiting law. Not proved: uniform local-limit errors, other noise mechanisms, finite boundaries, or uniqueness of scientific priority. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
