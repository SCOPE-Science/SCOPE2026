# Affine-plane incidence Rips complexes have two sphere dimensions

## Finding

Let \(\mathcal A\) be any finite affine plane of order \(q\ge3\). Give its point–line incidence graph \(G_{\mathcal A}\) the unit-edge shortest-path metric and use the inclusive Vietoris–Rips convention. Its scale-two complex has the homotopy type
\[
\mathrm{VR}_{\le}(G_{\mathcal A};2)\simeq
\bigvee^{(q-1)^2(q+1)}S^2\;\vee\;
\bigvee^{(q-1)^{q+1}}S^q.
\]
The scale-one complex is a wedge of \((q-1)^2(q+1)\) circles, and every scale at least \(3\) is contractible. Consequently, over any field the complete positive-dimensional persistence barcode consists of \((q-1)^2(q+1)\) intervals \([1,2)\) in degree one, the same number of intervals \([2,3)\) in degree two, and \((q-1)^{q+1}\) intervals \([2,3)\) in degree \(q\). No other positive-dimensional intervals occur. In particular, the order-three Hesse incidence configuration gives \(\bigvee^{16}S^2\vee\bigvee^{16}S^3\) at scale two.

## Assumptions and scope

An affine plane of order \(q\) has \(q^2\) points and \(q(q+1)\) lines; every line contains \(q\) points and each point belongs to \(q+1\) lines. Distinct points lie on exactly one common line. Lines split into \(q+1\) parallel classes of \(q\) pairwise disjoint lines; any two lines from different classes meet at one point. No coordinatization or Desarguesian assumption is imposed. The theorem applies whenever such a finite affine plane exists and does not assert its existence for every integer \(q\). The range \(q\ge3\) excludes the separately understood edge-subdivision case of order two.

For a finite graph \(G\), the complex \(\mathrm{VR}_{\le}(G;r)\) contains a vertex set exactly if all of its pairwise graph distances are at most \(r\). Thus at integer \(r\) it is the clique complex of the distance-\(r\) graph power. The barcode statement ignores degree-zero intervals and uses the inclusive threshold: a feature dying at \(2\) is absent at \(2\).

## Proof

Write \(P\) and \(L\) for the point and line sets. The incidence graph is connected and bipartite. Any two distinct points are distance \(2\). Two different lines have distance \(2\) if they intersect, and distance \(4\) if they are parallel. An incident point–line pair has distance \(1\), and a nonincident pair distance \(3\). The latter assertion uses a point on the given line and the unique affine line joining that point to the chosen nonincident point. A parallel pair has no common point, hence no length-two path, but has a length-four path via two intersecting lines. These distances establish a diameter of \(4\).

Put \(K=\mathrm{VR}_{\le}(G_{\mathcal A};2)\). For every line \(\ell\), let \(P_{\ell}\) be its \(q\) incident points; for every point \(p\), let \(L_p\) be its \(q+1\) incident lines. A clique of the distance-two graph cannot contain two distinct points and two distinct lines, since two distinct points have only one common line. Every mixed clique is therefore contained either in \(\{\ell\}\cup P_{\ell}\) or in \(\{p\}\cup L_p\).

Let
\[
U=\Delta(P)\cup\bigcup_{\ell\in L}\bigl(\{\ell\}*\Delta(P_{\ell})\bigr),\qquad
V=B\cup\bigcup_{p\in P}\bigl(\{p\}*\Delta(L_p)\bigr),
\]
where \(\Delta(S)\) denotes the full simplex on a finite set \(S\), the asterisk denotes simplicial join, and \(B\) is the flag complex of the graph on \(L\) connecting exactly the *nonparallel* pairs. The clique classification gives \(K=U\cup V\). Each line vertex belongs to just one cone of \(U\), attached along its full base \(\Delta(P_{\ell})\) in the simplex \(\Delta(P)\); deleting these line apexes by elementary simplicial collapses leaves \(\Delta(P)\). Thus \(U\) is contractible. Similarly, deleting the point apexes of the attached cones collapses \(V\) onto \(B\).

Both subcomplexes have all original vertices. A face involving two points belongs only to \(U\); a face involving two lines belongs only to \(V\). Their common one-simplices are precisely the incident point–line edges, and they share no simplex of dimension at least two. Hence \(U\cap V=G_{\mathcal A}\), literally as a simplicial subcomplex. All inclusions are simplicial cofibrations. Replacing the contractible \(U\) by a point and \(V\) by \(B\) in the homotopy pushout expresses \(K\) as the mapping cone of a map \(G_{\mathcal A}\to B\).

The graph underlying \(B\) is complete \((q+1)\)-partite with \(q\) vertices in each part: lines in distinct parallel classes intersect, while lines in the same class do not. Its flag complex is the simplicial join of \(q+1\) discrete \(q\)-point spaces. The join homology formula, or induction using \(X*Y\simeq\Sigma(X\wedge Y)\), gives
\[
B\simeq\bigvee^{(q-1)^{q+1}}S^q.
\]
In particular \(B\) is simply connected. Every map from a connected one-dimensional CW complex into a simply connected space is null-homotopic, so the attaching map \(G_{\mathcal A}\to B\) is null. Its cofiber therefore splits as
\[
K\simeq B\vee\Sigma G_{\mathcal A}.
\]
The incidence graph has \(q^2+q(q+1)=2q^2+q\) vertices and \(q^2(q+1)\) edges. Since it is connected, its integral first Betti number is
\[
q^2(q+1)-(2q^2+q)+1=(q-1)^2(q+1).
\]
Thus \(G_{\mathcal A}\simeq\bigvee^{(q-1)^2(q+1)}S^1\), and suspending gives the claimed scale-two wedge.

At threshold \(1\), the clique complex of the triangle-free bipartite graph is exactly the graph, establishing the circle wedge. At threshold \(3\), every point vertex has distance at most \(3\) from every vertex, so that Rips complex is a cone. At threshold \(4\), the diameter is reached and the complex is a full simplex. Distances are integral, so there are no changes between successive thresholds. All positive-dimensional classes present at threshold \(1\) die at threshold \(2\); every positive-dimensional class born at threshold \(2\) dies at threshold \(3\). This proves the barcode formula.

## Verification

The accompanying `verify_affine_rips.py` reconstructs incidence graphs of the prime affine planes of orders \(2\) and \(3\) from coordinates, independently recomputes all shortest-path distances, exhaustively enumerates the cliques of the scale-one and scale-two graphs, constructs exact mod-two simplicial boundary matrices and computes their ranks by binary elimination. The order-two case is included as a regression check, not as part of the stated scope. For \(q=3\), it verifies \(21\) vertices, \(36\) incidence edges, scale-two face vector \((21,126,282,255,135,84,36,9,1)\), and reduced mod-two Betti ranks \(16\) in degrees \(2\) and \(3\), zero otherwise. It checks the scale-three cone apex and scale-four diameter assertions without enumerating the exponential full simplex. Execution returns `VERIFY_OK`.

The code checks two small prime orders exactly; the conclusions for arbitrary existing affine planes, including non-Desarguesian ones, follow from the incidence-axiom proof above and do not depend on numerical extrapolation. The topological argument yields integral sphere wedges, so the barcode multiplicities hold over every field.

## Relationship to prior work

Adamaszek and Adams establish the Vietoris–Rips homotopy viewpoint in an archive-era paper on metric circles (first public version 2015-03-12; primary classification includes 55U10); their computation does not address incidence graphs or affine planes. Adamaszek's earlier work on clique complexes of graph powers treats cycles and squares of edge-subdivision graphs, but an affine-plane incidence graph of order at least three is not an edge-subdivision graph: its line vertices have degree \(q\ge3\), and its point vertices have degree \(q+1\). Kawamura's bipartite-graph-square analysis establishes relations among homology and fundamental groups of the flag complexes on the bipartition classes; its theorems do not compute the affine-plane mixed wedge or its persistence barcode.

A published computation for finite **projective** planes establishes a scale-two wedge of \(q^3\) two-spheres for their incidence graphs. That calculation is not the affine result: all distinct projective lines intersect, so the corresponding line-only flag complex is a simplex, while affine lines occur in parallel classes and their line-only flag complex is a noncontractible \(q\)-sphere wedge. The homotopy type of the projective graph's Rips complex does not determine the type of the proper induced affine subgraph obtained by deleting incidence vertices. The exceptional order-two affine graph is the subdivided complete graph on four vertices and falls under a previously known edge-subdivision calculation; the novel mixed-dimensional phenomenon here begins at order three.

## Limitations

The classification is for unit-edge shortest-path metrics and the inclusive scale convention. It does not address arbitrary weighted incidence graphs, generalized partial linear spaces lacking an affine parallelism, or existence of affine planes at unspecified orders. Although the main covering candidates were compared at statement level and their primary text inspected, obscure, unindexed incidence-geometry or graph-power treatments could contain an equivalent calculation. The finite verifier cannot replace the all-order topological proof.

## References

- M. Adamaszek and H. Adams, *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669 (v1 submitted 2015-03-12), *Pacific Journal of Mathematics* **290** (2017), 1–40, DOI: 10.2140/pjm.2017.290.1. Primary MSC includes 55U10.
- M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (v1 submitted 2011-04-03).
- K. Kawamura, *A variant of the bipartite relation theorem and its application to clique graphs*, *Contributions to Discrete Mathematics* **6** (2011), 91–100, DOI: 10.55016/ojs/cdm.v6i2.62059.
- *Scale-two Vietoris–Rips complexes of finite projective-plane incidence graphs*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-scale-two-vietoris-rips-complexes-of-finite-projective-plane-inc--c3740b96b3c3 (inspected full `RESULT.md`).
