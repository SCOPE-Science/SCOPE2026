# Independent mathematical audit

## correctness

PASS

The domain is all central Euclidean plane sections of C=[−1,1]³∩{||x||₁≤2}, not translated sections. Independent signed-permutation symmetry reduces unit normals to nonnormalized (1,b,c), 0≤c≤b≤1. The source derives the full plane–facet chord formula and rewrites P(b,c) via M=(R₊+R₋)/2. Jensen’s inequality gives M≥sqrt[2(1+b+b²)], and the checked derivative bound makes H(M)=(b−c²)M+(1−b)²c²/M nondecreasing; the square-root chord bound then establishes a strictly positive transverse gap for c>0,b<1 because 4(1+b+b²)−(1+2b)²=3. The b=1 wall satisfies P(1,c)=2sqrt(2)+2sqrt(6+2c²), hence also cannot improve. On c=0 one gets P=4F(b) with exact second derivatives proving F″>0 on [0,3/5] and [3/5,1]; endpoint derivative signs are opposite, yielding the unique critical root and all equality normals. Independent section-plane intersections over 12,000 generic normals, nine boundary cases, SymPy exact derivative/positivity checks and 60-digit root solve corroborate formula and constants. Finite tests do not prove the continuum theorem; the global analytic inequalities do.

## originality

PASS

Best-of-knowledge noncoverage judgment after mathematical comparison with the complete closest primary papers (Kovič, König–Koldobsky, Yaskin and Stephen), four targeted Resultary searches, and focused web/constant queries. Related statements concern classification of solids, cube maximum-perimeter sections, uniqueness from complete section-perimeter profiles, or maxima among parallel translations—not a fixed cuboctahedron’s minimum over all central-plane normals. No matching classical exact extremum found, but absence from the index is not proof of historical priority.

## value

PASS

The regular cuboctahedron is a canonical Archimedean solid and perimeter of an origin-centered Euclidean plane section is a natural geometric invariant. The exact globally minimizing plane has a genuinely oblique normal, despite octahedral symmetry; the fully classified signed-permutation equality set and quantitative transverse rigidity distinguish perimeter from area and diameter invariants. The exact optimizer and stability are not a textbook corollary or an arbitrary slice computation and may be directly used in future extremal-section comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
