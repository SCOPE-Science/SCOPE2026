# Independent mathematical audit

## correctness

PASS

For each blade K_m joined to a common hub, >=m-1 blade vertices must initially carry pairwise distinct colours: with two blanks no first leaf move can see q-1=m colours. With a seeded hub, every remaining leaf forces; with the hub blank it must be forced first, which fails exactly when all k blades omit the same one of the m nonhub colours. Each properly forced initial assignment has unique completed colouring. With (m+1)(m!)^k completions the seed polynomial equals (m+1)(m!)^k x^[k(m-1)] ((1+x)(m+x)^k-m), and minimum seed k(m-1) coefficient (m+1)(m!)^k(m^k-m)>0. Independent graph-based exhaustive initial-state counts for (k,m)=(2,2),(3,2),(2,3) gave respectively {2:24,3:96,4:60,5:12}, {3:144,4:480,5:432,6:168,7:24}, and {4:864,5:2160,6:1008,7:144}, agreeing with the derivation. The proof, not these small cases, covers all k,m>=2.

## originality

PASS

No prior examined theorem states or implies the clique-windmill all-k,m forcing polynomial. The combinatorial invariant is Farr's iterative local completion, not zero forcing or a unique-extension parameter. This is a best-of-knowledge claim only.

## value

PASS

The shared hub creates correlated missing-colour obstructions across k cliques; its m exclusions are not a product of single-clique formulas. Closed all-coefficient forcing and probability polynomials and the minimum successful seed for the natural generalized friendship family give reusable exact examples for a newly defined forced-colouring invariant, beyond a routine one-instance count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
