# Fourteen rank-four theories of finite strict-betweenness chains

## Finding
For each integer \(n\ge1\), define the finite ternary structure \(\mathcal B_n\) on \(\{1,\ldots,n\}\) by
\[
B(a,b,c)\quad\Longleftrightarrow\quad (a<b<c)\ \text{or}\ (c<b<a).
\]
The language contains **only** equality and the strict ternary betweenness relation \(B\). Let \(\equiv_4\) denote agreement on all first-order sentences of quantifier rank at most four. Then, for all positive integers \(m,n\),
\[
\mathcal B_n\equiv_4\mathcal B_m
\quad\Longleftrightarrow\quad
\min(n,14)=\min(m,14).
\]
Consequently the entire family of nonempty finite strict-betweenness chains has exactly fourteen rank-four theories. Every class has a representative with at most fourteen elements, and the largest class has no representative with fewer than fourteen. By comparison, the corresponding pure finite strict *linear orders* have fifteen rank-four theories and require a fifteen-element representative for their largest class.

## Assumptions and scope
The betweenness relation is strict: when two arguments coincide, \(B\) is false. No underlying linear order, endpoint constant, adjacency/successor relation, or orientation predicate is available in the signature. The domain is finite and nonempty. Quantifier rank counts nested quantifiers, not the total number of quantifiers. Atomic formulas include equality and ternary applications of \(B\). The theorem concerns rank exactly bounded above by four, not all finite quantifier ranks simultaneously.

## Proof
**1. The finite type recursion is exact.** For any \(n\ge1\), any ordered tuple \(\bar a=(a_1,\dots,a_k)\) of elements of \(\mathcal B_n\) (repetitions allowed), and any nonnegative integer \(r\), let \(T_0(n,\bar a)\) be the complete equality/betweenness atomic diagram on the listed variables. Thus it records all truth values of \(a_i=a_j\) and \(B(a_i,a_j,a_h)\); formulas with repeated variable *indices* in \(B\) are uniformly false and need not be enumerated. Define recursively
\[
T_{r+1}(n,\bar a)
=\bigl(T_0(n,\bar a),\ \{T_r(n,\bar a,b):1\le b\le n\}\bigr).
\]
The braces denote a *set*, not a multiset: ordinary first-order logic at bounded quantifier rank has no counting quantifiers. Induction on \(r\), using Boolean connectives and one existential or universal quantifier, establishes that two tuples of the same length have the same \(T_r\) exactly when they satisfy all corresponding first-order formulas of rank at most \(r\). In particular, \(\mathcal B_n\equiv_4\mathcal B_m\) exactly when \(T_4(n,())=T_4(m,())\).

**2. Exhaustive finite boundary.** The standalone program `verify_bet4.py` evaluates the preceding *definition* using exact integer comparisons, immutable sets and canonical structural interning. It enumerates **every** possible assignment at each of the four nested extensions on all domains of size one through fifteen. Its output `verify_bet4.out` records that
\[
T_4(1,()),\ T_4(2,()),\ldots,\ T_4(14,())
\]
are pairwise distinct, while \(T_4(14,())=T_4(15,())\). Thus there are fourteen different classes among sizes at most fifteen, with the fourteenth and fifteenth sizes equivalent. No sampling, randomized hashing, or cutoff extrapolation is used here: the interning dictionary compares full finite immutable symbolic keys.

**3. All larger sizes.** A standard interval-splitting Ehrenfeucht--Fraïssé argument shows that, for every \(r\ge0\), any two pure finite strict linear orders of sizes at least \(2^r-1\) are rank-\(r\) equivalent. Here is the needed inductive reasoning. In a game with \(r+1\) moves, each order has at least \(2(2^r-1)+1\) points. After the first choice, Duplicator chooses a response so that each pair of corresponding left and right remaining intervals is either exactly the same size below \(2^r-1\), or both of size at least \(2^r-1\). The two intervals can then be played independently using the inductive \(r\)-move strategies. The zero-move base is immediate. For \(r=4\), all pure chains with at least fifteen points are therefore equivalent.

The ternary relation \(B(a,b,c)\) is defined in a pure strict linear order by the *quantifier-free* formula \((a<b<c)\lor(c<b<a)\). Passing to this reduct cannot distinguish structures at any fixed rank when their pure orders are equivalent at that rank. Hence \(\mathcal B_n\equiv_4\mathcal B_m\) whenever \(n,m\ge15\). Step 2 supplies the additional boundary identification \(\mathcal B_{14}\equiv_4\mathcal B_{15}\), so transitivity includes all \(n,m\ge14\). Conversely step 2 distinguishes each size from one through thirteen from every other class, including size fourteen. This completes the exact classification and proves that fourteen is the smallest uniform representative-size bound.

## Verification
Run `python3 verify_bet4.py` using ordinary Python 3; no third-party packages or network are needed. The program prints all classes on domains from one through fifteen, verifies the rank-three pointed-character equality for the fourteen/fifteen boundary, and ends in `VERIFY_OK`. It also checks the lower-rank cutoffs on the same tested domains as independent consistency checks; these auxiliary outputs are not extrapolated to larger domains. The file `verify_bet4.out` is the recorded output. Full equality/betweenness diagrams, including repetitions and all strict ternary orientations, are represented in the computation. All domain sizes at least fifteen are handled by the separate symbolic interval lemma in the proof.

## Relationship to prior work
The Ehrenfeucht--Fraïssé theorem and classical interval strategies appear in standard finite-model-theory sources, including Libkin's *Elements of Finite Model Theory* and Immerman's *Descriptive Complexity*. Siders (2010) studies the more expressive **linear-order** language, not the ternary orientation-free reduct. Courcelle (2020) defines precisely this strict betweenness relation and studies axiomatizations in broader tree classes; the examined sections establish its object and relation to reversal, not the fourteen-class rank-four threshold. A published exact classification of **one-red coloured linear orders** (published-finding corpus ID `2026/10/4/SCOPE-exact-quantifier-rank-profiles-for-finite-one-red-linear-orders--eec9053b6af5`) concerns orders with an explicit orientation and unary marker; its rank-\(q\) formulas do not directly state this orientation-free sentence classification. A separate classification of directed successor paths (published-finding corpus ID `2026/10/4/SCOPE-exact-quantifier-rank-threshold-for-finite-directed-paths--75a6b05e7112`) uses a binary successor relation and different structures. The conclusion here is not the known rank-four cutoff fifteen for pure orders: the strict-betweenness reduct identifies the additional fourteen/fifteen boundary by an exact four-round test.

## Limitations
This is a complete theorem at rank four **only**. The numerical pattern observed in lower ranks is not claimed as an all-rank theorem. The result does not classify arbitrary ternary betweenness structures, partially ordered sets, cyclic orders, metric-betweenness graphs, or formulas with counting quantifiers. The finite certificate is reproducible but has not undergone independent external mathematical audit. Indexed and accessible literature searches do not establish exhaustive novelty; a 2009 thesis and inaccessible full texts remain possible overlap sources.

## References
1. L. Libkin, *Elements of Finite Model Theory*, Springer, first hardcover publication 2 July 2004, ISBN 978-3-540-21202-7, DOI 10.1007/978-3-662-07003-1.
2. N. Immerman, *Descriptive Complexity*, Springer, 1999, Chapter 6, “Ehrenfeucht–Fraïssé Games”; authorized chapter text: https://people.cs.umass.edu/~immerman/book/ch6.pdf.
3. R. Siders, “On quantifier-rank equivalence between linear orders,” *Information and Computation* 208 (2010), 417–432, DOI 10.1016/j.ic.2009.11.006. Only public abstract and bibliographic material were accessible in this review.
4. B. Courcelle, “Axiomatizations of betweenness in order-theoretic trees,” *Logical Methods in Computer Science* 17 (2021), arXiv:2004.10127 (first posted April 2020). Full open HTML text examined.
5. Published published-finding corpus works on one-red linear orders and directed successor paths, identifiers given in the preceding section; the complete `RESULT.md` contents of both were read for the comparison.
