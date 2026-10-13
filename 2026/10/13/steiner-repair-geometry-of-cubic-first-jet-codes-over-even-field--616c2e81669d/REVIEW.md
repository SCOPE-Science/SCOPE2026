# Self-review

## Correctness — PASS

The proof reduces to four explicit generator-column entries, uses the rank-two derivative subspace and Vandermonde independence to exhaust all small dependency types, and derives the unique fourth point of every three-evaluation circuit from the Hasse derivative of its vanishing cubic. The inverse-translation bijection proves the projective Steiner-triple incidence, while a two-evaluation lower bound and primitive-element construction match to give exact unrestricted disjoint availability. No inference for arbitrary dimensions is drawn solely from enumeration. The standalone verifier exhaustively checks all subsets of sizes two through four for \(q=4,8,16\), as well as the disjoint-repair construction.

## Originality — PASS, with residual risk

The first public GHRS paper establishes NRT-MDS/duality/LDPC/quasi-cyclic properties and publishes the construction, but not the stated ordinary-coordinate circuit classification or recovery optimum. The closely equivalent older univariate multiplicity code is acknowledged, rather than treated as novel. The detailed univariate dual formulas in Camps Moreno et al. do not give the enumerated minimal support sets or Steiner repair matching. Li–Wootters address lifted multivariate multiplicity codes and asymptotic disjoint recovery, not this low-degree univariate incidence theorem. Published-result searches using cubic-jet, Hermite, Steiner, value-repair, and equivalent terminology did not identify an implication that subsumes the result. An overlooked projective-geometric tangent configuration or unindexed exact dual-support calculation is an explicit residual risk.

## Value — PASS

The result extracts a concrete operational invariant—exact minimal repair choices and sharp maximum disjoint availability across arbitrarily large fields—from a natural family used to study derivative-evaluation codes. The derivative-level projective Steiner-system structure explains the combinatorics and supplies an explicit optimal recovery packing for value coordinates. It is more than a finite table or restatement of the NRT-MDS theorem and does not require downstream theorems to be a useful complete local classification.

## Scope and limitations

These conclusions cover every \(m\ge2\) with field characteristic two, polynomial degree at most three, all field evaluation points, and all nonzero coordinate multipliers. Only circuits up to size four and exact disjoint availability for value coordinates are established. Nothing is claimed about odd characteristic, higher derivative orders, or an independent review.

Self-review: passed. Independent audit: not yet performed.
