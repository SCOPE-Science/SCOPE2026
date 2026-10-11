# Čech retention and Rips collapse for projective-plane hypergraphs
## Finding
Let \(\Pi=(P,L)\) be any finite projective plane of order \(q\ge 2\), and put \(N=q^2+q+1\). Define the hypergraph \(\mathcal E_\Pi\) on ground set \(P\) by taking as hyperedges every singleton \(\{p\}\), with \(p\in P\), together with every projective line \(\ell\in L\). For the order complex \(S_{\mathcal E_\Pi}\), the Čech complex \(\mathcal N_{\mathcal E_\Pi}\), and the pairwise-intersection Vietoris–Rips complex \(\mathcal{VR}_{\mathcal E_\Pi}\) in the sense used for hypergraphs by Jost and Zhang, one has
\[
|\mathcal E_\Pi|\simeq |S_{\mathcal E_\Pi}|\simeq |\mathcal N_{\mathcal E_\Pi}|\simeq \bigvee^{q^3}S^1,
\qquad
|\mathcal{VR}_{\mathcal E_\Pi}|\simeq *.
\]
Thus the Čech construction retains the full homotopy type in this natural family, while the pairwise-intersection Rips construction erases all \(q^3\) independent loops.

## Assumptions and scope
A finite projective plane of order \(q\) has \(N=q^2+q+1\) points and the same number of lines; every point lies on \(q+1\) lines, every line contains \(q+1\) points, every two distinct points lie on a unique line, and every two distinct lines meet in a unique point. No Desarguesian or prime-power assumption is used.

The order complex has one vertex for each hyperedge and a simplex for each inclusion chain. The Čech complex has the same hyperedge set as vertices and declares a family to be a simplex when its total intersection is nonempty. The hypergraph Vietoris–Rips complex also has the hyperedges as vertices but declares a family to be a simplex when its members intersect pairwise. These are not graph-metric Vietoris–Rips complexes.

## Proof
The only strict inclusions among distinct hyperedges of \(\mathcal E_\Pi\) are \(\{p\}\subset \ell\) with \(p\in\ell\). Hence \(S_{\mathcal E_\Pi}\) is exactly the point-line incidence graph \(G_\Pi\). It has \(2N\) vertices and \((q+1)N\) edges and is connected. Its cycle rank is therefore
\[
(q+1)N-2N+1=(q-1)(q^2+q+1)+1=q^3.
\]
A connected graph of cycle rank \(q^3\) is homotopy equivalent to \(\bigvee^{q^3}S^1\). Proposition 5.6 of Jost and Zhang identifies \(|S_{\mathcal E_\Pi}|\) as a strong deformation retract of their hypergraph realization \(|\mathcal E_\Pi|\), giving the first two homotopy types.

For the Čech complex, let \(K_\Pi\) be the associated simplicial complex on point set \(P\) whose facets are the projective lines. Jost and Zhang note that \(|\mathcal N_{\mathcal E}|\simeq |K_{\mathcal E}|\) for any hypergraph, so it is enough to reduce \(K_\Pi\). Choose one root point \(r_\ell\) on each line \(\ell\). Because every face with at least two vertices lies on a unique line, the following linewise matching has no conflicts: for each \(\ell\), match every face \(\sigma\subseteq\ell\) with \(r_\ell\notin\sigma\) and \(|\sigma|\ge2\) to \(\sigma\cup\{r_\ell\}\). Any alternating path is trapped in one line and stops after the root is inserted, so the matching is acyclic. Its critical cells are all \(N\) vertices and, on each of the \(N\) lines, the \(q\) root edges \(\{r_\ell,p\}\). Thus the Morse model is a connected graph with \(N\) vertices and \(qN\) edges, whose cycle rank is
\[
qN-N+1=(q-1)(q^2+q+1)+1=q^3.
\]
Therefore \(|\mathcal N_{\mathcal E_\Pi}|\simeq\bigvee^{q^3}S^1\).

Finally, every two line-hyperedges intersect, so all \(N\) line vertices span a simplex in \(\mathcal{VR}_{\mathcal E_\Pi}\). A singleton hyperedge \(\{p\}\) intersects exactly the \(q+1\) line-hyperedges through \(p\), and it intersects no other singleton. Consequently it lies in a unique maximal simplex, namely \(\{\{p\}\}\cup L_p\), where \(L_p\) is the set of lines through \(p\). Any chosen line in \(L_p\) dominates the singleton vertex. Deleting all singleton vertices by dominated-vertex collapses leaves the full simplex on the line vertices. Hence \(|\mathcal{VR}_{\mathcal E_\Pi}|\) is contractible.

## Verification
The proof uses only the axioms and standard counting identities of a finite projective plane, together with the cited general hypergraph-topology statements. The bundled standard-library script independently constructs \(\mathrm{PG}(2,p)\) for \(p\in\{2,3,5\}\), verifies all incidence axioms and counts, recomputes the order-complex and incidence-complex cycle ranks, and checks the dominated-singleton structure of the Rips complex. It reports ranks \(8\), \(27\), and \(125\), agreeing with \(q^3\).

## Relationship to prior work
Jost and Zhang introduced the hypergraph realization used here, proved its strong deformation retraction to the order complex, and explicitly contrasted order, Čech, and pairwise-intersection Vietoris–Rips constructions. Their discussion is qualitative and does not treat finite projective planes. Cook, Migliore, Nagel, and Zanello defined the projective-plane incidence complex \(K_\Pi\) and studied its Stanley–Reisner algebra; their paper does not give the homotopy comparison above.

The closest checked database result concerns the graph-metric Vietoris–Rips complex of the point-line incidence graph at scale \(2\), which is a different construction on a different vertex set and has homotopy type \(\bigvee^{q^3}S^2\). It uses the same incidence-graph cycle rank but does not imply the hyperedge Čech/Rips contrast proved here.

## Limitations
The theorem concerns the specific hypergraph containing all point singletons and all projective lines. Removing the singleton hyperedges or changing the hyperedge family changes the order, Čech, and Rips complexes. No statement is made about embedded homology, graph-metric Rips persistence, or higher-dimensional projective geometries. The finite verifier checks only the Desarguesian prime-order examples \(q=2,3,5\); the general theorem is proved axiomatically and does not depend on those computations.

## References
J. Jost and D. Zhang, “Discrete-to-Continuous Extensions: Lovász Extension and Morse Theory,” arXiv:2003.06021v1 (12 March 2020); Discrete & Computational Geometry, DOI 10.1007/s00454-022-00461-1. In particular, Section 5 defines the hypergraph order, Čech, and Vietoris–Rips complexes and proves the strong deformation retraction to the order complex.

D. Cook II, J. Migliore, U. Nagel, and F. Zanello, “An algebraic approach to finite projective planes,” arXiv:1503.04335; Journal of Algebraic Combinatorics 43 (2016), 495–519. Definition 2.1 is the incidence complex used above.
