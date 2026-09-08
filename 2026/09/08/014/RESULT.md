# Cup-trivial but Massey-nonformal balanced presentation 2-complex

## Context

Cup products do not detect all higher multiplicative structure: triple
Massey products obstruct formality even when the cohomology ring is
trivial (Massey, Kraines, Sullivan, Deligne–Griffiths–Morgan–Sullivan).
The question audited here is where Massey non-formality first appears
among finite 2-complexes when all cups vanish. Link complements and lens
spaces carry boundary-torus/peripheral or torsion mechanisms; moment-angle
complexes live in high dimensions. The witness below is a closed balanced
(deficiency-zero) 2-dimensional presentation complex.

## Definitions

Let `K` be the presentation 2-complex of

```text
G = < x, y, z | r1, r2, r3 >
r1 = x^2 [y,z]^2   (word length 10)
r2 = [x,z]         (word length 4)
r3 = [[x,y],z]     (word length 10)
```

Explicit words (capitals = inverses):

```text
r1 = x x y z Y Z y z Y Z
r2 = x z X Z
r3 = x y X Y z y x Y X Z
```

`K` has one 0-cell, three 1-cells, three 2-cells: finite, closed,
balanced. Cellular chains: `C2 = Z^3 -> C1 = Z^3 -> C0 = Z`.
Cohomology cups `H^1 x H^1 -> H^2` are computed by the cellular/Fox
formula `C(u,v)_k = sum_{i,j} u_i v_j A^{(k)}_{ij}` where
`A^{(k)}_{ij}` is the augmentation of the second Fox derivative of
`r_k`. A triple Massey product `<a,b,c>` is defined when `a∪b = 0` and
`b∪c = 0` in cohomology; with bounding 1-cochains `ds = a∪b`,
`dt = b∪c`, the representative is `m = s∪c − a∪t`, well defined modulo
the indeterminacy ideal `a·H* + H*·c` plus coboundaries.

## Result

For `K` above:

1. `H1(K;Z) ≅ Z/2 ⊕ Z^2` (torsion from `x^2` in `r1`), `H2(K;Z) ≅ Z^2`,
   `H^1(K;Z) ≅ Z^2 = span{Y, Z}` dual to `[y],[z]`,
   `H^2(K;Z) ≅ Z/2 ⊕ Z^2`.
2. Every cup product of positive-degree integral cohomology classes on
   `K` is zero in cohomology; `H*(K;Z)` is the trivial extension.
3. The triple Massey product `<Y,Z,Z>` is strictly defined and
   `<Y,Z,Z> = (0,1,0) + I ≠ 0` in `H^2(K;Z)/I`, where
   `I = Y·H^1 + H^1·Z + B^2` is the full indeterminacy ideal.
   `<Z,Z,Y> = (0,−1,0) + I ≠ 0`; the other six triples on `{Y,Z}`
   vanish mod indeterminacy.
4. Hence `K` is non-formal and not (rationally) formal-homotopy
   equivalent to any formal complex with the same cohomology ring
   (e.g. a wedge of circles and spheres).

## Proof / evidence

Exponent matrix (Fox first derivatives augmented) is

```text
E = [[2,0,0],[0,0,0],[0,0,0]], SNF(E) = diag(2,0,0),
```

so `d^1 = E^T: C^1 -> C^2`, `δ(s1,s2,s3) = (2s1,0,0)`,
`B^2 = {(2k,0,0)}`; a class is null-cohomologous iff `c2 = c3 = 0`
and `c1` even. Homology claims follow.

Augmented second Fox matrices (independently recomputed by naive
group-ring Fox rules and two in-script recursions):

```text
A1 = [[1,0,0],[0,0,2],[0,-2,0]]
A2 = [[0,0,1],[0,0,0],[-1,0,0]]
A3 = [[0,0,0],[0,0,0],[0,0,0]]
```

On `Y = (0,1,0)`, `Z = (0,0,1)`:

```text
Y∪Y = (0,0,0),  Y∪Z = (2,0,0) = δ(1,0,0),
Z∪Y = (−2,0,0) = δ(−1,0,0),  Z∪Z = (0,0,0).
```

Thus all `H^1 × H^1` cups vanish in cohomology; cups landing in
`H^{≥3} = 0` vanish for degree reasons. Controls: `[x,y]` gives the
standard torus values `+1/−1`; the all-commutator complex gives
nonzero cups (correctly rejected).

Massey: with `s = (1,0,0)` (`δs = Y∪Z`) and `t = (0,0,0)`
(`δt = Z∪Z`), `m = s∪Z − Y∪t = (0,1,0)` since `C(s,Z)` picks
`A2_13 = 1` and `C(Y,t) = 0`. Indeterminacy generators
`B^2 ∪ {C(Y,h), C(h,Z)}` are `(2,0,0)` or `(0,0,0)` only: every
element of `I` has middle coordinate 0 while `m` has middle
coordinate 1. Middle-coordinate projection is an exact quotient
homomorphism killing `I` and sending `m` to 1, so `m ∉ I` with
infinite order. Any other bounding choice changes `m` by an element
of `I`, so the class is well defined and nonzero. Exact
integer-linear solver confirms non-membership; bounding-choice
robustness checked.

## Limitations

- Integral Massey non-vanishing proved; rational non-formality
  follows (cups vanish rationally, `m` has infinite order) but no
  minimal-model computation is included.
- No general 2-generator vanishing lemma is claimed; sharpness is
  only the minimal generator count for a triple product in `H^1`.
- The cup formula is the standard cellular/Fox second-derivative
  formula validated by the torus control, not re-derived from a
  simplicial diagonal in-script.

## Reproducibility

Stdlib-only script replays homology, cup vanishing, Massey defining
system, indeterminacy non-membership, full 8-triple table, controls,
and rewrites `results.json`:

```text
cd output/artifacts && python3 verify.py
```

Artifacts: `verify.py`, `results.json`.

## References

- Hatcher, Algebraic Topology, Ch. 3 (cup product; torus-vs-wedge
  separator). https://pi.math.cornell.edu/~hatcher/AT/ATpage.html
- Poirier–Tradler–Wilson, Massey products for homotopy inner
  products, arXiv:2507.15494. https://arxiv.org/abs/2507.15494
- Lee–Park–Park–Yim, An algorithm for a Massey triple product of a
  smooth projective plane curve, arXiv:1909.06714.
  https://arxiv.org/abs/1909.06714
- Limonchenko–Panov, Minimally non-Golod face rings and Massey
  products, arXiv:2201.12779. https://arxiv.org/abs/2201.12779
- Grbić–Linton, Non-trivial higher Massey products in moment-angle
  complexes, arXiv:1911.07083. https://arxiv.org/abs/1911.07083
