# Independent mathematical audit

## correctness

PASS

The unoriented incidence identity BB^T=Q and B^TB=A(L)+2I for connected bicyclic kayak paddles with n=p+q+r-1 and m=n+1 edges transfers inertia of Q-2I to line-graph adjacency, adding exactly one negative index (also valid for bipartite G). Four inserted degree-two vertices have shifted-path block T4 with inertia (2,0,2) and endpoint inverse response -1, so increasing any cycle by four preserves (signature,nullity). Two inserted vertices on a bridge have T2 with (1,0,1) and endpoint response +1, producing one sign-reversed edge, removable by diagonal switching on one bridge side. This reduces every p,q>=3,r>=1 to exactly twenty p0,q0 in {3,4,5,6}, r0 in {1,2} base cases. Our separately assembled line-graph adjacency and exact Fraction symmetric elimination reproduced all twenty (signature,nullity) entries; algebraic reductions, not supplemental scans, make them exhaustive for unbounded sizes. Formula n±=(m-n0±s)/2 and sharp signature and maximum-nullity cases follow by table inspection.

## originality

PASS

The object is also called a dumbbell/barbell/kayak-paddle graph. Search compared inertia of adjacency of the LINE graph with threshold inertia of the signless Laplacian Q(G)-2I; these are equivalent via rectangular incidence, but not equivalent to Laplacian spectral uniqueness of the original graph. Paone and Paone analyze any rose or generalized theta and some bridgeless cactus graphs; a kayak paddle with two vertex-disjoint cycles connected by a bridge path is neither a rose, theta, nor bridgeless cactus. They specifically flag bridge-connected disjoint cycles as outside their exact families. The general path-block technique is an antecedent but not an evaluated all-residue table for this graph class. The 2025 Akbari et al. paper gives two kayak signature-one examples, but neither the converse equality characterization nor maximum kernel dimension. Paone and Paone use similar Schur methods and explicit rose/theta results, but their theorem hypotheses exclude bridges. Francis–Uptain unbounded signature examples involve more complex cacti and do not imply the bounded kayak classification.

## value

PASS

Kayak paddles form the natural missing bicyclic two-core family between roses, generalized thetas and bridged cacti. A full signed inertia table determines nullity including singular branches, maximal kernel dimension three, and exact signatures attaining one, which isolated examples or general bounds cannot provide. The invariant is structurally motivated and useful in spectral graph classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
