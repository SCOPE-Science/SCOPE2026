# Double-relative K2 of the split node over F7 is nonzero (contains Z/48)

## Context

Let F = F_7, B = F[t], and A = F[x,y]/(y^2 - x^3 - x^2) embedded in B by
x = t^2 - 1, y = t(t^2 - 1). The curve y^2 = x^3 + x^2 is the split node:
over any field with 2 != 0 it has two distinct tangents at the origin,
and over F_7 the points t = 1 and t = -1 both lie over the node. Let
J = (t^2 - 1)B and I = Ann_B(B/A) be the conductor. The admitted target
asked whether the double-relative (birelative) group K_2(A,B,I) vanishes:
either (A) prove vanishing by a Dennis-Stein ledger, or (B) exhibit a
nonzero Dennis-Stein symbol detected by a Dennis/dlog trace to HC_1.

## Definitions

- A = {f in B : f(1) = f(-1)} = F + J; J is an ideal in both A and B and
  equals the conductor I = (x,y)A.
- A/I ~= F (diagonal), B/I = F[t]/((t-1)(t+1)) ~= F x F, giving a Milnor
  (pullback) square A -> B over F -> F x F.
- K_2(A,B,I) is the birelative group: the homotopy fibre of
  K(A,I) -> K(B,I), fitting into ... -> K_3(B)+K_3(A/I) -> K_3(B/I)
  -> K_2(A,B,I) -> K_2(A) -> ... (Geller-Weibel/Laubenbacher/Weibel
  Milnor-square Mayer-Vietoris sequence).
- Quillen: K_{2i-1}(F_q) ~= Z/(q^i - 1), K_{2i} = 0; hence K_3(F_7) ~=
  Z/48, K_2(F_7) = 0, K_1(F_7) ~= Z/6. Homotopy invariance gives
  K_*(F[t]) ~= K_*(F).

## Result

K_2(A,B,I) != 0 for this named nodal inclusion over F_7. In fact it
contains a subgroup isomorphic to Z/48, namely the image of the
Mayer-Vietoris boundary. Hence vanishing option (A) is false, and the
nonvanishing side of the target decision holds.

In addition, the literal method of option (B) as worded is impossible:
u = t-1, v = t+1 do not lie in A, 1+uv = t^2 is not a unit of B so
<u,v> is not a Dennis-Stein symbol in A or B, and in fact no nonzero
symbol <t-1,v> exists in B; moreover any Dennis/dlog trace to a
characteristic-7 HC_1/Hochschild target is an F_7-vector space
(7-torsion) while the detected class is 48-torsion with gcd(48,7) = 1,
so every such trace vanishes on it. The nonvanishing certificate is
therefore the Mayer-Vietoris boundary class, not a Dennis trace, and
this substitution is proved necessary.

## Proof / evidence

1. Conductor square: t^2 - 1 vanishes at t = +-1 (2 != 0 in F_7 so the
   factors are comaximal), so every multiple lies in
   A' = {f : f(1) = f(-1)}; conversely x, y generate A inside A' and
   f - f(1) vanishing at +-1 is divisible by (t-1)(t+1), giving
   A = A' = F + J. Any B-ideal in A vanishes at +-1 hence lies in
   (t^2-1), so I = J. CRT gives B/I ~= F x F and A/I the diagonal F.
   Units: B^x = F^x by degree, hence A^x = F^x.
2. Smooth corners: by Quillen, K_3(B) ~= Z/48 via (c_*)^{-1} where
   c : F -> B; K_3(A/I) ~= Z/48; K_3(B/I) ~= Z/48 + Z/48. Both
   evaluations ev_{+-1} : B -> F are retractions of c, so both induce
   the same isomorphism (c_*)^{-1} : K_3(B) -> K_3(F).
3. Boundary: the MV map phi : Z/48 + Z/48 -> Z/48^2 is
   phi(u,v) = (u+v, u+v), with image the diagonal and
   coker(phi) ~= Z/48 via (x,y) -> x - y. By exactness,
   im(boundary) ~= coker(phi) ~= Z/48 injects into K_2(A,B,I) with no
   knowledge of K_2(A) needed.
4. Literal-(B) refutation and trace obstruction as stated in Result,
   using the gluing condition and gcd(48,7) = 1.
5. Reproducibility: output/artifacts/verify.py passes all finite checks
   (Quillen orders, diagonal cokernel, conductor gluing with A = F+J in
   degree <= 2 plus general identity, units degree lemma, constant
   Dennis-Stein ledger in K_2(F_7) = 0, trace obstruction, literal-pair
   refutation).

## Limitations

The headline is the nonvanishing with Z/48 subgroup via the MV boundary.
It does not compute K_2(A) itself, does not produce a Dennis-Stein symbol
or nonzero Dennis trace (proved impossible for this class), and does not
classify K_2(A,B,I) beyond the exhibited subgroup. Only the named split
node over F_7 with the stated normalization and conductor is covered.

## Reproducibility

Run `python3 output/artifacts/verify.py` (expected: ALL CHECKS PASSED).
The proof steps above are self-contained given standard references:
Quillen on K_*(F_q); Geller-Weibel/Laubenbacher/Weibel Milnor-square
birelative Mayer-Vietoris sequence; CRT and degree arguments in F_7[t].

## References

- D. Quillen, On the cohomology and K-theory of GL over a finite field.
- S. Geller, C. Weibel, K_1(A,B,I); R. Laubenbacher, Generalized
  Mayer-Vietoris sequences; C. Weibel, Mayer-Vietoris and mod-p K-theory;
  C. Weibel, The K-book (conductor/Milnor squares).
- M. Morrow, K-theory of one-dimensional rings via pro-excision
  (arXiv:1211.1533): pro-MV, conductor ideals, singular curves over
  finite fields, Geller's conjecture.
- Y. Zhang, A general Mayer-Vietoris sequence in algebraic K-theory
  (arXiv:2603.13692): Milnor-square sequence with K(A,B,I) terms.
