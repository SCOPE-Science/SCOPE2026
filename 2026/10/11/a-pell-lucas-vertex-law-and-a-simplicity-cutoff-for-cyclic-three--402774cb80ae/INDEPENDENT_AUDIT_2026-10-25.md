# Independent mathematical audit

## correctness

PASS

For integer n>=4, Q_n is a Minkowski sum of n cycle edges and n cyclic triples in sum-coordinate hyperplane dimension n-1, since the edge segments span its tangent hyperplane. Any generic normal exposes a unique winner on each summand, and distinct feasible winner assignments map injectively to vertices by the standard sum of strict maximizing inequalities. Edge comparisons give a cyclic binary sign word s. Triple winner is forced except at each valley (-,+), where either neighboring coordinate may win, yielding 2^v formal assignments. Orient cycle comparisons and one chord across each valley. Feasibility is equivalent to DAG via topological ordering. Valleys are not adjacent, have only outward cycle arrows and no incident chords; removing them yields a directed multicycle, even in n=4 two-vertex parallel-chord case. Exactly one clockwise cycle occurs when minus positions are independent, and analogously for plus positions/counterclockwise; opposite obstructions cannot occur in the same complete chord assignment. Hence forbidden count 2L_n and all formal choices trace [[1,2],[1,1]]^n yielding Pell–Lucas trace. The n=4 24 order cases have 20 distinct winner assignments, all three-cover normals, independently checked. For n>=5 the explicit cyclic order w=(0,1,...,n-3,n-1,n-2) yields covers 0<1<...<n-2 plus 1<n-1<n-2, exactly n covers for a dimension n-1 polytope, proving nonsimplicity via the established Hasse-cover criterion. No unproved infinite inference is drawn from bounded numerical experiments.

## originality

PASS

Best-of-knowledge PASS with a real derivational-coverage qualification. Pešović–Stojadinović define the exact equivalent cycle 2-graph-polytope (up to a singleton translation) and their general f-polynomial specialization can evaluate its vertex number for each n, so the object and in-principle enumeration are not new. Their inspected formula (3) and examples do not give the uniform closed Pell–Lucas trace, the two explicit directed-cycle subtraction classes, or the iff n=4 simplicity boundary. Benedetti–Bergeron–Machacek already prove the general acyclic-orientation/normal-cone and forest-cover criteria used here; the proof applies those criteria nontrivially to this cyclic family. Padrol–Pilaud–Poullot give the deformation framework and Gélinas–Yang the cyclic hypergraphic-poset lattice criterion, not this f0 evaluation. Originality is limited to the evaluated family-specific all-dimensional pair of conclusions and combinatorial derivation, not general frameworks, transfer matrices or independent set counts. Stronger implicit deduction/unindexed tables remain priority risks; failed queries are not proof of novelty.

## value

PASS

The object is a natural cycle instance of second graph polytopes interpolating between graphical zonotopes and graph associahedra. The number of vertices and simplicity are canonical global and local combinatorial invariants. The exact all-dimensional difference of two distinct classic transfer traces is not a trivial count of a fixed-size table: it identifies the only two cyclic feasibility obstructions and a sharp transition to nonsimple normal cones already in dimension five. These provide a reusable worked structural classification for cyclic interval hypergraphic polytopes; no downstream theorem or paper-length discovery is required. Not claiming novelty of the general cycle, general orientation criterion, or independent-set recurrence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
