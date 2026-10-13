# Exact permission distributivity via join-generated witnesses

## Finding

For an arbitrary modal state space with inclusive exact verification, the positive exact-equivalence schema
\[
\Diamond(A\lor B)\approx\Diamond A\lor\Diamond B
\]
is valid at **every** model on the given state space, for **all** formulas \(A,B\), precisely when each exact permitter of a fused state is itself expressible as a nonempty fusion of exact permitters of at least one of the two constituent states. This is an exact frame-correspondence criterion, not merely a sufficient condition.

More formally, let \(P(X)=\{s\in S:\exists t\in X\ (s\triangleright t)\}\) and \(J(X)=\{\bigvee Y:\varnothing\ne Y\subseteq X\}\). The criterion is
\[
\tag{G} \forall t,u\in S:\quad
P(\{t\vee u\})\subseteq J(P(\{t\})\cup P(\{u\})).
\]
In a finite state space \(S\), \(G\) has a direct \(O(|S|^4)\) decision procedure from the join and permission tables.

The condition \(G\) is **strictly weaker** than condition \(C1\) in Berardi Gili (2026), Proposition 1. The smallest strict example has four states. Exhaustive enumeration on the labeled four-element Boolean join-semilattice gives \(42{,}448\) permitted relations satisfying \(G\), of which \(38{,}416\) satisfy \(C1\), leaving \(4{,}032\) strict examples.

## Assumptions and scope

A **modal state space** is a tuple \((S,\leq,\triangleright,\blacktriangleright)\), where \(S\ne\varnothing\), every subset of \(S\), including the empty subset, has a supremum, and exact permission \(\triangleright\) and exact preclusion \(\blacktriangleright\) are arbitrary binary relations. Write \(s\vee t\) for binary supremum. No monotonicity, finiteness, or consistency is assumed.

Each atomic positive and negative valuation is any subset closed under binary joins; the empty subset is allowed. The relevant inclusive exact verification clauses, for \(T_A=\{s:s\text{ exactly verifies }A\}\), are
\[
T_{A\land B}=\{x\vee y:x\in T_A,\ y\in T_B\},\qquad
T_{A\lor B}=T_A\cup T_B\cup T_{A\land B},\qquad
T_{\Diamond A}=J(P(T_A)).
\]
Exact equivalence means equality of positive verification sets. Negation swaps positive and negative content and does not change the claim: the theorem is valid for arbitrary nested formulas, since it is proved for arbitrary positive sets. The preclusion relation places no restriction on this statement.

## Proof

**Step 1: closure identities.** For all subsets \(X,Y\subseteq S\), \(J\) is monotone, extensive when its input is nonempty (and \(J(\varnothing)=\varnothing\)), and idempotent:
\[
J(J(X))=J(X).
\]
Indeed, an arbitrary nonempty collection of nonempty fusions is the fusion of the union of the corresponding nonempty generating collections. Moreover, with
\[
D(X,Y)=X\cup Y\cup\{x\vee y:x\in X,\ y\in Y\},
\]
we have the identity
\[
D(J(X),J(Y))=J(X\cup Y).
\]
For the nontrivial inclusion from right to left, separate a nonempty generating set into its \(X\)-part and its \(Y\)-part. If both are nonempty, the full fusion is the binary fusion of their two supremums; otherwise it is already in \(J(X)\) or \(J(Y)\). This also covers the empty-set boundary cases.

**Step 2: sufficiency.** Fix arbitrary positive sets \(X=T_A\), \(Y=T_B\). Since
\[
P(D(X,Y))=P(X)\cup P(Y)\cup\bigcup_{x\in X,\,y\in Y}P(\{x\vee y\}),
\]
condition \(G\) implies
\[
P(D(X,Y))\subseteq J(P(X)\cup P(Y)).
\]
Applying \(J\), and using its monotonicity/idempotence, gives \(J(P(D(X,Y)))\subseteq J(P(X)\cup P(Y))\). The reverse containment follows from \(X\cup Y\subseteq D(X,Y)\). By Step 1 and the displayed semantic clauses,
\[
T_{\Diamond(A\lor B)}=J(P(D(X,Y)))
=J(P(X)\cup P(Y))=T_{\Diamond A\lor\Diamond B}.
\]
No induction hypothesis on formulas is needed; the derivation applies to their complete positive contents regardless of nesting.

**Step 3: necessity.** Suppose the indicated exact equivalence holds in every model on the frame, in particular for the two distinct propositional variables \(p,q\). Choose positive atomic valuations \(T_p=\{t\}\) and \(T_q=\{u\}\), permissible because singletons are binary-join-closed; assign arbitrary admissible negative valuations. Since \(t\vee u\in T_{p\lor q}\), every \(s\in P(\{t\vee u\})\) belongs to \(T_{\Diamond(p\lor q)}\), by taking the singleton generator \(\{s\}\). The assumed equivalence and Step 1 imply
\[
s\in T_{\Diamond p\lor\Diamond q}
=J(P(\{t\})\cup P(\{u\})).
\]
Thus \(G\) holds for all \(t,u\), proving necessity, including when any relevant permission set is empty.

**Step 4: finite test.** Given \(s,t,u\), set
\[
Q_{s;t,u}=\{r\in S:r\le s\text{ and }(r\triangleright t\text{ or }r\triangleright u)\}.
\]
For finite \(S\), \(s\in J(P(\{t\})\cup P(\{u\}))\) if and only if \(Q_{s;t,u}\ne\varnothing\) and \(\bigvee Q_{s;t,u}=s\). The forward implication is because every possible generating witness \(r\) lies below \(s\), so its join is bounded by the join of all of \(Q\), which itself lies below \(s\). The reverse implication uses \(Q\) as the witnessing set. Iterate over \(n^3\) triples and scan \(n\) states each, with table lookup for joins/comparisons: total \(O(n^4)\) time (after input tables are available).

**Step 5: strictness, sharpness, and census.** On the four-element Boolean join-semilattice \(S=\{\bot,a,b,\top\}\), with \(a\vee b=\top\), set the permission relation to **exactly**
\[
a\triangleright a,\qquad b\triangleright b,\qquad \top\triangleright\top.
\]
Preclusion is arbitrary, for example empty. Condition \(C1\) fails at \((s,t,u)=(\top,a,b)\): \(\top\triangleright(a\vee b)\) but \(\top\) permits neither \(a\) nor \(b\). Condition \(G\) nevertheless holds. If \(t\vee u\) is \(\bot,a\), or \(b\), any actual permitter already permits an operand; if it is \(\top\) and neither operand is \(\top\), the only relevant pair is \(a,b\), whose permitters \(a,b\) fuse to \(\top\). If an operand is \(\top\), its permitter \(\top\) is present directly.

Every nonempty complete join-semilattice with fewer than four points is a chain: two incomparable points together with their bottom and join would already give four distinct points. In a chain, \(t\vee u\) is one of the operands, so \(C1\) holds automatically. The strict witness is therefore cardinality-minimal.

Finally, the complete enumeration in `artifacts/verify.cpp` loops over all \(2^{16}\) possible labeled permission relations on this Boolean semilattice, checks both frame conditions, and compares the two semantic sides for all join-closed positive atomic contents. Its outputs are \(42{,}448\) valid relations under \(G\), \(38{,}416\) under \(C1\), and \(4{,}032\) in their difference. This finite census is exhaustive for the stated labeled four-state domain, not for all finite or infinite state spaces.

## Verification

Compile and run `artifacts/verify.cpp` with a C++17 compiler, e.g. `g++ -O2 -std=c++17 artifacts/verify.cpp -o verify && ./verify`. It checks all permission relations on the one-, two-, and three-element chains and the four-element Boolean lattice; it independently evaluates the frame criterion and the semantic schema on all pairs of join-closed contents. On the four-element Boolean lattice, its output is:

```text
n=4 relations=65536 admissible=14 C1=38416 exact_condition=42448 schema_valid=42448 strict=4032
VERIFY_OK
```

The all-size and infinite-state-space equivalence is proved by Steps 1–3, **not** by this finite experiment. The code is limited to four-state Boolean testing; no external formal proof certificate is claimed.

## Relationship to prior work

Berardi Gili, *The Modal Logic of Exact Equivalence* (2026), Definitions 2–5 and Proposition 1, introduces the inclusive exact-verification clauses and establishes \(C1\) as a **sufficient** condition for the stated diamond/disjunction schema. The present result identifies an exact, weaker frame condition, proves necessity, and gives a minimal strict separation and decision test. The article's global soundness/completeness and normal-form results are distinct from this frame-correspondence question.

Kim (2024) studies an earlier non-inclusive exact modal verification clause; its diamond verification sets are not in general closed under arbitrary nonempty fusions. Results in that different semantics cannot be directly substituted for this correspondence statement. General descriptions of inclusive truthmaker disjunction (e.g. Champollion 2025) give the propositional component but do not themselves settle the interaction with the exact-permission relation.

## Limitations

The assertion is about **positive exact content only** and **all valuations on a fixed frame**. It does not characterize a logic axiomatization or the separate negative-content schema for \(\neg\Diamond\), which also involves the independent exact-preclusion relation. The finite algorithm assumes explicit finite order/join and permission tables. The four-state counts concern only the labeled Boolean semilattice, not all four-point state spaces. A possible unlocated equivalent representation in the general theory of join-generated relational operators remains a literature risk.

## References

1. Pietro Berardi Gili, *The Modal Logic of Exact Equivalence*, *The Review of Symbolic Logic*, online 6 May 2026, DOI: https://doi.org/10.1017/S1755020326101154. Definitions 2–5, Proposition 1, and the discussion surrounding its stronger axiom (A11)*.
2. Dongwoo Kim, *Exact Truthmaker Semantics for Modal Logics*, *Journal of Philosophical Logic* **53** (2024), 789–829. DOI: https://doi.org/10.1007/s10992-024-09752-9.
3. Lucas Champollion, *Truthmaker Semantics and Natural Language Semantics*, *Language and Linguistics Compass* (2025), DOI: https://doi.org/10.1111/lnc3.70004. Discussion of inclusive and non-inclusive disjunction.
