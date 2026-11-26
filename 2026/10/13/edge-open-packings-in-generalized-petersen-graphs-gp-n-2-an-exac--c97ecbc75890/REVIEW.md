# Independent mathematical audit

## correctness

PASS

For n≥9, writing each endpoint index as its column plus an increment in {0,1,2} shows that any third-edge conflict gives a signed column difference in [−4,4]. These residues are distinct for n≥9. Listing the possible endpoint types and excluding the two selected edges gives exactly the forbidden-pair table, with both orientations at offset zero. A four-column state therefore records all the history needed to test a new mask; a cyclic packing gives a closed walk, and conversely such a walk of length n≥9 supplies a packing. The sum around a closed walk of h(s)−h(t)≥9w−7 gives 9|F|≤7n. The nine base walks of lengths 9–17 all return to (2,4,0,6); concatenation with the length-nine walk adds seven edges and preserves all junction constraints, giving attainment in every residue class. For 5≤n≤8, fresh exact independent-set recursion on conflicts built from the actual graph returned 3,4,5,6 (the recursion exhausts whether a chosen vertex belongs to the set). The independent script fresh_gp_repro.py in /workspace/branches/75436585-d2d9-4cd5-8ec6-a86ea2d2087b/ also reconstructed the 120 states and verified all 291 exact potential inequalities, checked table agreement on eight orders and validated the thirteen base words. The finite certificate and proof, not the recorded pumped examples in verification_output.txt, establish the infinite formula. The uploaded verifier was inspected, not run.

## originality

PASS

Credit the known Petersen value at n=5. The supported distinct contribution is the sharp family-wide formula with attainable residue classes and integer upper certificate. The closest same-family indexed records measure a different invariant; the closest same-invariant periodic record concerns a different family. Inspected general bounds and tests do not yield the claimed formula without new family-specific work.

## value

PASS

GP(n,2) is a standard cubic family, and allowing mutually incident edges gives a packing problem not answered by induced matching or the cubic upper bound. The precise floor law quantifies the linear deficit from that bound, and the matching finite certificate and constructions explain the nine-column structure across all orders. It gives a usable exact benchmark for packing bounds and algorithms on this family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
