# Prime-power graph criterion and exact two-exponent covers of symmetric-group orders through degree 40

## Finding
For every integer \(k\ge2\), let \(\mathcal O_k\) denote the set of positive orders of elements of \(S_k\). A *two-exponent order cover* is a pair of positive integers \((d,e)\) such that every \(q\in\mathcal O_k\) divides \(d\) or \(e\). Define its optimal largest exponent as
\[
B_2(k)=\min_{d,e\ge1}\{\max(d,e):\forall q\in\mathcal O_k,\;q\mid d\ \text{or}\ q\mid e\}.
\]
Write \(P_k=\{p^a\le k:p\ \text{prime},\ a\ge1\}\). Form a graph \(G_k\) on \(P_k\), with an edge between \(p^a\) and \(q^b\) if their prime bases differ and \(p^a+q^b\le k\).

**Theorem.** A pair \((d,e)\) is a two-exponent order cover of \(S_k\) **if and only if** (i) every vertex \(v\in P_k\) divides at least one of \(d,e\), and (ii) for each edge \(\{v,w\}\in G_k\), both endpoints divide \(d\), or both divide \(e\). This is an exact local-to-global test: no orders involving three or more prime bases need separate checking.

Put \(E_k=\operatorname{lcm}(1,2,\ldots,k)\). The optimum satisfies
\[
B_2(k)=\min_{d\mid E_k}\max\bigl(d,\operatorname{lcm}\{q\in\mathcal O_k:q\nmid d\}\bigr),
\]
where the lcm of an empty set is one. The associated finite exhaustive calculation gives \(B_2(k)\) for **every \(3\le k\le40\)**. In particular
\[
B_2(40)=53{,}542{,}288{,}800,
\]
with an optimal pair \((35{,}959{,}964{,}040,53{,}542{,}288{,}800)\). The complete initial table, including a witness at each degree, is generated and recorded in `verification_output.txt`.

## Assumptions and scope
The symmetric group acts on \(k\) symbols. Element order means the least common multiple of the cycle lengths of a permutation, including the identity (order one). A prime-power support uses **only the largest power of each prime** appearing in an element order. Integers in a cover are not required to be orders of actual permutations. Optimality concerns the largest of *two covering exponents*, not number of integers in unrestricted covers, smallest positive identity, or smallest permutation automaton.

## Proof
**1. Realizable support sets.** Let an order \(q\in\mathcal O_k\) have maximal prime-power factorization \(q=\prod_{v\in T}v\), with different prime bases. For every cycle, choose the prime powers from \(T\) whose largest appearances are witnessed in that cycle. The product of these chosen powers divides that cycle length. For pairwise coprime prime powers greater than one, their product is at least their sum (by induction, using \(ab\ge a+b\) for distinct integers \(a,b\ge2\) that are coprime). Therefore the sum of all \(v\in T\) does not exceed the total of the cycle lengths, namely \(k\). Conversely, any set \(T\) of distinct-prime powers with \(\sum_{v\in T}v\le k\) occurs as the maximal-prime-power support of a permutation: use disjoint cycles of those lengths and fill remaining symbols by fixed points.

**2. Necessity of the graph criterion.** Every vertex power \(v\le k\) occurs as a cycle order, so some exponent must be divisible by \(v\). If \(\{v,w\}\) is an edge, disjoint cycles of lengths \(v\) and \(w\) exist in \(S_k\); their element order is \(vw\), because the prime bases differ. Thus one of \(d,e\) must be divisible by both endpoints.

**3. Sufficiency of the graph criterion.** Fix any permutation order \(q\) and its support \(T\). Step 1 gives \(\sum T\le k\), so every two distinct vertices of \(T\) have different prime bases and form an edge of \(G_k\). Associate to each \(v\in T\) the nonempty subset \(I_v\subseteq\{1,2\}\) containing index one when \(v\mid d\) and index two when \(v\mid e\). By the edge condition, \(I_v\cap I_w\ne\varnothing\) for each pair. A family of nonempty subsets of a two-element set with pairwise nonempty intersections has nonempty total intersection: otherwise it contains both the singleton \(\{1\}\) and the singleton \(\{2\}\). Hence every support power divides the *same* one of \(d,e\). Their coprime product \(q\) does too, proving sufficiency. For three or more covering integers, the analogous pairwise principle fails in general, e.g. \(\{1,2\},\{1,3\},\{2,3\}\).

**4. Exact finite optimization.** Every permutation order divides \(E_k\). Replacing an admissible \(d,e\) by \(\gcd(d,E_k),\gcd(e,E_k)\) preserves which permutation orders divide each exponent, and cannot raise the maximum. Therefore some optimum has \(d,e\mid E_k\). For fixed \(d\mid E_k\), the least positive eligible second exponent is
\[
R_k(d)=\operatorname{lcm}\{q\in\mathcal O_k:q\nmid d\},
\]
with empty lcm one. It divides every eligible second exponent and itself covers exactly the missing orders. Minimizing \(\max(d,R_k(d))\) over all divisors gives the formula. Equivalently, the first three steps compute \(R_k(d)\) by taking the lcm of all uncovered singleton vertices and the endpoints of graph edges not both dividing \(d\). This equality is checked independently for *each* examined divisor below.

**5. Certified finite segment.** The complete element-order set is generated inductively, without listing permutations:
\[
\mathcal O_0=\{1\},\qquad
\mathcal O_k=\{\operatorname{lcm}(j,t):1\le j\le k,\ t\in\mathcal O_{k-j}\}.
\]
The recurrence partitions an arbitrary permutation by the cycle containing a fixed symbol, and is exhaustive in both directions. The accompanying program iterates through *all* divisors of \(E_k\) for each integer \(3\le k\le40\), computes the residual second exponent independently from the complete order set and from the graph, confirms they coincide, and minimizes the resulting objective exactly. At \(k=40\) it processes 495 distinct element orders, 19 prime-power vertices, 105 edges, and all 36,864 divisors. It proves the displayed exact optimum and the entire recorded initial table; no extrapolation is used.

## Verification
Run `python3 verify.py` with Python 3; it uses the standard library only. The shipped `verification_output.txt` gives all 38 optimal values and witness pairs, and records the complete order/graph residual crosschecks. The proof of the universal graph criterion is deductive; the code certifies only the declared finite degree range.

## Relationship to prior work
Xu and Regan, *An Improved Lower Bound for Separating Words by Permutation Automata* (arXiv:2610.11098v1, first submitted 2026-10-08), introduce finite covers of symmetric-group element orders (Definition 3.2) and use them to construct positive binary identities (Lemmas 3.4–3.6). Section 4 chooses asymptotically efficient many-element covers through prime-power segmentation. The present theorem specializes to exactly two covering integers and replaces order-by-order coverage with a sharp vertex-and-edge graph test; its exhaustive optimal largest-exponent values are a different finite optimization problem. Bulatov–Karpova–Shur–Startsev (arXiv:1609.03199v1) examine shorter identities and word separation without reporting this two-exponent graph criterion or its exact table. Karpova–Shur's later work studies positive identities, including numerical-2 constructions, and remains a plausible source of equivalent constructions or overlooked coverage details.

The two-exponent optimum controls the best upper *bound* obtainable for the maximum exponent in the two-integer special case of the cover-based word construction of Xu and Regan: their Lemma 3.6 gives a word-length upper bound of \(6B_2(k)\). This does **not** assert that the resulting words have shortest possible length, that two-exponent covers optimize all covers, or that the observed finite values improve asymptotics.

## Limitations
Numerical optimality is proved only for \(3\le k\le40\), while the local-to-global graph theorem and divisor reduction apply to all \(k\ge2\). Full historical priority cannot be established by negative search results. The exhaustive code is a finite certificate for the computed range, not an infinite proof. These findings have not been independently audited.

## References
1. Chen Xu and Kenneth W. Regan, *An Improved Lower Bound for Separating Words by Permutation Automata*, arXiv:2610.11098v1, 2026-10-08. https://arxiv.org/html/2610.11098v1
2. Andrei Bulatov, Olga Karpova, Arseny Shur, Konstantin Startsev, *Lower Bounds on Words Separation: Are There Short Identities in Transformation Semigroups?*, arXiv:1609.03199v1, 2016. https://arxiv.org/html/1609.03199v1
3. Olga Karpova and Arseny Shur, *Words Separation and Positive Identities in Symmetric Groups*, Algorithmica 83 (2021), 1734–1766. DOI: 10.1007/s00453-020-00777-z. (Bibliographic/abstract comparison; complete article not inspected.)
