# Independent mathematical audit

## correctness

PASS

For a 3-of-4 committee omitting x, a JR-violating unrepresented group must be singleton-x voters, yielding iff condition 3 h_x e_x < n (equality violates). Sort h_a>=h_b>=h_c>=h_d. If omitting d violates, its singleton mass e_d>=n/(3 h_d) while e_d<=n-r, so h_d>=q=n/[3(n-r)]. If omitting c is safe, drop at most (1-q)/3 relative quality; otherwise e_c+e_d<=n-r forces 1/h_c+1/h_d<=1/q, giving h_c>=2q,h_d>=q/(1-q) for q<=1/2. Omitting b is then necessarily safe, and the final bound follows from nonnegative polynomial 2q^3-2q^2+4q-1 for q>=1/3 (value 5/27 and positive derivative). If 3r>=2n, top-three is safe except all-unit tie at equality, when some alternative full-quality omission is safe. Construct r joint top-three voters and n-r singleton-low voters with minimal supplemental approvals to saturate h_d=q and attain (2+q)/3. Independent exact rational exhaustive check of 200,000+ small electorate/grid ballot-quality instances n=2,3 passed, plus analytic boundary-polynomial verification; finite grid does not prove real-quality quantifiers.

## originality

PASS

Boehmer–Dong–Kreisel–Utke 2026 establish a general reciprocal JR quality guarantee, tight examples and related two-seat constructions. The primary manuscript Sections 2/5/Appendix G were read: no exact 3-seat 4-candidate n,r support-density frontier identified. The older ordinary-JR welfare-price theorem treats another axiom/objective. The new result is a complete constrained rJR quality frontier, not a claim to invent rJR or its 3/4 guarantee.

## value

PASS

Sharp parametric price of the first nontrivial rJR exclusion among four quality-scored candidates, including a support-density phase transition at 3r=2n and exact elections attaining the loss. It substantially strengthens a coarse universal 3/4 retention bound under natural support assumptions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
