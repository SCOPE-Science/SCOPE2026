# An explicit eight-state enumerator for all super-dominating sets of forests

## Finding

**Theorem.** For every finite simple forest \(F=(V,E)\), including the empty forest and isolated vertices, the full polynomial
\[
D_{\mathrm{sp}}(F;x)=\sum_{D\subseteq V\, :\, D\text{ is super dominating}} x^{|D|}
\]
is obtained exactly by the eight-state rooted-tree recurrence below. Each vertex passes at most eight polynomial messages to its parent; each child combination uses at most twelve intermediate states. Naive polynomial convolution therefore requires at most \(O(n^3)\) integer-arithmetic operations for \(n=|V|\). The result determines **every cardinality coefficient** and, in particular, counts every minimum super-dominating set of any forest.

As a corollary, the previously established tree formula \(\gamma_{\mathrm{sp}}(F)=n-\nu(F)\), where \(\nu(F)\) is maximum matching cardinality, identifies the minimum-set count as
\[
\#\{D\subseteq V: D\text{ super dominates }F,\ |D|=n-\nu(F)\}
=[x^{n-\nu(F)}]D_{\mathrm{sp}}(F;x).
\]
The scalar formula was previously established for trees by Bujtás, Ghanbari and Klavžar [2]; it is not a new claim here.

## Assumptions and scope

Every graph is undirected, finite and simple. A subset \(D\subseteq V\) is **super dominating** when, for each \(w\in V\setminus D\), there exists \(b\in D\) such that
\[
N_F(b)\cap(V\setminus D)=\{w\}.
\]
Call members of \(D\) *black* and other vertices *white*. Root each nontrivial component of \(F\) arbitrarily; an isolated vertex is a one-vertex rooted tree.

For a vertex \(v\) with descendant subtree \(T_v\), fix an external parent-color bit \(t\in\{0,1\}\), with \(1\) meaning black. Define polynomial messages \(M_v(t;c,h,q)\), indexed by the color \(c\) of \(v\), and two status bits \(h,q\). Exactly four triples occur:
\[
(c,h,q)\in\{(0,0,0),(0,1,0),(1,0,0),(1,0,1)\}.
\]
Thus there are at most eight messages over the two choices of \(t\). The coefficient of \(x^j\) counts black/white assignments on \(T_v\) having exactly \(j\) black vertices and satisfying these conditions:

1. Every white vertex strictly below \(v\) has a **genuine** black witness inside \(T_v\), with its actual neighborhood evaluated using the fixed external parent color at the relevant boundary.
2. If \(c=0\), then \(q=0\) and \(h=1\) exactly when no black child of \(v\) witnesses \(v\). In this case only its parent might still witness it; \(h=0\) means a black child already witnesses it.
3. If \(c=1\), then \(h=0\) and \(q=1\) exactly when \(v\) has no white children. In that case a white parent would be the **only** white neighbor of \(v\), so \(v\) could witness that parent.

When a child \(u\) is evaluated below \(v\), the parent bit passed to it is \(c\), the actual color of \(v\). No artificial boundary edge is inserted into the original forest.

## Proof

**Explicit transition.** Fix \(t,c\in\{0,1\}\). Choose one admissible triple \((c_u,h_u,q_u)\) and one message term from \(M_u(c;c_u,h_u,q_u)\) for each child \(u\) of \(v\). Let
\[
w=\#\{u:c_u=0\},\qquad r=\#\{u:c_u=0,\ h_u=1\},\qquad
s=\#\{u:c_u=1,\ q_u=1\}.
\]
Multiply the chosen child-message polynomials and multiply by \(x^c\); aggregate the resulting polynomial in the parent state prescribed by the following cases.

If \(c=0\), **reject** the combination when \(r>0\); a white parent cannot witness a pending white child. Otherwise contribute to
\[
M_v(t;0,\mathbf 1_{s=0},0).
\]
A black child is a valid witness for white \(v\) precisely when it has no white children, which is recorded by \(q_u=1\). Thus \(v\) remains pending exactly when \(s=0\).

If \(c=1\), **reject** the combination when both \(r>0\) and \(w+(1-t)\ne1\). Otherwise contribute to
\[
M_v(t;1,0,\mathbf 1_{w=0}).
\]
Indeed, any pending white child must be witnessed by \(v\). The black vertex \(v\) witnesses such a child exactly when \(v\) has one white neighbor in total: its \(w\) white children and, when \(t=0\), its white parent. The condition also forces \(r=1\) whenever \(r>0\). If \(r=0\), no child asks \(v\) to be a witness, so no restriction on \(w\) is needed. Finally \(q=1\) exactly when \(w=0\).

For a leaf, empty child products give the two nonzero messages, for each \(t\):
\[
M_v(t;0,1,0)=1,\qquad M_v(t;1,0,1)=x.
\]
Equivalently these are the base cases of the same transition.

**Root and components.** For a component rooted at \(r_0\), take the artificial boundary color \(t=1\), and define
\[
D_{\mathrm{sp}}(T;x)=\sum_{\substack{(c,h,q)\\ h=0}}M_{r_0}(1;c,h,q).
\]
The fake black parent cannot witness a white root: the root is accepted only when it already has a genuine child witness, i.e. \(h=0\). For a black root, assigning \(t=1\) correctly indicates that there is no *white* parent when testing whether the root can witness pending children. Finally, for components \(T_1,\ldots,T_m\), set
\[
D_{\mathrm{sp}}(F;x)=\prod_{i=1}^{m}D_{\mathrm{sp}}(T_i;x),
\]
where the empty product is \(1\).

**Why this is exact.** Proceed by induction on descendant subtree order. Child assignments are independent once the parent color is fixed. Any pending white child can acquire a witness outside its subtree only from its parent, and exactly the condition \(w+(1-t)=1\) makes that black parent its unique-white-neighbor witness. All other white descendants are already witnessed by induction. For a white parent, a black child witnesses it if and only if that child has no white children, which is precisely its \(q=1\) state. Thus the transition accepts exactly the assignments having the declared invariant. Colors and status bits are determined uniquely by any given assignment; disjoint child choices therefore never count an assignment twice. Conversely, every assignment satisfying the invariant satisfies one of the displayed transitions. At the root there is no external witness, so requiring \(h=0\) is necessary and sufficient. Component multiplication is valid because witnesses never cross components. This proves the coefficient identity for every finite forest and every nonnegative cardinality.

**State and time bounds.** Since only whether \(w=0\), \(w=1\), or \(w\ge2\) matters, cap \(w\) at two in each running child aggregate. Only the Boolean facts \(r>0\) and \(s>0\) matter; hence at most \(3\cdot2\cdot2=12\) aggregate states. Every child is merged into a constant number of states, with at most eight boundary polynomials at each vertex. All degrees are at most \(n\), so direct convolution yields an \(O(n^3)\) bound in integer-arithmetic operations over all \(O(n)\) edges, and polynomial bit complexity because no coefficient exceeds \(2^n\).

## Verification

The accompanying `verify_forest.py` implements the recurrence with exact integer coefficient dictionaries. Its **separate** brute-force routine iterates all vertex subsets and applies the super-domination definition without using the recurrence. Running `python3 verify_forest.py` produced the exact output in `verification_output.txt`.

Tests include every Prüfer-coded labeled tree through six vertices (\(1442\) tree instances and \(87230\) candidate subsets), \(400\) reproducibly seeded random forests through sixteen vertices (\(3363980\) candidate subsets cumulative), comparison of the minimum degree against an separately implemented greedy forest matching algorithm, \(160\) relabeling/root-order comparisons for paths, and \(44\) path-order boundary checks. All asserted comparisons passed. These finite experiments are not the proof of the theorem; the induction above establishes the unrestricted result.

For orientation, the path on five vertices has polynomial \(6x^3+5x^4+x^5\), while the path on six vertices has polynomial \(2x^3+11x^4+6x^5+x^6\). The empty forest has polynomial \(1\), and a single isolated vertex has polynomial \(x\).

## Relationship to prior work

Ghanbari, Jäger and Lehtilä [1, Section 7(d)] explicitly posed counting minimum super-dominating sets of trees, after counting minima for certain special graph families. Bujtás, Ghanbari and Klavžar [2, Theorem 3.1] determine the **minimum cardinality** on trees using maximum matchings and show that a minimum set can be found in linear time; their theorem does not provide the cardinality distribution. Kaidash [3] introduced the general super-domination polynomial and described formulas for certain graph families; only the abstract and bibliographic record were accessible for comparison, so any all-forest result within that chapter is an unresolved overlap risk.

General logical counting metatheorems for bounded-treewidth graphs [4] already imply **polynomial-time computability in principle** for counting MSO-definable vertex subsets, including super-dominating sets of trees. Polynomial-time existence is therefore **not** asserted to be novel. The specific contribution here is the explicit small-state recurrence for the full cardinality distribution, including concrete local witness states and edgewise transitions, with an implementable verifier. No proof is asserted that eight states are minimal or that this is the first possible counting algorithm.

## Limitations

The recurrence covers forests, not arbitrary graphs with cycles. It counts super-dominating sets rather than distinct choices of witnesses. The \(O(n^3)\) bound counts arithmetic operations, not constant-cost machine-word operations on arbitrarily large integers. The generic counting metatheorem already gives abstract tractability. The 2024 chapter [3] could not be fully inspected; equivalence under another finite-state or logical formulation cannot be ruled out. 

## References

[1] N. Ghanbari, G. Jäger, T. Lehtilä, *Super Domination: Graph Classes, Products and Enumeration*, arXiv:2209.01795 (first public version 2022-09-05), particularly Sections 6–7. https://arxiv.org/pdf/2209.01795

[2] C. Bujtás, N. Ghanbari, S. Klavžar, *Computational complexity aspects of super domination*, arXiv:2302.08862 (2023), particularly Theorem 3.1. https://arxiv.org/pdf/2302.08862

[3] P. A. Kaidash, *Super Domination Polynomial of a Graph*, Mathematical Optimization Theory and Operations Research: Recent Trends, CCIS 2239 (2024), 85–95, DOI:10.1007/978-3-031-73365-9_6. Abstract record: https://sciact.math.nsc.ru/public/article/5672/en

[4] B. Courcelle, J. A. Makowsky, U. Rotics, *On the fixed parameter complexity of graph enumeration problems definable in monadic second-order logic*, Discrete Applied Mathematics 108 (2001), 23–52, DOI:10.1016/S0166-218X(00)00221-3.
