# Self-review

## Correctness — PASS
The claimed first-pivot law uses precisely the GUE entry normalization in the motivating primary paper: real diagonal standard Gaussian and off-diagonal independent circular Gaussians with unit modulus variance. The exact polar survival integral is verified. For fixed \(p<2\), the four diagonal angular minima give \(\lambda_p=2^{1-2/p}\) and second derivative \(2\lambda_p(2-p)\). For fixed \(p>2\), four coordinate-axis minima give a universal second derivative 2, including \(p=\infty\). The Gaussian quadratic-density integration supplies the correct gamma and logarithmic factors. A uniform first-order expansion of the angular rate about \(p=2\) supplies the binary-entropy crossover. The exact prior \(p=1\) and \(p=2\) cases agree. A standalone program executed 34 deterministic checks. Finite integration alone is not an asymptotic proof.

## Originality — PASS, qualified
The closest primary source is Gunawan, Peca-Medlin and Zhong, *Random permutations using GEPP* (arXiv:2610.10481v1, especially Proposition 6), which derives the \(p=1\) and \(p=2\) no-swap probabilities. Those already known cases are explicitly outside the new contribution. Searches of equivalent Gaussian-norm and pivot-first formulations, related Gaussian-elimination works, published mathematical records, and accessible prior claims found no complete fixed-\(p\) phase diagram with the critical varying-exponent limit. The older Peca-Medlin (2023) paper was accessible here by abstract but not fully inspected, and a general Gaussian extremal theorem might implicitly subsume the method: both remain originality risks. A lack of search matches is not itself a novelty proof.

## Mathematical value — PASS
The exact norm used to compare complex entries matters for actual pivot selection. The full classification exhibits a moving power-law exponent below the Hilbert norm, an isolated logarithmic law at the Hilbert norm, and a universal super-Hilbert constant; the logarithmic window resolves the transition rather than merely juxtaposing limits. This classifies a motivated probability invariant across the entire natural norm family, while not claiming results about complete permutations or numerical stability.

## Sources and limits
Primary literature: Gunawan–Peca-Medlin–Zhong (2026), arXiv:2610.10481v1; Peca-Medlin (2023/2024), arXiv:2301.13452; Huang–Tikhomirov (2022/2024), arXiv:2206.01726. The full directly relevant part of the 2026 preprint was inspected; only abstracts of the older sources were accessible in this inspection. Scientific scope: one first pivot; GUE-normalized first-column entries; real/imaginary coordinate norms; fixed \(p\) except for the explicitly controlled \(1/\log n\) window. The four originality comparisons, source-inspection details and remaining risks are given in `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
