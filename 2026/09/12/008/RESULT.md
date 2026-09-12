# Rank-two numerical tilt-wall census for the conic-ideal projection class on a very general ordinary Gushel–Mukai threefold

## Context

Conics govern much of Gushel–Mukai (GM) geometry, from Hilbert schemes to EPW sextics and hyperkähler moduli identifications, yet the tilt wall for conic-ideal projections in Kuznetsov components of threefolds was unclassified. The admitted target asked for an empty-or-sharp verdict at tilt parameter beta=0 for the primitive conic-ideal projection class. In-session computation blocked the full target: the numerical census itself exhibits classical Bogomolov–Gieseker-admissible walls above alpha=1/2. This record reports the completed emergent numerical core that any continuation must build on.

## Definitions and setup

Let X be a very general ordinary Gushel–Mukai threefold over C, so Pic(X)=Z H with H^3=10, H^2=10 L (L = line class), H·L=1 (point). Work in the Kuznetsov component Ku_1 = <E, O_X>^perp where E = U_X is the rank-two exceptional bundle. Truncated Chern vectors are written (r,c,d,e) for ch_0=r, ch_1=c H, ch_2=d L, ch_3=e P. The Todd class is td(X)=1+(1/2)H+(17/6)L+1·P, and chi(A,B)=∫_X ch(A)^vee ch(B) td(X) with ch(A)^vee=(r,-c,d,-e). Key classes: O_X=(1,0,0,0), E=(2,-1,1,1/3), E^vee=(2,1,1,-1/3), I_C=(1,0,-2,0) for I_C the ideal sheaf of a smooth conic C ⊂ X. Tilt stability sigma_{a,0} at beta=0 uses Im Z_{a,0}=10c, Re Z_{a,0}=5a^2 r-d, mu=-Re/Im.

## Result

For the Kuznetsov projection class [G]=[pr(I_C)]=(-1,1,-3,-1/3) of a smooth conic at tilt parameter beta=0:

1. [G]=[I_C]-[E] is a primitive (-1)-class: chi(G,G)=-1, Delta(G)=40, gcd(1,1,3)=1, Im(G)=10.
2. Restriction splitting: E^vee|_C ≅ O(1)⊕O(1) or O(2)⊕O(0), hence h^0(C,E^vee|_C)=4, h^1=0. This yields 0 → Hom(E,I_C) → k^5 →rho→ k^4 → Ext^1(E,I_C) → 0 with Ext^{≥2}(E,I_C)=0; surjectivity of rho (RHom concentration in degree 0) is the single logged-open Hom-theoretic point.
3. Conditional Im-gap: given G ∈ Coh^0(X) (equivalently surjectivity of rho), every subobject F ↪ G in the tilt heart has Im(F)=10 c_F with c_F ∈ Z, so no subobject has 0<Im(F)<Im(G)=10; every destabilizer has c_F=1 or Im 0.
4. Rank-two c_F=1 numerical walls are exactly a^2=(d_F+3)/15 (K-theoretic, unconditional), with six classical-BG-admissible integer cases d_F=-3..2 at a ≈ {0, 0.258, 0.365, 0.447, 0.516, 0.577} and Delta(F)=220,180,140,100,60,20 respectively. The natural candidate F=E^vee sits on the d_F=1 wall (a=2/sqrt(15)≈0.516) with massless quotient Q=(-3,0,-4,0) and chi(E^vee,G)=+1.
5. No-go corollary: since the d_F=1,2 walls lie strictly above a=1/2, blanket tilt-wall emptiness above 1/2 is formally false on BG numerics; deciding empty-vs-sharp needs the Li improved BG value, ch_3-effectivity, tilt-semistability of F,Q, and torsion exclusion.

## Proof and evidence

Exact rational Riemann–Roch (script-replayed): chi(O_X,I_C)=0 and chi(E,I_C)=1 fix [G]=[I_C]-[E]=(-1,1,-3,-1/3); chi(G,G)=-1 and Delta(G)=(10·1)^2-20(-1)(-3)=40 follow directly. E^vee is globally generated as a quotient of a trivial bundle on Gr(2,5), so its restriction to C ≅ P^1 of degree H·C=2 splits as stated with the claimed cohomology. Applying Hom(E,-) to 0→I_C→O_X→O_C→0 with ambient vanishing H^0(X,E^vee)=k^5, H^{>0}=0 and the restriction computation gives the four-term sequence with Ext^{≥2}=0; the Euler check 5-4=1 matches chi(E,I_C). Conditional Coh^0 placement uses slope-stability of E (kernel of rank 1 with mu_H ≤ -1/2 in F) and rank-zero cokernel in T. The Im-gap is integrality of c_F. Equal tilt slopes with equal imaginary parts force Re(Q)=0 for Q=G-F with r_Q=-3, i.e. -15a^2+3+d_F=0, giving the wall equation; classical Delta(F)=100-40 d_F ≥ 0 plus a^2 ≥ 0 leaves exactly d_F ∈ {-3,...,2}. All numbers are printed by the replay script.

## Limitations

The census is numerical (K-theoretic plus classical BG admissibility), not a proof of actual-vs-empty wall status. Open and explicitly not claimed: surjectivity of rho (hence unconditional G ∈ Coh^0 placement); actual tilt-semistability of candidate subobjects (notably E^vee) and massless rank-(-3) quotients at their walls; Li improved BG values at (s,q)=(1/2,d_F/20) and ch_3-effectivity bounds to kill d_F=1,2; torsion (Im 0) subobject exclusion; Serre-invariant Bridgeland transfer to the beta=0 tilt ray (cited context only).

## Reproducibility

Run `python3 output/artifacts/wall_census.py` (exact rational arithmetic via fractions.Fraction); compare with committed log `output/artifacts/wall_census.log`. Expected output: chi(O,IC)=0, chi(E,IC)=1, chi(G,G)=-1, Delta(G)=40, chi(Edual,G)=1, and the six-wall table above. Proof details are in DRAFT-equivalent Sections 2–6 summarized here.

## References

- S. Zhang, Bridgeland moduli spaces for GM threefolds, arXiv:2012.12193 (conic-projection stability, minimal model of Fano surface of conics).
- L. Pertusi–E. Robinett, Stability conditions on Ku of GM threefolds, arXiv:2112.04769 (Serre-invariance).
- H. Guo–Z. Liu–S. Zhang, Conics on GM fourfolds, arXiv:2203.05442 (fourfold EPW context; different dimension/classes).
