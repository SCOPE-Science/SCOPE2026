# The finite mapping space from a minimal projective plane to the four-point circle has circle core
## Finding
Let \(P=\mathbb{P}^{2}_{2}\) be the 13-point minimal finite model of \(\mathbb{RP}^{2}\) described by Cianci and Ottina, and let \(C=S^{0}\circledast S^{0}\) be the four-point minimal finite circle. Then the compact-open mapping space \(\operatorname{Map}(P,C)\) has exactly \(868\) points and has core exactly the four constant maps. More precisely, there is a sequence of \(864\) legal beat-point deletions, with \(196\) up-beat and \(668\) down-beat deletions, after which the remaining four maps are the constants and inherit the order of \(C\). Therefore
\[
\operatorname{core}(\operatorname{Map}(P,C))\cong C,
\qquad
\operatorname{Map}(P,C)\simeq C.
\]
Consequently \([P,C]\) consists of one homotopy class and the order complex of the finite mapping space has homotopy type \(S^{1}\).

## Assumptions and scope
The source is the specific Cianci--Ottina model \(P=\mathbb{P}^{2}_{2}\). Write its minimal points as \(c_1,c_2,c_3,c_4\), its middle points as \(b_1,\ldots,b_6\), and its maximal points as \(a_1,a_2,a_3\). The upper incidences are
\[
\{b_1,b_2\}<\{a_1,a_2\},\qquad
\{b_3,b_4\}<\{a_1,a_3\},\qquad
\{b_5,b_6\}<\{a_2,a_3\},
\]
in the sense that each displayed middle point lies below each displayed maximal point. The lower incidences are
\[
\widehat U_{b_1}=\{c_1,c_2\},\quad
\widehat U_{b_2}=\{c_3,c_4\},\quad
\widehat U_{b_3}=\{c_1,c_3\},\quad
\widehat U_{b_4}=\{c_2,c_4\},\quad
\widehat U_{b_5}=\{c_2,c_3\},\quad
\widehat U_{b_6}=\{c_1,c_4\}.
\]
The target \(C\) has two incomparable minimal points and two incomparable maximal points, with every minimal point below every maximal point. The claim concerns the ordinary compact-open function space of continuous maps between these finite spaces.

## Proof
For finite \(T_0\)-spaces, continuity is equivalent to order preservation. Enumerate the points of \(P\) in the linear extension
\[
c_1,c_2,c_3,c_4,b_1,b_2,b_3,b_4,b_5,b_6,a_1,a_2,a_3.
\]
A recursive enumeration assigns a target point to each source point and retains an assignment exactly when the new target value is above the values already assigned to every predecessor. Because every predecessor occurs earlier in the displayed linear extension, this procedure enumerates every order-preserving map exactly once. It yields exactly \(868\) maps.

Give these maps the pointwise order: \(f\leq g\) when \(f(x)\leq g(x)\) for every \(x\in P\). For finite source and target this is the specialization order of the compact-open mapping space. The packaged certificate records \(864\) successive deletions. At each step the deleted map is checked in the current induced mapping poset to be either an up-beat point with a least strict upper neighbor or a down-beat point with a greatest strict lower neighbor. The sequence contains \(196\) up-beat and \(668\) down-beat deletions.

The four maps left by the certificate are exactly the four constant maps. For target points \(u,v\in C\), the corresponding constants satisfy \(\operatorname{const}_u\leq\operatorname{const}_v\) exactly when \(u\leq v\). Thus the terminal induced subposet is canonically isomorphic to \(C\). A final check shows that none of its four points is a beat point. Since deletion of a beat point is a strong deformation retraction, the terminal copy of \(C\) is a core of the full mapping space. This proves the stated homotopy equivalence. The mapping poset is connected, so there is one finite-space homotopy class of maps \(P\to C\). Finally, the order complex of \(C\) is the four-cycle, hence has homotopy type \(S^1\).

## Verification
The standalone verifier reconstructs \(P\) and \(C\) from the incidence data above, enumerates all order-preserving maps, reconstructs the entire pointwise order on the \(868\) maps, checks connectedness, and replays every beat-point certificate entry against the current induced subposet. It then verifies that the remaining indices are exactly the four constants, that their inherited order is \(C\), and that the terminal subspace has no beat points. Its exact terminal line is recorded in `verification_output.txt`.

The computation is exhaustive for this finite statement. It is not used as evidence for a claim about arbitrary finite models or an infinite family.

## Relationship to prior work
Cianci and Ottina prove that every 13-point finite model of \(\mathbb{RP}^2\) is one of two opposite models and explicitly identify the incidence pattern of \(\mathbb{P}^2_2\). Their paper does not compute the compact-open mapping space from that model to the four-point circle. May and Pishevar show that for finite spaces the compact-open specialization order on a function space is the pointwise order and that comparability fences characterize homotopy; they also review cores and beat-point reduction. Those general results convert the finite certificate here into the asserted homotopy statement but do not determine the \(868\)-point function poset or its core.

A closely related computation in the opposite direction, from the four-point circle into \(P\), is logically asymmetric: function spaces are contravariant in the source and covariant in the target, so neither its map count nor its homotopy components imply the present result. Searches for the exact map count, the reverse-direction mapping space, equivalent function-poset formulations, and a precomputed core did not locate a covering published statement.

## Limitations
The exact cardinality and deletion certificate are for the specified 13-point model \(\mathbb{P}^2_2\), not for every finite model weakly equivalent to \(\mathbb{RP}^2\). The result does not claim that finite mapping spaces preserve classical mapping-space homotopy types in general. The originality search cannot exclude an uncatalogued computation, and an older paper on pairings of finite spaces was available only through metadata and abstract-level evidence; its stated subject is finite multiplication and Hopf constructions rather than this function-poset core.

## References
1. Nicolás Cianci and Miguel Ottina, “Poset splitting and minimality of finite models,” arXiv:1512.06088v1, 2015.
2. J. P. May and Elle Pishevar, “Finite Spaces and Larger Contexts,” Chapter 3, especially Sections 3.2 and 3.4.
3. R. E. Stong, “Finite topological spaces,” Transactions of the American Mathematical Society 123 (1966), 325–340.
4. K. A. Hardie, J. J. C. Vermeulen, and P. J. Witbooi, “A nontrivial pairing of finite \(T_0\) spaces,” Topology and its Applications 125 (2002/2003), 533–542, DOI 10.1016/S0166-8641(01)00298-X.
