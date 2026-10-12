# The parity-classified optimal codes of the mixed pentagon-cycle channel

## Finding

For every integer \(n\ge 6\), let \(G_n=C_5\boxtimes C_n\) be the strong product of the two ordinary cycle graphs. Its vertices are the labeled ordered pairs \((a,j)\in\mathbb Z/5\mathbb Z\times\mathbb Z/n\mathbb Z\). Two distinct vertices are adjacent precisely when their coordinate differences lie in \(\{0,1,-1\}\) in both cyclic groups. An error-free code is an independent set of this confusability graph.

**Theorem.** Every maximum code has \(n\) words, and every maximum code belongs to exactly one of the following two families.

* **Walk family.** Exactly one word occurs in each second-coordinate column. The unique first-coordinate symbols \(a_j\) obey \(a_{j+1}-a_j\equiv 2\) or \(-2\pmod 5\) at each of the \(n\) cyclic transitions, including the transition from \(n-1\) to \(0\).
* **Alternating-pair family.** This family exists only when \(n\) is even. One of the two parity classes of second-coordinate columns is empty. Every other column contains an arbitrary nonadjacent pair of vertices of \(C_5\), independently chosen from the five such pairs.

Consequently the number \(T_n\) of distinct maximum code *sets* on the fixed labeled alphabet (with no quotient by automorphisms) is exactly
\[
T_n=5\sum_{\substack{0\le k\le n\\2k\equiv n\ (\mathrm{mod}\ 5)}}\binom nk+\mathbf 1_{2\mid n}\,2\cdot5^{n/2}.
\]
The first term is the number of length-\(n\) closed walks on a five-cycle. In particular, for \(n=6,7,8,9,10,11,12\), the respective numbers are \(350,70,1600,360,7520,1650,35990\).

If \(\phi=(1+\sqrt5)/2\), the number of walk-family codes is
\[
W_n=2^n+2\left(\frac{\sqrt5-1}{2}\right)^n+2\left(-\frac{\sqrt5+1}{2}\right)^n.
\]
Thus \(T_{2m}=2\cdot5^m+4^m+O(\phi^{2m})\), whereas \(T_{2m+1}=2\cdot4^m+O(\phi^{2m+1})\), as \(m\to\infty\). Optimal-code diversity has different exponential bases on the two parities.

## Assumptions and scope

Here \(C_r\) means the undirected simple cycle on \(r\) labeled vertices, and \(\boxtimes\) is the strong graph product (not the Cartesian or categorical product). The theorem covers every integer \(n\ge6\), including both odd and even lengths; no asymptotic or prime-power restriction is imposed. Each independent set is counted once as an unordered subset of \(\mathbb Z/5\mathbb Z\times\mathbb Z/n\mathbb Z\); cyclic shifts, reflections, and coordinate relabelings are *not* factored out. The operational interpretation is one use of a five-symbol pentagon-confusability channel followed by one use of an \(n\)-symbol cycle-confusability channel. This is a heterogeneous two-use channel, not a claim about homogeneous repeated uses of one fixed channel.

## Proof

For a code \(I\subseteq V(G_n)\), define the column sections \(S_j=\{a:(a,j)\in I\}\) for \(j\in\mathbb Z/n\mathbb Z\). Every \(S_j\) is independent in \(C_5\), so \(\lvert S_j\rvert\in\{0,1,2\}\). If \(\lvert S_j\rvert=2\), then \(S_j=\{a,a+2\}\) for a unique \(a\in\mathbb Z/5\mathbb Z\). The union of the closed cycle neighborhoods of \(a\) and \(a+2\) is the entire five-symbol alphabet:
\[
\{a-1,a,a+1\}\cup\{a+1,a+2,a+3\}=\mathbb Z/5\mathbb Z.
\]
Consequently both adjacent sections \(S_{j-1}\) and \(S_{j+1}\) must be empty.

Let \(D=\{j:\lvert S_j\rvert=2\}\) and \(E=\{j:\lvert S_j\rvert=0\}\). The preceding observation gives \(D+1\subseteq E\), and hence \(\lvert D\rvert\le\lvert E\rvert\). Therefore
\[
\lvert I\rvert=\sum_j\lvert S_j\rvert=n+\lvert D\rvert-\lvert E\rvert\le n.
\]
The upper bound is attained for all even \(n\) by taking \(S_{2j}=\{0\}\) and \(S_{2j+1}=\{2\}\). For every odd \(n\ge7\), a closed walk of length \(n\) on the complement five-cycle exists: take one traversal of its five edges and insert any number \((n-5)/2\) of immediate two-step backtracks. One chosen vertex in each column of such a walk is independent in the strong product. Thus the maximum size is exactly \(n\).

Now let \(\lvert I\rvert=n\). Equality forces \(\lvert D\rvert=\lvert E\rvert\), so the injections implied by \(D+1\subseteq E\) and \(D-1\subseteq E\) give
\[
E=D+1=D-1,\qquad D+2=D.
\]
If \(D\) is empty, \(E\) is empty as well: every column is a singleton. For neighboring columns, their two first-coordinate symbols must be distinct and nonadjacent in \(C_5\), giving precisely the walk family. Conversely, every such cyclic walk gives an independent set of cardinality \(n\).

Suppose \(D\ne\varnothing\). Invariance under addition by two means \(D\) contains a complete orbit of the step-two translation in \(\mathbb Z/n\mathbb Z\). If \(n\) is odd, that orbit is the entire group, contradicting \(D\cap(D+1)=\varnothing\). If \(n\) is even, each step-two orbit is a parity class. Since the two parity classes are adjacent, \(D\) cannot contain both, and hence \(D\) is exactly one parity class while \(E\) is the other. Every occupied section is an arbitrary independent two-set of \(C_5\). Sections in different occupied columns are separated by two steps in \(C_n\), so their choices are unconstrained. This proves the alternating-pair family and its converse. The two families are disjoint because their section cardinalities differ.

A walk-family code is uniquely determined by the initial symbol \(a_0\) (five choices) and its \(n\) step signs. If \(k\) signs are positive, the total increment is \(2k-2(n-k)=2(2k-n)\) modulo five; its vanishing is equivalent to \(2k\equiv n\pmod5\). Thus there are \(5\sum_{2k\equiv n\ (\mathrm{mod}\ 5)}\binom nk\) walk-family codes. When \(n\) is even, there are exactly two parity choices and five independent pair choices in each of \(n/2\) occupied columns, producing \(2\cdot5^{n/2}\) more codes. This gives the exact census.

Finally, the complement of \(C_5\) is isomorphic to \(C_5\), whose adjacency spectrum is \(\{2, (\sqrt5-1)/2,(\sqrt5-1)/2,-\phi,-\phi\}\). Taking the trace of its \(n\)-th adjacency-matrix power gives the stated expression for \(W_n\). Since \(\phi<2<\sqrt5\), the parity-dependent asymptotics follow.

## Verification

The included reproducible standard-library Python checker can be run with `python3 artifacts/verify.py` from the directory containing this file. It counts independent sets of the required size using a cyclic-column transfer matrix for every \(4\le n\le22\). It independently enumerates all legal column choices without transfer aggregation for \(4\le n\le8\), checking the exact number of maximum sets and the maximum size. It compares both finite methods with the closed binomial formula, prints the individual counts, and finishes with `VERIFY_OK`. The code uses eleven possible independent-section masks and performs exact integer arithmetic. An independent `python3 artifacts/check_graph.py` enumerates maximal cliques directly in the complement of the full \(5n\)-vertex confusability graph, recovering the maximum \(n\) and exact optimal-code counts for \(6\le n\le9\). The finite tests are corroboration, not an induction or a substitute for the all-length proof above.

## Relationship to prior work

Shannon introduced zero-error channel capacity and the graph-product formulation in 1956. Hales (1973), Sonnemann and Krafft (1974), Vesel (1998), and later authors established independence-number results for strong products of odd cycles. Their known numerical optimum for \(C_5\boxtimes C_n\) is \(n\) for odd \(n\ge5\); it does not itself determine the *number and shape* of maximum independent sets. The present finding is the all-optima equality classification and exact labeled census across even and odd \(n\ge6\), including the parity-dependent growth of the family of solutions. The full primary texts inspected for nearby work on generalized cycles and triple cycle products emphasize independence-number constructions, bounds, and capacities rather than this classification. The length-five symmetric case is not part of the new theorem's claimed scope.

## Limitations

This result is not a new bound on Shannon capacity and does not describe graph products of two arbitrary odd cycles. The proof relies essentially on the special fact that the closed neighborhoods of the two vertices in an independent pair of \(C_5\) cover all five vertices; its direct extension to \(C_7\) does not follow. The finite verifier establishes only its explicitly enumerated ranges, and no machine-assisted assertion is needed for the infinite theorem. The 1973 Hales, 1974 Sonnemann–Krafft, and 1998 Vesel papers were identifiable but their complete texts were not accessible in the literature inspection; possible uncatalogued earlier equality classifications remain a bibliographic risk.

## References

1. C. E. Shannon, “The zero error capacity of a noisy channel,” *IRE Transactions on Information Theory* **2** (1956), 8–19.
2. R. S. Hales, “Numerical invariants and the strong product of graphs,” *Journal of Combinatorial Theory B* **15** (1973), 146–155. DOI: `10.1016/0095-8956(73)90014-2`.
3. E. Sonnemann and O. Krafft, “Independence numbers of product graphs,” *Journal of Combinatorial Theory B* **17** (1974), 133–142. DOI: `10.1016/0095-8956(74)90081-1`.
4. A. Vesel, “The independence number of the strong product of cycles,” *Computers & Mathematics with Applications* **36** (1998), 9–21, DOI: `10.1016/S0898-1221(98)00169-2`.
5. S. Badalyan and S. Markosyan, “Numerical Invariants for the Strong Product of Generalized Cycles,” *CSIT Proceedings* (2009), `https://csit.am/2009/proceedings/2DMCA/2.pdf`.
6. D. Korže and A. Vesel, “A Note on the Independence Number of Strong Products of Odd Cycles,” *Ars Combinatoria* **106** (2012), 473–481, publicly dated 2012-07-31, `https://combinatorialpress.com/article/ars/Volume%20106/volume-106-paper-41.pdf`.
7. K. A. Mathew and P. R. J. Östergård, “New Lower Bounds for the Shannon Capacity of Odd Cycles,” arXiv:1504.01472v1 (2015-04-07), `https://arxiv.org/abs/1504.01472`.
