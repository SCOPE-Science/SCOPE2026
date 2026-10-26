# A sharp smooth filling-degree threshold on the elliptic quadric over \(\mathbf F_2\)

## Finding
Let \(Q\subset\mathbf P^3_{\mathbf F_2}\) be any smooth nonsplit (elliptic) quadric. Among smooth geometrically integral curves \(C\subset Q\) containing all \(5\) rational points of \(Q\), the least projective degree is exactly \(6\). In particular, degree \(4\) is impossible despite being the first degree above the conic sections. An explicit degree-six example is \(Q\cap V(G)\), where
\[
Q=w^2+wx+x^2+yz,\qquad
G=w^3+w^2z+wx^2+wxy+wyz+wz^2+x^3+x^2y+xy^2+xyz.
\]

## Assumptions and scope
All varieties and degrees are over \(\mathbf F_2\). The quadric is geometrically smooth with nonsplit rulings, hence its projective rational-point set has cardinality \(5\). The minimum is among **geometrically integral smooth** curves embedded in the quadric; we do not classify or optimize singular irreducible curves. Projective degree is degree with respect to \(\mathcal O_{\mathbf P^3}(1)\). We use smoothness over an algebraic closure rather than merely nonsingularity at rational points.

## Proof
**(1) Divisor degrees.** Over \(\mathbf F_4\), the quadric becomes \(\mathbf P^1\times\mathbf P^1\). Frobenius exchanges its two ruling classes. A divisor defined over \(\mathbf F_2\) consequently has geometric bidegree \((d,d)\) and projective degree \(2d\). The geometric genus of a smooth divisor of type \((d,d)\) is \((d-1)^2\). A degree-two curve has bidegree \((1,1)\) and is a conic; it cannot contain five distinct rational points because a smooth conic over \(\mathbf F_2\) has exactly three rational points.

**(2) Degree-four obstruction.** Suppose a smooth degree-four curve \(E\subset Q\) contains all five rational points of \(Q\). Then \(E\) has bidegree \((2,2)\) over \(\mathbf F_4\) and genus one. Write \(N_1=\#E(\mathbf F_2)=5\). The Frobenius trace is \(t=2+1-N_1=-2\), so
\[
\#E(\mathbf F_4)=2^2+1-(t^2-2\cdot2)=5.
\]
Because \(E(\mathbf F_2)\) is nonempty, the degree-two Picard torsor \(\operatorname{Pic}^2(E)\) has exactly \(\#E(\mathbf F_{2^r})\) points over each finite extension, and therefore its \(\mathbf F_4\)-points are all already \(\mathbf F_2\)-rational. The two rulings on \(Q_{\mathbf F_4}\) restrict to degree-two line bundles \(L_1,L_2\) on \(E_{\mathbf F_4}\), which Frobenius exchanges. Both are therefore rational and fixed individually, whence \(L_1\cong L_2\). But the two degree-two linear series of the two projections \(E_{\mathbf F_4}\to\mathbf P^1\) cannot coincide. On a genus-one curve a degree-two bundle has two sections, so if the series coincided the two maps would differ by a projectivity; the image of \(E\) in \(\mathbf P^1\times\mathbf P^1\) would then lie on the graph of a projectivity, a \((1,1)\)-curve, contradicting its \((2,2)\) divisor class and geometric integrality. Thus a smooth degree-four filling curve is impossible.

**(3) Sharp degree-six construction.** Consider the displayed polynomials \(Q\) and \(G\). The quadratic form \(w^2+wx+x^2\) is anisotropic over \(\mathbf F_2\), so \(Q=w^2+wx+x^2+yz\) is a nonsplit smooth quadric. Direct evaluation gives its five rational points:
\[
[0:0:0:1],\ [0:0:1:0],\ [0:1:1:1],\ [1:0:1:1],\ [1:1:1:1].
\]
Each satisfies \(G=0\). The exact four-chart Jacobian-minor certificates described next show \(Q\cap V(G)\) is geometrically smooth. Over the algebraic closure its divisor class is \((3,3)\), so its ample divisor class is connected; a smooth connected curve is geometrically integral. Thus it is a smooth degree-six genus-four filling curve. Combining (1)–(3) gives the minimum degree \(6\).

## Verification
Run \(`python verify.py`\) with SymPy. It reproduces all five rational points, checks that each vanishes on \(G\), forms all \(2\times2\) minors of the Jacobian of \(Q,G\), and computes a Gröbner basis in each of the four affine charts \(w=1,x=1,y=1,z=1\). Over \(\mathbf F_2\) every chart ideal has reduced Gröbner basis \([1]\), proving that the projective intersection has no geometric singular point. The corresponding program output is embedded. The nonexistence proof is conceptual and does not depend on an incomplete enumeration.

## Relationship to prior work
Homma and Kim (first circulated in 2022) prove the minimum filling bidegrees for a split quadric and explicitly single out filling curves on the **elliptic** quadric as a separate problem at the end of their article. Their split-quadric construction does not imply the nonsplit-quadric degree-six threshold. The later treatment of smooth space filling curves on products of projective lines continues to concern the split case. The new contribution is the degree-four genus-one obstruction plus a smooth degree-six witness in the nonsplit smallest-field case, not the general existence of filling curves.

## Limitations
This determines the **smooth** threshold for the nonsplit quadric only over \(\mathbf F_2\). It does not determine the least degree of possibly singular irreducible filling curves, classify all smooth sextics, or address other field sizes. Publication priority can be affected by unindexed projective-geometry catalogues; no independent review is claimed.

## References
1. Masaaki Homma and Seon Jeong Kim, *Filling curves for \(\mathbf P^1\times\mathbf P^1\)*, arXiv:2203.11595 (2022), particularly Section 5 (elliptic-quadric problem).
2. Menhaz Ahammed, Matthew Campbell and Han-Bom Moon, *Minimal algebraic space filling curves on the product of projective lines*, arXiv:2512.02796 (2025), Section 2.3 (split-quadric comparison).
