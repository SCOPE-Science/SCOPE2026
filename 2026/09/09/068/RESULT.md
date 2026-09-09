# Fiber-transverse cyclic obstruction in a property (T) wreath-like II_1 factor

## Context

Primeness and unique prime factorization of II_1 factors is a recognized frontier
of the Popa deformation-rigidity program. Chifan–Ioana–Osin–Sun (CIOS I,
arXiv:2111.04708) introduced wreath-like products, a class of groups arising from
Dehn filling, many with Kazhdan's property (T), and proved W\*-superrigidity:
L(G) remembers G. CIOS III (arXiv:2402.19461) classifies embeddings between
distinct wreath-like factors. Neither decides tensor splittings (primeness) of a
single fixed factor, and solid/biexact UPF theorems do not cover this (T) class.
The admitted investigation targeted primeness of L(G\*) for a fixed
WR(Z/2,B ↷ I) property-(T) factor via forcing a diffuse tensor leg into the
fiber algebra, with a pre-qualified fallback universal fiber-location lemma.
This record states the emergent obstruction found by stress-testing that route.

## Definitions

Let G\* ∈ WR(A, B ↷ I) be a wreath-like product in the CIOS sense: an extension

    1 → A^{(I)} → G\* →ε B → 1,   A^{(I)} = ⊕_{i∈I} A_i,

with w A_i w^{-1} = A_{ε(w)·i}. Take fiber A = Z/2Z (nontrivial abelian, hence
amenable), base B a nontrivial ICC subgroup of a hyperbolic group (hence B
contains an element b of infinite order), action B ↷ I with infinite orbits
(so G\* is ICC by CIOS I Lemma 4.11(b)), and G\* with property (T) (CIOS
Dehn-filling construction; cited, see Limitations). Put

    M  = L(G\*)          (II_1 factor),
    N  = L(A^{(I)}) ⊂ M  (abelian, hence amenable; τ-preserving E_N exists),
    g ∈ G\* any lift of b (ε(g) = b),  Q0 = L(⟨g⟩) ⊂ M.

Popa intertwining P ≺_M N (Popa, Invent. Math. 2006, Thm. 2.1; CIOS I §3.2):
P ≺_M N FAILS iff mixing unitaries exist; in particular a sequence
u_k ∈ U(Q0) with ‖E_N(x\* u_k y)‖_2 → 0 for all x,y ∈ M implies Q0 ⋠_M N.

## Result

**Theorem.** With G\*, M, N, Q0 as above:

  (a) Q0 ⊂ M is diffuse amenable.
  (b) Q0 ⋠_M N: Q0 does NOT intertwine into the fiber algebra in Popa's sense.
      Explicit mixing witness: u_n = u_{g^n} ∈ U(Q0), and for all x,y ∈ M,
      ‖E_N(x\* u_n y)‖_2 → 0 as |n| → ∞.

**Corollary.** (i) The universal fiber-location statement "every diffuse
amenable Q ⊂ M satisfies Q ≺_M N" is FALSE (witness Q0) — the preset fallback
lemma cannot hold as stated. (ii) The primeness strategy "force a diffuse
tensor leg into N, then conclude by type" cannot proceed through a universal
diffuse-amenable location step. Primeness of M itself remains OPEN; what is
closed is this route-segment.

The estimate uses only ker ε = A^{(I)} and infinite order of b, so it applies
verbatim to every WR group with an infinite-order base element and any
nontrivial abelian fiber (the whole CIOS infinite family).

## Proof / evidence

(a) ε(g^n) = b^n ≠ e for n ≠ 0, so g has infinite order, ⟨g⟩ ≅ Z, and
Q0 ≅ L(Z) ≅ L^∞(T) via Fourier is diffuse abelian, hence amenable.

(b) It suffices to check group unitaries and extend by contractivity of E_N
and L^2 density. For x = u_s, y = u_t (s,t ∈ G\*):

    E_N(u_s\* u_{g^n} u_t) = u_{s^{-1} g^n t} if s^{-1} g^n t ∈ A^{(I)}, else 0,

so ‖·‖_2 ∈ {0,1}, equal to 1 iff ε(s)^{-1} b^n ε(t) = e, i.e.
b^n = ε(s)ε(t)^{-1} =: b0 fixed per pair (s,t). Since n ↦ b^n is injective,
at most one n hits per pair. For finite linear combinations with supports
S,T the hitting set H satisfies |H| ≤ |S|·|T| < ∞, so E_N(x0\* u_n y0) = 0
for |n| large; extension to all x,y ∈ M follows by E_N 2-norm contractivity
(two-stage approximation). Hence (u_{g^n}) is mixing and Q0 ⋠_M N.

Replayable evidence: `output/artifacts/verify_obstruction.py` (stdlib only,
prints VERIFY_OK) certifies the combinatorial core on matrix model
B0 = SL(3,Z) ∋ b = E12: [1] 401 distinct powers |n| ≤ 200; [2] 441 (s,t)
pairs × 101 n-values with max 1 hit per pair (133 hit exactly once);
[3] (e,e) unique hit at n = 0; [4] amenability/diffuseness shadows.
The analytic dressing (Fourier, E_N contractivity, density) is the by-hand
proof above.

## Limitations

- Primeness of L(G\*) is NEITHER proved NOR refuted — remains open.
- CIOS Dehn-filling existence of property-(T) ICC G\* ∈ WR(Z/2,B ↷ I) with
  infinite-orbit action is CITED (Thm. 1.3/Thm. 2.6/Prop. 2.11 line), not
  re-proved. The obstruction needs only the extension shape plus one
  infinite-order base element.
- Popa's criterion, Fourier L(Z) ≅ L^∞(T), E_N contractivity quoted.
- No claim about stabilizer-subalgebra location
  (Q0 ≺ L(A^{(I)} ⋊ Stab) or similar); natural next attack, out of scope.

## Reproducibility

Run `python3 output/artifacts/verify_obstruction.py` (stdlib only, no
dependencies); expect VERIFY_OK with the logged numbers above. The full
proof is self-contained given the cited references below.

## References

- Chifan–Ioana–Osin–Sun, Wreath-like products I: W\*-superrigidity,
  arXiv:2111.04708v4 (Def. 1.2; Thm. 1.3; §2.2 Thm. 2.6; §2.3; §§3.2,3.5,4.2–4.3).
- Chifan–Ioana–Osin–Sun, Wreath-like products III: Embeddings,
  arXiv:2402.19461v2.
- Popa, Strong rigidity of II_1 factors arising from malleable actions,
  Invent. Math. 2006 (intertwining-by-bimodules criterion).
- Ozawa–Popa, Some prime factorization results for type II_1 factors,
  Invent. Math. 2004, https://doi.org/10.1007/s00222-003-0338-z
  (solid-class UPF; disjoint coverage).
- Bekka–de la Harpe–Valette, Kazhdan's Property (T) (SL(3,Z) has (T), ICC,
  E12 infinite order).
