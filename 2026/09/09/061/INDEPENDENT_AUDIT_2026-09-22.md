# Independent audit — 2026/09/09/061

## Correctness — PASS for the fixed golden state and the specified stabilizer convention

For a normalized 36×36 flattening, AM–GM on its 36 singular values gives |det M|≤(1/6)^36, so the product normalization 6^108 is ≤1 and equals 1 for an AME(4,6) 2-unitary. Rather et al. provide that golden state. Cha's open Theorem 1 factors any dimension-6 stabilizer state locally into qubit and qutrit stabilizers. Since no four-qubit AME exists, at least one qubit two-party reduction has rank at most 2 (stabilizer ranks are powers of 2); its quhex cut rank is at most 2·9=18, so one determinant vanishes. The same cut's reduced fidelity to I/36 is at most √(18/36)=1/√2. Thus the stated weak pure-state trace-distance lower bound follows. In fact monotonicity yields |<G|S>|²≤1/2 and pure-state T(G,S)≥1/√2. By linearity, every mixture σ of such stabilizer projectors has <G|σ|G>≤1/2, hence T(|G><G|,σ)≥1/2 using the projector as a binary test. This independently supplies an actual polytope bound stronger than the title's stated constant. For the cited mixed state of purity 1/2, ∥ρ∥∞≤1/√2 gives T≥1−2^(−1/4)≈0.1591.

The degree argument also checks: on global phase e^(iθ)G a homogeneous degree-m invariant changes by e^(imθ), forcing Euclidean Lipschitz L≥m|I(G)|. Vanishing on each singular-flattening hypersurface requires each irreducible determinant factor, so degree at least 108. A product of two Bell pairs has one singular cut and full-rank transverse cuts, showing the hypersurfaces differ. The term “orbit” must not be read as a uniform distance bound over the full noncompact SLOCC orbit: local invertible filters can approach lower-rank states. The bound is for G (and its local-unitary orbit).

## Originality — PASS, qualified

Rather et al. establish the 2-unitary golden state; Cha and Wójcik et al. establish qualitative stabilizer nonexistence. Combining the CRT factorization with rank quantization and reduced-state fidelity gives a quantitative distance for this state that I did not find stated in those open sources. The determinant construction is standard invariant algebra applied to this case, and no amplitude-level evaluation was independently available.

## Scientific value — PASS

A rigorous numerical robustness radius against stabilizer mixtures can guide approximate preparation benchmarks. It is a fixed-state separation, not a separation of an entire SLOCC orbit, and the degree-108 invariant is too high for the proposed low-Lipschitz route.

## Sources

- Original RESULT.md and METADATA.json; independent determinant, rank, fidelity and phase calculations above.
- Rather et al., https://arxiv.org/abs/2104.05122 .
- Cha, Theorem 1, https://arxiv.org/pdf/2603.13442 .
- Wójcik et al., https://arxiv.org/abs/2603.18193 .
