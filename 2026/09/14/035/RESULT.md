# Derived Hitchin map as shifted coisotropic morphism (g=2, r=3)

## Statement

Let k be algebraically closed of characteristic zero, C a smooth projective
genus-2 curve, M the moduli stack of stable rank-3 degree-d coprime GL(3)
Higgs bundles, B = H^0(C,K) + H^0(C,K^2) + H^0(C,K^3) ~= A^10, and
h: M -> B the Hitchin morphism. Then:

(a) h carries a canonical degenerate 0-shifted coisotropic structure in the
Melani-Safronov sense with zero Poisson structure on B and strict relative
polyvector data;
(b) over the smooth-spectral open B^sm it is nondegenerate: a smooth
Lagrangian fibration with anchor isomorphism and relative volume
Theta = X_1 ^ ... ^ X_10;
(c) over any open meeting the irreducible one-nodal discriminant
divisor-open D^irr_{1-nod}, no compatible nondegenerate coisotropic lift
exists. The obstruction delta_nod = det(anchor), equivalently Theta, is a
named explicit nonzero section vanishing exactly on Crit(h), dominating
D^irr_{1-nod}. Hence global nondegeneracy is disproved sharply.

## Context

The target asks whether the full derived Hitchin morphism for g=2, r=3
lifts to a canonical 0-shifted coisotropic morphism, nondegenerate over the
smooth spectral locus, with a named explicit obstruction over the nodal
discriminant. The coprime hypothesis makes the stable locus smooth and
classical, so derived machinery reduces to ordinary Poisson geometry while
retaining MS meaning.

## Definitions

- M: rigidified stable Higgs moduli, smooth quasi-projective irreducible
  20-fold; deformation complex [End E -> End E tensor K] in degrees 0,1.
- B = A^10 with coordinates u_i; f_i = h^*u_i; X_i = pi_M^#(df_i).
- pi_M: 0-shifted Poisson bivector inverse to PTVV/Hitchin symplectic form.
- Anchor a: h^*Omega_B -> T_{M/B}, du_i |-> X_i.
- Theta = wedge X_i; delta_nod = det(a).
- B^sm: smooth integral spectral curves, dense open; D^irr_{1-nod}: dense
  open of irreducible one-nodal spectral curves in discriminant hypersurface.

## Result

Degenerate-global canonical coisotropic structure exists strictly with
vanishing higher homotopies. It is nondegenerate precisely over B^sm and
explicitly obstructed over the nodal divisor by nonzero delta_nod. No
globally nondegenerate canonical structure exists.

## Proof / evidence

Classicality: curve case gives Ext^2 = 0, so stable coprime locus needs no
derived enhancement; MS Pol(h,0) reduces to ordinary relative polyvectors.
Over B^sm, spectral curves have arithmetic genus 10 by Riemann-Hurwitz
(2g_S-2 = 3*2+12), fibers Pic^d are 10-dimensional abelian varieties and
Hitchin Lagrangian; thus {f_i,f_j} = 0 on dense M^circ, hence everywhere by
regularity and irreducibility. Zero Poisson on B is forced by density and
algebraicity. MC equations hold strictly: [pi_M,pi_M]=0, [pi_M,X_i]=0,
[X_i,X_j]=0. Over B^sm the Lagrangian-fibration duality makes the anchor an
isomorphism, giving relative volume Theta. Discriminant is a degree-12
hypersurface; reducible loci have dimensions <=7 and <=6, hence codim >=3,
so generic discriminant is irreducible and D^irr_{1-nod} is nonempty dense
open. Its fibers are irreducible singular compactified Jacobians of
arithmetic genus 10 (non-locally-free locus = genus-9 Jacobian), so h|_U is
never smooth over nodals. But an everywhere-invertible anchor would force
smoothness (lci plus correct-rank relative cotangent), contradiction. Any
compatible anchor is Hamiltonian up to GL(10) gauge with degeneracy Crit,
so no alternative lift avoids Theta vanishing. Numerics reproduced by
artifacts/check_dims.py: h0 = 2,3,5; dimB = 10; dimM = 20; g_S = 10.

## Limitations

Requires coprime degree, k = closure, char 0; only stable locus treated.
Generic nodal statement uses standard discriminant, codimension counts, and
cited compactified-Jacobian singularity; no new Severi theorem proved.
Non-coprime and nilpotent-cone deeper strata not analyzed.

## Reproducibility

Run `python3 artifacts/check_dims.py`; all dimension, genus, and codimension
assertions pass. Arguments use cited Hitchin, BNR, Nitsure, Altman-Kleiman,
D'Souza, Esteves, PTVV, Melani-Safronov.

## References

- Hitchin, Stable bundles and integrable systems.
- Beauville-Narasimhan-Ramanan spectral correspondence; Nitsure moduli.
- Altman-Kleiman, D'Souza, Esteves compactified Jacobians.
- Pantev-Toen-Vaquie-Vezzosi shifted symplectic; Melani-Safronov derived
  coisotropic structures I-II; Calaque-Pantev-Toen-Vaquie-Vezzosi.
