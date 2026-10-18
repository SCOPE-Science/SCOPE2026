# Complete two-variable theories of colored equivalence relations and sharp induced cores

## Finding

Fix an integer \(r\geq0\). Consider nonempty, possibly infinite first-order structures in the signature consisting of equality, a distinguished equivalence relation \(E\), and exactly \(r\) unary predicates, with no other nonlogical symbols. Formulas of \(\mathrm{FO}^{2}\) may reuse the variables \(x,y\) and use unrestricted Boolean connectives and ordinary quantifiers, but no counting quantifiers.

Put \(q=2^r\) and let \(\mathcal C\) be the \(q\) complete unary colors. For an \(E\)-class \(K\), define its local vector
\[
 t_K=(\min\{2,|K\cap C|\})_{C\in\mathcal C}
 \in\mathcal T:=\{0,1,2\}^{\mathcal C}\setminus\{\boldsymbol0\}.
\]
For \(t\in\mathcal T\), write \(N_t(A)\) for the number of \(E\)-classes in structure \(A\) with vector \(t\), possibly infinite, and set \(h_A(t)=\min\{2,N_t(A)\}\).

**Theorem.** Two such nonempty structures, finite or infinite, satisfy exactly the same \(\mathrm{FO}^{2}\) sentences if and only if their functions \(h_A:\mathcal T\to\{0,1,2\}\) agree. All functions \(h\) except the identically zero function occur. Consequently the exact number of complete \(\mathrm{FO}^{2}\) sentence theories is
\[
 \boxed{3^{3^{2^r}-1}-1}.
\]
Moreover, every structure \(A\) has an *induced finite substructure* \(B\subseteq A\) with the same \(\mathrm{FO}^{2}\) sentence theory and
\[
 \boxed{|B|\leq 2q3^q=2^{r+1}3^{2^r}}.
\]
This is the least possible uniform bound: for each \(r\) a single satisfiable \(\mathrm{FO}^{2}\) sentence forces any model to have at least \(2q3^q\) elements. In particular, for \(r=0\) there are exactly \(8\) theories and the sharp bound is \(6\); for \(r=1\) there are \(6560\) theories and the sharp bound is \(36\).

## Assumptions and scope

The carrier is nonempty; \(E\) is reflexive, symmetric, and transitive on the carrier. The unary predicates are independent and may be empty or full, so the \(q\) complete unary colors are the Boolean truth assignments to them. These are *ordinary*, equality-using two-variable first-order formulas, with no additional binary predicates, constants, functions, generalized or counting quantifiers. The classification is for complete **sentence** theories, not pointed types or isomorphism types. A value \(2\) in either truncation means *at least two*, not exactly two.

## Proof

**1. Local vectors are definable using just two variables.** Fix a complete unary color formula \(C(x)\), a conjunction choosing each unary predicate positively or negatively (for \(r=0\), use \(x=x\)). Define
\[
 U_C^1(x):=\exists y\,[E(x,y)\land C(y)],
\]
\[
 U_C^2(x):=\exists y\,[E(x,y)\land C(y)\land
    \exists x\,(E(y,x)\land C(x)\land x\ne y)].
\]
The innermost occurrence of \(x\) is bound by its own quantifier: its shadowing is intentional. Since \(E\) is an equivalence relation, \(U_C^1\) and \(U_C^2\) say that the class containing the free element has at least one and at least two members of color \(C\), respectively. Let \(L_t(x)\) be the conjunction over all colors of \(\neg U_C^1(x)\) for \(t_C=0\), \(U_C^1(x)\land\neg U_C^2(x)\) for \(t_C=1\), and \(U_C^2(x)\) for \(t_C=2\). Then \(L_t(x)\) defines exactly the members of classes with local vector \(t\). Replacing the free variable \(x\) by \(y\) with capture-avoiding variable renaming gives \(L_t(y)\), still in the two-variable syntax.

For every \(t\), the sentences \(\exists x L_t(x)\) and
\[
 \exists x\exists y\,[\neg E(x,y)\land L_t(x)\land L_t(y)]
\]
express, respectively, that at least one and at least two different \(E\)-classes of type \(t\) exist. Nested quantifiers internal to each \(L_t\) shadow only their own variables. Thus disagreement of global profiles entails disagreement on an explicit two-variable sentence.

**2. Equal profiles imply equivalence in every quantifier rank.** Consider the usual two-pebble Ehrenfeucht–Fraïssé game on structures with equal profiles. Duplicator maintains a partial isomorphism of the pebbled points, together with the stronger invariant that the \(E\)-classes occupied by corresponding pebbles have identical local vectors. A lone newly selected point of any color can be matched because a nonzero global profile contains a class with that color. With one other pebble fixed, a new point in the *same* class can be matched using the local vector: a specified different point of the stationary color exists exactly when that color count is at least two; a point of another color exists exactly when its count is at least one. A new point in a *different* class of type \(t\) can be matched because either \(t\) differs from the stationary class type and \(h(t)\ge1\), or it equals that type and \(h(t)=2\). In all cases equality, \(E\), every unary predicate, and both pebbled class vectors remain matched. This back-and-forth strategy works for arbitrarily many rounds even if either structure is infinite. The two-variable game characterization consequently gives identical truth values for all \(\mathrm{FO}^{2}\) sentences.

**3. Every profile occurs, and each has a finite induced core.** In each class type \(t\) present in \(A\), select exactly \(h_A(t)\) actual classes. Within each selected class and color \(C\), retain exactly \(t_C\) actual elements (zero, one, or two). The resulting union \(B\) is a nonempty induced substructure, has exactly the same profile, and therefore the same \(\mathrm{FO}^{2}\) theory by step 2. Conversely, for any nonzero function \(h:\mathcal T\to\{0,1,2\}\), take \(h(t)\) disjoint classes each containing \(t_C\) points of each color \(C\). This finite structure realizes \(h\). There are \(|\mathcal T|=3^q-1\) local vectors, so the number of nonzero functions \(h\) is \(3^{3^q-1}-1\).

**4. The induced-core bound is exact.** For any \(A\), step 3 yields
\[
 |B|=\sum_{t\in\mathcal T}h_A(t)\sum_Ct_C
 \leq 2\sum_{t\in\{0,1,2\}^q}\sum_Ct_C
 = 2q3^q.
\]
The last equality follows by fixing a coordinate, summing its values \(0+1+2=3\), and choosing the remaining \(q-1\) coordinates in \(3^{q-1}\) ways. For sharpness, conjoin, over every \(t\in\mathcal T\), the two-class existence sentence from step 1. This is a finite \(\mathrm{FO}^{2}\) sentence for each fixed \(r\); any model has at least two distinct \(E\)-classes of each local type, and each such class has at least \(\sum_Ct_C\) elements, so every model has at least \(2q3^q\) elements. The canonical construction meets that lower bound.

## Verification

The standalone Python 3 verifier `verify.py` independently enumerates finite equivalence relations as set partitions, all unary colorings, predicted double-truncation profiles, and finite-rank two-variable semantic signatures obtained by repeatedly refining states with zero, one, or two assigned variables. The resulting signatures and profiles coincide in both tested universes: one color, sizes at most six (278 structures, eight profiles), and two colors, sizes at most five (1954 structures, 71 observed profiles). The rank-six computation and direct combinatorial counts also reproduce the bounds \(6\) and \(36\). Run `python3 verify.py`, with no third-party dependencies; expected final line: `COLORED_EQUIVALENCE_FO2_VERIFY_OK`. These finite tests are checks of the proof, not evidence by themselves for statements about all arities or infinite structures.

## Relationship to prior work

Fiuk's 2026 paper studies a much more general class of equality-free first-order fragments with an added equivalence predicate and proves finite model property and complexity results; its class-label machinery motivates the search for exact invariants in a very small equality-using fragment. Kieroński and Otto establish finite/small-model results for the general two-variable fragment with one equivalence, allowing other relation symbols. Pratt-Hartmann studies the richer two-variable language with counting and equivalence. Those results establish broad decidability or size bounds but the inspected statements do not provide this exact monadic-only sentence-theory census and the sharp *induced-substructure* bound. The two-pebble game principle and the bounded-observation phenomenon are classical, and are not claimed as new. A previous exact classification under a different algebraic or model-theoretic formulation could cover the formula; this historical-priority risk remains.

## Limitations

The classification fails if one adds unrestricted counting quantifiers, a second binary relation, or allows more than two distinct first-order variable symbols: such languages may distinguish multiplicities above two. The bound is uniform over *all* formulas in the stated fixed finite signature, but grows doubly exponentially in the number of unary predicates. No priority claim beyond the literature actually inspected is certified; no independent audit has been performed.

## References

1. O. Fiuk, *Maslov's class K with Equivalence*, arXiv:2610.06493v1 (first public version, 2026-10-05), https://arxiv.org/html/2610.06493v1 .
2. E. Kieroński and M. Otto, *Small Substructures and Decidability Issues for First-Order Logic with Two Variables*, LICS 2005 (full version), https://www2.mathematik.tu-darmstadt.de/~otto/papers/fo2eq2011.pdf .
3. I. Pratt-Hartmann, *The Two-Variable Fragment with Counting and Equivalence*, Mathematical Logic Quarterly 61 (2015), 474–515, https://doi.org/10.1002/malq.201400102 .
