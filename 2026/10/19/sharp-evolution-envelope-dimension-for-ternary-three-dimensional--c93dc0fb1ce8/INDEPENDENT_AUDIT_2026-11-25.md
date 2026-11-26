# Independent mathematical audit

## correctness

PASS

The free product columns e₀²,e₀e₁,e₁² give exactly 3⁹ labeled tables. The odd-characteristic unital envelope rank is the least number of squares spanning the three coordinate quadrics: polarization recovers multiplication and the map of their linear forms is injective because a vector annihilated by all forms would multiply every vector, including 1, to zero. Conversely an ideal embedding in a natural basis gives a symmetric multiplication decomposition from every coordinate nonzero on the ideal. Six projective squares of coordinate forms and their pairwise sums span the full quadric space. I reproduced the census independently without the bundled conic-incidence test. Replay: normalize the 13 projective triples by their first nonzero coordinate and form their square rows (x²,xy,y²,xz,yz,z²), using half-cross-term coordinates. For each of the 1287 five-row subsets take the signed 5×5 deletion minors of the resulting matrix modulo 3; retain and normalize the nonzero vectors. This yields 78 distinct hyperplanes, and every span of at most five squares extends to one of them. For each normal (a,b,c,u,v,w) mark all tables whose output-coordinate triples (Aᵢ,Bᵢ,Cᵢ) satisfy aAᵢ+bBᵢ+cCᵢ=−u,−v,−w for i=0,1,2 respectively. Separately enumerate all 19683 tables and compute the three-by-three determinant of (xe₀,xe₁,x) for the 13 projective x. The complement of the marked tables is identical to the determinant-nonzero set, of size 288. Enumerating each ordered (p,q) with det(p,q,1)≠0, rewriting the three products in that basis, gives two disjoint 144-element sets from the displayed representatives, exhausting the 288. Basis-triple associators select exactly the second orbit, whose associative division law identifies F₂₇. As a separate lower-bound check, a symmetric decomposition of a division product into at most five terms would map x injectively into a ternary length-five linear code of dimension three and minimum distance at least three: each nonzero x must activate at least three rank-one terms. The disjoint radius-one balls would require 27·11>3⁵ code positions.

## originality

PASS

Credit the earlier rank reduction and uniform bound, and do not claim that the two division-algebra types or the associative example are themselves new. The distinct supported content is the exact sharp envelope locus among all fixed-unit ternary tables, its equivalence with division, and the resulting labeled and unital orbit census as a sharpness classification.

## value

PASS

The count is tied to a motivated sharpness question for a concrete embedding dimension. It specifies all extremal ternary multiplication laws, and identifies division as the exact distinguishing condition, rather than finding an isolated high-rank field example or simply recounting known algebra types. The nonassociative witness and exclusion of nondivision tables give the census structural content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
