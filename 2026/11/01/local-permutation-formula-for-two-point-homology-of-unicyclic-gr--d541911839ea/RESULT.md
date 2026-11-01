# Local permutation formula for two-point homology of unicyclic graphs

## Finding

Let \(G\) be any finite connected simple graph with exactly one cycle, and let \(\Gamma=\operatorname{Aut}(G)\). Write \(X=\operatorname{UConf}_2(|G|)\) for the ordinary collision-free unordered two-point configuration space. At each vertex \(v\), let \(E_v\) denote its set of incident halfedges and let \(A_v=\ker(\mathbb Q[E_v]\xrightarrow{\sum}\mathbb Q)\). Let \(\varepsilon\) be the one-dimensional rational representation describing the action of \(\Gamma\) on the orientation of the unique cycle. Then, as rational \(\Gamma\)-representations,

\[
H_1(X;\mathbb Q)\cong\varepsilon\oplus\bigoplus_{v\in V(G)}\bigwedge^2 A_v.
\]

The group acts on the direct sum by transporting vertex summands. Also \(H_j(X;\mathbb Q)=0\) for every \(j\ge2\). Consequently, for any automorphism \(g\), if \(f_v(g)\) is the number of incident halfedges individually fixed by \(g\) at a fixed vertex \(v\), then

\[
\operatorname{tr}(g\mid H_1(X;\mathbb Q))=\varepsilon(g)+\frac12\sum_{v:gv=v}\left(f_v(g)^2-f_v(g^2)-2f_v(g)+2\right).
\]

In particular, \(\dim H_1(X;\mathbb Q)=1+\sum_v\binom{\deg(v)-1}{2}\). This dimension identity is not claimed as a new nonequivariant Betti-number formula; the finding is the uniform complete automorphism representation and fixed-local-data character.

## Assumptions and scope

Graphs are finite, undirected, connected, and simple. There is precisely one simple cycle, necessarily of length at least three; trees may be attached to its vertices. No hypothesis is placed on vertex degrees or on the automorphism group. All configuration points are distinct, the particles are unlabeled, and the space is formed from the geometric realization of the graph. The representation result is over \(\mathbb Q\) and applies to the full automorphism group and, by restriction, to each subgroup. The direct-sum isomorphism is an abstract rational representation isomorphism, not a specified canonical chain-level splitting or an integral lattice isomorphism.

## Proof

**1. Cubical model and absence of second homology.** The standard two-particle deleted-product cubical model has \(0\)-cells \(\{u,v\}\) for distinct vertices, \(1\)-cells \((e,v)\) for an edge disjoint from a vertex, and \(2\)-cells \(\{e,f\}\) for two edges with disjoint endpoint sets. Its inclusion in \(X\) induces an isomorphism on homology and commutes with graph automorphisms. The two-particle subdivision criterion holds: every cycle has at least three edges, and each path between distinct vertices of valence other than two has at least one edge.

For any integral \(2\)-cycle \(z\), fix an edge \(e\). Its coefficients on squares \(\{e,f\}\) constitute a \(1\)-cycle in the induced graph obtained by deleting the endpoints of \(e\): project \(\partial z\) onto the oriented \(1\)-cells \((e,v)\). If \(e\) lies on the unique cycle, deleting its endpoints breaks that cycle, so the induced graph is a forest. The resulting \(1\)-cycle vanishes, forcing every coefficient involving \(e\) to vanish. For an off-cycle edge, all remaining partner edges lie in the forest obtained by deleting the unique cycle's edges. The same projection then forces their coefficients to vanish. Hence \(\partial_2\) is injective over \(\mathbb Z\), so \(H_2=0\); no cells exist above dimension two. The configuration space is connected because the underlying graph is connected and particles are unordered.

**2. Equivariant cellular identities.** Work in the Grothendieck ring of finite-dimensional rational \(\Gamma\)-representations. Let \(P=\mathbb Q[V(G)]\), and let \(Q=C_1(G;\mathbb Q)\) be the oriented-edge representation. Let \(F=\bigoplus_v\mathbb Q[E_v]\) be the incident-halfedge permutation representation and \(K=\bigoplus_v\bigwedge^2\mathbb Q[E_v]\). The three cellular representations are

\[
[C_0(X)]=[\operatorname{Sym}^2 P]-[P],\qquad
[C_1(X)]=[Q\otimes P]-[F],\qquad
[C_2(X)]=[\bigwedge^2 Q]-[K].
\]

The first identity separates diagonal monomials from unordered distinct vertex pairs. The second removes incident edge-vertex pairs. The third removes incident edge-edge pairs from the exterior square; in a simple graph such a pair has a unique common vertex. For the latter two identifications, orienting each incident edge away from its fixed vertex converts orientation signs into the ordinary halfedge permutation action. The exterior-square sign also accounts for exchanging the two edges in a square.

Because the graph itself is connected and unicyclic, its exact cellular sequence gives \([Q]=[P]-[\mathbf1]+[\varepsilon]\). Put \(T=P-\mathbf1\) and use \(Q=T+\varepsilon\), \(\operatorname{Sym}^2P=\operatorname{Sym}^2T+T+\mathbf1\), and \(T\otimes T=\operatorname{Sym}^2T+\bigwedge^2T\). Since \(\bigwedge^2\varepsilon=0\), this yields

\[
[\mathbf1]-[\operatorname{Sym}^2P]+[Q\otimes P]-[\bigwedge^2 Q]=[\varepsilon].
\]

The equivariant Euler identity and the vanishing of higher homology now give

\[
[H_1(X;\mathbb Q)]=[\varepsilon]+[K]-[F]+[P]
=[\varepsilon]+\sum_{v\in V(G)}[\bigwedge^2 A_v].
\]

The last equality follows from the equivariant split exact sequence \(\mathbb Q[E_v]\cong\mathbf1\oplus A_v\) for a vertex stabilizer, and \(\bigwedge^2(\mathbf1\oplus A_v)\cong A_v\oplus\bigwedge^2 A_v\). Finite-group rational representations are semisimple, so equality of representation classes gives the stated isomorphism; it need not give a preferred integral splitting.

**3. Character and dimension.** A nonfixed vertex contributes zero to the trace of the transported local direct sum. At a fixed vertex, the incident-halfedge permutation character has trace \(f_v(g)\), and the square of that permutation has trace \(f_v(g^2)\). The identity \(\operatorname{tr}(\bigwedge^2 T)=(\operatorname{tr}T)^2/2-\operatorname{tr}(T^2)/2\), applied to the augmentation representation, gives the displayed formula. At the identity the local dimension is \(\binom{\deg(v)-1}{2}\), proving the stated dimension formula.

## Verification

Run `python unicyclic_two_point_verify.py` using Python 3 and no third-party packages. It independently builds the unordered cellular chain modules, enumerates graph automorphisms, computes signed fixed-cell traces including square-coordinate swaps, and evaluates the claimed local representation character. It also checks exact \(\mathbb F_2\) injectivity of the second boundary and Euler-derived first Betti numbers. The eight examples comprise a pure cycle, three sunlet graphs, and four asymmetrically decorated cycles; all sixty-six enumerated automorphisms satisfy the character formula. The recorded output is in `unicyclic_two_point_verification_output.txt`. These finite checks are supplementary; the proof above supplies the all-graph argument.

For illustration, in the sunlet graph with an attached leaf at each vertex of a cycle of length \(n\ge3\), the first Betti number is \(n+1\). Every nonidentity rotation has character \(1\); a reflection has character \(-2\) when \(n\) is odd; when \(n\) is even the character is \(-3\) for a reflection fixing two cycle vertices and \(-1\) for a reflection fixing no cycle vertex. These follow immediately from the local fixed-halfedge formula.

## Relationship to prior work

Barnett and Farber (first public arXiv version March 12, 2009) develop deleted-product homology and planar graph configuration cohomology, mainly for ordered pairs; they do not state this full automorphism representation. Ko and Park (first arXiv version January 13, 2011, Theorem 3.16) determine nonequivariant first-homology groups of graph braid groups, and their formula already covers the ranks quoted above; these ranks are not asserted to be new. Lütgehetmann (first arXiv version January 12, 2017) proves representation-stability properties for **ordered** graph configurations under graph-stabilizing symmetric groups, not this explicit character for arbitrary automorphisms of a fixed unicyclic graph. Existing work on configurations permitting vertex collisions and on Borel–Moore homology concerns distinct spaces or theories. The new point is a local, evaluable character formula and complete rational representation valid simultaneously for all finite unicyclic graphs, including asymmetric attached trees.

## Limitations

No integral equivariant lattice splitting is claimed. The theorem does not extend as written to graphs with more than one cycle, for which the cellular exterior-square cycle term and potentially nonzero second homology enter. It does not describe fundamental-group automorphisms, higher-particle spaces, or Borel-equivariant invariants. The prior-work comparison cannot rule out an equivalent unindexed identity and is not independent publication-priority certification.

## References

- K. Barnett and M. Farber, *Topology of Configuration Space of Two Particles on a Graph, I*, arXiv:0903.2180v1 (public March 12, 2009), https://arxiv.org/abs/0903.2180.
- K. H. Ko and H. W. Park, *Characteristics of Graph Braid Groups*, arXiv:1101.2648v1 (public January 13, 2011), https://arxiv.org/abs/1101.2648.
- D. Lütgehetmann, *Representation Stability for Configuration Spaces of Graphs*, arXiv:1701.03490 (first public January 12, 2017), https://arxiv.org/abs/1701.03490.
