# Fixed-point sphere profiles and integral orientation characters of directed path-avoidance complexes

## Finding
Let \(D=(V,E,s,t)\) be any finite directed multigraph with distinguished distinct vertices \(s,t\). Assume that \(E\ne\varnothing\), that \(D\) is acyclic, and that **every vertex and every arc lies on some directed path from \(s\) to \(t\)**. Thus \(s\) is its only source and \(t\) its only sink. Write \(U=V\setminus\{t\}\), the set of nonsink vertices, and let \(\Gamma\le\operatorname{Aut}(D;s,t)\) be any finite group of marked-digraph automorphisms (including permutations of parallel arcs).

Define the path-free and path-missing complexes on the *arc* set by
\[
\operatorname{PF}(D)=\{F\subseteq E:\text{no directed }s\text{-}t\text{ path lies in }F\},
\quad
\operatorname{PM}(D)=\{F\subseteq E:\text{some directed }s\text{-}t\text{ path lies in }E\setminus F\}.
\]
For every subgroup \(H\le\Gamma\), let \(D/H\) be the directed multigraph with vertex and arc sets the \(H\)-orbits, and induced endpoints. There are natural piecewise-linear homeomorphisms
\[
|\operatorname{PF}(D)|^H\cong |\operatorname{PF}(D/H)|,
\qquad |\operatorname{PM}(D)|^H\cong |\operatorname{PM}(D/H)|.
\]
Consequently the fixed-point spaces have homotopy types
\[
|\operatorname{PF}(D)|^H\simeq S^{\,|U/H|-2},
\qquad
|\operatorname{PM}(D)|^H\simeq S^{\,|E/H|-|U/H|-1}.
\]
The convention \(S^{-1}=\varnothing\) applies when a displayed dimension is \(-1\); the corresponding abstract simplicial complex is \(\{\varnothing\}\). No stronger assertion of equivariant homotopy equivalence to representation spheres is made.

The complete **integral rank-one homology modules** are
\[
\widetilde H_{|U|-2}(\operatorname{PF}(D);\mathbb Z)
\cong_\Gamma \det(\mathbb Z[U]),
\quad
\widetilde H_{|E|-|U|-1}(\operatorname{PM}(D);\mathbb Z)
\cong_\Gamma \det(\mathbb Z[E])\otimes\det(\mathbb Z[U]),
\]
with all other reduced groups zero. Here \(\det(\mathbb Z[S])\) denotes the rank-one orientation module \(\bigwedge^{|S|}\mathbb Z[S]\), on which \(g\) acts by the permutation sign. Equivalently, the two characters at \(g\in\Gamma\) are \(\operatorname{sgn}(g|_U)\) and \(\operatorname{sgn}(g|_E)\operatorname{sgn}(g|_U)\).

## Assumptions and scope
Every graph and automorphism group is finite, but parallel arcs are permitted. An arc orbit is kept distinct even if its endpoints coincide with those of another orbit. A path is directed; since the graph is acyclic, directed walks do not repeat vertices. Automorphisms fix \(s,t\), preserve endpoints, and may permute parallel arcs. The fixed-point notation refers to the fixed subset of the *geometric realization*, not the space of orbits \(|K|/H\). Reduced degree \(-1\) uses the usual augmented simplicial-chain convention. In the connected-nonempty geometric cases, reduced homology has its standard topological meaning.

## Proof
**1. Orbit graphs remain essential acyclic networks.** Every vertex is reachable from \(s\). Define \(\rho(v)\) to be the maximum length of a directed path from \(s\) to \(v\). Every arc \(u\to v\) satisfies \(\rho(u)<\rho(v)\). Since each automorphism fixes \(s\), \(\rho\) is constant on its vertex orbits. It therefore strictly increases on every quotient arc. Hence \(D/H\) is acyclic, even as a directed multigraph. Every quotient arc is on the image of an original directed \(s\)-to-\(t\) path, so it is useful, and every quotient vertex lies on such a path. Thus the published sphere theorem applies to \(D/H\) as well as to \(D\).

**2. Path lifting is exact for arc-orbit selections.** Let \(\bar F\subseteq E/H\), and let \(F\) be its full inverse image in \(E\). A path in \(F\) evidently projects to a directed \(s\)-to-\(t\) path in \(\bar F\). Conversely, given a quotient path and any lifted starting vertex, an outgoing quotient arc can always be represented by an original arc with that starting vertex: act by a suitable element of \(H\) on one representative arc. Induction lifts the entire quotient path; it starts at \(s\) and ends at \(t\), since both form singleton orbits. Hence \(F\) contains an \(s\)-to-\(t\) path exactly when \(\bar F\) does. The same equivalence holds for the complementary full orbit selections \(E\setminus F\) and \((E/H)\setminus\bar F\).

**3. Fixed spaces are orbit-face realizations.** A point in the geometric realization of an arc-set simplicial complex has nonnegative barycentric coordinates \((\lambda_e)_{e\in E}\) summing to one, with face support. It is \(H\)-fixed exactly when coordinates are constant along every \(H\)-orbit. The affine coordinate assignment \(\mu_{O}=\sum_{e\in O}\lambda_e\) has inverse \(\lambda_e=\mu_O/|O|\). By step 2, a union of complete arc orbits is a face of either path complex exactly when the corresponding orbit set is a face of the same complex of \(D/H\). The coordinate maps are inverse piecewise-linear homeomorphisms. They also identify empty realizations correctly.

**4. Fixed-point homotopy types.** Grinberg--Katthän--Lewis, Theorems 1.9(b) and 1.10(b), prove that the path-missing complex of an acyclic digraph without useless arcs is a sphere of dimension \(|E|-|U|-1\), and its path-free complex is a sphere of dimension \(|U|-2\), using \(S^{-1}\) when appropriate. Apply this *published nonequivariant theorem* to each \(D/H\) from step 1, then use step 3. This supplies all subgroup fixed-point sphere dimensions. We do not reattribute these underlying sphere classifications as new.

**5. Integral orientation characters.** Fix \(g\in\Gamma\), and write \(c_U(g)\), \(c_E(g)\) for the numbers of cycles in its vertex permutations on \(U\) and \(E\). For either arc-set complex \(K\), the reduced simplicial Lefschetz sum is a sum over \(g\)-invariant faces \(F\). Such a face is a union of \(g\)-arc-orbits. Its oriented-face contribution is
\[
(-1)^{|F|-1}\operatorname{sgn}(g|_F)=(-1)^{\#\{\text{arc orbits in }F\}-1},
\]
including the empty face with contribution \(-1\). The orbit lifting in step 2 therefore identifies this Lefschetz sum with the reduced Euler characteristic of \(K(D/\langle g\rangle)\). The fixed-point sphere dimensions in step 4 give these two sums as \((-1)^{c_U(g)-2}\) and \((-1)^{c_E(g)-c_U(g)-1}\). Since each original complex has only one rank-one reduced integral homology group, of degrees \(|U|-2\) and \(|E|-|U|-1\), its top-homology trace is respectively
\[
(-1)^{|U|-c_U(g)}=\operatorname{sgn}(g|_U),
\qquad
(-1)^{|E|-c_E(g)+|U|-c_U(g)}
=\operatorname{sgn}(g|_E)\operatorname{sgn}(g|_U).
\]
For a formal \(-1\)-sphere the augmented homology is \(\mathbb Z\) with trivial action. If the path-free degree is \(-1\), there are only vertices \(s,t\), possibly with parallel arcs, and the nonsink-vertex permutation sign is indeed trivial. If the path-missing degree is \(-1\), every nonsink has exactly one outgoing arc, so essentiality makes the whole graph one directed \(s\)-to-\(t\) path with trivial marked automorphism group. Both boundary cases satisfy the formulas. Since an automorphism of a rank-one free integral group is determined by its trace \(\pm1\), these are integral module isomorphisms, not merely rational character equalities.

**6. Distinguishing the two modules.** Consider the four-layer acyclic network with consecutive layer sizes \((1,a,b,1)\), all forward arcs between adjacent layers, and \(a,b\ge2\). The symmetry group \(S_a\times S_b\) permutes the two internal layers. Path-free top homology is the product of the two signs; path-missing top homology has character \(\operatorname{sgn}(\sigma)^b\operatorname{sgn}(\tau)^a\). For even \(a,b\), the first character is nontrivial but the second is trivial. At \(a=b=2\), the underlying spaces are \(S^3\) and \(S^2\), whereas their quotients by \(S_2\times S_2\) have respectively zero and one-dimensional *reduced rational top homology*. This last assertion follows from rational transfer for finite group actions on a barycentrically subdivided simplicial complex, not from the fixed-point formula.

## Verification
The standalone file `verify_path_orbits.py` reconstructs all essential labeled acyclic source-sink subgraphs of the forward complete digraph on three, four, five, and selected six vertices, with vertex sets in the fixed topological order. It tests 332 graphs and 405 marked automorphism actions. For each action it checks path lifting for **every** arc-orbit selection, evaluates both orbit-complex Euler sums, evaluates both signed simplicial Lefschetz sums independently by direct enumeration of invariant original faces, and tests the two sign characters. A separate complete four-element symmetry-group test on the \((1,2,2,1)\) layered network checks all five subgroups, including the noncyclic full group, and their fixed-point dimensions and orbit-face equivalences. The verifier prints `PATH_FREE_PATH_MISSING_FIXED_POINT_CHARACTERS_OK 405 332` and `LAYERED_NETWORK_SUBGROUP_FIXED_POINTS_OK` on success. These exhaustive *finite checks* corroborate, but do not replace, the all-size proof above.

## Relationship to prior work
Grinberg, Katthän and Lewis (arXiv:2102.07894, first posted February 15, 2021) introduced the two arc-set complexes and proved the nonequivariant sphere-versus-contractible theorem for directed multigraphs. Their Theorems 1.9 and 1.10 are deliberately used as inputs; the ordinary sphere dimensions themselves are not new. The additional statements here concern all-subgroup geometric fixed spaces, their explicit orbit-graph PL models, and integral automorphism orientation modules. The general equivariant discrete-Morse machinery of Yerolemou and Nanda studies arbitrary group actions and does not provide these network-specific dimensions or characters. Related graph path homology, multipath complexes, directed flag complexes and finite-space fixed-point theories use different chain or face definitions and do not imply the two formulas by identifying their objects.

## Limitations
This is a conditional theorem: the directed graph must be acyclic and every vertex and arc must participate in an \(s\)-to-\(t\) path. It does **not** claim the same fixed-point pattern for cyclic or inessential networks. The PL homeomorphism is to the orbit *path complex*, not to a geometric round sphere, and the proof does not construct a genuine \(\Gamma\)-equivariant homotopy equivalence with a linear representation sphere. A rank-one integral homology module does not determine the full equivariant homotopy type. The rational orbit-space consequence does not imply a homeomorphism or integral homology classification of the orbit spaces. Novelty remains conditional on the completeness of discoverable literature; equivalent unindexed results are possible.

## References
1. Darij Grinberg, Lukas Katthän, Joel Brewster Lewis, *The path-missing and path-free complexes of a directed graph*, arXiv:2102.07894, initially posted 2021-02-15, current accessible full text version 4 (2026-06-21), especially Definitions 1.1 and Theorems 1.9--1.10. https://arxiv.org/abs/2102.07894 and https://arxiv.org/pdf/2102.07894
2. Naya Yerolemou, Vidit Nanda, *Morse theory for complexes of groups*, Journal of Pure and Applied Algebra 228 (2024), article 107606, DOI:10.1016/j.jpaa.2024.107606, for broader equivariant discrete Morse context; the present proof does not require its machinery.
