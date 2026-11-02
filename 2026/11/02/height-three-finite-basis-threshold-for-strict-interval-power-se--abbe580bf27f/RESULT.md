# Height-three finite-basis threshold for strict interval power semirings

## Finding
Let \(P\) be any finite poset, and form its **strict interval semigroup**
\[
S(P)=\{0\}\mathbin{\cup}\{(a,b):a,b\in P,\ a<b\},
\]
with zero absorbing and
\[
(a,b)(c,d)=\begin{cases}(a,d),&b=c,\\0,&b\ne c.\end{cases}
\]
Here an output \((a,d)\) in the first case is automatically a strict comparable pair. Let \(\mathcal P(S(P))\) be the **full power semiring**, including the empty subset, with union as addition and setwise multiplication as multiplication. Finite basability refers to all equations in the constant-free signature of these two binary operations.

**Theorem.** For every finite poset \(P\), the equational theory of \(\mathcal P(S(P))\) admits a finite basis if and only if the height of \(P\), meaning the maximum number of vertices in a chain, is at most three:
\[
\boxed{\mathcal P(S(P))\text{ is finitely based}\quad\Longleftrightarrow\quad\operatorname{ht}(P)\le3.}
\]
In particular, the answer is independent of the width, number of elements, or branching of \(P\). The four-element chain is the first chain for which finite basability fails; its interval semigroup has seven elements. Unlike the flat interval semiring on the same strict intervals, the full power semiring becomes nonfinitely based at this threshold. For any height at least four, an explicit unbounded family of oriented odd-cycle relational obstructions witnesses failure of finite duality.

## Assumptions and scope
The order is finite and antisymmetric, and only **strict** comparable pairs occur as nonzero semigroup elements. There are no identity-loop elements \((a,a)\). Multiplication is as displayed, not convolution in the incidence algebra. The empty subset is included in \(\mathcal P(S(P))\); the nonempty power semiring is not covered. No constants are named in the equational signature. For the empty poset, the height is zero and \(S(P)=\{0\}\).

## Proof
**1. Associativity and nilpotence.** Strict composable intervals multiply as matrix units, and transitivity of the order ensures closure. A product of \(j\) nonzero intervals is nonzero exactly when the intervals form a composable strict chain
\[
(a_0,a_1)(a_1,a_2)\cdots(a_{j-1},a_j)=(a_0,a_j),\qquad a_0<a_1<\cdots<a_j.
\]
Thus, whenever \(h=\operatorname{ht}(P)\ge2\), the nilpotency index of \(S(P)\) is exactly \(h\). When \(h\le1\), the semigroup is \(\{0\}\), whose full power semiring is the two-element distributive lattice and is finitely based.

**2. Relational criterion used.** For a nonzero finite nilpotent semigroup \(S\) of index \(d\), let \(\mathcal N(S)\) have universe \(S\setminus\{0\}\) and relations \(R_j\) recording nonzero ordered products of length \(j\), for \(1\le j\le d-1\). Wang, Yin, and Wang, *Finite bases for full power semirings of finite nilpotent semigroups*, Theorem 1.1 (arXiv:2610.01329v1), prove that \(\mathcal P(S)\) is finitely based if and only if \(\mathcal N(S)\) has finite homomorphism duality. Finite duality means that a fixed finite list of finite relational obstructions detects every finite structure that does not map homomorphically to \(\mathcal N(S)\). The theorem's proof is via short-word identities, local homomorphism constraints, and closure quotients; the present proof supplies the required new analysis of \(\mathcal N(S(P))\).

**3. Heights two and three.** If \(h=2\), only the unary relation \(R_1\) appears, and it contains the whole nonempty universe, so every finite structure maps to \(\mathcal N(S(P))\); finite duality is immediate. If \(h=3\), the only nontrivial higher relation is
\[
R_2=\{((a,b),(b,c)):a<b<c\}.
\]
Its directed graph has at least one edge and has **no directed walk of length two**. Indeed, a vertex that is both the target of \(((a,b),(b,c))\) and the source of \(((b,c),(c,d))\) would give \(a<b<c<d\), contradicting height three. Consequently this graph is homomorphically equivalent to the single directed edge: every source maps to its tail, every target to its head, and isolated vertices can map arbitrarily; any existing edge supplies the converse map. The one-edge template admits a finite obstruction family, consisting of the directed two-edge walk (its vertices need not be distinct). Hence \(\mathcal N(S(P))\) has finite duality. This low-index argument is also subsumed by the broader classification of bipartite product digraphs for semigroups of nilpotency index three; the new content below concerns all higher nilpotency indices and all finite posets.

**4. An obstruction in every height at least four.** Choose a chain \(a<b<c<d\). Its consecutive intervals provide a directed two-edge path in \(R_2\):
\[
(a,b)\longrightarrow(b,c)\longrightarrow(c,d).
\]
For each odd integer \(\ell=2m+1\ge3\), define a finite relational structure \(H_\ell\) on vertices \(0,1,\ldots,2m\). Its unary relation is the full vertex set, all relations of arity at least three are empty, and its binary relation comprises exactly
\[
2j\to2j+1,\quad 2j+2\to2j+1\quad(0\le j<m),\qquad 2m\to0.
\]
This is an oriented odd cycle with a single directed two-edge walk, \(2m\to0\to1\).

No homomorphism \(H_\ell\to\mathcal N(S(P))\) exists. Otherwise, write the image of vertex \(i\) as a strict interval \((u_i,v_i)\). Every binary-relation edge \(i\to j\) forces \(v_i=u_j\). Following the alternating edges and the closing edge gives
\[
v_0=u_1=v_2=u_3=\cdots=v_{2m}=u_0,
\]
contradicting \(u_0<v_0\).

On the other hand, **every proper induced substructure of \(H_\ell\) maps** to \(\mathcal N(S(P))\). After deleting at least one vertex, the underlying graph is a disjoint union of oriented paths with at most one directed two-edge walk among them. A path without a directed two-edge walk maps to the one-edge digraph (its internal vertices are alternating sources and sinks). A path containing the unique directed two-edge walk maps to the directed three-vertex path by sending that walk to \(0\to1\to2\) and extending by alternating the values \(0,1\) toward its left end and \(1,2\) toward its right end. The chosen intervals \((a,b),(b,c),(c,d)\) embed this directed three-vertex path into the binary relation of \(\mathcal N(S(P))\). Empty higher-arity relations impose no extra condition.

Because \(\ell\) is arbitrarily large, no uniform size bound exists on induced substructures witnessing non-mappability; hence no finite obstruction family can exist. The cited finite-duality criterion now proves that \(\mathcal P(S(P))\) is not finitely based whenever \(\operatorname{ht}(P)\ge4\).

**5. Explicit semiring identities.** More concretely, for every odd \(\ell\ge\operatorname{ht}(P)\) in the nonfinitely based case, let \(E(H_\ell)\) be the displayed set of ordered arcs. Then
\[
\left(\prod_{i=0}^{\ell-1}x_i\right)+\left(\sum_{(i,j)\in E(H_\ell)}x_ix_j\right)
\ \approx\ \sum_{(i,j)\in E(H_\ell)}x_ix_j
\]
is a valid identity in the full power semiring. If some variable is empty, the left long product is empty; if all variables are nonempty, the long product is \(\{0\}\), and the odd-cycle obstruction forces at least one binary product to contain zero. By the quantitative local-obstruction argument in the cited paper (Theorem 4.1), choosing \(\ell>(h-1)(k+2)\) gives such an identity not derivable from the valid identities involving at most \(k\) variables. This also directly exhibits why no bounded-variable identity basis can suffice.

## Verification
The companion Python program `verify.py` checks associativity for all posets admitting a fixed linear extension on at most five vertices. It examines all \(5231\) transitive strict orders in fixed linear-extension coordinates through six vertices, confirms the absence of a directed two-edge \(R_2\)-walk at heights at most three, and finds a composable triple at heights at least four. Independently, it solves the homomorphism constraints for the oriented odd cycles of lengths \(3,5,\ldots,17\) against the chain templates on four through six vertices; none map. Deleting any one vertex from each tested odd cycle yields a map to the directed three-vertex path. The recorded result is `VERIFY_OK`. These finite checks corroborate the all-poset proof; they do not replace the infinite obstruction argument.

## Relationship to prior work
The general equivalence between finite basis and finite relational duality is **Theorem 1.1 of Wang–Yin–Wang (2026)**, not a new result here. Their Example 4.4 already treats the four-element nilpotent semigroup with a single nonzero product, which is exactly the strict interval semigroup of a three-element chain. Their Example 4.5 warns that finite basability does not pass reliably to subsemigroups or Rees quotients; therefore the four-chain result cannot be claimed simply by embedding an older obstruction. The contribution established here is the uniform if-and-only-if height criterion for **all finite posets**, with the **higher-nilpotency-index negative direction** established by an explicit family of increasingly large relational obstructions. The positive height-three case can also be obtained from more general previous index-three digraph results and is not claimed separately as new. Gao and Zhou (arXiv:2610.06351v1, Section 3 and Theorem 4.11) define a **flat interval semiring** on exactly the same strict comparable pairs and the same multiplicative table, but with idempotent *flat* addition: two distinct elements sum to the absorbing zero. They prove the flat interval semiring of every finite **chain** is finitely based, even when the chain has at least four elements. Thus their positive chain theorem cannot imply finite basability of the full powerset semiring: the latter replaces flat addition with **set union on every subset**, and the distinction changes the answer in each chain of at least four elements. Conversely their nonfinite-basis results for certain other flat interval semirings do not yield nonfinite basability of full power semirings, because finite basability need not pass through subalgebra/quotient constructions. This direct same-multiplication comparison supports the significance of the present boundary. Results on the power semiring of the three-element object \(S_7\) and on finite-group power semirings concern different underlying multiplicative semigroups.

## Limitations
The result concerns strict comparable-pair semigroups, not arbitrary nilpotent semigroups, all incidence algebras, or nonempty power semirings. It uses the published finite-duality theorem as a premise; it is not a new proof of that general theorem. No minimal finite equational basis is exhibited for every height-three poset. The explicit odd-cycle identities witness unbounded-variable complexity via the cited closure theorem, not an independently constructed family of finite countermodels. Historical priority beyond inspected publications and targeted record searches is not certified. Classical directed-graph duality may furnish an alternative abstract derivation, but a complete earlier height classification for the full powerset construction has not been identified.

## References
1. L. Wang, Q. Yin, A. Wang, *Finite bases for full power semirings of finite nilpotent semigroups*, arXiv:2610.01329v1 (publicly submitted 2026-10-01), especially Theorem 1.1, Lemma 3.3, Theorem 4.1, and Example 4.4. https://arxiv.org/abs/2610.01329
2. M. Yue, M. Ren, Z. Gao, *Explicit equational bases for the power semirings of* \(S_7\), arXiv:2609.19957v1 (2026-09-17). https://arxiv.org/abs/2609.19957
3. X. Shao, Z. Gao, *Nonfinitely based intervals of power semiring varieties*, arXiv:2609.26019v1 (2026-09-22). https://arxiv.org/abs/2609.26019
4. Z. Gao, Y. Zhou, *Equational Theories of Interval Semirings of Posets*, arXiv:2610.06351v1 (publicly submitted 2026-10-05), Section 3 (flat addition) and Theorem 4.11 (chain finite basis). https://arxiv.org/abs/2610.06351
