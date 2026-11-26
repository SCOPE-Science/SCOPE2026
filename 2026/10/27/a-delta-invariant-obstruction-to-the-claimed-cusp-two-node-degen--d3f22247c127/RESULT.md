# A δ-invariant obstruction in a claimed cusp–two-node deformation

## Finding

In Mounir Nisse's *Equisingular Deformations of Curves and Surfaces in Threefolds* (arXiv:2603.01540v1), the proof of Theorem 4.2 explicitly replaces each ordinary cusp by two ordinary nodes in an equigeneric deformation. This step is incompatible with constancy of total δ. If the initial curve has exactly κ ordinary cusps and no other singularities, an equigeneric nodal member, **if it exists**, must have κ nodes, not 2κ.

The related local error is phrased differently in Proposition 4.1. It starts with a reduced planar singularity of δ = 2 and offers a single ordinary cusp as an equigeneric alternative to two ordinary nodes. The cusp alone has δ = 1 and cannot occur as that alternative; a further δ = 1 contribution would be necessary. The proof of the proposition also describes two nodes coalescing into an ordinary cusp within the δ = 2 locus. These observations identify an obstruction to the stated mechanism, not a disproof of the global closure or codimension assertions in the statement of Theorem 4.2.

## Assumptions and scope

Work over an algebraically closed field of characteristic zero, with reduced curves and the indicated ordinary planar singularities. Equigeneric is used in the δ-constant sense. Total δ sums the local invariants over all singularities; the counts above require exactly the specified singularities in the relevant fiber or local deformation neighborhood.

## Proof

The local invariant δ is the length of the quotient of the normalization of the local ring by that ring. For the ordinary cusp \(y^2=x^3\), the inclusion \(k[[s^2,s^3]]\subset k[[s]]\) leaves only the class of \(s\) in the quotient, giving δ = 1. For the ordinary node \(xy=0\), the image in \(k[[x]]\oplus k[[y]]\) consists of pairs with equal constant terms, so the quotient also has length one. Thus two distinct nodes contribute δ = 2, and one ordinary cusp contributes δ = 1. Additivity over distinct points and constancy of total δ give the local and global incompatibilities above. In particular, the proof of Theorem 4.2 simultaneously asserts two nodes per cusp and a total of δ(C) nodes, which disagree when there is at least one cusp.

## Verification

The version-specific source is [arXiv:2603.01540v1](https://arxiv.org/pdf/2603.01540v1). PDF page 9 gives the δ = 2 hypothesis and the two alternatives in Proposition 4.1. PDF pages 9–10 give Theorem 4.2 and its proof; the latter states both that “each cusp has split into two distinct nodes” and that the total number of nodes is exactly δ(C). The local normalization computations above give exact checks of both counts. No computer calculation is needed.

## Relationship to prior work and limitations

The local values of δ and their additivity are standard; no novelty is claimed for them or for the numerical requirement that δ-constant nodal fibers have δ nodes. Related statements of generic equigeneric nodality appear in Nisse's separate preprint *Logarithmic Equigeneric Smoothing and Maximal Nodal Degenerations* ([arXiv:2603.01538v1](https://arxiv.org/pdf/2603.01538v1), PDF pp. 13–14). The point here is the mismatch between specified alternatives and node counts in arXiv:2603.01540v1. This check does not establish the existence of a global equigeneric nodal deformation, the codimension of a cuspidal stratum, or the correctness of any other result in that preprint.
