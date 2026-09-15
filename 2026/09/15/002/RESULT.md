# Atomic two-sided CSS repair obstruction in one homological-product-plus-reduction step

## Context

The admitted target asks for a testable analogue of the Golowich-Guruswami distance-only iteration: iterated homological products with truncation plus Hastings-type locality reduction preserving constant stabilizer weight and uniform constant soundness (linear confinement) at almost-linear dimension and distance. While pursuing that target, exact minimal probes showed the distance mechanism survives but the reduction step is lossy. This record isolates that obstruction as a self-contained finite lemma.

## Definitions

Work over F2. A CSS code is binary parity-check matrices HX, HZ with HX HZ^T = 0. Logical qubits K = n - rank(HX) - rank(HZ). Dressed radius-1 soundness measures, for errors at gauge distance 1, the minimum opposite-side measured syndrome weight; value 0 means a gauge-inequivalent weight-1 error is invisible to the measured syndrome set. The stabilizer convention instead mods out only stabilizer rows and uses the full repaired matrices as syndrome maps. A single-ancilla split of a weight-4 X-check with support halves A|B introduces ancilla q with c1 = 1_A + e_q, c2 = 1_B + e_q; CSS-safety requires both c1, c2 orthogonal to every embedded Z-row.

## Result

Let Q0 = [[4,2,2]] with HX0 = HZ0 = [1 1 1 1] and P the length-2 complex of the [3,2,2] parity code. Form Q0 tensor P and truncate to the middle three terms to obtain Q1. Then:

- Q1 has n = 13, rank(HX) = 6, rank(HZ) = 3, K = 4, row-space sizes 64 and 8, DX = 2, DZ = 4, all 7 X-checks weight 4, all 3 Z-checks weight 5, baseline dressed radius-1 soundness (1.0, 2.0).
- Zero of the 7 unordered bipartitions of a weight-4 X-check admit a CSS-safe single-ancilla split.
- Every consistent Z-gauge repair has exactly 64 solutions per partition, minimum added-fix weight 5 (partition {0,1}|{2,3}) versus 6 (partition {0}|{1,2,3}), and must drop clashing opposite-side checks with net syndrome loss (keep only Z0, respectively keep none).
- Repaired dressed-subsystem radius-1 soundness is (0,0) on both partitions with explicit gauge-inequivalent blind witnesses at dressed distance 1; stabilizer-convention radius-1 soundness is (0.0, 2.0) on both partitions.

## Proof / evidence

Proof is finite exhaustion, machine-verified deterministically in `output/artifacts/verify_emergent.py` (numpy only, GF(2) elimination, exact 2^13/2^14 enumerations, ending ALL EMERGENT-CHECKS PASSED). The script constructs Q1 from the Kunneth tensor-plus-truncation matrices, checks the complex and CSS conditions, computes GF(2) ranks, enumerates all 7 bipartitions for CSS-safety, exhaustively solves HXs g = 0 over 2^13 per partition for fix counts and minimum weights, identifies clashing Z-sets, and enumerates all 2^14 errors for dressed and stabilizer radius-1 soundness with witnesses verified outside the gauge groups. Corroborating probes include product, distance, reduction, gauge, and soundness scripts. The compounding interpretation over infinitely many steps cites Wills-Lin-Hsieh 2024 per-step tax Omega(rho/poly(w)) with no iterable stabilizer.

## Limitations

Proved only for the stated finite instance with single-ancilla splits; no general theorem over all constant-sized 7-term complexes C or multi-ancilla gadgets is claimed. The target's universal quantifier is therefore reported as blocked-with-obstruction, not fully disproved. All ranks are over GF(2); soundness uses the absolute convention, equivalent up to O(1) LDPC factors to normalized variants.

## Reproducibility

Run `python3 output/artifacts/verify_emergent.py`; expected summary: Q1 n=13 K=4 rankHX=6 rankHZ=3, baseline (1.0,2.0), 0/7 safe, p1 64 fixes min weight 5, p2 64 fixes min weight 6, dressed (0,0) both partitions, stabilizer (0,2) both partitions.

## References

- Wills, Lin, Hsieh, Tradeoff Constructions for Quantum Locally Testable Codes, IEEE TIT 2024 (arXiv:2309.05541).
- Golowich, Guruswami, Quantum LDPC Codes of Almost Linear Distance via Homological Products, arXiv:2411.03646.
- Hastings, Weight Reduction for Quantum Codes, arXiv:1611.03790.
- Error Correction Zoo, Homological product code entry.
