# Sharp connected-poset bound for nonalgebraic one-point types of the random poset

## Finding
Let \(\mathbb D\) be the countable universal ultrahomogeneous partial order. For a finite nonempty induced parameter poset \(P\subset\mathbb D\), let \(t(P)\) be the number of complete **nonalgebraic** one-point types over its individually named points. If the undirected comparability graph of \(P\) is connected and \(|P|=n\), then
\[
\boxed{t(P)\le 3\cdot 2^{n-1}.}
\]
Equality holds if and only if \(P\) is a height-two star, namely an ordinal sum \(\mathbf 1\oplus A_{n-1}\) or its dual \(A_{n-1}\oplus\mathbf 1\), where \(A_k\) denotes the \(k\)-element antichain. This also includes \(n=1\) (the singleton) and \(n=2\) (the two-element chain). In contrast, an unrestricted \(n\)-element antichain has \(2^{n+1}-1\) nonalgebraic types.

## Assumptions and scope
A comparability edge joins distinct comparable points, so connectedness is not restricted to the Hasse diagram or to height-two posets. Types distinguish every named parameter; equality types \(x=a\) are excluded. The assertion applies to all finite posets with connected comparability graphs, with no hypothesis about width, height or unique extrema. The countable random poset realizes all finite one-point extensions, and homogeneity identifies types with admissible extension patterns.

## Proof
**1. One-point extension encoding (established).** For \(x\notin P\), put \(L=\{p\in P:p<x\}\) and \(U=\{p\in P:x<p\}\). A pair \((L,U)\) is realizable exactly if \(L\) is an order ideal, \(U\) is an order filter, and \(l<u\) for all \(l\in L\) and \(u\in U\). The last condition is vacuous if one set is empty. A realizable pair gives one nonalgebraic complete type. Write \(\mathcal T(P)\) for all such pairs.

**2. An extremal non-cut vertex exists.** If the comparability graph \(G\) is connected and has at least two vertices, there is a minimal or maximal element \(z\) of \(P\) such that \(G-z\) remains connected. Indeed, use the standard block-cut decomposition of \(G\). Choose a leaf block, or the unique block if \(G\) has no cut vertex. This block has at least two vertices and at most one vertex \(a\) that is a cut vertex of \(G\). The induced finite poset on the block has at least one minimal vertex and at least one maximal vertex; at least one of these is different from \(a\) (otherwise the block would have only one vertex). Choose that extreme \(z\). Because \(z\) is not an articulation vertex, all its incident comparability edges belong to this block: an edge from \(z\) to outside the block would put \(z\) in another block and make it a cut vertex. Hence \(z\) is globally minimal or globally maximal in \(P\), and deletion preserves comparability-connectedness. The case of a single edge is included (it is a block).

**3. Doubling lemma with equality.** Let \(P=Q\cup\{z\}\), where \(Q\) is nonempty, \(z\) is maximal in \(P\), and \(B=\{q\in Q:q<z\}\ne\varnothing\). Then \(B\) is an ideal in \(Q\). Given an admissible \((L,U)\in\mathcal T(Q)\), the three possibilities for \(z\) relative to the newly adjoined \(x\) are admissible precisely under the following conditions:
\[
\begin{array}{c|c}
 z<x & U=\varnothing,\ B\subseteq L\\
 z\parallel x & U\cap B=\varnothing\\
 x<z & L\subseteq B
\end{array}
\]
These are necessary and sufficient by checking downward and upward closure and the transitivity condition in the extended poset. All three hold simultaneously only for \((L,U)=(B,\varnothing)\). Also \((L,U)=(\varnothing,Q)\) has only the option \(x<z\), because \(B\ne\varnothing\). Every other type has at most two extensions. Therefore
\[
t(P)\le 2t(Q).
\]
For equality, every type other than the two specified exceptional types must have exactly two extensions. For each \(b\in B\), the admissible \((\varnothing,\uparrow b)\) has only one extension, since \(\uparrow b\cap B\ne\varnothing\); consequently \(\uparrow b=Q\). Thus every \(b\in B\) is a least element of \(Q\); uniqueness of a least element implies \(B=\{b\}\). If there exist comparable \(q<r\) in \(Q\setminus\{b\}\), then \((\downarrow q,\uparrow r)\) is admissible and admits only \(z\parallel x\): \(U\ne\varnothing\), \(L\nsubseteq B\), and \(\uparrow r\cap B=\varnothing\). This yields another singly extending type and contradicts equality. Hence \(Q\setminus\{b\}\) is an antichain. Therefore \(P\) is the star with least element \(b\). Conversely when \(Q\) has that form and \(B=\{b\}\), exactly one type has three extensions and exactly one has one extension, and every other type has two, giving equality. The statement for minimal \(z\) follows by order duality.

**4. Induction.** For \(n=1\), precisely three relations to the singleton are possible, hence \(t(P)=3\). Suppose \(n\ge2\). Step 2 supplies a minimal or maximal \(z\) whose deletion \(Q\) is connected. Connectedness ensures that \(z\) is comparable with at least one member of \(Q\), so Step 3 (or its dual) yields
\[
t(P)\le2t(Q)\le2(3\cdot2^{n-2})=3\cdot2^{n-1}.
\]
If equality holds, the doubling lemma already forces \(P\) to be a star or dual star.

**5. Equality is attained.** If \(P=\mathbf1\oplus A_k\), a type with the center below \(x\) can put each leaf below or incomparable to \(x\), or each leaf above or incomparable to \(x\), yielding \(2^{k+1}-1\) patterns after subtracting the double-counted all-incomparable leaf pattern. If the center is incomparable with \(x\), leaves can be above or incomparable (\(2^k\) patterns). If \(x\) lies below the center, all leaves lie above it (one pattern). The total is \(2^{k+1}-1+2^k+1=3\cdot2^k\). Duality gives the same count for the opposite star, proving the full equality classification.

## Verification
The independently coded exhaustive enumerator in `verify.py` constructs all naturally labeled finite posets through order six, computes \(t(P)\) by admissible ternary labels, tests connectedness and the exact bound/equality condition, and separately checks the doubling lemma for all enumerated connected extensions by a maximal point. It checks 2996 connected instances and 4823 extension instances and returns `ALL_CHECKS_PASS`. Run with `python3 verify.py` using Python standard library; expected output is in `verification_output.txt`. Finite enumeration is not a proof for arbitrary \(n\); the preceding induction is.

## Relationship to prior work
The admissible ideal/filter encoding of one-point extensions is a known construction, stated explicitly in Dolinka and Mašulović, *A universality result for endomorphism monoids of some ultrahomogeneous structures*, arXiv:1009.2892, Section 3.1. The published finding *Finite-parameter 1-type counting in the random poset is #P-complete* (published-finding corpus identifier `2026/10/4/SCOPE-finite-parameter-1-type-counting-in-the-random-poset-is-p-comple--3b955f4020e1`) was inspected in full: it proves this encoding, #P-completeness, and the global chain/antichain endpoint counts, not the maximum restricted to connected comparability graphs or its equality classification. *Embeddings into the generic poset*, arXiv:2502.16695, Section 2, treats extension patterns and automorphism embeddings, not connected-poset extremal type counts. The new ingredient is the sharp connectedness-sensitive doubling induction and equality classification; no novelty is claimed for the standard encoding or graph block-cut decomposition.

## Limitations
This is a connected-comparability-graph extremal theorem for nonalgebraic complete 1-types, not a formula for all posets or for multi-types. It depends on the standard Fraïssé description of the random poset and standard finite graph block decomposition. Exact identification of every possible obscure or unpublished earlier equivalent theorem is not guaranteed; no independent review has been conducted.

## References
1. I. Dolinka and D. Mašulović, *A universality result for endomorphism monoids of some ultrahomogeneous structures*, arXiv:1009.2892, first public preprint 15 September 2010; see Section 3.1 for ideal/filter one-point extension patterns.
2. *Finite-parameter 1-type counting in the random poset is #P-complete*, published-finding corpus record `2026/10/4/SCOPE-finite-parameter-1-type-counting-in-the-random-poset-is-p-comple--3b955f4020e1`, inspected full RESULT.md.
3. *Embeddings into the generic poset*, arXiv:2502.16695, Section 2, full manuscript inspected.
4. Standard block-cut tree theorem for connected finite undirected graphs (used to select a non-articulation extremal vertex).
