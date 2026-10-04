# Review

## Correctness
PASS. For \(E(c,Q)\), the affine image of a unit-ball slice gives the exact formula
\[
V_E(u)=\kappa_{n-1}\sqrt{\det Q}\,\frac{[u^TQu-(r-u\cdot c)^2]^{(n-1)/2}}{(u^TQu)^{n/2}}.
\]
The odd part of the transformed data yields a polynomial identity whose irreducible quadratic factors force proportional shape forms; the unpowered identity then recovers the center exactly. The even part removes the remaining scalar. The centered case is handled separately, including the spherical subcase. Strict containment of the inner ball supplies all positivity hypotheses. The packaged verifier confirms the slice Jacobian and parity identities on independent numerical examples but is not the proof.

## Originality
PASS, with a stated historical-access risk. The closest full-text sources are Yaskin–Zhang (2015), which formulates the one-ball problem and gives different partial results, and Makai–Martini (2016), which explicitly calls the hyperplane case unsolved and proves local first-order determination only. Matthews (2026) proves a global polygon result in the plane and identifies extension beyond the polyhedral class as a further direction. Targeted published-finding corpus searches for ellipsoids, tangent inner-ball sections, sectional-volume injectivity, and Barker–Larman special cases returned no statement implying the theorem. The 2001 Barker–Larman full article could not be lawfully inspected in full during the bounded access attempt, so an older unindexed ellipsoid-specific argument remains a residual risk rather than being treated as absent.

## Value
PASS. Ellipsoids are the canonical smooth finite-dimensional class in convex geometry, but the data here are noncentral and encode both translation and anisotropy. A global injectivity theorem for arbitrary centers and axes gives a natural nonperturbative benchmark inside an open tomography problem and complements the known local-smooth and polygonal cases.

Same-model review: passed. Independent audit: not yet performed.
