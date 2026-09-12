# Empty tilt wall at beta = -1/2 for the line-ideal projection class on a Brill-Noether-general ordinary Gushel-Mukai threefold

## Context

General ordinary Gushel-Mukai (GM) threefolds are studied through their Fano
schemes of lines, Brill-Noether reconstruction as Brill-Noether loci in
Bridgeland moduli spaces of Kuznetsov-component objects, and categorical
Torelli recovery from Kuznetsov data plus tautological information. Those
programs assume stability inputs for line-geometry objects. The tilt wall
controlling stability of line-ideal projections at a standard tilt parameter
was an explicit missing link between Fano-line geometry and Bridgeland moduli.

## Definitions

- Let `X` be a Brill-Noether-general ordinary GM threefold over an
  algebraically closed field of characteristic zero: smooth prime Fano
  threefold of index 1, genus `g = 6`, `Pic(X) = Z H`, `-K_X = H`,
  `H^3 = 10`, with `D^b(X) = < Ku(X), E, O_X >` where `E` is the rank-2
  tautological subbundle pullback with `ch(E) = (2, -H, L, P/3)` (`L` = line
  class, `P` = point class).
- Let `L` be a line in `X` and `I_L` its ideal sheaf, with
  `ch(I_L) = (1, 0, -L, -P/2)`.
- Let `pr = L_E o L_O : D^b(X) -> Ku(X)` be the left-adjoint projection to
  the Kuznetsov component, and `v2 = [pr(I_L)]`.
- Truncated Chern lift: `ch_{<=2} = (m0, m1 H, m2 L)` with
  `L = H^2/H^3 = H^2/10`, so vectors are written `(m0, m1, m2)`.
- Tilt stability `sigma_{alpha,beta}` is the standard threefold tilt
  construction with `Im Z_{alpha,beta} = H^2 . ch_1^beta`
  `= H^3 (n1 - beta n0)` on a truncated class `(n0, n1, n2)`.
- The numerical Kuznetsov lattice at `g = 6` is `N(Ku(X)) = < v, w >` with
  Euler Gram `[[-2,-3],[-3,-5]]`; a class `u` is a `(-r)`-class if
  `chi(u,u) = -r`.

## Result

**Theorem (empty wall W2).** The class `v2 = [pr(I_L)]` has truncated Chern
lift `M = (-3, 2, -3)`, is primitive, and is a `(-2)`-class. At tilt
parameter `beta = -1/2`, there is no numerical tilt wall for this lift: for
every `alpha > 0` there is no strictly `sigma_{alpha,-1/2}`-semistable object
of that truncated class. Every such tilt-semistable object is tilt-stable,
and the sharp-destabilizer alternative does not occur. Conditionally on the
standard double-tilt induction (which applies verbatim since no wall is
crossed), such an object descends to a Serre-invariant Bridgeland-stable
object of `Ku(X)`.

## Proof / evidence

Hirzebruch-Riemann-Roch on `X` with `td_1 = H/2`, `td_2 = 17L/6`,
`td_3 = P` gives `chi(O_X, I_L) = chi(O_X) - chi(O_L) = 1 - 1 = 0` and

    chi(E, I_L) = P_3 + P_2.td_1 + P_1.td_2 + P_0.td_3
                = -7/3 - 1/2 + 17/6 + 2 = 2,

cross-checked via the dual bundle: `ch(E^vee) = (2, H, L, -P/3)` gives
`chi(E^vee) = 1 + 3/2 + 17/6 - 1/3 = 5`, restriction
`chi(E^vee|_L) = 2 + 1 = 3`, so `chi(E, I_L) = 5 - 3 = 2`.
Since `chi(O_X, I_L) = 0`, the `O_X`-correction vanishes and

    [pr(I_L)] = [I_L] - chi(E, I_L)[E] = [I_L] - 2[E],

hence `[pr(I_L)]_{<=2} = (1,0,-1) - 2(2,-1,1) = (-3, 2, -3)`.
Consequences: `gcd(3,2) = 1` (primitive); with `u = -3v + 2w`,
`chi(u,u) = -2` under the genus-6 Gram; discriminant
`Delta(M) = (10*2)^2 - 2(10*(-3))(-3) = 400 - 180 = 220 >= 0`.
The conic-ideal projection `-v + w = (-1, 1, -2)` is a `(-1)`-class with
`Delta = 60`, disjoint from the line class.

At `beta = -1/2`, `Im(E) = 10 n1 + 5 n0` lies in `5Z` for every object, while
`Im(M) = 10*2 + 5*(-3) = 5`. A numerical wall meeting `beta = -1/2` would
need `M = [E] + [F]` in `Coh^{-1/2}(X)` with `Im(E), Im(F) > 0` and slope
equality for some `alpha > 0`. But `Im(E) + Im(F) = 5` with each summand a
positive multiple of 5 is impossible, so one factor has `Im = 0` (slope
`+infinity`) while `M` has finite slope: equality is impossible. Thus no
numerical tilt wall exists on `beta = -1/2, alpha > 0`, no strictly
semistable object occurs there, and no destabilizing sequence with slope
equality exists. A brute-force search over `|ni| <= 30` confirms zero
both-`Im`-positive Bogomolov-Gieseker-compatible candidates.
Replay: `python3 output/artifacts/verify_target.py` prints `VERIFY_OK`.

## Limitations

Brill-Noether generality is assumed for the geometric setup (smooth line,
ordinary GM projection formula, nonzero primitive Kuznetsov class); the
quantization exclusion itself is uniform over ordinary GM threefolds. The
Bridgeland-stability transfer is stated via the standard double-tilt
induction rather than re-proved. No claim is made for special GM
threefolds, singular threefolds, or other beta values.

## Reproducibility

Run `python3 output/artifacts/verify_target.py` (stdlib only). It checks
both HRR Euler characteristics, the projection identity, primitivity,
`Delta(M) = 220`, the `(-2)`-class pairing, `Im(M) = 5`, the empty
both-`Im`-positive BG-compatible candidate list in the stated box, formal W2
samples (all with quotient `Im = 0`, hence not walls), and line/conic
separation.

## References

- Augustinas Jacovskis, Zhiyu Liu, Shizhuo Zhang, Brill-Noether
  reconstruction of index one prime Fano threefolds, arXiv:2207.01021v2.
- Jacovskis-Lin-Liu-Zhang, Categorical Torelli theorems for Gushel-Mukai
  threefolds, arXiv:2108.02946.
- Olivier Debarre, Alexander Kuznetsov, Gushel-Mukai varieties:
  classification and birationalities, arXiv:1510.05448.
- Alexander Perry, Laura Pertusi, Xiaolei Zhao, Stability conditions and
  moduli spaces for Kuznetsov components of Gushel-Mukai varieties,
  Geom. Topol. 26 (2022), 3055-3121.
