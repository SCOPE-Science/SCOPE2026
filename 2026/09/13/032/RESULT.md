# Nested Hilbert Hecke Lagrangian in Hilb^n x K3 x Hilb^{n+1}

## Context

Hilbert schemes of points on K3 surfaces are the prototypical compact holomorphic symplectic (hyperkahler) manifolds. Hecke-type nested Hilbert schemes parametrize flags of subschemes and underlie Nakajima operator constructions. Whether the natural nested flag locus is isotropic or Lagrangian in a signed triple product was motivated before computation as a test of Beauville-form functoriality and correspondence geometry.

## Definitions

Let S be a smooth complex projective K3 surface with holomorphic symplectic form sigma. Let X_n=Hilb^n(S) with Beauville form sigma_n, X_{n+1}=Hilb^{n+1}(S) with sigma_{n+1}. Let Z_n=Hilb^{n,n+1}(S) parametrize flags I_eta subset I_xi, i.e. xi subset eta with lengths n and n+1. Let x in S be the residual point with Supp(I_xi/I_eta)={x}. Define j:Z_n -> Y_n=X_n x S x X_{n+1} by (xi subset eta) |-> (xi,x,eta). Equip Y_n with Omega=pr_1^*sigma_n+pr_S^*sigma-pr_2^*sigma_{n+1}, holomorphic symplectic of dimension 4n+4.

## Result

For every such S and every n>=1, j is a closed embedding, Z_n is smooth irreducible of dimension 2n+2, and j(Z_n) is a Lagrangian subvariety of (Y_n,Omega): j^*Omega=0 and dim Z_n=(1/2)dim Y_n=2n+2. In particular the Hecke correspondence is compact Lagrangian with the + + - sign pattern; with all + signs it would not be isotropic.

## Proof / Evidence

Cited standard theorems, separated from new argument: Fogarty smoothness of X_n; Beauville symplectic structures; Cheah/Tikhomirov/Ellingsrud-Stromme smoothness, irreducibility, dimension 2n+2 for consecutive (n,n+1); Beauville sum normalization pi_n^*sigma_n=sum pr_i^*sigma on the distinct-point locus. Incidence description gives closed embedding i:Z_n -> X_n x X_{n+1}; residual length-1 quotient gives morphism res:Z_n -> S; graph lemma promotes (i,res) to closed embedding j.

Let V_n, V_{n+1} be reduced loci and U=j^{-1}(V_n x S x V_{n+1}), nonempty open hence dense by irreducibility; points are disjoint unions eta=xi disjoint {q}, x=q. On ordered etale cover tilde U=S^{n+1}_0 with alpha((p_i),q)=((p_i),q,((p_i),q)) and quotient rho by S_n, one has j circ rho=(pi_n x id x pi_{n+1}) circ alpha and (pi_n x id x pi_{n+1})^*Omega=sum sigma_{p_i}+sigma_q-(sum sigma_{p_i}+sigma_q). Hence alpha^*tilde Omega=0, so rho^*(j^*Omega|_U)=0; etale pullback is injective, so j^*Omega|_U=0. Since j^*Omega is holomorphic on smooth Z_n and vanishes on dense U, continuity gives j^*Omega=0 everywhere, including non-reduced flags, with no Ext-trace computation at special points. Dimension count yields Lagrangian.

## Limitations

Assumes S smooth complex projective K3 and consecutive colengths (n,n+1). Smoothness, irreducibility, dimension, Beauville structures with sum normalization, and incidence closed-embedding description are cited, not re-proved. No claim for Hilb^{n,m} with m-n>=2, which is generally singular, nor for non-K3 or non-projective surfaces.

## Reproducibility

Verify Fogarty/Beauville/nested-smoothness citations; check residual-point morphism via flat length-1 quotient; check U nonempty and dense; recompute ordered-cover pullback cancellation; use etale injectivity on forms and holomorphic continuity extension; confirm dimension 2n+2 vs 4n+4.

## References

Beauville on symplectic Hilb^n of K3; Fogarty on Hilb^n of surfaces; Cheah, Tikhomirov, Ellingsrud-Stromme on nested Hilb^{n,n+1} smoothness; Nakajima lectures on Hilbert schemes and Hecke correspondences; Ramkumar-Sammartano on nested singularities; von Flach-Neto arXiv:1909.08385 (distinct C^2 framed pre-symplectic study).
