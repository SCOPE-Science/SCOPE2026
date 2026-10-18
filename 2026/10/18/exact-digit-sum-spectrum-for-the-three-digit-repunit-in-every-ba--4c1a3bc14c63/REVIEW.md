# Mathematical review: three-digit repunit digit-sum spectrum

## Correctness — PASS

The main equivalence is exact for every integer \(b\ge2\): a digit sum \(s\ge1\) is attained by a positive multiple of \(m=b^2+b+1\) if and only if a nonnegative triple has total \(s\) and satisfies \(A+bB+b^2C\equiv0\pmod m\). One implication groups ordinary digits by exponent modulo three. The other constructs *distinct* powers of \(b\), so no carrying or bounded-length assumption enters. All three generating triples have weighted sum exactly \(m\). For sums at most \(2b+1\), subtracting the minimum coordinate and using cyclic rotation yields a positive two-coordinate weighted sum strictly below \(2m\), hence exactly \(m\). The resulting integer inequalities force exactly the two nontrivial generator sums. For larger sums, the three residue representatives settle the remaining congruence classes. The Apéry calculation yields exact conductor, Frobenius number, and genus; the divisible-by-three branch is handled separately. A standalone finite-state program independently checked \(1,162\) base/sum comparisons across \(18\) bases and visited \(551,625\) states. Finite checks are corroborating evidence, not the infinite proof.

## Originality — PASS with residual risk

The most relevant published full texts are Phunphayap–Noppakaew–Pongsriiam (2023), arXiv:2303.13017, and Clokie–Lidbetter–Molina Lovett–Shallit–Witzman (2020), arXiv:2002.02731. The 2023 paper establishes the relevant congruence obstruction and cofiniteness, supplies the general attained-multiples observation, and asks for Frobenius numbers (Question 4). The 2020 paper already proves an equivalent three-class power-sum existence criterion and constructions of infinite progressions, and repunit sturdiness. Those known portions are not claimed as novel. Neither inspected paper states, implies by its explicit results, or tabulates the exact \(\langle3,b+2,2b+1\rangle\) equality, sharp exclusion at \(2b-2\), or genus \(b\) for \(b\not\equiv1\pmod3\). Semantic mathematical-record searches for the exact modulus, base-repunit aliases, Apéry formulation, Frobenius formula, and originator names revealed no matching published result. A negative search is not proof of novelty, and a specialized unindexed source could overlap.

## Value — PASS

The exact attainable digit-sum set is the natural output set explicitly studied by the 2023 source; the cofinite branch yields an exact Frobenius number, answering its Question 4 for the infinite cyclotomic subfamily \(n=b^2+b+1\) across all bases with \(b\not\equiv1\pmod3\). The genus \(b\) and three-generator Apéry description provide more information than a mere existence bound. The three-exponent-class reduction is an explicit structural mechanism and gives a sharp, parameter-uniform classification instead of isolated computations. This is substantive even without any downstream density theorem.

## Closest literature and limitations

The divisible-by-three branch is already implied by Theorems 1 and 2 in Phunphayap–Noppakaew–Pongsriiam and is included solely to make the classification uniform. The general cofinite claim for the other branch was also established there; the new contribution is the **sharp** exceptional set and its invariants. Clokie and coauthors provide general attainable progressions, but not an exclusion theorem for this family. The theorem does not classify minimal multipliers, output multiplicities, or longer repunits. Unindexed exact special-case treatments remain a possible originality risk; independent mathematical audit has not occurred.

Self-review: passed. Independent audit: not yet performed.
