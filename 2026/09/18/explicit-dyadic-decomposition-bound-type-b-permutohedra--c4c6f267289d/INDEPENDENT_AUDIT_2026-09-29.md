# Independent audit — 2026-09-29

**Record:** `2026/09/18/explicit-dyadic-decomposition-bound-type-b-permutohedra--c4c6f267289d`  
**Audited source tree:** `998ee4499989807a76213edcf0198eb677255a90`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026@253a0fe5d0217455660a277f9adb940030e567ad`  
**Disposition:** **PASSED**

## Correctness — PASS

PASS. The lattice argument checks. For any independent set of type-B roots, peeling a degree-one row or column splits off a unimodular 1x1 block; if no such vertex remains, independence plus the two-nonzero-per-column structure forces the support bipartite graph to be a disjoint union of square cycles, each nonsingular cycle block having Smith form diag(1,...,1,2). Thus every saturation quotient has exponent at most 2. For independent root-spanned complementary spaces V,W this gives 2((V+W) cap Z^n) subset (V cap Z^n) direct-sum (W cap Z^n), and the same conclusion restricts to rational simplex-direction subspaces by uniqueness of the V+W decomposition. In a join across consecutive integer coordinate slices, quotienting the bridge vector reduces the lattice quotient to the sum of the two direction lattices, so a genuinely two-sided join adds at most one binary denominator and a point-sided join adds none. The recurrence 1+max b(r_i)<=b(r_0+r_1+1), b(r)=max(0,floor((r-1)/2)), is valid for positive r_0,r_1 and propagates through Vallée's deletion-contraction triangulation. Finally, the barycentric-coordinate argument correctly turns annihilation of each maximal-simplex quotient into the stated 2^m decomposition. The tetrahedron conv{000,110,101,011} gives the claimed non-IDP lower bound and products with cubes preserve it, yielding mu_3=mu_4=1.

## Originality — PASS

PASS, qualified. Vallée's September 2026 paper proves regular dyadic triangulations and a dimension-wise uniform dyadic decomposition exponent, but its published theorem is qualitative and chooses an exponent from finitely many simplex volumes rather than stating this intrinsic-dimension bound. The half-integrality of bidirected/type-B incidence configurations is classical (Bolker–Zaslavsky), and the nonnormal tetrahedral obstruction is known, but I found no source giving the recursive simplex quotient-exponent estimate or the uniform floor((d-1)/2) bound. Because the motivating paper is very recent, priority remains qualified against unindexed follow-up work.

## Scientific value — PASS

PASS. Replacing an unspecified dimension-dependent exponent by an explicit intrinsic-dimension bound materially strengthens the decomposition theorem and isolates the correct lattice invariant—quotient exponent rather than normalized volume. The proof also determines the optimal uniform exponent in dimensions 3 and 4 and supplies a reusable join-recursion method for further sharpening.

## Independent checks

- Reconstructed the Smith-normal-form argument for independent type-B root subconfigurations, including the signed cycle case.
- Checked the join-lattice quotient isomorphism and the binary-exponent recurrence in all point-sided and two-sided dimension cases.
- Verified directly that 111 lies in 2T_triangle but is not a sum of two lattice points of T_triangle.

## Sources checked

- https://arxiv.org/abs/2609.18331 — Mathieu Vallée (2026), Regular dyadic triangulations of delta-matroid polytopes; source for the triangulation/deletion-contraction framework and qualitative uniform dyadic decomposition.
- https://doi.org/10.1002/net.20117 — Bolker and Zaslavsky (2006), classical half-integrality for bidirected network matrices.
- https://arxiv.org/abs/2609.02778 — Santiago Morales (2026), nearby nonnormal delta-matroid/(0,1)-polytope context and the tetrahedral obstruction.

## Limitations

- The upper bound is not shown optimal for d>=5.
- The theorem concerns dyadic decomposition and simplex quotient exponent, not ordinary IDP/normality or a matching bound on normalized volumes.
- Originality is qualified by the recency of Vallée's preprint and possible unindexed follow-up work.

## Audit conclusion

All three audit axes pass. No substantive research-file correction is required. This audit updates only the independent-audit verification channel; the Lean and expert-attestation channels are preserved exactly. GitHub was used only as read-only evidence during this audit.
