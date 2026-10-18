# Scientific review: coherent preparation length and absorbing boundary

## Correctness — PASS
The exact boundary resolvent gives the full normalized-packet absorption effect, not merely one-site survival. The exterior-energy contribution is nonnegative and at most \(K/[2\pi n(n-1)]\) for all positive loss rates. The in-band multiplier is pointwise maximized at matched loss, and its Hermitian Toeplitz compression gives a genuine global optimizer in the far-field model. The two-sided multiplier-to-Dirichlet comparison proves the coefficient \(\pi^2/4\) without extrapolating from the numerical spectrum. The standalone checker passed 279 comparisons, including independently propagated finite-chain states. The finite simulation does not certify the infinite theorem; its proof is analytic.

## Originality — PASS, qualified
Riberi (arXiv:2605.08056) solves the exact forward propagator and localized-source absorption; that work is acknowledged, and the self-review was based on PDF formula sections, not a snippet alone. The present contribution is a sharp optimization over the *coherent preparation-window dimension*, including an exact \(K=2\) chiral limit, all-\(K\) finite bounds and a distance-uniform correction. Amorim and collaborators (arXiv:2512.02186) concern a coined discrete-time walk, not the present continuous-time boundary jump. The classical Hadamard-walk appearance of \(2/\pi\) is acknowledged as a different model. Generic Parter/Widom/Toeplitz extreme-eigenvalue theory may imply the eigenvalue asymptotics once the new physical operator is identified, and the original Green function implies the unoptimized linear response; these are the largest remaining novelty risks. Older full monograph text and the original Parter article were not fully inspected.

## Value — PASS
The result solves a nontrivial, physically natural finite-coherence resource problem rather than tabulating a small graph. It quantifies the coherence-window cost of nearly perfect absorption and demonstrates a substantial phase-controlled two-site effect, with an explicit far-field approximation valid uniformly over state coefficients and sink strength.

## Limitations and independent status
Exact ensemble eventual absorption only, no finite-time, dephasing or experimental noise guarantee. A full independent bibliographic and mathematical assessment remains outstanding.

Self-review: passed. Independent audit: not yet performed.
