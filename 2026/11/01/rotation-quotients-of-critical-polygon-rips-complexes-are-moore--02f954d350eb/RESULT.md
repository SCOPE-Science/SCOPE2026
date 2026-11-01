# Rotation quotients of critical polygon Rips complexes are Moore spaces

## Finding
For each integer \(k\ge2\), put \(n=3k\). Equip the vertex set \(\mathbb Z/n\mathbb Z\) of a cycle with its shortest-path metric, and form the inclusive Vietoris--Rips simplicial complex
\[
X_k=\operatorname{VR}_{\le k}(V(C_n),d)=\operatorname{Cl}(C_n^k).
\]
The canonical cyclic rotation \(r(i)=i+1\) acts on the geometric realization. For the **ordinary topological orbit space** there is a homotopy equivalence
\[
\boxed{\ |X_k|/\langle r\rangle\simeq S^1\cup_{\deg k}D^2=M(\mathbb Z/k,1).\ }
\]
Thus \(\pi_1\cong H_1(-;\mathbb Z)\cong\mathbb Z/k\), while all other reduced integral homology vanishes. The ordinary quotient has arbitrarily large torsion in degree one even though the unquotiented complex has the *previously established* homotopy type \(\bigvee^{k-1}S^2\) (Adamaszek, Corollary 6.7). The assertion concerns neither the Borel homotopy quotient nor the Rips complex of the quotient vertex metric: the latter is a single vertex because the rotation action is transitive on the vertices.

## Assumptions and scope
All complexes here are finite, abstract, and geometrically realized before quotienting. A face means a set of vertices having pairwise cyclic distance at most \(k\). The quotient identifies geometric points under the cyclic action, including the action *within* a setwise-invariant triangle; identifying vertex orbits first would give a different construction. The orbit theorem holds for every integer \(k\ge2\), with no primeness assumptions.

For \(1\le d\le k\), define an auxiliary rotation-invariant simplicial complex \(A_d\) by taking the full simplices
\[
F_i^{(d)}=\{i,i+1,\ldots,i+d\},\qquad i\in\mathbb Z/n\mathbb Z,
\]
and all their faces. Thus \(A_1=C_n\) as a simplicial circle.

## Proof
**1. Exhaustive clique decomposition.** Every maximal face of \(X_k\) is either contained in some \(F_i^{(k)}\), or is exactly one of the \(k\) equilateral triangles
\[
T_j=\{j,j+k,j+2k\},\qquad j=0,1,\ldots,k-1.
\]
To check completeness, translate a vertex of an arbitrary clique to zero. Every other vertex has a representative in \([-k,k]\). If vertices occur on both sides, let \(-a\) be the leftmost and \(b\) the rightmost, with \(1\le a,b\le k\). The cyclic distance bound for this pair gives either \(a+b\le k\) or \(a+b\ge2k\). In the first case the clique fits in the interval \([-a,b]\) of length at most \(k\). In the second case necessarily \(a=b=k\). Any additional vertex must be adjacent to both \(-k\) and \(k\), as well as zero, and a direct intersection of their cyclic distance neighborhoods yields no fourth vertex; this is precisely an equilateral triangle. Hence
\[
X_k=A_k\cup\bigcup_{j=0}^{k-1}T_j,
\]
with each \(T_j\cap A_k=\partial T_j\) and no triangle interiors shared.

**2. Equivariant collapse of the circular-arc part.** For each \(2\le d\le k\), the faces of \(A_d\setminus A_{d-1}\) are exactly the faces containing a cyclic length-\(d\) edge \(e_i=\{i,i+d\}\). Such a face lies in the unique simplex \(F_i^{(d)}\) and contains no other cyclic length-\(d\) edge. The uniqueness follows because \(d\le k=n/3\), and the only two vertices at distance \(d\) inside an interval of length \(d\) are its endpoints. For each \(i\), pair faces containing \(e_i\) but not \(i+1\) with the corresponding faces also containing \(i+1\). All pairs have codimension one, form an acyclic cone matching inside a single simplex, and different edge-index families do not interact: an unmatched boundary facet either has the same distinguished length-\(d\) edge or has dropped into \(A_{d-1}\). The matching is invariant under \(r\), and every matched face has trivial rotational stabilizer (since its distinguished edge does). Its free orbit of elementary collapses descends to the quotient. Thus for each \(d\), \(A_d/\langle r\rangle\) collapses to \(A_{d-1}/\langle r\rangle\), and consequently
\[
A_k/\langle r\rangle\simeq C_n/\langle r\rangle\cong S^1.
\]
Crucially this collapse can be viewed relative to the target quotient circle and does not identify the exceptional triangle interiors.

**3. Attaching degree.** The \(k\) equilateral triangles form one rotation orbit. The setwise stabilizer of \(T_0\) is the order-three subgroup \(\langle r^k\rangle\), acting by an orientation-preserving rotation on its three vertices. Its geometric quotient \(T_0/\langle r^k\rangle\) is a closed disk, and the boundary covering \(\partial T_0\to\partial(T_0/\langle r^k\rangle)\) has degree \(3\).

The edge \([i,i+k]\) within \(A_k\) is homotopic relative endpoints, via triangular faces of \(F_i^{(k)}\), to the forward chain \([i,i+1]+\cdots+[i+k-1,i+k]\). Therefore the oriented boundary of \(T_0\), viewed in \(A_k\), is homologous to the positive full \(n\)-edge cycle exactly once. Upon quotienting by all \(n\) rotations, the rim circle \(C_n\) maps with degree \(n\) to \(C_n/\langle r\rangle\). The quotient triangle boundary circle consequently attaches to \(A_k/\langle r\rangle\) with degree \(n/3=k\) (the orientations can change the sign, immaterial for the Moore space).

**4. Homotopy conclusion.** In the genuine CW orbit space the one orbit of exceptional triangles contributes exactly one disk, attached to \(A_k/\langle r\rangle\) with degree \(k\). Passing along the quotient collapse of step 2 induces a homotopy equivalence of the attached spaces, so the result is \(S^1\cup_{\deg k}D^2\). Its cellular boundary in degrees two to one is multiplication by \(k\). Van Kampen gives the cyclic presentation \(\langle t\mid t^k=1\rangle\), proving the claimed fundamental group and integral homology.

## Verification
The supplied standalone program `verify_orbit_homology.py` constructs every simplex for \(k=2,3,4\), barycentrically subdivides, takes the **geometric** cyclic orbit on face flags, and forms oriented cellular boundary matrices over \(\mathbb F_2\) and \(\mathbb F_3\). Since the action is without inversions on the barycentric subdivision, those matrices compute the true orbit-space homology. It reproduces the predicted characteristic-dependent Betti numbers: for \(k=2\), only characteristic two gives one-dimensional first and second homology; for \(k=3\), only characteristic three does; for \(k=4\), characteristic two does and three does not. These finite verifications support but are not substituted for the uniform proof.

## Relationship to prior work
Adamaszek (2011 preprint; 2013 publication), Corollary 6.7, already determines \(\operatorname{Cl}(C_{3k}^{k})\simeq\bigvee^{k-1}S^2\). Adamaszek--Adams (2015 preprint; 2017 publication) develops a much wider classification of circle Rips complexes and explicit cross-polytopal homology generators. Neither inspected treatment computes the **ordinary orbit space of the critical finite polygon under its full vertex rotation group**. Adams--Heim--Peterson (2019 preprint) investigates the relationship between Rips of metric quotient and quotients of Rips at sufficiently small scales; those comparison hypotheses cannot identify the present critical-scale quotient, and the metric orbit set in this example is a singleton. The contribution is the rotation-quotient homotopy classification and its integral torsion, *not* the known homotopy type or Betti numbers of the original complexes.

## Limitations
The result does not classify quotients by reflection groups, intermediate rotation subgroups, or other critical winding fractions. The computation is not a substitute for the proof and covers only three sizes and two coefficient fields. Originality is based on inspected accessible literature and actual overlap searches; an unindexed equivalent treatment is possible. No independent mathematical audit has been performed.

## References
1. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (first public 2011-04-03), especially Proposition 2.2 and Corollary 6.7. https://arxiv.org/html/1104.0433v3
2. M. Adamaszek and H. Adams, *The Vietoris--Rips complexes of a circle*, arXiv:1503.03669 (first public 2015-03-12), particularly the cyclic graph classification and Section 8. https://arxiv.org/html/1503.03669v2
3. H. Adams, M. Heim and C. Peterson, *Metric thickenings and group actions*, arXiv:1911.00732 (2019), especially Section 3 on comparisons between metric quotient and Rips quotient. https://arxiv.org/abs/1911.00732
