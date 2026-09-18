# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.**

The central identification is exact. After deleting strongly degenerate coordinates, a choice of basis for the k-dimensional singular subspace produces a full-rank row configuration. A k-subset is a good direction precisely when the corresponding coordinate projection is invertible, equivalently when those k rows are linearly independent. Thus the good directions are exactly the bases of the represented rank-k matroid. A strongly degenerate coordinate is exactly a loop, so every retained element belongs to at least one basis.

Vandanjon's defining coefficients for Xi form a probability distribution on good directions, and the coordinates alpha_j are exactly the element inclusion marginals. Therefore Xi is the intersection of the matroid base polytope with the open box (0,1/2)^E. Edmonds' base-polytope description then gives the stated rank inequalities.

The nonemptiness criterion was checked in two independent forms. Directly, any admissible base distribution forces every deletion set D that lowers rank by delta to have expected basis intersection at least delta, while the coordinate loads give expectation strictly below |D|/2; hence |D|>2 delta. Conversely, matroid strength greater than 2 gives a fractional base distribution with maximum load below 1/2. Because all retained elements are nonloops, a small mixture with a full-support base distribution enforces strictly positive marginals without losing the upper slack.

The exponent criterion follows from the standard box-intersection formula for the matroid independence polytope. The strict version is justified by shrinking all positive capacities by a common factor sufficiently close to one, applying the closed box theorem, and then making an arbitrarily small full-support perturbation inside the remaining upper slack. This also confirms that proper flats are the only rank sets that need to be checked.

The criterion was additionally stress-tested on small randomly generated represented matroids: direct linear programming over base distributions agreed with the matroid-strength formula, and independent box-constrained polymatroid programs agreed with the stated rank-defect feasibility formula. These computations are supporting checks, not substitutes for the proof.

## Originality

**PASS, to the best of our knowledge.**

The closest source is Vandanjon, arXiv:2609.18818, submitted 16 September 2026. Its Section 6 studies nonemptiness of Xi through the number and arrangement of good directions. Proposition 6.15 gives a counting sufficient condition; Remark 6.17 explicitly observes that this condition is not optimal for k>=3; Proposition 6.18 gives a further balanced-design sufficient condition; Example 6.19 constructs empty Xi; and the rank-two case is analyzed separately. The paper does not use matroid terminology and does not state an all-rank base-polytope, matroid-strength, or rank-defect characterization.

The matroid facts used here are classical and are not claimed as new. Edmonds' base-polytope theorem identifies convex combinations of basis indicators by rank inequalities. Matroid strength/fractional base packing gives the reciprocal optimal maximum load, and the box-intersection theorem gives the exact capacity-feasibility condition.

Searches combining the multiplier paper title and arXiv identifier with “matroid”, “base polytope”, “base packing”, and “matroid strength”, as well as broader searches combining degenerate multilinear Mikhlin multipliers with those terms, did not locate a prior statement making this identification. Searches of the current SCOPE repository for the source arXiv identifier, “Multilinear Mikhlin”, “fractional base packing”, and “matroid strength” found no overlapping record.

The originality claim is restricted to recognizing the new multiplier admissibility polytope as a matroid base polytope, deriving the exact all-rank strength/rank-defect nonemptiness criterion, and eliminating the existential alpha from the exponent condition. No originality is claimed for the underlying matroid theorems.

Residual risk: arXiv:2609.18818 is extremely recent, so a contemporaneous observation not yet indexed could overlap. No inaccessible paper was identified as specifically likely to contain this exact application.

## Value

**PASS.**

The result replaces several partial geometric criteria by a single exact criterion valid for every rank k. It also gives an explicit description of the entire Xi polytope, not only its nonemptiness, and converts the existential exponent condition in Theorem 1.4 into rank-defect inequalities. The two principal examples in the source paper become short strength certificates, and the complete rank-two case becomes a simple statement about parallel classes.

The result is structural rather than an independent multiplier theorem: it does not enlarge the analytic theorem when Xi is empty and does not claim unboundedness outside the criterion. This boundary is explicit in RESULT.md.

## Literature inspected

- H. Vandanjon, arXiv:2609.18818, including Definitions 1.1–1.2, Theorem 1.4, Section 6.3, Propositions 6.15 and 6.18, Example 6.19, and the rank-two discussion.
- T. de Vos and M. Grilnberger, *Dynamic Matroids: Base Packing and Covering*, ESA 2026, including the definition of matroid strength and the load/base-packing relation.
- Modern statements of Edmonds' matroid base-polytope theorem and box-intersection theorem, including Theorem 2.2 in *On the correlation gap of matroids*.

No independent validation, formal verification, or peer review is asserted.
