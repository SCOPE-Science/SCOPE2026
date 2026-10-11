# Scientific review

## Correctness — PASS

The fourth moment is expanded exactly by Walsh orthogonality. Every quartic cross term is indexed by an unoriented four-cycle, and its multiplicity is \(24\). The edge-incidence identities and direct Kneser disjointness eigenspaces yield an all-dimensional equality of two quartic expressions, whose right side is a sum of nonnegative squares. This proves the claimed bound for arbitrary real coefficients, not just numerical examples. Zero deficit forces uniform edge magnitude and balanced cycle signs, giving the stated exact switching extremizers. Symmetrization of any ellipsoid over all vertex-sign switches and vertex permutations proves that the standard Euclidean pullback realizes the Banach–Mazur infimum. Exact finite checks in `verify.py` reproduced the fourth moment and sum-of-squares formulas for dimensions \(6,7,8\). They are diagnostic rather than the infinite proof.

## Originality — PASS, with residual risk

Primary papers inspected: Blei–Janson (2004), including the chaos definition, hypercontractive bounds, finite-versus-asymptotic results, and Section 4; Adamczak–Wolff (arXiv:1304.1826v1), including Theorem 1.4 and Sections 1 and 5; Bhattacharya et al. (arXiv:2203.02850), including Proposition 1.11 and Sections 1 and 4. Their general inequalities and asymptotic four-cycle criteria do not imply the all-dimensional sharp arbitrary-real-coefficient fourth-moment formula, quantitative square remainder, and exact Euclidean distortion. Targeted semantic research-result searches for the formula, its Kneser sum-of-squares equivalence, and the Banach–Mazur invariant disclosed no stronger indexed coverage. A previously considered five-sign case is a **different fixed dimension**; the present theorem concerns the entire infinite family \(n\ge6\). Indexed-search incompleteness and possible unindexed equivalents are residual risks, not a proof of novelty.

## Value — PASS

The full quadratic chaos is a canonical Banach subspace of the Boolean-cube \(L^4\) space, with dimension \(\binom n2\). Its sharp finite-dimensional moment constant, all extremizers, coefficient-magnitude stability, and optimal Euclidean distortion are natural, functionally significant invariants. The exact \(n\)-dependence and \(15\) limit explain how finite-dimensional geometry approaches the standardized quadratic Gaussian limit, while the sum-of-squares decomposition links sharp hypercontractivity to the edge-disjointness spectrum. This is not a parameter substitution or isolated numerical curiosity.

## Closest literature and limitations

The generic hypercontractive bound from Blei–Janson is strictly weaker here. The concentration theorem of Adamczak–Wolff is not sharp in the form needed for this statement. Bhattacharya et al. impose binary edge weights and study asymptotic distributions rather than arbitrary real coefficient upper envelopes or Banach–Mazur distortion. The theorem is restricted to real, complete, homogeneous degree-two Walsh chaos on independent uniform signs, dimensions \(n\ge6\). No best possible stability coefficient or near-extremizer sign rigidity is claimed.

Same-model review: passed. Independent audit: not yet performed.
