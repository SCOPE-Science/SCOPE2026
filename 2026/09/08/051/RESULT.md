# Replayable Walsh Census of All 2^16 Boolean Functions in n=4 and the 256 Rotation-Symmetric Functions in n=5

## Context and motivation

Bent functions, nonlinearity, covering radius of first-order Reed–Muller codes,
and resiliency order are long-recognized cryptographic and combinatorial
benchmarks for S-box design. Exact small-n spectra and extremal witnesses
ground all general covering-radius and nonlinearity bounds. Exhaustive n=4
(2^16 truth tables) is the last fully feasible complete n before the 2^32
wall at n=5; rotation-symmetric Boolean functions (RSBFs) form a
literature-natural structured slice (Maitra–Stanica / Kavut line) that makes
an n=5 census tractable while retaining cryptographic interest. Isolated
values (rho(RM(1,4)) = 6, 896 bent functions in n=4, the Maiorana–McFarland
witness) are classical; the result is the joint stratified,
Parseval-checked, truth-table-replayable census itself.

## Definitions

Let f : {0,1}^n -> {0,1} with polarity a(x) = (-1)^{f(x)} in {±1}.
Walsh spectrum: W_f(u) = sum_{x in {0,1}^n} (-1)^{f(x) + u·x}.
Fast Walsh–Hadamard Transform (FWHT) computes all 2^n values in exact
integer arithmetic.
Nonlinearity: nl(f) = 2^{n-1} - (1/2) max_u |W_f(u)|.
f is balanced iff W_f(0) = 0; f is m-resilient iff balanced and
W_f(u) = 0 for all 1 <= wt(u) <= m. "Unbalanced" is encoded as resiliency -1.
Parseval identity: sum_u W_f(u)^2 = 2^{2n} for every f.
Covering radius: rho(RM(1,n)) = max_f nl(f).
RSBF in n=5: f invariant under cyclic rotation x -> (x1,x2,x3,x4,x0);
the 32 inputs partition into 8 rotation orbits.

## Result

Lemma (Parseval). For every f, sum_u W_f(u)^2 = 2^{2n}.
Lemma (Covering radius). rho(RM(1,4)) = 6: Parseval gives max|W_f| >= 2^{n/2}
= 4 for n=4, so nl(f) <= 8 - 2 = 6 for all f, and the witness below attains 6.

(a) Full n=4 census (65536 functions). Nonlinearity marginal:
nl=0: 32 (= 2^{n+1} affine functions); 1: 512; 2: 3840; 3: 17920;
4: 28000; 5: 14336; 6: 896 (bent, all unbalanced).
Resiliency marginal: -1 (unbalanced): 52666; 0: 12648; 1: 212; 2: 8; 3: 2.
Joint (nl, resiliency) -> count:
(0,-1):2, (0,0):8, (0,1):12, (0,2):8, (0,3):2;
(1,-1):512;
(2,-1):1920, (2,0):1920;
(3,-1):17920;
(4,-1):17080, (4,0):10720, (4,1):200;
(5,-1):14336;
(6,-1):896.
Rows sum to marginals; total 65536. Maximum nl = 6, hence rho(RM(1,4)) = 6.

(b) RSBF n=5 slice (256 functions, 8 rotation orbits
{0},{31},{1,2,4,8,16},{3,6,12,17,24},{5,9,10,18,20},{7,14,19,25,28},
{11,13,21,22,26},{15,23,27,29,30}, sizes 1,1,5,5,5,5,5,5).
Nonlinearity marginal: 0:4; 1:8; 2:4; 5:24; 6:48; 7:24; 10:36; 11:72; 12:36.
Resiliency marginal: -1:216; 0:30; 1:8; 4:2.
Joint (nl, resiliency) -> count:
(0,-1):2, (0,4):2, (1,-1):8, (2,-1):2, (2,0):2, (5,-1):24, (6,-1):48,
(7,-1):24, (10,-1):18, (10,0):18, (11,-1):72,
(12,-1):18, (12,0):10, (12,1):8.
Slice maximum nl = 12, attained by 36 functions (18 balanced, 18 unbalanced),
so rho(RM(1,5)) >= 12. The only 4-resilient RSBFs are the two affine
functions (nl = 0).

(c) Certified witnesses.
Bent witness (n=4): f = x0x1 + x2x3, truth table 30856, ANF degree 2,
unbalanced (res -1). Full spectrum:
[4,4,4,-4, 4,4,4,-4, 4,4,4,-4, -4,-4,-4,4]; all |W| = 4,
Parseval sum 256 = 2^8, nl = 8 - 4/2 = 6.
Balanced RSBF witness at slice maximum (n=5): orbit mask 30, truth table
2165774206, ANF degree 2, balanced, resiliency 0, max|W| = 8, nl = 12.
Spectrum:
[0,-8,-8,0,-8,0,0,8,-8,0,0,8,0,8,8,0,-8,0,0,8,0,8,8,0,0,8,8,0,8,0,0,-8];
Parseval sum 1024 = 2^10.
1-resilient RSBF witness at slice maximum: orbit mask 58, truth 2468239080,
ANF degree 3, resiliency exactly 1, max|W| = 8, nl = 12. Spectrum:
[0,0,0,0,0,8,0,8,0,8,8,0,0,0,8,-8,0,0,8,8,8,0,0,-8,0,8,0,-8,8,-8,-8,-8];
Parseval 1024 (W(0) and all weight-1 positions vanish; weight-2 position 5 is 8).

## Proof versus computed evidence

Proved: Parseval lemma (character orthogonality); covering-radius lemma
rho(RM(1,4)) = 6 (Parseval upper bound plus attaining witness); orbit
partition sizes. Classical and not claimed new: rho(RM(1,4)) = 6 as a value,
896 bent count, Maiorana–McFarland construction. Computed evidence (exact,
Parseval-checked, independently re-verified): both joint tables, witness
spectra, resiliency cross-checks (Walsh-zero conditions versus independent
fixing / Xiao–Massey definition, 65536/65536 and 256/256 agreement).
No conjectures are asserted.

## Limitations

Full-space n=5 (2^32) is untouched; only the 256-function RSBF slice and its
lower bound rho(RM(1,5)) >= 12 are claimed. Rotation means the cyclic shift;
dihedral or other symmetry classes are out of scope. Isolated n=4 values and
the bent witness are classical; novelty is the joint replayable census artifact.

## Reproducibility

Stdlib Python 3 only, runs in seconds. `census.py` enumerates 65536 n=4
truth tables and 256 RSBF n=5 orbit-masks with exact-integer FWHT, asserting
Parseval on every function, cross-checking resiliency by both definitions,
and writing `n4_joint.csv`, `rsbf5_joint.csv`, `rsbf5_orbits.csv`,
`witnesses.json`, `run_log.json` (with SHA-256 hashes). `verify.py` uses an
independent FWHT to replay all 256 RSBF spectra from committed orbit masks
against the joint cells, check n=4 totals (65536, bent 896, affine 32), and
replay both witnesses; it prints
`VERIFY_OK n4_total=65536 bent=896 rsbf5_total=256 slice_max=12`.
SHA-256: n4_joint.csv fd712c5e..., rsbf5_joint.csv 3abd2241...,
rsbf5_orbits.csv 4cd3380e..., witnesses.json c301ba8b... (full hashes in
run_log.json).

## References

- OEIS A004491, Number of bent functions of 2n variables (marginal 2,8,896,...).
- J. K. Haugland, A lower bound on the number of bent squares, arXiv:2508.14605.
- N. Anbar et al., On functions with the maximal number of bent components, arXiv:2010.03801.
- S. Hodzic et al., Designing plateaued Boolean functions in spectral domain and their classification, arXiv:1811.04171.
- S. Kavut and M. D. Yucel, 9-variable Boolean Functions with Nonlinearity 242 in the Generalized Rotation Class, arXiv:0808.0684.
