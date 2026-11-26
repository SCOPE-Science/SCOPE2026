# Independent mathematical audit

## correctness

PASS

On the radius-sqrt(3) representatives, restrictions through degree three are spanned by homogeneous cubics on the odd side and homogeneous quadratics on the even side. I recovered ranks 10 and 6 and independently checked the reported determinants 1024 and 32 in the original bases. Exact dot products give the disjoint-edge Petersen graph on the ten axes; a freshly found labeling identifies the five centered edge-coordinate columns as spanning the antipodal-even left kernel (rank four and exact orthogonality to the even evaluations). Deleting rows subtracts the number erased and adds the rank of the kernel projected to those rows. For the unsigned incidence matrix, the left kernel gives one alternating vector per bipartite component, including an isolated vertex; centering loses a dimension exactly when every such vector has sum zero. This proves the formula for all T, including the empty and full sets. Independent exact computation over Q(phi) checked all 1024 touched-pair patterns by direct even-block ranks (each represented retained pair gives one independent odd row) and verified ranks 14/15/16 with counts 45/1840/2960. Replay: python3 /workspace/branches/independent_dodecahedron.py (SymPy). The corresponding rank-four failures on four distinct axes are the 15 four-cycles and 10 triangle-plus-disjoint-edge sets; repeating an axis cannot give four independent kernel rows.

## originality

PASS

The inspected literature and published records contain parity and Gale-dual erasure methods, and substantial prior spectral information on the very same dodecahedral axes. The supported distinct result is the bandlimited all-deletion rule for individual vertices, in particular the centered unsigned K5 incidence criterion and its four-erasure census. None of the closest inspected statements supplies that criterion or determines the census without further work. This is a best-of-knowledge judgment, not global priority.

## value

PASS

For reconstruction of degree-at-most-three data on a canonical oversampled spherical grid, the issue is not one invertible sixteen-node choice but which missing-node patterns preserve information. The result turns every exact rank decision into a five-vertex balance criterion and explains the two forbidden four-axis configurations; it is more than redoing a determinant table. It makes no numerical conditioning or perturbation claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
