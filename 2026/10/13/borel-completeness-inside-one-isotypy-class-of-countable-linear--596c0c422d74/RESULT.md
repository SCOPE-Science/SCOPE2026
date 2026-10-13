# Borel completeness inside one isotypy class of countable linear orders

## Finding
For a countable linear order \(L\), put
\[
x\,E_L\,y \quad\Longleftrightarrow\quad \text{the interval between }x\text{ and }y\text{ is finite}.
\]
Let \(\mathcal I\) be the class of orders for which \(E_L\) has infinitely many classes and every \(E_L\)-class has order type \((\mathbb Z,<)\). Then
\[
\boxed{\mathcal I\text{ is exactly one isotypy class of countable linear orders,}}
\]
\[
\boxed{\mathcal I\text{ is an invariant Borel class, and }\cong\!\upharpoonright\mathcal I\text{ is Borel complete}.}
\]
Thus fixing the complete collection of realized finite tuple types does not lower isomorphism complexity: maximal Friedman--Stanley complexity already occurs inside a single isotypy class.

## Assumptions and scope
All structures are countable linear orders with underlying set \(\mathbb N\), in the usual standard Borel coding space. Isotypy means equality of the realized complete first-order types of finite tuples in both directions. Borel completeness is in the Friedman--Stanley sense for isomorphism relations on invariant Borel classes of countable structures.

## Proof
Gvozdevsky proves that for any infinite linear orders \(A,B\), the lexicographic products \(A\times\mathbb Z\) and \(B\times\mathbb Z\) are isotypic, and that
\[
A\times\mathbb Z\cong B\times\mathbb Z\quad\Longrightarrow\quad A\cong B,
\]
because the quotient by finite distance recovers the first factor.

First identify the whole isotypy class. Every \(L\in\mathcal I\) is isomorphic to \((L/E_L)\times\mathbb Z\): the \(E_L\)-classes are convex copies of \(\mathbb Z\), and the quotient orders those classes lexicographically. The quotient is infinite, so Gvozdevsky's corollary makes every two members of \(\mathcal I\) isotypic.

Conversely, fix any infinite \(A\) and suppose \(M\) is isotypic to \(A\times\mathbb Z\). Every element of \(A\times\mathbb Z\) has an immediate predecessor and successor. The same one-variable complete type is therefore realized by every element of \(M\), so each finite-distance class of \(M\) is a discrete order without endpoints. By definition any two points in such a class are separated by only finitely many points; consequently each class is order-isomorphic to \(\mathbb Z\). For every \(n\), the source has an \(n\)-tuple chosen from distinct fibers. Its complete type says, for every pair and every \(k\), that there are at least \(k\) points between those two coordinates. A realizing tuple in \(M\) therefore lies in \(n\) distinct finite-distance classes. Hence \(M\) has infinitely many such classes and belongs to \(\mathcal I\). So \(\mathcal I\) is exactly one isotypy class.

The class \(\mathcal I\) is Borel. For fixed coordinates, \(xE_Ly\) is Borel because it is the countable union over \(m\) of the condition that at most \(m\) points lie strictly between them. Saying that every \(E_L\)-class is \(\mathbb Z\) can be written as the Borel condition that every point has an immediate predecessor and immediate successor in its \(E_L\)-class; the finite-distance definition already ensures every two points in a class are only finitely many successor steps apart. Saying that there are infinitely many classes is the countable conjunction, over \(n\), that there are \(n\) pairwise \(E_L\)-inequivalent points. All these conditions are isomorphism invariant.

Finally fix a bijection \(\beta:\mathbb N\to\mathbb N\times\mathbb Z\). For a coded countable linear order \(A\), let \(F(A)\) be the pullback via \(\beta\) of the lexicographic order on \(A\times\mathbb Z\). Each output comparison depends on one input comparison and fixed integer data, so \(F\) is continuous. Its image lies in \(\mathcal I\), and
\[
A\cong B\iff F(A)\cong F(B),
\]
where the reverse implication is Gvozdevsky's quotient lemma. Isomorphism of all countable linear orders is Borel complete, so \(\cong\!\upharpoonright\mathcal I\) is Borel complete.

## Verification
The source theorem was checked directly in Gvozdevsky's paper: Corollary 3.4 gives isotypy of \(A\times\mathbb Z\) for arbitrary infinite \(A,B\), and Lemma 3.6 recovers \(A\) from the finite-distance quotient. The bundled verifier replays the coding reduction on all labeled finite linear orders through size seven, checking that the zero-slice decodes the input relation and that relabeling is transported functorially. It returns `VERIFY_OK 7184502 exact assertions`.

## Relationship to prior work
Gvozdevsky's 2023/2024 paper supplies the isotypy and quotient-rigidity ingredients but does not discuss Borel reducibility or identify the resulting entire isotypy class as a Borel complete invariant class. Friedman and Stanley introduced Borel reducibility and established maximal complexity for countable linear orders. Rast later proved a broad dichotomy for isomorphism on all countable models of a complete theory of linear orders: such a theory is either \(\aleph_0\)-categorical or Borel complete. That result concerns an elementary class, which is generally much larger than one isotypy class. The present statement sharpens the location of the complexity to a single realized-type spectrum.

Targeted exact-phrase web searches for “isotypy class” with “Borel complete,” broader searches for isotypic/Borel complexity, a semantic published-finding corpus search, and both cumulative owned ledgers found the ingredients and adjacent complete-theory results but no equivalent single-isotypy-class theorem.

## Limitations
The result is specific to countable linear orders and exploits the lexicographic \(\mathbb Z\)-fiber construction. It does not classify all isotypy classes of linear orders or assert that every nontrivial isotypy class is Borel complete. The originality claim is for the descriptive-set-theoretic synthesis and exact identification of this one class, not for Gvozdevsky's construction or Friedman--Stanley completeness separately. Because the deduction is short once those ingredients are juxtaposed, uncatalogued folklore remains a residual risk.

## References
1. Pavel Gvozdevsky, “On countable isotypic structures,” arXiv:2308.10812, first submitted 21 August 2023; journal of Groups, Complexity, Cryptology 16(1), 2024. Corollary 3.4 and Lemma 3.6.
2. Harvey Friedman and Lee Stanley, “A Borel reductibility theory for classes of countable structures,” Journal of Symbolic Logic 54(3), 1989, 894–914, DOI:10.2307/2274750.
3. Richard Rast, “The Borel Complexity of Isomorphism for Complete Theories of Linear Orders With Unary Predicates,” Archive for Mathematical Logic 55, 2016; arXiv:1504.03037.
