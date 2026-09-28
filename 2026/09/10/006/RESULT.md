# Certified equinumeration of left Gog and GOGAm trapezoids at (n,k) = (6,3)

## Context

The Gog–Magog (alternating-sign-matrix vs totally-symmetric-self-complementary-plane-partition) bijection remains a central open problem. Biane–Cheballah introduced left Gog and GOGAm trapezoids and conjectured equinumeration for all shapes, with explicit bijections for one- and two-diagonal cases. The three-diagonal regime is therefore a natural first width beyond those explicitly solved cases. Fischer's constant-term and Lindström–Gessel–Viennot (LGV) formulas provide an independent enumerative check.

## Definitions

- A Gog triangle of order `n` is a Gelfand–Tsetlin triangle with strictly increasing rows and bottom row `1,...,n`.
- A Magog triangle of order `n` is a Gelfand–Tsetlin triangle with diagonal caps `X[j][j] <= j` in the paper's one-indexed convention.
- A GOGAm triangle is the Schützenberger image of a Magog triangle; equivalently it satisfies the Biane–Cheballah inequality system used by the verifier.
- A left `(n,k)` Gog or GOGAm trapezoid consists of the `k` leftmost NW–SE diagonals. Write `G(6,3)` and `M(6,3)` for the two finite sets audited here.

## Result

For order `n=6` and width `k=3`,

`|G(6,3)| = |M(6,3)| = 4862`.

This is a finite computational theorem at one parameter pair. No all-`n` three-diagonal bijection or equinumeration theorem is claimed.

## Proof / evidence

### Leg 1: Gog exhaustion
`gen_gog(6)` generates exactly `7436` Gog triangles, the known ASM(6) count, and each generated object satisfies the Gog validator. Projection to the three leftmost diagonals gives exactly `4862` distinct trapezoids.

### Leg 2: GOGAm exhaustion
`gen_magog(6)` generates exactly `7436` Magog triangles, each satisfying the Magog validator. Applying the committed Schützenberger implementation gives `7436` images satisfying the implemented GOGAm inequality system. Their three-left-diagonal projection contains exactly `4862` distinct trapezoids. The Schützenberger implementation is also checked to be involutive on the complete order-4 Gog and Magog sets.

Nearby left-projection counts agree on both sides:
- `n=4`: `k=1,2,3` gives `14,35,42`;
- `n=5`: `42,219,387`;
- `n=6`: `132,1594,4862`.

### Leg 3: LGV determinant cross-check
The committed Fischer/LGV routine, summed over weakly increasing bottom rows, gives `4862` at `(m,n,k)=(0,6,3)`. The same routine reproduces the smaller calibration values `(3,2)=7`, `(4,2)=35`, `(4,3)=42`, `(5,2)=219`, and `(5,3)=387`.

The first two legs already establish the finite headline equality by exhaustive enumeration; the LGV computation is an independent integer cross-check.

## Limitations

- This is an exhaustive finite computation at `(6,3)`, not a bijective or analytic proof for all `n`.
- GOGAm membership is checked through the paper's inequality characterization as encoded in the committed verifier.
- The integer `4862` happens to equal Catalan `C_9`; no combinatorial identification is claimed.
- No claim is made about an unreplayed `n=7` census.

## Reproducibility

From the record's `output/` directory run:

`python3 artifacts/verify.py`

The repaired verifier uses only files actually committed in `output/artifacts/`: `gen.py`, `gogam.py`, `lgv_cert.py`, and `lgv2.py`. It checks the generator counts/validators, the complete `n=4,5,6` left-projection census, a complete `n=4` Schützenberger involution test, GOGAm inequalities, and the LGV calibration including `(0,6,3)=4862`; it prints `VERIFY_OK` on success.

The previous `verify.py` imported `sec92.py` and `relabel.py`, which are not present in the record or repository tree. Those non-headline checks have therefore been removed from the canonical verifier rather than being claimed reproducible.

## References

- P. Biane, H. Cheballah, *Inversions and the Gog-Magog problem*, arXiv:1401.6516.
- I. Fischer, *Constant term formulas for refined enumerations of Gog and Magog trapezoids*, arXiv:1804.07054.
- J. Bettinelli, *A simple explicit bijection between (n,2) Gog and Magog trapezoids*, arXiv:1512.03305.
- I. Fischer, M. Konvalinka, *A bijective proof of the ASM theorem, Part II: ASM enumeration and ASM-DPP relation*, arXiv:1912.01354.
