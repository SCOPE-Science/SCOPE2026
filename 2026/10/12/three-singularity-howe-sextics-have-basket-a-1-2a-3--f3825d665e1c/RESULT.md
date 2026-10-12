# Three-singularity Howe sextics have basket \(A_1+2A_3\)
## Finding
Let \(k\) be algebraically closed of characteristic \(0\) or at least \(7\). Consider the absolutely irreducible plane sextic \(\widetilde C\) constructed by Moriya and Kudo from a non-hyperelliptic genus-five Howe curve of parameter type \((g_1,g_2,r)=(2,2,4)\). Their Proposition 4.2.6 has two cases in which \(\widetilde C\) has exactly three singular points. In every such case the complete analytic singularity basket is
\[
A_1+2A_3.
\]
The point \((0:0:1)\) is the node already identified in the source. The other two singularities are ordinary tacnodes. Moreover, the second algebraic alternative in their Lemma 4.2.2 cannot occur for a sextic arising from Howe-type parameters.

## Assumptions and scope
The statement concerns the Moriya--Kudo model from arXiv:2310.15993v1 in the characteristic range used for its singularity analysis, namely characteristic \(0\) or at least \(7\). The sextic is absolutely irreducible and its normalization is the given smooth Howe curve of genus \(5\). The result is conditional only on being in Case II or Case III of Proposition 4.2.6; it makes no assertion about the analytic types of the four moving double points in the generic five-singularity case.

The relevant homogeneous form is even in each projective coordinate that changes sign in the construction. In Case II the two additional points are \((\pm y:1:0)\). In Case III they are either \((\pm y:0:1)\) or \((0:\pm z:1)\). The sign changes are automorphisms of the plane model, so the two members of each pair have the same local \(\delta\)-invariant.

## Proof
An irreducible plane sextic has arithmetic genus \(10\). Since the normalization of \(\widetilde C\) has genus \(5\), the sum of the local \(\delta\)-invariants of all singularities is exactly
\[
10-5=5.
\]
The source proves that \((0:0:1)\) is an ordinary node, hence contributes \(1\). In either three-singularity case the remaining two points are exchanged by a sign involution, so they have equal \(\delta\)-invariant. Each therefore contributes
\[
\frac{5-1}{2}=2.
\]

For Case III, take first a point \((y:0:1)\). With local coordinates \(u=Y-y\) and \(v=Z\), the source proves that the quadratic term in the \(u\)-direction is nonzero while the pure \(v^2\)-term vanishes, and that formally the germ has the shape \(U^2-h(v)\) with order at least \(4\). The original local equation is invariant under \(v\mapsto-v\). The formal critical section used in the splitting lemma is unique and is therefore even in \(v\); consequently \(h(v)\) is even. For a reduced plane germ \(U^2-h(v)\) in characteristic different from \(2\), if \(m=\operatorname{ord}_v h\), then \(\delta=\lfloor m/2\rfloor\). Here \(m\ge4\), \(m\) is even, and \(\delta=2\), so \(m=4\). Thus the germ is \(A_3\). The case \((0:z:1)\) is identical after interchanging the coordinates.

For Case II, work near \((y:1:0)\) in the chart \(Z=1\), writing \(u=Y-y\) and \(v=X\). Set
\[
P(s)=c_{60}s^3+c_{42}s^2+c_{24}s+c_{06}.
\]
Then \(F(Y,1,0)=P(Y^2)\). The second system in Lemma 4.2.2 is
\[
c_{42}^2-3c_{60}c_{24}=0,\qquad c_{42}c_{24}-9c_{60}c_{06}=0.
\]
It is exactly the condition that \(P\) have a triple root at \(s_0=-c_{42}/(3c_{60})\). Since \(y\ne0\), this makes \(F(y+u,1,0)\) start in degree \(3\) in \(u\). Proposition 4.2.6 says the point nevertheless has multiplicity \(2\), and the full local equation is even in \(v\); hence its quadratic term must be a nonzero multiple of \(v^2\). Formal splitting in the \(v\)-direction then gives an \(A_2\) cusp, whose \(\delta\)-invariant is \(1\). This contradicts the forced value \(\delta=2\). Therefore the second system cannot occur for Howe-type parameters.

Only the first system in Lemma 4.2.2 remains. There \(P\) has a double, not triple, root, so the local quadratic coefficient of \(u^2\) is nonzero. If a nonzero \(v^2\)-term were also present, then over the algebraically closed field the tangent cone would split into two distinct lines, making the point a node and giving \(\delta=1\), again impossible. Thus the tangent cone is a double line. Splitting in the \(u\)-direction gives \(U^2-h(v)\); invariance under \(v\mapsto-v\) makes \(h\) even. The already established value \(\delta=2\) forces \(\operatorname{ord} h=4\), so both Case-II points are \(A_3\) tacnodes.

## Verification
The accompanying `verify.py` checks three finite algebraic pieces. First, it verifies symbolically that Lemma 4.2.2 system (2) makes \(P\) have a triple root. Second, it checks the genus-defect arithmetic that forces \(\delta=2\) for each member of a three-singularity symmetric pair. Third, it replays the paper's explicit Case-II example over \(\mathbb F_{31}\): at \((13:1:0)\) the local quadratic term is a nonzero multiple of \(u^2\), and after formal completion of the square the first transverse term has order \(4\) with nonzero coefficient. The paired point follows by symmetry.

The computation is supplementary. The universal statement is proved by the genus formula, the source's exact singular-point classification, sign symmetry, and formal local splitting; it is not inferred from the finite-field example.

## Relationship to prior work
Moriya--Kudo prove that their model has either three or five multiplicity-two singular points, identify \((0:0:1)\) as a node, and in Case III obtain a formal equation \(Y^2-Z^\alpha\) (or its transpose) only with \(\alpha\ge4\), describing the situation parenthetically as, for example, a tacnode. They do not determine \(\alpha\), do not give the exact ADE basket of the three-singularity cases, and Lemma 4.2.2 retains a second coefficient alternative for points at infinity.

Kudo's companion paper on the other genus-five Howe parameter type \((1,1,0)\) restates the earlier result only as three or five multiplicity-two singularities for the \((2,2,4)\) model. Searches using the exact paper identifier, Howe-curve terminology, tacnode/ADE terminology, the basket \(A_1+2A_3\), and the coefficient alternative did not locate a published statement implying the result above.

## Limitations
The result does not classify the local analytic types in the generic five-singularity case. It also does not address characteristics \(2,3,5\), which lie outside the source's singularity-analysis range used here. A future or presently inaccessible treatment of the same sextic family under different coordinates could contain an equivalent local classification; the strongest identified residual risk is the cited in-preparation work on explicit genus-five Howe sextics and superspecial enumeration.

## References
1. T. Moriya and M. Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, I*, arXiv:2310.15993v1, first public 2023-10-24; Journal of Computational Algebra 11 (2024), 100018, DOI:10.1016/j.jaca.2024.100018.
2. M. Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, II*, arXiv:2401.00760v1; Journal of Computational Algebra 11 (2024), 100019, DOI:10.1016/j.jaca.2024.100019.
3. MSC2020, 14H20, *Singularities of curves, local rings*.
