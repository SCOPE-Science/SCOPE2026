# Independent mathematical audit

## correctness

PASS

Confirmed the eight idempotents, the 72 reachable elements, the nine exclusions, and the shortest-length counts 8, 12, 14, 18, 12, 8. The separate 81-element breadth-first computation derived the idempotents by squaring and replayed a witness for each reachable element. There is also a short exact replay on 12 orbits: let (a,w) denote scalar a and the number w of nonzero vector coordinates. Signed permutations act transitively on each orbit. Right multiplication by (2,σe_i) has scalar a'=2a+σv_i and new i-th coordinate −σa', with the other coordinates negated. Apart from loops and the transition to zero, the possible edges are (0,w)→(±1,w) for w>0 and (a,w)→(−a,w+1) for a≠0,w<3 and (a,w)→(0,w−1) for a≠0,w>0. Starting with (0,0),(1,0),(2,1), the new layers are (1,2); (2,3),(0,1); (0,2),(1,1); (2,2); (1,3). Orbit sizes for w=0,1,2,3 are 1,6,12,8. The missing orbits are (2,0),(0,3), as claimed. Nondegeneracy also gives simplicity: an ideal containing a nonzero pure vector contains the unit by pairing with a vector of nonzero inner product, and an ideal containing a nonscalar element with nonzero scalar part acquires a nonzero pure vector by multiplying by a vector orthogonal to its vector part.

## originality

PASS

The supported contribution is the form-specific all-length nonscalar obstruction and complete minimum-length census. The scalar obstruction is already known and receives no novelty credit. The strongest located related statements either change the underlying field/form or concern only products of two primitive idempotents.

## value

PASS

This is a concrete test of the field and form hypotheses in a motivated idempotent-generation problem. In the smallest odd field, this nonsplit spin factor has eight nonscalar elements that never occur and others that first occur at length six, in contrast to complete nonscalar generation within five for the split matrix form. The exact census identifies the boundary a finite-field extension must account for, not just that brute-force enumeration is possible.

The dated certificate retains the supplied scientific assessment, sources and limitations.
