# Independent mathematical audit

## correctness

PASS

I independently enumerated undirected edge-subset forests, then chose one root in every component and oriented towards it. Face counts 24,234,1192,3357,4968,3024 and F2 boundary ranks 23,211,981,2376,2592 agree. The rational ranks are at least these ranks; the first rank is at most 23 by augmentation, and adjacent ranks saturate the intervening chain dimensions, so the ranks over Q are equal and reduced homology is solely degree five, dimension 432. For an independent trace check, an invariant forest chooses parents on vertex cycles: a length-d tail cycle can choose an opposite-shore length-e parent cycle if e divides d, with e offsets. The orbit-parent digraph is acyclic exactly when its lift is acyclic. Each chosen tail cycle contributes -1 to the alternating signed-face weight, so in odd top degree the character is the sum of products of -e including the empty choice. This gives (432,-16,4,0,-2), (0,0,4,0,-2), (-3,-1,1,-3,1). Specht inner products by permutation, signed-standard and two-subset characters give (2,8,7,9,4), (5,17,12,19,8), (2,8,6,10,3), including two invariants. Independent replay: python -B /workspace/review_evidence/3_forest.py; output 3_forest.txt. Submitted verifier was inspected, not executed. The conclusion concerns rational representations, not integral lattices.

## originality

PASS

The 432-sphere wedge is prior. The supported distinct content is the actual full top action for the unbalanced K3,4 parameter. The inspected foundational theorem and narrower complete-bipartite results lack a statement that supplies it. Decision is conditional on the bounded literature evidence, not a priority certification.

## value

PASS

For a canonical small unbalanced bipartite graph, the full character refines a known wedge and is a concrete test for general automorphism formulas in rooted-forest homology. It resolves which actions occur on the classes, with all fifteen irreducibles present and exactly two trivial summands, neither supplied by the known Betti number. The useful result is the evaluated invariant, not the generic trace method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
