# Independent mathematical audit

## correctness

PASS

For a connected graphical zonotope, vertices correspond to acyclic orientations; maximal normal cones are transitive-closure order cones, whose irredundant facets correspond to Hasse cover edges (established Postnikov–Reiner–Williams). A directed cycle occurs precisely with two wholly directed terminal paths in opposite directions. In any acyclic orientation, alternate directed path for an edge on arm i can only use a whole other arm, so a redundant edge occurs precisely when a separate fully directed arm supplies a common direction and arm i has exactly one same-direction edge. This yields the three-way per-arm product enumerator; subtract all noncomplete cases, multiply both common directions, add no-complete orientations. Hasse cover graph is connected with V-1=E-t+1 minimum edges; equality means a spanning tree. Oriented incidence vectors of a tree are an integral basis, proving cone regularity, not just simplicity; thus smooth iff r=t-1. Fresh independent exhaustive topological sorting and deletion-DFS transitive-edge counts matched (2,2,2)=(10,12,24), (2,2,3)=(32,38,32), (2,3,4)=(256,154,52), (2,2,2,2)=(18,16,48,64), with predicted last coefficient smooth. Package checker contains nine finite tests; finite checks supplement general proof.

## originality

PASS

The poset/Hasse facet criterion and global graphical-zonotope simplicity classification were published by Postnikov–Reiner–Williams; the present exact distribution and smooth-orientation parameterisation over arbitrary generalized-theta arm lengths are not that standard criterion alone. Grujic counts global face numbers rather than local incident-facet degree per vertex. The K_(2,t) length-two specialization is known boundary prior art and not separately claimed.

## value

PASS

The full local facet-profile polynomial and explicit smooth toric fixed-point locus turn a general criterion into an exact natural graph-family classification. The invariant distinguishes the fixed-point singularity profile over arbitrary arm subdivisions, beyond just the total face polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
