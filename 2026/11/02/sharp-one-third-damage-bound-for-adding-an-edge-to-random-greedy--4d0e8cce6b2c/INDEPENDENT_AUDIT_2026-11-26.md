# Independent mathematical audit

## correctness

PASS

The frozen proof did not establish all of its isolated-endpoint refinement: its nonnegative induction branch uses k=deg(u)+deg(v)<=1, which is sufficient but not necessary for isolation; when, for example, one endpoint is isolated and the other has degree two, its k>=2 branch proves only the universal lower bound. The statement itself remains true. The corrected files branch first on isolation regardless of k. For a fixed order, conditioning on its first edge proves the vertex-deletion difference is in {0,1}: if that edge avoids the deleted vertex, both take it and reduce to smaller graphs, and otherwise apply the smaller-graph induction to its other endpoint in the deleted graph. Under uniform order this gives the two-vertex deletion loss at most two, or at most one when one vertex is isolated. Subtracting the two first-edge recurrences gives (m+1)Delta = 1+mu(G-{u,v})-mu(G) plus the sum over q old edges disjoint from uv of the smaller differences. Isolation is inherited in every such summand; hence delta is nonnegative in the entire corrected branch. Otherwise k>=2 gives the lower numerator -1-q/3 >= -(m+1)/3; the upper numerator is at most 1+q. The empty graph and the four-vertex path formed from two disjoint edges attain +1 and -1/3 respectively.

## originality

PASS

The repaired result explicitly credits the same-date separate wheel record's general deterministic vertex-deletion lemma: it entails isolated-endpoint monotonicity and the upper bound one. The surviving distinct contribution is the sharp worst-case expected lower bound -1/3 for arbitrary fixed graphs and single nonedges. The closest exact insertion law found applies only to one type of edge in a complete bipartite graph; it does not entail the arbitrary-graph lower bound. Equal catalog dates alone do not order work.

## value

PASS

An extra allowable match can make the randomized greedy policy worse, even though it cannot hurt the optimum. The repaired theorem quantifies exactly how bad one such change can be, by a graph-size-independent sharp constant stronger than the unit sensitivity from deleting vertices. The four-vertex example fixes the constant but is not the universal argument. This is a natural perturbation of a classical algorithm, not just a finite enumeration or a reformulation of the known deletion lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
