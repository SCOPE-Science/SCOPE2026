# Sharp finite-spectrum cutoff for Bernays–Schönfinkel sentences on equivalence relations

## Finding
Let \(k\ge 0\) and \(\ell\ge2\) be integers. Consider first-order sentences
\[
\Phi=\exists x_1\cdots\exists x_k\;\forall y_1\cdots\forall y_\ell\;\psi,
\]
where \(\psi\) is quantifier-free in equality and one binary symbol \(E\). Interpret \(E\) **only on nonempty finite equivalence structures**. Put
\[
B_E(k,\ell)=k\ell+(\ell-1)^2.
\]
If \(\Phi\) has a finite equivalence-structure model of size strictly greater than \(B_E(k,\ell)\), then \(\Phi\) has an equivalence-structure model of **every** size \(n\ge k+\ell\). Consequently, every nonempty finite relative spectrum has maximum at most \(B_E(k,\ell)\). For every allowed pair \((k,\ell)\), the bound is sharp: some such sentence has a finite relative spectrum whose maximum is exactly \(B_E(k,\ell)\).

## Assumptions and scope
The universe is nonempty and finite; \(E\) is reflexive, symmetric, and transitive, and equality has its usual meaning. The equivalence-relation laws are **semantic restrictions**, not additional axioms promised within the displayed quantifier prefix. The spectrum records cardinalities of models *within that semantic class*, not models over arbitrary binary relations. The matrix can contain Boolean combinations of atomic formulas in the variables displayed. The formula may use fewer than all its quantified variables. The construction allows \(k=0\) but assumes \(\ell\ge2\).

## Proof
**1. A pumping lemma for pointed equivalence structures.** Fix a model \(M\) and a witnessing tuple \(\bar a=(a_1,\dots,a_k)\). Let \(W\) be the set of its distinct values, \(t=|W|\le k\); call an \(E\)-class *marked* if it meets \(W\), and *free* otherwise. Let \(\mathcal D_\ell(M,\bar a)\) be the set of all complete atomic equality-and-\(E\) diagrams of assignments to \(\bar a\) and \(\ell\) universally quantified variables. If an extension \(M'\) of the same pointed structure has
\[
\mathcal D_\ell(M',\bar a)\subseteq\mathcal D_\ell(M,\bar a),
\]
then \(M'\models\Phi\), since the matrix is a Boolean combination of precisely those atoms.

There are two ways to obtain such a one-vertex extension.

(i) If some \(E\)-class \(C\) contains at least \(\ell\) elements **outside** \(W\), add one new element \(z\) equivalent exactly to the elements of \(C\). Given an assignment to the \(\ell\) universal variables in the extension, remap **all** distinct nonwitness values that occur in \(C\), including any occurrence of \(z\), injectively into \(\ell\) pre-existing nonwitness elements of \(C\). Keep witnesses and all values in other classes fixed. The complete equality-and-\(E\) diagram is preserved, so no new \(\ell\)-type appears.

(ii) If there are at least \(\ell\) distinct free \(E\)-classes, insert one new singleton free class. For any assignment to \(\ell\) universal variables, let \(r\) be the number of old free classes represented, and let \(q\) be the number of new singleton free classes represented (for a single insertion, \(q\) is either zero or one). Then \(r+q\le\ell\). Among \(\ell\) preselected old free classes, at least \(q\) are not among those \(r\) classes. Map the new singleton-class values to representatives of \(q\) different unused old free classes, fixing all other variable values. This again preserves the complete diagram. Repeating (i) or (ii) yields arbitrarily many larger pointed models; the relevant supply of old nonwitness elements or free classes is never depleted.

**2. The sharp bound.** If (i) is unavailable, every marked class contains at most \(\ell-1\) nonwitness vertices, and every free class also contains at most \(\ell-1\) vertices. There are at most \(t\le k\) marked classes. If (ii) is unavailable, there are at most \(\ell-1\) free classes. Consequently
\[
|M|\le |W|+t(\ell-1)+(\ell-1)^2
\le k\ell+(\ell-1)^2=B_E(k,\ell).
\]
Thus a model larger than the bound has at least one pumping mechanism.

**3. Every sufficiently large cardinality occurs.** Shrinking a pointed model to any induced substructure containing \(W\) preserves the universal matrix, and every restriction of an equivalence relation is still an equivalence relation. Starting from a model larger than \(B_E(k,\ell)\), pump by one vertex indefinitely as in step 1. If a requested order \(n\ge k+\ell\) is below the size of the original model, retain \(W\) and any other \(n-|W|\) elements. If it is above, pump to exactly that order. Hence **every** such \(n\) is in the relative spectrum; the spectrum cannot be finite.

**4. Realizing equality.** We construct a sentence in the stipulated prefix whose models have the required maximum. Require the \(k\) witnesses \(x_i\) to lie in pairwise different \(E\)-classes (vacuously if \(k=0\)). Put \(F(z)=\bigwedge_{i=1}^{k}\neg E(z,x_i)\), meaning that \(z\) belongs to a free class. In the quantifier-free matrix on \(y_1,\ldots,y_\ell\), forbid these three configurations:

(A) \(\ell\) pairwise distinct **nonwitness** values lying in the same marked class \([x_i]_E\), for any \(i\);

(B) \(\ell\) pairwise distinct values satisfying \(F\) and all \(E\)-equivalent to one another;

(C) \(\ell\) values satisfying \(F\) and pairwise \(E\)-inequivalent.

Each prohibition involves only the displayed \(\ell\) universal variables and the named existential witnesses and so is a quantifier-free clause. For example, (A) is the negation, for every \(i\), of
\[
\left(\bigwedge_{p<q}y_p\ne y_q\right)\wedge
\bigwedge_{p=1}^{\ell}\left(E(y_p,x_i)\wedge\bigwedge_{j=1}^k y_p\ne x_j\right).
\]
The models therefore have at most \(\ell-1\) nonwitness vertices per marked class, at most \(\ell-1\) elements per free class, and at most \(\ell-1\) free classes. Exactly \(k\ell+(\ell-1)^2\) vertices are attained: take \(k\) classes each of size \(\ell\), each with one designated witness, and \(\ell-1\) additional classes each of size \(\ell-1\). The model is nonempty because \(\ell\ge2\), and it satisfies all three prohibitions. This proves sharpness.

## Verification
The symbolic proof is independent of enumeration. A standalone Python script `artifacts/verify_equivalence_cutoff.py` enumerates finite equivalence-relation partition shapes and all witness tuples for parameter choices \((k,\ell)=(0,2),(0,3),(1,2),(1,3),(2,2)\). For each pointed model above the proposed bound in the tested range, it checks that an indicated pumping extension creates **no new equality-and-\(E\) atomic diagram** for \(\ell\) universally quantified variables. It also checks the extremal prohibition formula and explicit saturating examples. Its recorded output ends `VERIFY_OK pointed_cases=1655`. This finite test is not a proof for unbounded \(k\), \(\ell\), or model size.

## Relationship to prior work
The classical Bernays–Schönfinkel–Ramsey framework and Sankaran–Chakraborty's semantic treatment imply finite/cofinite behavior for large families of relational spectra, but do not by themselves provide the exact parameter-dependent endpoint on equivalence structures. Pikhurko and Verbitsky's graph-spectrum Ramsey argument yields a general simple-graph threshold through adjacency profiles and homogeneous sets, whereas equivalence structures have only *class-size* and *class-count* pumping obstructions. Here both obstructions are necessary and can be saturated simultaneously. The resulting sharp polynomial expression is a different, structure-restricted optimal endpoint; it is not implied numerically or via the extremizers of the unrestricted graph statement.

A published all-graph sharp endpoint \(k+(R(\ell,\ell)-1)2^k\), and results on bounded-variable definability of complete multipartite graphs, were also compared at the level of their full claims and proofs. The graph endpoint does not force the smaller equivalence-structure bound; logical width does not determine the finite-spectrum endpoint for this prenex fragment. Targeted database and literature searches found no statement of the specific sharp equivalence-structure formula, but this is **not** a proof of historical priority.

## Limitations
Only one equivalence relation and equality are present; arbitrary relational structures, multiple equivalence relations, and arbitrary first-order quantifier prefixes are not covered. The result determines the **largest possible endpoint of a finite relative spectrum**, not all possible spectra below it. The proof assumes semantic restriction to equivalence structures rather than syntactically axiomatizing equivalence within the prefix. Priority uncertainty remains: the pumping argument is elementary and an equivalent observation could appear in unindexed lecture notes, exercises, or folklore. Independent validation has not been performed.

## References
1. A. Sankaran and S. Chakraborty, *On Semantic Generalizations of the Bernays-Schönfinkel-Ramsey Class with Finite or Co-finite Spectra*, arXiv:1002.4334, first posted 2010-02-23; https://arxiv.org/abs/1002.4334.
2. O. Pikhurko and O. Verbitsky, *Logical Complexity of Graphs: A Survey*, arXiv:1003.4865, first posted 2010-03-25; see Section 7.3; https://arxiv.org/abs/1003.4865.
3. E. Kieroński and A. Kuusisto, *Uniform One-Dimensional Fragments with One Equivalence Relation*, CSL 2015, LIPIcs 41, 597–615; DOI:10.4230/LIPIcs.CSL.2015.597.
4. I. Pratt-Hartmann, *Logics with Counting and Equivalence*, CSL-LICS 2014; DOI:10.1145/2603088.2603117.
