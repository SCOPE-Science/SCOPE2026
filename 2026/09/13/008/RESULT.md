# Zero vs nilpotent-cone Springer intersection in [sl3*/SL3]

## Context

Let `g = sl3(C)`, `G = SL3(C)`, and `X = [g*/G]` with the PTVV 1-shifted
symplectic form induced by the invariant trace pairing `<A,B> = tr(AB)`.
Two Lagrangians (in the shifted sense) are compared at the stacky point 0:
the zero orbit `L0 = [pt/G]` and the nilpotent cone `L1 = [N/G]`, where
`N = V(tr X^2, det X)` in `g*`. The Lagrangian structure on `L1` relevant
to Springer theory is via the resolution
`S = [T*(G/B)/G] -> X` (Safford / Routis–Trauber Lagrangian correspondence),
which meets `L0` non-emptily over 0. The target is the fibre product
`W = L0 x_X L1`: its fibre-product cdga, tangent cohomology at 0, virtual
dimension, and a Springer-fibre intersection weight corrected by derived
excess. Scope is type-A adjoint quotients with Springer Lagrangian.

## Definitions

- `f2 = tr X^2` (degree 2), `f3 = det X` (degree 3); `N = V(f2, f3)`.
- Koszul cdga `K = Sym(g)[u2, u3]`, `|ui| = -1`, `d ui = fi`.
- `A_W` = base-change of `K` along augmentation `Sym(g) -> C` at 0.
- `B_0 = mu^{-1}(0) = G/B = Fl3`, full flag variety of `SL3`.
- `vd` = virtual dimension = alternating sum `(-1)^i dim H^i`.
- `w` = intersection weight `chi(B_0)` corrected by derived excess
  Euler-log `log(mult_0(N)/chi(B_0))`.

## Result

For `g = sl3(C)`, `G = SL3(C)`, `X = [g*/G]`, `L0 = [pt/G]`,
`L1 = [N/G]`, `W = L0 x_X L1` at 0:

- (cdga) `A_W = Lambda_C[u2, u3]`, `|u2| = |u3| = -1`, `d = 0`, trivial
  `G`-action; `W = [Spec A_W / G]`; classical truncation `BG`,
  `H^0 = C`, `H^{-1} = C^2`, `H^{-2} = C`.
- (tangent) `H^{-1}(T_W|_0) ~= sl3` (dim 8), `H^0(T_W|_0) = 0`,
  `H^1(T_W|_0) ~= C^2` (dim 2); virtual dimension `vd(W) = -10`.
- (weight) `chi(B_0) = chi(Fl3) = 6`; `mult_0(N) = 6`; derived excess
  Euler-log correction `log(6/6) = 0`; intersection weight `w = 6`.

Auxiliary resolved model `W_res = L0 x_X S` at `(eB, 0)` has
`H^{-1} = b` (dim 5), `H^0 = g/b` (dim 3), `H^1 = b*` (dim 5),
`vd = -7`, classical truncation `[Fl3/G] ~= BB`; it certifies the
Lagrangian correspondence fiberwise and contrasts with the naive
model `W` (classical truncation `BG` with `(8,0,2)` excess).

## Proof / evidence

1. Nondegeneracy: in basis `E12,E21,E13,E31,E23,E32,H1,H2` the trace Gram
   matrix is block-diagonal with pair blocks of det 1 and Cartan block
   `[[2,-1],[-1,2]]` of det 3; total det `-3 != 0`. Hence the 1-shifted
   2-form is nondegenerate at 0, and `f2` is a rank-8 nondegenerate
   quadratic form.
2. Regular sequence: `Sym(g)` is a domain and `f2 != 0`
   (`f2(diag(1,-1,0)) = 2`), so `f2` is a non-zerodivisor. `f2` is
   irreducible (a rank >= 3 nondegenerate quadric cannot factor), so
   `Sym(g)/(f2)` is a domain. With `w = -1/2 + i sqrt(3)/2`,
   `X0 = diag(1, w, w^2)` satisfies `tr = 0`, `f2 = 0`, `det = 1`, so
   `f3` is nonzero on `V(f2)`. Hence `(f2, f3)` is regular and
   `K -> O_N` resolves; base-change sends `fi |-> 0` giving
   `A_W = Lambda[u2,u3]`, `d = 0`, with trivial `G`-action since the
   `fi` are invariant. Zariski tangent `T_0 N = g*` (both differentials
   vanish): excess rank 2 over expected dim 6.
3. Tangent LES: `T_L0|_0 = g[1]`; `T_X|_0 = g[1] (+) g*`;
   `T_L1|_0 = g[1] (+) [g* -> C^2]` with vanishing differential at the
   vertex. Both maps to `T_X` are isomorphisms on `H^{-1}` and `H^0`.
   For `T_W = fib(T_L0 (+) T_L1 -> T_X)`: `H^{-1} = diag(g)` (dim 8),
   `H^0 = 0`, `H^1 = C^2` (dim 2). Thus `vd = -8 + 0 - 2 = -10`,
   independently `vd(L0)+vd(L1)-vd(X) = (-8)+(6-8)-0 = -10`.
   Fiberwise certificate for `S` at `(eB,0)` (stabilizer `B`,
   `V = (g/b) (+) n`, `d mu(v,eta) = eta`, `ker = g/b` dim 3,
   `coker = b*` dim 5) gives relative ranks `(0,6,5)` matching
   cotangent ranks `(0,6,5)`, i.e. the Safford/Routis–Trauber equivalence
   at the support point.
4. Euler and multiplicity: `P(Fl3) = (1+t^2)(1+t^2+t^4)`, so
   `chi = P(1) = 6`; confirmed by 6 Bruhat cells of `S3` (lengths
   `0,1,1,2,2,3`), `chi(P2) chi(P1) = 3*2`, and
   `|Fl3(Fq)| = (1+q)(1+q+q^2) -> 6`. `N` is a homogeneous complete
   intersection of type `(2,3)` with regular sequence, so by Bezout
   `mult_0(N) = 2*3 = 6`. Correction `log(6/6) = 0`; hence `w = 6`.

## Limitations

Global Safford/Routis–Trauber Lagrangian correspondence structure of `S`
is cited and certified fiberwise at the support point `(eB, 0)` only.
All rank and dimension counts are over `C` at the stacky point 0; they do
not cover other Springer fibres or non-principal orbits. The weight `w`
uses the target-defined excess Euler-log correction.

## Reproducibility

Scripts (copied to `output/artifacts/`):
`trace_gram.py` (Gram det `-3`), `excess_vdim.py` (witnesses, mult, vd),
`flag_euler.py` (Poincare/Bruhat/Fq Euler), `tangent_les.py` (naive and
resolved LES bookkeeping). Run with `python3 <script>`; each asserts the
claimed integers. Proofs above are self-contained given standard facts
(PTVV, Kostant regular sequence, Bezout, Bruhat decomposition).

## References

- Pantev–Toen–Vaquie–Vezzosi shifted symplectic geometry; Joyce exposition.
- Safronov, Poisson reduction and `g*/G` Lagrangian intersections
  (Higher Structures 1(1), 2017); Safford / Routis–Trauber Springer
  Lagrangian correspondence (cited for global structure).
- Kostant theorem on invariant polynomials / complete intersection
  nilpotent cone (cf. MIT 18.757 Lec17); Rider derived Springer correspondence.
- Standard flag-variety topology: Poincare polynomial, Bruhat cells,
  `|Fl3(Fq)| = (1+q)(1+q+q^2)`.
