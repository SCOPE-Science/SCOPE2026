# Exact hereditary discrepancy and determinant-bound gap for the canonical order-8 Sylvester Hadamard matrix

## Context

The Lovasz-Spencer-Vesztergombi (LSV, 1986) determinant lower bound `detLB`
lower-bounds the hereditary discrepancy `herdisc` of a matrix. Hoffman showed
the two quantities can differ by a near-logarithmic factor. Matousek (2011),
Jiang-Reis (2021), and Li-Nikolov (2023) bound the gap by polylogarithmic
factors and show asymptotic tightness via Kronecker/Haar-type constructions.
Those are asymptotic order estimates; no exact `(disc, herdisc, detLB, ratio)`
tuple or per-submatrix census for the canonical order-8 Sylvester Hadamard
matrix S8 was recorded in those sources. This record pins that exact
calibration point with certificates.

## Definitions

Let `S1 = [[1,1],[1,-1]]` and `S8 = S1 ⊗ S1 ⊗ S1` (Kronecker product), i.e.

```
row0: + + + + + + + +
row1: + - + - + - + -
row2: + + - - + + - -
row3: + - - + + - - +
row4: + + + + - - - -
row5: + - + - - + - +
row6: + + - - - - + +
row7: + - - + - + + -
```

(`+` = +1, `-` = -1). Rows are pairwise orthogonal (Gram = 8I): S8 is Hadamard
of order 8. All claims are entrywise recomputation against this fixed matrix.

For an m×n real matrix A:

- `disc(A) = min_{x in {±1}^n} ||A x||_inf`.
- `herdisc(A) = max over nonempty column subsets J of disc(A[:,J])`.
- `detLB(A) = max over all k×k submatrices B (k ≥ 1) of |det B|^{1/k}`.
- `M_k = max |det|` over k×k submatrices; `detLB = max_k M_k^{1/k}`.
- Gap ratio `R = herdisc(A) / detLB(A)`.

## Result

**Theorem.** For S8 as fixed above:

- (a) `disc(S8) = 4`.
- (b) `herdisc(S8) = 5`.
- (c) Determinant spectrum `M_1..M_8 = 1, 2, 4, 16, 32, 128, 512, 4096`.
- (d) `detLB(S8) = 4096^{1/8} = 2√2 ≈ 2.8284271247`.
- (e) `R = 5/(2√2) = 5√2/4 ≈ 1.7677669530 > 1`: a certified strict separation.

**Witnesses.**

- disc: `x* = (1,1,-1,-1,-1,-1,-1,-1)` gives
  `S8 x* = (-4,0,4,0,4,0,4,0)`, infinity norm 4.
- herdisc: `J* = {0,1,2,3,4,5,6}`, `x* = (1,-1,-1,-1,-1,-1,-1)` gives
  `S8[:,J*] x* = (-5,1,1,3,1,3,3,1)`, infinity norm 5.
- detLB: `B* = S8` itself, `det = 4096`, `4096^{1/8} = 2√2`.
  Each `M_k` is attained by the k×k leading principal submatrix, with signed
  determinants `1, -2, 4, 16, -32, -128, -512, 4096`.

Corroborating distribution over the 255 nonempty column subsets:
`disc=1:8, 2:42, 3:112, 4:85, 5:8`; per subset size:
`1:{1:8}, 2:{2:28}, 3:{3:56}, 4:{4:56,2:14}, 5:{3:56}, 6:{4:28}, 7:{5:8}, 8:{4:1}`.
The value 5 is attained exactly on the eight 7-element subsets.

## Proof / evidence

Finite exhaustive enumeration with exact integer arithmetic (proof by
computation, not an asymptotic argument):

1. Rebuild S8 from the Kronecker definition; check Gram = 8I.
2. Evaluate `||S8 x||_inf` for all 2^8 = 256 signings; minimum 4 (112 attainers).
3. For each of the 255 nonempty column subsets J, evaluate all 2^|J| signings;
   the maximum of the minima is 5, on exactly the eight 7-sets.
4. For every nonempty square submatrix — Σ_{k=1..8} C(8,k)² = 12869 of them —
   compute `|det|` by exact integer elimination (Bareiss in the replay script;
   independently cross-checked with exact rational Gaussian elimination);
   per-k maxima are the `M_k` above.
5. `detLB` is `max_k M_k^{1/k}`: values
   `1, √2≈1.414, ∛4≈1.587, 2, ⁵√32=2, ⁶√128≈2.245, ⁷√512≈2.438, ⁸√4096≈2.828`,
   maximized at k=8. `R = 5/(2√2)` follows exactly.

The replay script `artifacts/verify.py` (stdlib only) performs all steps,
writes `subset_table.csv` / `spectrum.json`, and prints `VERIFY_OK`.

## Limitations

- Values are specific to the committed Kronecker-ordered S8. Invariance of the
  triple under Hadamard equivalence (signed/permuted variants) is asserted by
  symmetry of the enumerated families, not separately enumerated here.
- `detLB` uses the standard `|det|^{1/k}` normalization; the numerical form of
  R depends on that convention.
- No claim beyond order 8; no asymptotic consequence is drawn.
- The proposal text wrote "12870" submatrices; the exact nonempty count is
  12869. The replay script counts 12869 evaluated.

## Reproducibility

Run `python3 artifacts/verify.py` (stdlib only, seconds). It regenerates S8,
recomputes the 256-signing disc scan, the 255-subset hereditary scan, all
12869 exact determinants, writes `subset_table.csv` / `spectrum.json`, and
checks every claimed value, printing `VERIFY_OK` on success.

## References

- J. Matousek, "The determinant bound for discrepancy is almost tight",
  arXiv:1101.0767 (2011). https://arxiv.org/abs/1101.0767
- H. Jiang and V. Reis, "A Tighter Relation Between Hereditary Discrepancy
  and Determinant Lower Bound", arXiv:2108.07945 (2021).
  https://arxiv.org/abs/2108.07945
- R. Li and A. Nikolov, "On the Gap between Hereditary Discrepancy and the
  Determinant Lower Bound", arXiv:2303.08167 (2023).
  https://arxiv.org/abs/2303.08167
- S. Lovett and R. Meka, "Constructive Discrepancy Minimization by Walking
  on The Edges", arXiv:1203.5747 (2012). https://arxiv.org/abs/1203.5747
