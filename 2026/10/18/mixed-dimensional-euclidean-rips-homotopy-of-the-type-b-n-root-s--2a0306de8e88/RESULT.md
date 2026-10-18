# Mixed-dimensional Euclidean Rips homotopy of the type-\(B_n\) root systems

## Finding

For every integer \(n\ge3\), let \(e_1,\ldots,e_n\) be the standard orthonormal basis of \(\mathbb R^n\), and let the *unrescaled* crystallographic root configuration of type \(B_n\) be
\[
B_n=\{\pm e_i:1\le i\le n\}\;\cup\;
\{\pm e_i\pm e_j:1\le i<j\le n\}.
\]
Its \(2n^2\) distinct points have the usual Euclidean distance. Define \(\operatorname{VR}_{\le r}(B_n)\) to be the flag complex of pairs at distance at most \(r\), including equality at critical values. The initial three ranges of its integral homotopy filtration are
\[
\operatorname{VR}_{\le r}(B_n)\simeq
\begin{cases}
\bigsqcup^{2n^2}\mathrm{pt},&0\le r<1,\\[2mm]
\displaystyle\bigvee^{2n(n-2)+1}S^1,&1\le r<\sqrt2,\\[2mm]
\displaystyle\left(\bigvee^{8\binom n3}S^2\right)\vee S^{n-1},&\sqrt2\le r<\sqrt3.
\end{cases}
\]
In particular, for \(n\ge4\) the final displayed stage has nonzero integral reduced homology in exactly dimensions \(2\) and \(n-1\), of ranks \(8\binom n3\) and \(1\). For \(n=3\) the two sphere dimensions coincide and the homotopy type is a wedge of nine two-spheres. All these groups are torsion-free. The theorem does *not* describe any filtration stage at or beyond \(\sqrt3\).

## Assumptions and scope

No roots are radially normalized: a short root has norm \(1\), and a long root has norm \(\sqrt2\). The distance parameter is the Euclidean diameter bound, rather than a ball radius or graph distance. Every assertion quantifies over all integers \(n\ge3\). The notation \(\bigvee^m S^q\) denotes a wedge of \(m\) copies of a \(q\)-sphere, and the displayed first-range disjoint union is literal rather than a wedge.

For bookkeeping, let \(V=\{\pm e_i\}\) be the short roots. Let \(G\) be the graph on \(V\) in which two distinct signed basis vectors are adjacent exactly when they have different coordinate supports. Thus \(G\) is the one-skeleton of the boundary of the \(n\)-crosspolytope: it has \(2n\) vertices and \(2n(n-1)\) edges. Put
\[
q=2n(n-2)+1,\qquad t=8\binom n3.
\]
The boundary crosspolytope \(S=\operatorname{Cl}(G)\) is an \((n-1)\)-sphere, and its two-skeleton contains exactly \(t\) triangles.

## Proof

**1. Exact distance tests and the first two ranges.** For short roots \(s,t\), the squared distance is \(2\) if they have different supports and \(4\) if antipodal. Every long root is uniquely \(s+t\) for an edge \(\{s,t\}\) of \(G\). This long root is distance \(1\) from each of \(s,t\), distance \(\sqrt3\) from every orthogonal short root, and distance \(\sqrt5\) from the two short roots opposed to its coordinates. Distinct long roots have squared distance at least \(2\). Consequently the minimum distance between distinct roots is \(1\). On the interval \(1\le r<\sqrt2\), the Rips complex is precisely the graph obtained by subdividing every edge of \(G\) once. It is connected, has cycle rank
\[
|E(G)|-|V(G)|+1=2n(n-2)+1=q,
\]
and is homotopy equivalent to a wedge of \(q\) circles. Below \(1\), all roots are isolated.

**2. Complete clique decomposition at squared threshold two.** Write \(K=\operatorname{VR}_{\le\sqrt2}(B_n)\). For each short root \(s\), let \(A_s\) be the induced flag complex on the long roots \(s+t\) with \(t\) adjacent to \(s\) in \(G\). Any two of these long roots are adjacent at squared threshold \(2\) except when their second short summands are antipodal. Hence \(A_s\) is the boundary of an \((n-1)\)-crosspolytope, homeomorphic to \(S^{n-2}\). Every clique involving exactly one short root \(s\) lies in the cone \(C_s=s*A_s\).

Two long roots are adjacent precisely when they have exactly one common signed coordinate. A family of at least four distinct pairwise intersecting two-element coordinate supports has a common coordinate; furthermore all shared-coordinate signs must agree. It follows that every long-root clique is contained in some \(A_s\), except a triangle indexed by three different coordinate supports and a sign choice on each. These exceptional triangles have vertices \(s+t,s+u,t+u\) for triples \(\{s,t,u\}\) of distinct-support short roots. There are exactly \(t\) such triangles and no higher-dimensional exceptional cliques. A clique involving at least two short roots has either only short roots, in which case it lies in \(S\), or exactly two nonantipodal short roots \(s,t\) together with their unique common long neighbor \(s+t\). Thus the complete list of maximal-simplex families consists of the cones \(C_s\), the exceptional long triangles, the facets of \(S\), and the bridging triangles \(\{s,t,s+t\}\). There are no overlooked mixed simplices.

**3. The long-root-and-cone subcomplex.** Define \(U_0=\bigcup_{s\in V} C_s\). Cones for nonantipodal \(s,t\) intersect in precisely the single long-root vertex \(s+t\); antipodal cones are disjoint; all triple intersections are empty. Let \(H\subset U_0\) be the subdivided graph with edges \(s\)--\((s+t)\)--\(t\) for every edge \(\{s,t\}\) of \(G\). Inside each \(C_s\), all nonvertex faces \(\tau\) of the crosspolytope boundary \(A_s\) can be paired with \(\tau\cup\{s\}\), in descending dimension. These are legitimate free-face collapses, leaving the star-shaped tree on \(s\) and its incident long-root vertices. Since different cones intersect only at such retained vertices, these collapses give \(U_0\searrow H\).

Now adjoin all exceptional long triangles, obtaining \(U\). Under the retraction of \(U_0\) to \(H\), each exceptional triangle \((s+t,s+u,t+u)\) has boundary homotopic to the six-edge subdivision of the corresponding triangular cycle \((s,t,u)\) in \(G\). Homotopy invariance of attaching maps shows that \(U\) is homotopy equivalent to the two-skeleton \(S^{(2)}\) of the crosspolytope boundary. The crosspolytope boundary is an \((n-1)\)-sphere, so \(S^{(2)}\) is simply connected for \(n\ge3\). It has \(2n\) vertices, \(2n(n-1)\) edges, and \(t\) triangles, whence its reduced second homology is free of rank \(t-q\), with all other reduced homology zero. By Hurewicz and homological Whitehead applied to a map from a wedge of two-spheres, it follows that
\[
U\simeq S^{(2)}\simeq\bigvee^{t-q}S^2.
\]
This step establishes an integral homotopy statement, not just a field homology calculation.

**4. Gluing the short-root sphere.** Let \(T\) consist of the subdivided graph \(H\), the original short-root graph \(G\), and all bridging triangles \(\{s,t,s+t\}\). For each edge of \(G\), its bridging triangle witnesses homotopy between that edge and the two-edge path through the associated long root. Consequently both inclusions \(H\hookrightarrow T\) and \(G\hookrightarrow T\) are homotopy equivalences; equivalently, \(T\) is an edgewise triangular mapping cylinder. The exact union is
\[
K=U\cup_H T\cup_G S,
\]
with subcomplex inclusions (hence cofibrations). Its homotopy type is therefore the homotopy pushout of \(U\leftarrow |G|\rightarrow S\). Since both \(U\) and \(S\cong S^{n-1}\) are simply connected, both maps from the connected graph \(G\) are null-homotopic. The homotopy pushout consequently splits as
\[
K\simeq U\vee S\vee\Sigma G
\simeq\left(\bigvee^{t-q}S^2\right)\vee S^{n-1}
\vee\left(\bigvee^qS^2\right)
\simeq\left(\bigvee^tS^2\right)\vee S^{n-1}.
\]
The next Euclidean pair distance above \(\sqrt2\) is \(\sqrt3\), so this type persists for every \(\sqrt2\le r<\sqrt3\). This finishes the proof.

## Verification

The accompanying `verify.py` constructs all \(2n^2\) root coordinates from integers, compares *all* maximal geometric cliques at squared threshold \(2\) with the four proved facet families, enumerates all faces, and performs exact binary boundary-matrix elimination. Executing `python3 verify.py` reports `VERIFY_OK` after exhaustive checks for \(n=3,4,5,6\). The nonzero Betti numbers are respectively \((\beta_2)=(9)\), \((\beta_2,\beta_3)=(32,1)\), \((\beta_2,\beta_4)=(80,1)\), and \((\beta_2,\beta_5)=(160,1)\). This code supplies finite cross-checks only: the proof above establishes the formula uniformly and integrally, including the attaching maps and torsion-free conclusions.

## Relationship to prior work

Adamaszek and Adams classified Vietoris–Rips homotopy types of the circle and developed methods for exact scale transitions. Their later hypercube-graph paper computes Rips homotopy of binary strings with Hamming metric, which is not the Euclidean root point cloud considered here. Previously studied Euclidean type-\(A\) and type-\(D\) root subconfigurations do not include the short roots of \(B_n\) or determine the gluing of the short-root crosspolytope sphere. In particular, knowing the long-root subcomplex's Betti numbers or even its homotopy type does not determine the additional mixed simplices and attachment data established here.

## Limitations

The roots are used at their standard unequal lengths; normalizing every root to the unit sphere changes distances and may change all conclusions. Only \(r<\sqrt3\) is classified. No statement about later persistence deaths, symmetry representations, root systems of other types, or other coefficient-local systems is made. The exhaustive verifier covers four finite dimensions, while infinite-family correctness rests on the independent structural proof. An equivalent formula under a different indexing convention or terminology may exist outside the literature inspected.

## References

1. M. Adamaszek and H. Adams, *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669 (first submitted 2015-03-12); especially Definitions 2.1–2.2 and the main homotopy-type results.
2. M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040 (first submitted 2021-03-01); especially Theorem 1 and its graph-metric setting.
3. A. Hatcher, *Algebraic Topology*, Cambridge University Press (2002), for CW attaching, homotopy pushouts, and Whitehead's theorem.
