# Independent mathematical audit

## correctness

PASS

A chord between the jth and kth heptagon vertices has normal angle pi(j+k)/7 modulo pi, yielding exactly 14 signed normal rays; support is 1 at even indices and c=cos(pi/7) at odd ones. Moving any enclosing side inward until support cannot increase area. A bounded four-normal intersection requires all four cyclic gaps to be 1..6, giving exactly 511 subsets. For an active four-line polygon, the edge-length identity A=sum_[adjacent i,j](h_i h_j-(h_i²+h_j²) cos(delta_ij)/2)/sin(delta_ij) follows from intersections and 2A=sum h_i*edge_length_i. Redundant lines produce enclosing triangles with area >=3 sqrt(3)c²>4.05, while winners have area <3.5. The actual bundled exact-rational certificate was reconstituted byte-for-byte from inspected source (Git blob 559efa2bd82951909169b86a6d9ca25a530183b0) and executed successfully: interval Machin pi bounds, Taylor remainder enclosures, 511 exhaustive four-normal values, exactly seven all-odd gap-(2,4,4,4) winning sets, all other 504 formal values > winner+1/40, and 1.2588<ratio<1.2589. Independent 70-digit direct half-plane intersection/shoelace enumeration separately found 511 bounded patterns, seven active winners, seven redundant triangles, normalized winner ratio 1.2588037735470042164 and minimum actual alternative margin 0.02594731998604824>0.025. Winners circumscribe the heptagon inball of radius c with angle gaps 2pi/7,4pi/7,4pi/7,4pi/7; tangential polygon area gives c²(tan(pi/7)+3tan(2pi/7)). The normal-gap configurations form exactly one orbit of seven under dihedral symmetry; affine maps preserve inclusion/parallelism and area ratio. The high-precision numerical experiment alone is not an exact proof; the independent reading of the rational bounds and the original exact certificate establish the finite inequalities.

## originality

PASS

Best-of-knowledge PASS for the exact sharp value, seven equality quadrilaterals and strict 1/40 combinatorial gap. The identical model is introduced in Vígh (2026), which already provides the approximate heptagon ratio 1.2588, but his full article does not give the exact formula or equality/certificate theorem. The primary Hong et al. and Fodor–Grundbacher results and the published exact parallelogram record do not logically imply it. Classical unindexed geometry literature remains a real priority risk.

## value

PASS

The exact chord-constrained quadrilateral area of a regular heptagon is a natural geometric invariant in the new chord conjecture, not an arbitrary subtable. For the first odd vertex count after the settled pentagon case, an exact value and complete optimizer orbit offer a rigorous benchmark for future extremal methods; the >1/40 discrete gap identifies a structural separation of competing permitted tangent configurations. The numeric value was already known approximately, so mathematical value rests on exact proof, equality and rigor, not the decimal itself or a claimed general polygon theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
