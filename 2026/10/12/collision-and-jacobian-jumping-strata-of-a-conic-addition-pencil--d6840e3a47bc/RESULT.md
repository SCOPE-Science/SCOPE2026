# Collision and Jacobian-jumping strata of a conic-addition pencil

## Finding
Let \(t\in\mathbb C^\times\) and let \(\mathcal A_t\subset\mathbb P^2_\mathbb C\) be the reduced degree-seven conic-line arrangement
\[
 f_t=(x^2+y^2-z^2)(y-z)(x^2-z^2)(y^2-txz)=0.
\]
Write \(AR(f_t)_r\) for the complex vector space of homogeneous triples \((a,b,c)\), each of degree \(r\), satisfying \(a(f_t)_x+b(f_t)_y+c(f_t)_z=0\). For **every** nonzero complex \(t\), the minimal degree of a nonzero Jacobian syzygy is \(\operatorname{mdr}(f_t)=4\). The **complete** singularity and first-syzygy stratification is:

| Condition on \(t\) | Singularities | \(\tau(\mathcal A_t)\) | \(\dim AR(f_t)_4\) | \(\dim AR(f_t)_5\) |
| --- | --- | ---: | ---: | ---: |
| \(t\notin\{\pm1,\pm2i\}\) | \(13A_1+3A_3\) | 22 | 2 | 7 |
| \(t=\pm1\) | \(10A_1+3A_3+D_4\) | 23 | 2 | 8 |
| \(t=\pm2i\) | \(9A_1+5A_3\) | 24 | 3 | 9 |

There are **no other exceptional nonzero parameters**. In particular, no smooth conic in this pencil produces a free, nearly free, or plus-one generated degree-seven curve: each such property would require the two least exponents to sum to at most seven, whereas both are at least four.

## Assumptions and scope
The base curve \((x^2+y^2-z^2)(y-z)(x^2-z^2)=0\) and the particular added conic \(y^2-xz=0\) occur in Măcinic–Pokora, Example 2.9. We vary the coefficient \(t\) in the added conic while fixing the base. A nonzero parameter is required because at \(t=0\) the added quadratic is the nonreduced double line \(y^2=0\). All assertions are over the algebraically closed characteristic-zero field \(\mathbb C\); the displayed Jacobian ranks are exact algebraic ranks, not numerical samples. For \(A_1,A_3,D_4\), we use the usual analytic ADE singularity notation. The table classifies the specified embedded pencil, not every possible smooth conic that could be added to the base.

## Proof
**Geometric collisions.** Set \(z=1\). The fixed smooth conic \(Q:x^2+y^2=1\) is tangent respectively to the lines \(y=1\), \(x=1\), and \(x=-1\), giving three fixed \(A_3\) points. The three pairwise line intersections contribute three fixed \(A_1\) points. For \(t\ne0\), the varying conic \(C_t:y^2=tx\) is smooth. Each of its three line intersections contributes two distinct points, except when it contains a pre-existing line-line node. Its four intersections with \(Q\), counted with multiplicity, are determined by
\[
 x^2+tx-1=0,\qquad y^2=tx.
\]
The quadratic discriminant is \(t^2+4\). When it is nonzero, the two roots for \(x\) are distinct and each supplies two distinct values of \(y\): all four intersections are transverse. When \(t^2+4=0\), one double root for \(x\) supplies two distinct \(y\)-values, giving two simple tangencies and thus two extra \(A_3\) points. The conic \(C_t\) passes through a fixed line-line node precisely for \(t=1\) at \([1:1:1]\) or \(t=-1\) at \([-1:1:1]\). At either parameter three smooth branches have pairwise distinct tangents, so the node and the two additional line-conic nodes merge into one ordinary triple point (\(D_4\)). The point \([0:1:0]\), where the lines \(x=\pm z\) meet, never lies on \(C_t\). The intersections of \(C_t\) with the fixed conic-line tangencies never coincide, as direct substitution shows. The remaining conic-line point at infinity, \([1:0:0]\), is transverse. These observations exhaust all intersections component by component by Bézout, proving the three baskets. The Tjurina numbers follow from \(\tau(A_1)=1\), \(\tau(A_3)=3\), \(\tau(D_4)=4\).

**Jacobian ranks.** For each degree \(r\), construct the linear multiplication matrix
\[
 \Phi_r(t): S_r^{\oplus3}\longrightarrow S_{r+6},\qquad
 (a,b,c)\longmapsto a(f_t)_x+b(f_t)_y+c(f_t)_z,
\]
where \(S_r=\mathbb C[x,y,z]_r\). Thus \(AR(f_t)_r=\ker\Phi_r(t)\). Ordered monomial bases and all explicitly indexed minors are reproduced in `verify.py`. Exact Gaussian elimination over \(\mathbb Q(t)\) gives ranks \(30,43,56\) for \(r=3,4,5\), respectively. Two exact degree-three maximal minors have greatest common divisor, up to a nonzero rational factor, \(t^7\); hence \(\Phi_3\) is injective for every \(t\ne0\). Two \(43\)-minors of \(\Phi_4\) have gcd, up to units, \(t^{11}(t^2+4)\). A \(56\)-minor of \(\Phi_5\) is
\[
 35746718357756313600\,t^{15}(t-1)(t+1)(t^2+4)^2.
\]
Since specialization cannot increase matrix rank over the generic-function-field rank, these minors establish the generic rows of the rank table away from their respective exceptional sets. Exact characteristic-zero rank computations at \(t=1\) give \(\operatorname{rank}\Phi_4=43\), \(\operatorname{rank}\Phi_5=55\); at \(t=2i\), they give \(42\) and \(54\). Substitution \(x\mapsto-x\) identifies the fibers at \(t\) and \(-t\), covering the negative exceptional parameters. Consequently the kernel dimensions are \((45-43,63-56)=(2,7)\), \((2,8)\), and \((3,9)\) in the respective rows. Injectivity in degree three rules out all lower-degree syzygies by multiplying by a nonzero monomial; degree four always has a nontrivial kernel. Thus \(\operatorname{mdr}=4\) for all \(t\ne0\).

**Exclusion of free and plus-one generated cases.** A free degree-seven curve has ordered exponents \(d_1\le d_2\) satisfying \(d_1+d_2=6\); a plus-one generated one has \(d_1+d_2=7\), including the nearly-free case. In either case \(d_1=\operatorname{mdr}(f_t)=4\), hence \(d_2\ge4\) and \(d_1+d_2\ge8\), a contradiction.

## Verification
Run `python verify.py`, `python verify_special.py 4` and `python verify_special.py 5` from a directory containing both files, with SymPy 1.14 or later. The first script reconstructs all three exact polynomial matrices, checks five integer-polynomial determinant identities, their gcd degrees, their characteristic-zero generic ranks, the value at \(t=1\), and the involution \(t\leftrightarrow-t\). The latter two scripts separately verify the exceptional ranks at \(t=2i\) over \(\mathbb Q(i)\) (separate processes avoid unnecessary algebraic-field cache growth). The displayed determinants have fully specified row and column indices, allowing independent exact replay without trusting opaque logs. Local intersection calculations are given in the proof and can be checked directly by polynomial substitution, discriminant, and Bézout counting.

## Relationship to prior work
Măcinic and Pokora, *On plus-one generated conic-line arrangements with simple singularities* (arXiv:2309.15228, Example 2.9), establish that the base arrangement is free and that adding the single conic \(y^2-xz=0\) gives a four-syzygy curve. The base arrangement's freeness already appears in Dimca and Pokora, *On conic-line arrangements with nodes, tacnodes, and ordinary triple points* (arXiv:2111.12349, Example 4.14). Those results are not claimed here. The result above treats the natural full nonzero-coefficient deformation, identifies **both** geometrically different collision loci, and proves the **complete** first-two-graded-piece Jacobian-jumping stratification and uniform obstruction to plus-one generation. Literature comparisons did not locate this full parameter statement; they do not establish absolute historical novelty.

## Limitations
The statement concerns this one-dimensional family only, in characteristic zero. It determines \(\operatorname{mdr}\) and the degree-four and degree-five Jacobian syzygy spaces, not every graded Betti number or the full minimal resolution. No global classification of all conics that can be added to the fixed free arrangement is asserted. The relevant historical literature may contain an unindexed equivalent computation; the source comparison is therefore not an independent originality certification.

## References
1. A. Măcinic and P. Pokora, *On plus-one generated conic-line arrangements with simple singularities*, arXiv:2309.15228 (first posted 26 September 2023), Example 2.9, Definitions 2.1–2.3.
2. A. Dimca and P. Pokora, *On conic-line arrangements with nodes, tacnodes, and ordinary triple points*, arXiv:2111.12349 (first posted 24 November 2021), Example 4.14.
