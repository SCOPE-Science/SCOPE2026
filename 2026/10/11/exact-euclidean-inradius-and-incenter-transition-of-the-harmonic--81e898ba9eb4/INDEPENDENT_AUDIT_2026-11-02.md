# Independent mathematical audit

## correctness

PASS

Verified the actual pinned RESULT.md proof and immutable Git tree 5149c51e0f88940e9020d427dfe02fee90ed11cb. Ardila--Escobar Proposition 3.8 has exactly the two affine sums C_n=n(n+1)/2+1 and 3^n-3 minimal bisubset facets. Projecting x_i=1 and y_i=1 normals onto the codimension-two affine tangent space gives length sqrt((n-1)/n); summing the shifted coordinate-facet inequalities yields r<=(mu_n-1)/sqrt((n-1)/n) and forces the unique uniform center at equality for n>=3. For any bisubset, with w=|S cap T| and d=|S\T|-|T\S|, the independently derived Q=n^2-w^2-d^2 satisfies projected norm^2=Q/(2n), uniform-center slack=Q/4+w/n and distance sqrt(nQ/8)+w sqrt(2/(nQ)). For w>=1, Q>=2w(n-w)>=2(n-1)>4w/n; the distance increases with Q and w so its unique equality class is w=1,Q=2(n-1), exactly 2n coordinate facets. For w=0, Q>=4(n-1), giving strictly larger distance for n>=3. At n=2 six facet distances have a diagonal pair summing to 2; radius 1 forces p=q and coordinate distances give |p|<=1-1/sqrt(2). Independently checked both symbolic identities with SymPy; enumerated all bisubsets (3^n-3) for n=2..8 using exact fractions, confirming formula and active counts; solved the independent Chebyshev linear program for n=2..5 with expected optima. These tests corroborate, not substitute for, the arbitrary-n proof.

## originality

PASS

Best-of-knowledge originality of the precise harmonic-polytope intrinsic Euclidean inradius, complete center locus and contact-facet classification. The first source gives the exact H-description but not its Chebyshev optimization. Same-object published vertex-shell/circumradius and simple-vertex results do not imply inscribed-ball data. A closely analogous bipermutahedron inball theorem concerns different supporting offsets and cannot be transferred by the known Minkowski relationship. Direct aliases, database and primary-source searches located no independent prior theorem covering the final claim; the target itself appears in Resultary as its own published mirror, not as independent antecedent. This is not an exhaustive novelty certificate.

## value

PASS

The harmonic polytope is a standard, independently motivated Minkowski-sum model arising in matroid conormal geometry. Its largest intrinsic Euclidean ball is a natural exact metric invariant not recovered from known face and volume formulas or from its vertex-shell circumradius. The final theorem provides an all-rank closed form, uniqueness for n>=3, an unexpectedly small 2n-contact subset of 3^n-3 facets and the rank-two positive-dimensional center locus. The global slack minimization and sharp boundary behavior are mathematical structural facts plausibly useful to geometric researchers, not a textbook relabeling or unmotivated finite sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
