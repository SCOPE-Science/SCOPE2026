# Countable Alexandrov fibre realization of transitive modalities by \(\omega\)-accumulation

## Finding

For a nonempty finite or countably infinite transitive Kripke frame \((W,R)\), the explicit countable partial order on \(X=W\times\mathbb N\) given below realizes every Kripke modal formula by the topological \(\omega\)-accumulation operation on **fibre-saturated valuations**. The same construction is \(\omega\)-scattered exactly when the original relation is conversely well-founded. This yields direct completeness of \(\mathsf{K4}\) and \(\mathsf{GL}\) even within countably infinite \(T_0\) Alexandrov spaces (and the \(\omega\)-scattered ones for \(\mathsf{GL}\)).

## Assumptions and scope

Let \(W\ne\varnothing\) be finite or countably infinite, and let \(R\subseteq W\times W\) be transitive, with no seriality or reflexivity assumption. Write \(\mathbb N=\{0,1,2,\ldots\}\) and \(X=W\times\mathbb N\). Define
\[
 (u,i)\preceq(v,j)\quad\Longleftrightarrow\quad
 ((u,i)=(v,j))\ \lor\ (i<j\ \land\ uRv).
\]
Let \(\tau\) be the topology of upper sets for \(\preceq\), and let \(\pi(u,i)=u\). For any \(A\subseteq X\), define
\[
\omega_X(A)=\{x\in X: \text{every open neighbourhood }U\ni x\text{ has }|U\cap A|\ge\aleph_0\}.
\]
For \(B\subseteq W\), let \(\Diamond_R B=\{u\in W: \exists v\in B\text{ such that }uRv}\). A set in \(X\) is *fibre-saturated* if it equals \(\pi^{-1}(B)\) for some \(B\subseteq W\). A space is \(\omega\)-scattered if it has no nonempty **closed** \(P\subseteq\omega_X(P)\). The relation \(R\) is conversely well-founded if each nonempty \(B\subseteq W\) has \(u\in B\) such that \(R(u)\cap B=\varnothing\).

## Proof

**1. A countable \(T_0\) Alexandrov space.** Reflexivity of \(\preceq\) follows from equality. Any proper comparison strictly increases the natural-number coordinate, so opposite proper comparisons cannot occur, giving antisymmetry. If \((u,i)\prec(v,j)\prec(w,k)\), then \(i<j<k\), \(uRv\), and \(vRw\); transitivity of \(R\) yields \(uRw\), so \((u,i)\prec(w,k)\). Comparisons involving equality are immediate. Thus \(\preceq\) is a partial order. Its upper-set topology is Alexandrov and \(T_0\), and its underlying set is countably infinite because \(W\) is nonempty and at most countable.

**2. Infinite-neighbourhood calculation.** The smallest open neighbourhood of \(x=(u,i)\) is the principal upper set
\[
\uparrow x=\{(u,i)\}\cup\{(v,j):j>i\ \land\ uRv\}.
\]
Every open neighbourhood of \(x\) contains \(\uparrow x\), so \(x\in\omega_X(A)\) exactly when \(\uparrow x\cap A\) is infinite. For \(A=\pi^{-1}(B)\), if some \(v\in B\) satisfies \(uRv\), then every \((v,j)\) for \(j>i\) belongs to \(\uparrow x\cap A\); there are infinitely many. If no such \(v\) exists, the intersection is contained in the singleton \(\{(u,i)\}\). Therefore, for every \(u,i,B\),
\[
 (u,i)\in\omega_X(\pi^{-1}(B))\quad\Longleftrightarrow\quad
 u\in\Diamond_R B.
\]
This proves \(\omega_X(\pi^{-1}(B))=\pi^{-1}(\Diamond_R B)\) with no finiteness assumption on \(B\) other than the stated bound on \(W\).

**3. Full modal preservation.** The map \(\pi^{-1}:\mathcal P(W)\to\mathcal P(X)\) is injective because every fibre is nonempty; it preserves complements, intersections and unions. Assign each propositional letter \(p\) the lifted valuation \(\pi^{-1}(V(p))\). Induct on the construction of any basic modal formula \(\varphi\): the propositional steps follow from Boolean preservation, and its possibility step follows from the exact identity in Step 2. Thus \(\llbracket\varphi\rrbracket_X=\pi^{-1}(\llbracket\varphi\rrbracket_W)\) for arbitrarily deeply nested formulas. For iterates, define \(B_0=B\), \(B_{\alpha+1}=\Diamond_R B_\alpha\), \(B_\lambda=\bigcap_{\beta<\lambda}B_\beta\) for limit ordinals, and analogously \(A_0=\pi^{-1}(B)\), \(A_{\alpha+1}=\omega_X(A_\alpha)\), \(A_\lambda=\bigcap_{\beta<\lambda}A_\beta\). Transfinite induction, using preservation of arbitrary intersections by inverse image, gives \(A_\alpha=\pi^{-1}(B_\alpha)\) for all ordinals. No such claim is made for arbitrary **nonsaturated** subsets of \(X\).

**4. Exact scatteredness criterion.** If \(R\) is conversely well-founded, suppose \(P\ne\varnothing\) and \(P\subseteq\omega_X(P)\), whether or not \(P\) is closed. Let \(B=\pi(P)\), choose \(u\in B\) without an \(R\)-successor inside \(B\), and choose \((u,i)\in P\). The expression for its principal upper neighbourhood shows \(\uparrow(u,i)\cap P\subseteq\{(u,i)\}\). Hence \((u,i)\notin\omega_X(P)\), a contradiction. Therefore no nonempty closed \(\omega\)-perfect set exists.

Conversely, if \(R\) is not conversely well-founded, some nonempty \(B\subseteq W\) satisfies \(\forall u\in B\;\exists v\in B\;(uRv)\). Put \(P=\pi^{-1}(B)\). The identity in Step 2 gives \(P\subseteq\omega_X(P)\). Define \(C=\omega_X(P)\). In every topological space, \(\omega_X(P)\) is closed: if a point has one open neighbourhood meeting \(P\) only finitely, that neighbourhood is disjoint from \(\omega_X(P)\). Since \(P\subseteq C\), monotonicity yields \(C=\omega_X(P)\subseteq\omega_X(C)\). Thus \(C\ne\varnothing\) is closed and \(\omega\)-perfect, so \(X\) is not \(\omega\)-scattered. Both implications are proved, including the **closedness** requirement of the definition.

**5. Restricted completeness.** Soundness of \(\mathsf{K4}\) for \(\omega\)-accumulation on every topological space and of \(\mathsf{GL}\) on every \(\omega\)-scattered space is established in Montacute [1, Theorems 6.16 and 6.18]. Conversely, a formula outside \(\mathsf{K4}\) has a finite transitive Kripke countermodel (standard finite-frame completeness). Lift that countermodel by Steps 1–3 to a countably infinite \(T_0\) Alexandrov countermodel. A formula outside \(\mathsf{GL}\) has a finite transitive *irreflexive* Kripke countermodel (standard finite-frame completeness of \(\mathsf{GL}\)); every such finite relation is conversely well-founded, so Step 4 makes its lift \(\omega\)-scattered. The lifted valuations preserve the counterexamples. Together with soundness this gives exactly the two stated logics on these restricted classes.

## Verification

The standalone script `verify.py` enumerates every transitive relation on labeled sets of sizes \(1\) through \(4\): exactly \(2\), \(13\), \(171\), and \(3994\) relations. For each, it checks that the three-level restriction of the proposed order is a partial order, compares the two sides of the symbolic successor profile for every subset, and checks converse well-foundedness or its finite obstruction. This totals \(4180\) frames and \(259828\) (frame, subset, world) profile checks. Running `python3 verify.py` produces `VERIFY_OK total_frames=4180 total_profiles=259828`. Finite truncations **do not** establish infinite accumulation; the infinite tail and the converse implication are proved in Steps 2 and 4.

## Relationship to prior work

Montacute [1] introduces the \(\omega\)-accumulation modal interpretation, proves closure of the operator, and proves \(\mathsf{K4}\) and \(\mathsf{GL}\) completeness for the larger classes of infinite spaces and infinite \(\omega\)-scattered spaces. Its proof uses metrizable spaces and derivative maps, rather than the countable Alexandrov fibre realization and exact converse-well-foundedness criterion above. Classical Kripke completeness for \(\mathsf{K4}\) and \(\mathsf{GL}\) is assumed and not claimed as new. The contribution here is the explicit operator-intertwining construction, precise scope of its Boolean subalgebra, scatteredness equivalence, and consequent strict topological-class restriction.

## Limitations

The theorem requires a transitive relation and a finite or countable nonempty carrier. Modal truth preservation is guaranteed for valuations constant on each \(\pi\)-fibre; arbitrary subsets of \(X\) do not generally admit Kripke relational semantics for \(\omega_X\). The construction is \(T_0\) and Alexandrov, but generally **not** \(T_1\) or metrizable. Generalization to uncountable frames and equivalences involving other topological modalities is not proved. The exact construction may overlap with representation arguments in older finite-poset or modal-algebra literature not identified in the comparison.

## References

[1] Yoàv Montacute, *Halo Semantics for Modal Logic*, EPTCS 447 (2026), 623–635; arXiv:2606.31885, first publicly submitted 2026-06-30; DOI: 10.4204/EPTCS.447.35. See Definitions 6.12, Lemma 6.13, Theorems 6.16 and 6.18.

[2] Standard finite transitive and finite transitive-irreflexive Kripke-frame completeness for \(\mathsf{K4}\) and \(\mathsf{GL}\), respectively; also used in [1, Theorems 6.16 and 6.18].
