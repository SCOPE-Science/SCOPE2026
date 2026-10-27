# A delta-invariant obstruction to the claimed cusp–two-node degeneration

## Finding

In the preprint *Equisingular Deformations of Curves and Surfaces in Threefolds* (arXiv:2603.01540v1), the local description in Proposition 4.1 and the global argument in Theorem 4.2 assert that a cusp can be replaced equigenerically by two ordinary nodes. This cannot hold as stated. An ordinary cusp has local delta invariant \(\delta=1\); an ordinary node also has \(\delta=1\), so two nodes contribute \(\delta=2\). An equigeneric deformation preserves total delta.

Consequently, if a reduced curve has exactly \(\kappa\) ordinary cusps and no other singularities, its total delta invariant is \(\kappa\). A nodal curve in the same equigeneric stratum therefore has exactly \(\kappa\) nodes, not \(2\kappa\). This is a statement-specific obstruction to the claimed cusp-to-two-node mechanism, not a claim about every other result in the preprint.

## Assumptions and scope

Work over an algebraically closed field of characteristic zero with reduced plane curves and their local analytic singularities. “Equigeneric” means that the total delta invariant is constant in the family. For a curve with other singularities, the count applies to the sum of delta invariants over all singular points; the \(\kappa\)-node conclusion above assumes exactly \(\kappa\) cusps and no other singularities on the initial curve.

## Proof

1. For a reduced plane curve singularity, \(\delta\) measures the length of the quotient of the normalization sheaf by the local ring. It is additive over distinct singular points.
2. The ordinary cusp \(y^2=x^3\) has \(\delta=1\), and the ordinary node \(xy=0\) has \(\delta=1\).
3. Thus a single cusp and a pair of nodes have different total delta invariants, respectively \(1\) and \(2\). They cannot be the two fibers of an equigeneric local deformation with no additional singularity contribution.
4. For a global curve with \(\kappa\) cusps and no other singularities, the total is \(\kappa\). Since each node contributes one, a nodal member of that same equigeneric stratum has \(\kappa\) nodes. This contradicts a replacement of every cusp by two nodes, which would give \(2\kappa\) nodes.

No numerical experiment is needed: the contradiction follows exactly from the definition of the invariant and the two local delta values.

## Verification

The cited preprint was read in full-text form at the relevant passages: Proposition 4.1 and its proof (PDF pages 9–10), Theorem 4.2 and its proof (PDF page 10), and the definitions of the plane cuspidal locus and its delta bound (PDF page 11). Those passages state that an ordinary cusp has \(\delta=1\), but also describe two nodes as replacing each cusp while preserving equigenericity. The invariant counts above reproduce the contradiction. The statement is limited to that implication; no independent audit has been performed.

## Relationship to prior work

The primary comparison is the preprint by Mounir Nisse, *Equisingular Deformations of Curves and Surfaces in Threefolds*, arXiv:2603.01540v1, first publicly posted on 2026-03-02. Its own text identifies the cusp's delta invariant as one and defines the equigeneric setting through preservation of the total delta invariant. Paul Cadman's thesis on the delta-constant stratum independently describes that stratum as the locus where the deformed curve has the same delta invariant as the original. The present claim is a narrow correction of the stated node count; it does not claim novelty for delta-constant deformation theory or propose a replacement theorem.

## Limitations

This result does not classify all deformations of a cusp, establish existence or nonexistence of a particular global equigeneric family beyond the incompatible count, or assess the remaining statements of the preprint. It only rules out the asserted one-cusp/two-node replacement when no other delta contribution compensates for the change.

## References

1. Mounir Nisse, “Equisingular Deformations of Curves and Surfaces in Threefolds,” arXiv:2603.01540v1, posted 2026-03-02, especially Proposition 4.1 and Theorem 4.2.
2. Paul Cadman, “Deformations of plane curve singularities and the delta-constant stratum,” PhD thesis, University of Warwick, 2011, abstract and definition of the delta-constant stratum.
3. G.-M. Greuel, C. Lossen, and E. Shustin, *Introduction to Singularities and Deformations*, Springer, 2007, sections on plane-curve singularities and delta-constant deformations.
