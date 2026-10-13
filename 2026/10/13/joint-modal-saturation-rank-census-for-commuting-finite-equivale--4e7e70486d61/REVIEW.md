# Scientific review: joint modal-saturation rank census

## Correctness

**PASS.** The modal-operation criterion is reduced to the equality of composed binary relations by evaluating existential powerset maps on singleton inputs. A transitive product of two equivalence relations equals their join; commutation is equivalent to that transitivity. Each join-class is therefore exactly a nonempty rectangular intersection grid. The grid-surjection count divides by the freely acting row/column label permutations, and the labelled-set construction proves the generating function. The resulting operator has precisely \(2^c\) image values. The minimum-\(n\) support theorem follows from \(\sum r_i s_i=a+b-c+\sum(r_i-1)(s_i-1)\), with explicit constructions attaining equality. All boundary cases, including empty set, one component, and singleton grid dimensions, are addressed. Exact recurrence, direct brute-force relation tests, and direct modal-powerset tests independently agree within stated finite bounds.

## Originality

**PASS, qualified by a genuine residual risk.** OEIS A354458 already gives the unrefined total numbers and composition/join criterion, so neither is asserted to be new. The inspected OEIS entry does not provide the joint \((a,b,c)\)-refinement, complete modal image-rank multiplicities, or the sharp \(c=1\) versus \(c\geq2\) support transition. Primary work on decidable-equivalence joins concerns computability; primary work on neighbourhood pooling concerns expressive semantics; partition/composition-matrix work concerns different matrix shapes and constraints. Statement-level comparisons do not give the present refinement. A historically equivalent multidimensional refinement or a translation through classical grid-partition enumeration may exist outside the searched material. Searches do not establish global novelty.

## Mathematical value

**PASS.** Composing finite equivalence modalities models successive accessibility saturation. Counts of individual equivalence classes record the information granularity of each modality, while the image cardinality of the composite records the number of possible saturated observable sets. Their complete joint distribution is a natural finite-algebraic invariant, not determined by the previously tabulated total count. The proof also finds a sharp and asymmetric feasible-support boundary: a single fully merged component requires at least \(ab\) states, but allowing at least two components reduces the minimum to \(a+b-c\). It provides reusable exact coefficient and recurrence methods for every finite size, not a narrow parameter slice or a restatement of an earlier integer sequence.

## Closest sources and limits

The closest exact-count source is Geoffrey Critzer's 2022 OEIS A354458, which decisively covers the unweighted marginal. Green's 2017 arXiv paper considers join/composition of decidable equivalence relations on infinite domains. Van De Putte–Klein's 2022 open-access article studies neighbourhood pooling, not this enumeration. Claesson–Dukes–Kubitzke's partition/composition matrices are structurally different from complete nonempty intersection grids. Equivalences under older partition/congruence terminology remain an originality risk. The finite verifications are corroboration, not a replacement for the unrestricted mathematical proof. The result does not count isomorphism classes or full term clones.

Self-review: passed. Independent audit: not yet performed.
