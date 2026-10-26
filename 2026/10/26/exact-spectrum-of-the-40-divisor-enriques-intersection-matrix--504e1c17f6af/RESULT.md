# Exact spectrum of the 40-divisor Enriques intersection matrix

## Finding
For the 40 distinguished \((-2)\)-divisors on the characteristic-two Enriques surfaces constructed by Katsura and Kondo, the intersection Gram matrix \(G=(D_i\cdot D_j)\) has characteristic polynomial
\[
\chi_G(\lambda)=\lambda^{30}(\lambda-28)(\lambda+12)^9.
\]
Its spectrum is therefore \(28\) with multiplicity one, \(-12\) with multiplicity nine, and \(0\) with multiplicity thirty. The nondegenerate span has rank \(10\) and signature \((1,9)\), matching the signature of the numerical Néron--Severi lattice of an Enriques surface.

## Assumptions and scope
Work with the 40 divisor classes in Sections 5--6 of Katsura--Kondo's one-dimensional family of Enriques surfaces in characteristic \(2\): fifteen duads, fifteen synthemes, and ten non-effective \((-2)\)-divisors called totals. A duad is a two-element subset of six letters; a syntheme is a perfect matching of the six letters into three pairs; a total is an unordered partition into two complementary triples. Each of the 40 classes has self-intersection \(-2\). The claim concerns the intersection matrix defined by that published configuration, not the adjacency matrix of an unweighted graph, and it does not determine the index of the generated sublattice.

## Proof
The published intersection rules determine every entry of \(G\): two duads intersect in \(1\) exactly when they share one letter; two synthemes intersect in \(1\) exactly when they have no pair in common; a duad and a syntheme intersect in \(2\) exactly when the duad is one of the syntheme's pairs. For a total \(T=(A\mid A^c)\), the associated divisor intersects in \(2\) with the six duads lying wholly in either triple and the six synthemes whose three pairs all cross between the triples. Distinct totals intersect in \(2\). All other off-diagonal intersections are zero.

These rules construct a symmetric integer matrix of order \(40\). Direct exact multiplication gives
\[
G^3-16G^2-336G=0,
\]
so every eigenvalue is a root of \(\lambda(\lambda-28)(\lambda+12)\). The exact traces are \(\operatorname{tr}(G)=-80\) and \(\operatorname{tr}(G^2)=2080\). If the multiplicities of \(28,-12,0\) are \(a,b,c\), respectively, then
\[
a+b+c=40,\qquad 28a-12b=-80,\qquad 784a+144b=2080.
\]
Solving gives \(a=1\), \(b=9\), and \(c=30\), proving the characteristic polynomial. Since \(G\) is real symmetric, its inertia is \((1,9,30)\). In particular the divisor classes span a rank-10 sublattice of \(\operatorname{Num}(X)\), whose ambient lattice has signature \((1,9)\). This rank statement does not imply that the sublattice has index one.

## Verification
The included standard-library script `verify.py` constructs the 40 vertices and all intersection numbers from the incidence rules, then checks the matrix identity and traces using exact integer arithmetic. Its output is:

- `PASS: constructed the 40-divisor intersection matrix from the published incidence rules`
- `PASS: exact matrix identity G^3 - 16 G^2 - 336 G = 0`
- `PASS: trace(G) = -80 and trace(G^2) = 2080`
- `CONCLUSION: spectrum 28^1, (-12)^9, 0^30; rank 10; inertia (1, 9, 30)`
- `LIMIT: the spectrum proves full rank in Num(X), not index one of the generated sublattice`

## Relationship to prior work
Katsura and Kondo explicitly construct the 30 nodal curves and ten non-effective \((-2)\)-divisors, give the duad/syntheme/total incidence rules, identify the graph automorphism group with \(\operatorname{Aut}(S_6)\), and prove that the associated reflection subgroup has finite index. They also state that \(\operatorname{Num}(X)\) has signature \((1,9)\). The paper does not give the characteristic polynomial of the 40-by-40 intersection Gram matrix; the present claim is the exact spectrum computed from its incidence data, not a new claim about the already-known signature or finite-index theorem.

Katsura--Kondo note that the same combinatorial graph appears in the level-two Siegel modular threefold studied by van der Geer. The introduction of van der Geer's paper says that intersection theory of the modular subvarieties is not treated there, but a full comparison of all later graph-spectral literature has not been completed. This is retained as a residual novelty risk.

## Limitations
The calculation depends on the published incidence rules for this specific 40-divisor configuration. It does not classify other Enriques surfaces, establish the index of the generated sublattice, or prove a general spectral law for divisor configurations. The result is an exact finite matrix invariant, not a replacement for the geometric construction of the divisors.

## References
1. T. Katsura and S. Kondo, “A 1-dimensional family of Enriques surfaces in characteristic 2 covered by the supersingular K3 surface with Artin invariant 1,” arXiv:1411.3079v1, first posted 12 November 2014; see Sections 5--7, Lemmas 5.1, 6.2, 6.3, Proposition 6.5, and Theorem 7.4.
2. G. van der Geer, “On the geometry of a Siegel modular threefold,” *Mathematische Annalen* 260 (1982), 317--350, DOI 10.1007/BF01461467.
3. H. F. Baker, *Principles of Geometry*, vol. II, Cambridge University Press, 1922, pp. 220--221.
4. F. Cossec and I. Dolgachev, *Enriques Surfaces I*, Progress in Mathematics 76, Birkhäuser, 1989.
