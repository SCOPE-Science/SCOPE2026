# Vanishing of the parallel-{0,2} crystalline lifting ring at a niveau-2 mod-3 point over Q_{3^2}

## Context

Let p=3 and K=Q_{3^2} be the unramified quadratic extension of Q_3, with residue field F_9 and absolute Galois group G_K. The admitted target asks for the geometry of the framed crystalline lifting ring over Z_3 at a fixed absolutely irreducible residual representation with parallel Hodge-Tate type {0,2}. Either the ring is nonzero formally smooth of stated dimension with an explicit lift, or it is zero/singular/non-equidimensional/reducible with an explicit certificate. This record resolves the target in the strongest form of branch (ii).

## Definitions

- K=Q_{3^2}: unramified degree-2 extension of Q_3; residue field F_9.
- G_K=Gal(bar K/K), I_K its inertia subgroup.
- omega_2: niveau-2 fundamental character of I_K of order 8; bar rho|_{I_K} ~= omega_2 + omega_2^3.
- omega: mod-3 cyclotomic character G_{Q_3} -> F_3^* of order 2.
- ur_2: unramified character sending geometric Frobenius to 2.
- Fixed residual representation bar rho: G_K -> GL_2(Fbar_3), absolutely irreducible, with det(bar rho)=omega*ur_2.
- chi_cyc: 3-adic cyclotomic character G_K -> Z_3^*, crystalline of labelled weight 1 at every embedding.
- Parallel Hodge-Tate type {0,2}: at each of the two embeddings tau: K -> Qbar_3 the Hodge-Tate weights are {0,2}.
- R^{square,crys,{0,2}}(bar rho): Kisin framed crystalline lifting ring over Z_3 of the above Hodge type, a Z_3-flat quotient of the unrestricted framed lifting ring.

## Result

R^{square,crys,{0,2}}(bar rho)=0.

Equivalently: there is no crystalline lift rho: G_K -> GL_2(E) with parallel Hodge-Tate weights {0,2} at both embeddings, for any finite extension E/Q_3, and the Z_3-flat crystalline quotient of the unrestricted framed lifting ring is the zero ring.

## Proof / Evidence

Step 1 (determinant weights). Suppose rho: G_K -> GL_2(E) is crystalline of parallel weight {0,2}. Then det rho is crystalline of labelled weight 0+2=2 at each embedding. Hence psi := det rho * chi_cyc^{-2} is a crystalline character of labelled weight 2-2=0 at every embedding. This is independent of Hodge-Tate sign convention since both terms negate together.

Step 2 (rank-one lemma). A crystalline character of G_K with all labelled weights 0 is unramified. Via D_crys it corresponds to a rank-one weakly admissible filtered phi-module over K_0=K with trivial filtration at every embedding, so t_H=0 forces Newton slope 0 (unit Frobenius eigenvalue); by Berger-Fontaine-Colmez rank-one equivalence, equivalently local class field theory, psi is trivial on O_K^* and factors through the valuation. Hence det rho|_{I_K}=chi_cyc^2|_{I_K}.

Step 3 (reduction). Take a G_K-stable lattice and reduce mod the maximal ideal. By irreducibility of bar rho the lattice is unique up to scale so the reduced determinant equals det(bar rho). Reducing Step 2: chi_cyc reduces to omega with omega^2=1 (image in F_3^*={+-1}), and psi reduces to an unramified character trivial on I_K. Thus any lift reduces to a determinant trivial on I_K.

Step 4 (contradiction). The prescribed det(bar rho)=omega*ur_2 restricts to omega|_{I_K} since ur_2 is unramified. Now Q_3(mu_3)/Q_3 is totally ramified quadratic while K/Q_3 is unramified quadratic, so they are linearly disjoint and omega|_{G_K} retains order 2; I_K=I_{Q_3} so omega|_{I_K} is nontrivial of order 2. Equivalently omega|_{I_K}=omega_2^{1+3}=omega_2^4 of order 8/gcd(8,4)=2. This contradicts Step 3. Hence no crystalline lift of the required type exists over any finite E/Q_3.

Step 5 (ring vanishing). R^{square,crys,{0,2}}(bar rho) is Z_3-flat by Kisin's construction. If nonzero, R[1/3]!=0 and the Nullstellenssatz for complete Noetherian local Z_3-algebras gives a maximal ideal with residue field finite over Q_3, i.e. a Qbar_3-point or crystalline lift. Since none exists, R=0. Coefficient independence follows because the obstruction rules out lifts over every finite E/Q_3.

Numerical checks: omega_2^4 has order 2; omega^2=1; det weight 0+2=2; K cap Q_3(mu_3)=Q_3 by ramified-vs-unramified disjointness. Verified by output/artifacts/determinant_obstruction_check.py (all checks passed).

## Limitations

This is a vanishing theorem (branch (ii)) rather than a smoothness/dimension statement; no component equations beyond the zero-ring certificate are needed since the generic fiber has no points. Weight 2 lies outside the Fontaine-Laffaille range [0,1] for p=3 but no Fontaine-Laffaille input is used. The rank-one lemma cites the standard weakly-admissible-implies-crystalline equivalence rather than re-proving it.

## Reproducibility

Run python3 output/artifacts/determinant_obstruction_check.py; it asserts the group orders and Hodge-Tate bookkeeping above. The logical steps use only exterior powers preserving crystallinity, the cited rank-one equivalence, lattice reduction for compact G_K, ramified/unramified quadratic disjointness, and Kisin flatness plus Nullstellenssatz.

## References

- M. Kisin, Potentially semi-stable deformation rings.
- M. Emerton, T. Gee, Moduli stacks of etale (phi,Gamma)-modules and the existence of crystalline lifts.
- T. Gee, F. Herzig, T. Liu, D. Savitt, Potentially crystalline lifts of certain prescribed types, arXiv:1506.01050.
- R. Bartlett, On the irreducible components of some crystalline deformation rings, arXiv:1904.12548.
- R. Bellovin et al., Irregular loci in the Emerton-Gee stack for GL_2, arXiv:2309.13665.
