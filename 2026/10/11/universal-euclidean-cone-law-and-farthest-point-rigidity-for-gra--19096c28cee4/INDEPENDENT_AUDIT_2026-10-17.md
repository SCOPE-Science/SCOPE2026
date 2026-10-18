# Independent mathematical audit

## correctness

PASS

Centering the unweighted graphical zonotope gives (1/2)∑[-b_e,b_e]; strict convexity of squared Euclidean norm puts farthest points at signed endpoints and gives D₂(G)²=max_ε||∑ε b_e||². For H with m leaves, inner signed imbalance d, spoke signs s and S={i:s_i=−1} of size k, expand ||(d+s,−∑s_i)||²=||d||²+m(m+1)−4[k(m−k)+∑_{i∈S}d_i]. Since −∑_{i∈S}d_i≤|∂_H S|≤k(m−k), every cone endpoint obeys claimed bound; choosing all spoke signs equal attains it. Exact equality requires original maximal imbalance and either uniform spokes or a complete nontrivial cut with every crossing contribution negative. Bipartite H has ||d||²≤∑deg², equality precisely componentwise source/sink orientations; a nontrivial complete cut in bipartite H forces the whole graph K_{p,q}, adding two contacts beyond 2^{c+1}. Isolates are handled. Independently enumerated all simple labeled H of orders 2,3,4 (74 graphs), checking squared cone maximum; general theorem is the exact cut proof, not the finite checks.

## originality

PASS

Best-of-knowledge PASS: Chapoton–Pilaud establish graphical zonotope shuffles under graph joins, including joining a vertex; this is a combinatorial/Minkowski construction and does not itself give Euclidean squared diameter additivity or equality contact classification. Padrol–Pilaud–Poullot study deformation cones, while Deza–Pournin–Sukegawa’s diameter is the one-skeleton graph distance. A relevant published complete-multipartite circumradius formula covers special H/cones only and does not imply an identity for arbitrary H. No inspected source supplies the full general cut bound.

## value

PASS

An exact edge-independent Euclidean cone increment for every finite simple graph is a structural law for a fundamental geometric operation; complete equality and bipartite contact counts add sharp geometric rigidity, including connected nonmultipartite families. It relates nontrivial graph structure to Euclidean polytopal extremal geometry and is not mere substitution of a known complete-graph value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
