# Scientific review

## Correctness — PASS
The proof counts distinct weight-one deletion descendants: each adjacent-one word consumes one, each separated-one word consumes two. Mutual exclusion of consecutive starts among adjacent-one words yields the sharp all-length upper bound. The periodic construction satisfies the matching size, and its weight-one and weight-two deletion descendants are proved disjoint by explicit support-coordinate cases. Boundary lengths, singleton descendant normalization, and deletion of zero versus one were checked. `verify.py` independently exercises the deletion definition through length 64 and searches the entire finite compatibility graph through length 9. Finite checks are auxiliary to the all-length argument.

## Originality — PASS, qualified by bibliographic uncertainty
The closest primary paper is Cullina--Kulkarni--Kiyavash (arXiv:1211.4056v1), Section IV: its exact result is the chromatic number of each constant-weight deletion graph, not the weight-two independence number, and it warns that color classes need not be maximum independent sets. The second primary paper (Kulkarni--Kiyavash, arXiv:1211.3128v1) gives more general packing bounds without this closed constant-weight exact optimum. Searches for weight-two, fixed-weight, sparse binary deletion codes, graph independence, checksum classes, and equivalent formulas did not reveal an implication to the claim. The 2015 Cullina thesis is a plausible source whose full text remained inaccessible, so earlier coverage there or in other unindexed work cannot be ruled out.

## Value — PASS
The number \(M_2(n)\) is a natural exact invariant of a classical constrained deletion channel, resolved for all lengths by an explicit linear-time construction and a sharp combinatorial obstruction. The result has substantive design content: a maximum code can be about 50 percent larger than the largest class in the known optimal coloring, emphasizing that chromatic optimality does not optimize a single codebook. The result is a complete infinite parameter family, not a single unmotivated numerical increment.

## Limits
No all-optima census, other-weight result, or independent validation is claimed. The all-length proof is human-readable and computation only corroborates finite cases. Priority has residual bibliographic uncertainty.

Self-review: passed. Independent audit: not yet performed.
