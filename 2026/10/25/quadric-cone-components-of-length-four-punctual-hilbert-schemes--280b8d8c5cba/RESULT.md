# Quadric-cone components of length-four punctual Hilbert schemes at plane triple points

## Finding
Let \(f\in\mathbb C[[x,y]]\) be reduced with multiplicity exactly \(3\), and write \(f_3\) for its nonzero degree-three homogeneous initial form. Let \(r\in\{1,2,3\}\) be the number of distinct zeros of \(f_3\) in the tangent projective line \(\mathbb P^1\). The *reduced variety* underlying the punctual Hilbert scheme of colength-four ideals of \(R=\mathbb C[[x,y]]/(f)\) has precisely \(r+1\) irreducible two-dimensional components: one \(\mathbb P^2\) and \(r\) rank-three projective quadric cones.

Each cone contains a dense \(\mathbb A^2\) of curvilinear ideals and meets the plane in a line; these lines are indexed by the distinct tangent directions. Different cones meet at the intersection of their boundary lines and nowhere else. Three distinct tangents give three nonconcurrent boundary lines. In particular, for an ordinary triple point the reduced punctual Hilbert scheme has four surface components, whose incidence configuration consists of a central plane and three quadric cones attached along a triangle of lines.

Writing \(\mathbb L=[\mathbb A^1]\) in the Grothendieck ring of complex varieties, the class and compactly supported Euler characteristic are
\[
[H]=[\mathbb P^2]+r\mathbb L^2=1+\mathbb L+(r+1)\mathbb L^2,\qquad \chi_c(H)=3+r.
\]
The motivic formula is a consequence of the geometric stratification; a special case of the coefficient is already known (see below), so the principal contribution is the complete component and incidence geometry.

## Assumptions and scope
Work over \(\mathbb C\). All punctual ideals \(I\) are ideals of \(S=\mathbb C[[x,y]]\) with \(\dim_{\mathbb C}(S/I)=4\), \(I\subset (x,y)\), and \(f\in I\). Every such ideal contains \(\mathfrak m^4\); consequently, all loci embed in a finite Grassmannian of subspaces of \(S/\mathfrak m^4\). All assertions about components, intersections, and motivic classes concern \(H=(\operatorname{Hilb}^4_0(\operatorname{Spec}R))_{\mathrm{red}}\), **not** a claim about the full possibly nonreduced Hilbert scheme.

A tangent direction \(\ell\) means a line through the origin in the tangent plane on which \(f_3\) vanishes. Here \(\ell\) also denotes a linear equation for that line; replacing \(\ell\) by a nonzero scalar does not change any conclusion. The expression \(\mathfrak m^2/\mathfrak m^3\) is three-dimensional, with basis \(x^2,xy,y^2\).

## Proof
**1. Classification by local Hilbert function.** Let \(A=S/I\) and let \(\mathfrak n\) be its maximal ideal. Since \(\operatorname{length}(A)=4\) and the embedding dimension is at most two, either \(\dim(\mathfrak n/\mathfrak n^2)=1\), giving the curvilinear algebra \(\mathbb C[t]/(t^4)\), or it equals two. In the latter case the Hilbert–Samuel function is necessarily \((1,2,1)\) and \(\mathfrak n^3=0\). Thus noncurvilinear ideals contain \(\mathfrak m^3\) and correspond bijectively, also as a projective linear family, to hyperplanes in \(\mathfrak m^2/\mathfrak m^3\):
\[
P=\{I:\mathfrak m^3\subseteq I,\ \dim(\mathfrak m^2/I)=1\}\simeq \mathbb P((\mathfrak m^2/\mathfrak m^3)^*)\simeq\mathbb P^2.
\]
Since \(f\in\mathfrak m^3\), all of \(P\) lies in the curve's punctual Hilbert scheme.

**2. Curvilinear strata.** Pick a tangent direction and independent linear coordinates \(u,v\) so that the direction is \(v=0\). Every length-four curvilinear ideal with that tangent admits a unique normal form
\[
I_{B,C}=\bigl(v-Bu^2-Cu^3,\ u^4\bigr),\qquad (B,C)\in\mathbb A^2.
\]
Substitute \(u=t\), \(v=Bt^2+Ct^3\) modulo \(t^4\). The coefficient of \(t^3\) in \(f\) is \(f_3(1,0)\), with all higher-order terms automatically zero. Therefore \(f\in I_{B,C}\) precisely for tangent directions lying on \(\{f_3=0\}\). Distinct tangent directions give disjoint two-dimensional affine strata, exactly \(r\) of them.

**3. The projective closure of one affine stratum.** Work in coordinates \(u=x,v=y\). In the ten-dimensional vector space \(V=S/\mathfrak m^4\), the six-dimensional ideal subspace has basis
\[
y-Bx^2-Cx^3,\quad xy-Bx^3,\quad y^2,\quad x^2y,\quad xy^2,\quad y^3.
\]
The final four vectors are fixed, and the first two span a moving two-plane in the four-dimensional space with ordered basis \((y,x^2,x^3,xy)\). The six Plücker minors of these two vectors, in index order \((01,02,03,12,13,23)\), are
\[
(0,-B,1,B^2,-B,-C).
\]
Thus the projective closure of the affine stratum lies in a linear \(\mathbb P^3\) of the ambient Plücker space and is exactly the irreducible rank-three quadric surface
\[
Q:\ X_0X_2=X_1^2\quad\subset\mathbb P^3_{[X_0:X_1:X_2:X_3]},
\]
where \((X_0,X_1,X_2,X_3)=(p_{03},p_{13},p_{12},p_{23})\). The chart \(X_0\ne0\) is the original \(\mathbb A^2\), and the boundary \(X_0=0\) consists of \(X_1=0\), a whole projective line. The Plücker map is a closed embedding of the Grassmannian, so no identification or extraneous point is introduced by this closure.

**4. Boundary and incidence.** At a boundary point, the limiting two-plane is spanned by \(x^3\) and a linear combination of \(x^2,xy\); together with the four fixed vectors, this gives a noncurvilinear ideal containing \(y^2\). Conversely every ideal of \(P\) containing \(y^2\) has that form. The boundary is therefore precisely
\[
L_y=\{\lambda\in P:\lambda(y^2)=0\}.
\]
After a linear coordinate change it becomes \(L_{\ell}=\{\lambda(\ell^2)=0\}\) for the original tangent \(\ell\). The affine strata of distinct tangents are disjoint, and every point outside them is in \(P\), so distinct cone closures intersect only in the unique intersection point of their boundary lines. Three distinct tangent lines give three distinct points on the Veronese conic \(\nu_2(\mathbb P^1)\subset\mathbb P^2\); no three points of this nonsingular conic are collinear. Their dual boundary lines are therefore nonconcurrent.

**5. Exhaustion and components.** Steps 1 and 2 classify every length-four ideal. Step 3 identifies the closure of every irreducible open affine stratum with a quadric cone, and Step 4 places its entire boundary in \(P\). The plane \(P\) is itself an irreducible surface and cannot be contained in finitely many boundary lines. Thus the full reduced variety has exactly \(r+1\) irreducible components, all of dimension two. It is stratified into \(P\) and \(r\) disjoint affine planes, yielding the stated motivic and Euler-characteristic formulas.

Only the cubic initial form was used to impose \(f\in I\), proving independence from all higher-order terms. The argument classifies reduced varieties and set-theoretic incidences, not nilpotent structures or scheme-theoretic intersection multiplicities.

## Verification
A standalone exact-arithmetic script, `verify.py`, implements the Plücker minors and independently enumerates ideal-subspaces of dimension six modulo \(\mathfrak m^4\) over the finite fields \(\mathbb F_3,\mathbb F_5,\mathbb F_7\) for the ordinary-triple-point cubic \(f=xy(y-x)\). It verifies that for \(q=3,5,7\) there are \(3q^2\) distinct curvilinear ideals and \(q^2+q+1\) noncurvilinear ideals, that all contain \(f\), and that the respective classifications do not overlap. The resulting totals are \(40,106,204\). The symbolic Plücker identity returns `PLUCKER_QUADRIC_OK`, and the enumeration returns `VERIFY_OK`. Finite-field computations verify only the displayed finite cases; the general complex theorem follows from the preceding algebraic argument.

Reproduce with `python3 verify.py` using Python and SymPy. No other external code, tables, or certificates are required.

## Relationship to prior work
Rossinelli, *Motivic classes of curvilinear Hilbert schemes and Igusa zeta functions* (arXiv:2405.20190, first submitted 2024-05-30), studies motives of curvilinear punctual Hilbert schemes of singularities via arcs and resolutions. Its §4 treats plane curves and a cusp example. That framework concerns the curvilinear open loci; it does not, in the inspected full text, identify the additional noncurvilinear plane, the Plücker quadric-cone closures, or their boundary incidence for every multiplicity-three germ.

Watari, *Motivic Hilbert zeta functions for curve singularities and related invariants* (arXiv:2403.12545, first submitted 2024-03-19), computes Hilbert-scheme motivic coefficients for selected plane-curve singularities. In particular, his displayed \(E_6\) case has fourth coefficient \(1+\mathbb L+2\mathbb L^2\), in agreement with the present \(r=1\) case. **That special numerical case is prior work and is not claimed as new.** The contribution asserted here is the uniform irreducible-component identification, singular projective compactification, and tangent-line incidence. Oblomkov and Shende (arXiv:1003.1568) study punctual Hilbert schemes and link polynomials, principally with explicit calculations for irreducible plane curves; their inspected paper does not state the present uniform component-and-incidence classification.

Ballico and Canino, *Postulation of schemes of length at most 4 on surfaces* (2026), §2 (especially Remark 2.9), recall the standard three types of punctual length-four subschemes on a smooth surface and identify the two-dimensional noncurvilinear locus. That prior ambient classification is acknowledged; their postulation paper does not provide the locus cut out by a singular curve's cubic initial form or the present quadric-cone attachment arrangement. The established classification of length-four punctual algebras is used as a starting point, not claimed as a new result.

## Limitations
The theorem concerns reduced underlying varieties in characteristic zero and multiplicity exactly three. It does not calculate nonreduced Hilbert-scheme structures, local intersection multiplicities, scheme-theoretic singularities, or higher-length punctual Hilbert schemes. In the three-tangent case the motive and Euler count are numerical consequences of the stronger incidence classification; related numerical special cases were previously computed. The novelty comparison is best-knowledge rather than a proof of priority against all unindexed sources.

## References
1. I. Rossinelli, *Motivic classes of curvilinear Hilbert schemes and Igusa zeta functions*, arXiv:2405.20190 (2024), especially §§2–4. https://arxiv.org/abs/2405.20190
2. M. Watari, *Motivic Hilbert zeta functions for curve singularities and related invariants*, arXiv:2403.12545 (2024), especially the \(E_6\) table and formula. https://arxiv.org/abs/2403.12545
3. A. Oblomkov and V. Shende, *The Hilbert scheme of a plane curve singularity and the HOMFLY polynomial of its link*, arXiv:1003.1568 (2010). https://arxiv.org/abs/1003.1568
4. E. Ballico and S. Canino, *Postulation of schemes of length at most 4 on surfaces*, Bulletin of the London Mathematical Society (2026), §2, background on length-four ambient strata. https://doi.org/10.1112/blms.70328
5. A. Iarrobino, *Punctual Hilbert Schemes*, Memoirs of the American Mathematical Society 188 (1977), background on punctual strata and local parameters. https://doi.org/10.1090/memo/0188
