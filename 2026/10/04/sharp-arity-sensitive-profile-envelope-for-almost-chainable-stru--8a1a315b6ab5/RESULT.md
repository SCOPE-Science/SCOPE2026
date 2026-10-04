# Sharp arity-sensitive profile envelope for almost-chainable structures

## Finding
Let \(\mathbb Y\) be an infinite almost-chainable relational structure and let its kernel be \(F=\operatorname{Ker}(\mathbb Y)\) with \(|F|=k\). Write \(\varphi_{\mathbb Y}(m)\) for the number of isomorphism types of \(m\)-element induced substructures. Then, for every \(m\ge 0\),
\[
\boxed{\varphi_{\mathbb Y}(m)\le E_k(m):=\sum_{j=0}^{\min(k,m)}\binom{k}{j}.}
\]
Moreover this envelope is sharp simultaneously in every arity: for each \(k\ge0\) there is an infinite almost-chainable structure with kernel size exactly \(k\) satisfying \(\varphi_{\mathbb Y}(m)=E_k(m)\) for every \(m\ge0\).

Thus the known uniform estimate \(\varphi_{\mathbb Y}(m)\le 2^k\) is the exact eventual extremal value. For \(k>0\), the extremal value \(2^k\) first becomes possible at arity \(m=k\); for smaller arities the sharp universal ceiling is strictly smaller.

## Assumptions and scope
The structure is relational and infinite. Almost chainability is in the Fraïssé–Pouzet sense used by Kurilić: there is a finite set \(F\) and a linear order on \(Y\setminus F\) such that every finite partial automorphism of that order, extended by the identity on \(F\), is a partial automorphism of \(\mathbb Y\). Kurilić records that every infinite almost-chainable structure has a finite minimal such set, its kernel, and proves the coarser bound \(\varphi_{\mathbb Y}(m)\le 2^k\).

The sharpness examples use a finite relational language depending on \(k\). No uniform bound on the number of relation symbols is asserted.

## Proof
Fix a chaining order on \(Y\setminus F\), with \(|F|=k\). Kurilić's proof of the \(2^k\) bound establishes the stronger local fact that whenever two \(m\)-element subsets \(A,B\subseteq Y\) have the same intersection with \(F\), the induced structures on \(A\) and \(B\) are isomorphic. Indeed, \(A\setminus F\) and \(B\setminus F\) have the same finite cardinality, so there is an order-isomorphism between them; extending it by the identity on \(F\) gives a partial automorphism of \(\mathbb Y\).

Therefore an \(m\)-element induced-substructure type can be indexed by at most one subset \(T=A\cap F\). Such a subset must satisfy \(|T|\le m\). Hence the number of possible intersections is
\[
\sum_{j=0}^{\min(k,m)}\binom{k}{j},
\]
which proves the upper bound.

For sharpness, fix distinct points \(f_1,\ldots,f_k\) in a countably infinite set \(Y\). In the language with unary predicates \(P_1,\ldots,P_k\), interpret \(P_i\) as the singleton \(\{f_i\}\), and put no other structure on \(Y\). Let \(F=\{f_1,\ldots,f_k\}\). Any linear order on \(Y\setminus F\) chains the structure over \(F\), since every partial order-automorphism of the outside points fixes the truth values of all predicates after adjoining the identity on \(F\).

Conversely, every chaining kernel must contain each \(f_i\). If \(f_i\) were left in the ordered part, a one-point partial automorphism of that order could send \(f_i\) to an ordinary outside point, contradicting preservation of \(P_i\). Thus the kernel is exactly \(F\).

Finally, an \(m\)-element induced substructure in this example is determined up to isomorphism exactly by the set \(T\subseteq F\) of named singleton points it contains. Every \(T\) with \(|T|\le m\) occurs, by adjoining \(m-|T|\) ordinary outside points, and distinct \(T\)'s yield non-isomorphic structures because the predicate symbols distinguish the singleton points. Hence
\[
\varphi_{\mathbb Y}(m)=\sum_{j=0}^{\min(k,m)}\binom{k}{j}
\]
for all \(m\), proving simultaneous sharpness.

## Verification
The bundled verifier checks the envelope formula for \(0\le k\le 8\) and \(0\le m\le 10\), verifies that it stabilizes at \(2^k\) exactly from arity \(k\) onward for \(k>0\), and independently enumerates finite truncations of the singleton-predicate sharpness construction. It canonically records each induced substructure by the set of singleton predicates realized and confirms exact agreement with \(E_k(m)\). The expected final line is `VERIFY_OK`.

The finite replay checks the extremal construction and arithmetic; the all-cardinality theorem is the structural argument above.

## Relationship to prior work
Kurilić proves that an infinite almost-chainable structure has a finite kernel and records, as Fact 2.3, the uniform bound \(\varphi_{\mathbb Y}(m)\le 2^k\), where \(k\) is the kernel size. His proof already contains the key statement that equal intersections with the kernel force isomorphic finite induced substructures. The arity-sensitive counting refinement above retains the cardinality constraint \(|A\cap F|\le m\), which is discarded when one bounds by all \(2^k\) subsets of the kernel.

Earlier work of Fraïssé and Pouzet characterizes bounded profiles in terms of almost-chainability (and equivalent finite monomorphic decompositions). Targeted searches of those profile results, the Kurilić paper, semantic research indexes, and exact-formula queries did not locate the partial-binomial envelope or a statement of its simultaneous sharpness. The contribution claimed here is therefore the sharp quantitative refinement, not the bounded-profile characterization or the coarse \(2^k\) estimate.

## Limitations
The originality assessment is literature-based and cannot exclude an unindexed observation or an equivalent statement phrased through monomorphic decompositions. The sharpness construction uses \(k\) unary predicate symbols, so no claim is made that the same envelope is attainable in every fixed finite signature. The result concerns induced-substructure profiles, not ordered tuple-orbit profiles.

## References
M. S. Kurilić, *Vaught's Conjecture for Almost Chainable Theories*, Journal of Symbolic Logic 86 (2021), 991–1005. arXiv:1905.05531; DOI:10.1017/jsl.2021.60.

M. Pouzet, *The Profile of Relations*, survey/preprint on profiles of relational structures; in particular the equivalence between bounded profile and almost-chainability discussed there.
