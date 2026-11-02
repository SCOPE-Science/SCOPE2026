# Materializer sublattices characterize finite Gödel algebras

## Finding

For a finite Heyting algebra \(H\) and an antecedent \(a\in H\), its **materializer** is
\[
M_H(a)=\{b\in H:a\to b=\neg a\vee b\}.
\]
The following statements hold, including for the one-element algebra.

**Individual-antecedent criterion.** Represent \(H\) as the downset Heyting algebra \(J(P)\) of a finite poset \(P\), and write \(I\subseteq P\) for the downset representing \(a\). Then \(M_H(a)\) is closed under the ambient join if and only if, for every \(p\in P\), the downset \(I\cap\downarrow p\) is either empty or a principal downset. Closure under the ambient meet and membership of both endpoints hold without this condition. Consequently this criterion characterizes exactly when \(M_H(a)\) is a bounded sublattice of \(H\).

**Global characterization.** The following conditions on a finite Heyting algebra are equivalent:

1. \(M_H(a)\) is a bounded sublattice of \(H\) for every \(a\in H\).
2. In the dual poset \(P\), every principal downset \(\downarrow p\) is a chain (\(P\) is a finite rooted forest).
3. \(H\) satisfies the prelinearity equation \((a\to b)\vee(b\to a)=\top\) for all \(a,b\in H\), so \(H\) is a finite Gödel algebra.

There is also an explicit closure operator recovering every materializer. Put \(D_I(p)=I\cap\downarrow p\) and
\[
c_I(J)=J\cup\downarrow\big\{p\in P:D_I(p)\ne\varnothing\ \text{and}\ D_I(p)\subseteq J\big\}
\qquad(J\in J(P)).
\]
Then \(c_I\) is extensive, monotone, idempotent, and its fixed points are exactly \(M_H(a)\). Thus, even when ambient joins are not preserved, every materializer is a lattice in its inherited order: its meet is intersection and its internal join is \(c_I(J\cup K)\).

These internal lattices need not be distributive. A four-point poset with three incomparable minimal points below one maximum has a nine-element downset algebra with a seven-element **nondistributive** materializer.

## Assumptions and scope

All posets, downsets and algebras in the theorem are finite. A downset is a subset closed downwards. \(J(P)\) consists of all downsets, including the empty and full downsets; its meet and join are intersection and union. For \(p\in P\), \(\downarrow p=\{q\in P:q\le p\}\). A principal downset is one of this form. The empty downset is allowed separately. A bounded sublattice means a subset containing the original bottom and top and closed under the original binary meet and join. This is **not** a claim of closure under Heyting implication.

Finite Birkhoff representation identifies the underlying bounded distributive lattice of each finite Heyting algebra with some \(J(P)\), and this identification preserves the unique finite Heyting implication. No assumption of connectedness, a unique least element, or a nontrivial algebra is needed.

## Proof

**1. Implication as a downset condition.** For downsets \(I,J\subseteq P\), define
\[
I\Rightarrow J=\{p\in P:I\cap\downarrow p\subseteq J\}.
\]
This is a downset. An arbitrary downset \(K\) satisfies \(K\cap I\subseteq J\) if and only if \(K\subseteq I\Rightarrow J\), proving that \(\Rightarrow\) is precisely the Heyting implication. In particular,
\[
\neg I=\{p\in P:D_I(p)=\varnothing\}.
\]
The inclusion \(\neg I\cup J\subseteq I\Rightarrow J\) always holds, because \(J\) is a downset. Therefore equality holds precisely when
\[
\forall p\in P:\quad
0<|D_I(p)|\ \land\ D_I(p)\subseteq J\quad\Longrightarrow\quad p\in J.\tag{1}
\]
Equation (1) is the exact materializer condition, with no implicit genericity assumptions.

**2. Canonical closure.** Let \(A_I(J)=\{p:D_I(p)\ne\varnothing,\ D_I(p)\subseteq J\}\), and set \(c_I(J)=J\cup\downarrow A_I(J)\). This is a downset and is extensive and monotone. Crucially,
\[
I\cap c_I(J)=I\cap J.\tag{2}
\]
Indeed, if \(q\in I\cap\downarrow A_I(J)\), then \(q\le p\) for some \(p\in A_I(J)\), so \(q\in D_I(p)\subseteq J\). As \(D_I(p)\) depends only on the intersection with \(I\), identity (2) implies \(A_I(c_I(J))=A_I(J)\), proving idempotence. It also implies that \(c_I(J)\) satisfies (1): whenever \(D_I(p)\subseteq c_I(J)\) and is nonempty, it already lies in \(J\), hence \(p\in A_I(J)\subseteq c_I(J)\). Any materializer containing \(J\) must contain every point of \(A_I(J)\), hence all of \(c_I(J)\). Thus \(c_I(J)\) is the least materializer above \(J\). In particular its fixed points are exactly the materializers. They are intersection-closed, contain \(\varnothing,P\), and have the internal joins asserted above.

**3. Exact ambient-join criterion.** Suppose for every \(p\) the set \(D_I(p)\) is empty or principal. Let \(J,K\) satisfy (1), and assume \(\varnothing\ne D_I(p)\subseteq J\cup K\). Write \(D_I(p)=\downarrow q\). As \(q\in J\cup K\), either \(D_I(p)\subseteq J\) or \(D_I(p)\subseteq K\). Equation (1) then gives \(p\in J\cup K\), proving ambient-join closure.

Conversely suppose \(D=D_I(p)\) has distinct maximal elements \(u,v\). The sets \(C_1=D\setminus\{u\}\) and \(C_2=\downarrow u\) are downsets in \(P\), and both are proper subsets of \(D\), while \(C_1\cup C_2=D\). Set \(J=c_I(C_1)\), \(K=c_I(C_2)\). By (2), \(I\cap J=C_1\) and \(I\cap K=C_2\). Thus neither \(J\) nor \(K\) contains \(p\): were \(p\in J\), its downset would force \(D\subseteq J\cap I=C_1\), a contradiction; likewise for \(K\). But \(D\subseteq J\cup K\), so (1) fails for their union. Hence ambient-join closure is impossible. Every nonempty finite downset has a unique maximal element exactly when it is principal, proving the criterion.

**4. All antecedents and prelinearity.** If every principal downset of \(P\) is a chain, every \(I\cap\downarrow p\) is empty or principal, so the individual criterion applies to every \(I\). Conversely, if some \(\downarrow p\) contains incomparable \(u,v\), choose \(I=\downarrow u\cup\downarrow v\). As \(u,v\le p\) are incomparable, \(p\notin I\) and \(D_I(p)=I\) has at least two maximal elements. Therefore this materializer is not an ambient sublattice.

Finally, if \(\downarrow p\) is a chain, the two downsets \(I\cap\downarrow p\) and \(J\cap\downarrow p\) are comparable by inclusion, so \(p\in(I\Rightarrow J)\cup(J\Rightarrow I)\). This establishes prelinearity when all principal downsets are chains. If instead \(u,v\le p\) are incomparable, choose \(I=\downarrow u\), \(J=\downarrow v\): at \(p\), neither \(D_I(p)\subseteq J\) nor \(D_J(p)\subseteq I\), so prelinearity fails. This proves all equivalences.

**5. Nondistributive materializer.** Let \(P=\{u,v,w,t\}\) with its only nonreflexive order relations \(u<t\), \(v<t\), \(w<t\), and put \(I=\{u,v\}\). The downsets are the eight subsets of \(\{u,v,w\}\) and \(P\). Formula (1) shows that
\[
M(I)=\{\varnothing,\{u\},\{v\},\{w\},\{u,w\},\{v,w\},P\}.
\]
Inside this seven-element lattice, \(\{u\}\vee_{M}\{v\}=P\), whereas all intersections of \(\{w\}\) with \(\{u\}\) and \(\{v\}\) are empty. Thus
\[
\{w\}\cap(\{u\}\vee_M\{v\})=\{w\}\ne\varnothing
=(\{w\}\cap\{u\})\vee_M(\{w\}\cap\{v\}).
\]
This proves nondistributivity and completes the theorem.

## Verification

Two stand-alone standard-Python programs are supplied. `verify_materializers.py` independently computes finite downset implication, closure, fixed points, ambient-join preservation, and the prelinearity/forest correspondence for every naturally labeled poset with at most six points (there are \(1,2,7,40,357,4824\) such posets by size). Every finite poset of those sizes admits at least one natural labeling, so this is exhaustive up to isomorphism at each tested size. `verify_example.py` uses a different representation, enumerating downsets as frozensets, to check the nine-element algebra and its nondistributive seven-element materializer. Both scripts are finite sanity checks; the general theorem is established in the proof above.

Reproduce with a standard Python 3 interpreter by running `python verify_materializers.py` and `python verify_example.py` from the directory containing these files. No packages, external data, internet connection, or machine-specific paths are needed.

## Relationship to prior work

Bumpus and Kocsis introduced and studied the materializer \(M_H(a)\) in *Degree of Satisfiability in Heyting Algebras* (arXiv:2110.11515, original public version 21 October 2021). They note that materializers contain the endpoints and are meet-closed, and explicitly identify their further algebraic structure as worthy of investigation. This result concerns ambient **joins**, exact fixed-point closure, and the lattice structure of materializers, none of which is asserted in the inspected materializer discussion of that paper.

The classical equivalence between finite Gödel algebras and finite forest posets is not claimed as new. Flaminio, Godo, Menchón and Rodriguez discuss this duality in *Algebras and relational frames for Gödel modal logic and some of its extensions* (arXiv:2110.02528). The contribution here is to relate that pre-existing prelinearity/forest criterion to a distinct family of materializer sublattice tests, including an exact antecedent-by-antecedent condition and nondistributive fixed-point phenomenon.

## Limitations

The theorem treats **finite** Heyting algebras. Infinite Esakia representations and topological or frame-theoretic extensions are not established. Closure under ambient meet and join is weaker than closure under implication; the theorem does not claim that the materializer is necessarily a Heyting subalgebra. The numerical example does not assert a minimum size among all finite Heyting algebras for the occurrence of a nondistributive internal materializer lattice. The literature comparison is limited to the identified and inspected sources; independent historical-priority review remains desirable.

## References

1. B. M. Bumpus and Z. A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, arXiv:2110.11515, first submitted 2021-10-21; later *Journal of Symbolic Logic* 90 (2025), 533–551. https://arxiv.org/abs/2110.11515
2. T. Flaminio, L. Godo, P. Menchón and R. O. Rodriguez, *Algebras and relational frames for Gödel modal logic and some of its extensions*, arXiv:2110.02528, first submitted 2021-10-06. https://arxiv.org/abs/2110.02528
3. S. Aguzzoli, B. Gerla and V. Marra, *Gödel Algebras Free over Finite Distributive Lattices*, *Annals of Pure and Applied Logic* 155 (2008), 183–193, DOI:10.1016/j.apal.2008.04.003 (background on the established forest duality).
