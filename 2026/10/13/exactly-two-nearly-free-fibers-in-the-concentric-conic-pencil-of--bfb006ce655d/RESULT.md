# Exactly two nearly-free fibers in the concentric-conic pencil of a square

## Finding
Let \(\mathcal A_t\subset\mathbb P^2_{\mathbb C}\) be the reduced degree-six plane curve
\[
 f_t=(x^2+y^2-tz^2)(y-x+4z)(y+x-4z)(y-x-4z)(y+x+4z)=0,
 \qquad t\in\mathbb C^\times.
\]
Its singularities and minimal Jacobian-relation degree \(r_t=\operatorname{mdr}(f_t)\) are completely determined:

| Parameter | Singularities | Total Tjurina number | \(r_t\) | Freeness |
|---|---|---:|---:|---|
| \(t\notin\{0,8,16\}\) | \(14A_1\) | \(14\) | \(4\) | Neither free nor nearly free |
| \(t=8\) | \(6A_1+4A_3\) | \(18\) | \(3\) | Nearly free, exponents \((3,3)\) |
| \(t=16\) | \(2A_1+4D_4\) | \(18\) | \(2\) | Nearly free, exponents \((2,4)\) |

In particular, **the complete nearly-free parameter locus within the smooth-conic pencil is precisely \(\{8,16\}\)**. It has two distinct geometric mechanisms: tangency to all four sides at the inscribed conic, and passage through all four finite line intersections at the circumscribed conic. No member with \(t\ne0\) is free. The \(t=16\) example and its near freeness were already given by Gałecka; the assertion is the exhaustive parameter classification, including the \(t=8\) fiber and the complement.

## Assumptions and scope
The base field is \(\mathbb C\) of characteristic zero, and \(t\) ranges over **all** nonzero complex numbers. The central conic \(x^2+y^2-tz^2=0\) is then smooth. The four displayed lines are distinct and fixed. Singularity types \(A_1,A_3,D_4\) mean, respectively, ordinary node, ordinary tacnode and ordinary three-branch transverse point. The minimal Jacobian relation degree is the least integer \(d\ge0\) for which there is a nonzero triple of homogeneous degree-\(d\) forms \((a,b,c)\) with \(a(f_t)_x+b(f_t)_y+c(f_t)_z=0\). The claim concerns this pencil, not all conic-line arrangements with the same component counts.

## Proof
**Singularities.** The four lines are the sides of the affine square with vertices \((4,0),(0,4),(-4,0),(0,-4)\). They meet at exactly six distinct projective points: these four finite vertices and the two distinct points at infinity \([1:1:0]\) and \([1:-1:0]\). Restricting the conic to any one line and taking its discriminant gives exactly \(8(t-8)\); its leading quadratic coefficient is \(2\), so it has two distinct transverse intersections unless \(t=8\), when the intersection is a tangency of order exactly two. The conic contains a finite vertex if and only if \(t=16\), and never contains either of the two points at infinity (where its value is \(2\) in the indicated normalizations). Thus no other collision parameters exist.

When \(t\notin\{0,8,16\}\), the six line-line nodes and eight transverse line-conic intersections are distinct, giving \(14A_1\). At \(t=8\), the four line-conic tangencies lie in the interiors of the four sides, away from the six line intersections; their reduced local germs are of type \(A_3\), giving \(6A_1+4A_3\). At \(t=16\), each of the four finite vertices acquires a smooth conic branch with a tangent distinct from the two line tangents, forming an ordinary \(D_4\) triple point, with the two points at infinity remaining nodes. Every pairwise intersection has been accounted for, and Bézout's theorem excludes further singularities. Since these are quasihomogeneous simple singularities, their local Tjurina numbers are respectively \(1,3,4\). Summing gives \(14,18,18\).

**All parameter-dependent Jacobian relations.** Write \(U=x^2+y^2\) and
\[
 f_t=(U-tz^2)\bigl((U-16z^2)^2-4x^2y^2\bigr).
\]
For \(d=1,2,3,4\), consider the matrix of the linear map
\[
 \Phi_d:\;\mathbb C[t][x,y,z]_d^3\longrightarrow
 \mathbb C[t][x,y,z]_{d+5},\quad
 (a,b,c)\longmapsto a(f_t)_x+b(f_t)_y+c(f_t)_z.
\]
Partition source columns and target rows according to exponent parity in \((x,y,z)\), noting that each derivative reverses the parity of precisely its corresponding variable. This reduces the matrices to four independent blocks in every displayed degree. Their exact Smith normal forms over the principal ideal domain \(\mathbb Q[t]\), with unit diagonal factors suppressed and all remaining factors made monic, have the following nonunit invariant factors:

| Degree | Parity block and nonunit Smith factors |
|---|---|
| \(1\) | None in any block; full column rank \(9\) |
| \(2\) | \(001:\ t-16\); all other diagonal factors units |
| \(3\) | \(000:\ t-16\); \(011:\ (t-8)(t-16)\); \(101:\ (t-8)(t-16)\); \(110:\ t-8\) |
| \(4\) | \(001:\ t-16,\ t(t-8)(t-16)\); \(010:\ (t-8)(t-16)\); \(100:\ (t-8)(t-16)\); \(111:\ t-8\). Each degree-four block also has exactly one zero diagonal invariant. |

Over \(\mathbb Q[t]\), all row and column operations for a Smith normal form are unimodular, so remain invertible upon specializing \(t\) to any complex value. Therefore these are **uniform rank certificates for every complex parameter**, not evidence from a finite sample. In degree \(4\), the source dimension is \(45\) and the generic rank is \(41\); at each of \(t=8,16\) the rank is \(37\). In degree \(3\), the source dimension is \(30\), with rank \(30\) away from \(8,16\) and rank \(27\) at those points. Degree \(2\) is injective except at \(16\), where it has one-dimensional kernel; degree \(1\) is always injective. Degree-zero relations would generate degree-one relations by multiplication, so none exist. Consequently \(\operatorname{mdr}(f_t)\) is exactly \(4,3,2\) in the three cases in the table.

For direct checks, an explicit degree-three relation at \(t=8\) is
\[
 \bigl(-y(x^2+3y^2-48z^2),\;-x(3x^2+y^2-48z^2),\;8xyz\bigr),
\]
and an explicit degree-two relation at \(t=16\) is
\[
 \bigl(16xz,\;-16yz,\;x^2-y^2\bigr).
\]
Both yield zero when contracted with the corresponding Jacobian gradient.

**Near freeness and freeness.** The established numerical characterization for these reduced degree-six curves is
\[
 r_t^2-5r_t+25=\tau(\mathcal A_t)+1.
\]
For \(t=8\) and \(t=16\), both sides are \(19\); their nearly-free exponents, summing to six and with first exponent \(r_t\), are \((3,3)\) and \((2,4)\). For all other smooth parameters the left side is \(21\) and the right side is \(15\), so the curves are not nearly free. They are not free either: a free degree-six curve of minimal relation degree \(r\) must have \(r\le2\), excluding \(t\ne16\); at \(16\), the free degree-six Tjurina value for exponents \((2,3)\) would be \(19\), but the actual value is \(18\).

## Verification
The standalone program `verify.py` reproduces all Smith blocks from the exact coefficient matrices and verifies every stated nonunit invariant factor over \(\mathbb Q[t]\), both explicit syzygies, the four line-restriction discriminants, and the four finite-vertex equations. Run `python verify.py` with Python 3 and SymPy 1.14; it prints `VERIFY_OK` only if all exact assertions pass. The Smith calculations apply to the complete complex parameter line; no numerical samples or truncated enumeration are used for rank claims.

## Relationship to prior work
Gałecka, *On the nearly freeness of conic-line arrangements with nodes, tacnodes, and ordinary triple points* (arXiv:2204.13969, first public 29 April 2022; journal DOI 10.1007/s40590-022-00461-4), §5.4, supplies precisely the \(t=16\) member, its two nodes, four ordinary triple points, and its near freeness; her Theorem 3.2 supplies the numerical near-free criterion. These facts are **prior results**, not claimed as new. Dimca–Pokora give general background on freeness of conic-line arrangements with nodes, tacnodes and ordinary triple points. The contribution here is the exhaustive smooth-conic pencil, its second, geometrically different near-free point \(t=8\), the exact Jacobian-rank specialization, and the absence of other near-free members.

## Limitations
The parameter \(t=0\), where the quadratic factor becomes a pair of lines over \(\mathbb C\), is excluded. The result is not a classification of every conic tangent to an arbitrary quadrilateral, all near-free degree-six conic-line arrangements, or full moduli of square-equivalent configurations. Search-based originality comparisons may miss unindexed computations, especially thesis material or implicit previous descriptions; no independence or exhaustive historical priority is asserted.

## References
1. A. Gałecka, *On the nearly freeness of conic-line arrangements with nodes, tacnodes, and ordinary triple points*, arXiv:2204.13969 (submitted 2022-04-29), DOI: 10.1007/s40590-022-00461-4, especially §§2–3 and 5.4.
2. A. Dimca and P. Pokora, *On conic-line arrangements with nodes, tacnodes, and ordinary triple points*, DOI: 10.1007/s10801-022-01116-3.
