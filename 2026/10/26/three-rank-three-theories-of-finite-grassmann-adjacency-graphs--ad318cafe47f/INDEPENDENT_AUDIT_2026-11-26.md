# Independent mathematical audit

## correctness

PASS

The 3-round game reduces by vertex transitivity to the set of labeled second-move profiles from any first vertex. Labels record equality and adjacency, and extensions record the achievable two adjacency bits for a fresh vertex; repetitions are automatic and the diagonal records existence of a distinct neighbor and nonneighbor. A mismatched label or extension is exposed in the remaining rounds. After annihilator duality, k≤n/2. For separation d=k−dim(U∩V), split the ambient space into H,A,B,C with U=H⊕A, V=H⊕B and dim C≥k−d. A diagonal span of the a_i+b_i completed in C is disjoint from both. For d≥2, retaining H and all but one A-direction and replacing the removed direction by a_1+b_1 gives a neighbor of U alone; when d=1, retain a_1 and all but one H-direction and add a vector in C. Swap U,V for the other asymmetry. Common neighbors come from replacing the sole direction with span(a_1+b_1) at d=1 or adding span(a_1,b_1) to H at d=2, and are impossible at d≥3 by the intersection-dimension inequality. All separations through k occur; the diagonal has both kinds of distinct vertex for k≥2. The k=1 case is complete on at least three vertices. A rank-two nonedge test and a rank-three nonedge-without-common-neighbor test separate the classes. Independently checked Johnson profiles on pair orbit representatives: for J(6,2) use pairs 12/13 and 12/34 with respective witnesses (11,10,01,00) equal to (14,24,34,45) and (13,15,35,56). For J(7,3) use 123/124, 123/145, 123/456 with witnesses (125,135,145,567), (124,126,146,267), and (none,127,457,147). The last missing common neighbor follows by disjointness. J(3,1) is K3. The Gaussian binomial is monotone in n by inclusion and in q by its nonnegative Schubert-cell coefficients, and the central sequence is monotone in k by adjoining a fixed line in two extra dimensions. The minima are 3,35,1395, the last from (63·31·15)/(7·3·1). The recorded outputs verification_output.txt and direct_output.txt can be reproduced by verify_grassmann.py and verify_logic.py, respectively; their evidence is finite and no replay is claimed.

## originality

PASS

The checked earlier and same-date material does not establish the uniform finite-field Grassmann classification or the cross-family equivalence. The Johnson representative list and ingredients from graph logic and strongly regular graphs are credited; the novelty is not the list restricted to Johnson graphs or the rank-three analysis of the diameter-two part in isolation. A distinct later catalogue result covers the complete nondegenerate Grassmann classification and its size bound, and adds a singleton case; that overlap is explicit and not evidence of prior publication before the frozen record.

## value

PASS

The result exactly identifies how much of a natural finite geometric graph family is visible in the pure adjacency language at a fixed nontrivial game depth. It shows that field size and higher dimensions disappear once effective rank reaches three, while distinguishing diameter two from larger diameter with a sharp rank threshold. The paired internal and much smaller cross-family representatives make the classification usable as a test set.

The dated certificate retains the supplied scientific assessment, sources and limitations.
