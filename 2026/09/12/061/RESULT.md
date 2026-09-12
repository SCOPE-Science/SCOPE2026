# One-pointed ψ⁵ point descendant on F₁ in class 3H−2E₁ equals 1/12

## Context
Hirzebruch surface F₁ is the blow-up of P² at one torus-fixed point. Its genus-zero Gromov–Witten theory is governed by Givental's toric mirror theorem. One-pointed gravitational descendants ⟨τ_k(α)⟩ encode intersections of psi-classes with evaluation classes on moduli spaces of stable maps. For Fano toric surfaces the small J-function equals the small I-function, so individual descendant invariants can be read from explicit I-function coefficients.

## Definitions
Let X₁ = F₁ = Bl_{p₁}P² with p₁=[1:0:0] for the standard torus action. Let H be the pullback of the hyperplane class, E₁ (also E) the exceptional divisor, F = H−E the fibre class, and pt the point class. Intersection: H²=1, H·E=0, E²=−1, hence F²=0, F·H=F·E=1. Canonical: c₁(X₁)=3H−E, so c₁(F)=2, c₁(E)=1. Let β₁=3H−2E₁=3F+E. Let M̄_{0,1}(X₁,β₁) be the genus-zero one-pointed stable-map moduli space with cotangent line class ψ₁ and evaluation map ev₁. The invariant is ⟨τ₅(pt)⟩_{0,1,β₁}^{X₁} = ∫_{[M̄]^{vir}} ψ₁⁵ ∪ ev₁^*(pt).

## Result
⟨τ₅(pt)⟩_{0,1,β₁}^{X₁} = 1/12.

## Proof / Evidence
Virtual dimension: vdim = dim X₁ − 3 + 1 + c₁(β₁) = 2−3+1+7 = 7, since c₁(β₁)=9−2=7. Insertion ψ₁⁵ (codimension 5) plus pt (codimension 2) gives codimension 7: a virtual zero-cycle degree, well-defined.

Toric data: fan rays (1,0),(0,1),(−1,1),(0,−1) with invariant divisors D₁=F, D₂=E, D₃=F, D₄=H. Mori cone NE=⟨F,E⟩; write d=aF+bE. Pairings D·d=(b,a−b,b,a), sum 2a+b=c₁(d). For β₁: a=3,b=1, pairings k=(1,2,1,3), sum 7.

F₁ is Fano (c₁·F=2>0, c₁·E=1>0 on Mori generators), so Givental's toric mirror theorem gives small J = small I with identical variables. Trivial mirror map verified directly: for every nonzero effective d, the I-summand is O(1/z): if all kᵢ≥0 then I_d=z×O(z^{−c₁(d)}) with c₁(d)≥2 (c₁=1 forces d=E with k₂=−1); if k₂=a−b<0, leading factor gives z^{b−a−1}·D₂ over z^{a+2b}, i.e. z^{−2a−b} with 2a+b≥1, hence O(1/z). Thus I=z+t+O(1/z).

Small J at t=0: J=z+Σ Q^d z^{−k−1}⟨τ_k(φ_α)⟩φ^α. The Q^{β₁}z^{−6} coefficient along identity 1 (dual of pt) is exactly ⟨τ₅(pt)⟩. Since J=I, I_{β₁}=zQ^{β₁}/[(D₁+z)(D₂+z)(D₂+2z)(D₃+z)(D₄+z)(D₄+2z)(D₄+3z)], leading term zQ^{β₁}·1/(1!2!1!3!)·z^{−7}=Q^{β₁}z^{−6}/12. Higher corrections carry positive divisor/point degree and lower z-powers. Exact expansion in H*(F₁)[w], w=1/z, using D³=0, confirms w⁷-coefficient 1/12·1, w⁸ divisor −(11/72)H−(1/6)F−(1/8)E, w⁹ pt-component 131/216, consistent with grading.

## Limitations
Relies on Givental's toric mirror theorem for Fano F₁ (verified trivial mirror map here). Identification β₁=3F+E with pairings (1,2,1,3) as stated. No independent fixed-point localization sum or tropical floor-diagram enumeration performed; no numerical cross-check beyond exact I-function expansion.

## Reproducibility
Run `python3 output/artifacts/leading_coeff.py` (exact Fraction arithmetic, no floating point). It multiplies the seven factors 1/(D+mz) expanded to O(w⁹) in basis {1,H,F,E,pt} with relations H²=pt, H·E=0, E²=−pt, and asserts the w⁷ coefficient equals 1/12·1.

## References
- Givental, toric mirror theorem (Fano small J=I).
- Coates–Corti–Iritani–Tseng, computing genus-zero twisted GW invariants (quantum Lefschetz).
- Gholampour–Tseng, genus-zero two-point descendants via one-point invariants.
- Cavalieri–Johnson–Markwig–Ranganathan, counting curves on Hirzebruch surfaces (tropical/floor/Fock descendant correspondence).
- Spielberg, counting genus-0 curves on Hirzebruch surfaces.
