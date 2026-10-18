# Scientific review

## Correctness

**PASS.** The support function is the positive weighted sum of coordinate-simplex supports. Its normal fan has a distinct vertex per hierarchical winner-side choice: uniqueness follows from equality in each positive summand's support inequality. For independent continuous ranks, the interleaving of two child orderings is independent of their internal permutations, so winner-side bits across the tree factor as independent Bernoulli variables with parameters determined by subtree sizes. The exact product collision follows. A lowest imbalanced node has perfect child subtrees of unequal power-of-two sizes, giving relative imbalance at least one third. The equality proof excludes non-root location via the forced sibling subtree and proves both sharpness and rigidity. The packaged exact checker verifies all tree shapes through six leaves by exhaustive score permutations and all shapes through eight leaves for the gap; the infinite proof does not rely on enumerations.

## Originality

**PASS, with residual bibliographic uncertainty.** The closest primary works are Colin Defant's *Fertilitopes* (arXiv:2102.11836), defining the integral binary nestohedron class, and Postnikov–Reiner–Williams's *Faces of Generalized Permutohedra* (arXiv:math/0609184), giving its cubical combinatorics and general normal fan/poset machinery. General fan descriptions can imply vertex cone angles once combined with linear-extension counts, so that mechanism is credited rather than asserted to be new. The present exact forbidden interval, its all-dimension equality characterization, and the sharp comparison of six-leaf full-tree realizations are not asserted in the inspected relevant sections. Published related work on fertilitope inradii and on graph-zonotope Gaussian collisions does not contain the same family-and-invariant claim. Queries under tree priorities, binary nestohedral angles, Pitman–Stanley normal cones, and geometric collision entropy found no dominating result. Earlier equivalent angle-gap inequalities expressed in random-tree language cannot be ruled out fully.

## Value

**PASS.** The invariant is the concentration of the isotropic direction-induced distribution on vertices, a canonical geometric characteristic of a combinatorial cube realization. The all-dimensional sharp gap says that an apparently continuously improvable measure of angular uniformity has a universal discontinuous rigidity threshold on this natural integral nestohedral class. Its equality family occurs in infinitely many dimensions and the six-leaf extremum demonstrates that locally balancing a tree may worsen angular uniformity. This is a structural geometric classification, not a numerical comparison at a chosen dimension.

## Scope and outstanding limitations

Positive internal simplex weights are essential. The result does not concern all nestohedra, all combinatorial cubes, or affine-transformed Euclidean metrics. The foundational normal-cone and cubical statements are existing results. The exact collision theorem has not received independent validation, and an equivalent result hidden under linear-extension or random-hierarchical-ranking terminology remains possible.

Self-review: passed. Independent audit: not yet performed.
