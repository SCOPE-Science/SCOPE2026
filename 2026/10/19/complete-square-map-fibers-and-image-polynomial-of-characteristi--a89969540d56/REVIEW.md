# Scientific review: complete characteristic-two graphical-group square-map fibers

## Correctness — PASS

In the explicit characteristic-two graphical-group coordinates, the square is exactly the central vector of edge products. The prescription of nonzero labelled edges forces the support endpoints to be nonzero and forbids zero-labelled internal edges. Vertices adjacent to the forced support are zero. On the other vertices, independent nonzero supports contribute the exact weighted independence polynomial. For each connected labelled support component, the map from nonzero vertex labels to edge products is a finite abelian group homomorphism, whose kernel has size \(q-1\) in the bipartite case and size one in the nonbipartite case because \(q-1\) is odd. Multiplying those factors proves the fiber formula. A disjoint decomposition by uniquely determined endpoint sets proves the square-image polynomial, and the identity fiber yields the element-order counts. These arguments do not extrapolate from finite tests.

The standalone executable exhausts all edge targets for 24 finite graph/field combinations over \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\), including direct group-square tests on small instances; every comparison passed. Limit: computational enumeration covers only finitely many instances.

## Originality — PASS, with residual priority risk

Rossmann's full open-access 2022 treatment of graphical groups (preprint arXiv:2107.05564, 2021-07-12) supplies the construction, conjugacy-class counts, and their graph polynomials, but the inspected mathematical sections do not supply the square-word fibers, their bipartite/odd-cycle dependence, or this square-image polynomial. Qiao's arXiv:2408.09963 studies totally isotropic subspace polynomials and group-theoretic abelian subgroups, principally the odd-prime exponent-prime setting; those enumerations neither state nor imply prescribed-square fibers over even fields. A published related graphical-group character-degree enumerator pertains to odd-field representations and does not cover characteristic-two element powers. Searches for directly matching square maps, edge-product systems, and involution counts returned no decisive dominating statement; negative search evidence is not a uniqueness proof.

Residual risk: an equivalent calculation might be implicit in older quadratic maps of class-two exponent-four groups or algebraic graph edge-product maps. Independent literature review remains warranted.

## Value — PASS

For every graph and every even prime-power field, the result completely determines a natural group-theoretic word-map fiber (including impossible targets), the image size, and the element-order distribution. The cycle-parity contrast gives an exact multiplicity distinction; the graph-polynomial square-image count is an additional complete invariant rather than a mere small-number table. The zero-fiber specialization connects those word-map invariants to graph independent sets. This is a natural family-wide classification, not an arbitrary parameter slice or previously known graph polynomial stated without its group-theoretic meaning.

## Closest sources and limits

- T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564; relevant group presentation and conjugacy-class structure read in the full-text open-access journal version.
- Y. Qiao, *A q-analogue of graph independence polynomials with a group-theoretic interpretation*, arXiv:2408.09963; relevant motivation, isotropic-subspace interpretation, and theorem read in full-text HTML.
- Published cycle-graphical character-degree enumeration, exact-title search hit: character degrees for odd \(q\), not element squares in characteristic two; only its publicly available title and summary were inspected.

The theorem's full generality rests on the displayed proof, not the finite checker. No historical uniqueness, external confirmation, or independent mathematical validation is claimed.

Self-review: passed. Independent audit: not yet performed.
