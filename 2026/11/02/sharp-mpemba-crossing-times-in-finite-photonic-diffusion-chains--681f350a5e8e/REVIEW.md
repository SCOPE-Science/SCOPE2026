# Scientific review — sharp photonic-path Mpemba crossings

## Correctness — PASS

The claim fixes the reflecting nearest-neighbor generator, the two initial measures, the equilibrium normalization, and an odd integer site count at least five. Exact discrete cosine eigenvectors give the two squared-distance sums. Multiplying their difference by the lowest-mode exponential and pairing each even mode with the following odd mode yields strictly positive, strictly decreasing pairs because the eigenvalue-gap ratio is at most \(8/3\), while the negative weight is at most \(1/16\). The scaled difference has opposite endpoint signs, establishing exactly one crossing for every stated finite size. Near the explicit reference time, the first even and first odd modes determine the crossing, while the sum of other modes is smaller than the derivative times \(o(1)\); this proves the additive constant and the \(N^2\log N\) scaling. A uniformly controlled midpoint Fourier/Taylor calculation identifies the mixed cubic term in relative entropy and proves one nearby relative-entropy crossing with the stated negative \(N^{-1/3}\) displacement. The proof does not claim global uniqueness for that second metric. A separate standard-library diagnostic program verifies finite eigenvalue, coefficient, positivity, pairing, and crossing checks; it is not used as infinite proof.

## Originality — PASS, with qualified priority

Longhi's 2024 full arXiv main text specifies the photonic system, its incoherent path generator, the two initial distributions, and qualitative delayed crossings. Its discussion is not an all-odd-size unique-crossing theorem, a sharp \(N^2\log N\) limit, an \(O(1)\) offset, or a relative-entropy/Hilbert--Schmidt displacement formula. Lu and Raz's general Markovian Mpemba spectral mechanism explains how a fast-relaxing initial condition can overtake another, but gives none of these path-specific evaluations. Actual searches for spectral variants, path diffusion, crossover time, entropy metric, and the same 2024 paper found related published results on quantum-path mixing and finite-dimensional dephasing, with different observables and no implication of the claimed crossing law. The original paper's separately hosted supplement did not yield readable content and remains a genuine priority uncertainty; its unavailability is not asserted as proof that it lacks the result.

## Mathematical value — PASS

The original paper's rapidly increasing crossing time poses a concrete scalability question for its photonic experiment. The theorem quantifies a super-diffusive \(N^2\log N\) delay relative to the natural \(N^2\) diffusion time, establishes uniqueness for a normalized squared-distance observable rather than merely finding a crossing numerically, and proves a subtle metric-specific \(N^{-1/3}\) advance of the relative-entropy crossing. The sign-pairing argument is structural across arbitrarily long odd chains; the cubic entropy term is an independent quantitative refinement. The specified pair of preparation protocols and dissipation observable motivate each exact invariant; this is not a generic finite table or a trivial reparameterization.

## Closest primary literature and limits

- S. Longhi, *Photonic Mpemba effect*, arXiv:2408.03296v1 (August 6, 2024), https://arxiv.org/html/2408.03296v1; *Optics Letters* 49, 5188–5191 (2024), doi:10.1364/OL.532503.
- Z. Lu and O. Raz, *Nonequilibrium thermodynamics of the Markovian Mpemba effect and its inverse*, PNAS 114, 5083–5088 (2017), doi:10.1073/pnas.1701264114.

A quantitative assertion for finite dephasing, an even chain, altered preparation states, or a joint size/dephasing limit has not been proved here. Neither has absence of additional relative-entropy crossings at earlier times. Priority remains qualified by the uninspected supplemental file and potentially broader path-semigroup literature.

Self-review: passed. Independent audit: not yet performed.
