# A uniform forest-pattern expectation identity fails at four letters

## Finding
Let \(\tau_n\) be uniformly selected among permutations of length \(n\ge 2\) whose inversion graph is a tree. For a pattern \(\sigma\), let \(\operatorname{occ}_{\sigma}(\tau_n)\) be the number of increasing-index subsequences order-isomorphic to \(\sigma\). Define \(\Delta_n=\mathbb E[\operatorname{occ}_{1243}(\tau_n)]-\mathbb E[\operatorname{occ}_{1324}(\tau_n)]\). Then
\[
\sum_{n\ge 2}2^{n-2}\Delta_n z^n=\frac{2z^5}{(1-z)^2(1-2z)^3}.
\]
Equivalently, for all integers \(n\ge2\),
\[
\Delta_n=\frac{n^2-11n+34}{2}-\frac{n+2}{2^{n-3}}.
\]
Consequently, \(\Delta_n=0\) for \(2\le n\le4\), \(\Delta_n>0\) for every \(n\ge5\), and \(\Delta_n\sim n^2/2\). The two forest patterns each have length four and exactly three direct-sum indecomposable blocks: \(1243=1\oplus1\oplus21\), \(1324=1\oplus21\oplus1\). Thus equality of exact expectations at common length and common block count does not generally extend from tree patterns to forest patterns, resolving the equality part of the question in Problem 7 of Janson (2022/2023) negatively.

## Assumptions and scope
A permutation's inversion graph has a vertex for each position and an undirected edge between positions \(i<j\) exactly when the earlier value exceeds the later value. A tree permutation has a connected acyclic inversion graph; a forest permutation has an acyclic inversion graph. The term “block” here means a direct-sum indecomposable component of a pattern, not a run in its binary code. The theorem concerns a **uniform random tree permutation as host**, not a uniform random forest permutation. Only the two named patterns, every finite length \(n\ge2\), and their mean difference are claimed. No pointwise inequality for individual hosts is claimed.

## Proof
**Binary code and marked-subsequence transfer.** The binary-code bijection for tree permutations (Acan–Hitczenko; Janson, Section 4, Lemma 11) associates every length-\(n\ge2\) tree permutation with exactly one word \(LwR\), where \(w\in\{L,R\}^{n-2}\). Thus there are \(2^{n-2}\) hosts. For code positions \(i<j\), the inversion-edge condition in Janson's Lemma 11(e1)–(e3) is equivalent to: the symbol at \(i\) is \(L\), that at \(j\) is \(R\), and the intervening symbols form either \(L^*\), \(R^*\), or \(R^+L^+\). Indeed, these alternatives say respectively that the chosen \(R\) is the first \(R\) after the chosen \(L\), that the chosen \(L\) is the last \(L\) before the chosen \(R\), or that they are the cross-block pair in Lemma 11(e3).

Count occurrences of any length-four pattern \(p=(p_1,p_2,p_3,p_4)\) by marking four increasing code positions, and requiring their six inversion edges to agree with comparisons \(p_i>p_j\). An unmarked or marked code letter extends the same finite-state scanner. For each already marked position retain a gap state in \(\{0,1,2,3,4,5\}\), with meanings: 0, marked symbol \(R\); 1, marked symbol \(L\) with empty gap; 2, gap \(L^+\); 3, gap \(R^+\); 4, gap \(R^+L^+\); 5, invalid mixed gap. Upon reading a letter \(L\) or \(R\), update these states by the explicit transition map implemented in `verify.py`. When marking a new position, check that all its inversion comparisons against earlier marked positions match the pattern; reject that transition if not. The new mark stores state 1 for \(L\), state 0 for \(R\). States are ordered tuples of at most four entries.

For \(p=1243\), this deterministic counting construction has 71 reachable states from the mandatory initial \(L\); for \(p=1324\), it has 45 reachable states. Each arbitrary internal letter creates weighted transitions corresponding to whether it is marked. The mandatory last letter is \(R\), and accepting transitions finish with exactly four marks. Let \(T_p\) denote the finite integer transition matrix, \(u_p\) the initial weight vector, and \(v_p\) the final acceptance vector. The total count generating function is therefore
\[
G_p(z)=\sum_{n\ge2}\Bigl(\sum_{\tau\ \mathrm{tree},\,|\tau|=n}\operatorname{occ}_p(\tau)\Bigr)z^n
=z^2u_p^\top(I-zT_p)^{-1}v_p.
\]
The denominator of \(G_p\) divides \(\det(I-zT_p)\), of degree at most 71 or 45 respectively, and its numerator has degree at most 72 or 46, respectively. Consequently \(G_{1243}-G_{1324}\) has a common-denominator representation whose numerator has degree at most \(117\). Let \(Q(z)=(1-z)^2(1-2z)^3=1-8z+25z^2-38z^3+28z^4-8z^5\). The numerator, after multiplying the desired identity \(Q(z)(G_{1243}-G_{1324})-2z^5=0\) by the product of the two determinant denominators, has degree at most \(122\). As both determinants have constant term one, it suffices to verify that the first 123 Taylor coefficients (degrees zero through 122) of this expression vanish.

**Finite exact certificate.** The standalone `verify.py` builds both complete reachable automata by breadth-first search, then performs integer dynamic programming for every length from 2 through 122. It checks the 123 exact coefficient identities
\[
\sum_{j=0}^{\min(5,n)}q_j\bigl([z^{n-j}]G_{1243}-[z^{n-j}]G_{1324}\bigr)=2\,\mathbf1\{n=5\}
\qquad(0\le n\le122),
\]
where \((q_0,\ldots,q_5)=(1,-8,25,-38,28,-8)\). The finite denominator-degree argument converts these exact checks into an identity of rational formal power series for **every** \(n\), not merely through 122. Partial-fraction decomposition yields the stated closed form for \(\Delta_n\). Finally, the rational generating function has strictly positive coefficients for every degree \(n\ge5\): it equals \(2z^5\) times products of geometric and negative-binomial generating functions with strictly positive coefficients. The leading asymptotic term follows from the triple pole at \(z=1/2\).

## Verification
Execute `python3 verify.py` using Python's standard library. The program verifies the two state counts (71, 45), the 123 coefficient identities, explicit sums for lengths 5–9, independent direct enumeration of marked choices on all \(LwR\) codewords through length 9, and an unrelated enumeration through length 7 over **all** ordinary permutations, retaining those with a connected inversion graph of \(n-1\) edges. The latter also verifies the \(2^{n-2}\) tree count. Example total occurrence differences for lengths 5–9 are \(2,16,78,300,1002\), respectively. Integer arithmetic throughout. The algebraic degree bound, not limited experiments or a guessed recurrence, is the step extending the identity to all lengths.

## Relationship to prior work
Janson, *The number of occurrences of patterns in a random tree or forest permutation*, arXiv:2203.04182v1, Problem 7 (journal pp. 4–5), proves finite-\(n\) equality for two **tree** patterns of equal length and explicitly asks whether it extends to **forest** patterns with equal length and block count. The present two forest patterns are a direct negative instance, together with a complete all-size expectation-difference identity. Janson's Section 4 supplies the binary-code inverse-edge description (Lemma 11) used in the proof. Acan and Hitczenko's earlier work introduces the coding and counts all tree permutations. These earlier results provide necessary machinery but do not state the particular difference law in the inspected material. Exact priority beyond these sources is not independently certified.

## Limitations
This is an identity for one pair of patterns, not a classification of all forest-pattern equivalence classes or a theorem for arbitrary patterns. The code proof is finite-state and exact but is not a mechanically formalized theorem prover certificate; its state model and denominator bound are explicitly specified for human reconstruction. The occurrence law in a uniform forest **host**, joint distributions, or pathwise domination are not addressed. Any stronger previously published formula subsuming the result would affect originality. Independent validation has not been carried out.

## References
1. Svante Janson, *The number of occurrences of patterns in a random tree or forest permutation*, arXiv:2203.04182v1 (first public 2022-03-08), *Electronic Journal of Combinatorics* 30 (2023), P2.27, DOI: 10.37236/11111; Problem 7 and Lemma 11.
2. Hüseyin Acan and Paweł Hitczenko, *On random trees obtained from permutation graphs*, arXiv:1406.3958v1 (2014); Section 2, binary insertion representation and tree count.
