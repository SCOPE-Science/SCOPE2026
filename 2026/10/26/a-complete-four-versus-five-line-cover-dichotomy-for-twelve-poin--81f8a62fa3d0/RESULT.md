# A complete four-versus-five line-cover dichotomy for twelve-point plane cubics
## Finding
Let \(C\subset\mathbb P^2_{\mathbb F_q}\) be a smooth plane cubic, and assume \(\#C(\mathbb F_q)=12\). Define \(\tau(C)\) as the minimum number of \(\mathbb F_q\)-lines whose union contains every rational point of \(C\). Then
\[
\tau(C)=\begin{cases}4,&\operatorname{Pic}^0(C)(\mathbb F_q)\cong C_2\times C_6\text{ and }C\text{ has an }\mathbb F_q\text{-rational flex},\\5,&\text{otherwise}.\end{cases}
\]
This statement includes plane cubics without rational flexes and is uniform across finite-field characteristics. The two Weierstrass cubics \(y^2=x^3+1\) and \(y^2=x^3+2x\) over \(\mathbb F_{11}\) both have \(12\) points but have respective cover numbers \(5\) and \(4\).

## Assumptions and scope
The curve is smooth, projective, and geometrically integral of degree three over a finite field. A covering line is defined over that field. A rational flex means a rational point whose tangent line intersects the cubic with multiplicity three at that point. Distinct rational points are counted once, regardless of tangent multiplicity. No characteristic restriction is imposed. The condition \(\#C(\mathbb F_q)=12\) guarantees a rational point and hence an identification of \(C\) with a genus-one group after choosing an origin.

## Proof
**Collinearity parameter.** Fix any \(O\in C(\mathbb F_q)\) and write \(G=C(\mathbb F_q)\) with origin \(O\). Let \(H\) denote the hyperplane divisor of the plane embedding and let \(T\in G\) correspond, under \(G\cong\operatorname{Pic}^0(C)(\mathbb F_q)\), to \([H-3O]\). For rational points \(P,Q,R\), counted with intersection multiplicity, a rational line cuts the divisor \(P+Q+R\) if and only if \(P+Q+R=T\) in \(G\). For distinct points this follows from the complete linear system of the degree-three line bundle \(\mathcal O_C(1)\); when two points agree, the relevant line is tangent at the repeated point. Thus a three-element subset \(\{a,b,c\}\subset G\) is the rational-point section of a line exactly when its elements are distinct and \(a+b+c=T\). A two-element subset \(\{a,b\}\) lies on such a line whenever \(2a+b=T\) or \(a+2b=T\). Every rational line meets \(C\) in at most three distinct rational points.

**The two possible groups.** Every abelian group of order \(12\) is isomorphic to either \(C_{12}\) or \(C_2\times C_6\). If four lines cover twelve points they must each contain three distinct rational points, and their sections must partition \(G\). Consequently
\[
\sum_{g\in G}g=4T.
\]
For \(G=C_{12}\), the sum of all elements is the unique nonzero involution, represented by \(6\), whereas no element satisfies \(4T=6\) modulo \(12\). Thus four lines are impossible. For \(G=C_2\times C_6\), the total group sum is zero and \(4T=0\) is equivalent to \(T\in3G\): the order-three component of \(T\) must vanish. Now \(T\in3G\) exactly when \(H\sim3P\) for some rational point \(P\), which is exactly the existence of a rational flex. This establishes the necessary condition for four lines.

**Finite universal line certificates.** Changing the rational origin translates \(T\) by a member of \(3G\), while preserving the number of covering lines. Thus for \(G=C_{12}\) there are only representatives \(T=0,1,2\) modulo \(3G\), and for \(G=C_2\times C_6\) only \(T=(0,0),(0,1),(0,2)\). The following explicit covers establish the complementary upper bounds. Each semicolon-separated group is the set of rational intersection points contributed by one line. A two-element group represents a tangent line; each three-element group is a full distinct-point secant.

For \(G=C_{12}\), use integer residues modulo \(12\):

- \(T=0\): \((0,3,9);(1,4,7);(1,10);(2,4,6);(5,8,11)\).
- \(T=1\): \((0,2,11);(1,5,7);(3,4,6);(7,8,10);(8,9)\).
- \(T=2\): \((0,3,11);(1,6,7);(2,10);(4,5);(8,9)\).

For \(G=C_2\times C_6\), write \((a,b)\) with \(a\) modulo \(2\) and \(b\) modulo \(6\):

- \(T=(0,0)\): \(((0,0),(1,2),(1,4));((0,1),(0,2),(0,3));((0,4),(1,3),(1,5));((0,5),(1,0),(1,1))\).
- \(T=(0,1)\): \(((0,0),(1,0),(1,1));((0,1),(0,3));((0,2),(1,2),(1,3));((0,4),(1,4),(1,5));((0,5),(1,1))\).
- \(T=(0,2)\): \(((0,0),(0,2));((0,1),(1,2),(1,5));((0,3),(1,2),(1,3));((0,4),(1,0),(1,4));((0,5),(1,1),(1,2))\).

Every displayed triple sums to its indicated \(T\). For each displayed pair, one of the two tangent-multiplicity sums equals \(T\). Each row of certificates covers all twelve group elements. The accompanying executable checker verifies those finite identities exhaustively. The first row for \(C_2\times C_6\) proves sufficiency of the rational-flex condition for four lines. The other five rows prove that five lines always suffice. With the lower bounds, the dichotomy follows.

**Realization over one field.** Over \(\mathbb F_{11}\), direct evaluation of \(y^2=x^3+1\) and \(y^2=x^3+2x\) shows \(12\) rational points for each (including infinity). Their respective numbers of nonidentity rational points of order two are \(1\) and \(3\), since the cubics \(x^3+1\) and \(x^3+2x\) have respectively one and three distinct roots in \(\mathbb F_{11}\). Therefore their rational point groups are \(C_{12}\) and \(C_2\times C_6\). Both are Weierstrass plane models and have a rational flex at infinity, giving covering numbers \(5\) and \(4\) respectively.

## Verification
Run `python elliptic_12_cover_check.py` with Python 3. The checker validates every entry of the six certificate rows, that each covers all twelve group elements, and the two smooth \(\mathbb F_{11}\) point counts and 2-torsion counts. The proof of the universal classification uses the collinearity divisor relation and the group-sum obstruction; finite checks are only for finite certificates and sample curves.

## Relationship to prior work
Asgarli, Dassarma, Ghioca, MacLean and Stokdyk study asymptotic covering of plane-curve rational points by lines (arXiv:2610.13042v1, first submitted October 9, 2026). Their abstract states a large-field bound approaching the degree-three counting constant; it does not imply a finite exact classification at cardinality twelve, particularly the dependence on rational flexes and 2-torsion. General zero-sum-partition literature studies related abstract finite-group partitions; the present proof combines the cubic hyperplane-class parameter, the four-line obstruction, and explicit tangent/secant certificates. The source preprint's complete body could not be inspected, so prior occurrence of a related example or proposition remains possible.

## Limitations
Only smooth plane cubics with exactly twelve rational points are classified. This does not determine covering numbers for other point counts or higher-degree curves. In the absence of a rational flex the relevant group-sum constant is generally nonzero; replacing it by zero would make the statement false. Literature-priority uncertainty remains because complete text of the motivating preprint was unavailable in the present review.

## References
- S. Asgarli, S. Dassarma, D. Ghioca, S. MacLean, E. Stokdyk, *Covering plane curves over finite fields with lines*, arXiv:2610.13042v1 (2026-10-09), https://arxiv.org/abs/2610.13042.
- S. Cichacz and K. Suchan, *Zero-sum partitions of Abelian groups and their applications to magic- and antimagic-type labelings*, Discrete Mathematics & Theoretical Computer Science 26:3 (2024), doi:10.46298/dmtcs.12361.
