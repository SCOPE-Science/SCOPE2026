# Complete branch, pole, and particle symmetry of two-point banana-graph configuration homology

## Finding
Let \(m\ge3\), and let \(\Theta_m\) be the graph with two poles \(p,q\) joined by \(m\) internally disjoint paths, each subdivided into three edges. Put
\[
F_m=\operatorname{Conf}_2(\Theta_m)=\{(x,y)\in\Theta_m^2:x\ne y\},\qquad B_m=F_m/\langle\tau\rangle,
\]
where \(\tau(x,y)=(y,x)\). Branch permutations form \(S_m\); \(\rho\) interchanges \(p\) and \(q\), reversing all paths. These actions commute with \(\tau\).

Let \(W_m\) be the rational vector space on directed pairs \(e_{ij}\), \(1\le i\ne j\le m\), and let \(u=\sum_{i\ne j}e_{ij}\). Give \(W_m\) the commuting actions
\[
\sigma e_{ij}=e_{\sigma(i)\sigma(j)},\qquad
\tau e_{ij}=-e_{ji},\qquad \rho e_{ij}=-e_{ij}.
\]
The line \(\mathbb Q u\) is invariant. As representations of \(S_m\times\langle\rho\rangle\times\langle\tau\rangle\),
\[
\boxed{H_1(F_m;\mathbb Q)\cong W_m/\mathbb Q u.}
\]
All rational homology above degree one vanishes and \(F_m\) is connected. In particular, \(\dim H_1(F_m;\mathbb Q)=m(m-1)-1\).

For \(\sigma\in S_m\), write \(f(\sigma)\) for its number of fixed branches and \(t(\sigma)\) for its number of two-cycles. Every character value is
\[
\boxed{\operatorname{tr}\bigl(\sigma\rho^h\tau^b\mid H_1(F_m;\mathbb Q)\bigr)=(-1)^h\begin{cases}
f(\sigma)(f(\sigma)-1)-1,&b=0,\\
1-2t(\sigma),&b=1,
\end{cases}}
\qquad h,b\in\{0,1\}.
\]

For unordered particles the invariant eigenspace under \(\tau\) gives the complete rational branch-and-pole representation
\[
\boxed{H_1(B_m;\mathbb Q)\cong\bigwedge^2\mathbb Q^m\otimes\varepsilon_\rho,}
\]
where \(S_m\) permutes the basis of \(\mathbb Q^m\) and \(\rho\) acts through its nontrivial sign \(\varepsilon_\rho\). Thus \(\dim H_1(B_m;\mathbb Q)=\binom m2\), and its branch character is \(\binom{f(\sigma)}2-t(\sigma)\), reversed by \(\rho\). Both spaces have vanishing *integral* homology in all degrees at least two; the theorem does not claim an integral lattice identification in degree one.

## Assumptions and scope
The parameter is every integer \(m\ge3\). Branch paths have precisely three edges, a symmetry-preserving sufficient subdivision for two-particle Abrams cubical models. The same topological graph with unsubdivided parallel edges has the same configuration spaces and actions up to equivariant homeomorphism after subdivision. There are no collisions; neither configuration space is a sink-configuration space. Both poles are distinguishable from the degree-two internal vertices when \(m\ge3\). All representation isomorphisms in the finding are over \(\mathbb Q\). The boundary case \(m=2\) is excluded: the ordered two-particle configuration of a circle is disconnected.

## Proof
**1. The exact cubical model and connectivity.** Put \(a_i,b_i\) along path \(p-a_i-b_i-q\), with all \(3m\) edges oriented from \(p\) to \(q\). The Abrams cubical two-particle model \(D_2(\Theta_m)\) has as its zero-cells ordered pairs of distinct vertices, as its one-cells a moving edge in one coordinate and a stationary vertex disjoint from the edge closure, and as its two-cells ordered pairs of edges whose closures are disjoint. The inclusion into \(F_m\) is a homotopy equivalence for this subdivision; it is equivariant for all stated symmetries, hence induces their true homology actions, even without choosing an equivariant inverse. Its cell counts are
\[
(c_0,c_1,c_2)=(4m^2+6m+2,\ 12m^2,\ 7m^2-5m).
\]
The unordered quotient has half as many cells in each dimension. The zero-/one-cell graph of the ordered model is connected when \(m\ge3\): two particles can be separated onto different branches, transported to the poles, and interchanged using a third vacant branch. The quotient is connected as well.

**2. Vanishing of second homology.** Embed the ordered cubical two-chains in \(C_1(\Theta_m;\mathbb Z)\otimes C_1(\Theta_m;\mathbb Z)\), extending their coefficients by zero on incident edge pairs. Let \(z\) be a two-cycle. The horizontal and vertical boundary components occupy different direct summands of the cubical one-chains, so both tensor partial boundaries vanish separately. Therefore, along each path, its coefficient is independent of which of that path's three edges is chosen in each coordinate. Write that coefficient \(\lambda_{ij}\) for branch pair \((i,j)\). Since the pair of first edges \((p a_i,p a_j)\) is forbidden for *every* \(i,j\) (the closures share \(p\)), it follows that every \(\lambda_{ij}=0\). Hence the ordered degree-two boundary is injective over \(\mathbb Z\). The two-sheeted cover transfers an unordered two-cycle to two disjointly supported labeled lifts; its chain-level transfer is injective, proving the same integral vanishing for the unordered model. Both models are two-dimensional, so all higher homology vanishes as well.

**3. Equivariant Lefschetz calculation.** Let \(f=f(\sigma)\), \(t=t(\sigma)\), and let \(h,b\in\{0,1\}\) indicate pole and particle exchanges. For the ordered model, count fixed oriented cells in each dimension. The signed chain traces \((T_0,T_1,T_2)\) are

| \(h,b\) | \(T_0\) | \(T_1\) | \(T_2\) |
|:--:|:--:|:--:|:--:|
| \(0,0\) | \((2f+2)(2f+1)\) | \(12f^2\) | \(7f^2-5f\) |
| \(0,1\) | \(4t\) | \(0\) | \(-2t\) |
| \(1,0\) | \(0\) | \(0\) | \(f(f-1)\) |
| \(1,1\) | \(2+2f+4t\) | \(0\) | \(-(2f+6t)\) |

For example, the final row's fixed ordered vertex pairs come from the pole transposition, the \(f\) internal swaps on fixed branches, and two internal swaps for each branch two-cycle. The fixed two-cells are exchanged pairs of first/last edges or of middle edges; exchanging particle coordinates reverses square orientation. Reversing both graph-edge orientations preserves square orientation. Every listed trace is therefore a signed fixed-cell count, with no homological assumption.

Since the only remaining homology degrees are zero and one, and \(H_0(F_m;\mathbb Q)\) is trivial as a representation, the Hopf trace formula yields
\[
\operatorname{tr}(g\mid H_1)=1-T_0(g)+T_1(g)-T_2(g).
\]
Substitution of the four rows gives exactly the boxed character formula.

**4. Identification of the modules.** The action of \(S_m\) on \(W_m\) has trace \(f(f-1)\); adjoining \(\tau\) as negative transposition gives trace \(-2t\) on \(\sigma\tau\); \(\rho\) multiplies both by \(-1\). The line \(\mathbb Q u\) has character \((-1)^{h+b}\). Subtraction yields precisely the computed homology character on every element. Semisimplicity of rational representations of the finite group proves the isomorphism. Finally, finite-cover transfer identifies \(H_1(B_m;\mathbb Q)\) with the \(\tau\)-positive part of \(H_1(F_m;\mathbb Q)\). The \(\tau\)-positive vectors in \(W_m\) are the antisymmetric pairs \(e_{ij}-e_{ji}\); the removed line is \(\tau\)-negative. Therefore the positive part is \(\bigwedge^2\mathbb Q^m\), with \(\rho\)-sign twist, as asserted.

## Verification
The supplied standalone `verify.py` reconstructs the ordered zero-, one-, and two-cell sets directly and computes signed fixed-cell traces for all \(S_m\) elements at \(m=3,4,5\) and a selected sample at \(m=6\), each with both pole- and particle-exchange choices. It checks all \(672\) character identities by exact integer arithmetic. The general proof above is not a finite enumeration.

## Relationship to prior work
Abrams-type cubical models and prior graph-braid homology and topological-complexity studies justify examining banana-graph configurations. Lütgehetmann–Recio-Mitter (arXiv:1806.00659, Section 5) establish homotopy-dimensional and topological-complexity statements for banana graph configurations; An–Maciazek (arXiv:2006.15256) study geometric generators and relations for general graph braid groups; and Maciazek et al. (DOI 10.1007/s00220-019-03583-5) examine configurations on complete bipartite and theta graphs. Their discussed results do not state the present complete \(S_m\times C_2\times C_2\) rational character or its explicit signed ordered-pair module. The known ranks or generators alone do not logically determine the action of all branch, pole, and particle symmetries. Related published records for three-particle generalized-theta homology address a different configuration space and homological degree.

## Limitations
The isomorphism class of the rational representation is determined; no integral identification of the degree-one lattice, explicit integral generating cycles, or new claim about fundamental-group presentations is made. Only two distinct particles are considered. The argument relies on the standard two-point cubical deformation-retract theorem. The literature comparison cannot exclude equivalent work under unindexed terminology, and independent mathematical validation has not been performed.

## References
1. D. Lütgehetmann and D. Recio-Mitter, *Topological complexity of configuration spaces of fully articulated graphs and banana graphs*, arXiv:1806.00659 (initial public version 2018-06-02), Section 5. https://arxiv.org/abs/1806.00659
2. B. H. An and T. Maciazek, *Geometric presentations of braid groups for particles on a graph*, arXiv:2006.15256 (2020), especially Sections 2–3. https://arxiv.org/abs/2006.15256
3. T. Maciazek and collaborators, *Non-Abelian Quantum Statistics on Graphs*, Commun. Math. Phys. (2019), especially the discussion of theta and complete-bipartite graph configuration homology. https://doi.org/10.1007/s00220-019-03583-5
4. A. Abrams, *Configuration spaces of braid groups of graphs*, University of California, Berkeley dissertation (2000), cited for the standard sufficiently subdivided cubical configuration model.
