# Integral homotopy type of the Möbius–Kantor independence complex

## Finding
Let \(G=\operatorname{GP}(8,3)\), the sixteen-vertex Möbius–Kantor graph, and let \(\operatorname{Ind}(G)\) be the abstract simplicial complex of vertex sets containing no edge of \(G\). Then
\[
\operatorname{Ind}(G)\simeq \left(\bigvee^{4}S^{3}\right)\vee S^{4}.
\]
In particular, the only nonzero reduced integral homology groups are \(\widetilde H_3\cong\mathbb Z^{4}\) and \(\widetilde H_4\cong\mathbb Z\). The proof supplies an explicit perfect discrete-Morse reduction of an eight-vertex Alexander-dual model and checks its one potentially nontrivial integral attaching map.

## Assumptions and scope
Write the vertices of \(G\) as \(u_i,v_i\) with indices \(i\in\mathbb Z/8\mathbb Z\), and its edges as \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\), for all eight indices. This is an undirected simple graph with sixteen vertices and twenty-four edges. We use the ordinary independence complex (not the matching complex, edge ideal, or clique complex of \(G\)). The homotopy equivalence is integral and applies to this graph only.

There is a bipartition
\[
A=\{u_0,u_2,u_4,u_6,v_1,v_3,v_5,v_7\},\qquad
B=\{u_1,u_3,u_5,u_7,v_0,v_2,v_4,v_6\}.
\]
Number the elements of \(A\) in the displayed order \(0,\ldots,7\). Each neighbor set \(N_G(b)\cap A\) is a three-element subset of \(A\). In the order \(u_1,u_3,u_5,u_7,v_0,v_2,v_4,v_6\) on \(B\), their characteristic bit masks are
\[
(19,38,76,137,97,194,148,56),
\]
where the bit mask of \(\sigma\subseteq A\) means \(\sum_{j\in\sigma}2^j\), using the stated numbering.

## Proof
**Incidence-graph reduction.** Regard the eight triples \(\mathcal L=\{N_G(b)\cap A:b\in B\}\) as hyperedges on \(A\). Then \(G\) is exactly the incidence graph of the finite hypergraph \((A,\mathcal L)\). Define its combinatorial Alexander-dual complex
\[
K=\{\sigma\subseteq A:\text{there exists }L\in\mathcal L\text{ with }\sigma\cap L=\varnothing\}.
\]
Tsukuda's incidence-graph homotopy theorem (Corollary 4.11, reference 2) yields \(\operatorname{Ind}(G)\simeq\Sigma K\), where \(\Sigma\) is the ordinary suspension. Both vertex and hyperedge sets are nonempty, as required by that theorem.

**Finite certificate for \(K\).** An exact enumeration of masks from \(1\) through \(255\) gives \(140\) nonempty faces of \(K\), with face vector \((8,28,56,40,8)\) in dimensions zero through four. The following fully specified matching uses no search heuristics. Initially mark every nonempty face unmatched. For each bit \(j=0,1,\ldots,7\), visit nonempty face masks in increasing numerical order. Whenever a face \(m\) lacks bit \(j\) and both \(m\) and \(m+2^j\) are presently unmatched faces, match them and remove them from further consideration. This produces \(67\) pairs and exactly six critical masks:
\[
\begin{array}{c|c}
\text{dimension}&\text{critical masks}\\\hline
0&1\\
2&14,22,82,164\\
3&204
\end{array}
\]
Orient each Hasse cover downward, except reverse the \(67\) matched covers. The attached verifier reconstructs and topologically sorts all \(140\) faces and all \(424\) oriented cover incidences. Since all vertices of this directed graph are removed, it is acyclic. Thus Forman's discrete-Morse theorem gives a CW model for \(K\) with one zero-cell, four two-cells, and one three-cell, and no others.

**Integral attaching degree.** Because no one-cells remain, the two-skeleton of this CW model is \(\bigvee^{4}S^{2}\). Its three-cell has an attaching map from \(S^2\); this map is determined up to homotopy by its four integral degree coordinates, since \(\pi_2(\bigvee^4 S^2)\cong H_2(\bigvee^4 S^2;\mathbb Z)\cong\mathbb Z^4\). The verifier computes the signed algebraic Morse boundary, with oriented faces in increasing vertex order, as
\[
\partial^{\mathrm{Morse}}_3(204)=(0,0,0,0)
\]
relative to the four critical two-cells \((14,22,82,164)\). Explicitly, for every matched lower face \(\sigma\) paired with its codimension-one upper face \(\tau\), the elimination substitutes the signed boundary relation of \(\tau\) for \(\sigma\); paired upper faces contribute zero, critical faces are retained, and the acyclic matching makes these substitutions terminate. Hence the attaching map is nullhomotopic and
\[
K\simeq\bigvee^4S^2\vee S^3.
\]
Suspending this equivalence and using suspension of wedges proves the finding.

## Verification
Run `python3 verify_dual.py` in the directory containing this document. The script independently reconstructs \(G\), both bipartition classes, the eight neighbor masks, every face of \(K\), the \(67\) matched pairs, the acyclic directed Hasse diagram and the zero integral Morse attaching-degree vector. It requires only the Python standard library and prints `DUAL_VERIFY_OK` after its assertions pass.

Run `python3 verify.py` for a separate direct calculation on \(\operatorname{Ind}(G)\). It enumerates \(1{,}090\) nonempty faces with face vector \((16,96,272,376,240,72,16,2)\), checks a \(541\)-pair acyclic matching over \(4{,}272\) directed face incidences, computes the exact integral critical boundary matrix
\[
\begin{pmatrix}0&0\\0&0\\1&1\\-1&-1\\0&0\end{pmatrix},
\]
and directly recomputes all original simplicial boundary ranks over \(\mathbb F_2\). Its primitive rank-one integral matrix also gives the claimed wedge, independently of the eight-vertex dual reduction. Reproducible results do not constitute an independent external audit.

## Relationship to prior work
Barmak (reference 1, Theorem 3.4) proves that independence complexes of triangle-free graphs are suspensions, without computing this graph's integral homotopy decomposition. Tsukuda (reference 2, Corollary 4.11) supplies the general incidence-graph/Alexander-dual reduction applied above, but not the specific six-critical-cell computation or null attaching degree. Fox, Gera, and Stănică (reference 3, Theorem 2.2) determine the independence number of the relevant generalized Petersen graphs; this determines maximal independent-set size, not homotopy type.

The Möbius–Kantor graph also has an ordinary matching complex, but this is the independence complex of its twenty-four-vertex line graph, a different simplicial complex from the sixteen-vertex independence complex studied here. Möbius ladder graphs likewise are not the Möbius–Kantor graph; their general homotopy classification cannot be substituted here.

## Limitations
The result is restricted to \(\operatorname{GP}(8,3)\). It does not classify independence complexes for arbitrary generalized Petersen graphs or all incidence graphs. A finite exact certificate proves the stated finite result, not a parameter-family theorem. Searches of accessible publications and indexed findings have not established that an equivalent previously unindexed calculation does not exist. A plausible same-graph source on graph-theoretic topology (reference 4) was available only at abstract level for this comparison; its possible treatment of the complementary flag complex remains a residual literature risk. No independent audit has been performed.

## References
1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1 (first publicly submitted 2010-07-02), Theorem 3.4; primary MSC 57M15.
2. S. Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics 12 (2017), 28–46, DOI:10.55016/ojs/cdm.v12i1.62277, Corollary 4.11.
3. J. Fox, R. Gera, and P. Stănică, *The Independence Number for the Generalized Petersen Graphs*, publicly accessible author manuscript at https://faculty.nps.edu/pstanica/research/GenPetersen.pdf, Theorem 2.2.
4. O. Knill, *Remarks about the Moebius-Kantor graph*, arXiv:2605.30799 (2026); abstract consulted, full text inaccessible in the current comparison.
5. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complex of Möbius Ladder Graph*, arXiv:2608.30601 (2026); different graph family.
