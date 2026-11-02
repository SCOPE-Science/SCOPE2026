# No nearly free degree-nine arrangement of one conic and seven lines with only \(A_1,A_3,D_4\) singularities

## Finding
There is no reduced arrangement \(C=Q\cup L_1\cup\cdots\cup L_7\subset\mathbf P^2_{\mathbb C}\), with \(Q\) a smooth conic and the \(L_i\) distinct lines, that is nearly free and whose only singularities are ordinary nodes (\(A_1\)), ordinary tacnodes (\(A_3\)), and ordinary transverse triple points (\(D_4\)). The nearly-free hypothesis is in the standard sense of the minimal Jacobian syzygy degree and a two-exponent nearly-free resolution.

This resolves the one-conic/seven-line component case of the degree-nine existence question in Gałecka's 2022 partial classification; it makes no claim for arrangements with two, three, or four conics, or those admitting higher-multiplicity singularities.

## Assumptions and scope
We work over \(\mathbb C\), where a smooth conic has a unique tangent at each point. The components are reduced and pairwise distinct. An ordinary triple point has three smooth pairwise transverse branches. A tacnode has two tangent smooth branches and, in this arrangement, necessarily consists of the conic and a line. Let \(t,n_2,n_3\) count tacnodes, nodes, and triple points. Write \(s=7-t\) for the number of secant (non-tangent) lines; no line is contained in the conic.

## Proof
**1. Numerical reduction.** Gałecka (arXiv:2204.13969, §§2–5) proves that a nearly free arrangement of total degree nine with the specified singularities must have exponents \((4,5)\); indeed the cited lower bound on minimal Jacobian syzygy degree is \(\operatorname{mdr}\ge 2m/3-2=4\), while the smaller exponent is at most \(m/2\). The nearly-free Tjurina formula gives \(\tau=8^2-4(5-1)-1=47\). For one conic and seven lines, Bézout gives \(n_2+2t+3n_3=35\) and \(\tau=n_2+3t+4n_3=47\). Hence
\[
 t+n_3=12,\qquad n_3=5+s,\qquad n_2=6-s.
\]
In particular \(s\le6\). Moreover Gałecka's published inequality \(8k+n_2+3n_3/4\ge d+5t/2\), with \((k,d)=(1,7)\), reduces to \(s\ge3\). Thus only \(s=3,4,5,6\) remain.

**2. Finite incidence reduction.** Call a triple point of the conic and two secant lines a **conic triple**, and call a triple among the seven lines a **line triple**. Their numbers are \(q\) and \(\ell=5+s-q\). Each secant meets \(Q\) at exactly two distinct points, so the graph of conic triples on the \(s\) secants has degree at most two; it is a simple graph. Conic triples consume one unordered secant pair each. A line triple consumes three unordered line pairs; no two distinct multiple points consume the same pair. No line triple may use three tangent lines, because at most two distinct tangents to a nonsingular conic pass through a point. It follows that the admissible incidence data are finite.

Exhausting these exact pair-disjointness constraints gives five labelled-orbit patterns: two for \(s=3\), one for \(s=4\), none for \(s=5\), and one for \(s=6\). The standalone `verify_incidence.py` enumerates every graph and every line-triple packing (no random samples or projective-realizability assumptions), applies all permutations of the secants and tangents, and returns class sizes \((18,36),(24),(),(60)\), respectively. The representatives are printed by the program. The next steps rule out **every** combinatorially admissible pattern geometrically.

**3. Four tangent lines and three secants (\(s=3\)).** Let the four tangent lines form a complete quadrilateral. Its six pairwise vertices have only three joining lines that are not themselves one of the four tangents: the three diagonal lines joining opposite vertices. In the first admissible incidence type, each of the three secants passes through two opposite tangent-pair vertices; hence they must be those three diagonals. The diagonal triangle of a quadrilateral circumscribed about a nonsingular conic is self-polar, and none of its three vertices lies on the conic (a point on a nonsingular conic is never incident with its own polar). But two secant-pair intersections are required to lie on the conic. Contradiction. In the second admissible type, two distinct secants are diagonal lines and their intersection is required to lie on the conic; again impossible.

**4. Three tangent lines and four secants (\(s=4\)).** The unique admissible pattern has three secant lines \(S_0,S_1,S_2\) forming a triangle inscribed in \(Q\) (their three pairwise intersections are conic triples), and a fourth secant \(S_3\). Normalize the three distinct points of tangency by \(\operatorname{PGL}_2\) on \(Q\) to \(0,1,\infty\). In homogeneous coordinates \(Q(t)=[t^2:t:1]\), the three tangent lines are
\[
 T_4:X=0,\qquad T_5:X-2Y+Z=0,\qquad T_6:Z=0.
\]
The chord joining parameters \(a,b\) has coordinates \([1,-(a+b),ab]\). Label the inscribed-triangle vertices \(u,v,w\) with sides \(S_0=(u,v),S_1=(v,w),S_2=(w,u)\). The three required incidences \(S_0\ni T_5\cap T_6\), \(S_1\ni T_4\cap T_6\), and \(S_2\ni T_4\cap T_5\) force
\[
 u+v=2,\quad v+w=0,\quad u+w=2uw;
 \qquad u=2-v,\ w=-v,\ v^2-v-1=0.
\]
The remaining three line triples force \(S_3\) to contain \(S_0\cap T_4\), \(S_1\cap T_5\), and \(S_2\cap T_6\). The determinant of these three homogeneous point columns equals
\[
 4(2v-1)(v^2-v+1).
\]
On \(v^2-v-1=0\) this equals \(8(2v-1)\ne0\). The three points are not collinear, so \(S_3\) cannot exist.

**5. One tangent line and six secants (\(s=6\)).** Here \(n_2=0\), so \(q=6\) and \(\ell=5\). The conic-triple graph on the six secants is 2-regular. If it is two disjoint triangles, its complementary available graph of secant pairs is bipartite and has no triangles, whereas two line-only triples involving three secants are forced; impossible. Thus it is a six-cycle. The six secants are precisely the sides of a hexagon inscribed in \(Q\). The other line triples force three alternate sides to concur at \(P\), the other three to concur at \(R\), and the unique tangent line to contain the three intersections of opposite sides (the Pascal line).

The two pencils through \(P,R\) induce distinct involutions of \(Q\cong\mathbf P^1\) whose product permutes three alternating vertices cyclically; it therefore has order three. Conjugating their dihedral action on \(\mathbf P^1\), the six distinct vertices may be written
\[
 u,\ u^{-1},\ \omega u,\ \omega^2u^{-1},\ \omega^2u,\ \omega u^{-1},
 \qquad \omega^2+\omega+1=0,\quad \omega\ne1.
\]
Here \(u\ne0\) and \(u^2\notin\{1,\omega,\omega^2\}\), since the vertices are distinct. Applying the chord equation from step 4 to successive pairs and intersecting opposite sides gives the Pascal line
\[
 X-\omega^2 Z=0.
\]
Its intersection with the nonsingular conic has distinct parameters \(t=\omega\) and \(t=-\omega\); it is a secant, not a tangent. The required last line cannot be a tangent. (A direct independent symbolic check of all three intersections appears in `verify_geometry.py`.)

All four possible values of \(s\) have been excluded; the asserted nonexistence follows. \(\square\)

## Verification
Run `python verify_incidence.py` and `python verify_geometry.py` (the second uses SymPy). Both were run from this package. Their success markers are `EXACT_DEGREE9_CONIC_SEVEN_LINES_INCIDENCE_CLASSES_OK`, `THREE_TANGENTS_FOUR_SECANTS_COLLINEARITY_IMPOSSIBLE_OK`, and `HEXAGON_PASCAL_LINE_NON_TANGENT_OK`. All incidence enumeration is finite and exhaustive, while the conic geometry steps are exact identities in characteristic zero. This is not a numerical experiment about all possible plane equations.

## Relationship to prior work
Gałecka's 2022 paper formulated the still-open degree-eight and degree-nine nearly-free existence cases and supplied the numerical Tjurina and BMY/Hirzebruch-type inequalities employed above. A separate published 2026 example with seven lines and a conic has ordinary quadruple points, outside the permitted singularity class, and hence neither proves nor contradicts the finding. The 2026 degree-eight existence construction in the published mathematical record likewise does not imply the degree-nine one-conic nonexistence. This proof adds the projective realization obstruction not contained in the cited numerical inequalities.

## Limitations
The statement does not exclude degree-nine arrangements containing two or more conics; degree-eight arrangements; or curves with singularities beyond nodes, tacnodes and ordinary triple points. No assertion about ordinary freeness, as opposed to near freeness, is made. The originality assessment cannot establish absolute priority against unindexed or inaccessible works. No independent external audit has occurred.

## References
1. A. Gałecka, *On the nearly freeness of conic-line arrangements with nodes, tacnodes, and ordinary triple points*, arXiv:2204.13969, first public 2022-04-29; Bol. Soc. Mat. Mex. 28 (2022), 67. https://arxiv.org/abs/2204.13969 .
2. A. Dimca and P. Pokora, *On conic-line arrangements with nodes, tacnodes, and ordinary triple points*, J. Algebr. Comb. 56 (2022), 403–424. https://doi.org/10.1007/s10801-022-01116-3 .
3. P. Pokora, *On the Numerical Terao Conjecture*, arXiv:2608.05662 (2026), higher-multiplicity comparison only.
