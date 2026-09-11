# Certified lift-16 (3,4)-regular QC window obstruction for Q16 (n=400, k=28)

## Context

Small lifted-product / quantum Tanner instances with certified expansion,
distance, and single-shot decodability are sought for fault-tolerant overhead
estimates. Asymptotic theorems (Panteleev–Kalachev, Leverrier–Zémor, Gu et al.)
leave small certifiable windows open. The admitted target pursued a
(3,4)-regular quasi-cyclic lift-16 instance Q16 with a Tanner spectral bound
implying linear distance/soundness plus a BP+SSF threshold witness.
The work found the spectral leg provable but arithmetically too weak to imply
anything, the instance distance small, and the threshold missed. The submitted
claim is the rigorous obstruction, filed as `EMERGENT_FINDING`.

## Definitions

- Shift matrix over Z_16: `A = [[14,1,9,6],[12,10,6,0],[4,4,8,3]]`, lift `L=16`.
- Base QC matrix `HA = expand_QC(A,16)`, 48×64, column weight 3, row weight 4,
  Tanner girth ≥6 (no 4-cycles: `(A[i1][j1]-A[i1][j2]-A[i2][j1]+A[i2][j2]) mod 16 ≠ 0`).
- Symmetric lifted product with `B=A`: `HX = [A⊗I | I⊗B]`,
  `HZ = [I⊗B* | A*⊗I]` (`*` = negated shifts mod 16).
  `HX,HZ` are 192×400, row weight 7, ranks 186/186, `N=400`, `k=28`,
  `HX·HZ^T=0`.
- `M = HA·HA^T` (exact 48×48 integer matrix, every row sums to 12).
- `s2` = second singular value of `HA` = sqrt(second eigenvalue of `M`);
  `lambda2(T16)` used synonymously.
- Classical base code: kernel of `HA` (length 64). Quantum code Q16: CSS
  kernel pair of `HX,HZ`.

## Result (headline)

For the logged Q16/T16 instance:

1. **Certified gap:** every nontrivial singular value of `HA` is ≤ 2.73,
   i.e. `lambda2(T16) ≤ 2.73 < sqrt(12) ≈ 3.4641`, by exact rational inertia.
   Numerically `s2 = 2.72800676`. The bound `≤ 2.70` is **false** for these
   matrices (exact inertia gives 9 eigenvalues above `2.70^2`).
2. **Transfer void:** with var-degree `c=3`, the Tanner small-set guarantee
   `|N(S)|/|S| ≥ c^2/s2^2` yields at most `9/2.73^2 = 90000/74529 ≈ 1.2076`,
   below `c/2 = 1.5` needed for any distance and below `3c/4 = 2.25` needed
   for SSF/soundness. Needing factor >1.5 is `s2 < 3/sqrt(1.5) ≈ 2.4495`.
   Bounded search (≈120k random matrices + annealing) floors at `≈2.728`,
   so the transfer leg is blocked instance-wide and empirically window-wide.
3. **Exact distances:** base classical distance is exactly 8 (no word ≤7 by
   exhaustive `C(64,4)=635376` meet-in-the-middle; explicit weight-8 word
   `{18,22,26,30,34,38,42,46}`).
   Quantum distance `d(Q16) ≤ 7` via explicit support
   `W={0,80,160,240,256,320,384}` in `ker HX ∩ ker HZ` outside both row spaces
   (genuine X- and Z-logical). No quantum lower bound is claimed.
4. **Decoding operating point (experimental):** fixed-seed min-sum BP
   (damping 0.8, ≤40 iters) + greedy SSF, X side, 300 shots/point:
   code-capacity LER 0.0000/0.0200/0.0500/0.1733/0.5400 at
   `p=0.03/0.04/0.05/0.06/0.075` (7.5% bar missed);
   phenomenological noisy syndrome (`q=p`, BP only) LER ≈0.60 at `p=q=0.01`,
   ≈0.76 at `0.02` (no suppression near 3% reference).

Bottom line: attainable gap of this natural window pinned at 2.728
(certified 2.73); standard spectral-to-distance/soundness route proved void
there; overhead work should change lift size or degree.

## Proof / evidence (what was replayed)

- `build_q16.py → BUILD_OK`: 4-cycle count 0; ranks 186/186; orthogonality
  violations 0; `n=400 k=28`; top singular values
  `[3.46410161, 2.72800676×2, …]` (independently reconfirmed with numpy).
- `inertia_cert.py → LAMBDA2_CERT_OK`: `T=2.73^2=74529/10000`; exact
  `Fraction` symmetric LDL congruence of `(T·I−M)` gives inertia
  `(pos,neg,zero)=(47,1,0)` with zero 2×2 blocks. By Sylvester, exactly one
  eigenvalue of `M` exceeds `T`. Row-sum 12 checked exactly, so spectral
  radius ≤12 with all-ones eigenvector eigenvalue 12; the one above `T` is
  the trivial Perron value. Hence all others ≤T. Replayed PASS.
- `check_270.py → CHECK270_OK`: same program at `T=2.70^2=729/100` gives
  `(39,9,0)`: nine eigenvalues above `2.70^2` (12 plus four pairs near
  2.70–2.73). Independently confirmed numerically (9 above 2.70, 1 above
  2.73). So `lambda2 ≤ 2.70` is false; fallback criterion correctly FAILS.
- `transfer_void.py → TRANSFER_VOID_OK`: exact `Fraction` check
  `9/2.73^2=10000/8281≈1.2076 < 3/2` and `< 9/4`; need
  `3/sqrt(1.5)≈2.4495 < 2.728`. Arithmetic only about what the spectral
  lower bound can certify, not a claim that true expansion is bounded above.
- `classical_d8.py → CLASSICAL_D8_OK`: 43745 syndromes of weight ≤3 all
  distinct (proves no word ≤3 and no collision among ≤3); all 635376
  4-patterns miss the table (proves no word ≤7 via 4+(≤3) split, including
  overlapping case as symmetric difference); explicit weight-8 word syndrome
  0. Logic reviewed and replayed PASS.
- `quantum_w7.py → QLOGICAL_W7_OK`: `W` syndrome 0 under both `HX,HZ`;
  exact RREF reduction over 400-bit masks shows `W` outside both row spaces.
  Reduction logic reviewed (full Gauss–Jordan, ordered reduction) and
  replayed PASS. Yields `d≤7` under either X/Z convention.
- `bp_replay.py → BP_REPLAY_OK` (replayed, ~minutes): code-capacity
  `p=0.03:0.0000, 0.04:0.0200, 0.05:0.0500, 0.06:0.1733, 0.075:0.5400`;
  noisy `0.01:0.5967, 0.02:0.7600`. Matches draft up to stated `~` rounding.
  Experimental, not a theorem; seeds/method fixed.

## Limitations

- Quantum lower bound (ruling out weight ≤6 logicals) not completed; only
  `d≤7` certified on quantum side.
- Noisy-syndrome leg used naive BP without soft-syndrome/SSF tuning.
- Window floor `~2.728` (120k samples + annealing) is strong empirical
  evidence, not a theorem; window-wide unreachability of 2.70 is not proved,
  only the instance falsification at 2.70 is proved.
- Inertia certificate covers the base 48×64 Tanner matrix, not the full
  400-qubit quantum complex.
- BP logs are 300 shots/point with one decoder setting; operating point only.

## Reproducibility

All artifacts stdlib+numpy only, deterministic. From `output/artifacts/`:

```
PYTHONPATH="" python3 build_q16.py      # BUILD_OK
PYTHONPATH="" python3 inertia_cert.py   # LAMBDA2_CERT_OK
PYTHONPATH="" python3 check_270.py      # CHECK270_OK
PYTHONPATH="" python3 classical_d8.py   # CLASSICAL_D8_OK
PYTHONPATH="" python3 quantum_w7.py     # QLOGICAL_W7_OK
PYTHONPATH="" python3 transfer_void.py  # TRANSFER_VOID_OK
python3 bp_replay.py                    # BP_REPLAY_OK
```

Shift matrix, dimensions, ranks, and seeds logged above.

## References

- N. Raveendran, D. Declercq, B. Vasić, On the Minimum Distances of
  Finite-Length Lifted Product QLDPC Codes, arXiv:2503.07567 (necessary-only
  finite-length LP distance conditions; no small-lift lambda2 certificate).
- S. Gu et al., Single-shot decoding of good quantum LDPC codes,
  arXiv:2306.12470 (asymptotic single-shot; no lift-16 witness).
- V. Guemard, G. Zémor, Moderate-length lifted quantum Tanner codes,
  arXiv:2502.20297 (different square-complex lifting; e.g. [[96,2,12]];
  no (3,4) lift-16 Q16 instance).
- Error Correction Zoo: expander_lifted_product, quantum_tanner,
  lifted_product, qc_ldpc pages (families only; no lift-16 T16 row or 2.70).
- A. Leverrier, G. Zémor, Quantum Tanner codes, arXiv:2202.13641; decoding
  arXiv:2208.05537 (asymptotic framework for transfer thresholds).
