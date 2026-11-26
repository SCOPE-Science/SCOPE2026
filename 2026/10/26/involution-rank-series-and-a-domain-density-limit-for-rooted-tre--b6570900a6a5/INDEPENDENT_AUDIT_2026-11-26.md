# Independent mathematical audit

## correctness

PASS

A partial map is uniquely determined by the partial injection on children and its nonempty sections. A self-inverse map pairs distinct active children in transpositions with mutually inverse sections of equal rank, and uses self-inverse sections on fixed children. Counting these injections and involutions gives the two general-d recurrences and base case t, including the root. In the binary case every nonempty partial injection has a unique completion to S_2; at empty sections, the two permutations distinguish the root-only map from the extra point. Inversion sends each section inverse to the inverse child permutation's section, so the recursive bijection is inversion-equivariant. The differentiated binary recurrences imply q_h=(1-B_h)q_{h-1}+(1-1/U_h)2^(-h)+2M_{h-1}/(2^h U_h). The last term is at most 2B_h and q_{h-1}<2, giving the stated summable error against the increments 2^(-h). U_1=6 and U_h>=U_{h-1}^2 yield the given doubly exponential bound for B_h. The normalized expectations converge to alpha; fixing the first L levels has probability tending to one for fixed L by the root type probabilities and the product decomposition. Conditional on this event the 2^L frontier maps are independent uniform self-inverses, with conditional variance of the normalized sum at most 1/(4*2^L); first h, then L tending to infinity proves convergence in probability.

## originality

PASS

Best-of-knowledge pass for the self-inverse rank refinement, explicit binary inversion bijection, and typical domain fraction. Unrefined counts, growth of those counts, and partial wreath products are expressly not the contribution.

## value

PASS

The result identifies which portion of a large binary tree a typical self-inverse partial symmetry occupies, with effective evaluation and an actual concentration law, not just the known size of the population. The general rank enumerator records exact distribution data and identifies the distinct fixed-child and paired-child mechanisms behind the conditioned model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
