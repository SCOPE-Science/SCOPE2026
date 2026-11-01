# Review of the octahedral maximal-norm result

## Correctness — PASS

The ball structure on the octahedron is explicit (one, five, or six vertices). Independent row-radius choice reduces the unrestricted real-input norm to the maximum singular norm of 729 nonnegative rational matrices. A standalone integer-only checker establishes 726 strict positive-definiteness certificates at squared level \(141/100\); each of the three remaining matrices is handled analytically by an orthogonal two-by-two block reduction, with unique top eigenvalue \((21+6\sqrt6)/25\). Direct substitution verifies that the positive top eigenvector activates exactly its chosen ball radii. The proof then obtains every equality case from simplicity and separation. The checker was executed on its actual packaged source.

## Originality — PASS, qualified

The relevant primary literature was inspected beyond abstracts: arXiv:1410.6204 (graph-ball definitions, the general strong/weak results, four-vertex examples and star cases); arXiv:2005.03146 (Theorem 4, Corollary 5, and the strong \(\ell^2\) proofs for complete graphs and stars); and arXiv:2011.02630 (strong-type sections and its star/complete-graph results). Their statements are not equivalent to, or stronger than, this octahedral exact strong \(\ell^2\) statement. Focused queries under the aliases octahedral graph, complete tripartite \(K_{2,2,2}\), cocktail-party graph, and the exact radical found no covering primary result. These negative searches do not establish global uniqueness; equivalent earlier calculations could be unindexed. Accessible earlier internal mathematical claims were checked for overlap separately without changing or reassessing their content.

## Mathematical value — PASS

The octahedral graph is the unique six-vertex four-regular simple graph, the one-skeleton of a Platonic solid, and the first three-pair matching-complement graph. Its intermediate centered ball omits exactly one antipode, producing a different stability geometry from the complete-graph and star cases. The exact strong \(\ell^2\) constant, full rigid equality pattern, and strict increase over the established complete \(K_6\) value settle a natural sharp invariant on this canonical object. A finite graph is not dismissed solely for its size: here the exact constant is motivated by a named symmetric graph and distinguishes the location of maximizing mass. The method's 726 strict certificates are mathematical evidence, not themselves the value claim.

## Closest work and limits

The strongest directly applicable published comparison is González-Riquelme--Madrid's complete-graph formula, yielding \(\sqrt{4/3}\) for \(K_6\). Soria--Tradacete's bounds and four-cycle example do not give this exact octahedral constant. The work concerns only the unweighted six-vertex graph and the centered real strong \(\ell^2\) norm; larger matching complements and other measures remain open here. Priority uncertainty and lack of independent review remain.

Self-review: passed. Independent audit: not yet performed.
