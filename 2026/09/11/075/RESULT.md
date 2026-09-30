# Order-10 orthogonal pair with an order-3 autotopism of profile 3+3+3+1 on all four coordinates

## Result

There exists an orthogonal pair of Latin squares of order 10 admitting a joint autotopism of order 3 whose action on rows, columns, and each symbol set has cycle profile 3+3+3+1.

Let `SIG = [1,2,0,4,5,3,7,8,6,9]`, i.e. σ=(0 1 2)(3 4 5)(6 7 8)(9). A witness is:

A =
```
1 4 3 7 9 2 8 0 6 5
4 2 5 0 8 9 7 6 1 3
3 5 0 9 1 6 2 8 7 4
5 6 1 8 7 4 9 3 0 2
2 3 7 5 6 8 1 9 4 0
8 0 4 6 3 7 5 2 9 1
0 8 9 3 2 1 4 7 5 6
9 1 6 2 4 0 3 5 8 7
7 9 2 1 0 5 6 4 3 8
6 7 8 4 5 3 0 1 2 9
```

B =
```
8 1 6 0 7 9 2 3 5 4
7 6 2 9 1 8 3 0 4 5
0 8 7 6 9 2 5 4 1 3
9 7 3 8 5 4 0 2 6 1
4 9 8 5 6 3 7 1 0 2
6 5 9 4 3 7 1 8 2 0
1 0 4 7 2 5 6 9 3 8
5 2 1 3 8 0 4 7 9 6
2 3 0 1 4 6 9 5 8 7
3 4 5 2 0 1 8 6 7 9
```

## Deterministic verification

Direct checking of the matrices gives: every row and column is a permutation of 0,...,9; σ has order 3 and orbit lengths 3,3,3,1; `G[SIG[r]][SIG[c]]=SIG[G[r][c]]` at every cell for both squares; and all 100 superimposed ordered pairs are distinct. Hence the pair is Latin, orthogonal, and jointly σ-equivariant. The fixed cell is (9,9), with value 9 in both squares.

The 2026-09-29 independent audit recomputed all four checks directly from the printed matrices.

## Scope and limitations

This is an existence result. It does not classify all order-10 pairs with this profile, determine the full autotopism group, prove uniqueness, or establish exhaustive historical priority. The earlier adjective “semiregular” is removed because the action has a fixed point. Missing verifier artifacts are no longer referenced because the matrices are self-contained.

## Context and references

Egan–Wanless is exhaustive only through order 9. Gill–Wanless studies order-10 pairs under a different non-trivial-relation condition. A targeted audit search found no source stating this exact witness/profile; search non-detection is not proof of priority.

- J. Egan, I. M. Wanless, “Enumeration of MOLS of small order,” arXiv:1406.3681.
- M. J. Gill, I. M. Wanless, “Pairs of MOLS of order ten satisfying non-trivial relations,” arXiv:2204.10996.
