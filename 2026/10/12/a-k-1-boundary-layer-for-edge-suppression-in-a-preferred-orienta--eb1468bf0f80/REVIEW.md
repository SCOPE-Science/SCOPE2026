# Self-review

## Correctness
**PASS.** The claim is derived directly from the exact degree-three scattering matrix and the exact boundary matching equations in the primary source. Solving the first two rows gives an explicit common denominator whose leading term has modulus \\(2k^2|\sin\delta|\\); this proves the shrinking-window estimate whenever \\(k|\sin\delta|\to\infty\\). On \\(k\delta\to\xi\\), direct expansion of the same exact ratios gives the stated transfer law, and the edge-norm ratio follows because oscillatory cross terms are \\(O(k^-1)\\). The singular curve is explicitly excluded. The standalone checker verifies the algebra at finite test points but is not used as an infinite proof.

## Originality
**PASS.** The primary article proves only fixed-width exclusion and \\(O(k^-1)\\) edge suppression. Its 2022 author thesis restates the same theorem. The earlier preferred-orientation paper gives the vertex scattering matrix and fixed high-energy parity limit but has no strip detuning or joint near-resonant scaling. Searches for boundary-layer, shrinking-window, detuning, Floquet-resonance, and equivalent preferred-orientation formulations found no statement implying the claimed \\(k^-1\\) crossover law. The main residual risk is an equivalent local transfer calculation in weakly indexed notes or theses.

## Value
**PASS.** The primary source explicitly identifies narrow exceptional energy intervals as the limitation of its edge-suppression theorem. Quantifying those intervals is therefore intrinsic to the paper's central bulk-edge transport mechanism. The result upgrades the fixed exclusion to a shrinking one and gives the first-order local profile precisely on the unresolved scale, including its Floquet-dependent resonance curve; this is a structural refinement rather than a routine numerical increment.

## Closest literature and limitations
The closest sources are arXiv:2001.10735v1 itself, arXiv:1710.02664v1 for the underlying vertex scattering matrix, and Lipovský's 2022 habilitation thesis, which repeats the fixed-width result. The finding does not assert that every point on the local pole curve occurs in the full-strip spectrum, and it excludes the pole itself.

Self-review: passed. Independent audit: not yet performed.
