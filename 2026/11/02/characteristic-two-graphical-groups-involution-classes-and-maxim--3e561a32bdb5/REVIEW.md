# Scientific review: characteristic-two graphical-group torsion

## Correctness — PASS

The central formula is derived from an explicit, associative bilinear group cocycle, not inferred from a computational pattern. In characteristic two the square of \((x,z)\) has edge coordinates \(x_i x_j\); it vanishes precisely for independent vertex support. For such support, the commutator image is a direct sum of one-dimensional field images indexed by distinct exterior neighbors, proving the exact class-size exponent \(|N(S)|\). The subgroup classification uses the elementary fact that a vector space is never a union of two proper linear subspaces, followed by inclusion-exclusion on coordinate support. Any elementary abelian subgroup extends by the central edge subgroup, proving the *global* maximal-subgroup classification. The formulas are valid in the edgeless and disconnected cases, including extension fields of characteristic two.

The bundled Python verifier exhaustively enumerates all two-, three-, and four-vertex graphs over \(\mathbb F_2\) and all two- and three-vertex graphs over \(\mathbb F_4\); the 84 graph-field cases independently verify squares, conjugacy sizes, full rank census for subgroups above the edge center, and maximal-rank multiplicities. These finite checks support, but do not replace, the proof.

## Originality — PASS, relative to inspected evidence

Rossmann, arXiv:2107.05564, supplies the defining graphical groups and the **unrestricted** conjugacy-class-size polynomial. These do not themselves record the joint order-two/class-size distribution or the classification of the *elementary abelian* subgroup orders in characteristic two. Qiao, arXiv:2408.09963, proves general totally-isotropic subspace counts and connects them to abelian subgroups in **odd-characteristic exponent-prime** groups; that subspace-isotropy condition is weaker than the quadratic zero-square condition required in characteristic-two exponent-four graphical groups. The statement-to-statement comparison therefore distinguishes the candidate from both works rather than relying on differences of terminology.

Additional searches for involution conjugacy classes, graph quadratic maps, maximal elementary abelian subgroups, and equivalent independence-polynomial formulations did not identify a theorem with this complete characteristic-two statement. This is a bounded best-knowledge comparison, not a proof of first publication. A general treatment of exponent-four graphical or quadratic-map groups could yield an equivalent statement implicitly; this remains a residual originality risk.

## Mathematical value — PASS

This is an exact structural classification for every finite graph and every characteristic-two field. Involutions and their conjugacy classes are canonical group invariants, while the sizes and number of maximal elementary abelian subgroups are natural measures of the elementary two-local structure of exponent-four groups. The result identifies a precise graph-to-group dictionary: independent vertex sets govern square-zero elements, exterior neighborhoods govern their conjugacy sizes, maximal independent sets govern all maximal elementary abelian subgroups, and graph well-coveredness is equivalent to equicardinality of these maximal subgroups. The full Gaussian rank transform is a motivated enumeration of every subgroup above the canonical edge center. These are not claims about arbitrary subgroups or about fields of odd characteristic.

## Boundaries and risks

The rank census does not include elementary abelian subgroups **avoiding** the edge center, although every inclusion-maximal elementary abelian subgroup necessarily contains it. Non-elementary abelian subgroups and full character tables are outside the claim. Priority remains provisional given possible equivalent results in general class-two exponent-four group theory. No independent mathematical audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
