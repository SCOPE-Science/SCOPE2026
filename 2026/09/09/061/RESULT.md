# Certified SLOCC invariant gap (1 vs 0) and unconditional trace-distance separation of the golden AME(4,6) orbit from the 4-quhex stabilizer polytope

## Context
General AME(4,6) existence was resolved by Rather et al. (arXiv:2104.05122) via the golden 2-unitary state G and a ((3,6,2))_6 code. March–April 2026 work (Wojcik et al. arXiv:2603.18193; Cha arXiv:2603.13442) closed the qualitative stabilizer/graph existence question: no stabilizer or graph AME(4,6) exists. The live question is quantitative: how far is G from the stabilizer polytope in an auditable invariant-plus-distance sense, governing Casas-type circuit fidelities, code thresholds, secret sharing, and perfect-tensor stability.

## Definitions
- Hilbert space H = (C^6)^{⊗4}, dim 1296. Pure-state trace distance T(psi,phi) = sqrt(1-|<psi|phi>|^2). Scott measures Q_m (Scott quant-ph/0310137): Q_m = [d^m/(d^m-1)]·[1 − avg_{|S|=m} Tr rho_S^2], d = 6.
- For a 4-tensor T and a 2-vs-2 cut c, M_c(T) is the 36×36 flattening, D_c(T) = det M_c(T), homogeneous degree 36.
- J(T) = 6^108 · D_{12|34}(T)·D_{13|24}(T)·D_{14|23}(T), homogeneous degree 108, SL(6)^4-invariant, hence holomorphic SLOCC invariant. Max-normalized Ĵ = J/sup|J|; proved sup|J| = 1 so Ĵ = J.
- G = Rather golden AME(4,6) state: all three 36×36 flattenings are unitary/6 (2-unitarity, P1). rho* = Wojcik optimal mixed 2-uniform 4-quhex state of purity 1/2 (P4).

## Result
Let J be as above, max-normalized (sup|J| = 1, attained).
- (A) Invariant gap: |J(G)| = 1 ≥ 1/2, and J(S) = 0 for every 4-quhex stabilizer state S (hence every graph state).
- (B) Unconditional radius: every such S satisfies T(G,S) ≥ 1−1/√2 ≈ 0.2929 (quantized rank ≤ 18; ≥ 1−√3/2 ≈ 0.1339 on the unquantized ≤ 27 bound), hence ≥ 1/24. The Wojcik mixed reference satisfies T(G,rho*) ≥ 0.159 ≥ 1/24.
- (C) Obstruction trilemma: any holomorphic homogeneous degree-m invariant I with |I(G)| = g has Euclidean Lipschitz L ≥ m·g on the unit sphere (so g ≥ 1/2, L ≤ 12 forces m ≤ 24; g = 1, L ≤ 12 forces m ≤ 12), while any variety-vanishing structural invariant needs deg ≥ 108 (D1·D2·D3 divides I). The degree-6 epsilon-wiring family is one-dimensional with I6 = ±10/3 ≠ 0 on the quhex GHZ stabilizer — so the literal L ≤ 12 structural holomorphic route is impossible.

## Proof / Evidence
- Normalization: for any 36×36 M with Tr MM† = 1, AM–GM on singular values gives |det M| ≤ 36^{−18}, equality iff M = unitary/6. Hence |J| ≤ 6^108·36^{−54} = 1, attained at any 2-unitary tensor. Replay: verify_fidelity_radius.py (random trials ≤ 1, equality = 1).
- Value at G: each M_c(G) = unitary/6 by Rather 2-unitarity, so |D_c(G)| = 36^{−18} and |J(G)| = 1. Deductive via cited theorem; no 1296-amplitude transcript claimed. Pipeline validated on AME(4,3): verify_ame43.py confirms Q1 = Q2 = 1, per-cut 9^{4.5}|det| = 1, and the stabilizer-AME negative control also gives 1 (no gap where stabilizer AME exists, as theory demands).
- Vanishing: Cha CRT factorization S =_loc S2 ⊗ S3 plus Higuchi–Sudbery no AME(4,2) implies some 2-vs-2 cut has non-maximal qubit factor; quantized rank ≤ 2 (unquantized ≤ 3) times qutrit rank ≤ 9 gives rank(S|_c) ≤ 18 (≤ 27) < 36, so D_c(S) = 0 and J(S) = 0. Wojcik Thm 1 gives the same for graph states factorization-free.
- Radius: on the vanishing cut G_red = I/36, S_red eigenvalues λ_i: F = (1/6)Σ√λ_i ≤ √r/6 (Cauchy–Schwarz, equality for flat spectrum), i.e. ≤ 1/√2 (r = 18) resp. √3/2 (r = 27). T ≥ 1−F plus monotonicity under partial trace. Constants replayed (r = 0.2929 vs 1/24 ratio 7.03). Mixed: F(G,rho*)² = <G|rho*|G> ≤ ‖rho*‖_∞ ≤ √purity = 1/√2, so T ≥ 0.159.
- Trilemma: (a) f(θ) = I(e^{iθ}G) = e^{imθ}I(G) gives L ≥ m·g. (b) Ideal of maximal minors is prime; I|_{V1} ≡ 0 ⇒ D1|I; paired-Bell witnesses show D1 ≢ 0 on V2 etc. (rank 1-vs-36, |det| = 6^{−36} ≈ 9.7e−29 on transverse cuts, verify_paired_bell.py), giving D1D2D3|I, deg ≥ 108 — incompatible with m ≤ 24. (d) Every degree-6 epsilon wiring equals ±I_id (ε_{σ(s)} = sgn(σ)ε_s) and I6(GHZ_4) = 720/216 = 10/3 ≠ 0 (exact sympy; wirings ±10/3, verify_ghz_I6.py).

## Limitations
- No 1296-amplitude machine-readable golden vector obtained; |J(G)| = 1 is deductive via Rather's proved 2-unitarity, not a direct amplitude transcript.
- Vanishing uses cited black boxes: Cha CRT factorization (Hostens/Looi convention), Higuchi–Sudbery, stabilizer rank quantization, prime minor ideals.
- Degree ≤ 24 finite-set interpolation route left open (neither proved nor disproved). J is degree 108, not Verstraete low-degree type; radius is fidelity-based, not Lipschitz-based.

## Reproducibility
- python3 output/artifacts/verify_ame43.py — pipeline + negative control
- python3 output/artifacts/verify_fidelity_radius.py — AM-GM bound, radii, L ≥ m·g demo
- python3 output/artifacts/verify_ghz_I6.py — 10/3 obstruction + wirings
- python3 output/artifacts/verify_paired_bell.py — non-containment witnesses + rank-2 GHZ cut
All replay with numpy/sympy only, VERIFY_OK.

## References
- Rather et al., arXiv:2104.05122 — golden AME(4,6)/2-unitary 36, ((3,6,2))_6 code.
- Wojcik et al., arXiv:2603.18193 — no N=4n even-d graph AME; mixed purity-1/2 (4,6).
- Cha, arXiv:2603.13442 — stabilizer AME prime-power reduction.
- Casas et al., arXiv:2504.05394 — non-stabilizer AME circuits.
- Scott, quant-ph/0310137 — multipartite Q measures.
- Higuchi–Sudbery, Phys. Lett. A 273 (2000) — no AME(4,2).
