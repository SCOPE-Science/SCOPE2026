# Independent mathematical audit

## correctness

PASS

For all n≥2 every pair of graph vertices is an exact resolving neighborhood: {u1,u2} via apices, {u_a,v_i} via spoke vertex–edge pair, and {v_i,v_j} via corresponding spoke edges. Singleton neighborhoods arise only from incident vertex–edge pairs; n=2 forces all 4, n=3 forces u1,u2,v1,v3, n≥4 forces v1,vn. Remaining neighborhoods contain ≥2 vertices and are implied by the pair inequalities. For n≥4 the n free vertices form fractional vertex cover of K_n; summing all pair constraints yields weight at least n/2, tight exactly when all free weights equal 1/2 (n≥3). Endpoint weights contribute 2: λ=(n+4)/2. The n=2,3 exceptions follow. Independently reconstructed all original mixed-distance neighborhoods and solved indicator and original absolute-difference LP for n=2,...,10 using SciPy HiGHS, obtaining predicted optima and same vectors; finite replay corroborates, arbitrary n follows the proof.

## originality

PASS

Fractional optima and optimizer rigidity are not the preexisting integer mixed metric dimension; the full pair/singleton resolving-neighborhood reduction supplies a new precise fractional-polyhedral result for double fans. Originality is best-of-knowledge, not a claim that all unindexed sources were excluded.

## value

PASS

The standard mixed-resolving LP for a named infinite graph family has an exact unique optimum and a near-factor-two integrality gap. This describes a natural relaxation’s polyhedral weakness, rather than a renaming, a tiny isolated computation, or recomputation of known integer mdim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
