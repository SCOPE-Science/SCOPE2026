# Scale-three Vietoris–Rips complexes of finite generalized quadrangles
## Finding
Let \(\mathcal Q\) be a finite thick generalized quadrangle of order \((s,t)\), where \(s,t\ge 2\). Let \(P\) and \(L\) be its point and line sets, and let \(\Gamma\) be the bipartite point–line incidence graph with its unweighted shortest-path metric. Using the inclusive convention, for every real \(r\) with \(3\le r<4\),
\[
\operatorname{VR}_{\le r}(\Gamma)\simeq igvee^{s^4t^4} S^3.
\]
More precisely, if \(K_P\) is the clique complex of the point-collinearity graph and \(K_L\) is the clique complex of the line-concurrency graph, then
\[
\operatorname{VR}_{\le 3}(\Gamma)=K_P*K_L,
\qquad
K_P\simeq K_L\simeq igvee^{s^2t^2}S^1.
\]

## Assumptions and scope
A generalized quadrangle of order \((s,t)\) has exactly \(s+1\) points on each line and \(t+1\) lines through each point, with the usual unique-nearest-point axiom for a nonincident point–line pair. The theorem is stated for finite thick generalized quadrangles, so \(s,t\ge2\). The metric is the graph metric on the full incidence graph, and the Rips convention is inclusive: a finite vertex set is a simplex exactly when its diameter is at most the scale.

Because graph distances are integral, the complex is constant for \(3\le r<4\). No assertion is made here about scale \(2\), scale \(4\), weighted metrics, or arbitrary diameter-four bipartite graphs.

## Proof
The incidence graph \(\Gamma\) of a generalized quadrangle has diameter \(4\) and girth \(8\). More explicitly, two distinct points have distance \(2\) exactly when they are collinear and distance \(4\) otherwise; dually, two distinct lines have distance \(2\) exactly when they meet and distance \(4\) otherwise. A point and a line have distance \(1\) when incident and distance \(3\) when nonincident, by the defining generalized-quadrangle axiom.

Therefore every point is within distance \(3\) of every line, while the distance-at-most-three graph induced on \(P\) is precisely the point-collinearity graph and the one induced on \(L\) is precisely the line-concurrency graph. Hence the distance-at-most-three graph is the graph join of these two same-type graphs. Taking clique complexes gives the exact simplicial identity
\[
\operatorname{VR}_{\le3}(\Gamma)=K_P*K_L.
\]

It remains to identify either factor. The maximal simplices of \(K_P\) are exactly the point sets of lines of \(\mathcal Q\). Distinct such simplices intersect in at most one point. For each line simplex, choose an interior point and replace that simplex by the star joining this interior point to its \(s+1\) vertices. The star and the simplex are both contractible CW subcomplexes after a compatible subdivision, so the inclusion of the star is a cofibration and a homotopy equivalence; consequently the simplex strongly deformation retracts onto the star while fixing its vertices. Since distinct line simplices meet only at vertices, these retractions glue. The resulting graph has one original vertex for each point, one new star-center for each line, and one edge for each incidence. It is exactly \(\Gamma\). Thus \(K_P\simeq\Gamma\). The dual argument gives \(K_L\simeq\Gamma\).

For completeness, the standard generalized-quadrangle counts can be recovered directly from the axioms:
\[
|P|=(s+1)(st+1),\qquad |L|=(t+1)(st+1),
\]
and therefore
\[
|E(\Gamma)|=(s+1)(t+1)(st+1).
\]
Since \(\Gamma\) is connected, its cycle rank is
\[
|E|-|P|-|L|+1
=(st+1)(st-1)+1=s^2t^2.
\]
Every connected graph is homotopy equivalent to a wedge of as many circles as its cycle rank, so
\[
K_P\simeq K_L\simeqigvee^{s^2t^2}S^1.
\]
Finally, for based CW complexes, \(X*Y\simeq\Sigma(X\wedge Y)\), and smash products distribute over finite wedges. Thus
\[
K_P*K_L\simeq
\Sigma\left(igvee^{s^2t^2}S^1\wedgeigvee^{s^2t^2}S^1ight)
\simeqigvee^{s^4t^4}S^3.
\]
This proves the claim.

## Verification
The proof is axiomatic and does not rely on finite experimentation. The accompanying `verify.py` is a finite sanity check, not a proof of the general theorem. It constructs the symplectic generalized quadrangles \(W(3,2)\) and \(W(3,3)\) from projective points over \(\mathbb F_2\) and \(\mathbb F_3\), reconstructs their totally isotropic lines and incidence graphs, verifies the required distance pattern and unique-line clique structure, and checks the factor Euler characteristics and incidence-graph cycle ranks.

For \(q=2\), it obtains \(15\) points, \(15\) lines, cycle rank \(16\), and the predicted \(256\) three-spheres. For \(q=3\), it obtains \(40\) points, \(40\) lines, cycle rank \(81\), and the predicted \(6561\) three-spheres. The verifier prints `VERIFY_OK` only after all assertions pass.

## Relationship to prior work
Saleh, Titz Mite, and Witzel determine Vietoris–Rips complexes of Platonic solids and explicitly identify extensions toward spherical-building settings as a natural direction. Their paper fixes the inclusive Rips convention used here and has primary MSC \(55N31\). The present theorem gives a uniform exact scale-three result for the incidence graphs of all finite thick generalized quadrangles rather than for one polyhedral graph.

Cioabă, Guo, Ji, and Mim study clique complexes of strongly regular graphs and verify the key finite-geometric fact that in the point graph of a generalized quadrangle the maximal cliques are its lines and every triangle lies in a unique such maximal clique. Their work concerns higher Laplacian spectra and cohomology rather than the scale-three Rips complex of the full incidence graph. A 2026 preprint of McCabe uses incidence graphs of generalized polygons, including generalized quadrangles, in Rips-filtration lower bounds; its girth criterion preserves the graph clique complex only when \(g\ge3j+1\), which for girth \(8\) reaches \(j=2\) but not the scale \(j=3\) treated here.

The order-\((2,2)\) case specializes to the previously computed \(256\)-sphere result for the Tutte–Coxeter incidence graph. The new content is the uniform factorization, deformation-retraction argument, and exact exponent \(s^4t^4\) for arbitrary finite thick order \((s,t)\).

## Limitations
The theorem uses the full generalized-quadrangle axioms, especially the distance-
\(3\) property for nonincident point–line pairs and the absence of ordinary triangles. It does not claim the same formula for pseudo-generalized-quadrangle strongly regular graphs, for general girth-eight graphs, or for metrics other than the incidence-graph shortest-path metric. The finite verifier checks only the classical symplectic examples with \(q=2,3\); general validity rests on the proof above.

A literature search cannot certify absolute novelty. The closest located works cover Platonic-solid Rips complexes, generalized-quadrangle clique-complex structure, and lower-bound uses of generalized-polygon incidence graphs, but no source located states the scale-three join decomposition and \(s^4t^4\) wedge formula.

## References
1. N. Saleh, T. Titz Mite, and S. Witzel, “Vietoris–Rips complexes of Platonic solids,” arXiv:2302.14388v1, first submitted 2023-02-28; *Innovations in Incidence Geometry* 21 (2024), 17–34, DOI: 10.2140/iig.2024.21.17.
2. S. M. Cioabă, K. Guo, C. Ji, and M. Mim, “Clique complexes of strongly regular graphs, their eigenvalues, and cohomology groups,” arXiv:2508.05871v1; *Linear Algebra and its Applications* 730 (2026), 152–197, DOI: 10.1016/j.laa.2025.10.013.
3. K. McCabe, “Lower Bounds for Approximating the Vietoris–Rips Filtration,” arXiv:2607.06524v1 (2026).
