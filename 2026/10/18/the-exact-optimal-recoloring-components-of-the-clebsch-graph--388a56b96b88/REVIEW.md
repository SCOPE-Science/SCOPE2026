# Review of the Clebsch optimal-recoloring classification

## Correctness — PASS

The graph is defined by its full 16-vertex adjacency relation. Every proper four-coloring arises in exactly one branch of the depth-sixteen recursive enumeration, and no improper full tuple is admitted. Both complete computations recover 28,560 states, 57,600 single-coordinate edges, and the stated degree and component distributions, with exact all-source BFS diameters on all 960 nontrivial components. The second verifier uses a separate antipodal quotient construction and dictionary membership for legal moves; this distinguishes it from the first verifier's bitwise generator and neighbor-color test. The symmetry generators are checked against every graph edge and their component orbits are fully traversed. An exhaustive independent-set scan gives independence number five, proving four is the minimum palette. The exact source files and their outputs are included in the same package.

## Originality — PASS, qualified

The 28,560 coloring count is already present in OEIS A159056 and **is not claimed as new**. The full inspected texts of Cereceda–van den Heuvel–Johnson, Bonsma–Cereceda and McDonald provide general recoloring connectivity and complexity rather than this exact 16-vertex component spectrum. The 2025 chromatic-pairs paper supplies an edge-count framework, not this connectivity classification. The abstract of Beier and coauthors' 2016 article addresses allowable coloring graphs; its complete text could not be inspected and is a residual risk. Targeted source and mathematical-record comparisons did not identify the component sizes, all-source diameters, or two distinct frozen symmetry orbits. This is a best-knowledge overlap assessment, not proof of worldwide priority.

## Value — PASS

At the chromatic palette size, single-site recoloring defines a canonical finite-state dynamics; both reachability and absorbing states matter. The complete decomposition of a canonical triangle-free, four-chromatic, strongly regular graph exhibits thousands of inequivalent communicating classes, a uniform nontrivial component shape, and two structurally different frozen orbits. These facts are not implied by the known total coloring count or by generic recoloring connectivity bounds, and supply a reproducible exact test case for chromatic reconfiguration.

## Boundaries and risks

The proof is finite and does not establish any behavior for an infinite Clebsch-related graph family or for larger palettes. The inaccessible complete 2016 classification and unindexed historical computations remain possible originality risks. Claims of independent peer verification are not made.

Self-review: passed. Independent audit: not yet performed.
