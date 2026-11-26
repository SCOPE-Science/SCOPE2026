# Independent mathematical audit

## correctness

PASS

The projective action exhausts the nonzero 15-bit forms. On each affine chart the ideal of the equation and its two derivatives detects geometric singularity exactly. A smooth plane quartic has no line component, and the first nonzero coefficient of the tangent restriction in a local parameter gives the claimed contact order. Independent replay: run python3 /workspace/reproductions/audit_quartics_f2.py with the frozen quartic package directory as its argument. It enumerates all masks directly by binary linear conditions for singularity at points over fields of orders 2, 4, 8 and 16. This cutoff is exact: an absolutely irreducible singular quartic has sum of geometric delta invariants at most three by the genus formula; a reduced reducible quartic of component degrees (3,1) or (2,2) has a Frobenius-stable intersection scheme of length at most four, of degrees (2,1,1) has a rational intersection of its two lines, and of degrees (1,1,1,1) has Frobenius orbits of pair intersections of size at most four. In the nonreduced case a unique repeated component is a rational line or conic with a rational point, or the two repeated lines intersect rationally. A separate elementary-generator orbit traversal and a 21-flag tangent-restriction calculation matched all 34 histogram rows and all 78 representative masks, sizes and contact data in both the TSV and JSON, with 279 orbits in the ambient nonzero space and 10,920 smooth equations. The stated weighted totals, extrema, and the two exceptional single orbits all match.

## originality

PASS

Pass applies to the joint ordinary-flex-sensitive 34-profile classification, not the previously classified set of curves, the hyperflex bound, the 28-equation orbit, or the joint point-count/hyperflex marginal. Prior work that counts theta contacts does not determine the ordinary-flex count even at a fixed full theta profile. The full enumeration after refining by ordinary tangent contact was not found in the compared earlier results.

## value

PASS

This is a complete joint distribution of natural local tangent contacts on the smallest-field smooth canonical quartics. The ordinary-flex refinement separates examples that have identical theta profiles and supplies exact simultaneous possibilities and incidence totals, useful as small-field arithmetic benchmarks beyond the known hyperflex extremum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
