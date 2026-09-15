# Elliott Classification of Crossed Products of Tracial-Rank-One Algebras by Compact-Group Actions with the Weak Tracial Rokhlin Property with Comparison

## Context

Let `A` be unital, separable, simple, infinite-dimensional, nuclear with tracial rank `TR(A) <= 1` and satisfying the Universal Coefficient Theorem (UCT). Let `G` be second-countable compact and `alpha: G -> Aut(A)` an action with the weak tracial Rokhlin property with comparison in the sense of Fang-Tian Definition 3.4. The target asks (a) whether `TR(A rtimes_alpha G) <= 1` exactly, and separately (b) whether `gTR((A rtimes_alpha G) tensor Q) <= 1` rationally, and in either affirmative case whether the Elliott invariant classifies such crossed products.

## Definitions

- `TR <= 1`: Lin's tracial topological rank at most one (approximation by 1-dimensional noncommutative CW building blocks up to small tracial remainder).
- Weak tracial Rokhlin property with comparison (Fang-Tian): for every finite `F subset A`, finite `S subset C(G)`, `eps > 0`, `x in A_+` norm one, `y in (A^alpha)_+ \ {0}`, there are invariant contraction `d in A^alpha` and contractive completely positive order-zero `psi: C(G) -> dAd` with `psi(1) = d`, approximately central equivariant behavior, Cuntz comparisons `(1-d-eps)_+ precsim_A x`, `precsim_{A^alpha} y`, `precsim_{A^alpha} d`, and largeness `||dxd|| > 1-eps`.
- `gTR`: generalized tracial rank; `Q`: universal UHF algebra; `Ell(.) = (K0, K0+, [1], K1, T, rho)`.

## Result

Put `C = A rtimes_alpha G`. Then `C` is unital, separable, simple, nuclear, satisfies the UCT, has rational generalized tracial rank at most one:

```
gTR(C tensor Q) <= 1,
```

hence is Elliott-classifiable: for any two admissible data `(A,alpha,G)`, `(B,beta,H)`,

```
Ell(A rtimes_alpha G) ~= Ell(B rtimes_beta H)  ==>  A rtimes_alpha G ~= B rtimes_beta H.
```

The exact permanence `TR(C) <= 1` (part (a)) is explicitly left open and is not claimed.

## Proof / Evidence

1. `A` is Z-stable: `TR(A) <= 1` implies finite nuclear dimension (Lin's structure plus Winter), and finite nuclear dimension implies Z-stability for simple unital separable nuclear non-elementary algebras (Winter 2012; Castillejos-Evington-Tikuisis-White-Winter).
2. Z-stability transfers: Fang-Tian Theorem 5.9 transfers tracial Z-stability to `A^alpha` via the averaging/local-approximation machine (Theorem 3.16); amenability upgrades to Z-stability (Hirshberg-Winter), and stable isomorphism `A^alpha ~_stable A rtimes G` (Theorems 4.1/4.5/4.7-4.9, Toms-Winter) gives Z-stability of `C` (Theorem 5.11). Simplicity, unitality, separability are from the same theorems.
3. Nuclearity passes for compact-group crossed products (Rosenberg / Takesaki-Takai corner picture); UCT passes because the Rosenberg-Schochet bootstrap class is preserved under crossed products by second-countable amenable (hence compact) groups (Baum-Connes with coefficients / Tu).
4. Z-stable separable simple unital nuclear `C` has finite nuclear dimension (CETWW); finite nuclear dimension plus UCT gives `gTR(C tensor Q) <= 1` (Elliott-Niu / Elliott-Gong-Lin-Niu).
5. Gong-Lin-Niu classify unital finite simple separable amenable Z-stable algebras of rational generalized tracial rank one by `Ell`; the stably-finite case covers `C` (TR1 base excludes the purely infinite branch; pure-infiniteness transfer is separately recorded). Hence isomorphic invariants imply isomorphic crossed products.

## Limitations

- Exact `TR(A rtimes_alpha G) <= 1` is not proved; Fang-Tian prove radius-of-comparison and comparison-property permanence instead.
- The argument depends on cited regularity theorems (Lin-Winter, Winter/CETWW, Tu/UCT permanence, Elliott-Niu, Gong-Lin-Niu) whose proofs are not reproduced.
- Requires the full Definition 3.4 including comparison conditions; the naive variant without them does not give saturation/stable isomorphism in general.
- Infinite-dimensionality excludes the elementary matrix case.

## Reproducibility

Verify Fang-Tian arXiv:2508.06844 Definition 3.4 and Theorems 4.1/4.5/4.7/4.8/4.9/5.9/5.11; check Lin-Winter TR1-to-finite-dimension, Winter/CETWW finite-dimension-to-Z-stable and converse, Tu/amenable UCT permanence, Elliott-Niu rational gTR1, Gong-Lin-Niu arXiv:1909.13382 classification; compose as above.

## References

- X. Fang, H. Tian, Crossed products by compact group actions with the weak tracial Rokhlin property, arXiv:2508.06844 (2026).
- J. Mohammadkarimi, N. C. Phillips, Compact group actions with the tracial Rokhlin property, arXiv:2110.12135 (2021).
- H. Tian, X. Fang, Permanence properties, Rocky Mountain J. Math. 55 (2025).
- G. A. Elliott, Z. Niu; Elliott-Gong-Lin-Niu, rational gTR1 from finite decomposition rank + UCT (2015/2024).
- G. Gong, H. Lin, Z. Niu, Classification II: rational generalized tracial rank one, arXiv:1909.13382 (2019).
- H. Lin, classification of amenable C*-algebras; tracial topological rank one.
- Castillejos-Evington-Tikuisis-White-Winter, nuclear dimension of simple Z-stable algebras (2021); Winter (2012).
- J.-L. Tu, Baum-Connes for amenable foliations/groupoids (1999); Rosenberg nuclearity/bootstrap results.
