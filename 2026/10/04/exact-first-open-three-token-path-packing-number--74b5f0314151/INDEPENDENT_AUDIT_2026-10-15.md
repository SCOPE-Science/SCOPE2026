# Independent mathematical audit

## correctness

PASS

For the path P_13 and three indistinguishable tokens, each vertex is an increasing triple 1≤i<j<k≤13. Adjacent token movement preserving order gives exact shortest-path metric d((i,j,k),(i',j',k'))=|i-i'|+|j-j'|+|k-k'|: every move changes one rank coordinate by 1, and ordered monotone routing realizes that sum. A graph packing corresponds to selecting triples at distance at least 3; equivalently an independent set in the distance≤2 conflict graph. Independently enumerated all C(13,3)=286 triples and all 2255 conflicting unordered pairs, built the binary integer optimization with x_u+x_v≤1 for every conflict and 0≤x_u≤1 integer. An entirely separately written SciPy/HiGHS model terminated with optimal objective 52, dual bound 52 and 0 reported MIP gap in 10.74 seconds, and extracted 52 pairwise distance≥3 codewords; the source contains its own explicit independent 52-element witness and complete verifier, also inspected. Thus finite n=13 exactness is supported by both a concrete lower witness and a complete finite optimization of the defined graph, not extrapolation from small n or a timeout. Solver arithmetic/tolerance is a residual computational-certification qualification, not a claim of a symbolic general n upper-bound proof.

## originality

PASS

Best-of-knowledge PASS for the first open value ρ(F_3(P_13))=52, rather than the known weight-two code problem or known n≤12 weight-three table. The direct 2024 source states exact weight-three n≤12 and lower/upper bounds 50 and 54 for n=13; this exact value is NOT in the table. Related OEIS A085684 lists the constant-weight triangle only for smaller n, while A085680 is weight two and cannot imply weight-three length 13. Exhaustive exact computational result has a meaningful published open boundary even though it is finite.

## value

PASS

Length 13 is exactly the FIRST uncomputed three-token path packing case following a published exhaustive n≤12 census; direct 2024 bounds 50 and 54 make its exact value a natural unknown structural graph invariant, not an arbitrary parameter. Closing that four-unit published gap has standalone coding-theoretic and extremal graph value even without an asymptotic formula or a general classifying theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
