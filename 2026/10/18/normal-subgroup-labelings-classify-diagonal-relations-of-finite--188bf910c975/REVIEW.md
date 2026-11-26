# Independent mathematical audit

## correctness

PASS

Projection of a diagonal subsemigroup gives a meet-closed support containing the diagonal. Each nonempty group-coordinate fiber is a subgroup since it is a finite subsemigroup of G×G. Multiplication by the diagonal at the semilattice top gives Δ_G in every such fiber. The subgroup H containing Δ_G is reconstructed uniquely from N={g:(g,1_G)∈H}; conjugation by Δ_G gives normality and right multiplication by (h⁻¹,h⁻¹) converts (g,h) into (gh⁻¹,1_G). Multiplication by the identity in a lower fiber forces reverse inclusion and that reverse inclusion suffices for multiplicative closure at meets. For a congruence the support is exactly its trace on identities, and translating along same-group-coordinate cross-level pairs forces all labels on a trace class to coincide. Quotient antitonicity follows by comparing a∧b to b whenever [a]≤[b]; the converse from the quotient labels follows from normality and antitonicity. For the chain, the congruence blocks are intervals and a k-block quotient has k+1 threshold labels, giving the binomial sum (n+3)2^(n−2), including 2 at n=1. A strict upper pair in a support has an initial segment of permitted second coordinates for fixed smaller first coordinate, forced by meeting with the diagonal; similarly below the diagonal. For sufficiency, if a meet is a strict upper pair use an input attaining its smaller first coordinate and the initial-segment rule, and reverse coordinates for a strict lower pair. This gives (n!)² supports. The n+1 diagonal cutoffs give distinct ideals in each support, so the ratio bound is strictly below χ(C_n) for n≥2. Independent NextClosure enumeration and a maximal-element downset recurrence, not the uploaded code's prefix enumeration and ambient ideal intersections, reproduced (2,17,337,12152,696076) through n=5. Replay: /workspace/branches/2b8eb76b-c8f8-4a40-9764-c0de1e1f2612/independent_d_counts.py and independent_d_counts.txt in that directory. Enumeration only checks the indicated finite counts, not the general theorem. The uploaded verifier was inspected and not executed.

## originality

PASS

The distinct contribution is the exhaustive normal-lattice formula for diagonal subsemigroups of the finite constant-group product and its exact chain/simplicity specialization and quantitative DSC bound. The congruence parametrization is a direct specialization of classical kernel–trace theory; the unlabelled chain support count is also covered. Neither is a distinct originality claim here.

## value

PASS

The exhaustive model explains why different finite groups with the same normal lattice give the same inclusion lattice of compatible reflexive relations on this product. It makes exact counts and stronger quantitative bounds possible where the general Clifford result gives only an injection and inequality. The simple-group chain specialization identifies genuinely extra relations and reduces large relation counts to tractable support and ideal counts; no unrestricted Clifford classification is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
