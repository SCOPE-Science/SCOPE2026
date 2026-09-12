# K2P single-triangle quarnet D12|34 does not have dimension 7: certified dimension at least 13

## Context

Exact dimensions of phylogenetic network varieties control parameter-count identifiability, degrees of freedom of triangle interiors beyond displayed trees, and penalty terms in algebraic model selection. Dimension formulas for group-based level-1 networks (Gross–Krone–Martin and successors) deliberately assume triangle-free networks, leaving 3-cycle (single-triangle) quarnets open. The admitted target asked whether the Kimura two-parameter (K2P) Fourier phylogenetic variety of the named single-triangle quarnet D12|34 has Krull dimension exactly 7. Both confirmation (dimension 7 with Hilbert certificate) and a certified corrected dimension were pre-approved as TARGET resolutions.

## Definitions and object

Let D12|34 be the binary semi-directed level-1 quarnet on taxa {1,2,3,4} with split 12|34, one 3-cycle, and hybrid leaf-child 1. Work in K2P Fourier coordinates over G = Z2 x Z2 with classes identity (0,0), transition (0,1), transversions (1,0),(1,1), edge normalization a_e^0 = 1, per-edge parameters (t_e, s_e) = (transition, transversion), nine network edges rc, r4, ca, c3, ab, b2, ah, bh, h1, plus interior mixture parameter delta (keep b->h) versus 1-delta (keep a->h), for 19 parameters total.

There are 64 Fourier pattern classes (g1,g2,g3,g4) with g1+g2+g3+g4 = 0 in G, s = g1+g2. The audited parametrization is, for each pattern p:

- M1(p) = bh(g1) h1(g1) b2(g2) c3(g3) r4(g4) ab(s) ca(s) rc(s),
- M2(p) = ah(g1) h1(g1) ab(g2) b2(g2) c3(g3) r4(g4) ca(s) rc(s),
- q(p) = delta M1(p) + (1-delta) M2(p),

where each factor contributes t_e if its group element is a transition, s_e if a transversion, and 1 if identity. The phylogenetic variety is the Zariski closure of the image of this polynomial map (equivalently the K2P Fourier mixture of the two displayed trees), irreducible as a polynomial image of irreducible parameter space. Displayed tree T1 (keep b->h) is the monomial map p -> M1(p) in 16 edge-class variables on 8 edges.

## Result

The K2P Fourier phylogenetic variety of D12|34 has Krull dimension at least 13, hence its Krull dimension is not 7. The target claim "dimension exactly 7" is rigorously false. A fortiori the displayed-tree K2P locus has dimension exactly 10 (at least 10 certified; at most 10 since it is a monomial image in 10 non-trivial edge-class coordinates after removing identities), which already exceeds 7.

## Proof / evidence

Jacobian rank lower bound at a smooth interior point of the domain. At the explicit rational point t_e = (2+i)/3, s_e = (1+i)/4 (enumerating the nine edges in order), delta = 1/5, all parameters are nonzero and delta is strictly interior, so the domain is smooth there.

1. Network rank 13. The exact 64x19 network Jacobian over QQ at this point has rank exactly 13, certified by the nonzero 13x13 minor on rows [1,2,4,5,8,10,16,20,24,32,36,40,44] and parameter columns [t_rc,s_rc,t_r4,s_r4,t_c3,s_c3,t_ab,s_ab,t_b2,s_b2,t_ah,s_ah,t_bh] with determinant 160576479/2097152 != 0 in exact rational (Bareiss/Fraction) arithmetic. By the Jacobian rank theorem for the dominant map onto its image, the irreducible network variety has dimension at least 13.
2. Tree rank 10. At the same edge values the displayed-tree Jacobian has exact rank 10, certified by a nonzero 10x10 minor with determinant 153125/192. The K2P tree map is monomial (toric), so rank 10 at a smooth point gives image dimension at least 10 (and exactly 10 by the ambient toric coordinate count).
3. Conclusion. 13 > 7 and 10 > 7, so "Krull dimension exactly 7" is impossible.

Robustness: recomputation with the phylogenetically corrected root-edge Fourier exponent rc = g1+g2+g3 (= g4) instead of s = g1+g2 still yields network rank exactly 13 at the witness point and at a second rational point, and tree rank 10, so the falsification does not hinge on that labeling detail.

## Limitations

Only the falsification dim != 7 via certified dim >= 13 is proved; the conjectured exact network value 13 (supported by generic-rank surveys) is not proved here because no Groebner or Hilbert-series upper bound was computed (no Singular/Macaulay2 available). The certificate is in K2P Fourier coordinates with a_e^0 = 1 normalization and uniform root only; it does not cover JC/K3P models or other normalizations.

## Reproducibility

Run `python3 output/artifacts/verify_disproof.py` (stdlib only: exact Fraction Jacobian plus Bareiss determinant, independent re-implementation) which prints VERIFY_OK with network rank 13, det13 = 160576479/2097152, and tree rank 10. A sympy cross-check is in `cert_lower_exact.py` (prints CERT_LOWER_OK). Witness: t_e=(2+i)/3, s_e=(1+i)/4 over the nine edges in order rc, r4, ca, c3, ab, b2, ah, bh, h1, delta=1/5; minor rows and columns listed above.

## References

- E. Gross, R. Krone, S. Martin, Dimensions of Level-1 Group-Based Phylogenetic Networks, Bull. Math. Biol. (2024), arXiv:2307.15166 — dimension formula for triangle-free level-1 group-based networks only.
- Group-based phylogenetic models on 3-sunlet networks — dimensions for three-leaf sunlets, not 4-taxon K2P triangles.
- On Tree-Network Distinguishability and Full Identifiability of Phylogenetic Networks, arXiv:2607.12919 — quarnet identifiability without exact Hilbert dimensions.
- Small Phylogenetic Trees (K2P model) tables — tree ideals/invariants, no K2P triangle-network dimension row.
