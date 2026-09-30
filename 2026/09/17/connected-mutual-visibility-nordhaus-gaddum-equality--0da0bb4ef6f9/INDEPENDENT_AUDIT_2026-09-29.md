# Independent Audit — connected-mutual-visibility-nordhaus-gaddum-equality--0da0bb4ef6f9

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `f071ea56970f50cb221b1eba4afa9cb6c450f361`  
**Audited current source tree:** `f071ea56970f50cb221b1eba4afa9cb6c450f361`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` directory tree SHA exactly matches the assignment tree SHA. No intervening source change required a stale-source re-audit.

## Correctness — PASSED

PASS. The n-1 characterization is reversible: if S=V\{x} is a connected mutual-visibility set, any nonneighbor y of x must be universal in G-x, otherwise a nonadjacent y,z in S would require the impossible geodesic y-x-z; conversely the stated condition makes every nonedge of G-x visible through x. The complement therefore has a star component at x. The Nordhaus--Gaddum equality classification then follows by forcing the unordered parameter pair {n-1,n-2}, reducing the star degree to at most 1, and splitting r=1 and r=0. As an independent exhaustive check, I recomputed mu_c on every unlabeled graph in the NetworkX graph atlas through 7 vertices: there were zero mismatches with the n-1 criterion, and for n=5,6,7 exactly the four expected isomorphism families (two complementary pairs) attained equality.

## Originality — PASSED

PASS, NARROWLY. The introducing preprint proves the Nordhaus--Gaddum bounds and supplies a sharpness example, but its open full text does not classify the second-largest value n-1 or all equality cases. Targeted searches around the exact parameter, n-1, and the K_{2,n-2}/join families did not locate a prior theorem subsuming the record. Because connected mutual visibility was introduced only in September 2026, parallel or not-yet-indexed work remains the main priority risk.

## Scientific value — PASSED

PASS. A complete structural characterization of the second-largest value and the full equality classification strengthen a newly introduced invariant's extremal theory beyond a single sharpness construction. The theorem is general, short, and reusable in subsequent connected-mutual-visibility work.

## Independent checks

- independently rederived the n-1 complement-star criterion
- independently enumerated all unlabeled graphs through order 7 and found zero criterion mismatches
- reproduced exactly four unlabeled equality graphs for each n=5,6,7
- checked the source paper's Theorem 7 gives bounds plus a sharpness example but no equality classification
- verified current tree SHA and absence of 2026-09-29 audit markers

## Limitations

- The equality theorem is intentionally restricted to n>=5; small-order coincidences at n=4 are outside its statement.
- Literature priority is necessarily provisional because the invariant is extremely recent.
- The finite graph-atlas enumeration is supporting evidence, not a substitute for the general proof.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/17/connected-mutual-visibility-nordhaus-gaddum-equality--0da0bb4ef6f9
- https://arxiv.org/abs/2609.18877
