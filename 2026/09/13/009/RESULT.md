# Genus-two b1>0 SL2 Heegaard Loc intersection: models, Lagrangian certificates, and proved integers

## Context

Let G=SL_2(C) with Lie algebra g=sl_2 (dim 3), Sigma=Sigma_2 a closed genus-2 surface, and X=Loc_G(Sigma)=Map(Sigma_B,BG) the derived character stack with its PTVV 0-shifted Atiyah-Bott-Goldman symplectic form. Let H_+,H_- be genus-2 handlebodies with boundary Sigma, L_pm=Loc_G(H_pm) their AKSZ-PTVV boundary Lagrangians, glued by a separating-curve Dehn twist so the closed 3-manifold M=H_+ union_Sigma H_- has pi_1=F_2, equivalently M homotopy equivalent to (S^2 x S^1)#(S^2 x S^1) with b_1=2 (not S^3). This tests shifted-symplectic Heegaard gluing: mapping-stack models, Lagrangian structures, and the derived intersection W=L_+ x_X L_-=Loc_G(M) at an explicit non-transverse point.

## Definitions

Sigma_B is the Betti homotopy type of Sigma (2-dimensional, 2-oriented); BG=[pt/G]. X=Map(Sigma_B,BG)=[Rep/G] where Rep=mu^{-1}(I) is the derived fiber of the commutator word mu(A_1,B_1,A_2,B_2)=[A_1,B_1][A_2,B_2] over I in G^4, modulo conjugation. Each handlebody retracts to a wedge of two circles with pi_1(H)=<a_1,a_2>=F_2; the inclusion q:pi_1(Sigma)->pi_1(H) kills meridians b_1,b_2. Hence L_pm=[G^2/G] with legs j_+(A_1,A_2)=(A_1,I,A_2,I) and j_-=tau_* circ k (same formula k), tau_* the separating-twist automorphism, both landing in Rep since [A,I]=I identically. The trivial representation rho has adjoint local system ad=g with trivial action. T_W|_rho denotes the tangent complex of W at rho; H^i(T_W|_rho) its cohomology; vdim the virtual dimension; w the derived-loop (Tor) Euler weight sum_i(-1)^i dim Tor_i.

## Result

Theorem. With W=L_+ x_X L_-=Loc_G(M) as above:

(a) Mapping-stack models: X=[Rep/G] as above; L_pm=[G^2/G] with legs j_+,j_- landing in Rep.

(b) Both legs carry AKSZ-PTVV Lagrangian structures; on tangent cohomology the restriction H^1(H;ad)->H^1(Sigma;ad) has 6-dimensional Lagrangian image (half of 12), isotropic because H^2(H)=0, with Goldman Gram matrix G_12=J_4 tensor K restricting to the 6x6 zero block on indices {0,1,2,6,7,8}.

(c) The separating-twist gluing gives pi_1(M)=F_2, H_*(M;Z)=(Z,Z^2,Z^2,Z), b_1=2, chi(M)=0; M not S^3.

(d) At rho, H^i(T_W|_rho) cong H^{i+1}(M;ad) has dimensions (h^{-1},h^0,h^1,h^2)=(3,6,6,3); virtual dimension 0; (-1)-shifted duality H^i cong (H^{1-i})^vee holds.

(e) The derived-loop Euler (Tor) weight at rho is w=-3+6-6+3=0, Tor-amplitude length 3, excess 3 (classical W^{cl}=[G^2/G] of stack-dimension 3 over vdim 0), Behrend sign (-1)^3=-1, loop-rotation secondary Euler sum(-1)^i i h^i=3.

## Proof / evidence

Word maps: [A_1,I][A_2,I]=I identically, so j_pm land in Rep as derived maps via the constant homotopy of the word (checked symbolically and on exact SL(2,C) test matrices). Separating curve c=[a_1,b_1]; twist tau_*(a_1)=a_1, tau_*(b_1)=b_1, tau_*(a_2)=c a_2 c^{-1}, tau_*(b_2)=c b_2 c^{-1}, a Torelli automorphism preserving the surface relation. On the meridian-killing sublocus B_1=B_2=I one has C=[A_1,B_1]=I identically, so tau_* restricts to the identity there; hence j_- agrees classically with k. Van Kampen: pi_1(M)=pi_1(H_+) *_{pi_1(Sigma)} pi_1(H_-) with q_+(g)=q_-tau_*(g); since c maps to 1 mod meridians, meridian relations still die and q_-tau_*(a_i)=y_i, giving <x_1,x_2,y_1,y_2|x_i=y_i> cong F_2. Mayer-Vietoris with Phi=i_+ (+) (-i_-):Z^4->Z^4 of rank 2 gives H_2(M)=ker Phi=Z^2, H_1(M)=coker Phi=Z^2, H_3(M) cong Z, H_0=Z; tensoring with 3-dimensional ad gives (3,6,6,3). Lagrangian certificate: Calaque boundary AKSZ-PTVV theorem gives (-1)-shifted Lagrangians L_pm->X (twist is symplectomorphic); tangent check via relative tangent C^*(H,Sigma;ad)[1] and Poincare-Lefschetz duality plus the explicit isotropic 6-plane verified in sympy (J_4 det 1, K det -128, G_12 nondegenerate, 6x6 zero block). Tangent of derived fiber product is the fiber of tangents, T_W|_rho simeq C^*(M;ad)[1] by excision, yielding the integers, vdim=-3+6-6+3=0=3+3-6, duality, and w=0. All assertions machine-checked by output/artifacts/verify_heegaard.py (ALL_ASSERTIONS_PASSED; output saved to verify_heegaard.json).

## Limitations

Computation is at the trivial representation with trivial ad action; no claim about irreducible loci. Full derived-stack AKSZ-PTVV functoriality is cited to PTVV/Calaque rather than re-proved; the tangent check certifies the Lagrangian restriction image. Behrend-sign and loop-rotation numbers are local refinements at a smooth classical point, not a global enumerative invariant.

## Reproducibility

Run `python3 output/artifacts/verify_heegaard.py` (requires sympy); it asserts word-leg identities, twist collapse, Phi rank 2 and Betti (1,2,2,1), Goldman nondegeneracy with Lagrangian zero block, tangent (3,6,6,3), vdim 0, duality, w=0, excess 3, sign -1, secondary 3, and prints ALL_ASSERTIONS_PASSED.

## References

T. Pantev, B. Toen, M. Vaquie, G. Vezzosi, Shifted Symplectic Structures, arXiv:1111.3209. D. Calaque, Shifted cotangent stacks are shifted symplectic, arXiv:1612.08101. D. Joyce, A classical model for derived critical loci, arXiv:1304.4508.
