# Universal reciprocal symmetry of the odd-OSASM r=1 slice is false: minimal counterexample at order 5

## Context

Refined enumeration of alternating sign matrices under symmetry is a classical enumerative-combinatorics problem. Behrend–Fischer–Koutschan obtain refined DSASM/OSASM generating functions, and Kumari proves the odd-order unrefined product together with an algebraic symmetry result for even-order OSASMs. The natural question considered here is whether the odd-order `r=1` slice has an analogous reciprocal symmetry in `t`.

## Definitions

- A DSASM is a symmetric alternating sign matrix.
- An OSASM is a DSASM with zero nonzero diagonal entries in even order and exactly one nonzero diagonal entry in odd order.
- `T(A)` is the column of the unique `1` in the first row.
- `X^O_n(r,t) = sum_A r^{R(A)} t^{T(A)}` over OSASMs of order `n`.
- For the odd `r=1` slice write `P_n(t)=X^O_{2n+1}(1,t)`.
- Call a nonzero Laurent polynomial `P(t)` **reciprocal up to monomial shift** if there is an integer `m` such that `P(t)=t^m P(1/t)`. If the support of `P` has smallest and largest exponents `a` and `b`, any such shift is forced to be `m=a+b`. This is the normalization compatible with the known even-order identity `X^O_{2n}(r,t)=t^{2n+2}X^O_{2n}(r,1/t)`.

Kumari's odd-order product gives `P_n(1)=|OSASM(2n+1)|`.

## Result

**Theorem.** The universal claim that every `P_n(t)=X^O_{2n+1}(1,t)` is reciprocal up to a monomial shift is false. The smallest tested odd order already separating the phenomenon is order 5 (`n=2`):

`P_2(t)=3t+7t^2+9t^3+9t^4+4t^5`.

Its support is `{1,2,3,4,5}`, so a reciprocal shift, if one existed, would have to be `m=1+5=6`. But reciprocity with shift 6 would require the coefficients of `t` and `t^5` to agree, whereas they are `3` and `4`; it would also require the coefficients of `t^2` and `t^4` to agree, whereas they are `7` and `9`. Hence no monomial shift makes `P_2` reciprocal. The unrefined check is consistent with Kumari's product: `P_2(1)=32`.

By contrast, order 3 (`n=1`) gives

`P_1(t)=t+2t^2+t^3`,

and `P_1(t)=t^4 P_1(1/t)`. Thus `n=2` is the first counterexample after the `n=1` case.

## Proof / evidence

The accompanying exhaustive certificate `output/artifacts/verify_osasm.py` enumerates all ASMs through order 5 by valid-row backtracking, filters to DSASMs by transpose symmetry and then to OSASMs by the diagonal condition. It reproduces the standard counts

- ASM: `1,2,7,42,429`,
- DSASM: `1,2,5,16,67`,
- OSASM: `1,1,4,3,32`,

and the refined `T`-distributions

- order 3: `{1:1,2:2,3:1}`,
- order 4: `{2:1,3:1,4:1}`,
- order 5: `{1:3,2:7,3:9,4:9,5:4}`.

The order-3 and order-4 rows agree with the published low-order refined data, and the order-5 total `32` agrees with the odd-order product. The script then checks reciprocal shifts directly and reports that order 3 has shift 4 while order 5 has none. An independent reimplementation of the enumeration during this audit reproduced the same counts and distributions.

## Limitations

- Exhaustive enumeration is only needed through order 5 for the disproof and makes no claim about a repaired identity for larger odd orders.
- The contribution is the exact counterexample and its validated refined row; the enumeration algorithm itself is standard.

## Reproducibility

Run `python3 output/artifacts/verify_osasm.py` with Python 3 standard library only.

## References

- Roger E. Behrend, Ilse Fischer, Christoph Koutschan, *Diagonally symmetric alternating sign matrices*, arXiv:2309.08446.
- Nishu Kumari, *Off-diagonally symmetric alternating sign matrices*, arXiv:2503.18685.
- Greg Kuperberg, *Symmetry classes of alternating-sign matrices under one roof*, arXiv:math/0008184.
