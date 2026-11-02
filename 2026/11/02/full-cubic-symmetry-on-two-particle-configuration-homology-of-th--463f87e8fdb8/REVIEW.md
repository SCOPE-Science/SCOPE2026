# Review: full cubic symmetry on two-particle configuration homology

## Correctness (PASS)

The claim concerns the unordered configuration of two distinct points in the geometric cube graph. The published stable-equivalence criterion makes its compact disjoint-cell configuration complex homotopy equivalent to the continuous configuration space. The natural inclusion is equivariant, so the group representation is preserved on rational homology. The exact cellular data are \((28,72,42)\) cells and integer boundary ranks \((27,39)\); the independent mod-two computation agrees. The script checks all \(48\) group actions against both differentials, reconstructs every image of a rational top cycle, and verifies the full characters of the displayed irreducible modules. Rational finite-group transfer proves the quotient assertions. Limit: neither integral first-homology torsion nor the quotient fundamental group is classified.

## Originality (PASS against inspected literature)

The closest foundations are Prue–Scrimshaw's cubical stable-equivalence theorem, An–Maciazek's three-connected planar braid presentations, and the subdivisional configuration chain models of An–Drummond-Cole–Knudsen. None of their inspected relevant claims gives the two complete \(B_3\)-homology modules of the three-cube. Other published equivariant two-particle calculations concern different graph objects (notably the cuboctahedron and dodecahedron), whose homology characters do not imply the cube-graph answer. A 2026 stable-representation paper lists other graph families in its abstract; its inaccessible full text remains an explicit risk. Search failure is not proof of uniqueness; unindexed equivalent work remains possible.

## Value (PASS)

The cube is a canonical three-connected planar test graph with the full signed coordinate group \(B_3\). Its two-particle second homology is the irreducible geometric coordinate module; its first homology splits into a \(3\)-dimensional, \(2\)-dimensional and orientation-character summand. The distinction between the rotational quotient retaining one rational first-homology class and the full quotient retaining none cannot be recovered from Betti numbers or non-equivariant braid presentations. This provides a motivated, natural complete classification for the first genuinely three-dimensional cube graph.

## Sources and limits

See RESULT.md for primary citations, AUDIT.json for the actual semantic comparisons and source inspections, and check_cube.py for an independent executable finite calculation. Only rational homology representations and their rational quotient consequences are claimed.

Self-review: passed. Independent audit: not yet performed.
