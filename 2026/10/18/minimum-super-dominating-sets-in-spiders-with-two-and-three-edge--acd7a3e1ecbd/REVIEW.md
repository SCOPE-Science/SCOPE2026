# Review of minimum super dominating sets in short-arm spiders

## Correctness — PASS

For \(a+b\geq3\), the proof treats all finite choices of black/white membership on arms of length two or three. With a black hub, the only possible one-black long arm is WWB and requires the hub to have precisely one white neighbor. With a white hub, every long arm requires at least two blacks and the hub must have a BBW or BBB arm (or a BB short arm). These statements are proved directly from the private-neighbor definition, not inferred from experiments. The resulting sharp lower bounds are matched by explicitly classified constructions. The four disjoint classes count to the formulas in RESULT.md. The accompanying executable independently reconstructs the underlying graphs and checks all minimum sets for 24 small profiles, then checks many larger constructed configurations.

## Originality — PASS, with residual risks

The nearest full-text article on super-domination enumeration (Ghanbari, Jäger, Lehtilä, 2022/2024, arXiv:2209.01795, §§6–7) counts minimum sets in paths, cycles, friendship graphs and a few other families, and proposes enumerating minimum sets in trees as a question. Bujtás, Ghanbari and Klavžar (2023, arXiv:2302.08862, Theorem 3.1) settle the *numerical value* of super domination for every tree via maximum matchings; that known theorem subsumes the minimum-cardinality part here but does not enumerate the sets or imply their exact multiplicity by itself. A published result on one-leaf coronas is not applicable because the spiders here have no leaf adjacent to the hub, whereas coronas require a private leaf at each base vertex. Searches for spider/starlike-tree enumeration, exact formula aliases, polynomial coefficients and the two arm-length parameters found no covering statement. Mere absence from search results is not a proof of uniqueness.

A relevant 2024 work of Kaidash, *Super Domination Polynomial of a Graph* (DOI 10.1007/978-3-031-73365-9_6), gives formulas for unnamed families in its accessible abstract. The full chapter could not be read; there remains a genuine possibility of a previously known special coefficient. This is an identified bibliographic risk, not a claim of negative full-text evidence.

## Value — PASS

Counting all optima in trees is a directly stated research direction of the 2022 enumeration paper. The two-/three-edge spider family is a natural labeled two-parameter subclass of trees, not an arbitrary numerical slice. The result yields a complete structural classification and explains the nonobvious phenomenon that the number of minimum configurations ceases to depend on the number of length-two arms as soon as one length-three arm is present. It separates the known minimum numerical invariant from previously unaccounted multiplicity and supplies a reusable local-arm method for longer subdivisions.

## Boundaries

The theorem does not address length-one or length-four-plus arms, general tree enumeration, or all coefficients of the super domination polynomial. Its theoretical correctness depends on the explicit case analysis in RESULT.md, not on the finite verification runs. Unindexed prior results and the inaccessible 2024 chapter remain limitations.

Self-review: passed. Independent audit: not yet performed.
