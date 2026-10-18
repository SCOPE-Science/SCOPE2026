# The seven central-section face inventories of the regular 24-cell

## Finding

Let \(C\subset\mathbb R^4\) be the regular root-system \(24\)-cell
\[
C=\operatorname{conv}\{\epsilon_i e_i+\epsilon_j e_j:1\le i<j\le4,\ \epsilon_i,\epsilon_j\in\{-1,1\}\}.
\]
For every nonzero \(u\in\mathbb R^4\), write \(Q(u)=C\cap u^\perp\). The complete collection of possible vertex–edge–facet counts and polygonal facet inventories of these three-dimensional central sections consists of precisely the following seven rows. In the table, \(p_j\) is the number of \(j\)-gonal facets.

| Chamber stratum \((b,k)\) | \(f_0\) | \(f_1\) | \(f_2\) | \(p_3\) | \(p_4\) | \(p_5\) | \(p_6\) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| \((0,1)\) | 12 | 24 | 14 | 8 | 6 | 0 | 0 |
| \((0,2)\) | 18 | 30 | 14 | 0 | 12 | 0 | 2 |
| \((0,3)\) | 26 | 42 | 18 | 0 | 12 | 0 | 6 |
| \((1,0)\) | 14 | 24 | 12 | 0 | 12 | 0 | 0 |
| \((1,1)\) | 20 | 32 | 14 | 0 | 6 | 8 | 0 |
| \((1,2)\) | 26 | 40 | 16 | 0 | 4 | 8 | 4 |
| \((1,3)\) | 32 | 48 | 18 | 0 | 6 | 0 | 12 |

Here \((b,k)\) has an exact geometric meaning. By the signed-even-permutation symmetry of \(C\), every \(u\ne0\) can be represented with
\[
u_1\ge u_2\ge u_3\ge |u_4|.
\]
There are unique \(\lambda_i\ge0\) with
\[
u=\lambda_1(1,0,0,0)+\lambda_2(1,1,0,0)
 +\lambda_3(1,1,1,-1)+\lambda_4(1,1,1,1).
\]
Take \(b=\mathbf1_{\lambda_2>0}\) and
\(k=\mathbf1_{\lambda_1>0}+\mathbf1_{\lambda_3>0}+\mathbf1_{\lambda_4>0}\).
The possible pairs are exactly the seven displayed in the table. The diagram-triality symmetry permutes the three outer rays, so the table determines the section inventory for **every** nonzero normal. Each row occurs.

In particular, the possible numbers of section vertices are exactly
\[12,\ 14,\ 18,\ 20,\ 26,\ 32.\]
A generic central section has \(32\) vertices, \(48\) edges and \(18\) facets, consisting of six quadrilaterals and twelve hexagons. There are two distinct types with \(26\) vertices: their edge and facet counts differ.

## Assumptions and scope

The intersection is through the origin in the Euclidean \(4\)-space of the stated regular \(24\)-cell. The normal may lie on any reflection-chamber boundary; hence nongeneric and vertex-containing sections are included. Every \(Q(u)\) is a full-dimensional convex \(3\)-polytope within \(u^\perp\), since the origin is interior to \(C\). Facets mean maximal two-dimensional faces of this section and include polygons obtained by intersecting original octahedral cells with the hyperplane. The table is a classification of face inventories, not a metric congruence classification of the sections.

## Proof

**1. The chamber reduction.** The \(24\) vertices of \(C\) are the \(D_4\) roots. Reflection in any root hyperplane preserves the root system, and the standard fundamental chamber is \(u_1\ge u_2\ge u_3\ge|u_4|\). Its four extreme rays are precisely the four displayed above. Moreover,
\[
\lambda_1=u_1-u_2,\qquad
\lambda_2=u_2-u_3,\qquad
\lambda_3=(u_3-u_4)/2,\qquad
\lambda_4=(u_3+u_4)/2.
\]
For a root \(v\), each inner product with one of the four chamber rays is nonnegative, nonpositive or zero in a sign pattern compatible with the positive-root decomposition. Consequently the sign of \(u\cdot v\) depends only on which \(\lambda_i\) vanish. There are \(2^4-1=15\) nonempty support masks. The symmetry of the \(D_4\) diagram induces genuine isometries of \(C\) that permute rays numbered \(1,3,4\) while fixing ray \(2\). Thus these \(15\) masks fall into the seven specified \((b,k)\)-classes. This exhausts all real nonzero normals, not merely sampled normals.

**2. The finite face-incidence rule.** The root polytope has \(96\) edges, joining exactly those unordered pairs of distinct roots \(v,w\) with \(v\cdot w=1\). Its \(24\) octahedral facets have the vertex sets
\[
F_{i,s}=\{v:s v_i=1\},\quad 1\le i\le4,\ s\in\{-1,1\},
\]
\[
G_{\sigma}=\{v:\sigma\cdot v=2\},\quad \sigma\in\{-1,1\}^4.
\]
These are \(8+16=24\) genuine distinct supporting facets, each containing exactly six affinely independent-in-dimension-three root vertices. The standard \(24\)-cell has exactly \(24\) facets, so the list is complete.

Write \(h_v=u\cdot v\). A vertex of \(Q(u)\) arises either from an original vertex satisfying \(h_v=0\), or from an original edge \(vw\) with \(h_vh_w<0\). The latter intersection is the explicitly computable rational point
\[
p_{vw}=\frac{h_vw-h_wv}{h_v-h_w}.
\]
Distinct original edges cannot give the same new vertex outside an original vertex. This is the standard one-codimensional face-intersection rule: for a line segment edge not lying within the hyperplane, an interior intersection is an extreme point of \(C\cap u^\perp\), while any section extreme point arises in a face of the ambient polytope of dimension at most one.

Every two-dimensional facet of \(Q(u)\) is an intersection of \(u^\perp\) with an octahedral facet of \(C\). For each of the \(24\) displayed ambient facet vertex sets, collect (i) its vertices of zero height, and (ii) intersections on its constituent strictly-crossing edges. Retain the set of intersection points exactly when it has affine rank two, and identify equal point sets. This is exhaustive even when the section contains original vertices, edges or lower-dimensional faces. The size of each retained set is the polygon's vertex count.

**3. Exhaustive exact count.** Use \(u=\sum_{i\in I}w_i\) for each of the \(15\) nonempty subsets \(I\subseteq\{1,2,3,4\}\), where \(w_i\) are the rays of Step 1. All points in the incidence rule are rational. The literal finite enumeration algorithm in `checker.py` enumerates all \(24\) roots, all \(96\) edges and all \(24\) octahedral facet sets; for every support mask, it constructs every section vertex and every polygon face by exact fractions and rational row reduction. It checks all \(15\) support masks against the seven displayed inventories, checks Euler's identity and the polygon side-sum identity in every case, and repeats the computation at a second positive interior representative of each face of the chamber. No floating point or unverified geometric oracle is used.

The exact vertex subtotals, by \((b,k)\) in table order, are respectively
\[
\#\{v:h_v=0\}=(12,6,2,6,4,2,0),
\]
\[
\#\{vw\text{ edge}:h_vh_w<0\}=(0,12,24,8,16,24,32).
\]
These add to \(12,18,26,14,20,26,32\); the face construction gives the polygon inventories in the table. Its \(f_1\) values may also be recovered from \(2f_1=\sum_j j p_j\). The preceding chamber argument extends these finitely certified counts to every real normal in the corresponding support class. All seven are realized by the explicitly listed representatives, completing the proof.

## Verification

Run `python3 checker.py` using only the Python 3 standard library. Expected first line:

```text
D4_CENTRAL_SECTIONS_OK root_vertices=24 edges=96 facets=24 chamber_strata=15 orbit_types=7 sample_normals=15
```

The program computes all plane-edge intersections as exact `Fraction` objects, obtains affine ranks by exact Gaussian elimination, deduplicates coincident planar faces, verifies all seven face inventories, all fifteen chamber masks, Euler's relation and an independent family of positive normal coefficients. Finite execution certifies the finite list after the chamber reduction; the reduction is the mathematical justification that the check exhausts an infinite continuum of normal directions.

## Relationship to prior work

The \(D_4\) root realization, the full \(F_4\) symmetry and Dynkin triality are established classical facts, used here rather than claimed as new. Koca, Koca and Al-Barwani (2011) explicitly derive the outer-node permutation symmetry and discuss the regular and snub \(24\)-cells. Dechant (2013) independently develops the root-system geometry and triality. A cuboctahedral and a rhombic-dodecahedral section are already described in classical expositions of the \(24\)-cell; those individual examples are not new. The assessed result is the exhaustive seven-stratum section-inventory classification including nongeneric cuts and both distinct \(26\)-vertex cases. Primary full-text comparisons inspected do not state this exhaustive classification; an older equivalent census remains a genuine historical-priority risk.

## Limitations

The proof covers only central hyperplane sections of the regular \(D_4\) root polytope, not all affine sections, other rank-four polytopes, or volumes and metric shapes of the resulting sections. The classification describes combinatorial facet-size profiles, not all metric or incidence-isomorphism refinements. It relies on classical \(D_4\) chamber symmetry and an inspectable exact finite incidence calculation. Complete literature priority and independent validation have not been established.

## References

1. M. Koca, N. O. Koca and M. Al-Barwani, *Snub 24-Cell Derived from the Coxeter–Weyl Group W(D4)*, first arXiv submission 17 June 2011, arXiv:1106.3433v1, https://arxiv.org/abs/1106.3433; Sections 2 and 4, especially the \(D_4\) triality diagram action.
2. P.-P. Dechant, *Platonic solids generate their four-dimensional analogues*, first arXiv submission 25 July 2013, arXiv:1307.6768v1, https://arxiv.org/abs/1307.6768; Sections 2–4 on root systems, \(24\)-cell and triality.
3. *24-cell honeycomb*, publicly available geometric exposition, https://en.wikipedia.org/wiki/24-cell_honeycomb (consulted 16 October 2026); describes previously known special cuboctahedral and rhombic-dodecahedral cuts.
