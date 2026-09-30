# Exact normalized census of C5-equivariant Latin squares of order 10

## Result

Let σ=(0 1 2 3 4)(5 6 7 8 9), require `L[σ(r)][σ(c)] = σ(L[r][c])`, and normalize one distinguished orbit value by `X[(0,0,0)] = 0`.

There are exactly **2,082,000** normalized σ-equivariant Latin squares of order 10. By transitivity of the centralizer of σ on the ten symbols, the unnormalized count is **20,820,000**.

The earlier 65-specimen orthogonal-mate obstruction is not retained because its cited specimen/search artifacts are absent from the current package and could not be independently audited.

## Orbit model and exact enumeration

The diagonal action on `(r,c)` has 20 cell orbits of size 5. Put `er=floor(r/5)`, `ec=floor(c/5)`, and `d=(c mod 5-r mod 5) mod 5`. If an orbit value is `v=5*s+b`, equivariance forces the symbol in row residue `q=r mod 5` to be `5*s+(b+q mod 5)`. Thus 20 orbit variables determine the array and Latinness becomes finite all-different constraints.

The 2026-09-29 audit independently reconstructed this model and exhaustively counted the normalized solutions. Exactly **29,420** first-row-group assignments survive internal column constraints. Their compatible second-row-group counts have histogram:

| completions | states |
|---:|---:|
| 45 | 1,125 |
| 55 | 2,750 |
| 65 | 7,500 |
| 70 | 7,000 |
| 75 | 6,500 |
| 90 | 4,500 |
| 225 | 45 |

The state counts sum to 29,420 and the weighted sum is exactly **2,082,000**. Centralizer transitivity makes the count equal for each of the ten possible distinguished-orbit values, giving the unnormalized factor 10.

## Scope and limitations

This is only the exact census for the stated diagonal fixed-point-free C5 action. It does not classify isotopy classes, count orthogonal pairs, or decide a C5-equivariant 3-MOLS(10). A targeted search found no earlier statement of the number 2,082,000 for this stratum; search non-detection is not proof of priority.

## References

- J. Egan, I. M. Wanless, “Enumeration of MOLS of small order,” arXiv:1406.3681.
- M. J. Gill, I. M. Wanless, “Pairs of MOLS of order ten satisfying non-trivial relations,” arXiv:2204.10996.
