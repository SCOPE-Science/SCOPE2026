# Complete Walsh-Hadamard Nonlinearity Distribution of All Rotation-Symmetric Boolean Functions in Seven Variables

## Context
Nonlinearity governs resistance to linear cryptanalysis and equals the distance to the first-order Reed-Muller code RM(1,n); its maximum is the covering radius. Rotation-symmetric Boolean functions (RSBFs) form a cryptographically relevant, computationally tractable subclass. Prior literature gives counts, general bounds and heuristic high-nonlinearity examples, but no openly reproducible complete Walsh-certified nonlinearity distribution with canonical extremal representatives for the full n=7 RSBF class (2^20 functions).

## Definitions and conventions
- Variables `x0..x6`. Integer `v in 0..127` encodes `x` by bit `i` (LSB=`x0`) = `xi`.
- Rotation `rho(v)=((v>>1)|((v&1)<<6))&0x7F`, i.e. `(x0,..,x6)->(x1,..,x6,x0)`.
- `f:{0,1}^7->{0,1}` is rotation-symmetric iff `f(rho(x))=f(x)`. The 128 inputs split into `G=20` orbits: `g_7=(2^7+6*2)/7=20`, namely `{0}`, `{127}` plus 18 orbits of size 7. Sorted by minimal element `m`: `0,1,3,5,7,9,11,13,15,19,21,23,27,29,31,43,47,55,63,127` with weights `0,1,2,2,3,2,3,3,4,3,3,4,4,4,5,4,5,5,6,7`.
- Mask `m in 0..2^20-1`: bit `k` = `f`-value on orbit `k` (`k=0` is `{0}`). Truth table `T_m[v]=(m>>orbit_id[v])&1`.
- Dot product `a.x=parity(a&x)`. Walsh transform `W(a)=sum_x(-1)^{f(x)+a.x}` by integer FWHT in natural binary order. Nonlinearity `nl(f)=64-max_a|W(a)|/2` (`N/2-max|W|/2`, `N=128`).
- ANF vector `A` (length 128) by binary Mobius transform; `A` is likewise rotation-symmetric. ANF-orbit mask: bit `j=A[orbit_min[j]]`. Truth->ANF is GF(2)-linear `20x20` with row masks (ANF orbit `j` <- truth mask): `0x00001,0x00003,0x00005,0x00009,0x0001b,0x00021,0x0006f,0x000af,0x001e5,0x00207,0x00423,0x00e51,0x010e9,0x02691,0x07c3b,0x080cd,0x12f27,0x2aa1f,0x4b92d,0xfffff`, rank 20 (bijective). Degree = max `wt(u)` with `A[u]=1` (`-1` for zero function).
- Hex packing: 16 bytes; byte `j` holds `T[8j..8j+7]` LSB-first.
- Canonical representative per `nl`: among masks attaining that `nl`, minimize full 128-bit ANF vector lexicographically (`v=0` first), i.e. lex order on ANF-orbit bits with orbit 0 most significant.

## Result (computed theorem)
Under the above conventions, the `1048576` RSBFs in `n=7` have:

(a) Exact nonlinearity histogram (`nl:count`), summing to `1048576`; no other values occur:

| nl | count | nl | count | nl | count |
|----|-------|----|-------|----|-------|
| 0 | 4 | 28 | 12240 | 48 | 12460 |
| 1 | 8 | 29 | 24480 | 49 | 100968 |
| 2 | 4 | 30 | 12240 | 50 | 176344 |
| 7 | 72 | 35 | 33264 | 51 | 118440 |
| 8 | 144 | 36 | 66528 | 52 | 70000 |
| 9 | 72 | 37 | 33264 | 53 | 48720 |
| 14 | 612 | 42 | 64512 | 54 | 23940 |
| 15 | 1224 | 43 | 129024 | 55 | 22344 |
| 16 | 612 | 44 | 64512 | 56 | 11788 |
| 21 | 3264 | 45 | 280 | | |
| 22 | 6528 | 46 | 1820 | | |
| 23 | 3264 | 47 | 5600 | | |

Hence the RSBF-restricted covering radius of `RM(1,7)` is `max nl=56`, equal to the unrestricted covering radius `56`.

(b) Extremal counts: `11788` maximizers (`nl=56`, `max|W|=16`, ~1.124%) and `22344` next-maximizers (`nl=55`, `max|W|=18`).

(c) Lex-min representatives (full per-nl table with hex, weight, `W0`, `acmax`, `|W|` multiset archived):
- `nl=56`: truth mask `194304` (`0x2f700`), ANF mask `46848` (`0x0b700`), degree 4, weight 56, `W0=16`, `truth_hex 008028eae02eec5c80f67c2ed8765a13`, `anf_hex 0080286ae02e6c1480767c0658161201`, ANF orbits `{8,9,10,12,13,15}` (mins `15,19,21,27,29,43`), `|W| {0:64,16:64}` (signed `-16:28,0:64,+16:36`), autocorrelation `|r| (s!=0) {0:63,16:64}`, max 16. Full 128-point `W` and `r(s)` archived.
- `nl=55`: truth mask `718592` (`0xaf700`), ANF mask `571136` (`0x8b700`), degree 7, weight 57, `W0=14`, `truth_hex 008028eae02eec5c80f67c2ed8765a93`, `anf_hex 0080286ae02e6c1480767c0658161281`, ANF orbits `{8,9,10,12,13,15,19}` = max ANF plus `x0...x6`, `|W| {2:64,14:36,18:28}`, autocorr max 20.
- `nl=56` ANF orbit-sum (each group one rotation orbit-sum): `(x0x1x2x3+x0x1x2x6+x0x1x5x6+x0x4x5x6+x1x2x3x4+x2x3x4x5+x3x4x5x6)+(x0x1x4+x0x3x4+x0x3x6+x1x2x5+x1x4x5+x2x3x6+x2x5x6)+(x0x2x4+x0x2x5+x0x3x5+x1x3x5+x1x3x6+x1x4x6+x2x4x6)+(x0x1x3x4+x0x1x4x5+x0x2x3x6+x0x3x4x6+x1x2x4x5+x1x2x5x6+x2x3x5x6)+(x0x1x2x5+x0x1x4x6+x0x2x3x4+x0x3x5x6+x1x2x3x6+x1x3x4x5+x2x4x5x6)+(x0x1x3x5+x0x2x3x5+x0x2x4x5+x0x2x4x6+x1x2x4x6+x1x3x4x6+x1x3x5x6)`. The `nl=55` lex-min adds `+x0x1x2x3x4x5x6`.

(d) Affine-inequivalence lower bounds via invariants (degree for `deg>=2`, multiset `{|W(a)|}`, multiset `{|r(s)|,s!=0}` and its max; `W0`/weight explicitly not used as EA maps move the spectrum):
- Maximizers: degree distribution `2:28,3:560,4:5880,5:4704,6:616`; 4 `|W|` types `{0:64,16:64}`, `{0:22,8:56,16:50}`, `{0:1,4:28,8:28,12:36,16:35}`, `{0:8,4:56,12:8,16:56}`; `acmax in {16,40,72,96,128}`; jointly 11 distinct `(degree,|W|,acmax)` groups, hence >=11 affine classes.
- Next-maximizers: all degree 7; 4 `|W|` types x `acmax` values give >=12 affine classes. Max vs next-max inequivalent by `nl` alone.
- Exact class counts (upper bounds) are not claimed. Bounded random affine search (100k trials x 4 pairs, all NOT-FOUND) is consistency evidence only and proves nothing given group size ~5e18.

What is proved vs computed: (a)-(c) are exhaustive computations (proof by deterministic enumeration with independent re-implementation); (d) lower bounds are mathematical consequences of affine-invariant equalities evaluated on enumerated sets.

## Proof / evidence
- Deterministic C enumeration `masks 0..2^20-1 -> polarity -> in-place integer FWHT(128) -> max|W| -> nl`; ANF mask via 20-bit row parities; lex-min tracking per `nl`. Second dump pass collected all `nl in {55,56}`; bulk invariant pass computed degree, weight/`W0`, full `|W|` histogram, autocorrelation max via `R=FWHT(W^2)/N` (exact division). Parseval `sum W^2=16384` holds for every extremal mask.
- Independent NumPy FWHT+Mobius re-verified all 33 lex-min reps (nl, ANF mask, degree, spectra); naive `O(N^2)` Walsh double loop matches on 33 best + 20 random (Python) and 1000 deterministic pseudo-random masks (C, seed `0xDEADBEEF12345678`); histogram sums to `1048576` in both tallies; full 128-integer spectra for both extremal lex-min reps published for direct `nl=64-max|W|/2` check; SHA-256 checksums archived.
- Independent audit reproduced: orbits/G, full histogram via batched NumPy FWHT over all 1048576 masks (exact match), all-33 lex-min via batched Mobius+FWHT (exact match), all-33 invariants + Parseval, extremal spectra bit-for-bit, hex packing, degree/weight distributions, 11/12 collapsed cluster counts, SHA-256 of all files.

## Limitations
- Originality capped: live-web prior-art search unavailable; comparison rests on knowledge-cutoff sources. No priority claim; a missed thesis/paper with same table would supersede novelty but not correctness.
- Partial classification: only lower bounds on affine classes (11/12); full classification open.
- Scope RSBF subclass only; nothing about non-symmetric functions beyond equality of restricted/unrestricted covering radii in n=7.
- Conjecture (not claimed): structured low-nl gaps (33 values; steps of 7 below nl=44) suggest a divisibility theorem for RSBF Walsh values.

## Reproducibility
Compile with `gcc -O3` (no external deps; Python needs only NumPy for second implementation). Bit order, orbit order and hex packing must not be altered; they are part of the claim.
- `generator_rsbf7.c` -> full sweep + histogram + best-per-nl (seconds).
- `generator_dump_extreme.c` -> maximizer/next-max lists.
- `generator_analyze_bulk2.c` -> joint invariant clusters.
- `generator_affine_search.c maskF maskG trials seed` -> bounded search.
- `generator_verify_naive1000.c` -> 1000-mask naive check.
- `second_impl_verify.py`, `gen_final_artifacts.py` -> independent verification + final tables.
Artifacts: `nl_histogram.csv`, per-value representatives (`representatives_full.csv`, `anf_expressions.txt`), full 128-point Walsh spectra for extremals, `orbits_and_map.txt`, generator code, run logs, `SHA256SUMS`.

## References
- Stanica-Maitra, Rotation symmetric Boolean functions: count and cryptographic properties, Discrete Applied Mathematics 2008. https://doi.org/10.1016/j.dam.2007.05.029
- Kavut-Maitra-Sarkar-Yucel, Search for Boolean functions with excellent profiles, ePrint 2006/449 ff. https://eprint.iacr.org/2006/449
- Carlet, Boolean Functions for Cryptography and Coding Theory (Walsh spectrum, nonlinearity, covering radius). https://www.math.univ-paris13.fr/~carlet/chap-fcts-Bool.pdf
