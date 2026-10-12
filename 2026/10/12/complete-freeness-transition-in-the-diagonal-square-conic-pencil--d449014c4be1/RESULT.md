# Complete freeness transition in the diagonal-square conic pencil

## Finding

The published nearly-free septic of Gałecka belongs to a natural one-parameter family. For every \(t\in\mathbb C^\times\), define the reduced plane curve
\[
\mathcal A_t:\quad f_t=(x^2+y^2-tz^2)(x^2-z^2)(y^2-z^2)(x+y)=0.
\]
The conic is smooth for every permitted parameter. The complete parameter stratification is:

| Parameter | Singularities | Total Tjurina number | Minimal Jacobian syzygy degree | Status |
|---|---|---:|---:|---|
| \(t\notin\{0,1,2\}\) | \(14A_1+2D_4\) | \(22\) | \(4\) | Neither free nor nearly free |
| \(t=1\) | \(6A_1+4A_3+2D_4\) | \(26\) | \(3\) | Nearly free, exponents \((3,4)\) |
| \(t=2\) | \(2A_1+2D_4+2X_9\) | \(28\) | \(2\) | Free, exponents \((2,4)\) |

Here \(A_1\) is a node, \(A_3\) is a tacnode, \(D_4\) is an ordinary triple point, and \(X_9\) means an ordinary quadruple point (four smooth branches with pairwise distinct tangents). Consequently, within this smooth-conic pencil, the unique free fiber occurs at \(t=2\), and the unique nearly-free fiber occurs at \(t=1\).

## Assumptions and scope

The base field is \(\mathbb C\), characteristic zero. The parameter ranges over all nonzero complex numbers; \(t=0\) is excluded because the quadratic factor degenerates into a pair of lines. Each \(\mathcal A_t\) has five distinct line components and one smooth conic. Freeness refers to the graded Jacobian syzygy module of the reduced degree-seven defining polynomial, and \(\operatorname{mdr}\) is the least degree of a nonzero homogeneous triple \((a,b,c)\) satisfying \(af_x+bf_y+cf_z=0\). Singularities and the Tjurina number are taken over \(\mathbb C\).

## Proof

**(1) All singularities.** The five fixed lines are \(x-z=0\), \(x+z=0\), \(y-z=0\), \(y+z=0\), and \(x+y=0\). Without the conic, they have four ordinary nodes and two ordinary triple points. In particular, the two triple intersections are \([1:-1:1]\) and \([-1:1:1]\), while the other two finite square corners are nodes; the two remaining nodes lie at infinity. The smooth conic \(Q_t=x^2+y^2-tz^2=0\) meets each of the five lines with total multiplicity two, giving ten conic-line intersections counted with multiplicities.

On any of the four side lines, the quadratic restriction has discriminant proportional to \(t-1\). Hence exactly at \(t=1\) each side becomes tangent to the conic at a distinct nonsingular line point, giving four tacnodes. On the diagonal \(y=-x\), the restriction is \(2x^2-tz^2\) and has two simple projective roots for every \(t\ne0\). At any finite square corner, the value of \(Q_t\) is \(2-t\); thus the conic passes through all four such corners precisely when \(t=2\). It meets all lines there transversely: at the triple corner \([1:-1:1]\), the tangent directions in local affine coordinates \(u=x-z\), \(v=y+z\) are \(u\), \(v\), \(u+v\), \(u-v\), which are pairwise distinct. The other triple corner is symmetric. At the two other finite corners the conic adds a third transverse branch. For generic \(t\), the ten conic-line intersections are all distinct and transverse. Pairwise Bézout sums \(20=14+2\cdot3=6+4\cdot2+2\cdot3=2+2\cdot3+2\cdot6\) independently exhaust all possibilities in the three strata; there is no additional parameter locus.

For an ordinary multiple point with \(m\le4\) branches, \(\tau=(m-1)^2\). In particular the ordinary fourfold singularities here have \(\tau=9\): their homogeneous quartic tangent cones have four distinct lines, whose two cubic partial derivatives form a regular sequence; the Jacobian quotient has no terms in degree \(5\) or greater, so the higher-order terms are analytically removable. Nodes, tacnodes, and ordinary triple points have Tjurina numbers \(1,3,4\). Therefore the three total numbers are \(22\), \(26\), and \(28\) as stated.

**(2) Universal absence of small Jacobian syzygies away from the exceptional parameters.** For an integer \(d\ge0\), let \(M_d(t)\) be the coefficient matrix of \((a,b,c)\mapsto af_x+bf_y+cf_z\), from three copies of homogeneous forms of degree \(d\) to homogeneous forms of degree \(d+6\). Choose monomial order \(x^a y^b z^{d-a-b}\), enumerated by increasing \(a\) and then increasing \(b\); use the same convention for codomain monomials. The resulting \(M_3(t)\) has \(55\) rows and \(30\) columns. With zero-based indexing, its full-column minors on row sets

\[
R_1=[0,1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31]
\]
and
\[
R_2=[0,1,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,31,33]
\]
are respectively
\[
370091753472\,t^8(t-2)^3(t-1)^8(t+1),\qquad
740183506944\,t^7(t-2)^3(t-1)^8.
\]
Both vanish simultaneously only at \(t\in\{0,1,2\}\). Thus \(M_3(t)\) is injective for every \(t\notin\{0,1,2\}\), excluding all syzygies of degree at most three. A nonzero universal degree-four syzygy is explicitly provided and symbolically checked in `verify.py`, giving \(\operatorname{mdr}=4\) for all those parameters.

**(3) The two exceptional syzygies.** At \(t=1\), the following nonzero degree-three triple is a Jacobian syzygy:
\[
\begin{aligned}
a&=-z(3x^2-3xy+7y^2-7z^2),\\
b&=z(7x^2-3xy+3y^2-7z^2),\\
c&=(x-y)(7xy+4z^2).
\end{aligned}
\]
The degree-two matrix \(M_2(1)\), of shape \(45\times18\), has a nonzero \(18\times18\) minor with row indices \([0,1,2,3,4,5,9,10,11,12,13,14,17,18,19,20,21,25]\) and determinant \(-44957696\). Hence \(\operatorname{mdr}(f_1)=3\).

At \(t=2\), there is the nonzero degree-two syzygy
\[
(a,b,c)=(-z(x-7y),\;z(7x-y),\;7xy-z^2).
\]
The degree-one matrix \(M_1(2)\), of shape \(36\times9\), has determinant \(-2322432\) on its nine rows \([0,1,2,3,4,8,9,10,12]\) (all nine columns). Thus \(\operatorname{mdr}(f_2)=2\).

**(4) Numerical free and nearly-free criteria.** For a reduced plane curve of degree \(d=7\) and minimal syzygy degree \(r\), the equality \(\tau=(d-1)^2-r(d-r-1)\), for \(r\le(d-1)/2\), characterizes free curves. At \(t=2\), \(28=36-2\cdot4\), hence the curve is free with exponents \((2,4)\). The nearly-free criterion is \(r^2-r(d-1)+(d-1)^2=\tau+1\). At \(t=1\), \(27=26+1\), yielding exponents \((3,4)\). At all remaining permitted parameters \(r=4\) and \(\tau=22\), so neither of these numerical equalities holds. This completes the classification.

## Verification

The accompanying `verify.py` uses exact rational polynomial arithmetic with SymPy. It constructs every Jacobian coefficient matrix from the displayed defining polynomial, verifies the universal and exceptional syzygy identities, reproduces both generic full-column minor factorizations and both exceptional nonzero determinants, checks conic smoothness and parameter discriminants, and checks the combinatorial intersection and free/nearly-free numerical equalities. Run `python verify.py` with SymPy installed. The expected final output starts with `VERIFY_OK`. The determinant certificates are identities over \(\mathbb Q[t]\), not finite parameter samples.

## Relationship to prior work

Gałecka, *On the nearly freeness of conic-line arrangements with nodes, tacnodes, and ordinary triple points*, section 5.5, gives exactly the \(t=1\) arrangement, its basket \(6A_1+4A_3+2D_4\), and its near freeness. Those results are prior literature, not claimed as new here. The additional assertions are the complete complex-parameter stratification, generic syzygy rigidity, and the previously unreported free \(t=2\) fiber. Dimca's numerical criteria supply the final freeness implications. Czarnota's 2024 work on maximizing septics treats different conic-line examples and prescribed ADE singularities; its displayed examples do not give this pencil classification. 

## Limitations

This result concerns exactly the displayed pencil, not all degree-seven one-conic/five-line arrangements. The point \(t=0\) is deliberately excluded because the conic splits. No assertion of geometric or arithmetic uniqueness outside the pencil is made. Searches of published records and the inspected primary sources did not establish an equivalence to a previously stated pencil theorem; unindexed computations or historical overlap remain possible.

## References

1. A. Gałecka, *On the nearly freeness of conic-line arrangements with nodes, tacnodes, and ordinary triple points*, 2022, arXiv:2204.13969v1 (first public 2022-04-29); Boletín de la Sociedad Matemática Mexicana 28 (2022), article 67, DOI:10.1007/s40590-022-00461-4, especially section 5.5. Open-access full text: https://link.springer.com/article/10.1007/s40590-022-00461-4.
2. A. Dimca, *Freeness versus maximal global Tjurina number for plane curves*, arXiv:1508.04954; Mathematical Proceedings of the Cambridge Philosophical Society 163 (2017), DOI:10.1017/S0305004116000803.
3. I. Czarnota, *On maximizing curves of degree 7*, Annali dell'Università di Ferrara 70 (2024), 1479–1489, DOI:10.1007/s11565-024-00523-7, particularly section 4. Open-access full text: https://link.springer.com/article/10.1007/s11565-024-00523-7.
