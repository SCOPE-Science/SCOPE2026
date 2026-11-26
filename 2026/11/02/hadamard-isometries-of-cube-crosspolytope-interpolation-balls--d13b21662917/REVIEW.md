# Independent mathematical audit

## correctness

PASS

A coordinate vector has norm max(1,1/s), while its normalized Hadamard image has norm max(1/√n,√n/s); equality is impossible for s<1 and forces s=√n otherwise. At n=2 the eight vertices (±1,±(√2−1)) and their swaps are permuted by the standard Hadamard reflection and signed coordinate permutations. At n=4 the orthant polytopes have zero-one vertices of support at most two; zero and singleton supports are nonextreme in the full symmetric ball. Each two-support signed vector is extreme: the two saturated cube coordinates and the ℓ₁ constraint force any endpoints of a midpoint representation to be that vector. Any pair of Hadamard columns agree on exactly two rows and disagree on two, so the normalized transform permutes the 24 vertices. For three distinct columns h_i,h_j,h_k, orthogonality makes the rowwise pairs (h_i h_j,h_i h_k) uniformly distributed over the four sign patterns, since all three nonconstant sign characters sum to zero. Thus U(e_i+e_j+e_k) has absolute coordinate 3/√n on n/4 rows and 1/√n on the rest. At s=√n this gives output norm 3/2 and input norm max(1,3/√n), yielding exactly the claimed lower bounds on the operator norm. The same pattern proves the Hadamard order divisibility used to exclude intervening dimensions, without asserting existence. check.py was inspected, not executed; its Sylvester tests do not establish arbitrary-Hadamard quantifiers.

## originality

PASS

The interpolation bodies, exceptional small-dimensional symmetries and critical scale are established ingredients. The qualitative higher-dimensional obstruction can also be obtained from the earlier polar vertex description by distance comparison. Credit the distinct quantitative conclusion: an explicit uniform norm distortion bound for every existing real Hadamard order at the uniquely possible parameter, not an exact operator norm or a general automorphism classification. The inspected same-body geometry and Hadamard literature do not give that bound.

## value

PASS

The known positive cases and forced parameter make the stability question natural: is failure outside these dimensions arbitrarily weak, or does a uniform witness separate every such transform from isometry? The three-column argument answers the latter with explicit constants independent of matrix equivalence or construction in higher orders. It adds quantitative information beyond the qualitative vertex obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
