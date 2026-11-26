# Independent mathematical audit

## correctness

PASS

The product map fixes the absorbing zero, so its injectivity forces the complete mapping to fix zero and prohibits any other zero output. For each source first coordinate i, the second coordinates of the product outputs must form a permutation pi_i. For each fixed target second coordinate mu, the first coordinates of the mapping outputs then form a permutation sigma_mu. Conversely these row and output-column permutations give bijective product and mapping in the all-one case, hence the all-one factorial count. In this parametrization the forbidden product for source (i,lambda0) occurs exactly if A(i)=pi_i(lambda0) and B(A(i))=i with B(mu)=sigma_mu^(-1)(j0). The functions A:I->Lambda and B:Lambda->I are uniform and independent under the all-one measure. Simultaneous forbidden products specify mutual edges in the two-part directed function graph; compatible r-edge sets are matchings, numbering (m)_r(n)_r/r!, each with probability (mn)^(-r). Incompatible sets have probability zero. Inclusion-exclusion therefore gives the exact count. Relabelling the two sets independently moves the zero. For the joint limit the r-th unsigned term, extended by zero, is bounded by 1/r! and tends to 1/r! for each fixed r; for one dimension fixed the sum is finite and the binomial theorem gives the stated fixed-dimension limit. A separate exhaustive recursion over nonzero-cell target permutations, testing product outputs from the multiplication rule, produced all-one counts 16,288,288,46656 and defect counts 2,48,48,9984 for (2,2),(2,3),(3,2),(3,3), with zero coordinates (lambda0,j0)=(1,1),(2,0),(0,2),(1,1) in zero-based labels, respectively.

## originality

PASS

The supported distinct contribution is the exact labelled enumeration and survival law for one missing sandwich entry. The all-one baseline is covered by the known rectangular-band case, and the avoidance probability is equivalent to absence of a directed two-cycle in a standard random bipartite mapping. The reduction from complete mappings of this semigroup to that probability, and the resulting enumeration, were not supplied by the inspected Rees, Latin-square, rook or random-mapping statements. The random-mapping equivalence is a material access risk, not a claim to a new probabilistic model or counting technique.

## value

PASS

Removing one allowed sandwich entry is a natural minimal change to a fully supported rectangular Rees semigroup. An exact count goes beyond the known existence test: it shows that one defect removes a nonvanishing fraction of complete mappings and quantifies how joint growth differs from keeping one side fixed. The weighted-matching reduction explains why the loss is macroscopic despite the single modified entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
