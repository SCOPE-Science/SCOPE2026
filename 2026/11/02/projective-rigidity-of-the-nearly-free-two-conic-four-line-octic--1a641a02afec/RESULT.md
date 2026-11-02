# Projective rigidity of the nearly free two-conic, four-line octic

## Finding
Let \(\mathcal A\subset\mathbb P^2_{\mathbb C}\) be a reduced arrangement of exactly two distinct smooth conics and four distinct lines, whose only singularities are ordinary nodes \(A_1\), ordinary tacnodes \(A_3\), and ordinary transverse triple points \(D_4\). If \(\mathcal A\) is nearly free, then its singularity counts, respectively, are
\[
(n_2,t,n_3)=(2,6,4),
\]
and it is projectively equivalent, with unlabeled components, to the arrangement defined by
\[
\begin{aligned}
F={}&XZ(X-2Y+Z)(4X-4Y+Z)\\
&\quad\cdot(XZ-Y^2)(4X^2-8XY+8XZ-4YZ+Z^2)=0.
\end{aligned}
\]
Conversely, this displayed octic has precisely these singularities and is nearly free, with minimal Jacobian-syzygy degree \(4\) and exponents \((4,4)\). Consequently **exactly one projective equivalence class** occurs for this component type.

## Assumptions and scope
All varieties and projective equivalences are over \(\mathbb C\); projective equivalence means an element of \(\operatorname{PGL}_3(\mathbb C)\) carrying the unlabeled arrangement onto another. No claim is made about other degree-eight component decompositions, other singularity types, or arrangement classes over nonclosed ground fields. A tacnode is the contact of exactly two smooth local branches with local intersection multiplicity two. All ordinary triple points have three pairwise transverse branches.

Write \(C_1,C_2\) for the conics and \(L_1,\ldots,L_4\) for the lines. Every singular point belongs to two or three distinct components. Set \(\operatorname{mdr}(F)\) equal to the least degree of a nonzero homogeneous triple \((A,B,C)\) satisfying \(AF_X+BF_Y+CF_Z=0\).

## Proof
**1. Necessary numerical data.** In degree \(m=8\), the published bound \(\operatorname{mdr}(F)\ge 2m/3-2\) and the exponents of a nearly free octic force \(\operatorname{mdr}(F)=4\). The nearly free Tjurina equality is therefore \(\tau=4^2-4(8-1)+(8-1)^2-1=36\). Bézout and the Tjurina contributions give
\[
n_2+2t+3n_3=26,\qquad n_2+3t+4n_3=36.
\]
Hence \(t+n_3=10\) and \(n_2+n_3=6\). Gałecka's published inequality \(8k+n_2+3n_3/4\ge d+5t/2\) with \((k,d)=(2,4)\) gives \(9n_3\ge28\). Thus \(4\le n_3\le6\).

**2. Classify the component incidences.** Let \(x\), \(y\), \(z\) count ordinary triple points involving, respectively, both conics and one line; one conic and two lines; and three lines. Then \(n_3=x+y+z\) and \(z\le1\), because four distinct lines cannot support two distinct ordinary three-line intersections. Let \(u\in\{0,1,2\}\) be the number of conic-conic tacnodes, so there are \(t-u\) conic-line tacnodes. From the sixteen conic-line pairwise intersection units,
\[
2(t-u)+2x+2y\le16,
\]
whence \(u+z\ge2\). From the four conic-conic intersection units, \(x+2u\le4\). Further, the line-line nodes number \(6-y-3z\), at most \(n_2=6-n_3\).

If \(z=0\), then \(u=2\), and the line-line node inequality gives \(y\ge n_3\), so \(x=0\) and \(y=n_3\). Both the conic-conic node count and the conic-line node count vanish. Hence every conic-line pair is either tangent or meets at exactly two transverse ordinary triple points. When two conics have two tacnodes, no arrangement line can be tangent to both: their common tangent lines pass through the conic-conic tacnodes, where a third branch is forbidden (Dimca--Pokora, Lemma 5.1). A single line cannot be secant to both conics in two triple points each, since it has only three intersections with the remaining lines. Consequently at each of the four lines one conic is tangent and the other passes through two line-line intersections. The graph of line-line intersections lying on a conic has degree two at each of four vertices, hence is the unique four-cycle. Its edge coloring is constant around the cycle, since at each vertex both triple points are on the same conic. Therefore \(y=n_3=4\), one conic is tangent to all four lines, and the other passes through precisely the four cycle vertices.

If \(z=1\), three lines are concurrent and every \(QLL\) triple uses the fourth line. If \(u=2\), then \(x=0\), so \(4\le n_3=y+1\le4\). All three intersection points of the fourth line with the concurrent lines are \(QLL\) triples. The fourth line is secant to both conics (three points distributed among two conics), so it cannot be tangent to either; the remaining three lines contribute at most three conic-line tacnodes by the common-tangent obstruction. This contradicts \(t-u=4\). If \(u=1\), the conic-line node count is exactly \(2(u+z-2)=0\). Each conic-line pair then contains either one tacnode or two ordinary transverse triple intersections. For any one of the three concurrent lines, the total number of transverse conic-line incidences is even; \(C_1C_2L\) triples contribute two each, while its only possible \(QLL\) triple contributes one. Hence no such \(QLL\) triple occurs. It follows that \(y=0\) and \(n_3=x+1\le3\), a contradiction. These exhaust the cases because \(u+z\ge2\).

**3. Projective uniqueness.** Name the conic tangent to all four lines \(Q\), and the other \(R\). A smooth conic and three marked distinct tangent lines may be sent projectively to \(Q:XZ-Y^2=0\) and tangent parameters \(\infty,0,1\). Write the fourth parameter \(r\notin\{0,1\}\). The four lines have equations
\[
Z=0,\quad X=0,\quad X-2Y+Z=0,\quad X-2rY+r^2Z=0.
\]
The four \(R\)-triple vertices are the complete intersection of the unions of the first and fourth lines and the second and third lines. Thus \(R\) lies in the pencil
\[
\lambda Z(X-2rY+r^2Z)+\mu X(X-2Y+Z)=0,
\]
with \(\lambda\mu\ne0\), since \(R\) is smooth. On \(Q\), parametrized by \([X:Y:Z]=[T^2:TU:U^2]\), the intersection divisor is cut out by
\[
\lambda U^2(T-rU)^2+\mu T^2(T-U)^2.
\]
Its two quadratic factors \(T(T-U)\pm\eta U(T-rU)\), where \(\eta^2=-\lambda/\mu\), are coprime. The two conic-conic tacnodes require the whole quartic to be the square of a separable quadratic. Thus each quadratic factor must have a repeated root. Their discriminants are \(1+\eta^2\pm\eta(4r-2)\). Both vanish precisely when \(r=1/2\) and \(\eta^2=-1\), i.e. \(\lambda=\mu\). This fixes the projective class, yielding the displayed equation after clearing denominators.

**4. Existence and near freeness.** Put \(Q=XZ-Y^2\) and \(R=4X^2-8XY+8XZ-4YZ+Z^2\). The Hessian determinant of \(R\) is \(256\), so it is smooth. The four displayed lines are tangent to \(Q\) at parameters \(\infty,0,1,1/2\). The identity \(R=4X(X-2Y+Z)+Z(4X-4Y+Z)\) shows that \(R\) passes through the four transverse line-line vertices of the cycle, and its intersection with each line is exactly the two corresponding vertices. On \(Q\) we have the factorization
\[
R(T^2,TU,U^2)=(2T^2-2TU+U^2)^2.
\]
The quadratic has distinct roots \((1\pm i)/2\), different from all four tangent parameters. Thus the two conics meet at exactly two ordinary tacnodes, disjoint from the line intersections. The two remaining line-line points are nodes; no other singularities occur. Hence \((n_2,t,n_3)=(2,6,4)\) and \(\tau=2+3\cdot6+4\cdot4=36\).

The accompanying exact symbolic program provides a degree-four Jacobian relation, verifies it as a polynomial identity over \(\mathbb Q\), and proves that the degree-three syzygy map has trivial kernel; lower-degree syzygies would multiply to degree three. Hence \(\operatorname{mdr}(F)=4\). The published numerical criterion for nearly freeness now applies because \(4^2-4\cdot7+7^2=37=\tau+1\). This proves existence and completes the classification.

## Verification
Run `python verify_symbolic.py` and `python verify_incidence.py` with SymPy available. The symbolic program verifies smoothness, the restricted conic intersection square, the defining polynomial identity for all cycle vertices, an explicit degree-four Jacobian syzygy, and injectivity of the cubic syzygy map using exact rational arithmetic. The second program exhausts finite abstract incidence distributions and confirms that only six labeled four-cycle assignments survive, representing the one unlabeled type. The geometric argument, not enumeration, proves uniqueness over all complex parameters.

## Relationship to prior work
Gałecka (arXiv:2204.13969, first public April 29, 2022) proves the numerical constraints, constructs nearly free examples through degree seven, and leaves degree eight open. Dimca--Pokora (arXiv:2111.12349) prove the common-tangent lemma and classify *free*, not nearly free, arrangements. Măcinic--Pokora (arXiv:2309.15228, Section 3) study defect-two plus-one-generated arrangements, distinct from nearly free defect one; their degree-eight displayed example consists of one conic and six lines. A separately recorded degree-eight nearly free example with singularity basket \((3,3,6)\) also has one conic and six lines. None of those results supplies a two-conic/four-line classification or the harmonic pencil argument. Search and literature comparison do not prove absolute priority; unindexed equivalent work remains a risk.

## Limitations
This is a self-reviewed mathematical result, not an independent audit or external certification. The classification assumes the three specified local singularity types and complex ground field. The parity and four-cycle incidence argument does not apply to arrangements allowing quadruple points, conic singularities, or higher contacts. A computational check alone is not a proof of geometric uniqueness. Possible unindexed prior equivalent geometric normal forms or near-freeness calculations have not been ruled out.

## References
- A. Gałecka, *On the nearly freeness of conic-line arrangements with nodes, tacnodes, and ordinary triple points*, arXiv:2204.13969 (first posted 2022-04-29), DOI:10.1007/s40590-022-00461-4, esp. Theorem 3.2 and Propositions 4.1 and 4.4.
- A. Dimca and P. Pokora, *On conic-line arrangements with nodes, tacnodes, and ordinary triple points*, arXiv:2111.12349 (2021-11-24), DOI:10.1007/s10801-022-01116-3, esp. Lemma 5.1.
- A. Măcinic and P. Pokora, *On plus-one generated conic-line arrangements with simple singularities*, arXiv:2309.15228 (2023-09-26), DOI:10.4171/RLM/1044, esp. Section 3.
