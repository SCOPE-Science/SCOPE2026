# Two-torsion in unstable bidirected complete-bipartite multipath complexes

## Finding

For each integer \(n\ge1\), let \(D_n\) be the digraph obtained by replacing every edge of \(K_{2,n}\) with both directed arcs. Let \(X_n\) be its **ordinary multipath simplicial complex**, with one simplicial vertex for each directed arc, and a face for every collection of arcs whose connected components are (possibly trivial) directed paths. The following exact integral homotopy equivalences hold:

\[
X_4\simeq\left(\bigvee^{7}S^2\right)\vee M(\mathbb Z/2,2),\qquad
X_5\simeq M(\mathbb Z/2,2)\vee\left(\bigvee^{31}S^3\right),\qquad
X_6\simeq\bigvee^{169}S^3.
\]

Here \(M(\mathbb Z/2,2)=S^2\cup_{2}e^3\) is the mod-two Moore space (one degree-two three-cell attaching map). In particular,
\[
\widetilde H_2(X_4;\mathbb Z)\cong\mathbb Z^7\oplus\mathbb Z/2,
\qquad\widetilde H_2(X_5;\mathbb Z)\cong\mathbb Z/2,
\qquad\widetilde H_3(X_5;\mathbb Z)\cong\mathbb Z^{31}.
\]

**Each \(D_n\) is itself one unstable dynamical module** under Definitions 4.1, 4.2, and 4.4 of Caputi–Collari–Di Trani–Smith. Consequently, \(D_4\) and \(D_5\) contradict the stability–torsion conjecture stated in the introduction of *On the homotopy type of multipath complexes* (arXiv:2208.04656v1): torsion need not come from a stable dynamical module.

Within this fixed family, \(n=4\) is the first torsion-bearing case: the exact smaller-case chain calculations yield no integral torsion for \(n=1,2,3\). No all-\(n\) homotopy formula is asserted.

## Assumptions and scope

The two left vertices are indexed \(0,1\), the \(n\) right vertices are indexed \(2,\ldots,n+1\), and all \(4n\) arcs occur exactly once. All graph vertices are distinct; a directed two-cycle is forbidden in a multipath, as is every other oriented cycle. Thus an arc subset is a simplex if and only if (i) every graph vertex has at most one selected incoming and one selected outgoing arc, and (ii) the selected successor relation has no directed cycle. This characterization implements the source definitions of a disjoint union of directed paths. Every simplex contains at most four arcs because its two left vertices can contribute at most one incoming and one outgoing arc apiece; the complex is therefore at most three-dimensional for **all** \(n\).

Integral homology and integral CW attaching maps are used. The stated sphere wedges are homotopy equivalences of geometric realizations, not merely homology-rank statements. There is no claim about the corresponding (different) one-way-oriented bipartite graph or the ordinary undirected matching complex.

## Proof

**1. Exact simplicial enumeration.** For each \(n\in\{1,2,3,4,5,6\}\), enumerate every subset of size one through four of the \(4n\) arcs; reject a subset when some vertex receives more than one selected arc, emits more than one, or belongs to a directed cycle. The complete simplex face vectors \((f_0,f_1,f_2,f_3)\) are, respectively,
\[
(4,2,0,0),\ (8,16,8,0),\ (12,42,48,12),\ (16,80,144,72),\ (20,130,320,240),\ (24,192,600,600).
\]
The finite verifier checks face closure and \(\partial^2=0\) using the alternating signed simplicial boundary, with vertices ordered by arc index.

**2. Reproducible discrete-Morse matching.** For each arc index in increasing order, pair every currently unmatched nonempty simplex not containing that arc with the currently unmatched simplex obtained by adjoining it, whenever both exist. Remove each paired pair before proceeding. The full Hasse diagram is oriented from larger to smaller simplex at an unmatched incidence, and reversely at a matched incidence. The verifier constructs **every incidence**, computes the directed topological ordering and confirms that no directed cycle exists. For \(n=4,5,6\), the complete Hasse incidence counts are \(880,2180,4584\), and the matched-pair counts are \(151,338,623\). The remaining critical cells (dimension: count) are:
\[
\begin{array}{c|ccc}
n&0&2&3\\\hline
4&1&8&1\\
5&1&1&32\\
6&1&0&169
\end{array}
\]
All unlisted dimensions have zero critical cells. Forman's discrete Morse theorem gives a CW complex with precisely these critical cells; the matching removes no essential attaching information.

**3. Exact integral Morse differentials.** For a matched lower simplex \(\sigma\) paired to an upper simplex \(\tau\), solve the integral boundary equation \(\partial\tau=\epsilon\sigma+\sum_{\rho\ne\sigma}c_\rho\rho\) for \(\sigma\), where \(\epsilon=\pm1\). Recursively substitute in every higher-cell boundary, using the acyclic orientation to guarantee termination. Treat unmatched critical cells as generators and matched upper cells as canceled. This yields the cellular Morse differential with **integer signs**, not merely a mod-two proxy.

For \(n=4\), the unique critical three-cell has a boundary vector in the basis of eight critical two-cells with six nonzero entries, four equal to \(-2\) and two equal to \(2\); its entries have greatest common divisor \(2\). Thus, after a unimodular change of basis, its attaching degree vector is \((2,0,\ldots,0)\). Because the two-skeleton is \(\bigvee^8S^2\), the Hurewicz isomorphism \(\pi_2\cong H_2\) classifies this three-cell's attaching map. Consequently the resulting CW type is \(M(\mathbb Z/2,2)\vee\bigvee^7S^2\).

For \(n=5\), the one critical two-cell and thirty-two critical three-cells give a \(1\times32\) integral Morse boundary matrix. Exactly twenty-six entries are nonzero, all even, and their greatest common divisor is **exactly two** (the observed coefficients are among \(\pm2, -4,-6\)). Integral Smith reduction of this rank-one matrix gives one invariant factor two; a unimodular change of three-cell basis reduces it to a single degree-two attaching map and thirty-one null attachments, giving \(M(\mathbb Z/2,2)\vee\bigvee^{31}S^3\). At \(n=6\), there are only a single critical vertex and 169 critical three-cells, so all attach to a point and form the displayed wedge.

**4. The smaller cases and independent coefficient check.** At \(n=1,2,3\) the complete exact Morse differential is zero, and therefore their integral homology is torsion-free; no unsupported homotopy classification in these lower cases is needed. As a separate check, direct sparse Gaussian elimination on the **original simplicial** boundary matrices over \(\mathbb F_2\) and \(\mathbb F_3\) yields ranks of \((\partial_1,\partial_2,\partial_3)\): \(n=4\), \((15,65,71)\) versus \((15,65,72)\); \(n=5\), \((19,111,208)\) versus \((19,111,209)\). These independent rank differences agree with exactly one integral two-torsion invariant at each size; the exact Smith factor is obtained from the integer Morse differential, rather than inferred from finite-field data alone.

**5. The dynamical-module counterexample.** Definitions 4.1–4.4 in the 2022 source say a dynamical region \(R\subseteq G\) is a connected full subgraph with at least one arc, with (a) boundary vertices stable within \(R\) and its complement, and (b) every oriented cycle of \(G\) touching an arc of \(R\) wholly contained in \(R\); a dynamical module is a minimal region. In \(D_n\), every arc lies in an oriented two-cycle together with its reverse. If a dynamical region \(R\) contains an arc, condition (b) forces its reverse into \(R\). Both endpoints then have positive in- and outdegree **inside \(R\)**, so condition (a) forbids either endpoint from lying on the boundary. Consequently **every** arc incident to these endpoints lies in \(R\). Propagating through the connected bipartite graph forces \(R=D_n\). Conversely \(D_n\) itself is a dynamical region with empty boundary. It is therefore the unique minimal dynamical region and hence a dynamical module. Every vertex of \(D_n\) has positive indegree and outdegree, so it is an **unstable**, not stable, dynamical module. Together with the proven integral \(\mathbb Z/2\)-torsion at \(n=4,5\), this disproves the published conjecture for its precise stated class of modules.

## Verification

The standalone Python 3 standard-library file `verify_moore.py` builds all simplices, checks downward closure and \(\partial^2=0\), independently verifies complete matching acyclicity, computes signed integral Morse cancellations and mod-two and mod-three original-chain boundary ranks, and enforces numerical assertions for each relevant value of \(n\). Execute `python3 verify_moore.py` in the directory containing this document and the checker. Expected final message: `BIDIRECTED_K2N_TWO_TORSION_UNSTABLE_MODULE_MOORE_VERIFIED`.

The proof of the dynamical-region property is structural and does not depend on an unreported exhaustive digraph census. Finite computation is invoked **only** for the three specified homotopy types and the three strictly smaller torsion tests, not to infer an all-parameter classification.

## Relationship to prior work

Caputi–Collari–Di Trani–Smith explicitly formulate the stability–torsion conjecture in the 9 August 2022 preprint, and derive complete-bipartite Euler information for **alternating** orientations, not the bidirected objects treated here. The subsequent 2024 weak categorical quiver-minor paper gives general bounded torsion properties and comparisons with matching complexes in acyclic digraphs; its acyclic hypothesis excludes \(D_n\), and its specific torsion examples do not imply the above rank-one integral Moore decompositions. Vrećica–Živaljević study cycle-free chessboard complexes for **complete directed graphs** and general connectivity, not this specified bipartite-induced cycle-free subcomplex's precise integral homotopy or dynamical-module status. An earlier path-poset study supplies the definitions and computational setting, not these homotopy equivalences.

## Limitations

This is a reproducible finite classification for \(n\in\{4,5,6\}\), with a minimality check inside the restricted family for \(n<4\). It does not prove a statement for arbitrary \(n\), classify all unstable modules, or establish global minimality among all digraphs. The 2022 arXiv version of the conjecture is verified as its original public statement; no claim is made about subsequent author positions. The literature searches and inspected primary texts cannot rule out every unpublished or unindexed equivalent. The finite calculation uses a deterministic exact integer algorithm and ordinary mathematical proof; it has not undergone independent external audit.

## References

1. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (9 August 2022), especially Definitions 2.1–2.2, 4.1–4.4, Section 3 and the stability–torsion conjecture in the introduction; https://arxiv.org/pdf/2208.04656 .
2. S. T. Vrećica and R. T. Živaljević, *Cycle-free chessboard complexes and symmetric homology of algebras*, arXiv:0710.5252 (2007), Sections 1–2; https://arxiv.org/pdf/0710.5252 .
3. L. Caputi, C. Collari and E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, arXiv:2401.01248v1 (2024), Sections 1 and 4; https://arxiv.org/pdf/2401.01248 .
4. L. Caputi, C. Collari and S. Di Trani, *Combinatorial and topological aspects of path posets, and multipath cohomology*, arXiv:2110.11206 (2021); https://arxiv.org/abs/2110.11206 .
