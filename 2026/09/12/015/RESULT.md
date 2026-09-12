# Bracket rigidity of the mixed HH^1 action on the punctured-torus base gentle algebra

## Context

Hochschild cohomology governs infinitesimal deformations and derived invariants of algebras. For gentle algebras arising from surfaces, a sought dictionary links the Gerstenhaber bracket on Hochschild cohomology to mapping-class geometry: HH^1 directions should act nontrivially exactly along Dehn-twist-mobile directions. The minimal punctured-surface test case is the once-punctured torus with its three-arc triangulation. The admitted target asked whether the mixed action HH^1 x HH^2 -> HH^2 vanishes on the associated base gentle algebra A0. Admission heuristics (Ladkani AG-formula, relation-cycle counts) expected both HH^1 and HH^2 nonzero, making zero-versus-nonzero a substantive dichotomy.

## Definitions

Let k be an algebraically closed field of characteristic 0. Let S be the once-punctured torus with ideal triangulation T0 of three arcs forming two triangles. Its FST/cluster quiver is the Markov quiver on vertices {0,1,2} with two arrows in each cyclic direction: a1,a2: 0->1, b1,b2: 1->2, c1,c2: 2->0, with potential terms a1b1c1 + a2b2c2. Fix the minimal admissible cut c0 = {c1,c2} (up to the manifest Z3 rotation symmetry). The base algebra is

A0 = kQ_{T0}/I_{T0,c0} = k<a1,a2,b1,b2>/(a1b1, a2b2),

with vertices e0,e1,e2, arrows as above, surviving length-2 paths p1 = a1b2, p2 = a2b1. Then dim_k A0 = 9 with basis {e0,e1,e2,a1,a2,b1,b2,p1,p2}; all products of three or more arrows vanish. HH^i denotes Hochschild cohomology; the Gerstenhaber bracket has degree |[a,b]| = |a|+|b|-1, so HH^1 x HH^2 -> HH^2 is the Lie-module (outer-derivation) action on second-order deformations.

## Result

Theorem. For A0 as above over any algebraically closed field of characteristic zero, HH^2(A0) = 0 while HH^1(A0) = k^2. Consequently the Gerstenhaber bracket pairing HH^1(A0) x HH^2(A0) -> HH^2(A0) vanishes identically, in the strengthened vacuous form: every bracket class lands in the zero space, while the source HH^1 is nonzero.

## Proof / Evidence

Work in the E-reduced (E = k^3) bar complex with C^0 = k^3 (vertex weights), C^1 = k^12 (values F(a_i), F(b_i), F(p_i) each in a 2-dimensional parallel span), C^2 = k^8 (values G(a_i,b_j) in span(p1,p2) over 4 composable pairs). Differentials:

(delta lambda)(u) = (lambda_t - lambda_s) u,
(delta F)(a_i,b_j) = a_i F(b_j) - F(a_i b_j) + F(a_i) b_j,

using a1b1 = a2b2 = 0, a1b2 = p1, a2b1 = p2. In coordinates F(a1)=(r1,r2), F(a2)=(r3,r4), F(b1)=(s1,s2), F(b2)=(s3,s4):

- a1b1-block: (s2, r2); a2b2-block: (r3, s3);
- a1b2-block: (s4+r1, 0) - F(p1); a2b1-block: (0, s1+r4) - F(p2).

Hence delta1: k^12 -> k^8 is surjective (rank 8): the relation-free coordinates surject the a1b1/a2b2 blocks and F(p1), F(p2) surject the remaining blocks. So im(delta1) = k^8 and HH^2 = 0. Meanwhile rank(delta0) = 2, dim ker(delta1) = 12-8 = 4, so HH^1 = ker/im = k^2, with certified representatives v1 = (F(a2)=-a2, F(b1)=b1) and v2 = (F(a1)=a1, F(p1)=p1), each a cocycle and independent mod coboundaries (adjunction raises rank 2->3->4). Bardzell cross-check: AP2 = {a1b1, a2b2}, C^2_Bar = k^4, restricted delta1 full rank 4, independently giving HH^2 = 0. All matrices have integer entries; exact rational row reduction transfers to every characteristic-zero field. Since the target HH^2 = 0, [x,y] = 0 for all x in HH^1, y in HH^2.

## Limitations

The vanishing holds in strengthened vacuous form HH^2 = 0, contrary to the admission expectation of nonzero HH^2; the mapping-class-rigid interpretation collapses to rigidity via a zero target (no infinitesimal deformations at all, stronger than bracket vanishing), with HH^1 = k^2 nonzero. The proof covers the minimal surface cut c0 up to Z3 rotation; non-minimal or non-surface cuts (e.g. diagonal pairing a1b2 = a2b1 = 0) are out of scope. Characteristic-zero hypothesis is used only for exact rational linear algebra; no positive-characteristic torsion analysis is claimed.

## Reproducibility

`output/artifacts/verify.py` (Python stdlib only, exact Fraction arithmetic) checks: (E1) associativity on all 9^3 basis triples; (E2) d^2 = 0; (E3) rank(delta0) = 2, rank(delta1) = 8 giving HH^1 = k^2, HH^2 = 0; (E4) Bardzell AP2 full-rank cross-check; (E5) two explicit HH^1 representatives certified as cocycles and independent mod coboundaries. It prints VERIFY_OK.

## References

- S. Ladkani, Hochschild cohomology of gentle algebras, arXiv:1208.2230 (dimension formulas from Avella-Alaminos-Geiss invariant; Corollary 4 unpunctured-surface only).
- C. Chaparro, S. Schroll, A. Solotar, M. Suarez-Alvarez, The Hochschild cohomology and the Tamarkin-Tsygan calculus of gentle algebras, arXiv:2311.08003 (general calculus, no A0 evaluation).
- M. J. Redondo, L. Roman, Gerstenhaber algebra structure on the Hochschild cohomology of quadratic string algebras (Bardzell bracket route).
- C. Chaparro, S. Schroll, A. Solotar, On the Lie algebra structure of the first Hochschild cohomology of gentle algebras and Brauer graph algebras, J. Algebra 2020.
