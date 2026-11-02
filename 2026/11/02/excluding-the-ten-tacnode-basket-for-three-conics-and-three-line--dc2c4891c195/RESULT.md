# Excluding the ten-tacnode basket for three conics and three lines

## Finding

Let \(\mathcal A\subset\mathbb P^2_{\mathbb C}\) be a reduced union of **three distinct smooth conics and three distinct lines**. Suppose all singularities of the union are ordinary nodes \(A_1\), ordinary tacnodes \(A_3\), or ordinary transverse triple points \(D_4\). Let \(n_2,t,n_3\) be their respective numbers. Then the basket
\[
 (n_2,t,n_3)=(1,10,4)
\]
**cannot occur**, independently of any assumption about freeness.

Consequently, if \(\mathcal A\) is nearly free, its only possible weak singularity basket is
\[
(n_2,t,n_3)=(0,9,5).
\]
This is a necessary condition, **not** an existence theorem for the latter basket.

## Assumptions and scope

All six components are reduced and pairwise distinct, the base field is \(\mathbb C\), and each conic is nonsingular. A node is a transverse intersection of two smooth branches, a tacnode is an ordinary contact of two smooth branches of intersection multiplicity two, and an ordinary triple point consists of three pairwise transverse smooth branches. Fourfold points, cusps and nonordinary triple tangencies are excluded. In particular, two distinct lines never contribute a tacnode, and a line passing through a conic--conic tacnode would create a forbidden singularity if it were tangent to both branches.

Label the conics \(C_0,C_1,C_2\) and lines \(L_0,L_1,L_2\). Write \(t_{CC}\) and \(t_{CL}\) for tacnodes involving two conics and a conic with a line. Let \(x,y,z,w\), respectively, count transverse triple points with component types \(CCC\), \(CCL\), \(CLL\), and \(LLL\). For the excluded basket,
\[
 x+y+z+w=4,\qquad t_{CC}+t_{CL}=10.
\]
The pairwise Bézout total is \(3\cdot4+9\cdot2+3=33=1+2(10)+3(4)\).

## Proof

**Preliminary incidence restrictions.** Every conic--line pair has total intersection multiplicity two. Its contribution at a tacnode is two, at a transverse triple point involving that pair is one, and at a node is one. Summing over nine conic--line pairs, we obtain
\[
18=2t_{CL}+2y+2z+n_{CL},
\]
where \(n_{CL}\) is the number of conic--line nodes. Hence \(n_{CL}\) is even; since the basket contains only one node in total, \(n_{CL}=0\). Therefore
\[
 t_{CL}=9-y-z,\qquad t_{CC}=1+y+z.
\]
Each conic pair has Bézout intersection total four. In particular, a pair containing a transverse triple point of type \(CCC\) has at most one tacnode, whereas a pair with two tacnodes has no remaining transverse intersection.

**Common-tangent obstruction.** If two smooth conics meet in precisely two ordinary tacnodes, *no arrangement line can be tangent to both*. Indeed, the dual conics meet with intersection multiplicity at least two at the dual points of the tangent lines at the two tacnodes. Their dual intersection number is four; these are therefore the only common tangent lines. Each of those passes through the corresponding original tacnode, and adjoining it would make a forbidden triple contact. This also proves the version of the obstruction used in Dimca--Pokora, Lemma 5.1 [1].

**Case 1: the three lines are concurrent.** Their common point contributes one \(LLL\) triple point and no line--line node, so \(w=1,z=0\). No conic passes through that common point, since four smooth branches there would be forbidden. Thus \(x+y=3\), and
\[
 t_{CL}=9-y=6+x.
\]
From a point outside a smooth conic, at most two lines through that point can be tangent to it, as follows by Bézout or by intersecting the dual conic with the pencil line. Therefore the three conics admit at most six tangencies with the concurrent lines. Hence \(x=0,y=3,t_{CL}=6,t_{CC}=4\). Each conic is tangent to exactly two of the three lines. Any two conics share at least one of these tangent lines. By the common-tangent obstruction, no conic pair can have two tacnodes, so \(t_{CC}\le3\), a contradiction.

**Case 2: the three lines form a triangle.** Their three pairwise intersections are distinct. At most one can remain a node, so either \(z=2\) or \(z=3\); no \(LLL\) triple point occurs. If a conic passes through a triangle vertex as a transverse \(CLL\) triple point, it cannot be tangent anywhere to either incident side: the one transverse intersection already consumes one of that conic--line pair's two Bézout units. Thus that conic has at most the opposite side available as a tangent.

**Subcase \(z=2\).** One triangle vertex is the unique node. Then \(x+y=2\), and
\[
 t_{CL}=7-y,\qquad t_{CC}=3+y.
\]
If the two occupied vertices lie on *different* conics, those two conics each have at most one tangent side, and the third has at most three. This gives \(t_{CL}\le5\), forcing \(y=2,x=0,t_{CL}=5,t_{CC}=5\). All five available conic--side tangencies occur. The third conic shares a tangent side with each of the first two, so each of these two conic pairs has at most one tacnode. The remaining conic pair has at most two. Hence \(t_{CC}\le4\), contradiction.

If the two occupied vertices lie on the *same* conic \(C_0\), that conic is transverse to all three sides and tangent to none. Thus \(t_{CL}\le6\), ruling out \(y=0\). If \(y=1\), then \(x=1\) and \(t_{CC}=4\). The \(CCC\) point lies on every conic pair, permitting at most one tacnode per pair; therefore \(t_{CC}\le3\), contradiction. If \(y=2\), then \(x=0,t_{CL}=5,t_{CC}=5\). All tangencies come from \(C_1,C_2\); five of their six potential conic--side slots are tangent. They share a tangent side, so the pair \(C_1,C_2\) contributes at most one tacnode. Reaching five conic--conic tacnodes requires both \(C_0C_1\) and \(C_0C_2\) to have two tacnodes each. Those pairs therefore have no transverse intersection; both \(CCL\) triples must involve \(C_1,C_2\). But such a transverse triple requires one side **nontangent to both** \(C_1\) and \(C_2\). With five of six slots tangent, no such side exists, contradiction.

**Subcase \(z=3\).** All three triangle vertices contain \(CLL\) triples; the sole node belongs to two conics. Now \(x+y=1\) and
\[
 t_{CL}=6-y,\qquad t_{CC}=4+y.
\]
If the vertices involve at least two distinct conics, they use at least five conic--side incidence slots: one conic appearing at two vertices cannot tangent to any of the three sides, while another appearing at one vertex cannot tangent to its two incident sides. Consequently at most four conic--side tangencies remain, contrary to \(t_{CL}\ge5\). Thus all three vertices must lie on the *same* conic \(C_0\), which is tangent to no side. If \(y=0\), then \(x=1\), and the \(CCC\) triple bounds \(t_{CC}\le3<4\). If \(y=1\), then \(x=0,t_{CL}=5,t_{CC}=5\). As in the final paragraph of subcase \(z=2\), the other two conics have five of their six side slots tangent, so they share a tangent line. Their pair has at most one tacnode, forcing the two pairs involving \(C_0\) to be doubly tangent. The required \(CCL\) triple would involve the other two conics on a side transverse to both, but there is no such side. Contradiction.

These cases exhaust all triples of distinct projective lines, proving nonexistence of the basket.

**Nearly free corollary.** A nearly free curve of total degree \(m=9\) has minimal Jacobian-relation degree \(r\) satisfying
\[
 \frac{2m}{3}-2\le r\le\frac m2
\]
by Gałecka, Proposition 4.1 [2]; hence \(r=4\). The near-freeness Tjurina identity gives
\[
\tau=r^2-r(m-1)+(m-1)^2-1=47.
\]
Subtracting Bézout's identity \(n_2+2t+3n_3=33\) from \(n_2+3t+4n_3=47\) yields \(t+n_3=14\), and then \(n_2+n_3=5\). Gałecka's orbifold inequality (Proposition 4.4 [2]) is
\[
8k+n_2+\tfrac34n_3\ge d+\tfrac52t.
\]
For \(k=d=3\), these equalities imply \(n_3\ge4\) and \(n_3\le5\). The two numerical possibilities are \((1,10,4)\) and \((0,9,5)\). We have excluded the first, leaving only the second as a necessary weak basket. \(\square\)

## Verification

Execute `python3 verify_incidence.py` in a Python 3 environment. The script exhausts a finite **over-approximation** of all permitted incidence assignments: concurrent versus triangular lines; occupied vertices and their conic assignments; the nine binary conic--line tangency slots; the three conic-pair tacnode counts; and the placement of all \(CCL\) points. Its exact-integer feasibility test returns `EXACT_THREE_CONIC_THREE_LINE_INCIDENCE_INFEASIBLE_OK`. Because the program deliberately allows incidence assignments that might not be geometrically realizable, its finding of **no** feasible assignments is a valid corroboration. The written projective incidence proof, not the finite program alone, supplies the mathematical justification.

## Relationship to prior work

Dimca--Pokora [1] provide the combinatorial framework and common-tangent obstruction, and classify **free** conic--line arrangements in this singularity class. Gałecka [2] studies **nearly free** arrangements and leaves degree nine open, giving the inequality and near-freeness identities used here. The new claim concerns an unconditional weak basket for precisely three conics and three lines, and the resulting necessary near-freeness basket. It does not reassert an earlier free-arrangement exclusion. Later conic-only classifications do not directly imply a statement about three additional lines. No claim of a complete degree-nine classification is made.

## Limitations

Only the one basket \((1,10,4)\) is excluded here; the status and realizability of \((0,9,5)\) are open under this argument. The assertion requires all three conics smooth, all six components distinct, and only the listed ordinary singularity types. Additional singularity types, repeated components, and positive-characteristic settings are outside its scope. Searches cannot rule out all unindexed earlier incidence arguments; independent mathematical audit and validation have not been performed.

## References

[1] A. Dimca and P. Pokora, *On conic-line arrangements with nodes, tacnodes, and ordinary triple points*, arXiv:2111.12349 (first public version 2021-11-24); *Journal of Algebraic Combinatorics* 56 (2022), 403–424, Lemma 5.1 and Section 5. https://arxiv.org/abs/2111.12349 ; https://doi.org/10.1007/s10801-022-01116-3 .

[2] A. Gałecka, *On the nearly freeness of conic-line arrangements with nodes, tacnodes, and ordinary triple points*, arXiv:2204.13969 (first public version 2022-04-29); *Boletín de la Sociedad Matemática Mexicana* 28 (2022), 67, Propositions 4.1 and 4.4, Section 5. https://arxiv.org/abs/2204.13969 ; https://doi.org/10.1007/s40590-022-00461-4 .
