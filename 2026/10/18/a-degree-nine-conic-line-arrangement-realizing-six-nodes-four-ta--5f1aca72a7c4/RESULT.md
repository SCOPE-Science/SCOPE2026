# A degree-nine conic–line arrangement realizing six nodes, four tacnodes, and seven triple points

## Finding
Over \(\mathbb C\), the reduced degree-nine plane curve
\[
F= (XZ-Y^2)Y(X-Y)(Z-Y)\left((X^2+6XZ+Z^2-4Y^2)^2-16Y^2(X-Z)^2\right)=0
\]
is the union of a smooth conic and seven distinct lines. Its complete singularity basket consists of six nodes \(A_1\), four tacnodes \(A_3\), and seven ordinary triple points \(D_4\), and no others. Thus its weak combinatorics is \((k,d;n_2,t_2,n_3)=(1,7;6,4,7)\), its total Tjurina number is \(\tau=46\), and the least degree of a nonzero Jacobian syzygy is \(\operatorname{mdr}(F)=5\). It attains the du Plessis–Wall upper bound for a reduced degree-nine plane curve with \(\operatorname{mdr}=5\).

## Assumptions and scope
All geometric assertions are over the algebraically closed field \(\mathbb C\). Coordinates are homogeneous on \(\mathbb P^2\). A node means two smooth branches meeting transversely, a tacnode means two smooth branches with intersection multiplicity two, and an ordinary triple point means three smooth branches with three distinct tangent directions. The invariant \(\operatorname{mdr}(F)\) is the least nonnegative integer \(r\) for which there is a nonzero homogeneous triple \((a,b,c)\) of degree \(r\) satisfying \(aF_X+bF_Y+cF_Z=0\).

## Proof
Set \(Q=XZ-Y^2\). The three lines \(Y=0\), \(X-Y=0\), and \(Z-Y=0\) form a triangle with vertices \([1:0:0]\), \([0:0:1]\), and \([1:1:1]\), all lying on \(Q\). Each vertex is a transverse meeting of its two lines and \(Q\). In particular these are three ordinary triple points.

Let \(T=\{-1+\sqrt2,-1-\sqrt2,1+\sqrt2,1-\sqrt2\}\). The additional four lines are
\[L_t:t^2X-2tY+Z=0\qquad(t\in T).\]
They are tangent to \(Q\) at \(P_t=[1:t:t^2]\). Since the four \(t\) values are distinct and none equals \(0\) or \(1\), the contact points are pairwise distinct and separate from the triangle vertices. Their product is precisely the quartic factor displayed in \(F\):
\[\prod_{t\in T}(t^2X-2tY+Z)=(X^2+6XZ+Z^2-4Y^2)^2-16Y^2(X-Z)^2.\]
All four conic contacts are ordinary tacnodes, and exact substitution excludes an additional line through each contact.

The seven-line subarrangement has exactly four points of multiplicity three, with line triples \(\{Y,L_{-1+\sqrt2},L_{1-\sqrt2}\}\), \(\{Y,L_{-1-\sqrt2},L_{1+\sqrt2}\}\), \(\{X-Y,L_{1+\sqrt2},L_{1-\sqrt2}\}\), and \(\{Z-Y,L_{-1+\sqrt2},L_{-1-\sqrt2}\}\). All four lie off \(Q\). There are exactly nine remaining line–line double points; three are the triangle vertices on \(Q\), and six are off \(Q\). This list exhausts all \(21\) unordered line pairs because \(4\binom32+9=21\). Moreover, the three secant lines contribute six transverse conic–line intersections at the triangle vertices (counted with multiplicity), and the four tangent lines contribute eight; hence \(6+8=14=2\cdot7\), exhausting all conic–line intersections by Bézout. Consequently the complete singularity counts are \((6,4,7)\). Since the local Tjurina numbers of \(A_1,A_3,D_4\) are \(1,3,4\), respectively, \(\tau=6+4\cdot3+7\cdot4=46\).

For the syzygy assertion, form the coefficient matrix of the map \((a,b,c)\mapsto aF_X+bF_Y+cF_Z\) in homogeneous degree \(4\), with columns ordered by the three derivative blocks and within each block monomials \(X^iY^jZ^{4-i-j}\) in increasing \(i\), then \(j\). Order target monomials \(X^iY^jZ^{12-i-j}\) analogously. The resulting integer matrix is \(91\times45\). Its square submatrix with zero-based row indices
\[
(2,3,4,5,6,15,16,17,18,27,28,29,38,39,48,7,8,19,20,21,22,23,24,25,30,31,32,40,41,49,26,33,34,35,36,37,12,9,10,42,43,44,45,46,50)
\]
has determinant congruent to \(89\pmod {101}\). Thus the degree-four map is injective over \(\mathbb Q\), and there can be no nonzero syzygy of degree at most four. The degree-five matrix, of size \(105\times63\), has a nonzero rational kernel of dimension four; the accompanying exact rational-arithmetic script explicitly constructs one nonzero triple and verifies \(aF_X+bF_Y+cF_Z=0\) as an identity. Therefore \(\operatorname{mdr}(F)=5\).

For \(d=9,r=5\), the du Plessis–Wall upper bound is \((d-1)^2-r(d-r-1)-\binom{2r-d+2}{2}=64-15-3=46\), attained here.

## Verification
The accompanying `verify.py` uses exact SymPy arithmetic in \(\mathbb Q(\sqrt2)\), \(\mathbb Q\), and \(\mathbf F_{101}\). It enumerates all line pairs, groups projectively identical intersections, checks the conic incidence and tangency conditions and the polynomial factorization, computes the modular \(45\times45\) determinant, obtains rational degree-five syzygies, and verifies the syzygy identity exactly. Execute `python verify.py` with Python 3 and SymPy installed. No floating-point geometry or finite-search inference over \(\mathbb C\) is used.

## Relationship to prior work
Măcinic and Pokora list the numerical configuration \((1,7;6,4,7)\) among complex conic–line realizability cases not settled by their degree-nine analysis; their Corollary 3.9 excludes the distinct configuration \((1,7;7,5,6)\). The present statement supplies a coordinate realization of the former numerical type, **not** an example of a plus-one generated curve: its minimum Jacobian syzygy degree is five, so no plus-one generation with defect two is claimed. Earlier work of Dimca and Pokora treats freeness and classification under additional assumptions, rather than providing the equation and incidence count above. Later examples with ordinary quadruple points concern different singularity baskets.

## Limitations
This is one explicit complex realization and one exact syzygy computation, not a classification of all realizations or their moduli, and not a demonstration of plus-one generation. The rational polynomial has four tangent-line components defined over \(\mathbb Q(\sqrt2)\), although its total equation is rational. The novelty comparison is necessarily subject to imperfect indexing of prior explicit constructions. The modular determinant is a characteristic-zero lower-bound certificate, not a claim about every positive characteristic.

## References
1. A. Măcinic and P. Pokora, *On plus-one generated conic-line arrangements with simple singularities*, arXiv:2309.15228, first posted 26 September 2023; especially the concluding degree-nine discussion and Corollary 3.9. https://arxiv.org/abs/2309.15228 .
2. A. Dimca and P. Pokora, *On conic-line arrangements with nodes, tacnodes, and ordinary triple points*, Journal of Algebraic Combinatorics 56 (2022), 403–424, DOI 10.1007/s10801-022-01116-3.
3. A. du Plessis and C. T. C. Wall, *Application of the theory of the discriminant to highly singular plane curves*, Math. Proc. Cambridge Philos. Soc. 126 (1999), 259–266, for the Tjurina bound; see also standard modern formulations for \(r\ge d/2\).
