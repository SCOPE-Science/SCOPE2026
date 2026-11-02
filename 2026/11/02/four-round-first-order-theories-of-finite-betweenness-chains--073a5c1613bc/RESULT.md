# Four-round first-order theories of finite betweenness chains

## Finding
For each integer \(n\ge1\), let \(\mathcal B_n\) have domain \(\{1,\ldots,n\}\), with equality and one strict ternary relation
\[
B(x,y,z)\quad\Longleftrightarrow\quad (x<y<z)\ \lor\ (z<y<x).
\]
No order relation, successor relation, endpoint constants, or unary labels belong to the language. Write \(\equiv_4\) for agreement on all first-order sentences of quantifier rank at most four. Then, for all positive integers \(m,n\),
\[
\boxed{\mathcal B_m\equiv_4\mathcal B_n\quad\Longleftrightarrow\quad (m=n<14)\ \lor\ (m,n\ge14).}
\]
The family therefore has exactly fourteen rank-four equivalence classes. Every member has a rank-four-equivalent member with at most fourteen points, and no smaller universal representative bound is possible. In particular, \(\mathcal B_{14}\equiv_4\mathcal B_{15}\), whereas the corresponding *oriented* finite linear orders of sizes fourteen and fifteen are distinguishable at rank four.

## Assumptions and scope
The relation is strict: repeated entries never satisfy \(B\). Domains are nonempty finite chains; their linear order is used only to define \(B\), and is not accessible to formulas. First-order quantifier rank is maximum nesting depth; quantifier alternations and repeated choices are unrestricted. The result is restricted to rank four, not a claim about all ranks or general trees.

## Proof
**Exact finite-type lemma.** For a tuple \(\bar a\) of \(j\le4\) selected elements, let \(A_j(\bar a)\) be its complete atomic diagram, recording every equality and every instance of the ternary predicate on tuple positions. Define complete four-round extension types backward by
\[
T_4^n(\bar a)=A_4(\bar a),\qquad
T_j^n(\bar a)=\bigl(A_j(\bar a),\ \{T_{j+1}^n(\bar a,b):b\in\mathcal B_n\}\bigr),\quad j=3,2,1,0.
\]
The braces denote a **set**, not a multiset: an existential move sees whether a response type occurs, not how often. Repeated vertices are permitted, including a move that repeats an earlier choice. Equality of these recursively defined types across two structures is equivalent to a winning strategy for Duplicator in the remaining \(4-j\) Ehrenfeucht–Fraïssé rounds, provided the current atomic diagrams match. This is proved by backward induction. At \(j=4\) it is precisely the terminal partial-isomorphism condition. At a smaller \(j\), Duplicator must answer every next Spoiler choice in either structure with a child of the same type; equality of the two sets of child types is necessary and sufficient by the induction hypothesis. At \(j=0\), equality is therefore exactly \(\equiv_4\).

**Finite boundary, without approximation.** Both standalone programs enumerate all \(n^4\) ordered four-tuples (including repeated entries) and intern each exact atomic diagram. They then compute the above exact child-type sets for tuples of lengths three, two, one, and zero. Signatures use lossless equality and betweenness bit patterns plus sorted integer sets, not hash equality. The files `python_output.txt` and `cpp_output.txt` record complete root-type classifications for \(1\le n\le17\). Both programs produce fourteen root types: sizes \(1,\ldots,13\) have pairwise different types, size fourteen has a new type, and sizes fifteen, sixteen, and seventeen have that same last type. In particular the exhaustive recurrence proves
\[
\mathcal B_{14}\equiv_4\mathcal B_{15},
\]
and distinguishes every two different sizes up to fourteen. As an additional inspectable certificate for the nontrivial equality, the one-point type sets for fourteen and fifteen points are equal. The ordered one-point type labels from the independently compiled verifier are, respectively,

`16,20,24,27,30,32,34,34,32,30,27,24,20,16`

and

`16,20,24,27,30,32,34,34,34,32,30,27,24,20,16`.

The extra occurrence of label `34` is immaterial because the type recurrence uses sets. The labels are local exact-signature identifiers, not a mathematical numbering of first-order formulas.

**Infinite tail.** A standard theorem for finite linear orders, recalled explicitly by Mwesigye and Truss (2010, pp. 389–390), says that at quantifier rank \(q\), the pure linear orders of different positive sizes at least \(2^q-1\) are equivalent. With \(q=4\), all oriented orders of sizes at least fifteen are four-equivalent. Strict betweenness is definable **without additional quantifiers** from order, by the displayed definition. Forgetting order therefore preserves four-equivalence: all \(\mathcal B_n\) for \(n\ge15\) are four-equivalent. Transitivity and the finite verified equivalence \(\mathcal B_{14}\equiv_4\mathcal B_{15}\) extend the class to all \(n\ge14\). Combined with the exact finite distinctions, this proves both directions and the optimal representative bound.

## Verification
Reproduce using `python3 check_types.py` and `g++ -std=c++17 -O2 check_types.cpp -o check_types && ./check_types`; their outputs are embedded separately. The implementations use distinct tuple indexing and atomic-type encodings and independently implement the complete backward recurrence. Both confirm, for all sizes one through seventeen, the class-index sequence \(1,2,\ldots,13,14,14,14,14\). For the infinite tail only the cited linear-order theorem plus quantifier-free reduct and transitivity is used; finite results are not extrapolated. The recurrence lemma is mathematical, and the executable programs are finite exhaustive certificates of its specified boundary instances.

## Relationship to prior work
Mwesigye and Truss classify finite **coloured ordered** structures by Ehrenfeucht–Fraïssé games and explicitly recall the sharp \(2^q-1\) stabilization of uncoloured linear orders (2010, pp. 389–390). That sharp oriented threshold does **not** imply the new smaller one for the ternary betweenness reduct: at rank four the oriented structures of sizes fourteen and fifteen are distinguished, whereas the betweenness reducts coincide. Courcelle (2020, pp. 1–2) treats axiomatization and reconstruction of the betweenness relation of linear and partial orders, including order reconstruction up to reversal; he does not give a finite rank-four spectrum. Published related classifications of directed paths and one-marked coloured linear orders concern successor or full order signatures and do not imply the ternary reduct's fourteen-point boundary. No checked source established this exact fourteen-class statement.

## Limitations
The classification depends on the strict ternary betweenness relation, not binary successor, total order, or non-strict betweenness. It does not classify other quantifier ranks, arbitrary paths with nongeodesic ternary predicates, partial-order betweenness, or infinite structures. The proof of the fourteen-versus-fifteen boundary has an executable exhaustive certificate rather than a short closed-form Duplicator strategy. Literature searches and primary-document reading cannot exclude an unindexed earlier observation, and no independent mathematical audit is claimed.

## References
1. F. Mwesigye and J. K. Truss, “Classification of Finite Coloured Linear Orderings,” *Order* 28 (2011), 387–397. First public online: 2010-09-07. DOI: 10.1007/s11083-010-9178-9. Full text: https://ir.must.ac.ug/bitstreams/ce8f9fc1-8064-4e56-b7ae-a30dd6b401c0/download.
2. B. Courcelle, “Betweenness of partial orders,” arXiv:2004.09777v1, 2020-04-21; *RAIRO Theoretical Informatics and Applications* 54 (2020), article 7. https://arxiv.org/abs/2004.09777.
3. “Exact quantifier-rank threshold for finite directed paths,” published published-finding corpus record 2026/10/4/SCOPE-exact-quantifier-rank-threshold-for-finite-directed-paths--75a6b05e7112 (distinct successor-only signature).
4. “Exact quantifier-rank profiles for finite one-red linear orders,” published published-finding corpus record 2026/10/4/SCOPE-exact-quantifier-rank-profiles-for-finite-one-red-linear-orders--eec9053b6af5 (distinct full-order signature).
