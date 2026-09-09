# Minimal Dilation Saturation Holes for Height-≤3 Kronecker Triples within S_n, n≤12

## Context

Kronecker coefficients govern tensor-product multiplicities of symmetric-group
irreducibles. Unlike Littlewood–Richardson coefficients, they fail the
saturation property: `g(λ,μ,ν) = 0` can coexist with
`g(kλ,kμ,kν) > 0` for an integer dilation factor `k > 1`.
Such triples are called saturation (or dilation) holes; they witness the gap
between the Kronecker cone and the Kronecker semigroup and are of recognized
interest for saturation studies, complexity lower bounds, and the GCT program
(Ikenmeyer–Mulmuley–Walter; Burgisser–Landsberg–Manivel–Weyman; Klyachko
marginals). Asymptotic hole theorems prove many holes exist but record no
exact minimal-hole census in any bounded few-row window.

## Definitions

- `g(λ,μ,ν)` is the Kronecker coefficient: the multiplicity of
  `[ν]` in `[λ] ⊗ [μ]`, computed by the class-algebra inner product
  `g = (1/n!) Σ_C |C| χ_λ(C)χ_μ(C)χ_ν(C) = Σ_C χ_λχ_μχ_ν/z_C`.
- `kλ` is dilation: every part multiplied by `k` (so `|kλ| = k|λ|`).
- Height `ℓ(λ)` is the number of parts. Window: all **ordered** base triples
  `(λ,μ,ν)` with `|λ| = |μ| = |ν| = n ≤ 6` and `ℓ ≤ 3` (568 triples total).
- Stretches: `k = 2` at degree `2n ≤ 12` for every vanishing base triple;
  `k = 3` at degree `3n ≤ 12` only where `3n ≤ 12` (i.e. `n ≤ 4`).
  No claim is made outside this window.

## Result

Over the 568 ordered height-≤3 base triples with `n ≤ 6`:

- Base positivity: 280 have `g > 0`; 288 vanish.
  Per-`n` zeros for `n = 1..6`: 0, 4, 16, 33, 51, 184.
  Per-`n` nonzeros: 1, 4, 11, 31, 74, 159.
- Dilation holes at `k = 2`: exactly **42** of the 288 vanishing triples lift
  to `g(2λ,2μ,2ν) > 0`, per-`n` 0, 1, 4, 6, 0, 31.
  In-window hole rate 42/288 = 14.58%.
- `k = 3`: no `k = 3`-only hole in-window. All 4 triples with `g₃ > 0`
  (all at `n = 3`) already have `g₂ > 0`; at `n = 4`, `g₃ = 0` throughout.
  `n = 5` is hole-free at `k = 2` (all 51 zeros stay 0 at `n = 10`).
- **Lex-least dilation hole** (ordered-lexicographic on `(n,λ,μ,ν)`):
  base `((1,1),(1,1),(1,1))` at `n = 2` has `g = 0`; its 2-stretch
  `((2,2),(2,2),(2,2))` at `n = 4` has `g = 1`.
  Its 3-stretch `((3,3),(3,3),(3,3))` at `n = 6` has `g = 0`
  (non-monotone dilation).
- Runner-up: `((1,1,1)³)` at `n = 3` has `g = 0`;
  `((2,2,2)³)` at `n = 6` has `g = 1`.

## Proof / Evidence (computational proof)

Exact exhaustive computation with integer certificates, independently
re-audited by a disjoint Frobenius-polynomial route
(Vandermonde × power-sums in 3 variables, coefficient extraction —
no Murnaghan–Nakayama subset enumeration):

- Lex-least base, `N = 2`, classes `(2)` (size 1, χ = −1) and `(1²)`
  (size 1, χ = +1): terms −1, +1; sum 0; `g = 0/2! = 0`. `z`-route
  `−1/2 + 1/2 = 0`.
- Lex-least stretch, `N = 4`, `χ_(2,2) = (0,−1,2,0,2)` on
  `(4),(3,1),(2²),(2,1²),(1⁴)` with sizes `6,8,3,6,1`:
  terms `0, −8, +24, 0, +8`; sum `24 = 4!`; `g = 1`.
  `z`-route `−8/3 + 24/8 + 8/24 = 1`.
- Runner-up base `N = 3`: terms `+2, −3, +1` (sizes `2,3,1`); sum 0; `g = 0`.
  Runner-up stretch `N = 6`: 11-class terms including
  `−90, +90, +320, −120, −40, +405, +45, −15, +125`; sum `720 = 6!`; `g = 1`.
- Full-table audit: independent Frobenius recomputation reproduces every
  base zero/nonzero label (zeros 0,4,16,33,51,184), all 288 stored `g₂`
  values (holes 0,1,4,6,0,31), and all 53 in-window `g₃` values with zero
  mismatches; zero-triple sets match file row-for-row at each `n`.
  Lex-minimality verified per slice; `n = 5` gives 0/51 lifts at `N = 10`.
- Candidate tables additionally satisfy row orthogonality `Σ|C|χ² = n!`,
  hook-length dimension checks, and dual-route agreement at every `N ≤ 12`.

## Limitations

- Ordered triples (not S₃-quotiented); counts and lex order use that convention.
- `k = 3` only where `3n ≤ 12`; `n = 5, 6` have no `g₃` by design.
- Window-limited census (`n ≤ 6` base, `N ≤ 12` stretched); no general
  saturation theorem or criterion is claimed.
- Evidence is computational (exact integer arithmetic), not a structural proof.

## Reproducibility

- `output/artifacts/hole_table.json`: all 288 vanishing rows with
  `(g₂, g₃ or null when 3n > 12)`, per-`n` tallies, and the 42-hole list.
- `output/artifacts/cert_base_zero.txt`,
  `cert_stretch_pos.txt`, `cert_runnerup_base.txt`,
  `cert_runnerup_stretch.txt`: committed class-sum certificates above.
- Candidate code `inputs/artifacts/compute1_tables.py`
  (Murnaghan–Nakayama, dual routes A/B) and replay script
  `inputs/artifacts/verify_replay.py` document the original computation.
- Audit replay used only stdlib exact arithmetic (Frobenius in 3 variables
  + `Σ abc/z` with `Fraction`); every Kronecker value is an exact integer
  quotient. Rerun time is minutes on one core.

## References

- C. Ikenmeyer, K. Mulmuley, M. Walter, On vanishing of Kronecker
  coefficients, arXiv:1507.02955. Asymptotic holes; NP-hardness; holes
  "of great interest".
- C. Ikenmeyer, G. Panova, All Kronecker coefficients are reduced Kronecker
  coefficients, arXiv:2305.03003. Reduced-vs-ordinary construction.
- S. Sam, A. Snowden, Proof of Stembridge's conjecture on stability of
  Kronecker coefficients, arXiv:1501.00333. Padding (not dilation) stability.
- I. Pak, G. Panova, On the complexity of computing Kronecker coefficients,
  arXiv:1404.0653. Bounded-parts tractability; height-≤3 feasibility support.
- P. Bürgisser, J. Landsberg, L. Manivel, J. Weyman, An overview of
  mathematical issues arising in the GCT approach to VP vs VNP,
  arXiv:0907.2850. GCT motivation for semigroup base cases.
